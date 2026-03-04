"""Generate or copy the frontend bundle for PyXFlow.

Two modes:

1. **copy** (default) -- extract pre-built bundle from Vaadin Maven JARs
   in ``~/.m2/repository/``.  Instant (seconds), no Java/Maven build needed.

2. **build** -- generate a Maven project, run a full Vite production build,
   and extract the bundle from the resulting WAR.

Usage (via CLI)::

    # Copy from Maven JARs (fast, default)
    pyxflow bundle                            # → src/pyxflow/bundle/
    pyxflow bundle --copy                     # explicit
    pyxflow bundle --vaadin-version 25.0.6    # pin version

    # Full Maven build
    pyxflow bundle --build                    # → src/pyxflow/bundle/
    pyxflow bundle --build --keep             # keep bundle-project/

    # User project
    pyxflow my_app bundle                     # → my_app/bundle/
"""

import os
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path


def _read_pyproject_version() -> str:
    """Read Vaadin version from pyproject.toml [tool.pyxflow] section."""
    pyproject = Path(__file__).parent.parent.parent / "pyproject.toml"
    if not pyproject.is_file():
        # Fallback: look relative to package install location
        pyproject = Path(__file__).parent / "pyproject.toml"
    vaadin_ver = "25.0.6"
    if pyproject.is_file():
        in_section = False
        for line in pyproject.read_text().splitlines():
            stripped = line.strip()
            if stripped == "[tool.pyxflow]":
                in_section = True
                continue
            if in_section and stripped.startswith("["):
                break
            if in_section and "=" in stripped:
                key, _, val = stripped.partition("=")
                val = val.strip().strip('"')
                if key.strip() == "vaadin-version":
                    vaadin_ver = val
    return vaadin_ver


_DEFAULT_VAADIN_VERSION = _read_pyproject_version()


def _resolve_flow_version(vaadin_version: str) -> str:
    """Resolve the Flow version from the vaadin-spring-bom POM.

    Looks up ``vaadin-spring-bom-<vaadin_version>.pom`` in
    ``~/.m2/repository/``.  If not found locally, downloads from Maven
    Central.  Parses ``<properties><flow.version>`` from the POM XML.
    """
    group_path = "com/vaadin"
    artifact = "vaadin-spring-bom"
    pom_dir = _m2_repo() / group_path / artifact / vaadin_version
    pom_path = pom_dir / f"{artifact}-{vaadin_version}.pom"

    if not pom_path.is_file():
        pom_path = _download_pom(group_path, artifact, vaadin_version)

    return _parse_flow_version(pom_path)


def _download_pom(group_path: str, artifact: str, version: str) -> Path:
    """Download a POM from Maven Central into ~/.m2/repository/.

    Returns the local path to the downloaded POM.
    """
    import urllib.request
    import urllib.error

    pom_dir = _m2_repo() / group_path / artifact / version
    pom_path = pom_dir / f"{artifact}-{version}.pom"

    group_url = group_path.replace(os.sep, "/")
    url = f"https://repo1.maven.org/maven2/{group_url}/{artifact}/{version}/{artifact}-{version}.pom"

    print(f"  Downloading {artifact}-{version}.pom ...", end="", flush=True)
    try:
        with urllib.request.urlopen(url) as resp:
            data = resp.read()
            pom_dir.mkdir(parents=True, exist_ok=True)
            pom_path.write_bytes(data)
            print(f" ({len(data) / 1024:.1f} KB)")
    except urllib.error.HTTPError as e:
        print(f" FAILED")
        print(f"\n  ERROR: HTTP {e.code} downloading {url}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f" FAILED")
        print(f"\n  ERROR: {e.reason}")
        sys.exit(1)

    return pom_path


def _parse_flow_version(pom_path: Path) -> str:
    """Parse <flow.version> from a Maven POM's <properties> section."""
    tree = ET.parse(pom_path)
    root = tree.getroot()
    # Maven POM uses a namespace
    ns = {"m": "http://maven.apache.org/POM/4.0.0"}
    flow_ver = root.findtext("m:properties/m:flow.version", namespaces=ns)
    if not flow_ver:
        # Try without namespace (some POMs omit it)
        flow_ver = root.findtext("properties/flow.version")
    if not flow_ver:
        print(f"  ERROR: <flow.version> not found in {pom_path}")
        sys.exit(1)
    return flow_ver


def generate_pom_xml(vaadin_version: str, *, optimize_bundle: bool = True) -> str:
    """Minimal pom.xml: WAR packaging, vaadin-core, vaadin-maven-plugin."""
    optimize_str = "true" if optimize_bundle else "false"
    return f"""\
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.vaadin.pyxflow</groupId>
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
                        <configuration>
                            <optimizeBundle>{optimize_str}</optimizeBundle>
                        </configuration>
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

    Imports pyxflow.components (which imports all component modules),
    then walks the Component class hierarchy collecting _v_fqcn values.
    Returns {PythonClassName: JavaFQCN}.
    """
    from pyxflow.core.component import Component
    import pyxflow.components  # noqa: F401 — triggers all component imports

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
package com.vaadin.pyxflow;

{imports_str}

@Push
@Route("")
@JsModule("./pyxflow-bundle.js")
{uses_str}
public class FakeView extends Div {{
}}
"""


def generate_feature_flags() -> str:
    """Feature flags for experimental components (e.g. MasterDetailLayout)."""
    return "com.vaadin.experimental.masterDetailLayoutComponent=true\n"


def generate_project(output_dir: Path, vaadin_version: str, *, optimized: bool = True) -> None:
    """Create a complete Maven project in output_dir."""
    registry = discover_java_components()

    # Clean and create directories
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    java_dir = output_dir / "src" / "main" / "java" / "com" / "vaadin" / "pyxflow"
    java_dir.mkdir(parents=True)

    resources_dir = output_dir / "src" / "main" / "resources"
    resources_dir.mkdir(parents=True)

    # pom.xml
    (output_dir / "pom.xml").write_text(generate_pom_xml(vaadin_version, optimize_bundle=optimized))

    # FakeView.java
    (java_dir / "FakeView.java").write_text(
        generate_fake_view(registry)
    )

    # frontend/pyxflow-bundle.js — triggers Vaadin's frontend build
    frontend_dir = output_dir / "frontend"
    frontend_dir.mkdir()
    (frontend_dir / "pyxflow-bundle.js").write_text("// marker for Vaadin bundle build\n")

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


def _m2_repo() -> Path:
    """Return the local Maven repository root (~/.m2/repository)."""
    return Path.home() / ".m2" / "repository"


def _find_m2_jar(group_path: str, artifact: str, version: str) -> Path | None:
    """Locate a JAR in the local Maven repository.

    Args:
        group_path: e.g. ``"com/vaadin"``
        artifact: e.g. ``"vaadin-prod-bundle"``
        version: e.g. ``"25.0.6"``

    Returns the Path if the JAR exists, else *None*.
    """
    jar = _m2_repo() / group_path / artifact / version / f"{artifact}-{version}.jar"
    return jar if jar.is_file() else None


def _download_jar(group_path: str, artifact: str, version: str) -> Path:
    """Download a JAR from Maven Central into ~/.m2/repository/.

    Returns the local path to the downloaded JAR.
    Raises SystemExit on failure.
    """
    import urllib.request
    import urllib.error

    jar_dir = _m2_repo() / group_path / artifact / version
    jar_path = jar_dir / f"{artifact}-{version}.jar"

    # Maven Central URL
    group_url = group_path.replace(os.sep, "/")
    url = f"https://repo1.maven.org/maven2/{group_url}/{artifact}/{version}/{artifact}-{version}.jar"

    print(f"  Downloading {artifact}-{version}.jar ...", end="", flush=True)
    try:
        with urllib.request.urlopen(url) as resp:
            data = resp.read()
            size_mb = len(data) / 1024 / 1024
            jar_dir.mkdir(parents=True, exist_ok=True)
            jar_path.write_bytes(data)
            print(f" ({size_mb:.1f} MB)")
    except urllib.error.HTTPError as e:
        print(f" FAILED")
        print(f"\n  ERROR: HTTP {e.code} downloading {url}")
        print(f"  Check that the artifact and version exist on Maven Central.")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f" FAILED")
        print(f"\n  ERROR: {e.reason}")
        print(f"  URL: {url}")
        sys.exit(1)

    return jar_path


def _extract_jar_to(jar_path: Path, prefix: str, dest_dir: Path, *, strip_prefix: str = "") -> int:
    """Extract files from *jar_path* whose names start with *prefix*.

    Args:
        jar_path: Path to the JAR file.
        prefix: Only extract entries starting with this.
        dest_dir: Root directory to write into.
        strip_prefix: Remove this prefix from entry names before writing.
            Defaults to *prefix* itself.

    Returns the number of files extracted.
    """
    if not strip_prefix:
        strip_prefix = prefix
    count = 0
    with zipfile.ZipFile(jar_path) as zf:
        for entry in zf.namelist():
            if entry.startswith(prefix) and not entry.endswith("/"):
                rel = entry[len(strip_prefix):]
                dest = dest_dir / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(entry) as src, open(dest, "wb") as dst:
                    dst.write(src.read())
                count += 1
    return count


def copy_from_jars(
    bundle_dir: Path,
    vaadin_version: str = _DEFAULT_VAADIN_VERSION,
    *,
    optimized: bool = False,
) -> None:
    """Extract a complete bundle from pre-built Vaadin Maven JARs.

    This is much faster than a full Maven build and produces the exact same
    files.  Requires the JARs to be present in ``~/.m2/repository/``.
    """
    flow_version = _resolve_flow_version(vaadin_version)

    # --- Locate all 4 JARs (download if missing) -----------------------------
    specs = [
        ("prod-bundle", "vaadin-prod-bundle", vaadin_version),
        ("flow-push", "flow-push", flow_version),
        ("lumo-theme", "vaadin-lumo-theme", vaadin_version),
        ("aura-theme", "vaadin-aura-theme", vaadin_version),
    ]
    found: dict[str, Path] = {}
    for label, artifact, ver in specs:
        jar = _find_m2_jar("com/vaadin", artifact, ver)
        if jar is None:
            jar = _download_jar("com/vaadin", artifact, ver)
        found[label] = jar

    # --- Clean existing bundle ------------------------------------------------
    vaadin_dir = bundle_dir / "VAADIN"
    if vaadin_dir.exists():
        shutil.rmtree(vaadin_dir)
    for theme in ("lumo", "aura"):
        d = bundle_dir / theme
        if d.exists():
            shutil.rmtree(d)
    bundle_dir.mkdir(parents=True, exist_ok=True)

    # --- Extract prod-bundle -------------------------------------------------
    prod_jar = found["prod-bundle"]
    if optimized:
        prefix = "vaadin-prod-bundle/webapp/"
    else:
        prefix = "vaadin-prod-bundle-unoptimized/webapp/"
    n = _extract_jar_to(prod_jar, prefix, bundle_dir)
    print(f"  prod-bundle: {n} files from {prod_jar.name}")

    # --- Extract flow-push (push scripts) -------------------------------------
    push_jar = found["flow-push"]
    n = _extract_jar_to(push_jar, "META-INF/resources/", bundle_dir, strip_prefix="META-INF/resources/")
    print(f"  flow-push:   {n} files from {push_jar.name}")

    # --- Extract Lumo theme ---------------------------------------------------
    lumo_jar = found["lumo-theme"]
    n = _extract_jar_to(lumo_jar, "META-INF/resources/lumo/", bundle_dir, strip_prefix="META-INF/resources/")
    print(f"  lumo-theme:  {n} files from {lumo_jar.name}")

    # --- Extract Aura theme ---------------------------------------------------
    aura_jar = found["aura-theme"]
    n = _extract_jar_to(aura_jar, "META-INF/resources/aura/", bundle_dir, strip_prefix="META-INF/resources/")
    print(f"  aura-theme:  {n} files from {aura_jar.name}")

    # --- Write version marker ---------------------------------------------------
    (bundle_dir / "VAADIN").mkdir(parents=True, exist_ok=True)
    (bundle_dir / "VAADIN" / "version").write_text(vaadin_version)

    # --- Report ---------------------------------------------------------------
    js_size = sum(f.stat().st_size for f in bundle_dir.rglob("*.js"))
    css_size = sum(f.stat().st_size for f in bundle_dir.rglob("*.css"))
    print()
    print(f"  JavaScript: {js_size / 1024 / 1024:.2f} MB")
    print(f"  CSS: {css_size / 1024:.1f} KB")
    print(f"  Bundle extracted to: {bundle_dir}")


def generate_and_build(
    app_dir: Path | None = None,
    keep: bool = False,
    vaadin_version: str = _DEFAULT_VAADIN_VERSION,
    *,
    optimized: bool = True,
) -> None:
    """CLI entry point: generate project, build, extract bundle.

    Args:
        app_dir: App package directory (e.g. ``my_app/``).  When *None*,
                 auto-detects pyxflow dev tree.
        keep: If *True*, keep ``bundle-project/`` after extraction.
        vaadin_version: Vaadin platform version for the pom.xml.
        optimized: If *True* (default), Vite produces code-split chunks.
                   If *False*, produces a single monolithic JS file.
    """
    is_pyxflow_dev = (Path.cwd() / "src" / "pyxflow").is_dir()

    if is_pyxflow_dev:
        project_dir = Path.cwd() / "bundle-project"
        bundle_dir = Path.cwd() / "src" / "pyxflow" / "bundle"
    elif app_dir:
        project_dir = app_dir / "bundle-project"
        bundle_dir = app_dir / "bundle"
    else:
        print("ERROR: Cannot determine bundle output directory.")
        print("  Run from a pyxflow source tree (src/pyxflow/ exists)")
        print("  or specify an app module: pyxflow <app_module> --bundle")
        sys.exit(1)

    print("===================================================")
    print("  Vaadin PyXFlow Bundle Generator")
    print("===================================================")
    print(f"  Vaadin version: {vaadin_version}")
    print(f"  Project dir:    {project_dir}")
    print(f"  Bundle output:  {bundle_dir}")
    print()

    if project_dir.exists():
        # Reuse existing Maven project — only update FakeView.java
        print("  Reusing existing Maven project in bundle-project/")
        registry = discover_java_components()
        java_dir = project_dir / "src" / "main" / "java" / "com" / "vaadin" / "pyxflow"
        (java_dir / "FakeView.java").write_text(generate_fake_view(registry))
        print()
        build_and_extract(project_dir, bundle_dir, clean=False)
    else:
        generate_project(project_dir, vaadin_version, optimized=optimized)
        print()
        build_and_extract(project_dir, bundle_dir, clean=True)

    # Write version marker
    (bundle_dir / "VAADIN").mkdir(parents=True, exist_ok=True)
    (bundle_dir / "VAADIN" / "version").write_text(vaadin_version)

    if not keep:
        shutil.rmtree(project_dir)
        print(f"  Cleaned up {project_dir}")

    print()
    print("===================================================")
    print("  Bundle generated successfully!")
    print("===================================================")
