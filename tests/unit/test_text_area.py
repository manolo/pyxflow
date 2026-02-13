"""Tests for TextArea component."""

import pytest

from vaadin.flow.components import TextArea
from vaadin.flow.core.state_tree import StateTree


class TestTextArea:
    """Test TextArea component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_text_area_without_label(self):
        """TextArea can be created without a label."""
        text_area = TextArea()
        assert text_area.get_label() == ""
        assert text_area.get_value() == ""

    def test_create_text_area_with_label(self):
        """TextArea can be created with a label."""
        text_area = TextArea("Description")
        assert text_area.get_label() == "Description"

    def test_text_area_tag(self):
        """TextArea has correct tag."""
        text_area = TextArea()
        assert text_area._tag == "vaadin-text-area"

    def test_set_value(self, tree):
        """set_value updates the value."""
        text_area = TextArea("Comment")
        text_area._attach(tree)

        text_area.set_value("Hello\nWorld")
        assert text_area.get_value() == "Hello\nWorld"

    def test_value_property(self, tree):
        """value property works correctly."""
        text_area = TextArea("Comment")
        text_area._attach(tree)

        text_area.value = "Multi\nline\ntext"
        assert text_area.value == "Multi\nline\ntext"

    def test_set_label(self, tree):
        """set_label updates the label."""
        text_area = TextArea()
        text_area._attach(tree)

        text_area.set_label("New label")
        assert text_area.get_label() == "New label"

    def test_set_placeholder(self, tree):
        """set_placeholder updates the placeholder."""
        text_area = TextArea("Comment")
        text_area._attach(tree)

        text_area.set_placeholder("Enter your comment here...")
        assert text_area.get_placeholder() == "Enter your comment here..."

    def test_value_change_listener(self, tree):
        """Value change listener is called on change."""
        text_area = TextArea("Comment")
        text_area._attach(tree)

        received_events = []

        def listener(event):
            received_events.append(event)

        text_area.add_value_change_listener(listener)

        # Simulate change event from client
        text_area._handle_change({"value": "New value"})

        assert len(received_events) == 1
        assert text_area.get_value() == "New value"

    def test_sync_property(self, tree):
        """_sync_property updates internal state."""
        text_area = TextArea("Comment")
        text_area._attach(tree)

        text_area._sync_property("value", "Synced value")
        assert text_area.get_value() == "Synced value"

    def test_attach_sets_properties(self, tree):
        """Attach sets initial properties on element."""
        text_area = TextArea("Description")
        text_area._attach(tree)

        changes = tree.collect_changes()

        # Find label property change
        label_change = next(
            (c for c in changes if c.get("key") == "label" and c.get("value") == "Description"),
            None
        )
        assert label_change is not None

        # Find value property change
        value_change = next(
            (c for c in changes if c.get("key") == "value"),
            None
        )
        assert value_change is not None
