"""Tests for @Menu decorator and MenuConfiguration."""

import pytest
from vaadin.flow.menu import Menu, MenuEntry, get_menu_entries, get_page_header
from vaadin.flow.router import Route, PageTitle, _routes, clear_routes
from vaadin.flow.core.component import Component


@pytest.fixture(autouse=True)
def clean_routes():
    clear_routes()
    yield
    clear_routes()


class TestMenuDecorator:
    def test_menu_sets_attributes(self):
        @Route("")
        @Menu(title="Home", order=0, icon="vaadin:home")
        class HomeView(Component):
            pass

        assert HomeView._menu_title == "Home"
        assert HomeView._menu_order == 0
        assert HomeView._menu_icon == "vaadin:home"

    def test_menu_defaults(self):
        @Route("test")
        @Menu()
        class TestView(Component):
            pass

        assert TestView._menu_title is None
        assert TestView._menu_order == 0
        assert TestView._menu_icon is None

    def test_menu_exclude(self):
        @Route("admin")
        @Menu(exclude=True)
        class AdminView(Component):
            pass

        assert AdminView._menu_exclude is True

    def test_menu_custom_order(self):
        @Route("late")
        @Menu(title="Late", order=99)
        class LateView(Component):
            pass

        assert LateView._menu_order == 99


class TestGetMenuEntries:
    def test_basic_entries(self):
        @Route("")
        @Menu(title="Home", order=0, icon="vaadin:home")
        class HomeView(Component):
            pass

        @Route("about")
        @Menu(title="About", order=1, icon="vaadin:info")
        class AboutView(Component):
            pass

        entries = get_menu_entries()
        assert len(entries) == 2
        assert entries[0].title == "Home"
        assert entries[0].path == "/"
        assert entries[0].order == 0
        assert entries[0].icon == "vaadin:home"
        assert entries[1].title == "About"
        assert entries[1].path == "/about"

    def test_sorted_by_order(self):
        @Route("c")
        @Menu(title="Third", order=3)
        class CView(Component):
            pass

        @Route("a")
        @Menu(title="First", order=1)
        class AView(Component):
            pass

        @Route("b")
        @Menu(title="Second", order=2)
        class BView(Component):
            pass

        entries = get_menu_entries()
        assert [e.title for e in entries] == ["First", "Second", "Third"]

    def test_sorted_by_path_on_tie(self):
        @Route("b")
        @Menu(title="B", order=0)
        class BView(Component):
            pass

        @Route("a")
        @Menu(title="A", order=0)
        class AView(Component):
            pass

        entries = get_menu_entries()
        assert [e.title for e in entries] == ["A", "B"]

    def test_excludes_no_menu(self):
        @Route("")
        class HomeView(Component):
            pass

        @Route("about")
        @Menu(title="About")
        class AboutView(Component):
            pass

        entries = get_menu_entries()
        assert len(entries) == 1
        assert entries[0].title == "About"

    def test_excludes_excluded(self):
        @Route("admin")
        @Menu(title="Admin", exclude=True)
        class AdminView(Component):
            pass

        @Route("home")
        @Menu(title="Home")
        class HomeView(Component):
            pass

        entries = get_menu_entries()
        assert len(entries) == 1
        assert entries[0].title == "Home"

    def test_excludes_required_params(self):
        @Route("user/:id")
        @Menu(title="User")
        class UserView(Component):
            pass

        @Route("home")
        @Menu(title="Home")
        class HomeView(Component):
            pass

        entries = get_menu_entries()
        assert len(entries) == 1
        assert entries[0].title == "Home"

    def test_includes_optional_params(self):
        @Route("search/:q?")
        @Menu(title="Search")
        class SearchView(Component):
            pass

        entries = get_menu_entries()
        assert len(entries) == 1
        assert entries[0].title == "Search"

    def test_title_from_page_title(self):
        @Route("about", page_title="About Us")
        @Menu()
        class AboutView(Component):
            pass

        entries = get_menu_entries()
        assert entries[0].title == "About Us"

    def test_title_derived_from_class(self):
        @Route("hello-world")
        @Menu()
        class HelloWorldView(Component):
            pass

        entries = get_menu_entries()
        assert entries[0].title == "Hello World"

    def test_menu_entry_dataclass(self):
        entry = MenuEntry(path="/", title="Home", order=0, icon="vaadin:home")
        assert entry.path == "/"
        assert entry.title == "Home"
        assert entry.order == 0
        assert entry.icon == "vaadin:home"

    def test_empty_routes(self):
        entries = get_menu_entries()
        assert entries == []

    def test_root_path(self):
        @Route("")
        @Menu(title="Root")
        class RootView(Component):
            pass

        entries = get_menu_entries()
        assert entries[0].path == "/"


class TestGetPageHeader:
    def test_none_view(self):
        assert get_page_header(None) is None

    def test_page_title_annotation(self):
        @Route("about")
        @PageTitle("About Us")
        class AboutView(Component):
            pass

        view = AboutView()
        assert get_page_header(view) == "About Us"

    def test_route_page_title_param(self):
        @Route("info", page_title="Info Page")
        class InfoView(Component):
            pass

        view = InfoView()
        assert get_page_header(view) == "Info Page"

    def test_dynamic_title(self):
        @Route("dynamic")
        class DynamicView(Component):
            def get_page_title(self):
                return "Dynamic Title"

        view = DynamicView()
        assert get_page_header(view) == "Dynamic Title"

    def test_dynamic_title_takes_priority(self):
        @Route("prio")
        @PageTitle("Static Title")
        class PrioView(Component):
            def get_page_title(self):
                return "Dynamic Wins"

        view = PrioView()
        assert get_page_header(view) == "Dynamic Wins"

    def test_fallback_to_class_name(self):
        @Route("dashboard")
        class MyDashboardView(Component):
            pass

        view = MyDashboardView()
        assert get_page_header(view) == "My Dashboard"

    def test_fallback_class_name_no_view_suffix(self):
        @Route("settings")
        class Settings(Component):
            pass

        view = Settings()
        assert get_page_header(view) == "Settings"

    def test_menu_title_not_used(self):
        """get_page_header uses @PageTitle / class name, not @Menu title."""
        @Route("foo")
        @Menu(title="Menu Title")
        @PageTitle("Page Title")
        class FooView(Component):
            pass

        view = FooView()
        assert get_page_header(view) == "Page Title"
