"""Tests for DrawerToggle component."""

import pytest

from pyflow.components.drawer_toggle import DrawerToggle
from pyflow.components.button import Button
from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature


class TestDrawerToggle:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        toggle = DrawerToggle()
        assert toggle._tag == "vaadin-drawer-toggle"

    def test_extends_button(self):
        toggle = DrawerToggle()
        assert isinstance(toggle, Button)

    def test_attach(self, tree):
        toggle = DrawerToggle()
        toggle._attach(tree)

        tag = toggle.element.node.get(Feature.ELEMENT_DATA, "tag")
        assert tag == "vaadin-drawer-toggle"

    def test_click_listener(self, tree):
        toggle = DrawerToggle()
        clicked = []
        toggle.add_click_listener(lambda e: clicked.append(True))
        toggle._attach(tree)

        toggle.element.fire_event("click", {})
        assert len(clicked) == 1

    def test_with_text(self, tree):
        toggle = DrawerToggle("Menu")
        toggle._attach(tree)

        changes = tree.collect_changes()
        text_changes = [c for c in changes if c.get("feat") == Feature.TEXT_NODE]
        assert any(c["value"] == "Menu" for c in text_changes)
