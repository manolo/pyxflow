"""Tests for the complete bundle workflow: generate_and_build paths and CLI."""

import os
import shutil
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from pyflow.bundle_generator import generate_and_build


class TestGenerateAndBuildPyflowDev:
    """Test generate_and_build() in pyflow developer mode."""

    def test_detects_pyflow_dev_tree(self, tmp_path, monkeypatch):
        """When src/pyflow/ exists, targets src/pyflow/bundle/."""
        # Create pyflow source tree marker
        (tmp_path / "src" / "pyflow").mkdir(parents=True)
        monkeypatch.chdir(tmp_path)

        with patch("pyflow.bundle_generator.generate_project") as mock_gen, \
             patch("pyflow.bundle_generator.build_and_extract") as mock_build:
            # generate_project is mocked, so create the dir it would create
            mock_gen.side_effect = lambda d, v: d.mkdir(parents=True, exist_ok=True)
            generate_and_build(app_dir=None, keep=False, vaadin_version="25.0.4")

            # Should target src/pyflow/bundle/
            bundle_dir = mock_build.call_args[0][1]
            assert str(bundle_dir).endswith("src/pyflow/bundle")

    def test_project_dir_is_bundle_project(self, tmp_path, monkeypatch):
        """Maven project should be at cwd/bundle-project."""
        (tmp_path / "src" / "pyflow").mkdir(parents=True)
        monkeypatch.chdir(tmp_path)

        with patch("pyflow.bundle_generator.generate_project") as mock_gen, \
             patch("pyflow.bundle_generator.build_and_extract"):
            generate_and_build(app_dir=None, keep=True)

            project_dir = mock_gen.call_args[0][0]
            assert project_dir == tmp_path / "bundle-project"

    def _create_bundle_project(self, base_path):
        """Create a minimal bundle-project/ with java dir structure."""
        bp = base_path / "bundle-project"
        java_dir = bp / "src" / "main" / "java" / "com" / "vaadin" / "pyflow"
        java_dir.mkdir(parents=True)
        (java_dir / "FakeView.java").write_text("// placeholder")
        return bp

    def test_keep_preserves_project_dir(self, tmp_path, monkeypatch):
        """With keep=True, bundle-project/ should not be deleted."""
        (tmp_path / "src" / "pyflow").mkdir(parents=True)
        monkeypatch.chdir(tmp_path)

        with patch("pyflow.bundle_generator.build_and_extract"):
            self._create_bundle_project(tmp_path)
            generate_and_build(keep=True)
            assert (tmp_path / "bundle-project").exists()

    def test_no_keep_deletes_project_dir(self, tmp_path, monkeypatch):
        """With keep=False, bundle-project/ should be deleted after build."""
        (tmp_path / "src" / "pyflow").mkdir(parents=True)
        monkeypatch.chdir(tmp_path)

        with patch("pyflow.bundle_generator.build_and_extract"):
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

        with patch("pyflow.bundle_generator.generate_project") as mock_gen, \
             patch("pyflow.bundle_generator.build_and_extract") as mock_build:
            generate_and_build(app_dir=app_dir, keep=True)

            bundle_dir = mock_build.call_args[0][1]
            assert bundle_dir == app_dir / "bundle"

    def test_user_project_project_dir(self, tmp_path, monkeypatch):
        """Maven project should be at app_dir/bundle-project."""
        monkeypatch.chdir(tmp_path)
        app_dir = tmp_path / "my_app"
        app_dir.mkdir()

        with patch("pyflow.bundle_generator.generate_project") as mock_gen, \
             patch("pyflow.bundle_generator.build_and_extract"):
            generate_and_build(app_dir=app_dir, keep=True)

            project_dir = mock_gen.call_args[0][0]
            assert project_dir == app_dir / "bundle-project"

    def test_no_pyflow_no_app_dir_exits(self, tmp_path, monkeypatch):
        """Without pyflow tree or app_dir, should sys.exit(1)."""
        monkeypatch.chdir(tmp_path)
        with pytest.raises(SystemExit) as exc_info:
            generate_and_build(app_dir=None)
        assert exc_info.value.code == 1

    def test_custom_vaadin_version(self, tmp_path, monkeypatch):
        """Custom vaadin_version is passed to generate_project."""
        monkeypatch.chdir(tmp_path)
        app_dir = tmp_path / "my_app"
        app_dir.mkdir()

        with patch("pyflow.bundle_generator.generate_project") as mock_gen, \
             patch("pyflow.bundle_generator.build_and_extract"):
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
        java_dir = bp / "src" / "main" / "java" / "com" / "vaadin" / "pyflow"
        java_dir.mkdir(parents=True)
        (java_dir / "FakeView.java").write_text("// old")

        with patch("pyflow.bundle_generator.generate_project") as mock_gen, \
             patch("pyflow.bundle_generator.build_and_extract") as mock_build:
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
        java_dir = bp / "src" / "main" / "java" / "com" / "vaadin" / "pyflow"
        java_dir.mkdir(parents=True)
        (java_dir / "FakeView.java").write_text("// old content")

        with patch("pyflow.bundle_generator.build_and_extract"):
            generate_and_build(app_dir=app_dir, keep=True)

            new_content = (java_dir / "FakeView.java").read_text()
            assert "// old content" not in new_content
            assert "@Uses(" in new_content

    def test_fresh_build_uses_clean(self, tmp_path, monkeypatch):
        """Fresh build (no existing project) should use clean=True."""
        monkeypatch.chdir(tmp_path)
        app_dir = tmp_path / "my_app"
        app_dir.mkdir()

        with patch("pyflow.bundle_generator.generate_project"), \
             patch("pyflow.bundle_generator.build_and_extract") as mock_build:
            generate_and_build(app_dir=app_dir, keep=True)

            assert mock_build.call_args[1]["clean"] is True


class TestCliArgParsing:
    """Test CLI argument parsing in main()."""

    def _run_main(self, argv):
        """Run main() with given argv, capturing the generate_and_build call."""
        with patch("sys.argv", ["vaadin"] + argv), \
             patch("pyflow.bundle_generator.generate_and_build") as mock_gab:
            from pyflow.app import main
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0
            return mock_gab

    def test_bundle_only(self):
        """vaadin --bundle → generate_and_build(app_dir=None)."""
        mock = self._run_main(["--bundle"])
        mock.assert_called_once()
        assert mock.call_args[1]["app_dir"] is None
        assert mock.call_args[1]["keep"] is False

    def test_bundle_with_module(self):
        """vaadin my_app --bundle → app_dir=cwd/my_app."""
        mock = self._run_main(["my_app", "--bundle"])
        mock.assert_called_once()
        app_dir = mock.call_args[1]["app_dir"]
        assert app_dir is not None
        assert app_dir.name == "my_app"

    def test_bundle_with_keep(self):
        """vaadin --bundle --keep → keep=True."""
        mock = self._run_main(["--bundle", "--keep"])
        assert mock.call_args[1]["keep"] is True

    def test_bundle_with_module_and_keep(self):
        """vaadin my_app --bundle --keep → app_dir + keep=True."""
        mock = self._run_main(["my_app", "--bundle", "--keep"])
        assert mock.call_args[1]["app_dir"].name == "my_app"
        assert mock.call_args[1]["keep"] is True

    def test_bundle_with_vaadin_version(self):
        """vaadin --bundle --vaadin-version 25.1.0 → custom version."""
        mock = self._run_main(["--bundle", "--vaadin-version", "25.1.0"])
        assert mock.call_args[1]["vaadin_version"] == "25.1.0"

    def test_bundle_default_vaadin_version(self):
        """vaadin --bundle → default version 25.0.4."""
        mock = self._run_main(["--bundle"])
        assert mock.call_args[1]["vaadin_version"] == "25.0.4"

    def test_module_with_hyphen_converted_to_underscore(self):
        """vaadin my-app --bundle → app_dir=cwd/my_app."""
        mock = self._run_main(["my-app", "--bundle"])
        assert mock.call_args[1]["app_dir"].name == "my_app"

    def test_bundle_flag_after_module(self):
        """vaadin demo --bundle works (not just vaadin --bundle)."""
        mock = self._run_main(["demo", "--bundle"])
        mock.assert_called_once()
        assert mock.call_args[1]["app_dir"].name == "demo"

    def test_all_flags_combined(self):
        """vaadin my_app --bundle --keep --vaadin-version 25.1.0."""
        mock = self._run_main(["my_app", "--bundle", "--keep", "--vaadin-version", "25.1.0"])
        assert mock.call_args[1]["app_dir"].name == "my_app"
        assert mock.call_args[1]["keep"] is True
        assert mock.call_args[1]["vaadin_version"] == "25.1.0"
