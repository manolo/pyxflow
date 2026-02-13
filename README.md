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
pip install vaadin-pyflow
```

## Quick start

Create a project:

```
myapp/
  __init__.py
  __main__.py
  views/
    __init__.py
    hello.py
```

`myapp/views/hello.py`:

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

`myapp/__main__.py`:

```python
from vaadin.flow import FlowApp

FlowApp(port=8080).run()
```

Run it:

```bash
python -m myapp
# http://localhost:8080
```

Or use the CLI (auto-detects any directory with `views/`):

```bash
vaadin --port 8080
```

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
  --dev                    Auto-reload on source changes
  --debug                  Verbose UIDL protocol logging
  --port PORT              Server port (default: 8080)
  --host HOST              Server host (default: localhost)
  --bundle                 Generate frontend bundle
  --bundle --keep          Keep build artifacts after generation
  --bundle --vaadin-version VERSION   Pin a Vaadin version
```

## Development

### Setup

```bash
git clone https://github.com/vaadin/vaadin-pyflow.git
cd vaadin-pyflow
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### Run the demo

```bash
python -m demo                # http://localhost:8088
python -m demo --dev          # hot-reload on file changes
python -m demo --debug        # verbose protocol logging
```

### Tests

```bash
# Unit tests (default, ~2100 tests)
pytest

# Specific test file
pytest tests/test_rpc_events.py -v
```

UI integration tests require Playwright:

```bash
pip install playwright pytest-playwright
playwright install chromium

# Run UI tests (auto-starts the server if needed)
pytest tests/ui/

# With visible browser
pytest tests/ui/ --headed
```

UI tests are excluded from the default `pytest` run. They launch a real browser against the demo server and verify component behavior end-to-end.

### Project structure

```
src/vaadin/flow/
├── core/           # StateTree, StateNode, Element, Component
├── components/     # 49 Vaadin components
├── data/           # Binder, DataProvider, validators, converters
└── server/         # HTTP server (aiohttp), UIDL protocol handler

demo/
├── views/          # Demo views (hello, grid, dialog, push, etc.)
└── __main__.py     # python -m demo

tests/
├── *.py            # Unit tests
└── ui/             # Playwright integration tests
```

### Architecture

```
Browser                          Server (Python)
┌──────────────────┐             ┌──────────────────────┐
│ Vaadin Web       │   HTTP/WS   │ StateTree            │
│ Components       │◄───────────►│ Components (Python)  │
│ FlowClient.js    │   (UIDL)    │ UIDL Handler         │
└──────────────────┘             └──────────────────────┘
```

The browser runs the standard Vaadin frontend (web components + FlowClient.js). The Python server maintains a state tree and communicates changes via the UIDL protocol over HTTP, with optional WebSocket for push.

## License

Apache License 2.0
