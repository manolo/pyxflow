"""Tests for bundle_generator: project generation, component discovery, FakeView."""

import pytest
from pathlib import Path

from pyxflow.resources.generate_bundle import (
    generate_pom_xml,
    generate_fake_view,
    generate_feature_flags,
    discover_java_components,
    generate_project,
    _DEFAULT_VAADIN_VERSION,
    _read_pyproject_version,
    _parse_flow_version,
    _resolve_flow_version,
)


class TestGeneratePomXml:
    """Test pom.xml generation."""

    def test_contains_vaadin_version(self):
        pom = generate_pom_xml("25.0.4")
        assert "<vaadin.version>25.0.4</vaadin.version>" in pom

    def test_custom_version(self):
        pom = generate_pom_xml("25.1.0")
        assert "<vaadin.version>25.1.0</vaadin.version>" in pom

    def test_war_packaging(self):
        pom = generate_pom_xml("25.0.4")
        assert "<packaging>war</packaging>" in pom

    def test_vaadin_core_dependency(self):
        pom = generate_pom_xml("25.0.4")
        assert "<artifactId>vaadin-core</artifactId>" in pom

    def test_vaadin_maven_plugin(self):
        pom = generate_pom_xml("25.0.4")
        assert "<artifactId>vaadin-maven-plugin</artifactId>" in pom
        assert "<goal>prepare-frontend</goal>" in pom
        assert "<goal>build-frontend</goal>" in pom

    def test_fail_on_missing_web_xml_false(self):
        pom = generate_pom_xml("25.0.4")
        assert "<failOnMissingWebXml>false</failOnMissingWebXml>" in pom

    def test_java_17(self):
        pom = generate_pom_xml("25.0.4")
        assert "<java.version>17</java.version>" in pom

    def test_optimize_bundle_true(self):
        pom = generate_pom_xml("25.0.4", optimize_bundle=True)
        assert "<optimizeBundle>true</optimizeBundle>" in pom

    def test_optimize_bundle_false(self):
        pom = generate_pom_xml("25.0.4", optimize_bundle=False)
        assert "<optimizeBundle>false</optimizeBundle>" in pom

    def test_optimize_bundle_default_true(self):
        pom = generate_pom_xml("25.0.4")
        assert "<optimizeBundle>true</optimizeBundle>" in pom


class TestDiscoverJavaComponents:
    """Test auto-discovery of _v_fqcn from Component subclasses."""

    def test_returns_dict(self):
        registry = discover_java_components()
        assert isinstance(registry, dict)

    def test_discovers_button(self):
        registry = discover_java_components()
        assert "Button" in registry
        assert registry["Button"] == "com.vaadin.flow.component.button.Button"

    def test_discovers_grid(self):
        registry = discover_java_components()
        assert "Grid" in registry
        assert registry["Grid"] == "com.vaadin.flow.component.grid.Grid"

    def test_discovers_dialog(self):
        registry = discover_java_components()
        assert "Dialog" in registry

    def test_discovers_many_components(self):
        """Should find a substantial number of components with _v_fqcn."""
        registry = discover_java_components()
        assert len(registry) >= 40  # We have 49+ components

    def test_does_not_include_base_classes(self):
        """Base classes like Component, HtmlContainer should not appear."""
        registry = discover_java_components()
        assert "Component" not in registry
        assert "HtmlContainer" not in registry

    def test_values_are_java_fqcn(self):
        """All values should be valid Java fully-qualified class names."""
        registry = discover_java_components()
        for name, fqcn in registry.items():
            assert "." in fqcn, f"{name} has invalid FQCN: {fqcn}"
            assert fqcn.startswith("com.vaadin.flow.component."), \
                f"{name} FQCN doesn't start with com.vaadin.flow.component.: {fqcn}"


class TestGenerateFakeView:
    """Test FakeView.java generation."""

    def test_has_route_annotation(self):
        registry = {"Button": "com.vaadin.flow.component.button.Button"}
        java = generate_fake_view(registry)
        assert '@Route("")' in java

    def test_has_uses_annotation(self):
        registry = {"Button": "com.vaadin.flow.component.button.Button"}
        java = generate_fake_view(registry)
        assert "@Uses(Button.class)" in java

    def test_has_import_for_component(self):
        registry = {"Button": "com.vaadin.flow.component.button.Button"}
        java = generate_fake_view(registry)
        assert "import com.vaadin.flow.component.button.Button;" in java

    def test_has_push_annotation(self):
        registry = {}
        java = generate_fake_view(registry)
        assert "@Push" in java
        assert "import com.vaadin.flow.component.page.Push;" in java

    def test_has_jsmodule_annotation(self):
        registry = {"Button": "com.vaadin.flow.component.button.Button"}
        java = generate_fake_view(registry)
        assert '@JsModule("./pyxflow-bundle.js")' in java

    def test_extends_div(self):
        registry = {}
        java = generate_fake_view(registry)
        assert "public class FakeView extends Div {" in java

    def test_multiple_components(self):
        registry = {
            "Button": "com.vaadin.flow.component.button.Button",
            "Grid": "com.vaadin.flow.component.grid.Grid",
            "Dialog": "com.vaadin.flow.component.dialog.Dialog",
        }
        java = generate_fake_view(registry)
        assert "@Uses(Button.class)" in java
        assert "@Uses(Grid.class)" in java
        assert "@Uses(Dialog.class)" in java
        assert "import com.vaadin.flow.component.button.Button;" in java
        assert "import com.vaadin.flow.component.grid.Grid;" in java

    def test_package_declaration(self):
        registry = {}
        java = generate_fake_view(registry)
        assert "package com.vaadin.pyxflow;" in java

    def test_with_real_registry(self):
        """Generate FakeView from the actual component registry."""
        registry = discover_java_components()
        java = generate_fake_view(registry)
        assert "@Uses(Button.class)" in java
        assert "@Uses(Grid.class)" in java
        # Should have many @Uses lines
        uses_count = java.count("@Uses(")
        assert uses_count >= 40


class TestGenerateFeatureFlags:
    """Test feature flags generation."""

    def test_master_detail_flag(self):
        flags = generate_feature_flags()
        assert "masterDetailLayoutComponent=true" in flags


class TestGenerateProject:
    """Test Maven project generation on disk."""

    def test_creates_project_structure(self, tmp_path):
        output_dir = tmp_path / "test-project"
        generate_project(output_dir, "25.0.4")

        assert (output_dir / "pom.xml").is_file()
        assert (output_dir / "frontend" / "pyxflow-bundle.js").is_file()
        assert (output_dir / "src" / "main" / "resources" / "vaadin-featureflags.properties").is_file()

        java_dir = output_dir / "src" / "main" / "java" / "com" / "vaadin" / "pyxflow"
        assert (java_dir / "FakeView.java").is_file()

    def test_pom_has_correct_version(self, tmp_path):
        output_dir = tmp_path / "test-project"
        generate_project(output_dir, "25.1.0")
        pom = (output_dir / "pom.xml").read_text()
        assert "<vaadin.version>25.1.0</vaadin.version>" in pom

    def test_fake_view_has_uses(self, tmp_path):
        output_dir = tmp_path / "test-project"
        generate_project(output_dir, "25.0.4")
        java_dir = output_dir / "src" / "main" / "java" / "com" / "vaadin" / "pyxflow"
        java = (java_dir / "FakeView.java").read_text()
        assert "@Uses(Button.class)" in java

    def test_mvnw_is_executable(self, tmp_path):
        output_dir = tmp_path / "test-project"
        generate_project(output_dir, "25.0.4")
        mvnw = output_dir / "mvnw"
        assert mvnw.is_file()
        import stat
        assert mvnw.stat().st_mode & stat.S_IXUSR

    def test_maven_wrapper_properties(self, tmp_path):
        output_dir = tmp_path / "test-project"
        generate_project(output_dir, "25.0.4")
        props = output_dir / ".mvn" / "wrapper" / "maven-wrapper.properties"
        assert props.is_file()

    def test_overwrites_existing(self, tmp_path):
        """Calling generate_project twice should clean and recreate."""
        output_dir = tmp_path / "test-project"
        generate_project(output_dir, "25.0.4")
        # Add a marker file
        (output_dir / "marker.txt").write_text("test")
        # Regenerate
        generate_project(output_dir, "25.0.4")
        assert not (output_dir / "marker.txt").exists()


class TestDefaultVaadinVersion:
    """Test default version constant."""

    def test_default_version_is_set(self):
        assert _DEFAULT_VAADIN_VERSION == "25.1.0-beta1"


class TestReadPyprojectVersion:
    """Test _read_pyproject_version() reads from pyproject.toml."""

    def test_reads_from_pyproject(self):
        vaadin_ver = _read_pyproject_version()
        assert vaadin_ver == "25.1.0-beta1"

    def test_version_matches_module_constant(self):
        vaadin_ver = _read_pyproject_version()
        assert vaadin_ver == _DEFAULT_VAADIN_VERSION


class TestParseFlowVersion:
    """Test _parse_flow_version() parsing from a Maven POM."""

    def test_parses_flow_version_from_pom(self, tmp_path):
        pom_content = """\
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.vaadin</groupId>
  <artifactId>vaadin-spring-bom</artifactId>
  <version>25.0.6</version>
  <properties>
    <flow.version>25.0.7</flow.version>
    <hilla.version>25.0.6</hilla.version>
  </properties>
</project>
"""
        pom = tmp_path / "test.pom"
        pom.write_text(pom_content)
        assert _parse_flow_version(pom) == "25.0.7"

    def test_parses_different_flow_version(self, tmp_path):
        pom_content = """\
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <properties>
    <flow.version>25.1.0</flow.version>
  </properties>
</project>
"""
        pom = tmp_path / "test.pom"
        pom.write_text(pom_content)
        assert _parse_flow_version(pom) == "25.1.0"

    def test_missing_flow_version_exits(self, tmp_path):
        pom_content = """\
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <properties>
    <hilla.version>25.0.6</hilla.version>
  </properties>
</project>
"""
        pom = tmp_path / "test.pom"
        pom.write_text(pom_content)
        with pytest.raises(SystemExit):
            _parse_flow_version(pom)


class TestResolveFlowVersion:
    """Test _resolve_flow_version() resolves from local Maven repo."""

    def test_resolves_from_local_pom(self):
        """Should resolve flow version from the local Maven repo."""
        flow_ver = _resolve_flow_version("25.0.6")
        assert flow_ver == "25.0.7"
