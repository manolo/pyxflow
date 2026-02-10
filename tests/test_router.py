"""Tests for the routing system."""

import pytest

from vaadin.flow.router import Route, PageTitle, match_route, get_view_class, get_page_title, get_all_routes, clear_routes, discover_views, AppShell, Push, get_app_shell, clear_app_shell
from vaadin.flow.menu import get_menu_entries
from vaadin.flow.components import VerticalLayout


class TestRouteDecorator:
    """Test @Route decorator."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Clear routes before each test."""
        clear_routes()
        yield
        clear_routes()

    def test_route_registers_view(self):
        """@Route should register view in registry."""
        @Route("")
        class TestView(VerticalLayout):
            pass

        assert get_view_class("") == TestView

    def test_route_with_path(self):
        """@Route with path should register correctly."""
        @Route("about")
        class AboutView(VerticalLayout):
            pass

        assert get_view_class("about") == AboutView
        assert get_view_class("") is None

    def test_route_normalizes_path(self):
        """@Route should normalize paths (strip slashes)."""
        @Route("/users/")
        class UsersView(VerticalLayout):
            pass

        assert get_view_class("users") == UsersView
        assert get_view_class("/users/") == UsersView

    def test_multiple_routes(self):
        """Multiple routes should all be registered."""
        @Route("")
        class HomeView(VerticalLayout):
            pass

        @Route("about")
        class AboutView(VerticalLayout):
            pass

        @Route("contact")
        class ContactView(VerticalLayout):
            pass

        routes = get_all_routes()
        assert len(routes) == 3
        assert routes[""] == HomeView
        assert routes["about"] == AboutView
        assert routes["contact"] == ContactView


class TestPageTitle:
    """Test page title functionality."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Clear routes before each test."""
        clear_routes()
        yield
        clear_routes()

    def test_explicit_page_title(self):
        """Explicit page_title should be used."""
        @Route("", page_title="My Home Page")
        class HomeView(VerticalLayout):
            pass

        assert get_page_title("") == "My Home Page"

    def test_auto_page_title_from_class_name(self):
        """Page title should be derived from class name."""
        @Route("about")
        class AboutView(VerticalLayout):
            pass

        assert get_page_title("about") == "About"

    def test_auto_page_title_camel_case(self):
        """Page title should split camel case."""
        @Route("users")
        class UserProfileView(VerticalLayout):
            pass

        assert get_page_title("users") == "User Profile"

    def test_page_title_not_found(self):
        """Non-existent route should return None."""
        assert get_page_title("nonexistent") is None


class TestRouteMatching:
    """Test route matching."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Clear routes before each test."""
        clear_routes()
        yield
        clear_routes()

    def test_exact_match(self):
        """Exact path should match."""
        @Route("users")
        class UsersView(VerticalLayout):
            pass

        assert get_view_class("users") == UsersView
        assert get_view_class("user") is None
        assert get_view_class("users/123") is None

    def test_root_route(self):
        """Root route should match empty path."""
        @Route("")
        class HomeView(VerticalLayout):
            pass

        assert get_view_class("") == HomeView
        assert get_view_class("/") == HomeView

    def test_no_match_returns_none(self):
        """Non-matching path should return None."""
        @Route("home")
        class HomeView(VerticalLayout):
            pass

        assert get_view_class("about") is None


class TestRouteAttributes:
    """Test route attributes stored on class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Clear routes before each test."""
        clear_routes()
        yield
        clear_routes()

    def test_route_path_stored_on_class(self):
        """Route path should be stored on class."""
        @Route("users")
        class UsersView(VerticalLayout):
            pass

        assert UsersView._route_path == "users"

    def test_page_title_stored_on_class(self):
        """Page title should be stored on class."""
        @Route("about", page_title="About Us")
        class AboutView(VerticalLayout):
            pass

        assert AboutView._page_title == "About Us"

    def test_none_page_title_stored(self):
        """None page title should be stored."""
        @Route("home")
        class HomeView(VerticalLayout):
            pass

        assert HomeView._page_title is None


class TestMatchRoute:
    """Test match_route function."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        yield
        clear_routes()

    def test_match_static_route(self):
        """match_route should return class, title, empty params for static route."""
        @Route("about", page_title="About")
        class AboutView(VerticalLayout):
            pass

        result = match_route("about")
        assert result is not None
        cls, title, params, _layout = result
        assert cls == AboutView
        assert title == "About"
        assert params == {}

    def test_match_parameterized_route(self):
        """match_route should return params for parameterized route."""
        @Route("user/:id")
        class UserView(VerticalLayout):
            pass

        result = match_route("user/42")
        assert result is not None
        cls, title, params, _layout = result
        assert cls == UserView
        assert params == {"id": "42"}

    def test_match_returns_none(self):
        """match_route should return None for no match."""
        @Route("home")
        class HomeView(VerticalLayout):
            pass

        assert match_route("other") is None

    def test_match_route_normalizes_path(self):
        """match_route should normalize path."""
        @Route("test")
        class TestView(VerticalLayout):
            pass

        result = match_route("/test/")
        assert result is not None
        assert result[0] == TestView


class TestPageTitleDecorator:
    """Test @PageTitle decorator."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        yield
        clear_routes()

    def test_page_title_sets_class_attr(self):
        """@PageTitle should set _page_title attribute."""
        @PageTitle("My Title")
        class MyView(VerticalLayout):
            pass

        assert MyView._page_title == "My Title"

    def test_page_title_not_overwritten_by_route(self):
        """@Route without page_title should not overwrite @PageTitle."""
        @Route("pt")
        @PageTitle("From PageTitle")
        class PTView(VerticalLayout):
            pass

        assert PTView._page_title == "From PageTitle"
        assert get_page_title("pt") == "From PageTitle"


class TestDiscoverViews:
    """Test discover_views() auto-discovery."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        clear_app_shell()
        yield
        clear_routes()
        clear_app_shell()

    def test_discover_views_registers_routes(self):
        """discover_views should import all modules and trigger @Route registration."""
        imported = discover_views("demo.views")
        assert len(imported) > 0
        routes = get_all_routes()
        # At minimum, the example views should be registered
        assert "" in routes  # AboutView at root
        assert "hello" in routes
        assert "components" in routes
        assert "grid" in routes

    def test_discover_views_returns_module_names(self):
        """discover_views should return list of imported module names."""
        imported = discover_views("demo.views")
        assert "demo.views.hello_world" in imported
        assert "demo.views.about" in imported
        assert "demo.views.components" in imported
        assert "demo.views.grid" in imported

    def test_discover_views_menu_entries(self):
        """After discover_views, get_menu_entries should return @Menu entries."""
        discover_views("demo.views")
        entries = get_menu_entries()
        assert len(entries) == 6
        titles = [e.title for e in entries]
        assert titles == ["About", "Hello", "Components", "Grid", "Master-Detail", "Stopwatch"]
        # Verify order
        orders = [e.order for e in entries]
        assert orders == [0, 1, 2, 3, 4, 10]
        # Verify icons
        icons = [e.icon for e in entries]
        assert icons == ["vaadin:info-circle", "vaadin:hand", "vaadin:grid-small", "vaadin:table", "vaadin:split-h", "vaadin:timer"]

    def test_discover_views_registers_app_shell(self):
        """discover_views should register @AppShell from MainLayout."""
        discover_views("demo.views")
        app_shell = get_app_shell()
        assert app_shell is not None
        assert app_shell.__name__ == "MainLayout"
        assert getattr(app_shell, '_push_enabled', False) is True
        assert "lumo/lumo.css" in getattr(app_shell, '_stylesheets', [])
        assert "styles/styles.css" in getattr(app_shell, '_stylesheets', [])


class TestAppShellDecorator:
    """Test @AppShell decorator."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_app_shell()
        yield
        clear_app_shell()

    def test_app_shell_registers_class(self):
        """@AppShell should register the class globally."""
        @AppShell
        class MyShell:
            pass

        assert get_app_shell() is MyShell

    def test_app_shell_returns_class(self):
        """@AppShell should return the original class."""
        @AppShell
        class MyShell:
            pass

        assert MyShell.__name__ == "MyShell"

    def test_clear_app_shell(self):
        """clear_app_shell should reset the registered class."""
        @AppShell
        class MyShell:
            pass

        assert get_app_shell() is not None
        clear_app_shell()
        assert get_app_shell() is None

    def test_no_app_shell_by_default(self):
        """get_app_shell should return None if nothing registered."""
        assert get_app_shell() is None


class TestPushDecorator:
    """Test @Push decorator."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_app_shell()
        yield
        clear_app_shell()

    def test_push_sets_flag(self):
        """@Push should set _push_enabled on the class."""
        @Push
        class MyShell:
            pass

        assert MyShell._push_enabled is True

    def test_no_push_by_default(self):
        """Classes without @Push should not have _push_enabled."""
        class MyShell:
            pass

        assert not getattr(MyShell, '_push_enabled', False)

    def test_app_shell_with_push(self):
        """@AppShell @Push should set both registration and push flag."""
        @AppShell
        @Push
        class MyShell:
            pass

        assert get_app_shell() is MyShell
        assert MyShell._push_enabled is True

    def test_app_shell_without_push(self):
        """@AppShell without @Push should have push disabled."""
        @AppShell
        class MyShell:
            pass

        assert get_app_shell() is MyShell
        assert not getattr(MyShell, '_push_enabled', False)
