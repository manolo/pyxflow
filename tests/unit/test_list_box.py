"""Tests for ListBox and MultiSelectListBox components."""

import pytest

from pyxflow.components.list_box import ListBox, MultiSelectListBox
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature


class TestListBox:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        lb = ListBox()
        assert lb._tag == "vaadin-list-box"

    def test_create(self):
        lb = ListBox()
        assert lb._items == []
        assert lb._value is None

    def test_set_items(self):
        lb = ListBox()
        lb.set_items("A", "B", "C")
        assert lb._items == ["A", "B", "C"]

    def test_get_items(self):
        lb = ListBox()
        lb.set_items("A", "B")
        items = lb.get_items()
        assert items == ["A", "B"]
        items.append("C")
        assert lb._items == ["A", "B"]

    def test_attach_creates_item_children(self, tree):
        lb = ListBox()
        lb.set_items("Item 1", "Item 2")
        lb._attach(tree)

        changes = tree.collect_changes()
        item_tags = [
            c for c in changes
            if c.get("key") == "tag" and c.get("value") == "vaadin-item"
        ]
        assert len(item_tags) == 2

    def test_attach_creates_text_nodes(self, tree):
        lb = ListBox()
        lb.set_items("Hello")
        lb._attach(tree)

        changes = tree.collect_changes()
        text_nodes = [
            c for c in changes
            if c.get("key") == "text" and c.get("feat") == Feature.TEXT_NODE
        ]
        assert len(text_nodes) == 1
        assert text_nodes[0]["value"] == "Hello"

    def test_set_value(self):
        lb = ListBox()
        lb.set_items("A", "B", "C")
        lb.set_value("B")
        assert lb._value == "B"

    def test_set_value_after_attach(self, tree):
        lb = ListBox()
        lb.set_items("A", "B", "C")
        lb._attach(tree)
        tree.collect_changes()

        lb.set_value("B")
        changes = tree.collect_changes()
        selected_changes = [c for c in changes if c.get("key") == "selected"]
        assert any(c["value"] == 1 for c in selected_changes)

    def test_set_value_none(self, tree):
        lb = ListBox()
        lb.set_items("A", "B")
        lb._attach(tree)
        lb.set_value("A")
        tree.collect_changes()

        lb.set_value(None)
        changes = tree.collect_changes()
        selected_changes = [c for c in changes if c.get("key") == "selected"]
        assert selected_changes[-1]["value"] == -1

    def test_get_value(self):
        lb = ListBox()
        assert lb.get_value() is None
        lb.set_items("A", "B")
        lb.set_value("A")
        assert lb.get_value() == "A"

    def test_value_change_listener(self, tree):
        lb = ListBox()
        lb.set_items("A", "B", "C")
        lb._attach(tree)

        events = []
        lb.add_value_change_listener(lambda e: events.append(e))
        # Selection arrives via mSync -> _sync_property
        lb._sync_property("selected", 1)
        assert len(events) == 1
        assert events[0]["value"] == "B"

    def test_value_change_listener_invalid_index(self, tree):
        lb = ListBox()
        lb.set_items("A")
        lb._attach(tree)

        events = []
        lb.add_value_change_listener(lambda e: events.append(e))
        # First select a valid item
        lb._sync_property("selected", 0)
        assert len(events) == 1
        assert events[0]["value"] == "A"
        # Then select an invalid index — value goes back to None
        lb._sync_property("selected", 99)
        assert len(events) == 2
        assert events[1]["value"] is None

    def test_item_label_generator(self, tree):
        lb = ListBox()
        lb.set_item_label_generator(lambda x: x.upper())
        lb.set_items("hello", "world")
        lb._attach(tree)

        changes = tree.collect_changes()
        text_nodes = [
            c for c in changes
            if c.get("key") == "text" and c.get("feat") == Feature.TEXT_NODE
        ]
        labels = [t["value"] for t in text_nodes]
        assert "HELLO" in labels
        assert "WORLD" in labels

    def test_item_enabled_provider(self, tree):
        lb = ListBox()
        lb.set_item_enabled_provider(lambda x: x != "B")
        lb.set_items("A", "B", "C")
        lb._attach(tree)

        changes = tree.collect_changes()
        disabled_changes = [
            c for c in changes
            if c.get("key") == "disabled" and c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
        ]
        assert len(disabled_changes) == 1

    def test_sync_property_selected(self):
        lb = ListBox()
        lb.set_items("A", "B")
        lb._sync_property("selected", 0)
        assert lb._value == "A"

    def test_sync_property_selected_out_of_range(self):
        lb = ListBox()
        lb.set_items("A", "B")
        lb._sync_property("selected", 99)
        assert lb._value is None

    def test_selected_changed_registers_listener(self, tree):
        lb = ListBox()
        lb._attach(tree)
        assert "selected-changed" in lb.element._listeners

    def test_set_value_before_attach(self, tree):
        lb = ListBox()
        lb.set_items("A", "B", "C")
        lb.set_value("C")
        lb._attach(tree)

        changes = tree.collect_changes()
        selected_changes = [c for c in changes if c.get("key") == "selected"]
        assert any(c["value"] == 2 for c in selected_changes)

    def test_no_items_no_children(self, tree):
        lb = ListBox()
        lb._attach(tree)

        changes = tree.collect_changes()
        item_tags = [
            c for c in changes
            if c.get("key") == "tag" and c.get("value") == "vaadin-item"
        ]
        assert len(item_tags) == 0


class TestMultiSelectListBox:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        lb = MultiSelectListBox()
        assert lb._tag == "vaadin-list-box"

    def test_create(self):
        lb = MultiSelectListBox()
        assert lb._items == []
        assert lb._value == set()

    def test_set_items(self):
        lb = MultiSelectListBox()
        lb.set_items("A", "B", "C")
        assert lb._items == ["A", "B", "C"]

    def test_multiple_property_set_on_attach(self, tree):
        lb = MultiSelectListBox()
        lb._attach(tree)

        changes = tree.collect_changes()
        multiple_changes = [
            c for c in changes
            if c.get("key") == "multiple" and c.get("value") is True
        ]
        assert len(multiple_changes) == 1

    def test_attach_creates_items(self, tree):
        lb = MultiSelectListBox()
        lb.set_items("X", "Y")
        lb._attach(tree)

        changes = tree.collect_changes()
        item_tags = [
            c for c in changes
            if c.get("key") == "tag" and c.get("value") == "vaadin-item"
        ]
        assert len(item_tags) == 2

    def test_set_value(self):
        lb = MultiSelectListBox()
        lb.set_items("A", "B", "C")
        lb.set_value({"A", "C"})
        assert lb._value == {"A", "C"}

    def test_set_value_after_attach(self, tree):
        lb = MultiSelectListBox()
        lb.set_items("A", "B", "C")
        lb._attach(tree)
        tree.collect_changes()

        lb.set_value({"A", "C"})
        changes = tree.collect_changes()
        selected_changes = [c for c in changes if c.get("key") == "selectedValues"]
        assert len(selected_changes) > 0
        indices = set(selected_changes[-1]["value"])
        assert indices == {0, 2}

    def test_get_value_returns_copy(self):
        lb = MultiSelectListBox()
        lb.set_items("A", "B")
        lb.set_value({"A"})
        v = lb.get_value()
        v.add("B")
        assert lb._value == {"A"}

    def test_value_change_listener(self, tree):
        lb = MultiSelectListBox()
        lb.set_items("A", "B", "C")
        lb._attach(tree)

        events = []
        lb.add_value_change_listener(lambda e: events.append(e))
        # Selection arrives via mSync -> _sync_property
        lb._sync_property("selectedValues", [0, 2])
        assert len(events) == 1
        assert events[0]["value"] == {"A", "C"}

    def test_sync_property(self):
        lb = MultiSelectListBox()
        lb.set_items("A", "B", "C")
        lb._sync_property("selectedValues", [1])
        assert lb._value == {"B"}

    def test_sync_property_empty_list(self):
        lb = MultiSelectListBox()
        lb.set_items("A", "B")
        lb._sync_property("selectedValues", [])
        assert lb._value == set()

    def test_selected_values_changed_listener(self, tree):
        lb = MultiSelectListBox()
        lb._attach(tree)
        assert "selected-values-changed" in lb.element._listeners

    def test_item_label_generator(self, tree):
        lb = MultiSelectListBox()
        lb.set_item_label_generator(lambda x: f"[{x}]")
        lb.set_items("a", "b")
        lb._attach(tree)

        changes = tree.collect_changes()
        text_nodes = [
            c for c in changes
            if c.get("key") == "text" and c.get("feat") == Feature.TEXT_NODE
        ]
        labels = [t["value"] for t in text_nodes]
        assert "[a]" in labels
        assert "[b]" in labels

    def test_get_items_returns_copy(self):
        lb = MultiSelectListBox()
        lb.set_items("X", "Y")
        items = lb.get_items()
        items.append("Z")
        assert lb._items == ["X", "Y"]

    def test_no_items_no_children(self, tree):
        lb = MultiSelectListBox()
        lb._attach(tree)

        changes = tree.collect_changes()
        item_tags = [
            c for c in changes
            if c.get("key") == "tag" and c.get("value") == "vaadin-item"
        ]
        assert len(item_tags) == 0
