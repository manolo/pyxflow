#!/usr/bin/env python3
"""Generate MCP documentation content from PyXFlow source code.

Scans source modules via import + inspect to produce markdown/JSON
files under docs/mcp/ that are served via GitHub Pages and consumed
by the MCP Cloudflare Worker.

Usage:
    cd pyxflow && python -m scripts.build_mcp_content
"""

import importlib
import inspect
import json
import os
import re
import shutil
import sys
import textwrap
from enum import Enum
from pathlib import Path
from typing import Any

# Ensure pyxflow is importable
ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))
sys.path.insert(0, str(ROOT))

OUT = ROOT / "docs" / "mcp"

# ---------------------------------------------------------------------------
#  Component metadata: name -> (module_path, category, description)
# ---------------------------------------------------------------------------

COMPONENT_CATEGORIES = {
    # Layout & Containers
    "AppLayout": ("app_layout", "Layout", "Application shell with navbar/drawer"),
    "FlexLayout": ("flex_layout", "Layout", "Flexible CSS layout"),
    "HorizontalLayout": ("horizontal_layout", "Layout", "Horizontal flex container with spacing"),
    "VerticalLayout": ("vertical_layout", "Layout", "Vertical flex container with spacing"),
    "FormLayout": ("form_layout", "Layout", "Responsive form layout with label positioning"),
    "SplitLayout": ("split_layout", "Layout", "Resizable split panel"),
    "MasterDetailLayout": ("master_detail_layout", "Layout", "Responsive master-detail with drawer"),
    "Details": ("details", "Layout", "Collapsible content panel"),
    "Accordion": ("accordion", "Layout", "Vertically stacked collapsible panels"),
    "Card": ("card", "Layout", "Content card with optional media/actions"),
    "Scroller": ("scroller", "Layout", "Scrollable content container"),
    "TabSheet": ("tab_sheet", "Layout", "Tab-based content switcher"),
    "Popover": ("popover", "Layout", "Popup content anchored to a target"),
    "Dialog": ("dialog", "Overlay", "Modal dialog window"),
    "ConfirmDialog": ("confirm_dialog", "Overlay", "Pre-built confirmation dialog"),

    # Input Fields
    "TextField": ("text_field", "Input", "Single-line text input"),
    "TextArea": ("text_area", "Input", "Multi-line text input"),
    "NumberField": ("number_field", "Input", "Numeric input with step buttons"),
    "IntegerField": ("number_field", "Input", "Integer-only input"),
    "PasswordField": ("password_field", "Input", "Password input with reveal toggle"),
    "EmailField": ("email_field", "Input", "Email input with validation"),
    "DatePicker": ("date_picker", "Input", "Date selection with calendar popup"),
    "TimePicker": ("time_picker", "Input", "Time selection"),
    "DateTimePicker": ("date_time_picker", "Input", "Combined date and time picker"),
    "Select": ("select", "Input", "Dropdown selection (single value)"),
    "ComboBox": ("combo_box", "Input", "Searchable dropdown with type-ahead"),
    "MultiSelectComboBox": ("multi_select_combo_box", "Input", "Multi-value searchable dropdown"),
    "RadioButtonGroup": ("radio_button_group", "Input", "Radio button group"),
    "CheckboxGroup": ("checkbox_group", "Input", "Checkbox group for multiple selection"),
    "Checkbox": ("checkbox", "Input", "Single checkbox toggle"),
    "CustomField": ("custom_field", "Input", "Wrapper for custom field compositions"),

    # Data
    "Grid": ("grid", "Data", "Data table with sorting, selection, lazy loading"),
    "TreeGrid": ("grid", "Data", "Hierarchical data grid"),
    "VirtualList": ("virtual_list", "Data", "Virtualized list for large datasets"),

    # Navigation
    "Tabs": ("tabs", "Navigation", "Horizontal/vertical tab bar"),
    "Tab": ("tabs", "Navigation", "Individual tab within Tabs"),
    "RouterLink": ("router_link", "Navigation", "Client-side navigation link"),
    "SideNav": ("side_nav", "Navigation", "Vertical navigation menu"),
    "SideNavItem": ("side_nav", "Navigation", "Item within SideNav"),
    "DrawerToggle": ("drawer_toggle", "Navigation", "Toggle button for AppLayout drawer"),
    "MenuBar": ("menu_bar", "Navigation", "Horizontal menu with dropdowns"),
    "ContextMenu": ("context_menu", "Navigation", "Right-click context menu"),

    # Display
    "Button": ("button", "Action", "Clickable button"),
    "Icon": ("icon", "Display", "Vaadin/Lumo icon"),
    "ProgressBar": ("progress_bar", "Display", "Progress indicator"),
    "Avatar": ("avatar", "Display", "User avatar image/initials"),
    "AvatarGroup": ("avatar", "Display", "Group of overlapping avatars"),
    "Notification": ("notification", "Feedback", "Toast notification"),
    "Markdown": ("markdown", "Display", "Markdown renderer"),
    "Upload": ("upload", "Input", "File upload component"),
    "LoginForm": ("login", "Authentication", "Inline login form"),
    "LoginOverlay": ("login", "Authentication", "Login dialog overlay"),
    "MessageList": ("message_list", "Display", "Chat message list"),
    "MessageInput": ("message_input", "Input", "Chat message input"),
    "ListBox": ("list_box", "Input", "Scrollable single-select list"),
    "MultiSelectListBox": ("list_box", "Input", "Scrollable multi-select list"),

    # HTML elements
    "Div": ("html", "HTML", "Generic <div> container"),
    "Span": ("span", "HTML", "Inline <span> element"),
    "H1": ("html", "HTML", "Heading level 1"),
    "H2": ("html", "HTML", "Heading level 2"),
    "H3": ("html", "HTML", "Heading level 3"),
    "H4": ("html", "HTML", "Heading level 4"),
    "H5": ("html", "HTML", "Heading level 5"),
    "H6": ("html", "HTML", "Heading level 6"),
    "Paragraph": ("html", "HTML", "Paragraph element"),
    "Pre": ("html", "HTML", "Preformatted text"),
    "Header": ("html", "HTML", "Semantic header"),
    "Footer": ("html", "HTML", "Semantic footer"),
    "Section": ("html", "HTML", "Semantic section"),
    "Nav": ("html", "HTML", "Navigation section"),
    "Main": ("html", "HTML", "Main content area"),
    "Article": ("html", "HTML", "Article section"),
    "Aside": ("html", "HTML", "Sidebar content"),
    "Hr": ("html", "HTML", "Horizontal rule"),
    "Anchor": ("html", "HTML", "Hyperlink element"),
    "IFrame": ("html", "HTML", "Inline frame"),
    "Image": ("html", "HTML", "Image element"),
    "NativeLabel": ("html", "HTML", "Native <label> element"),
}

# Support classes documented alongside their parent component
SUPPORT_CLASSES = {
    "Column": "Grid",
    "ColumnGroup": "Grid",
    "HeaderRow": "Grid",
    "HeaderCell": "Grid",
    "GridSortOrder": "Grid",
    "EditorImpl": "Grid",
    "FormItem": "FormLayout",
    "FormRow": "FormLayout",
    "ResponsiveStep": "FormLayout",
    "AccordionPanel": "Accordion",
    "AvatarGroupItem": "AvatarGroup",
    "MenuItem": "MenuBar",
    "ContextMenuItem": "ContextMenu",
    "SideNavItem": "SideNav",
    "MessageListItem": "MessageList",
}

# Renderers documented separately
RENDERER_CLASSES = ["LitRenderer", "TextRenderer", "ComponentRenderer"]


def _to_kebab(name: str) -> str:
    """Convert PascalCase to kebab-case: TextField -> text-field."""
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", name).lower()


def _public_methods(cls) -> list[tuple[str, inspect.Signature, str]]:
    """Return (name, signature, docstring) for public methods defined on cls."""
    methods = []
    for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
        if name.startswith("_"):
            continue
        # Only methods defined directly on cls (not inherited from Component/object)
        if name in ("add", "remove", "remove_all") and cls.__name__ not in ("Notification", "Dialog"):
            # Skip inherited layout methods unless overridden
            if name not in cls.__dict__:
                continue
        try:
            sig = inspect.signature(method)
        except (ValueError, TypeError):
            sig = None
        doc = inspect.getdoc(method) or ""
        methods.append((name, sig, doc))
    return sorted(methods, key=lambda x: x[0])


def _get_constructor_sig(cls) -> str:
    """Get readable constructor signature."""
    try:
        sig = inspect.signature(cls.__init__)
        # Remove 'self' parameter
        params = list(sig.parameters.values())[1:]
        parts = []
        for p in params:
            if p.default is inspect.Parameter.empty:
                parts.append(f"{p.name}: {_format_annotation(p.annotation)}")
            else:
                default = repr(p.default) if not isinstance(p.default, str) else f'"{p.default}"'
                if default == "''":
                    default = '""'
                parts.append(f"{p.name}: {_format_annotation(p.annotation)} = {default}")
        return f"{cls.__name__}({', '.join(parts)})"
    except (ValueError, TypeError):
        return f"{cls.__name__}()"


def _format_annotation(ann) -> str:
    """Format type annotation to readable string."""
    if ann is inspect.Parameter.empty:
        return "Any"
    if isinstance(ann, str):
        return ann
    if hasattr(ann, "__name__"):
        return ann.__name__
    return str(ann).replace("typing.", "")


def _get_mixins(cls) -> list[str]:
    """Get mixin class names (HasReadOnly, HasValidation, HasRequired)."""
    mixin_names = []
    for base in cls.__mro__:
        if base.__name__ in ("HasReadOnly", "HasValidation", "HasRequired"):
            mixin_names.append(base.__name__)
    return mixin_names


def _get_variant_enum(component_name: str) -> type | None:
    """Find the variant enum for a component."""
    from pyxflow.components import constants
    variant_name = f"{component_name}Variant"
    return getattr(constants, variant_name, None)


# ---------------------------------------------------------------------------
#  Generators
# ---------------------------------------------------------------------------

def generate_primer():
    """Generate primer.md -- PyXFlow overview."""
    import pyxflow
    version = pyxflow.__version__
    component_count = len(COMPONENT_CATEGORIES)

    # Build import list for primer
    from pyxflow.components import __all__ as comp_all

    content = f"""\
# PyXFlow - Python Server-Side UI Framework

**Version:** {version} | **Components:** {component_count}+ | **Python 3.10+**

PyXFlow is a Python port of Vaadin Flow. It lets you build reactive web UIs
entirely in Python -- no JavaScript, HTML, or CSS required. The browser runs
Vaadin web components; your Python code controls them via a WebSocket/HTTP
protocol.

## Quick Start

```bash
pip install pyxflow
```

Create `app.py`:

```python
from pyxflow import Route, FlowApp
from pyxflow.components import VerticalLayout, TextField, Button, Notification

@Route("")
class HelloView(VerticalLayout):
    def __init__(self):
        name = TextField("Your name")
        self.add(
            name,
            Button("Greet", lambda e: Notification.show(f"Hello {{name.value}}!")),
        )

FlowApp("app").run()
```

Run it:

```bash
python app.py
# Open http://localhost:8080
```

## Key Concepts

### Views are Python classes
Every view is a `Component` subclass decorated with `@Route("path")`.
Views are instantiated per browser session.

### Components map to Vaadin web components
`Button`, `TextField`, `Grid`, etc. are thin Python wrappers around
`<vaadin-button>`, `<vaadin-text-field>`, `<vaadin-grid>`.

### No templates -- build UI in `__init__`
```python
@Route("example")
class MyView(VerticalLayout):
    def __init__(self):
        self.add(H1("Title"), Paragraph("Content"))
```

### Events are Python callbacks
```python
button = Button("Click me", lambda e: Notification.show("Clicked!"))
# Or:
button.add_click_listener(self.on_click)
```

### Data binding with Binder
```python
from pyxflow.data import Binder
binder = Binder(Person)
binder.for_field(name_field).as_required("Name required").bind(
    lambda p: p.name, lambda p, v: setattr(p, "name", v))
binder.read_bean(person)
binder.write_bean(person)  # Validates + writes
```

### Server push for async updates
```python
import asyncio

@Route("live")
@Push
class LiveView(VerticalLayout):
    def __init__(self):
        self.label = Span("0")
        self.add(self.label, Button("Start", self.start))

    def start(self, e):
        asyncio.create_task(self.update_loop())

    async def update_loop(self):
        ui = self.get_ui()
        for i in range(100):
            await asyncio.sleep(1)
            ui.access(lambda: self.label.set_text(str(i)))
```

## Imports

```python
# Core
from pyxflow import Route, RouteAlias, Menu, FlowApp, Push, AppShell
from pyxflow import ColorScheme, StyleSheet, PageTitle, BeforeEnterEvent
from pyxflow import Component, Element, Location, QueryParameters, RouteParameters
from pyxflow import Request, Response  # HTTP request/response context

# Components (use what you need)
from pyxflow.components import Button, TextField, Grid, Dialog, Notification
from pyxflow.components import VerticalLayout, HorizontalLayout, FormLayout
# ... all {component_count}+ components available

# Data binding
from pyxflow.data import Binder, ValidationError
from pyxflow.data import ListDataProvider, DataProvider

# Constants & Enums
from pyxflow.components import ButtonVariant, GridVariant, SelectionMode
from pyxflow.components import FlexDirection, JustifyContentMode, Alignment
```

## Component Categories

| Category | Components |
|----------|-----------|
| Layout | AppLayout, VerticalLayout, HorizontalLayout, FlexLayout, FormLayout, SplitLayout, MasterDetailLayout, Card, Details, Accordion, Scroller, TabSheet, Popover |
| Input | TextField, TextArea, NumberField, IntegerField, PasswordField, EmailField, DatePicker, TimePicker, DateTimePicker, Select, ComboBox, MultiSelectComboBox, RadioButtonGroup, CheckboxGroup, Checkbox, CustomField, Upload, MessageInput, ListBox, MultiSelectListBox |
| Data | Grid, TreeGrid, VirtualList |
| Navigation | Tabs, Tab, RouterLink, SideNav, MenuBar, ContextMenu, DrawerToggle |
| Overlay | Dialog, ConfirmDialog, Notification |
| Display | Button, Icon, ProgressBar, Avatar, AvatarGroup, Markdown, MessageList |
| Auth | LoginForm, LoginOverlay |
| HTML | Div, Span, H1-H6, Paragraph, Pre, Header, Footer, Section, Nav, Anchor, Image, Hr |

## Common Patterns

- **Routing:** `@Route("path/:param?")` with `before_enter(self, event)` for URL params
- **App Layout:** `@AppShell` on layout class with `AppLayout` + `SideNav`
- **Forms:** `FormLayout` + `Binder` + field validation
- **Grids:** `Grid` with lazy `DataProvider` or `set_items()`, `LitRenderer` for custom cells
- **Push:** `@Push` + `asyncio.create_task()` + `ui.access(callback)` for live updates
- **Theming:** `@ColorScheme("dark")`, `@StyleSheet("styles.css")`, `ButtonVariant.LUMO_PRIMARY`
- **@ClientCallable:** Decorate methods to call from client JS
- **Request/Response:** `Request.get_current()` / `Response.get_current()` for cookies/headers
"""

    (OUT / "primer.md").write_text(content)
    print(f"  primer.md ({len(content)} bytes)")


def generate_components_json():
    """Generate components.json -- component inventory."""
    components = []
    for name, (module, category, description) in sorted(COMPONENT_CATEGORIES.items()):
        components.append({
            "name": name,
            "file": f"components/{_to_kebab(name)}.md",
            "category": category,
            "description": description,
        })
    data = {"count": len(components), "components": components}
    text = json.dumps(data, indent=2)
    (OUT / "components.json").write_text(text)
    print(f"  components.json ({len(components)} components)")


def generate_component_doc(name: str, module_name: str, category: str, description: str):
    """Generate a single component markdown doc."""
    try:
        mod = importlib.import_module(f"pyxflow.components.{module_name}")
    except ImportError as e:
        print(f"    SKIP {name}: {e}")
        return

    cls = getattr(mod, name, None)
    if cls is None:
        # Try components __init__
        import pyxflow.components as comp_mod
        cls = getattr(comp_mod, name, None)
    if cls is None:
        print(f"    SKIP {name}: class not found in {module_name}")
        return

    lines = [f"# {name}\n"]
    lines.append(f"**Category:** {category} | {description}\n")

    # Constructor
    lines.append("## Constructor\n")
    lines.append(f"```python\n{_get_constructor_sig(cls)}\n```\n")

    # Mixins
    mixins = _get_mixins(cls)
    if mixins:
        lines.append(f"**Mixins:** {', '.join(mixins)}\n")
        mixin_methods = []
        if "HasReadOnly" in mixins:
            mixin_methods.extend(["set_read_only(bool)", "is_read_only()"])
        if "HasValidation" in mixins:
            mixin_methods.extend(["set_invalid(bool)", "is_invalid()", "set_error_message(str)", "get_error_message()"])
        if "HasRequired" in mixins:
            mixin_methods.extend(["set_required_indicator_visible(bool)", "is_required_indicator_visible()"])
        lines.append("Mixin methods: " + ", ".join(f"`{m}`" for m in mixin_methods) + "\n")

    # Public methods
    methods = _public_methods(cls)
    if methods:
        lines.append("## Methods\n")
        lines.append("| Method | Description |")
        lines.append("|--------|-------------|")
        for mname, sig, doc in methods:
            sig_str = str(sig).replace("(self, ", "(").replace("(self)", "()") if sig else "()"
            # Truncate long sigs
            if len(sig_str) > 60:
                sig_str = sig_str[:57] + "..."
            first_line = doc.split("\n")[0] if doc else ""
            lines.append(f"| `{mname}{sig_str}` | {first_line} |")
        lines.append("")

    # Theme variants
    variant_enum = _get_variant_enum(name)
    if variant_enum:
        lines.append("## Theme Variants\n")
        lines.append(f"```python\nfrom pyxflow.components import {variant_enum.__name__}\n```\n")
        lines.append("| Variant | Value |")
        lines.append("|---------|-------|")
        for member in variant_enum:
            lines.append(f"| `{variant_enum.__name__}.{member.name}` | `\"{member.value}\"` |")
        lines.append("")

    # Support classes
    support = [sc for sc, parent in SUPPORT_CLASSES.items() if parent == name]
    if support:
        lines.append("## Related Classes\n")
        for sc in support:
            sc_cls = getattr(mod, sc, None)
            if sc_cls is None:
                import pyxflow.components as comp_mod
                sc_cls = getattr(comp_mod, sc, None)
            if sc_cls:
                lines.append(f"### {sc}\n")
                lines.append(f"```python\n{_get_constructor_sig(sc_cls)}\n```\n")
                sc_methods = _public_methods(sc_cls)
                if sc_methods:
                    lines.append("| Method | Description |")
                    lines.append("|--------|-------------|")
                    for mname, sig, doc in sc_methods:
                        sig_str = str(sig).replace("(self, ", "(").replace("(self)", "()") if sig else "()"
                        if len(sig_str) > 60:
                            sig_str = sig_str[:57] + "..."
                        first_line = doc.split("\n")[0] if doc else ""
                        lines.append(f"| `{mname}{sig_str}` | {first_line} |")
                    lines.append("")

    content = "\n".join(lines)
    filename = _to_kebab(name) + ".md"
    (OUT / "components" / filename).write_text(content)


def generate_all_component_docs():
    """Generate docs for all components."""
    (OUT / "components").mkdir(parents=True, exist_ok=True)
    for name, (module, category, desc) in sorted(COMPONENT_CATEGORIES.items()):
        generate_component_doc(name, module, category, desc)
    print(f"  components/*.md ({len(COMPONENT_CATEGORIES)} files)")


def generate_examples():
    """Generate example files from demo views."""
    (OUT / "examples").mkdir(parents=True, exist_ok=True)

    demo_dir = ROOT / "demo" / "views"
    count = 0

    example_map = {
        "hello_view.py": ("hello", "Hello World", "Simplest PyXFlow view -- text input + button + notification"),
        "grid_view.py": ("grid", "Grid with Lazy Data", "Grid with lazy data provider, sorting, and selection"),
        "crud_view.py": ("crud", "CRUD with Binder", "Full CRUD with Grid, Binder, URL routing, and ConfirmDialog"),
        "master_detail_view.py": ("master-detail", "Master-Detail", "Master-detail pattern with SplitLayout and Binder"),
        "push_demo_view.py": ("push", "WebSocket Push", "Stopwatch using asyncio + UI.access() for live updates"),
        "dialog_demo_view.py": ("dialog", "Dialog Examples", "Various dialog patterns"),
        "main_layout.py": ("app-layout", "App Layout", "Application shell with AppLayout, SideNav, and @Menu"),
    }

    for filename, (slug, title, desc) in example_map.items():
        filepath = demo_dir / filename
        if not filepath.exists():
            continue
        source = filepath.read_text()
        content = f"# Example: {title}\n\n{desc}\n\n```python\n{source}```\n"
        (OUT / "examples" / f"{slug}.md").write_text(content)
        count += 1

    print(f"  examples/*.md ({count} files)")


def generate_constants():
    """Generate constants documentation."""
    (OUT / "constants").mkdir(parents=True, exist_ok=True)
    from pyxflow.components import constants as const_mod

    all_enums = []
    for name in sorted(dir(const_mod)):
        obj = getattr(const_mod, name)
        if isinstance(obj, type) and issubclass(obj, Enum) and obj is not Enum:
            all_enums.append((name, obj))

    # Categorize
    categories = {
        "layout": [],
        "grid": [],
        "field": [],
        "variants": [],
    }

    for name, enum_cls in all_enums:
        if name.endswith("Variant"):
            categories["variants"].append((name, enum_cls))
        elif name in ("FlexDirection", "FlexWrap", "JustifyContentMode", "ContentAlignment",
                       "Alignment", "Orientation", "ScrollDirection", "PopoverPosition",
                       "AppLayoutSection"):
            categories["layout"].append((name, enum_cls))
        elif name in ("SortDirection", "SelectionMode", "ColumnTextAlign", "GridDropMode",
                       "AutoExpandMode"):
            categories["grid"].append((name, enum_cls))
        elif name in ("ValueChangeMode", "Autocomplete"):
            categories["field"].append((name, enum_cls))
        else:
            categories["layout"].append((name, enum_cls))

    def _write_enum_file(filename: str, title: str, enums: list):
        lines = [f"# {title}\n"]
        for name, enum_cls in enums:
            doc = inspect.getdoc(enum_cls) or ""
            lines.append(f"## {name}\n")
            if doc:
                lines.append(f"{doc}\n")
            lines.append(f"```python\nfrom pyxflow.components import {name}\n```\n")
            lines.append("| Name | Value |")
            lines.append("|------|-------|")
            for member in enum_cls:
                lines.append(f"| `{name}.{member.name}` | `\"{member.value}\"` |")
            lines.append("")
        content = "\n".join(lines)
        (OUT / "constants" / filename).write_text(content)

    _write_enum_file("layout.md", "Layout Constants", categories["layout"])
    _write_enum_file("grid.md", "Grid Constants", categories["grid"])
    _write_enum_file("field.md", "Field Constants", categories["field"])
    _write_enum_file("variants.md", "Theme Variants", categories["variants"])

    # all.md -- everything
    lines = ["# All Constants & Enums\n"]
    for name, enum_cls in all_enums:
        lines.append(f"## {name}\n")
        lines.append(f"```python\nfrom pyxflow.components import {name}\n```\n")
        lines.append("| Name | Value |")
        lines.append("|------|-------|")
        for member in enum_cls:
            lines.append(f"| `{name}.{member.name}` | `\"{member.value}\"` |")
        lines.append("")
    (OUT / "constants" / "all.md").write_text("\n".join(lines))

    print(f"  constants/*.md (5 files, {len(all_enums)} enums)")


def generate_patterns():
    """Copy pattern templates from scripts/templates/patterns/."""
    (OUT / "patterns").mkdir(parents=True, exist_ok=True)
    templates_dir = ROOT / "scripts" / "templates" / "patterns"
    count = 0
    if templates_dir.exists():
        for f in sorted(templates_dir.glob("*.md")):
            shutil.copy2(f, OUT / "patterns" / f.name)
            count += 1
    print(f"  patterns/*.md ({count} files)")


def generate_index():
    """Generate index.json manifest."""
    import pyxflow
    tools = {
        "get_pyxflow_primer": {"file": "primer.md"},
        "list_components": {"file": "components.json"},
        "get_component_api": {
            "param": "component_name",
            "file_pattern": "components/{name}.md",
        },
        "get_example": {
            "param": "example_name",
            "file_pattern": "examples/{name}.md",
        },
        "get_pattern": {
            "param": "pattern_name",
            "file_pattern": "patterns/{name}.md",
        },
        "get_constants": {
            "param": "category",
            "file_pattern": "constants/{category}.md",
            "default": "all",
        },
    }

    # Collect available files
    examples = sorted(f.stem for f in (OUT / "examples").glob("*.md")) if (OUT / "examples").exists() else []
    patterns = sorted(f.stem for f in (OUT / "patterns").glob("*.md")) if (OUT / "patterns").exists() else []
    components = sorted(f.stem for f in (OUT / "components").glob("*.md")) if (OUT / "components").exists() else []

    index = {
        "version": pyxflow.__version__,
        "generated": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "base_url": "https://manolo.github.io/pyxflow/mcp",
        "tools": tools,
        "available": {
            "components": components,
            "examples": examples,
            "patterns": patterns,
            "constants": ["all", "layout", "grid", "field", "variants"],
        },
    }
    text = json.dumps(index, indent=2)
    (OUT / "index.json").write_text(text)
    print(f"  index.json")


# ---------------------------------------------------------------------------
#  Main
# ---------------------------------------------------------------------------

def main():
    print(f"Building MCP content -> {OUT}/")

    # Clean output
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    generate_primer()
    generate_components_json()
    generate_all_component_docs()
    generate_examples()
    generate_constants()
    generate_patterns()
    generate_index()

    # Count total files
    total = sum(1 for _ in OUT.rglob("*") if _.is_file())
    print(f"\nDone! {total} files generated in {OUT}/")


if __name__ == "__main__":
    main()
