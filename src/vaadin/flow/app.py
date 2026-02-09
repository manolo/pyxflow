"""FlowApp — single entry point to configure and run a PyFlow application."""

import asyncio
import inspect
import json
import os
import sys


class FlowApp:
    """Configure and run a PyFlow application.

    Usage::

        # demo/__main__.py
        from vaadin.flow import FlowApp

        FlowApp(port=8088).run()

    CLI flags:
        --dev     Auto-reload on source changes (requires watchfiles)
        --debug   Verbose UIDL protocol logging
    """

    def __init__(self, *, port: int = 8080, host: str = "localhost"):
        # Auto-detect caller's package → views module
        frame = inspect.stack()[1]
        module_name = frame.frame.f_globals.get("__name__", "")
        if module_name == "__main__":
            # python -m <package> → resolve from __spec__ or file path
            spec = frame.frame.f_globals.get("__spec__")
            if spec and spec.parent:
                package = spec.parent
            else:
                # Fallback: derive from file path (e.g. demo/__main__.py → demo)
                from pathlib import Path
                caller_path = Path(frame.filename).resolve()
                package = caller_path.parent.name
        elif "." in module_name:
            package = module_name.rsplit(".", 1)[0]
        else:
            package = module_name
        self._views = f"{package}.views"
        self._port = port
        self._host = host

    def run(self):
        """Parse CLI flags and start the server."""
        args = set(sys.argv[1:])
        dev = "--dev" in args
        debug = "--debug" in args

        if dev:
            os.environ["_PYFLOW_APP"] = json.dumps({
                "views": self._views,
                "port": self._port,
                "host": self._host,
                "debug": debug,
            })
            import watchfiles
            watchfiles.run_process(
                ".",
                target="vaadin.flow.app._dev_serve",
                watch_filter=watchfiles.PythonFilter(),
            )
        else:
            _serve(self._views, self._host, self._port, debug)


def _dev_serve():
    """Entry point for watchfiles child process (reads config from env)."""
    cfg = json.loads(os.environ["_PYFLOW_APP"])
    _serve(cfg["views"], cfg["host"], cfg["port"], cfg["debug"])


def _serve(views: str, host: str, port: int, debug: bool):
    import importlib
    from pathlib import Path
    from vaadin.flow.router import discover_views
    from vaadin.flow.server.http_server import run_server, set_app_directory

    discover_views(views)

    # Resolve app package directory (e.g. "demo.views" → demo/)
    package = views.rsplit(".", 1)[0]
    pkg_mod = importlib.import_module(package)
    if pkg_mod.__file__:
        set_app_directory(Path(pkg_mod.__file__).parent)

    try:
        asyncio.run(run_server(host=host, port=port, debug=debug))
    except KeyboardInterrupt:
        pass
