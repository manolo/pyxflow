"""HTTP Server for Vaadin Flow."""

import json
import secrets
import uuid
from pathlib import Path
from typing import Any

from aiohttp import web

from vaadin.flow.server.uidl_handler import UidlHandler
from vaadin.flow.core.state_tree import StateTree


# Session storage (in-memory for now)
_sessions: dict[str, dict[str, Any]] = {}


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

    # Serve index.html
    html = generate_index_html()
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
    print(f"[UIDL] Received request", flush=True)
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
    print(f"[UIDL] RPC: {payload.get('rpc', [])}", flush=True)
    handler: UidlHandler = session["handler"]
    response_data = handler.handle_uidl(payload)

    # Wrap response with XSS protection prefix
    response_text = f"for(;;);[{json.dumps(response_data)}]"
    print(f"[UIDL] Response: {response_text[:500]}...", flush=True)
    return web.Response(
        text=response_text,
        content_type="application/json"
    )


async def handle_static(request: web.Request) -> web.Response:
    """Handle static file requests for /VAADIN/*."""
    path = request.match_info.get("path", "")

    # Try to find the file in the bundle directory
    bundle_dir = get_bundle_directory()
    if bundle_dir:
        file_path = bundle_dir / "VAADIN" / path
        if file_path.is_file():
            content_type = guess_content_type(file_path)
            return web.FileResponse(file_path, headers={"Content-Type": content_type})

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


def generate_index_html() -> str:
    """Generate the index.html page matching Vaadin's format."""
    # Find the actual indexhtml JS file
    bundle_dir = get_bundle_directory()
    js_file = "indexhtml.js"  # fallback
    css_file = "indexhtml.css"  # fallback
    if bundle_dir:
        build_dir = bundle_dir / "VAADIN" / "build"
        if build_dir.exists():
            for f in build_dir.iterdir():
                if f.name.startswith("indexhtml-") and f.name.endswith(".js") and not f.name.endswith(".br"):
                    js_file = f.name
                elif f.name.startswith("indexhtml-") and f.name.endswith(".css") and not f.name.endswith(".br"):
                    css_file = f.name

    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <style>
    html, body, #outlet {{
      height: 100%;
      width: 100%;
      margin: 0;
    }}
  </style>
  <script type="module" crossorigin src="./VAADIN/build/{js_file}"></script>
  <link rel="modulepreload" crossorigin href="./VAADIN/build/commonjsHelpers-CqkleIqs.js">
  <link rel="stylesheet" crossorigin href="./VAADIN/build/{css_file}">
</head>
<body>
  <div id="outlet"></div>
</body>
</html>
"""


def create_app() -> web.Application:
    """Create the aiohttp application."""
    app = web.Application()

    # Routes
    app.router.add_get("/", handle_root)
    app.router.add_post("/", handle_uidl_post)
    app.router.add_get("/VAADIN/{path:.*}", handle_static)
    # Catch-all for other routes (e.g., /about) - serve index.html
    app.router.add_get("/{path:.*}", handle_route)
    app.router.add_post("/{path:.*}", handle_route_post)

    return app


async def handle_route(request: web.Request) -> web.Response:
    """Handle GET for any route - serve index.html (client handles routing)."""
    # Check if this is an init request
    if request.query.get("v-r") == "init":
        return await handle_init(request)

    # Serve index.html - the client will handle the routing
    html = generate_index_html()
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


async def run_server(view_class=None, host: str = "localhost", port: int = 8080):
    """Run the Vaadin Flow server.

    Args:
        view_class: (Deprecated) Use @Route decorator instead.
                    If provided, registers as fallback for "/" route.
        host: The host to bind to.
        port: The port to listen on.
    """
    # Store view class for backwards compatibility
    if view_class:
        global _view_class
        _view_class = view_class

    # Show registered routes
    from vaadin.flow.router import get_all_routes
    routes = get_all_routes()
    if routes:
        print("Registered routes:")
        for path, cls in routes.items():
            print(f"  /{path} -> {cls.__name__}")
    elif view_class:
        print(f"Using view: {view_class.__name__} (consider using @Route decorator)")

    app = create_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()
    print(f"Server running at http://{host}:{port}")

    # Keep running
    import asyncio
    while True:
        await asyncio.sleep(3600)


# Default view class (for backwards compatibility)
_view_class = None
