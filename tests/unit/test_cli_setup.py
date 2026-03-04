"""Tests for vaadin --setup, --vscode, and CLI auto-detection."""

import json
import sys
from pathlib import Path
from unittest import mock

import pytest

from pyxflow.main import _auto_detect_app
from pyxflow.resources.setup_app import _scaffold_dir, _setup_project, _setup_vscode


# ---------------------------------------------------------------------------
# _scaffold_dir
# ---------------------------------------------------------------------------

class TestScaffoldDir:
    def test_returns_traversable(self):
        d = _scaffold_dir()
        assert (d / "favicon.ico").is_file()

    def test_has_project_templates(self):
        d = _scaffold_dir() / "project"
        assert (d / "__main__.py.tmpl").is_file()
        assert (d / "views" / "main_layout.py.tmpl").is_file()
        assert (d / "views" / "hello_world.py.tmpl").is_file()
        assert (d / "static" / "styles" / "styles.css").is_file()

    def test_has_vscode_templates(self):
        d = _scaffold_dir() / "vscode"
        assert (d / "settings.json").is_file()
        assert (d / "extensions.json").is_file()
        assert (d / "python.code-snippets").is_file()
        assert (d / "templates" / "pyxflow_view.py").is_file()


# ---------------------------------------------------------------------------
# _setup_project -- no app_name (scaffold in cwd)
# ---------------------------------------------------------------------------

class TestSetupProjectInCwd:
    def test_creates_views_and_static_in_cwd(self, tmp_path, monkeypatch):
        project = tmp_path / "my-app"
        project.mkdir()
        monkeypatch.chdir(project)

        _setup_project(app_name=None)

        assert (project / "views" / "__init__.py").exists()
        assert (project / "views" / "main_layout.py").exists()
        assert (project / "views" / "hello_world.py").exists()
        assert (project / "static" / "styles" / "styles.css").exists()
        assert (project / "static" / "favicon.ico").exists()
        assert (project / "static" / "images").is_dir()
        assert (project / "__init__.py").exists()
        assert (project / "__main__.py").exists()

    def test_cwd_mode_uses_relative_import(self, tmp_path, monkeypatch):
        project = tmp_path / "cool-app"
        project.mkdir()
        monkeypatch.chdir(project)

        _setup_project(app_name=None)

        # cwd mode: import from views directly, not cool_app.views
        hello = (project / "views" / "hello_world.py").read_text()
        assert "from views.main_layout import MainLayout" in hello
        assert "cool_app.views" not in hello

    def test_main_py_uses_cwd_name(self, tmp_path, monkeypatch):
        project = tmp_path / "my-demo"
        project.mkdir()
        monkeypatch.chdir(project)

        _setup_project(app_name=None)

        main = (project / "__main__.py").read_text()
        assert "python -m my_demo" in main
        assert "FlowApp" in main

    def test_does_not_create_subdirectory(self, tmp_path, monkeypatch):
        project = tmp_path / "flat-app"
        project.mkdir()
        monkeypatch.chdir(project)

        _setup_project(app_name=None)

        # Should NOT have a flat_app/ subdirectory
        assert not (project / "flat_app").exists()

    def test_idempotent_does_not_overwrite(self, tmp_path, monkeypatch):
        project = tmp_path / "myapp"
        project.mkdir()
        monkeypatch.chdir(project)

        _setup_project(app_name=None)

        # Modify a file
        hello = project / "views" / "hello_world.py"
        hello.write_text("# custom content\n")

        # Run again -- should NOT overwrite
        _setup_project(app_name=None)
        assert hello.read_text() == "# custom content\n"


# ---------------------------------------------------------------------------
# _setup_project -- explicit app_name (subdirectory)
# ---------------------------------------------------------------------------

class TestSetupProjectSubdir:
    def test_creates_subdirectory(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)

        _setup_project(app_name="myapp")

        assert (tmp_path / "myapp" / "views" / "hello_world.py").exists()
        assert (tmp_path / "myapp" / "__main__.py").exists()
        assert (tmp_path / "myapp" / "static" / "favicon.ico").exists()

    def test_template_uses_explicit_name(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)

        _setup_project(app_name="webapp")

        hello = (tmp_path / "webapp" / "views" / "hello_world.py").read_text()
        assert "from webapp.views.main_layout import MainLayout" in hello

    def test_does_not_touch_existing_files(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)

        # Pre-existing file
        (tmp_path / "existing.txt").write_text("keep me")

        _setup_project(app_name="myapp")

        assert (tmp_path / "existing.txt").read_text() == "keep me"


# ---------------------------------------------------------------------------
# _setup_vscode
# ---------------------------------------------------------------------------

class TestSetupVscode:
    def test_creates_all_files(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        # Patch shutil.which to return None (skip extension install)
        with mock.patch("shutil.which", return_value=None):
            _setup_vscode()

        assert (tmp_path / ".vscode" / "settings.json").exists()
        assert (tmp_path / ".vscode" / "extensions.json").exists()
        assert (tmp_path / ".vscode" / "python.code-snippets").exists()
        assert (tmp_path / ".vscode" / "templates" / "pyxflow_view.py").exists()

    def test_settings_json_valid(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with mock.patch("shutil.which", return_value=None):
            _setup_vscode()

        settings = json.loads((tmp_path / ".vscode" / "settings.json").read_text())
        assert settings["files.exclude"]["**/__pycache__"] is True
        assert settings["python.analysis.autoImportCompletions"] is True
        assert settings["python.defaultInterpreterPath"] == ".venv/bin/python"
        assert settings["editor.snippetSuggestions"] == "top"
        assert "folderTemplates.structures" in settings

    def test_extensions_json_valid(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with mock.patch("shutil.which", return_value=None):
            _setup_vscode()

        ext = json.loads((tmp_path / ".vscode" / "extensions.json").read_text())
        recs = ext["recommendations"]
        assert "ms-python.python" in recs
        assert "ms-python.pylance" in recs
        assert "huuums.vscode-fast-folder-structure" in recs

    def test_snippets_has_vview(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with mock.patch("shutil.which", return_value=None):
            _setup_vscode()

        snippets = json.loads((tmp_path / ".vscode" / "python.code-snippets").read_text())
        assert "Vaadin View" in snippets
        assert snippets["Vaadin View"]["prefix"] == "vview"

    def test_settings_merge_preserves_custom(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        vscode = tmp_path / ".vscode"
        vscode.mkdir()
        (vscode / "settings.json").write_text(json.dumps({
            "my.custom": True,
            "editor.snippetSuggestions": "bottom",  # user override
        }))

        with mock.patch("shutil.which", return_value=None):
            _setup_vscode()

        settings = json.loads((vscode / "settings.json").read_text())
        # Custom setting preserved
        assert settings["my.custom"] is True
        # User override NOT replaced
        assert settings["editor.snippetSuggestions"] == "bottom"
        # Missing defaults added
        assert "python.analysis.autoImportCompletions" in settings

    def test_extensions_merge_no_duplicates(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        vscode = tmp_path / ".vscode"
        vscode.mkdir()
        (vscode / "extensions.json").write_text(json.dumps({
            "recommendations": ["ms-python.python", "my.custom.ext"]
        }))

        with mock.patch("shutil.which", return_value=None):
            _setup_vscode()

        ext = json.loads((vscode / "extensions.json").read_text())
        recs = ext["recommendations"]
        # No duplicates
        assert recs.count("ms-python.python") == 1
        # Custom preserved
        assert "my.custom.ext" in recs
        # Missing added
        assert "ms-python.pylance" in recs

    def test_code_install_called_when_available(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        calls = []
        with mock.patch("shutil.which", return_value="/usr/bin/code"):
            with mock.patch("subprocess.run", side_effect=lambda *a, **kw: calls.append(a[0])):
                _setup_vscode()

        # Should have called code --install-extension for each
        ext_ids = [c[2] for c in calls]  # [code, --install-extension, <id>]
        assert "ms-python.python" in ext_ids
        assert "ms-python.pylance" in ext_ids


# ---------------------------------------------------------------------------
# _auto_detect_app
# ---------------------------------------------------------------------------

class TestAutoDetectApp:
    def test_finds_subdir_with_views(self, tmp_path, monkeypatch):
        (tmp_path / "myapp" / "views").mkdir(parents=True)
        monkeypatch.chdir(tmp_path)

        assert _auto_detect_app() == "myapp"

    def test_finds_views_in_cwd(self, tmp_path, monkeypatch):
        (tmp_path / "views").mkdir()
        monkeypatch.chdir(tmp_path)

        result = _auto_detect_app()
        assert result == tmp_path.name.replace("-", "_")

    def test_finds_views_in_cwd_with_hyphens(self, tmp_path, monkeypatch):
        project = tmp_path / "my-cool-app"
        project.mkdir()
        (project / "views").mkdir()
        monkeypatch.chdir(project)

        assert _auto_detect_app() == "my_cool_app"

    def test_prefers_subdir_over_cwd(self, tmp_path, monkeypatch):
        # Both subdir and cwd have views/
        (tmp_path / "myapp" / "views").mkdir(parents=True)
        (tmp_path / "views").mkdir()
        monkeypatch.chdir(tmp_path)

        # Should find subdirectory first
        assert _auto_detect_app() == "myapp"

    def test_returns_none_when_no_views(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)

        assert _auto_detect_app() is None


# ---------------------------------------------------------------------------
# CLI argument parsing (main function internals)
# ---------------------------------------------------------------------------

class TestCliParsing:
    """Test CLI argument parsing by simulating sys.argv."""

    def test_dot_treated_as_auto_detect(self, tmp_path, monkeypatch):
        """vaadin . should auto-detect like vaadin (no args)."""
        from pyxflow.main import main

        (tmp_path / "myapp" / "views").mkdir(parents=True)
        (tmp_path / "myapp" / "__init__.py").touch()
        (tmp_path / "myapp" / "views" / "__init__.py").touch()
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(sys, "argv", ["vaadin", "."])

        # main() will try to _serve which needs real views -- just verify it
        # resolves to the right module. We mock _serve to capture the args.
        captured = {}

        def mock_serve(views, host, port, debug, *, dev=False, socket_fd=None):
            captured["views"] = views
            captured["host"] = host
            captured["port"] = port

        monkeypatch.setattr("pyxflow.main._serve", mock_serve)
        main()

        assert captured["views"] == "myapp.views"

    def test_explicit_module(self, tmp_path, monkeypatch):
        """vaadin myapp should use myapp.views."""
        from pyxflow.main import main

        (tmp_path / "myapp" / "views").mkdir(parents=True)
        (tmp_path / "myapp" / "__init__.py").touch()
        (tmp_path / "myapp" / "views" / "__init__.py").touch()
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(sys, "argv", ["vaadin", "myapp"])

        captured = {}

        def mock_serve(views, host, port, debug, *, dev=False, socket_fd=None):
            captured["views"] = views

        monkeypatch.setattr("pyxflow.main._serve", mock_serve)
        main()

        assert captured["views"] == "myapp.views"

    def test_no_args_auto_detects(self, tmp_path, monkeypatch):
        """vaadin (no args) should auto-detect module."""
        from pyxflow.main import main

        (tmp_path / "demo" / "views").mkdir(parents=True)
        (tmp_path / "demo" / "__init__.py").touch()
        (tmp_path / "demo" / "views" / "__init__.py").touch()
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(sys, "argv", ["vaadin"])

        captured = {}

        def mock_serve(views, host, port, debug, *, dev=False, socket_fd=None):
            captured["views"] = views

        monkeypatch.setattr("pyxflow.main._serve", mock_serve)
        main()

        assert captured["views"] == "demo.views"

    def test_port_flag(self, tmp_path, monkeypatch):
        from pyxflow.main import main

        (tmp_path / "myapp" / "views").mkdir(parents=True)
        (tmp_path / "myapp" / "__init__.py").touch()
        (tmp_path / "myapp" / "views" / "__init__.py").touch()
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(sys, "argv", ["vaadin", "--port", "9999"])

        captured = {}

        def mock_serve(views, host, port, debug, *, dev=False, socket_fd=None):
            captured["port"] = port

        monkeypatch.setattr("pyxflow.main._serve", mock_serve)
        main()

        assert captured["port"] == 9999

    def test_setup_flag_creates_project(self, tmp_path, monkeypatch):
        from pyxflow.main import main

        project = tmp_path / "new-app"
        project.mkdir()
        monkeypatch.chdir(project)
        monkeypatch.setattr(sys, "argv", ["vaadin", "--setup"])

        # Mock _setup_vscode to skip extension install
        with mock.patch("shutil.which", return_value=None):
            with pytest.raises(SystemExit) as exc_info:
                main()

        assert exc_info.value.code == 0
        assert (project / "views" / "hello_world.py").exists()

    def test_setup_with_name_creates_subdir(self, tmp_path, monkeypatch):
        from pyxflow.main import main

        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(sys, "argv", ["vaadin", "--setup", "webapp"])

        with mock.patch("shutil.which", return_value=None):
            with pytest.raises(SystemExit) as exc_info:
                main()

        assert exc_info.value.code == 0
        assert (tmp_path / "webapp" / "views" / "hello_world.py").exists()

    def test_vscode_flag_only(self, tmp_path, monkeypatch):
        from pyxflow.main import main

        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(sys, "argv", ["vaadin", "--vscode"])

        with mock.patch("shutil.which", return_value=None):
            with pytest.raises(SystemExit) as exc_info:
                main()

        assert exc_info.value.code == 0
        assert (tmp_path / ".vscode" / "settings.json").exists()
        # Should NOT create views/
        assert not (tmp_path / "views").exists()

    def test_cwd_views_synthetic_module(self, tmp_path, monkeypatch):
        """When views/ is in cwd, a synthetic module should be injected."""
        from pyxflow.main import main

        # Simulate --setup result: views/ at root
        project = tmp_path / "my-app"
        project.mkdir()
        (project / "views").mkdir()
        (project / "__init__.py").touch()
        (project / "views" / "__init__.py").touch()
        # Need at least one view file
        (project / "views" / "hello.py").write_text(
            "from pyxflow import Route\n"
            "from pyxflow.components import Div\n"
            "@Route('hello')\n"
            "class HelloView(Div): pass\n"
        )
        monkeypatch.chdir(project)
        monkeypatch.setattr(sys, "argv", ["vaadin", "."])

        captured = {}

        def mock_serve(views, host, port, debug, *, dev=False, socket_fd=None):
            captured["views"] = views

        monkeypatch.setattr("pyxflow.main._serve", mock_serve)
        main()

        # Should derive my_app from my-app
        assert captured["views"] == "my_app.views"
        # Synthetic module should be in sys.modules
        assert "my_app" in sys.modules
        assert sys.modules["my_app"].__path__ == [str(project)]

        # Cleanup
        del sys.modules["my_app"]

    def test_cwd_views_sibling_packages_importable(self, tmp_path, monkeypatch):
        """When views/ is in cwd, sibling packages (e.g. lib/) must be importable."""
        from pyxflow.main import main

        project = tmp_path / "my-app"
        project.mkdir()
        (project / "views").mkdir()
        (project / "__init__.py").touch()
        (project / "views" / "__init__.py").touch()
        (project / "views" / "hello.py").write_text(
            "from pyxflow import Route\n"
            "from pyxflow.components import Div\n"
            "@Route('hello')\n"
            "class HelloView(Div): pass\n"
        )
        # Create a sibling package (like lib/)
        (project / "lib").mkdir()
        (project / "lib" / "__init__.py").write_text("MAGIC = 42\n")

        monkeypatch.chdir(project)
        monkeypatch.setattr(sys, "argv", ["vaadin", "."])

        def mock_serve(views, host, port, debug, *, dev=False, socket_fd=None):
            pass

        monkeypatch.setattr("pyxflow.main._serve", mock_serve)
        main()

        # cwd must be in sys.path so sibling packages are importable
        assert str(project) in sys.path

        # Cleanup
        del sys.modules["my_app"]
        if "lib" in sys.modules:
            del sys.modules["lib"]


# ---------------------------------------------------------------------------
# Favicon link in index.html
# ---------------------------------------------------------------------------

class TestFaviconInIndexHtml:
    def test_index_html_has_favicon_link(self):
        from pyxflow.server.http_server import get_index_html
        html = get_index_html()
        assert '<link rel="icon" href="/favicon.ico">' in html

    def test_favicon_link_is_in_head(self):
        from pyxflow.server.http_server import get_index_html
        html = get_index_html()
        head_end = html.index("</head>")
        favicon_pos = html.index('<link rel="icon" href="/favicon.ico">')
        assert favicon_pos < head_end


class TestFaviconFallback:
    """Test that /favicon.ico falls back to scaffold when no static file."""

    def test_scaffold_favicon_exists(self):
        """The package scaffold must ship a favicon.ico."""
        import importlib.resources
        favicon = importlib.resources.files("pyxflow") / "resources" / "scaffold" / "favicon.ico"
        with importlib.resources.as_file(favicon) as f:
            assert f.is_file()
            data = f.read_bytes()
            assert data[:4] == b"\x00\x00\x01\x00"  # ICO magic


# ---------------------------------------------------------------------------
# Scaffold template content
# ---------------------------------------------------------------------------

class TestScaffoldTemplateContent:
    def test_main_template_has_placeholder(self):
        d = _scaffold_dir() / "project"
        text = (d / "__main__.py.tmpl").read_text()
        assert "{{app_name}}" in text
        assert "FlowApp" in text

    def test_hello_world_template_has_placeholder(self):
        d = _scaffold_dir() / "project"
        text = (d / "views" / "hello_world.py.tmpl").read_text()
        assert "{{app_name}}" in text
        assert "@Route" in text

    def test_main_layout_template_has_appshell(self):
        d = _scaffold_dir() / "project"
        text = (d / "views" / "main_layout.py.tmpl").read_text()
        assert "@AppShell" in text
        assert "AppLayout" in text

    def test_styles_css_has_lumo_import(self):
        d = _scaffold_dir() / "project"
        text = (d / "static" / "styles" / "styles.css").read_text()
        assert "lumo" in text

    def test_favicon_is_valid_ico(self):
        import importlib.resources
        favicon = _scaffold_dir() / "favicon.ico"
        with importlib.resources.as_file(favicon) as f:
            data = f.read_bytes()
        # ICO files start with \x00\x00\x01\x00
        assert data[:4] == b"\x00\x00\x01\x00"
        assert len(data) > 1000  # Should be a real icon
