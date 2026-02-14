"""Tests for CustomField component."""

import pytest

from vaadin.flow.components.custom_field import CustomField
from vaadin.flow.components.text_field import TextField
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestCustomField:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        cf = CustomField()
        assert cf._tag == "vaadin-custom-field"

    def test_create_default(self):
        cf = CustomField()
        assert cf._label == ""
        assert cf._children == []
        assert cf._value == ""

    def test_create_with_label(self):
        cf = CustomField("Phone")
        assert cf._label == "Phone"

    def test_set_label(self):
        cf = CustomField()
        cf.set_label("Address")
        assert cf.get_label() == "Address"

    def test_set_label_after_attach(self, tree):
        cf = CustomField()
        cf._attach(tree)
        tree.collect_changes()

        cf.set_label("Phone")
        changes = tree.collect_changes()
        labels = [c for c in changes if c.get("key") == "label"]
        assert any(c["value"] == "Phone" for c in labels)

    def test_add_children_before_attach(self):
        cf = CustomField()
        tf = TextField()
        cf.add(tf)
        assert len(cf._children) == 1

    def test_add_children_after_attach(self, tree):
        cf = CustomField()
        cf._attach(tree)
        tf = TextField()
        cf.add(tf)
        assert len(cf._children) == 1
        assert tf._element is not None

    def test_set_helper_text(self):
        cf = CustomField()
        cf.set_helper_text("Enter phone number")
        assert cf.get_helper_text() == "Enter phone number"

    def test_set_helper_text_after_attach(self, tree):
        cf = CustomField()
        cf._attach(tree)
        tree.collect_changes()

        cf.set_helper_text("Help")
        changes = tree.collect_changes()
        helper_changes = [c for c in changes if c.get("key") == "helperText"]
        assert any(c["value"] == "Help" for c in helper_changes)

    def test_set_error_message(self):
        cf = CustomField()
        cf.set_error_message("Required")
        assert cf.get_error_message() == "Required"

    def test_set_error_message_after_attach(self, tree):
        cf = CustomField()
        cf._attach(tree)
        tree.collect_changes()

        cf.set_error_message("Error!")
        changes = tree.collect_changes()
        error_changes = [c for c in changes if c.get("key") == "errorMessage"]
        assert any(c["value"] == "Error!" for c in error_changes)

    def test_set_invalid(self):
        cf = CustomField()
        cf.set_invalid(True)
        assert cf.is_invalid()

    def test_set_invalid_after_attach(self, tree):
        cf = CustomField()
        cf._attach(tree)
        tree.collect_changes()

        cf.set_invalid(True)
        changes = tree.collect_changes()
        invalid_changes = [c for c in changes if c.get("key") == "invalid"]
        assert any(c["value"] is True for c in invalid_changes)

    def test_set_value(self):
        cf = CustomField()
        cf.set_value("test")
        assert cf.get_value() == "test"

    def test_set_value_after_attach(self, tree):
        cf = CustomField()
        cf._attach(tree)
        tree.collect_changes()

        cf.set_value("+1\t555-1234")
        changes = tree.collect_changes()
        value_changes = [c for c in changes if c.get("key") == "value"]
        assert any(c["value"] == "+1\t555-1234" for c in value_changes)

    def test_value_change_listener(self, tree):
        cf = CustomField()
        cf._attach(tree)

        events = []
        cf.add_value_change_listener(lambda e: events.append(e))
        # Real protocol: mSync sets value first, then change event fires listeners
        cf._sync_property("value", "test")
        cf._handle_change({})
        assert len(events) == 1
        assert events[0]["value"] == "test"

    def test_value_change_listener_updates_internal(self, tree):
        cf = CustomField()
        cf._attach(tree)
        # Real protocol: mSync sets value first
        cf._sync_property("value", "updated")
        cf._handle_change({})
        assert cf._value == "updated"

    def test_sync_property_value(self):
        cf = CustomField()
        cf._sync_property("value", "hello")
        assert cf._value == "hello"

    def test_sync_property_value_none(self):
        cf = CustomField()
        cf._sync_property("value", None)
        assert cf._value == ""

    def test_change_event_registered(self, tree):
        cf = CustomField()
        cf._attach(tree)
        assert "change" in cf.element._listeners

    def test_attach_with_label(self, tree):
        cf = CustomField("Test Label")
        cf._attach(tree)

        changes = tree.collect_changes()
        labels = [c for c in changes if c.get("key") == "label"]
        assert any(c["value"] == "Test Label" for c in labels)

    def test_attach_with_helper_text(self, tree):
        cf = CustomField()
        cf.set_helper_text("Help text")
        cf._attach(tree)

        changes = tree.collect_changes()
        helper_changes = [c for c in changes if c.get("key") == "helperText"]
        assert any(c["value"] == "Help text" for c in helper_changes)

    def test_attach_with_invalid_and_error(self, tree):
        cf = CustomField()
        cf.set_invalid(True)
        cf.set_error_message("Error")
        cf._attach(tree)

        changes = tree.collect_changes()
        invalid_changes = [c for c in changes if c.get("key") == "invalid"]
        error_changes = [c for c in changes if c.get("key") == "errorMessage"]
        assert any(c["value"] is True for c in invalid_changes)
        assert any(c["value"] == "Error" for c in error_changes)

    def test_add_multiple_children(self, tree):
        cf = CustomField()
        tf1 = TextField()
        tf2 = TextField()
        cf.add(tf1, tf2)
        assert len(cf._children) == 2

    def test_children_attached_on_parent_attach(self, tree):
        cf = CustomField()
        tf = TextField()
        cf.add(tf)
        cf._attach(tree)
        assert tf._element is not None
