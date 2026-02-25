# Vaadin Flow for Python

Build web applications in Python using [Vaadin](https://vaadin.com/) web components. Write server-side Python code, get a fully interactive UI in the browser — no JavaScript required.

```python
from vaadin.flow import Route
from vaadin.flow.components import Button, Notification, TextField, VerticalLayout

@Route("")
class HelloView(VerticalLayout):
    def __init__(self):
        self.name = TextField("Your name")
        self.add(
            self.name,
            Button("Say hello", on_click=self._greet),
        )

    def _greet(self, event):
        Notification.show(f"Hello {self.name.value}")
```

## Features

- **49 components** — buttons, text fields, grids, dialogs, date pickers, menus, and more
- **Server-side only** — all logic runs in Python, no JavaScript to write
- **Lazy data loading** — Grid with virtual scrolling and server-side sorting
- **Real-time push** — update the UI from background tasks via WebSocket
- **Theming** — Lumo and Aura themes with dark mode support
- **Form validation** — Binder with validators and converters
- **Hot reload** — `--dev` mode watches for file changes

## Installation

```bash
pip install git+https://github.com/manolo/vaadin-pyflow.git@main
```

## Quick start

### New project (empty directory)

```bash
mkdir my-project && cd my-project
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install git+https://github.com/manolo/vaadin-pyflow.git@main
vaadin --setup
```

This creates everything you need:

```
my_project/
  __init__.py
  __main__.py
  views/
    __init__.py
    main_layout.py    # AppLayout with SideNav
    hello_world.py    # Sample view with TextField + Button
  static/
    favicon.ico
    styles/
      styles.css
    images/
.vscode/              # VSCode settings, snippets, extensions
```

Run it:

```bash
python -m my_project
# http://localhost:8080
```

### Existing project

If you already have a project with a virtual environment and other code:

```bash
cd my-project
source .venv/bin/activate   # activate your existing venv
pip install git+https://github.com/manolo/vaadin-pyflow.git@main
vaadin --setup myapp
```

This scaffolds a `myapp/` package inside your project without touching existing files. VSCode configuration is included automatically.

If you only need the VSCode config (without scaffolding a project), use `vaadin --vscode`.

### Running

```bash
# Auto-detect (finds the directory with views/)
vaadin

# Explicit module
vaadin myapp

# Dev mode with hot-reload
vaadin --dev

# Custom port
vaadin --port 3000
```

### Project structure

The `--setup` command generates this structure. Only `views/` is required -- everything else is optional:

| File | Purpose |
|------|---------|
| `__main__.py` | Entry point (`python -m myapp`) |
| `views/main_layout.py` | `@AppShell` with `AppLayout`, drawer, navigation |
| `views/hello_world.py` | Sample view with `@Route` and `@Menu` |
| `views/*.py` | Add more views here -- one class per file |
| `static/styles/*.css` | CSS loaded via `@StyleSheet` in the layout |
| `static/images/` | Images served at `/images/...` |
| `static/favicon.ico` | Browser favicon |

## Components

### Forms and input

| Component | Description |
|-----------|-------------|
| `TextField` | Single-line text input |
| `TextArea` | Multi-line text input |
| `PasswordField` | Masked password input |
| `EmailField` | Email input with RFC 5322 validation |
| `NumberField` | Numeric input with min/max/step |
| `IntegerField` | Integer-only variant |
| `Checkbox` / `CheckboxGroup` | Toggle and multiple selection |
| `RadioButtonGroup` | Single selection from options |
| `Select` | Dropdown single selection |
| `ComboBox` / `MultiSelectComboBox` | Filterable dropdown (multi-select) |
| `DatePicker` / `TimePicker` / `DateTimePicker` | Date and time selection |
| `Upload` | File upload |
| `CustomField` | Composite custom field |

### Data

| Component | Description |
|-----------|-------------|
| `Grid` | Data table with sorting, selection, lazy loading, renderers |
| `TreeGrid` | Hierarchical data table with expand/collapse |

### Layout

| Component | Description |
|-----------|-------------|
| `VerticalLayout` / `HorizontalLayout` | Stack children vertically or horizontally |
| `FlexLayout` | CSS Flexbox layout |
| `FormLayout` | Responsive form with labels and colspan |
| `SplitLayout` | Resizable two-panel split |
| `AppLayout` | Application shell with navbar and drawer |
| `Scroller` | Scrollable container |
| `Card` | Styled card container |
| `Details` / `Accordion` | Collapsible sections |
| `Dialog` / `ConfirmDialog` | Modal dialogs |
| `MasterDetailLayout` | Master-detail pattern |

### Navigation

| Component | Description |
|-----------|-------------|
| `Tabs` / `TabSheet` | Tab navigation with content panels |
| `SideNav` | Side navigation with items |
| `MenuBar` / `ContextMenu` | Hierarchical and right-click menus |
| `RouterLink` | Client-side navigation link |

### Display

| Component | Description |
|-----------|-------------|
| `Button` | Click listener, icon support, keyboard shortcuts |
| `Icon` | Vaadin and Lumo icon sets |
| `Notification` | Toast notifications with position and duration |
| `ProgressBar` | Determinate and indeterminate progress |
| `Avatar` / `AvatarGroup` | User avatars |
| `Span`, `H1`–`H6`, `Paragraph`, `Pre` | Text elements |
| `Image`, `Anchor`, `IFrame` | Media and links |

## Routing

```python
from vaadin.flow import Route, Menu

@Route("dashboard", page_title="Dashboard", layout=MainLayout)
@Menu(title="Dashboard", order=1, icon="vaadin:dashboard")
class DashboardView(VerticalLayout):
    ...
```

- `@Route(path)` — register a view at a URL path
- `@Route(path, layout=MainLayout)` — wrap in a layout
- `@Menu(title, order, icon)` — add to the navigation menu
- Route parameters: `@Route("greet/:name")` with `on_parameter_changed(self, params)`

## Application shell

```python
from vaadin.flow import AppShell, Push, ColorScheme, StyleSheet
from vaadin.flow.components import AppLayout, DrawerToggle, H1, SideNav, SideNavItem
from vaadin.flow.menu import get_menu_entries

@AppShell
@Push
@ColorScheme("dark")
@StyleSheet("lumo/lumo.css", "styles/styles.css")
class MainLayout(AppLayout):
    def __init__(self):
        self.add_to_navbar(DrawerToggle(), H1("My App"))
        nav = SideNav()
        for entry in get_menu_entries():
            nav.add_item(SideNavItem(entry.title, entry.path))
        self.add_to_drawer(nav)
```

- `@AppShell` — global configuration (one per app)
- `@Push` — enable WebSocket push for real-time updates
- `@ColorScheme("dark")` — initial color scheme
- `@StyleSheet(...)` — inject CSS files

## Grid with lazy data

```python
grid = Grid()
grid.add_column("name", header="Name").set_sortable(True).set_auto_width(True)
grid.add_column("email", header="Email").set_auto_width(True)
grid.set_data_provider(my_fetch)

def my_fetch(offset, limit, sort_orders):
    return items[offset:offset+limit], len(items)
```

## Real-time push

```python
import asyncio

@Route("live")
class LiveView(VerticalLayout):
    def __init__(self):
        self.label = Span("0")
        self.add(self.label)
        asyncio.get_event_loop().create_task(self._tick())

    async def _tick(self):
        n = 0
        while True:
            await asyncio.sleep(1)
            n += 1
            ui = self.get_ui()
            if ui:
                ui.access(lambda: self.label.set_text(str(n)))
```

Requires `@Push` on the `@AppShell` class.

## CLI

```
vaadin [app_module] [options]

  app_module               Python module with views/ (auto-detected if omitted)
  --setup [app_name]       Scaffold a new project (views, static, __main__.py, .vscode/)
  --vscode                 Generate .vscode/ config and install recommended extensions
  --dev                    Auto-reload on source changes
  --debug                  Verbose UIDL protocol logging
  --port PORT              Server port (default: 8080)
  --host HOST              Server host (default: localhost)
  --bundle                 Generate frontend bundle
  --bundle --keep          Keep build artifacts after generation
  --bundle --vaadin-version VERSION   Pin a Vaadin version
```

## Development

See [README-DEV.md](README-DEV.md) for setup, running the demo, tests, project structure, and architecture.

## License

Apache License 2.0
