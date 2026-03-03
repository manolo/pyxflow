"""Tests for the routing system."""

import pytest

from pyxflow.router import Route, RouteAlias, PageTitle, match_route, get_view_class, get_page_title, get_all_routes, clear_routes, discover_views, AppShell, Push, get_app_shell, clear_app_shell
from pyxflow.menu import get_menu_entries
from pyxflow.components import VerticalLayout


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


class TestMatchRouteSpecificity:
    """Test that parameterized routes are matched by specificity, not registration order."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        yield
        clear_routes()

    def test_literal_segment_beats_all_params(self):
        """Route with literal segment wins over all-optional route."""
        @Route(":version?/:starter?")
        class CatchAllView(VerticalLayout):
            pass

        @Route("run-local/:run_id?")
        class RunLocalView(VerticalLayout):
            pass

        result = match_route("run-local")
        assert result is not None
        cls, _title, params, _layout = result
        assert cls == RunLocalView
        assert params == {}

    def test_more_literals_wins(self):
        """Route with more literal segments has higher priority."""
        @Route(":a/:b")
        class GenericView(VerticalLayout):
            pass

        @Route("api/:id")
        class ApiView(VerticalLayout):
            pass

        result = match_route("api/123")
        assert result is not None
        assert result[0] == ApiView
        assert result[2] == {"id": "123"}

    def test_fewer_optionals_wins(self):
        """Route with fewer optional params wins at same literal count."""
        @Route("docs/:page?/:section?")
        class DocsOptView(VerticalLayout):
            pass

        @Route("docs/:page")
        class DocsReqView(VerticalLayout):
            pass

        result = match_route("docs/intro")
        assert result is not None
        assert result[0] == DocsReqView
        assert result[2] == {"page": "intro"}

    def test_static_still_beats_parameterized(self):
        """Static route always wins over parameterized."""
        @Route(":slug?")
        class SlugView(VerticalLayout):
            pass

        @Route("about")
        class AboutView(VerticalLayout):
            pass

        result = match_route("about")
        assert result is not None
        assert result[0] == AboutView
        assert result[2] == {}


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
        assert "demo.views.hello_view" in imported
        assert "demo.views.about_view" in imported
        assert "demo.views.components_view" in imported
        assert "demo.views.grid_view" in imported

    def test_discover_views_menu_entries(self):
        """After discover_views, get_menu_entries should return @Menu entries."""
        discover_views("demo.views")
        entries = get_menu_entries()
        assert len(entries) == 9
        titles = [e.title for e in entries]
        assert titles == ["About", "Hello", "Components", "Grid", "Grid Editor", "Master-Detail", "Responsive CRUD", "Stopwatch", "File Explorer"]
        # Verify sorted by (order, path)
        orders = [e.order for e in entries]
        assert orders == sorted(orders)

    def test_discover_views_registers_app_shell(self):
        """discover_views should register @AppShell from MainLayout."""
        discover_views("demo.views")
        app_shell = get_app_shell()
        assert app_shell is not None
        assert app_shell.__name__ == "MainLayout"
        assert getattr(app_shell, '_push_enabled', False) is True
        assert "lumo/lumo.css" in getattr(app_shell, '_stylesheets', [])
        assert "styles/styles.css" in getattr(app_shell, '_stylesheets', [])


class TestRouteAlias:
    """Test @RouteAlias decorator."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        yield
        clear_routes()

    def test_alias_registers_additional_path(self):
        """@RouteAlias should register an additional path for the same view."""
        @Route("dashboard")
        @RouteAlias("admin-dashboard")
        class DashboardView(VerticalLayout):
            pass

        assert get_view_class("dashboard") is DashboardView
        assert get_view_class("admin-dashboard") is DashboardView

    def test_multiple_aliases(self):
        """Multiple @RouteAlias on the same class should all work."""
        @Route("dashboard")
        @RouteAlias("admin")
        @RouteAlias("home")
        class DashboardView(VerticalLayout):
            pass

        assert get_view_class("dashboard") is DashboardView
        assert get_view_class("admin") is DashboardView
        assert get_view_class("home") is DashboardView

    def test_alias_shares_page_title(self):
        """Alias routes should share the same page title as the primary route."""
        @Route("dashboard", page_title="Dashboard")
        @RouteAlias("admin-dashboard")
        class DashboardView(VerticalLayout):
            pass

        assert get_page_title("dashboard") == "Dashboard"
        assert get_page_title("admin-dashboard") == "Dashboard"

    def test_alias_shares_page_title_decorator(self):
        """Alias should use @PageTitle if present."""
        @Route("dashboard")
        @RouteAlias("admin-dashboard")
        @PageTitle("My Dashboard")
        class DashboardView(VerticalLayout):
            pass

        assert get_page_title("dashboard") == "My Dashboard"
        assert get_page_title("admin-dashboard") == "My Dashboard"

    def test_alias_inherits_layout(self):
        """Alias without explicit layout should inherit from @Route."""
        class MyLayout(VerticalLayout):
            _is_router_layout = True

        @Route("dashboard", layout=MyLayout)
        @RouteAlias("admin-dashboard")
        class DashboardView(VerticalLayout):
            pass

        result_primary = match_route("dashboard")
        result_alias = match_route("admin-dashboard")
        assert result_primary[3] is MyLayout
        assert result_alias[3] is MyLayout

    def test_alias_with_different_layout(self):
        """Alias with explicit layout should use its own layout."""
        class AdminLayout(VerticalLayout):
            _is_router_layout = True

        class PublicLayout(VerticalLayout):
            _is_router_layout = True

        @Route("dashboard", layout=AdminLayout)
        @RouteAlias("public-dash", layout=PublicLayout)
        class DashboardView(VerticalLayout):
            pass

        result_primary = match_route("dashboard")
        result_alias = match_route("public-dash")
        assert result_primary[3] is AdminLayout
        assert result_alias[3] is PublicLayout

    def test_alias_with_no_layout(self):
        """Alias with layout=None should have no layout."""
        class MyLayout(VerticalLayout):
            _is_router_layout = True

        @Route("dashboard", layout=MyLayout)
        @RouteAlias("standalone", layout=None)
        class DashboardView(VerticalLayout):
            pass

        result_primary = match_route("dashboard")
        result_alias = match_route("standalone")
        assert result_primary[3] is MyLayout
        assert result_alias[3] is None

    def test_alias_normalizes_path(self):
        """Alias should normalize paths (strip slashes)."""
        @Route("dashboard")
        @RouteAlias("/admin-dashboard/")
        class DashboardView(VerticalLayout):
            pass

        assert get_view_class("admin-dashboard") is DashboardView

    def test_alias_with_parameters(self):
        """Alias should support parameterized paths."""
        @Route("user/:id")
        @RouteAlias("profile/:id")
        class UserView(VerticalLayout):
            pass

        result = match_route("profile/42")
        assert result is not None
        assert result[0] is UserView
        assert result[2] == {"id": "42"}

    def test_alias_stored_on_class(self):
        """Aliases should be tracked on _route_aliases."""
        @Route("dashboard")
        @RouteAlias("admin")
        @RouteAlias("home")
        class DashboardView(VerticalLayout):
            pass

        assert hasattr(DashboardView, '_route_aliases')
        assert "admin" in DashboardView._route_aliases
        assert "home" in DashboardView._route_aliases

    def test_alias_in_get_all_routes(self):
        """Aliases should appear in get_all_routes."""
        @Route("dashboard")
        @RouteAlias("admin")
        class DashboardView(VerticalLayout):
            pass

        routes = get_all_routes()
        assert "dashboard" in routes
        assert "admin" in routes
        assert routes["dashboard"] is DashboardView
        assert routes["admin"] is DashboardView

    def test_alias_not_in_menu(self):
        """Aliases should not generate @Menu entries (only primary @Route does)."""
        from pyxflow.menu import Menu

        @Route("dashboard")
        @RouteAlias("admin-dashboard")
        @Menu(title="Dashboard", order=0)
        class DashboardView(VerticalLayout):
            pass

        entries = get_menu_entries()
        paths = [e.path for e in entries]
        assert "/dashboard" in paths
        # Alias should NOT appear as a separate menu entry
        assert "/admin-dashboard" not in paths

    def test_alias_without_route_not_registered(self):
        """@RouteAlias without @Route should not register (pending, never flushed)."""
        @RouteAlias("orphan-alias")
        class OrphanView(VerticalLayout):
            pass

        # Without @Route, alias stays pending and is not navigable
        assert get_view_class("orphan-alias") is None

    def test_alias_after_route_registers_immediately(self):
        """@RouteAlias applied after @Route (unusual order) should register."""
        @RouteAlias("alt-path")
        @Route("main-path")
        class MyView(VerticalLayout):
            pass

        assert get_view_class("main-path") is MyView
        assert get_view_class("alt-path") is MyView


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
