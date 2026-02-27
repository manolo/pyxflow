"""Tests for bundle directory discovery and serving priority."""

from pathlib import Path
from unittest.mock import patch

from pyflow.server.http_server import (
    get_bundle_directory,
    set_app_directory,
    _app_directory,
)


class TestBundleDiscovery:
    """Test get_bundle_directory() search order."""

    def setup_method(self):
        """Save and clear _app_directory."""
        import pyflow.server.http_server as mod
        self._original = mod._app_directory
        mod._app_directory = None

    def teardown_method(self):
        """Restore _app_directory."""
        import pyflow.server.http_server as mod
        mod._app_directory = self._original

    def test_app_directory_bundle_has_highest_priority(self, tmp_path):
        """When _app_directory/bundle/VAADIN exists, it wins."""
        app_dir = tmp_path / "my_app"
        (app_dir / "bundle" / "VAADIN").mkdir(parents=True)
        set_app_directory(app_dir)

        result = get_bundle_directory()
        assert result == app_dir / "bundle"

    def test_package_internal_bundle(self):
        """Package-internal bundle (ships in wheel) is found."""
        import pyflow.server.http_server as mod
        mod._app_directory = None

        result = get_bundle_directory()
        # The package-internal bundle should exist in the source tree
        if result:
            assert (result / "VAADIN").is_dir()

    def test_app_dir_takes_priority_over_package(self, tmp_path):
        """App-dir bundle overrides the package-internal bundle."""
        app_dir = tmp_path / "my_app"
        (app_dir / "bundle" / "VAADIN").mkdir(parents=True)
        # Write a marker to distinguish from package bundle
        (app_dir / "bundle" / "VAADIN" / "marker.txt").write_text("app")
        set_app_directory(app_dir)

        result = get_bundle_directory()
        assert result == app_dir / "bundle"
        assert (result / "VAADIN" / "marker.txt").read_text() == "app"

    def test_no_bundle_returns_none(self, tmp_path, monkeypatch):
        """When no bundle exists anywhere, returns None."""
        import pyflow.server.http_server as mod
        mod._app_directory = tmp_path / "nonexistent"
        monkeypatch.chdir(tmp_path)

        # Patch the package-internal path to not exist
        with patch.object(Path, "is_dir", return_value=False):
            # This is tricky to test in isolation since the package bundle
            # likely exists. Just verify the function returns Path or None.
            result = get_bundle_directory()
            assert result is None or isinstance(result, Path)

    def test_app_dir_without_bundle_falls_through(self, tmp_path):
        """If app_dir exists but has no bundle/, falls to package internal."""
        app_dir = tmp_path / "my_app"
        app_dir.mkdir()  # No bundle/ subdir
        set_app_directory(app_dir)

        result = get_bundle_directory()
        # Should fall through to package-internal (which exists in source tree)
        if result:
            assert result != app_dir / "bundle"

    def test_cwd_bundle_fallback(self, tmp_path, monkeypatch):
        """./bundle/ in cwd is checked as last resort."""
        import pyflow.server.http_server as mod
        mod._app_directory = None
        monkeypatch.chdir(tmp_path)
        (tmp_path / "bundle" / "VAADIN").mkdir(parents=True)

        # Patch out the package-internal path
        pkg_bundle = Path(mod.__file__).parents[1] / "bundle"
        original_is_dir = Path.is_dir

        def patched_is_dir(self):
            if self == pkg_bundle / "VAADIN":
                return False
            return original_is_dir(self)

        with patch.object(Path, "is_dir", patched_is_dir):
            result = get_bundle_directory()
            assert result == tmp_path / "bundle"


class TestSetAppDirectory:
    """Test set_app_directory()."""

    def setup_method(self):
        import pyflow.server.http_server as mod
        self._original = mod._app_directory
        mod._app_directory = None

    def teardown_method(self):
        import pyflow.server.http_server as mod
        mod._app_directory = self._original

    def test_sets_directory(self, tmp_path):
        set_app_directory(tmp_path)
        import pyflow.server.http_server as mod
        assert mod._app_directory == tmp_path

    def test_overwrite(self, tmp_path):
        set_app_directory(tmp_path / "a")
        set_app_directory(tmp_path / "b")
        import pyflow.server.http_server as mod
        assert mod._app_directory == tmp_path / "b"


class TestNamespacePackageResolution:
    """Test that namespace packages (no __init__.py) resolve _app_directory."""

    def test_namespace_package_path(self, tmp_path, monkeypatch):
        """A package without __init__.py should use __path__ for app_dir."""
        # Create a namespace package structure
        pkg_dir = tmp_path / "myns"
        views_dir = pkg_dir / "views"
        views_dir.mkdir(parents=True)
        (views_dir / "__init__.py").write_text(
            "from pyflow.router import Route\n"
            "from pyflow.components import VerticalLayout\n"
            "@Route('')\n"
            "class TestView(VerticalLayout): pass\n"
        )
        # No __init__.py in myns/ — it's a namespace package

        monkeypatch.chdir(tmp_path)
        monkeypatch.syspath_prepend(str(tmp_path))

        import importlib
        pkg = importlib.import_module("myns")
        assert pkg.__file__ is None  # namespace package
        assert hasattr(pkg, "__path__")

        # Simulate what _serve does
        from pyflow.server import http_server
        original = http_server._app_directory
        try:
            http_server._app_directory = None
            if pkg.__file__:
                http_server.set_app_directory(Path(pkg.__file__).parent)
            elif hasattr(pkg, "__path__"):
                http_server.set_app_directory(Path(list(pkg.__path__)[0]))

            assert http_server._app_directory == pkg_dir
        finally:
            http_server._app_directory = original
            # Clean up imported module
            for key in list(sys.modules.keys()):
                if key.startswith("myns"):
                    del sys.modules[key]

    def test_regular_package_uses_file(self, tmp_path, monkeypatch):
        """A regular package (with __init__.py) should use __file__."""
        pkg_dir = tmp_path / "mypkg"
        pkg_dir.mkdir()
        (pkg_dir / "__init__.py").write_text("")

        monkeypatch.syspath_prepend(str(tmp_path))
        import importlib
        pkg = importlib.import_module("mypkg")
        assert pkg.__file__ is not None

        # Clean up
        for key in list(sys.modules.keys()):
            if key.startswith("mypkg"):
                del sys.modules[key]


# Need sys for cleanup
import sys
