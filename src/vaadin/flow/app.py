"""FlowApp — single entry point to configure and run a PyFlow application."""

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
            self._run_dev(debug)
        else:
            _serve(self._views, self._host, self._port, debug)

    def _run_dev(self, debug: bool):
        """Dev mode: parent owns the socket, children are restarted on changes.

        The listening socket is created once in this parent process and
        inherited by each child via pass_fds.  When a child is killed for
        reload, the socket stays open — no EADDRINUSE race.
        """
        import signal
        import socket
        import subprocess
        import watchfiles
        from pathlib import Path

        watch_dir = Path(".").resolve()
        print(f"  Dev mode: watching {watch_dir} for Python file changes", flush=True)

        # Create listening socket in the parent — survives child restarts
        srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            srv_sock.bind((self._host, self._port))
        except OSError as e:
            if e.errno == 48:
                print(f"\n  ERROR: Port {self._port} is already in use.")
                print(f"  Kill the other process:  lsof -ti :{self._port} | xargs kill -9\n")
                return
            raise
        srv_sock.listen(128)
        srv_sock.set_inheritable(True)
        fd = srv_sock.fileno()
        print(f"  Listening on http://{self._host}:{self._port}", flush=True)

        env = os.environ.copy()
        env["_PYFLOW_APP"] = json.dumps({
            "views": self._views,
            "host": self._host,
            "port": self._port,
            "debug": debug,
            "socket_fd": fd,
        })

        def start_child():
            return subprocess.Popen(
                [sys.executable, "-c",
                 "from vaadin.flow.app import _dev_serve; _dev_serve()"],
                pass_fds=(fd,),
                env=env,
            )

        def stop_child(proc):
            if proc.poll() is None:
                proc.send_signal(signal.SIGINT)
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait(timeout=1)

        # Track mtimes to ignore metadata-only events (macOS FSEvents
        # fires for extended attribute changes like "last opened date")
        file_mtimes: dict[str, float] = {}

        proc = start_child()
        try:
            for changes in watchfiles.watch(
                ".",
                watch_filter=watchfiles.PythonFilter(),
                debounce=1600,
            ):
                actually_changed = []
                for _, p in changes:
                    try:
                        mtime = os.path.getmtime(p)
                    except OSError:
                        mtime = 0
                    if file_mtimes.get(p) != mtime:
                        file_mtimes[p] = mtime
                        actually_changed.append(os.path.relpath(p, watch_dir))
                if not actually_changed:
                    continue
                paths = sorted(actually_changed)
                print(f"  Reloading because files modified: {', '.join(paths)}", flush=True)
                stop_child(proc)
                proc = start_child()
        except KeyboardInterrupt:
            pass
        finally:
            stop_child(proc)
            srv_sock.close()


def _usage() -> None:
    print("Usage: vaadin <app_module> [--dev] [--debug] [--port PORT] [--host HOST]")
    print("       vaadin [app_module] --bundle [--keep] [--vaadin-version VERSION]")
    print()
    print("  app_module  Python module with views (e.g. demo)")
    print("  --dev       Auto-reload on source changes")
    print("  --debug     Verbose UIDL protocol logging")
    print("  --port N    Server port (default: 8080)")
    print("  --host H    Server host (default: localhost)")
    print("  --bundle    Generate frontend bundle from component registry")
    print("  --keep      Keep build/bundle-project/ after extraction")
    sys.exit(0)


def main():
    """CLI entry point: ``vaadin <app_module> [--dev] [--debug]``."""
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        _usage()

    # Parse all arguments: find module name (first non-flag) and flags
    args = sys.argv[1:]
    views = None
    rest: list[str] = []
    for arg in args:
        if views is None and not arg.startswith("-"):
            views = arg
        else:
            rest.append(arg)

    if "--bundle" in rest:
        from pathlib import Path
        from vaadin.flow.bundle_generator import generate_and_build

        keep = "--keep" in rest
        vaadin_version = "25.0.4"
        if "--vaadin-version" in rest:
            idx = rest.index("--vaadin-version")
            vaadin_version = rest[idx + 1]

        # Resolve app_dir from module name if given
        app_dir = None
        if views:
            # "demo" → "demo/", "my_app" → "my_app/"
            app_dir = Path.cwd() / views.replace(".", os.sep).replace("-", "_")

        cwd = os.getcwd()
        if cwd not in sys.path:
            sys.path.insert(0, cwd)

        generate_and_build(app_dir=app_dir, keep=keep, vaadin_version=vaadin_version)
        sys.exit(0)

    if views is None:
        _usage()

    if "." not in views:
        views = f"{views}.views"

    cwd = os.getcwd()
    if cwd not in sys.path:
        sys.path.insert(0, cwd)

    port = 8080
    host = "localhost"
    if "--port" in rest:
        idx = rest.index("--port")
        port = int(rest[idx + 1])
        rest = rest[:idx] + rest[idx + 2:]
    if "--host" in rest:
        idx = rest.index("--host")
        host = rest[idx + 1]
        rest = rest[:idx] + rest[idx + 2:]

    debug = "--debug" in rest
    dev = "--dev" in rest

    if dev:
        # Reuse FlowApp dev mode
        app = FlowApp.__new__(FlowApp)
        app._views = views
        app._port = port
        app._host = host
        app._run_dev(debug)
    else:
        _serve(views, host, port, debug)


def _dev_serve():
    """Entry point for dev-mode child process (reads config from env)."""
    cwd = os.getcwd()
    if cwd not in sys.path:
        sys.path.insert(0, cwd)
    try:
        cfg = json.loads(os.environ["_PYFLOW_APP"])
        _serve(cfg["views"], cfg["host"], cfg["port"], cfg["debug"],
               socket_fd=cfg.get("socket_fd"))
    except KeyboardInterrupt:
        pass


def _serve(views: str, host: str, port: int, debug: bool, socket_fd: int | None = None):
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

    if socket_fd is not None:
        import socket
        sock = socket.socket(fileno=socket_fd)
        run_server(debug=debug, sock=sock)
    else:
        run_server(host=host, port=port, debug=debug)
