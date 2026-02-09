"""HTTP Server for Vaadin Flow."""

import json
import logging
import secrets
import uuid
from pathlib import Path
from typing import Any, Callable

from aiohttp import web

from vaadin.flow.server.uidl_handler import UidlHandler
from vaadin.flow.core.state_tree import StateTree

log = logging.getLogger("vaadin.flow")

# Session storage (in-memory for now)
_sessions: dict[str, dict[str, Any]] = {}

# Upload handler registry: resource_id → (session_id, handler_callable)
_upload_handlers: dict[str, tuple[str, Callable]] = {}

# App package directory (e.g. demo/) — set by FlowApp
_app_directory: Path | None = None

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
    """Get existing session or create new one."""
    session_id = request.cookies.get("JSESSIONID")

    if session_id and session_id in _sessions:
        return session_id, _sessions[session_id]

    # Create new session
    session_id = str(uuid.uuid4())
    tree = StateTree()
    handler = UidlHandler(tree)

    # Use the handler's CSRF token for the session
    session = {
        "csrf_token": handler._csrf_token,
        "tree": tree,
        "handler": handler,
        "initialized": False,
    }
    _sessions[session_id] = session
    return session_id, session


async def handle_root(request: web.Request) -> web.Response:
    """Handle GET / - serve index.html."""
    # Check if this is an init request
    if request.query.get("v-r") == "init":
        return await handle_init(request)

    # Serve index.html from bundle
    html = get_index_html()
    return web.Response(text=html, content_type="text/html")


async def handle_init(request: web.Request) -> web.Response:
    """Handle GET /?v-r=init - return appConfig."""
    session_id, session = get_or_create_session(request)

    # Parse browser details (optional)
    browser_details = {}
    if "v-browserDetails" in request.query:
        try:
            browser_details = json.loads(request.query["v-browserDetails"])
        except json.JSONDecodeError:
            pass

    # Get init response from handler
    # Pass the request path so the handler knows the initial route
    handler: UidlHandler = session["handler"]
    initial_route = request.path.strip("/")  # "/about" -> "about", "/" -> ""
    response_data = handler.handle_init(browser_details, initial_route=initial_route)

    session["initialized"] = True

    # Set session cookie
    response = web.json_response(response_data)
    response.set_cookie("JSESSIONID", session_id, httponly=True)
    return response


async def handle_uidl(request: web.Request) -> web.Response:
    """Handle POST /?v-r=uidl - process UIDL request."""
    session_id = request.cookies.get("JSESSIONID")

    if not session_id or session_id not in _sessions:
        return web.json_response(
            {"error": "Invalid session"},
            status=403
        )

    session = _sessions[session_id]

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

    # Process UIDL
    log.debug("RPC: %s", payload.get("rpc", []))
    handler: UidlHandler = session["handler"]
    response_data = handler.handle_uidl(payload)

    # Wrap response with XSS protection prefix
    response_text = f"for(;;);[{json.dumps(response_data)}]"
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

    return web.Response(text="Not found", status=404)


def get_bundle_directory() -> Path | None:
    """Find the bundle directory containing Vaadin frontend assets.

    The bundle contains the FlowClient, web components, and Lumo theme.
    It is generated from a reference Java Vaadin application.

    Search order:
    1. ./bundle/ in the project root (recommended)
    2. ../my-hello/target/... (development fallback)
    """
    # Check common locations (in priority order)
    candidates = [
        # Project-local bundle (recommended)
        Path.cwd() / "bundle",
        # Development: my-hello reference app
        Path(__file__).parents[5] / "my-hello" / "target" / "classes" / "META-INF" / "VAADIN" / "webapp",
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
            # Enable experimental feature flags before bundle loads
            html = html.replace(
                "</head>",
                '  <script>window.Vaadin=window.Vaadin||{};window.Vaadin.featureFlags=window.Vaadin.featureFlags||{};window.Vaadin.featureFlags.masterDetailLayoutComponent=true;</script>\n</head>'
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


def create_app() -> web.Application:
    """Create the aiohttp application."""
    app = web.Application()

    # Routes
    app.router.add_get("/", handle_root)
    app.router.add_post("/", handle_uidl_post)
    app.router.add_post("/VAADIN/dynamic/resource/{ui_id}/{resource_id}/{name}", handle_upload)
    app.router.add_get("/VAADIN/{path:.*}", handle_static)
    app.router.add_get("/lumo/{path:.*}", handle_theme)
    app.router.add_get("/aura/{path:.*}", handle_theme)
    app.router.add_get("/styles/{path:.*}", handle_styles)
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


async def handle_route(request: web.Request) -> web.Response:
    """Handle GET for any route - serve index.html (client handles routing)."""
    # Check if this is an init request
    if request.query.get("v-r") == "init":
        return await handle_init(request)

    # Serve index.html - the client will handle the routing
    html = get_index_html()
    return web.Response(text=html, content_type="text/html")


async def handle_route_post(request: web.Request) -> web.Response:
    """Handle POST for any route."""
    if request.query.get("v-r") == "uidl":
        return await handle_uidl(request)
    return web.Response(text="Bad request", status=400)


async def handle_uidl_post(request: web.Request) -> web.Response:
    """Handle POST / with v-r=uidl query param."""
    if request.query.get("v-r") == "uidl":
        return await handle_uidl(request)
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
    if sock is not None:
        web.run_app(app, sock=sock)
    else:
        web.run_app(app, host=host, port=port, reuse_address=True)


# Default view class (for backwards compatibility)
_view_class = None
