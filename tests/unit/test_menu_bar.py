"""Tests for MenuBar component."""

import pytest

from pyflow.components.menu_bar import MenuBar, MenuItem, SubMenu
from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature


class TestMenuItem:

    def test_create(self):
        item = MenuItem("File")
        assert item.get_text() == "File"
        assert item.is_enabled()
        assert not item.is_checkable()
        assert not item.is_checked()

    def test_create_with_click_listener(self):
        listener = lambda e: None
        item = MenuItem("Click", listener)
        assert item._click_listener is listener

    def test_set_text(self):
        item = MenuItem("Old")
        item.set_text("New")
        assert item.get_text() == "New"

    def test_set_enabled(self):
        item = MenuItem("Test")
        item.set_enabled(False)
        assert not item.is_enabled()

    def test_checkable(self):
        item = MenuItem("Check")
        item.set_checkable(True)
        assert item.is_checkable()
        item.set_checked(True)
        assert item.is_checked()

    def test_is_parent_item(self):
        item = MenuItem("File")
        assert not item.is_parent_item()
        item.get_sub_menu().add_item("New")
        assert item.is_parent_item()


class TestSubMenu:

    def test_add_item(self):
        parent = MenuItem("File")
        sub = parent.get_sub_menu()
        child = sub.add_item("New")
        assert isinstance(child, MenuItem)
        assert child.get_text() == "New"
        assert len(parent._children) == 1

    def test_add_item_with_listener(self):
        parent = MenuItem("File")
        listener = lambda e: None
        child = parent.get_sub_menu().add_item("New", listener)
        assert child._click_listener is listener

    def test_get_items(self):
        parent = MenuItem("File")
        sub = parent.get_sub_menu()
        sub.add_item("New")
        sub.add_item("Open")
        items = sub.get_items()
        assert len(items) == 2
        assert items[0].get_text() == "New"
        assert items[1].get_text() == "Open"

    def test_get_items_returns_copy(self):
        parent = MenuItem("File")
        sub = parent.get_sub_menu()
        sub.add_item("New")
        items = sub.get_items()
        items.append(MenuItem("Extra"))
        assert len(parent._children) == 1


class TestMenuBar:

    @pytest.fixture
    def tree(self):
        tree = StateTree()
        tree._app_id = "ROOT-1234567"
        return tree

    def test_create(self):
        mb = MenuBar()
        assert mb._tag == "vaadin-menu-bar"
        assert mb.get_items() == []

    def test_add_item(self):
        mb = MenuBar()
        item = mb.add_item("File")
        assert isinstance(item, MenuItem)
        assert item.get_text() == "File"
        assert len(mb.get_items()) == 1

    def test_add_item_with_listener(self):
        mb = MenuBar()
        listener = lambda e: None
        item = mb.add_item("Help", listener)
        assert item._click_listener is listener

    def test_get_items_returns_copy(self):
        mb = MenuBar()
        mb.add_item("File")
        items = mb.get_items()
        items.append(MenuItem("Extra"))
        assert len(mb.get_items()) == 1

    def test_connector_init(self, tree):
        mb = MenuBar()
        mb.add_item("File")
        mb._attach(tree)

        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("menubarConnector.initLazy" in js for js in js_strings)

    def test_connector_init_uses_client_key(self, tree):
        mb = MenuBar()
        mb.add_item("File")
        mb._attach(tree)

        execute = tree.collect_execute()
        init_cmd = [cmd for cmd in execute if "menubarConnector.initLazy" in cmd[-1]][0]
        # Second arg should be "ROOT" (client key), not full "ROOT-1234567"
        assert init_cmd[1] == "ROOT"

    def test_generate_items_called(self, tree):
        mb = MenuBar()
        mb.add_item("File")
        mb._attach(tree)

        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("generateItems" in js for js in js_strings)

    def test_item_nodes_created(self, tree):
        mb = MenuBar()
        mb.add_item("File")
        mb.add_item("Edit")
        mb._attach(tree)

        changes = tree.collect_changes()
        tag_changes = [c for c in changes if c.get("key") == "tag" and c.get("feat") == Feature.ELEMENT_DATA]
        tags = [c["value"] for c in tag_changes]
        assert "vaadin-menu-bar" in tags
        assert tags.count("vaadin-menu-bar-item") == 2
        # Container divs
        assert tags.count("div") >= 2

    def test_item_text_nodes(self, tree):
        mb = MenuBar()
        mb.add_item("File")
        mb._attach(tree)

        changes = tree.collect_changes()
        text_changes = [c for c in changes if c.get("feat") == Feature.TEXT_NODE]
        assert any(c["value"] == "File" for c in text_changes)

    def test_submenu_creates_container(self, tree):
        mb = MenuBar()
        file_item = mb.add_item("File")
        file_item.get_sub_menu().add_item("New")
        file_item.get_sub_menu().add_item("Open")
        mb._attach(tree)

        changes = tree.collect_changes()
        # The file item should have _containerNodeId property
        container_props = [c for c in changes if c.get("key") == "_containerNodeId"]
        assert len(container_props) == 1
        assert isinstance(container_props[0]["value"], int)

    def test_submenu_item_nodes(self, tree):
        mb = MenuBar()
        file_item = mb.add_item("File")
        file_item.get_sub_menu().add_item("New")
        file_item.get_sub_menu().add_item("Open")
        mb._attach(tree)

        changes = tree.collect_changes()
        text_changes = [c for c in changes if c.get("feat") == Feature.TEXT_NODE]
        texts = [c["value"] for c in text_changes]
        assert "File" in texts
        assert "New" in texts
        assert "Open" in texts

    def test_disabled_item(self, tree):
        mb = MenuBar()
        item = mb.add_item("File")
        item.set_enabled(False)
        mb._attach(tree)

        changes = tree.collect_changes()
        disabled = [c for c in changes if c.get("key") == "disabled" and c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP]
        assert len(disabled) == 1

    def test_open_on_hover(self, tree):
        mb = MenuBar()
        mb.set_open_on_hover(True)
        mb._attach(tree)

        changes = tree.collect_changes()
        hover = [c for c in changes if c.get("key") == "openOnHover"]
        assert any(c["value"] is True for c in hover)

    def test_open_on_hover_after_attach(self, tree):
        mb = MenuBar()
        mb._attach(tree)
        tree.collect_changes()

        mb.set_open_on_hover(True)
        changes = tree.collect_changes()
        hover = [c for c in changes if c.get("key") == "openOnHover"]
        assert any(c["value"] is True for c in hover)

    def test_click_listener_registered(self, tree):
        events = []
        mb = MenuBar()
        mb.add_item("Help", lambda e: events.append(e))
        mb._attach(tree)

        # Find the registered element for the item
        item = mb._items[0]
        element = tree.get_element(item._node.id)
        assert element is not None
        element.fire_event("click", {"test": True})
        assert len(events) == 1

    def test_virtual_children_splice(self, tree):
        mb = MenuBar()
        mb.add_item("File")
        mb._attach(tree)

        changes = tree.collect_changes()
        virtual_splices = [c for c in changes if c.get("feat") == Feature.VIRTUAL_CHILDREN_LIST]
        assert len(virtual_splices) == 1

    def test_generate_items_gets_container_node_id(self, tree):
        mb = MenuBar()
        mb.add_item("File")
        mb._attach(tree)

        execute = tree.collect_execute()
        gen_cmd = [cmd for cmd in execute if "generateItems" in cmd[-1]][0]
        # Second arg should be a node ID (int)
        assert isinstance(gen_cmd[1], int)

    def test_container_has_in_memory_payload(self, tree):
        """Virtual child container must have payload: {"type": "inMemory"} on Feature 0."""
        mb = MenuBar()
        mb.add_item("File")
        mb._attach(tree)

        changes = tree.collect_changes()
        # Find the payload change on the container node
        payload_changes = [c for c in changes if c.get("key") == "payload" and c.get("feat") == Feature.ELEMENT_DATA]
        assert len(payload_changes) == 1
        assert payload_changes[0]["value"] == {"type": "inMemory"}

    def test_submenu_container_attached_to_main_container(self, tree):
        """Sub-containers for submenus should be children of the main container."""
        mb = MenuBar()
        file_item = mb.add_item("File")
        file_item.get_sub_menu().add_item("New")
        mb._attach(tree)

        # The main container should have at least 2 children:
        # the root sub-container and the File submenu sub-container
        container = mb._container
        children_splices = [c for c in tree.collect_changes()
                          if c.get("node") == container.id
                          and c.get("type") == "splice"
                          and c.get("feat") == Feature.ELEMENT_CHILDREN_LIST]
        assert len(children_splices) >= 2


class TestMenuItemKeepOpen:
    """Tests for MenuItem.set_keep_open / is_keep_open."""

    def test_default_is_false(self):
        item = MenuItem("Test")
        assert item.is_keep_open() is False

    def test_set_keep_open_true(self):
        item = MenuItem("Test")
        item.set_keep_open(True)
        assert item.is_keep_open() is True

    def test_set_keep_open_false(self):
        item = MenuItem("Test")
        item.set_keep_open(True)
        item.set_keep_open(False)
        assert item.is_keep_open() is False

    def test_keep_open_creates_node_property(self):
        tree = StateTree()
        tree._app_id = "ROOT-1234567"

        mb = MenuBar()
        item = mb.add_item("Stay Open")
        item.set_keep_open(True)
        mb._attach(tree)

        changes = tree.collect_changes()
        keep_open = [c for c in changes
                     if c.get("key") == "keepOpen"
                     and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert len(keep_open) == 1
        assert keep_open[0]["value"] is True

    def test_keep_open_false_no_property(self):
        """When keep_open is False (default), no keepOpen property should be emitted."""
        tree = StateTree()
        tree._app_id = "ROOT-1234567"

        mb = MenuBar()
        mb.add_item("Normal")
        mb._attach(tree)

        changes = tree.collect_changes()
        keep_open = [c for c in changes
                     if c.get("key") == "keepOpen"
                     and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert len(keep_open) == 0


class TestMenuItemDisableOnClick:
    """Tests for MenuItem.set_disable_on_click / is_disable_on_click."""

    def test_default_is_false(self):
        item = MenuItem("Test")
        assert item.is_disable_on_click() is False

    def test_set_disable_on_click_true(self):
        item = MenuItem("Test")
        item.set_disable_on_click(True)
        assert item.is_disable_on_click() is True

    def test_set_disable_on_click_false(self):
        item = MenuItem("Test")
        item.set_disable_on_click(True)
        item.set_disable_on_click(False)
        assert item.is_disable_on_click() is False

    def test_disable_on_click_creates_node_property(self):
        tree = StateTree()
        tree._app_id = "ROOT-1234567"

        mb = MenuBar()
        item = mb.add_item("Once")
        item.set_disable_on_click(True)
        mb._attach(tree)

        changes = tree.collect_changes()
        disable = [c for c in changes
                   if c.get("key") == "disableOnClick"
                   and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert len(disable) == 1
        assert disable[0]["value"] is True

    def test_disable_on_click_false_no_property(self):
        """When disable_on_click is False (default), no property emitted."""
        tree = StateTree()
        tree._app_id = "ROOT-1234567"

        mb = MenuBar()
        mb.add_item("Normal")
        mb._attach(tree)

        changes = tree.collect_changes()
        disable = [c for c in changes
                   if c.get("key") == "disableOnClick"
                   and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert len(disable) == 0


class TestMenuItemAriaLabel:
    """Tests for MenuItem.set_aria_label / get_aria_label."""

    def test_default_is_none(self):
        item = MenuItem("Test")
        assert item.get_aria_label() is None

    def test_set_aria_label(self):
        item = MenuItem("Test")
        item.set_aria_label("Open file menu")
        assert item.get_aria_label() == "Open file menu"

    def test_aria_label_creates_node_property(self):
        tree = StateTree()
        tree._app_id = "ROOT-1234567"

        mb = MenuBar()
        item = mb.add_item("File")
        item.set_aria_label("File menu")
        mb._attach(tree)

        changes = tree.collect_changes()
        aria = [c for c in changes
                if c.get("key") == "ariaLabel"
                and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert len(aria) == 1
        assert aria[0]["value"] == "File menu"

    def test_no_aria_label_no_property(self):
        """When aria_label is not set, no ariaLabel property should be emitted."""
        tree = StateTree()
        tree._app_id = "ROOT-1234567"

        mb = MenuBar()
        mb.add_item("Normal")
        mb._attach(tree)

        changes = tree.collect_changes()
        aria = [c for c in changes
                if c.get("key") == "ariaLabel"
                and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert len(aria) == 0


class TestSubMenuSeparator:
    """Tests for SubMenu.add_separator."""

    def test_add_separator(self):
        parent = MenuItem("File")
        sub = parent.get_sub_menu()
        sep = sub.add_separator()
        assert isinstance(sep, MenuItem)
        assert sep._is_separator is True
        assert sep.get_text() == ""

    def test_separator_in_items_list(self):
        parent = MenuItem("File")
        sub = parent.get_sub_menu()
        sub.add_item("New")
        sub.add_separator()
        sub.add_item("Open")
        items = sub.get_items()
        assert len(items) == 3
        assert items[1]._is_separator is True

    def test_separator_creates_node_property(self):
        tree = StateTree()
        tree._app_id = "ROOT-1234567"

        mb = MenuBar()
        file_item = mb.add_item("File")
        file_item.get_sub_menu().add_item("New")
        file_item.get_sub_menu().add_separator()
        file_item.get_sub_menu().add_item("Open")
        mb._attach(tree)

        changes = tree.collect_changes()
        sep_props = [c for c in changes
                     if c.get("key") == "separator"
                     and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert len(sep_props) == 1
        assert sep_props[0]["value"] is True


class TestSubMenuRemove:
    """Tests for SubMenu.remove and SubMenu.remove_all."""

    def test_remove_single_item(self):
        parent = MenuItem("File")
        sub = parent.get_sub_menu()
        item1 = sub.add_item("New")
        item2 = sub.add_item("Open")
        sub.remove(item1)
        items = sub.get_items()
        assert len(items) == 1
        assert items[0] is item2

    def test_remove_multiple_items(self):
        parent = MenuItem("File")
        sub = parent.get_sub_menu()
        item1 = sub.add_item("New")
        item2 = sub.add_item("Open")
        item3 = sub.add_item("Save")
        sub.remove(item1, item3)
        items = sub.get_items()
        assert len(items) == 1
        assert items[0] is item2

    def test_remove_nonexistent_item(self):
        """Removing an item not in the submenu should not raise an error."""
        parent = MenuItem("File")
        sub = parent.get_sub_menu()
        sub.add_item("New")
        other_item = MenuItem("Other")
        sub.remove(other_item)  # should not raise
        assert len(sub.get_items()) == 1

    def test_remove_all(self):
        parent = MenuItem("File")
        sub = parent.get_sub_menu()
        sub.add_item("New")
        sub.add_item("Open")
        sub.add_item("Save")
        assert len(sub.get_items()) == 3
        sub.remove_all()
        assert len(sub.get_items()) == 0

    def test_remove_all_empty(self):
        """remove_all on empty submenu should not raise."""
        parent = MenuItem("File")
        sub = parent.get_sub_menu()
        sub.remove_all()
        assert len(sub.get_items()) == 0
