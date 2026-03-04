"""Server startup: production and dev-mode runners."""

import json
import os
import sys


def _ensure_importable(views: str) -> None:
    """Make sure the views module is importable from the current directory."""
    cwd = os.getcwd()
    package = views.rsplit(".", 1)[0]
    package_dir = os.path.join(cwd, package.replace(".", os.sep))
    if os.path.isdir(package_dir):
        # Package is a subdirectory of cwd (e.g. myapp/views/)
        if cwd not in sys.path:
            sys.path.insert(0, cwd)
    elif os.path.isdir(os.path.join(cwd, "views")):
        # Package is cwd itself (views/ at root, from --setup without name).
        # Directory may have hyphens (app-1) while module uses underscores (app_1).
        # Inject cwd as a synthetic package so `import app_1.views` works.
        import types
        pkg_mod = types.ModuleType(package)
        pkg_mod.__path__ = [cwd]
        pkg_mod.__package__ = package
        sys.modules[package] = pkg_mod
        # Also add cwd to sys.path so sibling packages (e.g. lib/) are importable.
        if cwd not in sys.path:
            sys.path.insert(0, cwd)
    else:
        if cwd not in sys.path:
            sys.path.insert(0, cwd)


def _dev_serve():
    """Entry point for dev-mode child process (reads config from env)."""
    try:
        cfg = json.loads(os.environ["_PYFLOW_APP"])
        _ensure_importable(cfg["views"])
        _serve(cfg["views"], cfg["host"], cfg["port"], cfg["debug"],
               dev=True, socket_fd=cfg.get("socket_fd"))
    except KeyboardInterrupt:
        pass


def _serve(views: str, host: str, port: int, debug: bool, *, dev: bool = False, socket_fd: int | None = None):
    import importlib
    from pathlib import Path
    from pyxflow.router import discover_views
    from pyxflow.server.http_server import run_server, set_app_directory
    import pyxflow.server.http_server as _http

    _http._dev_mode = dev
    _http._views_module = views
    discover_views(views)

    # Resolve app package directory (e.g. "demo.views" -> demo/)
    package = views.rsplit(".", 1)[0]
    pkg_mod = importlib.import_module(package)
    if getattr(pkg_mod, "__file__", None):
        set_app_directory(Path(pkg_mod.__file__).parent)
    elif hasattr(pkg_mod, "__path__"):
        # Namespace or synthetic package -- use __path__
        set_app_directory(Path(list(pkg_mod.__path__)[0]))

    if socket_fd is not None:
        import socket
        sock = socket.socket(fileno=socket_fd)
        run_server(debug=debug, sock=sock)
    else:
        run_server(host=host, port=port, debug=debug)
