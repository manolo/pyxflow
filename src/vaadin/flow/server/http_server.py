"""HTTP Server for Vaadin Flow."""

import asyncio
import datetime
import json
import logging
import secrets
import time
import uuid
from pathlib import Path
from typing import Any, Callable

import aiohttp
from aiohttp import web

from vaadin.flow.server.uidl_handler import UidlHandler
from vaadin.flow.core.state_tree import StateTree

log = logging.getLogger("vaadin.flow")

SESSION_TIMEOUT = 1800  # 30 minutes (matches Java servlet default)


class _UidlEncoder(json.JSONEncoder):
    """JSON encoder that handles Python types in UIDL responses.

    Must never raise — a serialization error after _build_response() has
    consumed tree changes would leave the client with a blank screen and
    no way to recover (the changes are gone).
    """

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        if isinstance(o, datetime.date):
            return o.isoformat()
        try:
            return super().default(o)
        except TypeError:
            log.warning("Unsupported type %s in UIDL response, converting to str", type(o).__name__)
            return str(o)

def _critical_error_json(
    caption: str | None = None,
    message: str | None = None,
    details: str | None = None,
    url: str | None = None,
) -> str:
    """Build a UIDL response that triggers FlowClient's critical error overlay.

    Matches Java's VaadinService.createCriticalNotificationJSON().
    The client shows a fixed overlay (top-right, z-index 10000) with the error
    info.  Click or ESC redirects to ``url`` or refreshes the page (if url is
    None).  After displaying, UIState is set to TERMINATED.

    If all four fields are None the client refreshes immediately without
    showing any message (Java's default for unhandled internal errors).
    """
    app_error = {
        "caption": caption,
        "message": message,
        "details": details,
        "url": url,
    }
    response = {
        "syncId": -1,
        "changes": [],
        "meta": {"appError": app_error},
    }
    return f"for(;;);[{json.dumps(response)}]"


# Session storage (in-memory for now)
_sessions: dict[str, dict[str, Any]] = {}

# Upload handler registry: resource_id → (session_id, handler_callable)
_upload_handlers: dict[str, tuple[str, Callable]] = {}

# App package directory (e.g. demo/) — set by FlowApp
_app_directory: Path | None = None

# Dev mode flag — enables detailed not-found view with route list
_dev_mode: bool = False

# Views module name (e.g. "demo.views", "tests.views") — set by _serve()
_views_module: str = ""

def set_app_directory(directory: Path):
    """Set the app package directory for serving styles etc."""
    global _app_directory
    _app_directory = directory


def register_upload_handler(session_id: str, handler: Callable) -> str:
    """Register an upload handler and return its resource_id (UUID)."""
    resource_id = str(uuid.uuid4())
    _upload_handlers[resource_id] = (session_id, handler)
    return resource_id


def get_or_create_session(request: web.Request) -> tuple[str, dict[str, Any]]:
    """Get existing session or create new one.

    The session shell contains shared state (csrf_token, last_activity)
    and a ``uis`` dict keyed by ui_id.  Each browser tab gets its own
    UI entry created in ``handle_init()``.
    """
    session_id = request.cookies.get("JSESSIONID")

    if session_id and session_id in _sessions:
        _sessions[session_id]["last_activity"] = time.monotonic()
        return session_id, _sessions[session_id]

    # Create new session shell (no tree/handler yet — created per UI in handle_init)
    session_id = str(uuid.uuid4())
    session = {
        "csrf_token": secrets.token_hex(16),
        "last_activity": time.monotonic(),
        "next_ui_id": 0,
        "uis": {},
    }
    _sessions[session_id] = session
    return session_id, session


async def handle_root(request: web.Request) -> web.Response:
    """Handle GET / - serve index.html."""
    vr = request.query.get("v-r")
    if vr == "init":
        return await handle_init(request)

    # Serve index.html from bundle
    html = get_index_html()
    return web.Response(text=html, content_type="text/html")


async def handle_init(request: web.Request) -> web.Response:
    """Handle GET /?v-r=init - return appConfig.

    Each init call allocates a new UI (tree + handler) within the session,
    allowing multiple browser tabs to coexist independently.
    """
    session_id, session = get_or_create_session(request)

    # Parse browser details (optional)
    browser_details = {}
    if "v-browserDetails" in request.query:
        try:
            browser_details = json.loads(request.query["v-browserDetails"])
        except json.JSONDecodeError:
            pass

    # Allocate a new UI for this tab
    ui_id = session["next_ui_id"]
    session["next_ui_id"] = ui_id + 1

    tree = StateTree()
    handler = UidlHandler(tree, csrf_token=session["csrf_token"])

    session["uis"][ui_id] = {
        "tree": tree,
        "handler": handler,
        "push_ws": None,
        "push_sender_task": None,
        "pending_push": None,
    }

    # Pass the request path so the handler knows the initial route
    initial_route = request.path.strip("/")  # "/about" -> "about", "/" -> ""
    response_data = handler.handle_init(browser_details, initial_route=initial_route, ui_id=ui_id)

    # Set session cookie
    response = web.json_response(response_data)
    response.set_cookie("JSESSIONID", session_id, httponly=True)
    return response


def _session_expired_response() -> web.Response:
    """Return session-expired JSON (HTTP 200) so FlowClient reloads the page."""
    return web.Response(
        text='for(;;);[{"meta":{"sessionExpired":true}}]',
        content_type="application/json"
    )


def _push_session_expired(request: web.Request) -> web.Response:
    """Return the right response for an expired push session.

    Long-polling requests get a sessionExpired JSON so FlowClient reloads.
    WebSocket upgrade requests get a 403 — the WS upgrade fails, Atmosphere
    falls back to long-polling, which then receives sessionExpired.
    """
    if request.headers.get("Upgrade", "").lower() == "websocket":
        return web.Response(status=403)
    return _session_expired_response()


async def handle_uidl(request: web.Request) -> web.Response:
    """Handle POST /?v-r=uidl - process UIDL request."""
    session_id = request.cookies.get("JSESSIONID")

    if not session_id or session_id not in _sessions:
        return _session_expired_response()

    session = _sessions[session_id]

    # Route to the correct UI by v-uiId
    ui_id = int(request.query.get("v-uiId", "0"))
    ui_state = session["uis"].get(ui_id)
    if ui_state is None:
        return _session_expired_response()

    try:
        payload = await request.json()
    except json.JSONDecodeError:
        return web.json_response({"error": "Invalid JSON"}, status=400)

    # Validate CSRF token
    csrf = payload.get("csrfToken")
    if csrf != session["csrf_token"]:
        return web.json_response(
            {"error": "Invalid CSRF token"},
            status=403
        )

    session["last_activity"] = time.monotonic()

    # Process UIDL
    log.debug("RPC: %s", payload.get("rpc", []))
    handler: UidlHandler = ui_state["handler"]
    try:
        response_data = handler.handle_uidl(payload)
        # _UidlEncoder has a str() fallback so json.dumps should never raise.
        # User code errors are already caught in _process_rpc() which shows
        # an error notification before _build_response() consumes tree changes.
        response_text = f"for(;;);[{json.dumps(response_data, cls=_UidlEncoder)}]"
    except Exception:
        # Safety net for truly unexpected errors (serialization bugs, etc.).
        # At this point _build_response() may have already consumed tree changes,
        # so we can't add a Notification (it would be the only content → blank page).
        # Instead, send meta.appError with syncId=-1 — FlowClient shows an error
        # overlay and refreshes on click/ESC.  Matches Java's
        # VaadinService.handleExceptionDuringRequest() behavior.
        log.exception("Unexpected error processing UIDL request")
        response_text = _critical_error_json(
            "Internal error",
            "An internal error has occurred. Click to reload.",
        )

    log.debug("Response: %s...", response_text[:500])
    return web.Response(
        text=response_text,
        content_type="application/json"
    )


async def handle_upload(request: web.Request) -> web.Response:
    """Handle file upload POST.

    vaadin-upload sends the file as raw body (not multipart) with headers:
    - Content-Type: application/octet-stream (or the file's MIME type)
    - X-Filename: URL-encoded filename
    """
    resource_id = request.match_info.get("resource_id", "")
    if resource_id not in _upload_handlers:
        return web.Response(text="Not found", status=404)

    session_id = request.cookies.get("JSESSIONID")
    expected_session_id, handler = _upload_handlers[resource_id]
    if session_id != expected_session_id:
        return web.Response(text="Forbidden", status=403)

    try:
        content_type = request.content_type or "application/octet-stream"

        if content_type.startswith("multipart/"):
            # Multipart form data
            reader = await request.multipart()
            while True:
                part = await reader.next()
                if part is None:
                    break
                if not hasattr(part, 'filename') or not part.filename:  # type: ignore[union-attr]
                    continue
                data = await part.read()  # type: ignore[union-attr]
                mime_type = part.headers.get("Content-Type", "application/octet-stream")
                handler(part.filename, mime_type, data)  # type: ignore[union-attr]
        else:
            # Raw body upload (vaadin-upload default)
            data = await request.read()
            from urllib.parse import unquote
            filename = unquote(request.headers.get("X-Filename", "unknown"))
            mime_type = request.headers.get("Content-Type", "application/octet-stream")
            handler(filename, mime_type, data)
    except Exception as e:
        print(f"[Upload] Error: {e}", flush=True)
        return web.Response(
            text="<html><body>upload failed</body></html>",
            content_type="text/html",
            status=500,
        )

    return web.Response(
        text="<html><body>download handled</body></html>",
        content_type="text/html",
    )


async def handle_push(request: web.Request) -> web.Response:
    """Handle WebSocket push connection (Atmosphere protocol).

    Each browser tab has its own push WebSocket, keyed by v-uiId.
    """
    session_id = request.cookies.get("JSESSIONID")
    session = _sessions.get(session_id) if session_id else None

    if session is None:
        return _push_session_expired(request)

    # Route to the correct UI by v-uiId
    ui_id = int(request.query.get("v-uiId", "0"))
    ui_state = session["uis"].get(ui_id)
    if ui_state is None:
        return _push_session_expired(request)

    handler: UidlHandler = ui_state["handler"]

    # Validate push ID
    push_id = request.query.get("v-pushId", "")
    if push_id != getattr(handler, "_push_id", None):
        return _push_session_expired(request)

    # Cancel existing push sender for this UI if reconnecting
    old_task = ui_state.get("push_sender_task")
    if old_task and not old_task.done():
        old_task.cancel()
        try:
            await old_task
        except asyncio.CancelledError:
            pass

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    # Send Atmosphere protocol handshake with trackMessageLength format:
    # <length>|<UUID>|<heartbeat_interval_ms>|<heartbeat_padding_char>
    atmo_uuid = str(uuid.uuid4())
    handshake_data = f"{atmo_uuid}|30000|X"
    await ws.send_str(f"{len(handshake_data)}|{handshake_data}")

    ui_state["push_ws"] = ws
    session["last_activity"] = time.monotonic()

    # Start push sender task
    sender_task = asyncio.create_task(_push_sender(ws, ui_state))
    ui_state["push_sender_task"] = sender_task

    try:
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                if msg.data == "X":
                    # Atmosphere heartbeat
                    session["last_activity"] = time.monotonic()
                    continue
            elif msg.type in (aiohttp.WSMsgType.ERROR, aiohttp.WSMsgType.CLOSE):
                break
    finally:
        sender_task.cancel()
        try:
            await sender_task
        except asyncio.CancelledError:
            pass
        ui_state["push_ws"] = None
        ui_state["push_sender_task"] = None

    return ws


async def _push_sender(ws: web.WebSocketResponse, ui_state: dict):
    """Coroutine that waits for push signals and sends UIDL over WebSocket."""
    tree: StateTree = ui_state["tree"]
    handler: UidlHandler = ui_state["handler"]

    # Replay any buffered message from a previous failed connection
    pending = ui_state.pop("pending_push", None)
    if pending:
        try:
            await ws.send_str(pending)
        except (ConnectionResetError, ConnectionError):
            ui_state["pending_push"] = pending
            return

    while not ws.closed:
        await tree._push_event.wait()
        tree._push_event.clear()

        if ws.closed:
            break

        # Skip if no actual changes to push.  This check MUST happen before
        # _build_response() because that method increments syncId.  When
        # ui.access() is called during an HTTP request handler, the changes
        # are already consumed by the HTTP response; only notify_push() fires.
        # Without this guard, _build_response() bumps syncId for an empty
        # response, desynchronising client and server → next RPC triggers a
        # full resync and the page goes blank.
        if not tree._changes and not tree._pending_execute:
            continue

        try:
            # Build UIDL response with pending changes
            response_data = handler._build_response()

            # Mark as async push (not a response to an HTTP request).
            # Without this, FlowClient calls endRequest() which throws
            # IllegalStateException when no request is active.
            response_data["meta"] = {"async": True}

            response_json = json.dumps(response_data, cls=_UidlEncoder)
            message = f"for(;;);[{response_json}]"
            # Atmosphere trackMessageLength format: <length>|<message>
            prefixed = f"{len(message)}|{message}"
        except Exception:
            log.exception("Error in push sender")
            break
        try:
            await ws.send_str(prefixed)
        except (ConnectionResetError, ConnectionError):
            ui_state["pending_push"] = prefixed
            break
        except Exception:
            log.exception("Error in push sender")
            break


_BUNDLE_CACHE = "public, max-age=31536000, immutable"


async def handle_static(request: web.Request) -> web.Response:
    """Handle static file requests for /VAADIN/*."""
    path = request.match_info.get("path", "")

    # Try to find the file in the bundle directory
    bundle_dir = get_bundle_directory()
    if bundle_dir:
        file_path = bundle_dir / "VAADIN" / path
        if file_path.is_file():
            content_type = guess_content_type(file_path)
            return web.FileResponse(file_path, headers={"Content-Type": content_type, "Cache-Control": _BUNDLE_CACHE})  # type: ignore[return-value]

    print(f"  [404] /VAADIN/{path}", flush=True)
    return web.Response(text="Not found", status=404)


def get_bundle_directory() -> Path | None:
    """Find the bundle directory containing Vaadin frontend assets.

    The bundle contains the FlowClient, web components, and Lumo theme.
    It is generated from a reference Java Vaadin application.

    Search order:
    1. App-directory bundle (user project: ``my_app/bundle/``)
    2. Package-internal bundle (inside installed package / pyflow source)
    3. ./bundle/ in the project root (development fallback)
    """
    candidates: list[Path] = []
    if _app_directory:
        candidates.append(_app_directory / "bundle")
    candidates += [
        # Package-internal bundle (ships inside the wheel)
        Path(__file__).parents[1] / "bundle",
        # Project-local bundle (development fallback)
        Path.cwd() / "bundle",
    ]

    for candidate in candidates:
        if (candidate / "VAADIN").is_dir():
            return candidate

    return None


def guess_content_type(path: Path) -> str:
    """Guess content type from file extension."""
    suffix = path.suffix.lower()
    types = {
        ".js": "application/javascript",
        ".css": "text/css",
        ".html": "text/html",
        ".json": "application/json",
        ".svg": "image/svg+xml",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
        ".ico": "image/x-icon",
    }
    return types.get(suffix, "application/octet-stream")


def get_index_html() -> str:
    """Get index.html from the bundle directory.

    The bundle's index.html is generated by Vaadin and contains
    the correct bootstrap script references.
    """
    bundle_dir = get_bundle_directory()
    if bundle_dir:
        index_path = bundle_dir / "index.html"
        if index_path.is_file():
            html = index_path.read_text()
            # Add <base href="/"> for client-side routing (React Router checks
            # document.baseURI to intercept link clicks for SPA navigation)
            html = html.replace(
                '<meta charset="UTF-8" />',
                '<meta charset="UTF-8" />\n  <base href="/">'
            )
            # Prevent document-level scrolling — AppLayout handles its own
            # internal scroll.  Without this the browser can scroll the
            # <html> element past the layout, leaving a white gap.
            html = html.replace(
                "margin: 0;",
                "margin: 0;\n      overflow: hidden;"
            )
            # Enable experimental feature flags before bundle loads
            # + CSS for v-system-error overlay (Java's BootstrapHandler injects this;
            # FlowClient creates a div.v-system-error on meta.appError responses)
            html = html.replace(
                "</head>",
                '  <script>window.Vaadin=window.Vaadin||{};window.Vaadin.featureFlags=window.Vaadin.featureFlags||{};window.Vaadin.featureFlags.masterDetailLayoutComponent=true;</script>\n'
                '  <style>.v-system-error{color:indianred;pointer-events:auto;position:absolute;background:#fff;top:1em;right:1em;border:1px solid #000;padding:1em;z-index:10000;max-width:calc(100vw - 4em);max-height:calc(100vh - 4em);overflow:auto}.v-system-error .caption{color:red;font-weight:700}</style>\n'
                '</head>'
            )
            # Apply @ColorScheme from AppShell to <html> tag
            from vaadin.flow.router import get_app_shell
            app_shell = get_app_shell()
            color_scheme = getattr(app_shell, '_color_scheme', None) if app_shell else None
            if color_scheme and color_scheme != "normal":
                theme_attr = color_scheme.replace(' ', '-')
                html = html.replace('<html', f'<html theme="{theme_attr}" style="color-scheme: {color_scheme};"', 1)
            # In dev mode, inject a meta tag identifying the views module
            if _dev_mode and _views_module:
                html = html.replace(
                    '<base href="/">',
                    f'<base href="/">\n  <meta name="pyflow-views" content="{_views_module}">'
                )
            return html

    # Fallback if no bundle found
    return """<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>PyFlow - Bundle Not Found</title>
</head>
<body>
  <h1>Bundle not found</h1>
  <p>Please generate the Vaadin bundle first.</p>
</body>
</html>
"""


def _cleanup_expired_sessions():
    """Remove sessions that have been idle longer than SESSION_TIMEOUT."""
    now = time.monotonic()
    expired = [
        sid for sid, session in _sessions.items()
        if now - session.get("last_activity", 0) > SESSION_TIMEOUT
    ]
    if not expired:
        return
    for sid in expired:
        del _sessions[sid]
    # Clean upload handlers belonging to expired sessions
    expired_set = set(expired)
    stale_uploads = [
        rid for rid, (sid, _) in _upload_handlers.items()
        if sid in expired_set
    ]
    for rid in stale_uploads:
        del _upload_handlers[rid]
    log.info("Cleaned up %d expired session(s)", len(expired))


async def _session_cleanup_ctx(app: web.Application):
    """Background task that periodically cleans expired sessions."""
    async def _run():
        while True:
            await asyncio.sleep(60)
            _cleanup_expired_sessions()

    task = asyncio.create_task(_run())
    yield
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass


async def _close_push_connections(app: web.Application):
    """Close all active WebSocket push connections on shutdown.

    Without this, push handlers block on ``async for msg in ws:`` and
    push senders block on ``await _push_event.wait()``, causing Ctrl+C
    to hang until the connections time out.
    """
    for session in _sessions.values():
        for ui_state in session.get("uis", {}).values():
            ws = ui_state.get("push_ws")
            if ws and not ws.closed:
                await ws.close()


def create_app() -> web.Application:
    """Create the aiohttp application."""
    app = web.Application()
    app.cleanup_ctx.append(_session_cleanup_ctx)
    app.on_shutdown.append(_close_push_connections)

    # Routes
    app.router.add_get("/", handle_root)
    app.router.add_post("/", handle_uidl_post)
    app.router.add_post("/VAADIN/dynamic/resource/{ui_id}/{resource_id}/{name}", handle_upload)
    app.router.add_get("/VAADIN/push", handle_push)
    app.router.add_get("/VAADIN/{path:.*}", handle_static)
    app.router.add_get("/lumo/{path:.*}", handle_theme)
    app.router.add_get("/aura/{path:.*}", handle_theme)
    app.router.add_get("/styles/{path:.*}", handle_styles)
    app.router.add_get("/static/{path:.*}", handle_app_static)
    # Catch-all for other routes (e.g., /about) - serve index.html
    app.router.add_get("/{path:.*}", handle_route)
    app.router.add_post("/{path:.*}", handle_route_post)

    return app


async def handle_theme(request: web.Request) -> web.Response:
    """Handle static file requests for /lumo/* and /aura/*."""
    theme = request.path.split("/")[1]  # "lumo" or "aura"
    path = request.match_info.get("path", "")
    bundle_dir = get_bundle_directory()
    if bundle_dir:
        file_path = bundle_dir / theme / path
        if file_path.is_file():
            content_type = guess_content_type(file_path)
            return web.FileResponse(file_path, headers={"Content-Type": content_type, "Cache-Control": _BUNDLE_CACHE})  # type: ignore[return-value]
    return web.Response(text="Not found", status=404)


async def handle_styles(request: web.Request) -> web.Response:
    """Handle static file requests for /styles/*.

    Serves CSS files from the app package's styles/ directory
    (e.g. demo/styles/ when running ``python -m demo``).
    """
    if _app_directory is None:
        return web.Response(text="Not found", status=404)
    path = request.match_info.get("path", "")
    file_path = _app_directory / "styles" / path
    # Security: ensure resolved path stays within styles directory
    styles_dir = (_app_directory / "styles").resolve()
    resolved = file_path.resolve()
    if not str(resolved).startswith(str(styles_dir)):
        return web.Response(text="Forbidden", status=403)
    if resolved.is_file() and resolved.suffix == ".css":
        return web.FileResponse(resolved, headers={"Content-Type": "text/css", "Cache-Control": "no-cache"})  # type: ignore[return-value]
    return web.Response(text="Not found", status=404)


async def handle_app_static(request: web.Request) -> web.Response:
    """Handle static file requests for /static/*.

    Serves files from the app package's static/ directory
    (e.g. demo/static/ when running ``python -m demo``).
    """
    if _app_directory is None:
        return web.Response(text="Not found", status=404)
    path = request.match_info.get("path", "")
    file_path = _app_directory / "static" / path
    static_dir = (_app_directory / "static").resolve()
    resolved = file_path.resolve()
    if not str(resolved).startswith(str(static_dir)):
        return web.Response(text="Forbidden", status=403)
    if resolved.is_file():
        content_type = guess_content_type(resolved)
        return web.FileResponse(resolved, headers={"Content-Type": content_type, "Cache-Control": "no-cache"})  # type: ignore[return-value]
    return web.Response(text="Not found", status=404)


async def handle_route(request: web.Request) -> web.Response:
    """Handle GET for any route - serve index.html (client handles routing)."""
    # Check if this is an init request
    if request.query.get("v-r") == "init":
        return await handle_init(request)

    # Serve index.html - the client will handle the routing
    html = get_index_html()
    return web.Response(text=html, content_type="text/html")


async def handle_heartbeat(request: web.Request) -> web.Response:
    """Handle POST /?v-r=heartbeat - keep session alive."""
    session_id = request.cookies.get("JSESSIONID")
    if not session_id or session_id not in _sessions:
        return web.Response(status=403)
    _sessions[session_id]["last_activity"] = time.monotonic()
    return web.Response(status=200)


async def handle_route_post(request: web.Request) -> web.Response:
    """Handle POST for any route."""
    vr = request.query.get("v-r")
    if vr == "uidl":
        return await handle_uidl(request)
    if vr == "heartbeat":
        return await handle_heartbeat(request)
    return web.Response(text="Bad request", status=400)


async def handle_uidl_post(request: web.Request) -> web.Response:
    """Handle POST / with v-r=uidl query param."""
    vr = request.query.get("v-r")
    if vr == "uidl":
        return await handle_uidl(request)
    if vr == "heartbeat":
        return await handle_heartbeat(request)
    return web.Response(text="Bad request", status=400)


def run_server(host: str = "localhost", port: int = 8080, debug: bool = False, sock=None):
    """Run the Vaadin Flow server.

    Uses web.run_app() for proper signal handling and graceful shutdown.
    In dev mode, ``sock`` is a pre-bound listening socket owned by the
    parent process (avoids EADDRINUSE on reload).
    """
    if debug:
        logging.basicConfig(level=logging.DEBUG, format="%(name)s  %(message)s")
        log.setLevel(logging.DEBUG)

    # Show registered routes
    from vaadin.flow.router import get_all_routes
    routes = get_all_routes()
    if routes:
        print("Registered routes:")
        for path, cls in routes.items():
            print(f"  /{path} -> {cls.__name__}")

    app = create_app()
    # shutdown_timeout=0 avoids waiting for open WebSocket push connections
    # to close gracefully (the default 60s causes Ctrl+C to hang).
    if sock is not None:
        web.run_app(app, sock=sock, shutdown_timeout=0)
    else:
        web.run_app(app, host=host, port=port, reuse_address=True, shutdown_timeout=0)


# Default view class (for backwards compatibility)
_view_class = None
