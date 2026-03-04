# Project Setup

## Installation

```bash
pip install pyxflow
```

## Recommended Project Structure

```
my-app/
  __init__.py
  __main__.py          # Entry point: FlowApp().run()
  views/
    __init__.py
    main_layout.py     # AppShell with theme + navigation
    home.py            # Your views
  lib/
    __init__.py        # Business logic, services, data models
  static/
    styles/
      styles.css       # Custom CSS (loaded via @StyleSheet)
    images/            # Static assets (logo, icons, etc.)
```

### Directory roles

| Directory | Purpose |
|-----------|---------|
| `views/`  | UI views decorated with `@Route`. Auto-discovered by PyXFlow. |
| `lib/`    | Business logic, services, data access, models. Imported by views. |
| `static/` | CSS, images, fonts. Served automatically at their path (e.g. `/styles/styles.css`). |

### When to use multiple apps

For projects with multiple independent apps, nest each under its own package:

```
my-project/
  app_admin/
    views/
    lib/
    static/
  app_public/
    views/
    lib/
    static/
```

Run each with: `pyxflow app_admin` or `pyxflow app_public`.

## Scaffolding a New Project

The fastest way to create this structure:

```bash
mkdir my-app && cd my-app
pyxflow --setup
```

This creates `views/`, `static/`, `__main__.py`, a starter layout, and a hello-world view.

## Entry Point

```python
# __main__.py
from pyxflow import FlowApp

FlowApp().run()  # auto-discovers views/ in the current package
```

Run with:

```bash
python -m my_app                    # from parent directory
pyxflow                             # from inside my-app/ (auto-detects views/)
pyxflow --port 9090                 # custom port
pyxflow --dev                       # auto-reload on changes
```

## App Layout with Theme

Most apps need an `AppLayout` with navigation and theme configuration.
Create `views/main_layout.py`:

```python
from pyxflow import *
from pyxflow.components import *
from pyxflow.menu import get_menu_entries

@AppShell
@Push
@StyleSheet("styles/styles.css")
class MainLayout(AppLayout):
    def __init__(self):
        self.add_to_navbar(DrawerToggle(), H2("My App"))
        nav = SideNav()
        for entry in get_menu_entries():
            icon = Icon(entry.icon) if entry.icon else None
            nav.add_item(SideNavItem(entry.title, entry.path, icon))
        self.add_to_drawer(nav)
```

**Important:**
- `@AppShell` must be the outermost decorator (first line)
- `@Push` enables WebSocket push (needed for background tasks updating the UI)
- `@StyleSheet("styles/styles.css")` loads your custom CSS from `static/styles/styles.css`
- Add `@ColorScheme("dark")` for dark mode

## Starter CSS

The scaffold creates `static/styles/styles.css` with:

```css
/* Global Theme: aura or lumo */
/* @import url('/aura/aura.css'); */
@import url('/lumo/lumo.css');

/* Set custom styles below */
```

The `@import url('/lumo/lumo.css')` line loads Lumo utility CSS classes.
Add your custom styles below it.

See `get_pattern("theming")` for the full Lumo CSS variable reference.

## View Discovery

PyXFlow auto-discovers all `@Route`-decorated classes in the views module:

```python
# views/home.py
from pyxflow import *
from pyxflow.components import *
from my_app.views.main_layout import MainLayout

@Route("", layout=MainLayout)
@Menu(title="Home", order=1, icon="vaadin:home")
class HomeView(VerticalLayout):
    def __init__(self):
        super().__init__()
        self.add(H1("Welcome!"))
```

## Business Logic in lib/

Keep UI and logic separate. Views import from `lib/`:

```python
# lib/people_service.py
class PeopleService:
    def get_all(self) -> list[Person]:
        ...

# views/people_view.py
from my_app.lib.people_service import PeopleService

@Route("people", layout=MainLayout)
class PeopleView(VerticalLayout):
    def __init__(self):
        service = PeopleService()
        grid = Grid()
        grid.set_items(service.get_all())
        self.add(grid)
```

## Simple App (no AppLayout)

For quick prototypes without navigation:

```python
# views/main_view.py
from pyxflow import Route
from pyxflow.components import VerticalLayout, H1

@Route("")
class MainView(VerticalLayout):
    def __init__(self):
        super().__init__()
        self.add(H1("Hello PyXFlow!"))
```

## Static Files

Place static assets in `static/`:

```
my-app/
  static/
    styles/
      styles.css       # /styles/styles.css
    images/
      logo.png         # /images/logo.png
    fonts/
      custom.woff2     # /fonts/custom.woff2
```

Files are served at their path relative to `static/`.

## Custom Bundle

To generate a project-specific bundle (optional):

```bash
pyxflow --bundle
```

## Production

```bash
pyxflow --host 0.0.0.0 --port 8080
```

## FlowApp Options

```python
app = FlowApp(
    "views",           # Module with @Route views (default: auto-detect)
    host="0.0.0.0",    # Bind address
    port=8080,         # Port
)
app.run()
```
