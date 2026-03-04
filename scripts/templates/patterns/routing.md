# Routing

PyXFlow uses decorator-based routing with support for URL parameters, wildcards,
and programmatic navigation.

## Basic Route

```python
from pyxflow import Route
from pyxflow.components import VerticalLayout, H1

@Route("")  # Root path
class HomeView(VerticalLayout):
    def __init__(self):
        self.add(H1("Home"))

@Route("about")
class AboutView(VerticalLayout):
    def __init__(self):
        self.add(H1("About"))
```

## URL Parameters

```python
@Route("user/:id")
class UserView(VerticalLayout):
    def before_enter(self, event):
        user_id = event.get("id")
        # Load user by id...
```

## Optional Parameters

```python
@Route("products/:category?/:id?")
class ProductView(VerticalLayout):
    def before_enter(self, event):
        category = event.get("category")  # None if not in URL
        product_id = event.get("id")
```

## Wildcard Routes

```python
@Route("docs/:path*")
class DocsView(VerticalLayout):
    def before_enter(self, event):
        path = event.get("path")  # "guide/getting-started"
```

## Page Title and Route Aliases

```python
from pyxflow import Route, RouteAlias, PageTitle

@Route("dashboard")
@RouteAlias("home")
@PageTitle("Dashboard")
class DashboardView(VerticalLayout):
    pass
```

## Navigation

```python
# Programmatic navigation
ui = self.get_ui()
ui.navigate("user/42")

# Update URL without navigation (push state)
ui.push_url("/user/42")
```

## Layouts

```python
from pyxflow import AppShell, Route
from pyxflow.components import AppLayout

@AppShell
class MainLayout(AppLayout):
    def __init__(self):
        self.add_to_navbar(H2("My App"))

    def show_router_layout_content(self, content):
        super().show_router_layout_content(content)

@Route("home", layout=MainLayout)
class HomeView(VerticalLayout):
    pass
```

## Query Parameters

```python
from pyxflow import BeforeEnterEvent

@Route("search")
class SearchView(VerticalLayout):
    def before_enter(self, event: BeforeEnterEvent):
        query = event.location.query_parameters.get("q", [""])[0]
```

## Menu Integration

```python
from pyxflow import Route, Menu

@Route("dashboard")
@Menu(title="Dashboard", order=1, icon="vaadin:dashboard")
class DashboardView(VerticalLayout):
    pass
```
