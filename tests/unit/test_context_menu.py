"""Tests for ContextMenu component."""

import pytest
from vaadin.flow.components import ContextMenu, ContextMenuItem, Span
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


@pytest.fixture
def tree():
    return StateTree()


class TestContextMenuItem:
    def test_text(self):
        item = ContextMenuItem("Edit")
        assert item.get_text() == "Edit"

    def test_set_text(self):
        item = ContextMenuItem("Edit")
        item.set_text("Delete")
        assert item.get_text() == "Delete"

    def test_enabled_default(self):
        item = ContextMenuItem("Edit")
        assert item.is_enabled() is True

    def test_disabled(self):
        item = ContextMenuItem("Edit")
        item.set_enabled(False)
        assert item.is_enabled() is False

    def test_checkable(self):
        item = ContextMenuItem("Toggle")
        item.set_checkable(True)
        assert item.is_checkable() is True

    def test_checked(self):
        item = ContextMenuItem("Toggle")
        item.set_checked(True)
        assert item.is_checked() is True

    def test_submenu(self):
        item = ContextMenuItem("Parent")
        sub = item.get_sub_menu()
        child = sub.add_item("Child")
        assert len(sub.get_items()) == 1
        assert child.get_text() == "Child"


class TestContextMenu:
    def test_tag(self, tree):
        menu = ContextMenu()
        menu._attach(tree)
        assert menu.element.node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-context-menu"

    def test_add_item(self, tree):
        menu = ContextMenu()
        item = menu.add_item("Edit")
        assert item.get_text() == "Edit"
        assert len(menu.get_items()) == 1

    def test_add_multiple_items(self, tree):
        menu = ContextMenu()
        menu.add_item("Edit")
        menu.add_item("Delete")
        menu.add_item("Copy")
        assert len(menu.get_items()) == 3

    def test_items_with_click_listener(self, tree):
        clicked = []
        menu = ContextMenu()
        menu.add_item("Edit", lambda e: clicked.append("edit"))
        menu._attach(tree)
        # Item nodes created, click listeners registered
        items = menu.get_items()
        assert items[0]._node is not None

    def test_add_separator(self, tree):
        menu = ContextMenu()
        menu.add_item("Edit")
        menu.add_separator()
        menu.add_item("Delete")
        menu._attach(tree)
        items = menu.get_items()
        assert len(items) == 3
        assert getattr(items[1], '_is_separator', False) is True

    def test_submenu(self, tree):
        menu = ContextMenu()
        parent = menu.add_item("Export")
        sub = parent.get_sub_menu()
        sub.add_item("PDF")
        sub.add_item("CSV")
        menu._attach(tree)
        assert parent._node is not None

    def test_set_target(self, tree):
        target = Span("Right-click me")
        target._attach(tree)
        menu = ContextMenu(target)
        menu.add_item("Action")
        menu._attach(tree)
        # Target's node should be a child of the context-menu
        assert target.element.node in menu.element.node._children

    def test_open_on_click(self, tree):
        menu = ContextMenu()
        menu.set_open_on_click(True)
        menu._attach(tree)
        assert menu.element.get_property("openOn") == "click"

    def test_open_on_click_after_attach(self, tree):
        menu = ContextMenu()
        menu._attach(tree)
        menu.set_open_on_click(True)
        assert menu.element.get_property("openOn") == "click"

    def test_disabled_item(self, tree):
        menu = ContextMenu()
        item = menu.add_item("Disabled")
        item.set_enabled(False)
        menu._attach(tree)
        assert item._node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "disabled") == ""

    def test_virtual_child_container(self, tree):
        """Context menu creates a virtual child container with inMemory payload."""
        menu = ContextMenu()
        menu.add_item("Test")
        menu._attach(tree)
        container = menu._container
        assert container.get(Feature.ELEMENT_DATA, "payload") == {"type": "inMemory"}

    def test_items_copy(self, tree):
        menu = ContextMenu()
        menu.add_item("A")
        items = menu.get_items()
        items.clear()
        assert len(menu.get_items()) == 1

    def test_no_items_no_error(self, tree):
        menu = ContextMenu()
        menu._attach(tree)
        assert menu.element is not None

    def test_separator_in_submenu(self, tree):
        menu = ContextMenu()
        parent = menu.add_item("File")
        sub = parent.get_sub_menu()
        sub.add_item("New")
        sub.add_separator()
        sub.add_item("Open")
        menu._attach(tree)
        assert len(sub.get_items()) == 3
