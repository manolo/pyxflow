"""Tests for the complete bundle workflow: generate_and_build paths and CLI."""

import os
import shutil
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from pyxflow.resources.generate_bundle import generate_and_build


class TestGenerateAndBuildPyflowDev:
    """Test generate_and_build() in pyxflow developer mode."""

    def test_detects_pyxflow_dev_tree(self, tmp_path, monkeypatch):
        """When src/pyxflow/ exists, targets src/pyxflow/bundle/."""
        # Create pyxflow source tree marker
        (tmp_path / "src" / "pyxflow").mkdir(parents=True)
        monkeypatch.chdir(tmp_path)

        with patch("pyxflow.resources.generate_bundle.generate_project") as mock_gen, \
             patch("pyxflow.resources.generate_bundle.build_and_extract") as mock_build:
            # generate_project is mocked, so create the dir it would create
            mock_gen.side_effect = lambda d, v, **kw: d.mkdir(parents=True, exist_ok=True)
            generate_and_build(app_dir=None, keep=False, vaadin_version="25.0.6")

            # Should target src/pyxflow/bundle/
            bundle_dir = mock_build.call_args[0][1]
            assert str(bundle_dir).endswith("src/pyxflow/bundle")

    def test_project_dir_is_bundle_project(self, tmp_path, monkeypatch):
        """Maven project should be at cwd/bundle-project."""
        (tmp_path / "src" / "pyxflow").mkdir(parents=True)
        monkeypatch.chdir(tmp_path)

        with patch("pyxflow.resources.generate_bundle.generate_project") as mock_gen, \
             patch("pyxflow.resources.generate_bundle.build_and_extract"):
            generate_and_build(app_dir=None, keep=True)

            project_dir = mock_gen.call_args[0][0]
            assert project_dir == tmp_path / "bundle-project"

    def _create_bundle_project(self, base_path):
        """Create a minimal bundle-project/ with java dir structure."""
        bp = base_path / "bundle-project"
        java_dir = bp / "src" / "main" / "java" / "com" / "vaadin" / "pyxflow"
        java_dir.mkdir(parents=True)
        (java_dir / "FakeView.java").write_text("// placeholder")
        return bp

    def test_keep_preserves_project_dir(self, tmp_path, monkeypatch):
        """With keep=True, bundle-project/ should not be deleted."""
        (tmp_path / "src" / "pyxflow").mkdir(parents=True)
        monkeypatch.chdir(tmp_path)

        with patch("pyxflow.resources.generate_bundle.build_and_extract"):
            self._create_bundle_project(tmp_path)
            generate_and_build(keep=True)
            assert (tmp_path / "bundle-project").exists()

    def test_no_keep_deletes_project_dir(self, tmp_path, monkeypatch):
        """With keep=False, bundle-project/ should be deleted after build."""
        (tmp_path / "src" / "pyxflow").mkdir(parents=True)
        monkeypatch.chdir(tmp_path)

        with patch("pyxflow.resources.generate_bundle.build_and_extract"):
            bp = self._create_bundle_project(tmp_path)
            generate_and_build(keep=False)
            assert not bp.exists()


class TestGenerateAndBuildUserProject:
    """Test generate_and_build() for user projects."""

    def test_user_project_bundle_dir(self, tmp_path, monkeypatch):
        """With app_dir, bundle goes to app_dir/bundle/."""
        monkeypatch.chdir(tmp_path)
        app_dir = tmp_path / "my_app"
        app_dir.mkdir()

        with patch("pyxflow.resources.generate_bundle.generate_project") as mock_gen, \
             patch("pyxflow.resources.generate_bundle.build_and_extract") as mock_build:
            generate_and_build(app_dir=app_dir, keep=True)

            bundle_dir = mock_build.call_args[0][1]
            assert bundle_dir == app_dir / "bundle"

    def test_user_project_project_dir(self, tmp_path, monkeypatch):
        """Maven project should be at app_dir/bundle-project."""
        monkeypatch.chdir(tmp_path)
        app_dir = tmp_path / "my_app"
        app_dir.mkdir()

        with patch("pyxflow.resources.generate_bundle.generate_project") as mock_gen, \
             patch("pyxflow.resources.generate_bundle.build_and_extract"):
            generate_and_build(app_dir=app_dir, keep=True)

            project_dir = mock_gen.call_args[0][0]
            assert project_dir == app_dir / "bundle-project"

    def test_no_pyxflow_no_app_dir_exits(self, tmp_path, monkeypatch):
        """Without pyxflow tree or app_dir, should sys.exit(1)."""
        monkeypatch.chdir(tmp_path)
        with pytest.raises(SystemExit) as exc_info:
            generate_and_build(app_dir=None)
        assert exc_info.value.code == 1

    def test_custom_vaadin_version(self, tmp_path, monkeypatch):
        """Custom vaadin_version is passed to generate_project."""
        monkeypatch.chdir(tmp_path)
        app_dir = tmp_path / "my_app"
        app_dir.mkdir()

        with patch("pyxflow.resources.generate_bundle.generate_project") as mock_gen, \
             patch("pyxflow.resources.generate_bundle.build_and_extract"):
            generate_and_build(app_dir=app_dir, keep=True, vaadin_version="25.1.0")

            version = mock_gen.call_args[0][1]
            assert version == "25.1.0"


class TestGenerateAndBuildReuse:
    """Test reusing existing Maven project."""

    def test_reuses_existing_project(self, tmp_path, monkeypatch):
        """When bundle-project/ exists, should NOT call generate_project."""
        monkeypatch.chdir(tmp_path)
        app_dir = tmp_path / "my_app"
        app_dir.mkdir()

        # Create existing bundle-project with required structure
        bp = app_dir / "bundle-project"
        java_dir = bp / "src" / "main" / "java" / "com" / "vaadin" / "pyxflow"
        java_dir.mkdir(parents=True)
        (java_dir / "FakeView.java").write_text("// old")

        with patch("pyxflow.resources.generate_bundle.generate_project") as mock_gen, \
             patch("pyxflow.resources.generate_bundle.build_and_extract") as mock_build:
            generate_and_build(app_dir=app_dir, keep=True)

            # generate_project should NOT be called
            mock_gen.assert_not_called()
            # build_and_extract should be called with clean=False
            assert mock_build.call_args[1]["clean"] is False

    def test_reuse_updates_fake_view(self, tmp_path, monkeypatch):
        """Reuse should update FakeView.java with current registry."""
        monkeypatch.chdir(tmp_path)
        app_dir = tmp_path / "my_app"
        app_dir.mkdir()

        bp = app_dir / "bundle-project"
        java_dir = bp / "src" / "main" / "java" / "com" / "vaadin" / "pyxflow"
        java_dir.mkdir(parents=True)
        (java_dir / "FakeView.java").write_text("// old content")

        with patch("pyxflow.resources.generate_bundle.build_and_extract"):
            generate_and_build(app_dir=app_dir, keep=True)

            new_content = (java_dir / "FakeView.java").read_text()
            assert "// old content" not in new_content
            assert "@Uses(" in new_content

    def test_fresh_build_uses_clean(self, tmp_path, monkeypatch):
        """Fresh build (no existing project) should use clean=True."""
        monkeypatch.chdir(tmp_path)
        app_dir = tmp_path / "my_app"
        app_dir.mkdir()

        with patch("pyxflow.resources.generate_bundle.generate_project"), \
             patch("pyxflow.resources.generate_bundle.build_and_extract") as mock_build:
            generate_and_build(app_dir=app_dir, keep=True)

            assert mock_build.call_args[1]["clean"] is True


class TestBundleCopyOptimized:
    """Test --optimized flag for copy_from_jars."""

    def _run_main_copy(self, argv):
        """Run main() with copy mode, capturing the copy_from_jars call."""
        with patch("sys.argv", ["pyxflow"] + argv), \
             patch("pyxflow.resources.generate_bundle.copy_from_jars") as mock_cfj:
            from pyxflow.main import main
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0
            return mock_cfj

    def test_bundle_copy_optimized(self):
        """pyxflow bundle --optimized -> copy_from_jars(optimized=True)."""
        mock = self._run_main_copy(["bundle", "--optimized"])
        assert mock.call_args[1]["optimized"] is True

    def test_bundle_copy_default_not_optimized(self):
        """pyxflow bundle -> copy_from_jars(optimized=False)."""
        mock = self._run_main_copy(["bundle"])
        assert mock.call_args[1]["optimized"] is False

    def test_copy_from_jars_optimized_prefix(self, tmp_path):
        """copy_from_jars(optimized=True) uses vaadin-prod-bundle/webapp/ prefix."""
        from pyxflow.resources.generate_bundle import copy_from_jars, _extract_jar_to
        with patch("pyxflow.resources.generate_bundle._find_m2_jar") as mock_find, \
             patch("pyxflow.resources.generate_bundle._download_jar") as mock_dl, \
             patch("pyxflow.resources.generate_bundle._extract_jar_to") as mock_extract:
            mock_find.return_value = Path("/fake.jar")
            mock_extract.return_value = 1
            copy_from_jars(tmp_path, "25.0.6", optimized=True)
            # First call is the prod-bundle extraction
            first_call = mock_extract.call_args_list[0]
            assert first_call[0][1] == "vaadin-prod-bundle/webapp/"

    def test_copy_from_jars_unoptimized_prefix(self, tmp_path):
        """copy_from_jars(optimized=False) uses vaadin-prod-bundle-unoptimized/webapp/ prefix."""
        from pyxflow.resources.generate_bundle import copy_from_jars, _extract_jar_to
        with patch("pyxflow.resources.generate_bundle._find_m2_jar") as mock_find, \
             patch("pyxflow.resources.generate_bundle._download_jar") as mock_dl, \
             patch("pyxflow.resources.generate_bundle._extract_jar_to") as mock_extract:
            mock_find.return_value = Path("/fake.jar")
            mock_extract.return_value = 1
            copy_from_jars(tmp_path, "25.0.6", optimized=False)
            first_call = mock_extract.call_args_list[0]
            assert first_call[0][1] == "vaadin-prod-bundle-unoptimized/webapp/"


class TestCliArgParsing:
    """Test CLI argument parsing in main()."""

    def _run_main_build(self, argv):
        """Run main() with --build flag, capturing the generate_and_build call."""
        with patch("sys.argv", ["pyxflow"] + argv), \
             patch("pyxflow.resources.generate_bundle.generate_and_build") as mock_gab:
            from pyxflow.main import main
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0
            return mock_gab

    def _run_main_copy(self, argv):
        """Run main() with copy mode, capturing the copy_from_jars call."""
        with patch("sys.argv", ["pyxflow"] + argv), \
             patch("pyxflow.resources.generate_bundle.copy_from_jars") as mock_cfj:
            from pyxflow.main import main
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0
            return mock_cfj

    def test_bundle_build_only(self):
        """pyxflow --bundle --build -> generate_and_build(app_dir=None)."""
        mock = self._run_main_build(["--bundle", "--build"])
        mock.assert_called_once()
        assert mock.call_args[1]["app_dir"] is None
        assert mock.call_args[1]["keep"] is False
        assert mock.call_args[1]["optimized"] is False

    def test_bundle_build_optimized(self):
        """pyxflow --bundle --build --optimized -> optimized=True."""
        mock = self._run_main_build(["--bundle", "--build", "--optimized"])
        assert mock.call_args[1]["optimized"] is True

    def test_bundle_build_with_module(self):
        """pyxflow my_app --bundle --build -> app_dir=cwd/my_app."""
        mock = self._run_main_build(["my_app", "--bundle", "--build"])
        mock.assert_called_once()
        app_dir = mock.call_args[1]["app_dir"]
        assert app_dir is not None
        assert app_dir.name == "my_app"

    def test_bundle_build_with_keep(self):
        """pyxflow --bundle --build --keep -> keep=True."""
        mock = self._run_main_build(["--bundle", "--build", "--keep"])
        assert mock.call_args[1]["keep"] is True

    def test_bundle_build_with_module_and_keep(self):
        """pyxflow my_app --bundle --build --keep -> app_dir + keep=True."""
        mock = self._run_main_build(["my_app", "--bundle", "--build", "--keep"])
        assert mock.call_args[1]["app_dir"].name == "my_app"
        assert mock.call_args[1]["keep"] is True

    def test_bundle_build_with_vaadin_version(self):
        """pyxflow --bundle --build --vaadin-version 25.1.0 -> custom version."""
        mock = self._run_main_build(["--bundle", "--build", "--vaadin-version", "25.1.0"])
        assert mock.call_args[1]["vaadin_version"] == "25.1.0"

    def test_bundle_default_vaadin_version(self):
        """pyxflow bundle -> default version from pyproject.toml (25.0.6)."""
        from pyxflow.resources.generate_bundle import _DEFAULT_VAADIN_VERSION
        mock = self._run_main_copy(["bundle"])
        assert mock.call_args[0][1] == _DEFAULT_VAADIN_VERSION

    def test_bundle_copy_custom_version(self):
        """pyxflow bundle --vaadin-version 25.1.0 -> custom version."""
        mock = self._run_main_copy(["bundle", "--vaadin-version", "25.1.0"])
        assert mock.call_args[0][1] == "25.1.0"

    def test_module_with_hyphen_converted_to_underscore(self):
        """pyxflow my-app --bundle --build -> app_dir=cwd/my_app."""
        mock = self._run_main_build(["my-app", "--bundle", "--build"])
        assert mock.call_args[1]["app_dir"].name == "my_app"

    def test_bundle_flag_after_module(self):
        """pyxflow demo --bundle --build works."""
        mock = self._run_main_build(["demo", "--bundle", "--build"])
        mock.assert_called_once()
        assert mock.call_args[1]["app_dir"].name == "demo"

    def test_all_flags_combined(self):
        """pyxflow my_app --bundle --build --keep --vaadin-version 25.1.0."""
        mock = self._run_main_build(["my_app", "--bundle", "--build", "--keep", "--vaadin-version", "25.1.0"])
        assert mock.call_args[1]["app_dir"].name == "my_app"
        assert mock.call_args[1]["keep"] is True
        assert mock.call_args[1]["vaadin_version"] == "25.1.0"
