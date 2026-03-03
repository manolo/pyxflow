"""Tests for AppLayout component."""

import pytest

from pyxflow.components.app_layout import AppLayout
from pyxflow.components.constants import AppLayoutSection
from pyxflow.components.button import Button
from pyxflow.components.drawer_toggle import DrawerToggle
from pyxflow.components.icon import Icon
from pyxflow.components.side_nav import SideNav, SideNavItem
from pyxflow.components.html import H1, Div
from pyxflow.components.vertical_layout import VerticalLayout
from pyxflow.core.component import UI
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature


class TestAppLayout:

    @pytest.fixture
    def tree(self):
        return StateTree()

    @pytest.fixture
    def ui(self, tree):
        return UI(tree)

    def test_tag(self):
        layout = AppLayout()
        assert layout._tag == "vaadin-app-layout"

    def test_is_router_layout(self):
        assert AppLayout._is_router_layout is True

    def test_attach_basic(self, tree):
        layout = AppLayout()
        layout._attach(tree)

        tag = layout.element.node.get(Feature.ELEMENT_DATA, "tag")
        assert tag == "vaadin-app-layout"

    def test_drawer_opened_default(self, tree):
        layout = AppLayout()
        layout._attach(tree)

        prop = layout.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "drawerOpened")
        assert prop is True

    def test_add_to_navbar(self, tree, ui):
        layout = AppLayout()
        layout._ui = ui
        layout._attach(tree)

        toggle = DrawerToggle()
        title = H1("My App")
        layout.add_to_navbar(toggle, title)

        slot_toggle = toggle.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        slot_title = title.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        assert slot_toggle == "navbar"
        assert slot_title == "navbar"

    def test_add_to_drawer(self, tree, ui):
        layout = AppLayout()
        layout._ui = ui
        layout._attach(tree)

        nav = SideNav()
        layout.add_to_drawer(nav)

        slot = nav.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        assert slot == "drawer"

    def test_set_content(self, tree, ui):
        layout = AppLayout()
        layout._ui = ui
        layout._attach(tree)

        content = Div("Hello")
        layout.set_content(content)

        # Content should be a child but NOT have a slot attribute
        assert content.element.node in layout.element.node._children
        slot = content.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        assert slot is None

    def test_set_content_replaces_previous(self, tree, ui):
        layout = AppLayout()
        layout._ui = ui
        layout._attach(tree)

        old = Div("Old")
        layout.set_content(old)
        assert old.element.node in layout.element.node._children

        new = Div("New")
        layout.set_content(new)
        assert old.element.node not in layout.element.node._children
        assert new.element.node in layout.element.node._children

    def test_get_content(self, tree, ui):
        layout = AppLayout()
        layout._ui = ui
        layout._attach(tree)

        assert layout.get_content() is None

        content = Div("Test")
        layout.set_content(content)
        assert layout.get_content() is content

    def test_navbar_components_before_attach(self, tree, ui):
        layout = AppLayout()
        layout._ui = ui
        toggle = DrawerToggle()
        title = H1("Title")
        layout.add_to_navbar(toggle, title)
        layout._attach(tree)

        slot_toggle = toggle.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        slot_title = title.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        assert slot_toggle == "navbar"
        assert slot_title == "navbar"

    def test_drawer_components_before_attach(self, tree, ui):
        layout = AppLayout()
        layout._ui = ui
        nav = SideNav()
        layout.add_to_drawer(nav)
        layout._attach(tree)

        slot = nav.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        assert slot == "drawer"

    def test_set_drawer_opened(self, tree):
        layout = AppLayout()
        layout._attach(tree)
        tree.collect_changes()

        layout.set_drawer_opened(False)
        changes = tree.collect_changes()
        prop_changes = [c for c in changes if c.get("key") == "drawerOpened"]
        assert any(c["value"] is False for c in prop_changes)

    def test_set_primary_section(self, tree):
        layout = AppLayout()
        layout._attach(tree)
        tree.collect_changes()

        layout.set_primary_section("drawer")
        changes = tree.collect_changes()
        prop_changes = [c for c in changes if c.get("key") == "primarySection"]
        assert any(c["value"] == "drawer" for c in prop_changes)

    def test_section_enum_values(self):
        assert AppLayout.Section.NAVBAR.value == "navbar"
        assert AppLayout.Section.DRAWER.value == "drawer"
        # Enum is accessible both from class and from constants
        assert AppLayout.Section is AppLayoutSection
        assert AppLayoutSection.NAVBAR == "navbar"
        assert AppLayoutSection.DRAWER == "drawer"

    def test_section_enum_from_string(self):
        assert AppLayoutSection("navbar") == AppLayoutSection.NAVBAR
        assert AppLayoutSection("drawer") == AppLayoutSection.DRAWER

    def test_set_primary_section_with_enum(self, tree):
        layout = AppLayout()
        layout._attach(tree)
        tree.collect_changes()

        layout.set_primary_section(AppLayout.Section.DRAWER)
        changes = tree.collect_changes()
        prop_changes = [c for c in changes if c.get("key") == "primarySection"]
        assert any(c["value"] == "drawer" for c in prop_changes)

    def test_get_primary_section_returns_enum(self):
        layout = AppLayout()
        assert layout.get_primary_section() == AppLayoutSection.NAVBAR
        layout.set_primary_section("drawer")
        assert layout.get_primary_section() == AppLayoutSection.DRAWER

    def test_primary_section_before_attach(self, tree):
        """Setting primary section before attach should flush in _attach()."""
        layout = AppLayout()
        layout.set_primary_section(AppLayout.Section.DRAWER)
        layout._attach(tree)

        prop = layout.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "primarySection")
        assert prop == "drawer"

    def test_drawer_opened_false_before_attach(self, tree):
        """Setting drawer closed before attach should flush in _attach()."""
        layout = AppLayout()
        layout.set_drawer_opened(False)
        layout._attach(tree)

        prop = layout.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "drawerOpened")
        assert prop is False

    def test_is_drawer_opened(self):
        layout = AppLayout()
        assert layout.is_drawer_opened() is True
        layout.set_drawer_opened(False)
        assert layout.is_drawer_opened() is False

    def test_show_router_layout_content(self, tree, ui):
        layout = AppLayout()
        layout._ui = ui
        layout._attach(tree)

        view = Div("View")
        layout.show_router_layout_content(view)
        assert layout.get_content() is view

    def test_remove_router_layout_content(self, tree, ui):
        layout = AppLayout()
        layout._ui = ui
        layout._attach(tree)

        view = Div("View")
        layout.show_router_layout_content(view)
        layout.remove_router_layout_content(view)
        assert layout.get_content() is None
        assert view.element.node not in layout.element.node._children
