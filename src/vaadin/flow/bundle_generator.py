"""Generate a Maven project that produces the frontend bundle for PyFlow.

Usage (via CLI)::

    # PyFlow developer (from vaadin-pyflow/ checkout)
    vaadin --bundle                          # → src/vaadin/flow/bundle/
    vaadin --bundle --keep                   # keep bundle-project/ for debugging
    vaadin --bundle --vaadin-version 25.0.4  # pin Vaadin version

    # User project
    vaadin my_app --bundle                   # → my_app/bundle/
    vaadin my_app --bundle --keep            # keep my_app/bundle-project/
"""

import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

# Default Vaadin version (matches bundle-generator/pom.xml)
_DEFAULT_VAADIN_VERSION = "25.0.4"


def generate_pom_xml(vaadin_version: str) -> str:
    """Minimal pom.xml: WAR packaging, vaadin-core, vaadin-maven-plugin."""
    return f"""\
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.vaadin.pyflow</groupId>
    <artifactId>bundle-generator</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <properties>
        <java.version>17</java.version>
        <vaadin.version>{vaadin_version}</vaadin.version>
        <maven.compiler.source>${{java.version}}</maven.compiler.source>
        <maven.compiler.target>${{java.version}}</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>com.vaadin</groupId>
                <artifactId>vaadin-bom</artifactId>
                <version>${{vaadin.version}}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <dependencies>
        <dependency>
            <groupId>com.vaadin</groupId>
            <artifactId>vaadin-core</artifactId>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>com.vaadin</groupId>
                <artifactId>vaadin-maven-plugin</artifactId>
                <version>${{vaadin.version}}</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>prepare-frontend</goal>
                            <goal>build-frontend</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <configuration>
                    <failOnMissingWebXml>false</failOnMissingWebXml>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
"""


def discover_java_components() -> dict[str, str]:
    """Auto-discover all Component subclasses that have _v_fqcn.

    Imports vaadin.flow.components (which imports all component modules),
    then walks the Component class hierarchy collecting _v_fqcn values.
    Returns {PythonClassName: JavaFQCN}.
    """
    from vaadin.flow.core.component import Component
    import vaadin.flow.components  # noqa: F401 — triggers all component imports

    registry: dict[str, str] = {}
    queue = list(Component.__subclasses__())
    while queue:
        cls = queue.pop()
        # Only take _v_fqcn declared directly on this class, not inherited
        if "_v_fqcn" in cls.__dict__:
            registry[cls.__name__] = cls.__dict__["_v_fqcn"]
        queue.extend(cls.__subclasses__())
    return registry


def generate_fake_view(registry: dict[str, str]) -> str:
    """Generate FakeView.java with @Route and @Uses for every component."""
    imports: list[str] = [
        "import com.vaadin.flow.component.html.Div;",
        "import com.vaadin.flow.component.dependency.JsModule;",
        "import com.vaadin.flow.component.dependency.Uses;",
        "import com.vaadin.flow.component.page.Push;",
        "import com.vaadin.flow.router.Route;",
    ]
    uses: list[str] = []

    for _py_name, java_fqcn in sorted(registry.items()):
        class_name = java_fqcn.rsplit(".", 1)[1]
        imports.append(f"import {java_fqcn};")
        uses.append(f"@Uses({class_name}.class)")

    imports_str = "\n".join(sorted(set(imports)))
    uses_str = "\n".join(sorted(uses))

    return f"""\
package com.vaadin.pyflow;

{imports_str}

@Push
@Route("")
@JsModule("./pyflow-bundle.js")
{uses_str}
public class FakeView extends Div {{
}}
"""


def generate_feature_flags() -> str:
    """Feature flags for experimental components (e.g. MasterDetailLayout)."""
    return "com.vaadin.experimental.masterDetailLayoutComponent=true\n"


def generate_project(output_dir: Path, vaadin_version: str) -> None:
    """Create a complete Maven project in output_dir."""
    registry = discover_java_components()

    # Clean and create directories
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    java_dir = output_dir / "src" / "main" / "java" / "com" / "vaadin" / "pyflow"
    java_dir.mkdir(parents=True)

    resources_dir = output_dir / "src" / "main" / "resources"
    resources_dir.mkdir(parents=True)

    # pom.xml
    (output_dir / "pom.xml").write_text(generate_pom_xml(vaadin_version))

    # FakeView.java
    (java_dir / "FakeView.java").write_text(
        generate_fake_view(registry)
    )

    # frontend/pyflow-bundle.js — triggers Vaadin's frontend build
    frontend_dir = output_dir / "frontend"
    frontend_dir.mkdir()
    (frontend_dir / "pyflow-bundle.js").write_text("// marker for Vaadin bundle build\n")

    # Feature flags
    (resources_dir / "vaadin-featureflags.properties").write_text(
        generate_feature_flags()
    )

    # Copy Maven wrapper from packaged resources
    resources_pkg = Path(__file__).parent / "bundle_generator_resources"
    if not resources_pkg.exists():
        print(f"ERROR: Maven wrapper resources not found at {resources_pkg}")
        sys.exit(1)

    for name in ("mvnw", "mvnw.cmd"):
        src = resources_pkg / name
        dst = output_dir / name
        shutil.copy2(src, dst)
        if name == "mvnw":
            os.chmod(dst, 0o755)

    mvn_wrapper_dir = output_dir / ".mvn" / "wrapper"
    mvn_wrapper_dir.mkdir(parents=True)
    shutil.copy2(
        resources_pkg / ".mvn" / "wrapper" / "maven-wrapper.properties",
        mvn_wrapper_dir / "maven-wrapper.properties",
    )

    print(f"  Maven project generated in {output_dir}")


def _find_mvn(project_dir: Path) -> list[str]:
    """Return the command to invoke Maven, preferring the wrapper."""
    if sys.platform == "win32":
        mvnw = project_dir / "mvnw.cmd"
        if mvnw.exists():
            return [str(mvnw)]
    else:
        mvnw = project_dir / "mvnw"
        if mvnw.exists():
            # Ensure executable (permissions may be lost during copy/zip)
            mvnw.chmod(0o755)
            return [str(mvnw)]
    # Fallback to mvn on PATH
    if shutil.which("mvn"):
        return ["mvn"]
    print("ERROR: Neither mvnw nor mvn found. Install Maven or check the project.")
    sys.exit(1)


def build_and_extract(project_dir: Path, bundle_dir: Path, *, clean: bool = True) -> None:
    """Run Maven build and extract bundle from WAR into bundle_dir."""
    # Build
    mvn_cmd = _find_mvn(project_dir)
    goals = ["clean", "package"] if clean else ["package"]
    print(f"  Building Maven project (production mode) with {mvn_cmd[0]}...")
    result = subprocess.run(
        [*mvn_cmd, *goals, "-DskipTests", "-Pproduction"],
        cwd=project_dir,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("ERROR: Maven build failed!")
        # Show last 30 lines of output for diagnosis
        lines = (result.stdout + result.stderr).strip().splitlines()
        for line in lines[-30:]:
            print(f"    {line}")
        sys.exit(1)

    # Find WAR
    war_file = project_dir / "target" / "bundle-generator-1.0-SNAPSHOT.war"
    if not war_file.exists():
        print(f"ERROR: WAR file not found at {war_file}")
        sys.exit(1)
    print(f"  WAR created: {war_file}")

    # Clean existing bundle
    vaadin_dir = bundle_dir / "VAADIN"
    if vaadin_dir.exists():
        shutil.rmtree(vaadin_dir)
    bundle_dir.mkdir(parents=True, exist_ok=True)

    # Extract bundle from WAR
    print("  Extracting bundle from WAR...")
    with zipfile.ZipFile(war_file) as zf:
        # WAR layout: WEB-INF/classes/META-INF/VAADIN/webapp/*
        war_prefix = "WEB-INF/classes/META-INF/VAADIN/webapp/"
        for entry in zf.namelist():
            if entry.startswith(war_prefix) and not entry.endswith("/"):
                rel = entry[len(war_prefix):]
                dest = bundle_dir / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(entry) as src, open(dest, "wb") as dst:
                    dst.write(src.read())

    # Extract nested JARs from exploded WAR
    exploded_lib = project_dir / "target" / "bundle-generator-1.0-SNAPSHOT" / "WEB-INF" / "lib"
    _extract_theme_jar(exploded_lib, "vaadin-lumo-theme-", "lumo", bundle_dir)
    _extract_theme_jar(exploded_lib, "vaadin-aura-theme-", "aura", bundle_dir)
    _extract_jar_resources(exploded_lib, "flow-push-", bundle_dir, "Push scripts")

    # Report
    js_size = sum(f.stat().st_size for f in bundle_dir.rglob("*.js"))
    css_size = sum(f.stat().st_size for f in bundle_dir.rglob("*.css"))
    print(f"  JavaScript: {js_size / 1024 / 1024:.2f} MB")
    print(f"  CSS: {css_size / 1024:.1f} KB")
    print(f"  Bundle extracted to: {bundle_dir}")


def _extract_theme_jar(lib_dir: Path, prefix: str, theme_name: str, bundle_dir: Path) -> None:
    """Extract theme CSS from a JAR in the exploded WAR's WEB-INF/lib/."""
    if not lib_dir.exists():
        print(f"  WARNING: {lib_dir} not found, skipping {theme_name} theme")
        return

    jar_files = [f for f in lib_dir.iterdir() if f.name.startswith(prefix) and f.suffix == ".jar"]
    if not jar_files:
        print(f"  WARNING: {theme_name} theme JAR not found in {lib_dir}")
        return

    jar_file = jar_files[0]
    jar_prefix = f"META-INF/resources/{theme_name}/"
    theme_dir = bundle_dir / theme_name

    with zipfile.ZipFile(jar_file) as zf:
        for entry in zf.namelist():
            if entry.startswith(jar_prefix) and not entry.endswith("/"):
                rel = entry[len(jar_prefix):]
                dest = theme_dir / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(entry) as src, open(dest, "wb") as dst:
                    dst.write(src.read())

    print(f"  {theme_name.capitalize()} CSS extracted to: {theme_dir}")


def _extract_jar_resources(lib_dir: Path, jar_prefix: str, bundle_dir: Path, label: str) -> None:
    """Extract META-INF/resources/* from a JAR in WEB-INF/lib/ into bundle_dir."""
    if not lib_dir.exists():
        return

    jar_files = [f for f in lib_dir.iterdir() if f.name.startswith(jar_prefix) and f.suffix == ".jar"]
    if not jar_files:
        return

    entry_prefix = "META-INF/resources/"
    with zipfile.ZipFile(jar_files[0]) as zf:
        for entry in zf.namelist():
            if entry.startswith(entry_prefix) and not entry.endswith("/"):
                rel = entry[len(entry_prefix):]
                dest = bundle_dir / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(entry) as src, open(dest, "wb") as dst:
                    dst.write(src.read())

    print(f"  {label} extracted from {jar_files[0].name}")


def generate_and_build(
    app_dir: Path | None = None,
    keep: bool = False,
    vaadin_version: str = _DEFAULT_VAADIN_VERSION,
) -> None:
    """CLI entry point: generate project, build, extract bundle.

    Args:
        app_dir: App package directory (e.g. ``my_app/``).  When *None*,
                 auto-detects pyflow dev tree.
        keep: If *True*, keep ``bundle-project/`` after extraction.
        vaadin_version: Vaadin platform version for the pom.xml.
    """
    is_pyflow_dev = (Path.cwd() / "src" / "vaadin" / "flow").is_dir()

    if is_pyflow_dev:
        project_dir = Path.cwd() / "bundle-project"
        bundle_dir = Path.cwd() / "src" / "vaadin" / "flow" / "bundle"
    elif app_dir:
        project_dir = app_dir / "bundle-project"
        bundle_dir = app_dir / "bundle"
    else:
        print("ERROR: Cannot determine bundle output directory.")
        print("  Run from a pyflow source tree (src/vaadin/flow/ exists)")
        print("  or specify an app module: vaadin <app_module> --bundle")
        sys.exit(1)

    print("===================================================")
    print("  Vaadin PyFlow Bundle Generator")
    print("===================================================")
    print(f"  Vaadin version: {vaadin_version}")
    print(f"  Project dir:    {project_dir}")
    print(f"  Bundle output:  {bundle_dir}")
    print()

    if project_dir.exists():
        # Reuse existing Maven project — only update FakeView.java
        print("  Reusing existing Maven project in bundle-project/")
        registry = discover_java_components()
        java_dir = project_dir / "src" / "main" / "java" / "com" / "vaadin" / "pyflow"
        (java_dir / "FakeView.java").write_text(generate_fake_view(registry))
        print()
        build_and_extract(project_dir, bundle_dir, clean=False)
    else:
        generate_project(project_dir, vaadin_version)
        print()
        build_and_extract(project_dir, bundle_dir, clean=True)

    if not keep:
        shutil.rmtree(project_dir)
        print(f"  Cleaned up {project_dir}")

    print()
    print("===================================================")
    print("  Bundle generated successfully!")
    print("===================================================")
