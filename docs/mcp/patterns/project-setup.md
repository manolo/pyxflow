# Project Setup

## Installation

```bash
pip install pyxflow
```

## Project Structure

```
my-app/
  app.py               # Entry point
  views/
    __init__.py
    layout.py          # AppShell with theme config
    home.py            # Your views
  static/
    styles/
      app.css          # Custom styles
    images/            # Static assets
```

## Entry Point

```python
# app.py
from pyxflow import FlowApp

app = FlowApp("views")
app.run()  # http://localhost:8080
```

Or with CLI:

```bash
pyxflow views --port 8080
```

## App Layout with Theme

Most apps need an AppLayout with navigation and a configured theme.
Create `views/layout.py`:

```python
from pyxflow import AppShell, ColorScheme, StyleSheet
from pyxflow.components import AppLayout, DrawerToggle, H2, SideNav, SideNavItem, Icon
from pyxflow.menu import get_menu_entries

@AppShell
@ColorScheme("dark")
@StyleSheet("lumo/lumo.css", "styles/app.css")
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
- Always include `"lumo/lumo.css"` as the first stylesheet in `@StyleSheet`
- `@ColorScheme("dark")` or `@ColorScheme("light")` sets the initial theme

## Starter CSS

Create `static/styles/app.css`:

```css
/* Full-height app */
html, body {
  height: 100%;
  margin: 0;
}

/* Uncomment to customize Lumo theme colors */
/* html {
  --lumo-primary-color: hsl(220, 90%, 52%);
  --lumo-border-radius-m: 8px;
} */
```

See the `get_pattern("theming")` tool for the full Lumo CSS variable reference and
a more complete starter CSS template.

## View Discovery

PyXFlow auto-discovers all `@Route`-decorated classes in the views module:

```python
# views/home.py
from pyxflow import Route, Menu
from pyxflow.components import VerticalLayout, H1
from views.layout import MainLayout

@Route("", layout=MainLayout)
@Menu(title="Home", order=1, icon="vaadin:home")
class HomeView(VerticalLayout):
    def __init__(self):
        super().__init__()
        self.add(H1("Welcome!"))
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

Place static assets in `<app_dir>/static/`:

```
my-app/
  views/
  static/
    styles/
      app.css
    images/
      logo.png
```

Access them at `/styles/app.css` and `/images/logo.png`.

## Custom Bundle

To generate a project-specific bundle (optional):

```bash
pyxflow views --bundle
```

This creates `views/bundle/` with only the components your app uses.

## Production

```bash
pyxflow views --host 0.0.0.0 --port 8080
```

## FlowApp Options

```python
app = FlowApp(
    "views",           # Module with @Route views
    host="0.0.0.0",    # Bind address
    port=8080,         # Port
)
app.run()
```
