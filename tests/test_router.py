"""Tests for the routing system."""

import pytest

from vaadin.flow.router import Route, get_view_class, get_page_title, get_all_routes, clear_routes
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
