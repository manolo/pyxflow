# PyXFlow - Python Server-Side UI Framework

**Version:** 0.5.3 | **Components:** 78+ | **Python 3.10+**

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
            Button("Greet", lambda e: Notification.show(f"Hello {name.value}!")),
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
# ... all 78+ components available

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
