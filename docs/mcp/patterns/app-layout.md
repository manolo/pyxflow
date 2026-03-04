# Application Layout

AppLayout provides a standard application shell with navbar, drawer, and content area.

## Basic Setup

```python
from pyxflow import AppShell, Push, ColorScheme, StyleSheet, Route
from pyxflow.components import *
from pyxflow.menu import get_menu_entries, get_page_header

@AppShell
@Push
@ColorScheme("dark")
@StyleSheet("lumo/lumo.css", "styles/styles.css")
class MainLayout(AppLayout):
    def __init__(self):
        # Navbar
        self._title = H2("My App")
        self.add_to_navbar(DrawerToggle(), self._title)

        # Drawer with SideNav
        nav = SideNav()
        for entry in get_menu_entries():
            icon = Icon(entry.icon) if entry.icon else None
            nav.add_item(SideNavItem(entry.title, entry.path, icon))
        self.add_to_drawer(H2("My App"), nav)

        self.set_primary_section(AppLayoutSection.DRAWER)

    def show_router_layout_content(self, content):
        super().show_router_layout_content(content)
        title = get_page_header(content) or "My App"
        self._title.set_text(title)
```

## Views with Layout

```python
@Route("dashboard", layout=MainLayout)
@Menu(title="Dashboard", order=1, icon="vaadin:dashboard")
class DashboardView(VerticalLayout):
    def __init__(self):
        self.add(H1("Dashboard"))
```

## @AppShell Decorator

Marks the layout as the application shell. Only one class per app.
It receives the `@Push`, `@ColorScheme`, and `@StyleSheet` decorators.

## @Menu Decorator

Registers a view in the auto-generated menu:

```python
@Route("users", layout=MainLayout)
@Menu(title="Users", order=2, icon="vaadin:users")
class UsersView(VerticalLayout):
    pass
```

## Sections

```python
from pyxflow.components import AppLayoutSection

# Navbar primary (default)
layout.set_primary_section(AppLayoutSection.NAVBAR)

# Drawer primary (full-height drawer)
layout.set_primary_section(AppLayoutSection.DRAWER)
```

## Dynamic Title

```python
class MainLayout(AppLayout):
    def show_router_layout_content(self, content):
        super().show_router_layout_content(content)
        title = get_page_header(content) or "Default"
        self._title.set_text(title)
```

## Custom Drawer Content

```python
class MainLayout(AppLayout):
    def __init__(self):
        logo = Image("/images/logo.png", "Logo")
        logo.get_style().set("height", "60px")

        nav = SideNav()
        nav.add_item(SideNavItem("Home", "/", Icon("vaadin:home")))
        nav.add_item(SideNavItem("Settings", "/settings", Icon("vaadin:cog")))

        self.add_to_drawer(logo, nav)
        self.add_to_navbar(DrawerToggle(), H2("My App"))
```
