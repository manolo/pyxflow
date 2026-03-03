"""Tests for Checkbox component."""

import pytest

from pyxflow.components import Checkbox
from pyxflow.core.state_tree import StateTree


class TestCheckbox:
    """Test Checkbox component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_checkbox_without_label(self):
        """Checkbox can be created without a label."""
        checkbox = Checkbox()
        assert checkbox.get_label() == ""
        assert checkbox.is_checked() is False

    def test_create_checkbox_with_label(self):
        """Checkbox can be created with a label."""
        checkbox = Checkbox("Accept terms")
        assert checkbox.get_label() == "Accept terms"

    def test_checkbox_tag(self):
        """Checkbox has correct tag."""
        checkbox = Checkbox()
        assert checkbox._tag == "vaadin-checkbox"

    def test_set_checked(self, tree):
        """set_checked updates the checked state."""
        checkbox = Checkbox("Test")
        checkbox._attach(tree)

        checkbox.set_checked(True)
        assert checkbox.is_checked() is True

        checkbox.set_checked(False)
        assert checkbox.is_checked() is False

    def test_value_property(self, tree):
        """value property is alias for checked state."""
        checkbox = Checkbox("Test")
        checkbox._attach(tree)

        checkbox.value = True
        assert checkbox.value is True
        assert checkbox.is_checked() is True

    def test_get_set_value(self, tree):
        """get_value/set_value work correctly."""
        checkbox = Checkbox("Test")
        checkbox._attach(tree)

        checkbox.set_value(True)
        assert checkbox.get_value() is True

    def test_set_label(self, tree):
        """set_label updates the label."""
        checkbox = Checkbox()
        checkbox._attach(tree)

        checkbox.set_label("New label")
        assert checkbox.get_label() == "New label"

    def test_indeterminate_state(self, tree):
        """Indeterminate state can be set and retrieved."""
        checkbox = Checkbox("Test")
        checkbox._attach(tree)

        checkbox.set_indeterminate(True)
        assert checkbox.is_indeterminate() is True

        checkbox.set_indeterminate(False)
        assert checkbox.is_indeterminate() is False

    def test_set_checked_clears_indeterminate(self, tree):
        """Setting checked clears indeterminate state."""
        checkbox = Checkbox("Test")
        checkbox._attach(tree)

        checkbox.set_indeterminate(True)
        assert checkbox.is_indeterminate() is True

        checkbox.set_checked(True)
        assert checkbox.is_indeterminate() is False

    def test_value_change_listener(self, tree):
        """Value change listener is called on change."""
        checkbox = Checkbox("Test")
        checkbox._attach(tree)

        received_events = []

        def listener(event):
            received_events.append(event)

        checkbox.add_value_change_listener(listener)

        # Simulate change event from client
        checkbox._handle_change({"checked": True})

        assert len(received_events) == 1
        assert checkbox.is_checked() is True

    def test_sync_property(self, tree):
        """_sync_property updates internal state."""
        checkbox = Checkbox("Test")
        checkbox._attach(tree)

        checkbox._sync_property("checked", True)
        assert checkbox.is_checked() is True

    def test_attach_sets_properties(self, tree):
        """Attach sets initial properties on element."""
        checkbox = Checkbox("Accept")
        checkbox._attach(tree)

        changes = tree.collect_changes()

        # Find label property change
        label_change = next(
            (c for c in changes if c.get("key") == "label" and c.get("value") == "Accept"),
            None
        )
        assert label_change is not None

        # Find checked property change
        checked_change = next(
            (c for c in changes if c.get("key") == "checked"),
            None
        )
        assert checked_change is not None
