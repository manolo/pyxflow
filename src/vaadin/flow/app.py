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
            _serve(self._views, self._host, self._port, debug, dev=False)

    def _run_dev(self, debug: bool):
        """Dev mode: parent owns the socket, children are restarted on changes.

        The listening socket is created once in this parent process and
        inherited by each child via pass_fds.  When a child is killed for
        reload, the socket stays open — no EADDRINUSE race.
        """
        import socket
        import subprocess
        import watchfiles
        from pathlib import Path

        watch_dir = Path(".").resolve()
        print(f"  Dev mode: watching {watch_dir} for Python file changes", flush=True)

        # Check if something is already listening on the port
        probe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            probe.connect((self._host, self._port))
            probe.close()
            print(f"\n  ERROR: Port {self._port} is already in use.")
            print(f"  Kill the other process:  lsof -ti :{self._port} | xargs kill -9\n")
            return
        except ConnectionRefusedError:
            pass  # Nothing listening — good
        finally:
            probe.close()

        # Create listening socket in the parent — survives child restarts
        srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv_sock.bind((self._host, self._port))
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
                proc.kill()
                proc.wait(timeout=2)

        # Track mtimes to ignore metadata-only events (macOS FSEvents
        # fires for extended attribute changes like "last opened date")
        file_mtimes: dict[str, float] = {}

        proc = start_child()
        try:
            for changes in watchfiles.watch(
                ".",
                watch_filter=watchfiles.PythonFilter(),
                debounce=800,
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


def _auto_detect_app() -> str | None:
    """Try to find an app module in cwd by looking for <pkg>/views/ or ./views/."""
    from pathlib import Path
    # Check subdirectories first (e.g. myapp/views/)
    for entry in sorted(Path.cwd().iterdir()):
        if entry.is_dir() and (entry / "views").is_dir():
            return entry.name
    # Check cwd itself (e.g. views/ at root, from --setup without name)
    if (Path.cwd() / "views").is_dir():
        return Path.cwd().name.replace("-", "_")
    return None


def _usage() -> None:
    print("Usage: vaadin [app_module] [--dev] [--debug] [--port PORT] [--host HOST]")
    print("       vaadin [app_module] bundle [--keep] [--vaadin-version VERSION]")
    print("       vaadin --vscode")
    print("       vaadin --setup [app_name]")
    print()
    print("  app_module  Python module with views (auto-detected if omitted)")
    print("  --dev       Auto-reload on source changes")
    print("  --debug     Verbose UIDL protocol logging")
    print("  --port N    Server port (default: 8080)")
    print("  --host H    Server host (default: localhost)")
    print("  bundle      Generate frontend bundle from component registry")
    print("  --keep      Keep build/bundle-project/ after extraction")
    print("  --vscode    Generate .vscode/ config and install recommended extensions")
    print("  --setup     Scaffold a new Vaadin PyFlow project (views, static, __main__.py)")
    sys.exit(0)


def _scaffold_dir():
    """Return the scaffold resource directory."""
    import importlib.resources
    return importlib.resources.files("vaadin.flow") / "scaffold"


def _setup_project(app_name: str | None = None) -> None:
    """Scaffold a new Vaadin PyFlow project structure."""
    import shutil
    from pathlib import Path

    root = Path.cwd()
    if app_name is not None:
        # Explicit name: create as subdirectory
        pkg = root / app_name
    else:
        # No name: scaffold in cwd, derive name from directory
        app_name = root.name.replace("-", "_")
        pkg = root
    scaffold = _scaffold_dir() / "project"

    # --- Package directories ---
    views_dir = pkg / "views"
    static_styles = pkg / "static" / "styles"
    static_images = pkg / "static" / "images"

    for d in (views_dir, static_styles, static_images):
        d.mkdir(parents=True, exist_ok=True)

    def _write(path: Path, content: str) -> None:
        action = "Updated" if path.exists() else "Created"
        path.write_text(content)
        print(f"  {action} {path.relative_to(root)}")

    def _write_template(src_name: str, dest: Path) -> None:
        """Read a .tmpl file from scaffold, replace {{app_name}}, write to dest."""
        if dest.exists():
            return
        text = (scaffold / src_name).read_text()
        if pkg == root:
            # cwd mode: "from views.main_layout" not "from pepe.views.main_layout"
            text = text.replace("{{app_name}}.", "")
        text = text.replace("{{app_name}}", app_name)
        _write(dest, text)

    # --- __init__.py ---
    for init in (pkg / "__init__.py", views_dir / "__init__.py"):
        if not init.exists():
            _write(init, "")

    # --- Templated files ---
    _write_template("__main__.py.tmpl", pkg / "__main__.py")
    _write_template("views/main_layout.py.tmpl", views_dir / "main_layout.py")
    _write_template("views/hello_world.py.tmpl", views_dir / "hello_world.py")

    # --- Static files (copy as-is) ---
    css_dest = static_styles / "styles.css"
    if not css_dest.exists():
        text = (scaffold / "static" / "styles" / "styles.css").read_text()
        _write(css_dest, text)

    # --- favicon.ico (binary copy) ---
    favicon_dest = pkg / "static" / "favicon.ico"
    if not favicon_dest.exists():
        try:
            import importlib.resources
            favicon_src = _scaffold_dir() / "favicon.ico"
            with importlib.resources.as_file(favicon_src) as src:
                shutil.copy2(src, favicon_dest)
            print(f"  Created {favicon_dest.relative_to(root)}")
        except (FileNotFoundError, TypeError):
            print("  Warning: favicon.ico not found in package scaffold")

    print(f"\n  Project '{app_name}' scaffolded!")
    if pkg == root:
        print(f"  Run:  cd .. && python -m {app_name}")
    else:
        print(f"  Run:  python -m {app_name}")


def _setup_vscode() -> None:
    """Generate .vscode/ config for Vaadin PyFlow development."""
    import shutil
    import subprocess
    from pathlib import Path

    scaffold = _scaffold_dir() / "vscode"
    vscode_dir = Path.cwd() / ".vscode"
    vscode_dir.mkdir(exist_ok=True)

    def _rel(path: Path) -> str:
        return str(path.relative_to(Path.cwd()))

    # --- settings.json (merge, don't overwrite) ---
    settings_path = vscode_dir / "settings.json"
    defaults = json.loads((scaffold / "settings.json").read_text())
    if settings_path.exists():
        existing = json.loads(settings_path.read_text())
        for key, val in defaults.items():
            if key not in existing:
                existing[key] = val
        settings_path.write_text(json.dumps(existing, indent=4) + "\n")
        print(f"  Updated {_rel(settings_path)}")
    else:
        settings_path.write_text(json.dumps(defaults, indent=4) + "\n")
        print(f"  Created {_rel(settings_path)}")

    # --- extensions.json (merge recommendations) ---
    extensions_path = vscode_dir / "extensions.json"
    ext_defaults = json.loads((scaffold / "extensions.json").read_text())
    recommended = ext_defaults["recommendations"]
    if extensions_path.exists():
        ext_data = json.loads(extensions_path.read_text())
        existing_recs = ext_data.get("recommendations", [])
        for ext_id in recommended:
            if ext_id not in existing_recs:
                existing_recs.append(ext_id)
        ext_data["recommendations"] = existing_recs
        extensions_path.write_text(json.dumps(ext_data, indent=4) + "\n")
        print(f"  Updated {_rel(extensions_path)}")
    else:
        extensions_path.write_text(json.dumps(ext_defaults, indent=4) + "\n")
        print(f"  Created {_rel(extensions_path)}")

    # --- python.code-snippets ---
    snippets_path = vscode_dir / "python.code-snippets"
    snippets_path.write_text((scaffold / "python.code-snippets").read_text())
    print(f"  Created {_rel(snippets_path)}")

    # --- templates/vaadin_view.py ---
    templates_dir = vscode_dir / "templates"
    templates_dir.mkdir(exist_ok=True)
    template_dest = templates_dir / "vaadin_view.py"
    template_dest.write_text((scaffold / "templates" / "vaadin_view.py").read_text())
    print(f"  Created {_rel(template_dest)}")

    # --- Install extensions ---
    code_cmd = shutil.which("code")
    if code_cmd:
        for ext_id in recommended:
            try:
                subprocess.run(
                    [code_cmd, "--install-extension", ext_id],
                    capture_output=True, timeout=30,
                )
                print(f"  Installed extension {ext_id}")
            except (subprocess.TimeoutExpired, OSError):
                print(f"  Warning: failed to install {ext_id}")
    else:
        print("  Warning: 'code' CLI not found -- install extensions manually in VSCode")

    print("\n  VSCode configuration ready!")


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
    else:
        if cwd not in sys.path:
            sys.path.insert(0, cwd)


def main():
    """CLI entry point: ``vaadin [app_module] [--dev] [--debug]``."""
    if len(sys.argv) >= 2 and sys.argv[1] in ("-h", "--help"):
        _usage()

    # Parse all arguments: find module name (first non-flag) and flags.
    # "bundle" is a subcommand alias for "--bundle"
    _SUBCOMMANDS = {"bundle": "--bundle"}
    # Flags that consume the next token as their value:
    _VALUE_FLAGS = {"--vaadin-version", "--port", "--host"}
    args = sys.argv[1:]
    views = None
    rest: list[str] = []
    skip_next = False
    for arg in args:
        if skip_next:
            rest.append(arg)
            skip_next = False
        elif arg in _VALUE_FLAGS:
            rest.append(arg)
            skip_next = True
        elif arg in _SUBCOMMANDS:
            rest.append(_SUBCOMMANDS[arg])
        elif views is None and not arg.startswith("-"):
            views = arg
        else:
            rest.append(arg)

    if "--setup" in rest:
        _setup_project(views)
        _setup_vscode()
        sys.exit(0)

    if "--vscode" in rest:
        _setup_vscode()
        sys.exit(0)

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

    if views is None or views == ".":
        views = _auto_detect_app()
        if views is None:
            print("  No views/ directory found in the current directory.")
            print()
            print("  To scaffold a new project:  vaadin --setup")
            print("  Or create views/ manually:  mkdir -p views && touch views/__init__.py")
            print()
            _usage()

    if "." not in views:
        views = f"{views}.views"

    _ensure_importable(views)

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
        _serve(views, host, port, debug, dev=dev)


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
    from vaadin.flow.router import discover_views
    from vaadin.flow.server.http_server import run_server, set_app_directory
    import vaadin.flow.server.http_server as _http

    _http._dev_mode = dev
    _http._views_module = views
    discover_views(views)

    # Resolve app package directory (e.g. "demo.views" → demo/)
    package = views.rsplit(".", 1)[0]
    pkg_mod = importlib.import_module(package)
    if getattr(pkg_mod, "__file__", None):
        set_app_directory(Path(pkg_mod.__file__).parent)
    elif hasattr(pkg_mod, "__path__"):
        # Namespace or synthetic package — use __path__
        set_app_directory(Path(list(pkg_mod.__path__)[0]))

    if socket_fd is not None:
        import socket
        sock = socket.socket(fileno=socket_fd)
        run_server(debug=debug, sock=sock)
    else:
        run_server(host=host, port=port, debug=debug)
