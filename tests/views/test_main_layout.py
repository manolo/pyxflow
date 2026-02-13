"""Shared layout for all test views — provides SideNav menu."""

from vaadin.flow import AppShell, Push, StyleSheet, ColorScheme
from vaadin.flow.components import HorizontalLayout, SideNav, SideNavItem, VerticalLayout
from vaadin.flow.menu import get_menu_entries


@AppShell
@Push
@StyleSheet("lumo/lumo.css")
@ColorScheme("dark")
class TestMainLayout(HorizontalLayout):
    """Simple router layout: SideNav on the left, content on the right."""

    _is_router_layout = True

    def __init__(self):
        self._content_area = VerticalLayout()
        self._content_area.set_id("test-content")
        self._content_area.get_style().set("flex-grow", "1")
        self._content_area.get_style().set("overflow", "auto")

        nav = SideNav()
        nav.set_id("test-nav")
        nav.get_style().set("overflow", "auto")
        for entry in get_menu_entries():
            if entry.path.startswith("/test/"):
                nav.add_item(SideNavItem(entry.title, entry.path))

        self.add(nav, self._content_area)
        self.get_style().set("height", "100vh")

    def show_router_layout_content(self, content):
        self._content_area.add(content)

    def remove_router_layout_content(self, old):
        self._content_area.remove(old)
