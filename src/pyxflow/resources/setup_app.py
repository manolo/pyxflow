"""Project scaffolding: --setup and --vscode."""

import json
import sys


def _scaffold_dir():
    """Return the scaffold resource directory."""
    import importlib.resources
    return importlib.resources.files("pyxflow") / "resources" / "scaffold"


def _setup_project(app_name: str | None = None) -> None:
    """Scaffold a new Vaadin PyXFlow project structure."""
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
    lib_dir = pkg / "lib"
    static_styles = pkg / "static" / "styles"
    static_images = pkg / "static" / "images"

    for d in (views_dir, lib_dir, static_styles, static_images):
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
    for init in (pkg / "__init__.py", views_dir / "__init__.py", lib_dir / "__init__.py"):
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
    """Generate .vscode/ config for Vaadin PyXFlow development."""
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

    # --- templates/pyxflow_view.py ---
    templates_dir = vscode_dir / "templates"
    templates_dir.mkdir(exist_ok=True)
    template_dest = templates_dir / "pyxflow_view.py"
    template_dest.write_text((scaffold / "templates" / "pyxflow_view.py").read_text())
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
