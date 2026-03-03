"""Tests for missing getter methods added in the getter batch."""

from pyxflow.core.state_tree import StateTree


class TestTextFieldGetters:
    def test_get_label(self):
        from pyxflow.components import TextField
        tf = TextField("Name")
        assert tf.get_label() == "Name"

    def test_get_label_after_set(self):
        from pyxflow.components import TextField
        tf = TextField()
        tf.set_label("Email")
        assert tf.get_label() == "Email"

    def test_get_placeholder(self):
        from pyxflow.components import TextField
        tf = TextField()
        tf.set_placeholder("Enter text...")
        assert tf.get_placeholder() == "Enter text..."

    def test_get_placeholder_default(self):
        from pyxflow.components import TextField
        tf = TextField()
        assert tf.get_placeholder() == ""


class TestTabsGetters:
    def test_is_autoselect_default(self):
        from pyxflow.components import Tabs
        tabs = Tabs()
        assert tabs.is_autoselect() is True

    def test_is_autoselect_after_set(self):
        from pyxflow.components import Tabs
        tabs = Tabs()
        tabs.set_autoselect(False)
        assert tabs.is_autoselect() is False

    def test_get_orientation_default(self):
        from pyxflow.components import Tabs
        tabs = Tabs()
        assert tabs.get_orientation() == "horizontal"

    def test_get_orientation_after_set(self):
        from pyxflow.components import Tabs, Tab
        tabs = Tabs(Tab("A"))
        tree = StateTree()
        tabs._attach(tree)
        tabs.set_orientation("vertical")
        assert tabs.get_orientation() == "vertical"

    def test_get_orientation_before_attach(self):
        from pyxflow.components import Tabs
        tabs = Tabs()
        tabs.set_orientation("vertical")
        assert tabs.get_orientation() == "vertical"


class TestTabSheetGetters:
    def test_get_tab_count(self):
        from pyxflow.components import TabSheet
        from pyxflow.components.html import Div
        ts = TabSheet()
        assert ts.get_tab_count() == 0
        ts.add("Tab1", Div("Content1"))
        assert ts.get_tab_count() == 1
        ts.add("Tab2", Div("Content2"))
        assert ts.get_tab_count() == 2

    def test_get_tab_at(self):
        from pyxflow.components import TabSheet
        from pyxflow.components.html import Div
        ts = TabSheet()
        tab1 = ts.add("First", Div("C1"))
        tab2 = ts.add("Second", Div("C2"))
        assert ts.get_tab_at(0) is tab1
        assert ts.get_tab_at(1) is tab2

    def test_get_index_of(self):
        from pyxflow.components import TabSheet
        from pyxflow.components.html import Div
        ts = TabSheet()
        tab1 = ts.add("A", Div("CA"))
        tab2 = ts.add("B", Div("CB"))
        assert ts.get_index_of(tab1) == 0
        assert ts.get_index_of(tab2) == 1

    def test_get_index_of_unknown_tab(self):
        from pyxflow.components import TabSheet
        from pyxflow.components.tabs import Tab
        ts = TabSheet()
        assert ts.get_index_of(Tab("X")) == -1


class TestAppLayoutGetters:
    def test_get_primary_section_default(self):
        from pyxflow.components import AppLayout
        layout = AppLayout()
        assert layout.get_primary_section() == "navbar"

    def test_get_primary_section_after_set(self):
        from pyxflow.components import AppLayout
        layout = AppLayout()
        layout.set_primary_section("drawer")
        assert layout.get_primary_section() == "drawer"

    def test_is_drawer_opened_default(self):
        from pyxflow.components import AppLayout
        layout = AppLayout()
        assert layout.is_drawer_opened() is True

    def test_is_drawer_opened_after_set(self):
        from pyxflow.components import AppLayout
        layout = AppLayout()
        tree = StateTree()
        layout._attach(tree)
        layout.set_drawer_opened(False)
        assert layout.is_drawer_opened() is False


class TestContextMenuGetters:
    def test_get_target(self):
        from pyxflow.components import ContextMenu
        from pyxflow.components.html import Div
        target = Div("Click me")
        menu = ContextMenu(target)
        assert menu.get_target() is target

    def test_get_target_none(self):
        from pyxflow.components import ContextMenu
        menu = ContextMenu()
        assert menu.get_target() is None

    def test_is_open_on_click_default(self):
        from pyxflow.components import ContextMenu
        menu = ContextMenu()
        assert menu.is_open_on_click() is False

    def test_is_open_on_click_after_set(self):
        from pyxflow.components import ContextMenu
        menu = ContextMenu()
        menu.set_open_on_click(True)
        assert menu.is_open_on_click() is True


class TestCardGetters:
    def test_get_media(self):
        from pyxflow.components import Card
        from pyxflow.components.html import Div
        media = Div("img")
        card = Card()
        card.set_media(media)
        assert card.get_media() is media

    def test_get_media_none(self):
        from pyxflow.components import Card
        assert Card().get_media() is None

    def test_get_header(self):
        from pyxflow.components import Card
        from pyxflow.components.html import Div
        header = Div("Header")
        card = Card()
        card.set_header(header)
        assert card.get_header() is header

    def test_get_header_prefix(self):
        from pyxflow.components import Card, Icon
        icon = Icon("vaadin:user")
        card = Card()
        card.set_header_prefix(icon)
        assert card.get_header_prefix() is icon

    def test_get_header_suffix(self):
        from pyxflow.components import Card
        from pyxflow.components.html import Div
        suffix = Div("X")
        card = Card()
        card.set_header_suffix(suffix)
        assert card.get_header_suffix() is suffix


class TestScrollerGetters:
    def test_get_content(self):
        from pyxflow.components import Scroller
        from pyxflow.components.html import Div
        content = Div("Content")
        scroller = Scroller(content)
        assert scroller.get_content() is content

    def test_get_content_empty(self):
        from pyxflow.components import Scroller
        scroller = Scroller()
        assert scroller.get_content() is None

    def test_get_content_after_set(self):
        from pyxflow.components import Scroller
        from pyxflow.components.html import Div
        scroller = Scroller()
        tree = StateTree()
        scroller._attach(tree)
        new_content = Div("New")
        scroller.set_content(new_content)
        assert scroller.get_content() is new_content


class TestSideNavGetters:
    def test_is_collapsible_default(self):
        from pyxflow.components import SideNav
        nav = SideNav()
        assert nav.is_collapsible() is False

    def test_is_collapsible_after_set(self):
        from pyxflow.components import SideNav
        nav = SideNav()
        nav.set_collapsible(True)
        assert nav.is_collapsible() is True


class TestSideNavItemGetters:
    def test_is_expanded_default(self):
        from pyxflow.components import SideNavItem
        item = SideNavItem("Home", "/")
        assert item.is_expanded() is False

    def test_is_expanded_after_set(self):
        from pyxflow.components import SideNavItem
        item = SideNavItem("Home", "/")
        tree = StateTree()
        item._attach(tree)
        item.set_expanded(True)
        assert item.is_expanded() is True

    def test_is_expanded_before_attach(self):
        from pyxflow.components import SideNavItem
        item = SideNavItem("Home", "/")
        item.set_expanded(True)
        assert item.is_expanded() is True


class TestIconGetters:
    def test_get_color_default(self):
        from pyxflow.components import Icon
        icon = Icon("home")
        assert icon.get_color() is None

    def test_get_color_after_set(self):
        from pyxflow.components import Icon
        icon = Icon("home")
        icon.set_color("red")
        assert icon.get_color() == "red"


class TestDialogCloseProperties:
    def test_close_on_esc_default(self):
        from pyxflow.components import Dialog
        dlg = Dialog()
        assert dlg.is_close_on_esc() is True

    def test_close_on_esc_after_set(self):
        from pyxflow.components import Dialog
        dlg = Dialog()
        dlg.set_close_on_esc(False)
        assert dlg.is_close_on_esc() is False

    def test_close_on_outside_click_default(self):
        from pyxflow.components import Dialog
        dlg = Dialog()
        assert dlg.is_close_on_outside_click() is True

    def test_close_on_outside_click_after_set(self):
        from pyxflow.components import Dialog
        dlg = Dialog()
        dlg.set_close_on_outside_click(False)
        assert dlg.is_close_on_outside_click() is False

    def test_close_on_esc_property_sent_on_attach(self):
        from pyxflow.components import Dialog
        dlg = Dialog()
        dlg.set_close_on_esc(False)
        tree = StateTree()
        dlg._attach(tree)
        # Verify property was sent in changes
        changes = tree.collect_changes()
        close_on_esc_changes = [
            c for c in changes
            if c.get("key") == "closeOnEsc" and c.get("value") is False
        ]
        assert len(close_on_esc_changes) == 1

    def test_close_on_outside_click_property_sent_on_attach(self):
        from pyxflow.components import Dialog
        dlg = Dialog()
        dlg.set_close_on_outside_click(False)
        tree = StateTree()
        dlg._attach(tree)
        changes = tree.collect_changes()
        close_outside_changes = [
            c for c in changes
            if c.get("key") == "closeOnOutsideClick" and c.get("value") is False
        ]
        assert len(close_outside_changes) == 1
