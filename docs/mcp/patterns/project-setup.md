# Project Setup

## Installation

```bash
pip install pyxflow
```

## Minimal Project Structure

```
my-app/
  app.py           # Entry point
  views/
    __init__.py
    main_view.py   # Your views
  static/          # Optional CSS/images
    styles.css
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

## View Discovery

PyXFlow auto-discovers all `@Route`-decorated classes in the views module:

```python
# views/main_view.py
from pyxflow import Route
from pyxflow.components import VerticalLayout, H1

@Route("")
class MainView(VerticalLayout):
    def __init__(self):
        self.add(H1("Hello PyXFlow!"))
```

## With App Layout

```python
# views/layout.py
from pyxflow import AppShell, Push, ColorScheme, StyleSheet
from pyxflow.components import AppLayout, DrawerToggle, H2, SideNav, SideNavItem, Icon
from pyxflow.menu import get_menu_entries

@AppShell
@Push
@ColorScheme("dark")
@StyleSheet("styles/app.css")
class MainLayout(AppLayout):
    def __init__(self):
        self.add_to_navbar(DrawerToggle(), H2("My App"))
        nav = SideNav()
        for entry in get_menu_entries():
            icon = Icon(entry.icon) if entry.icon else None
            nav.add_item(SideNavItem(entry.title, entry.path, icon))
        self.add_to_drawer(nav)

# views/home.py
from pyxflow import Route, Menu
from pyxflow.components import VerticalLayout, H1
from views.layout import MainLayout

@Route("", layout=MainLayout)
@Menu(title="Home", order=1, icon="vaadin:home")
class HomeView(VerticalLayout):
    def __init__(self):
        self.add(H1("Welcome!"))
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
