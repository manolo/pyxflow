"""Tests for NumberField and IntegerField components."""

import pytest

from pyxflow.components import NumberField, IntegerField
from pyxflow.core.state_tree import StateTree


class TestNumberField:
    """Test NumberField component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_number_field_without_label(self):
        """NumberField can be created without a label."""
        field = NumberField()
        assert field.get_label() == ""
        assert field.get_value() is None

    def test_create_number_field_with_label(self):
        """NumberField can be created with a label."""
        field = NumberField("Amount")
        assert field.get_label() == "Amount"

    def test_number_field_tag(self):
        """NumberField has correct tag."""
        field = NumberField()
        assert field._tag == "vaadin-number-field"

    def test_set_value(self, tree):
        """set_value updates the value."""
        field = NumberField("Price")
        field._attach(tree)

        field.set_value(42.5)
        assert field.get_value() == 42.5

    def test_set_value_none(self, tree):
        """set_value with None clears the value."""
        field = NumberField("Price")
        field._attach(tree)

        field.set_value(42.5)
        field.set_value(None)
        assert field.get_value() is None

    def test_value_property(self, tree):
        """value property works correctly."""
        field = NumberField("Price")
        field._attach(tree)

        field.value = 99.99
        assert field.value == 99.99

    def test_set_min_max(self, tree):
        """set_min and set_max work correctly."""
        field = NumberField("Quantity")
        field._attach(tree)

        field.set_min(0)
        field.set_max(100)

        assert field.get_min() == 0
        assert field.get_max() == 100

    def test_set_step(self, tree):
        """set_step works correctly."""
        field = NumberField("Duration")
        field._attach(tree)

        field.set_step(0.5)
        assert field.get_step() == 0.5

    def test_value_change_listener(self, tree):
        """Value change listener is called on change."""
        field = NumberField("Amount")
        field._attach(tree)

        received_events = []

        def listener(event):
            received_events.append(event)

        field.add_value_change_listener(listener)

        # Simulate change event from client
        field._handle_change({"value": "123.45"})

        assert len(received_events) == 1
        assert field.get_value() == 123.45

    def test_handle_change_empty_value(self, tree):
        """Empty value from client results in None."""
        field = NumberField("Amount")
        field._attach(tree)

        field.set_value(100.0)
        field._handle_change({"value": ""})

        assert field.get_value() is None

    def test_sync_property(self, tree):
        """_sync_property updates internal state."""
        field = NumberField("Amount")
        field._attach(tree)

        field._sync_property("value", "50.5")
        assert field.get_value() == 50.5

    def test_sync_property_empty(self, tree):
        """_sync_property with empty value sets None."""
        field = NumberField("Amount")
        field._attach(tree)

        field.set_value(100.0)
        field._sync_property("value", "")
        assert field.get_value() is None


class TestIntegerField:
    """Test IntegerField component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_integer_field_tag(self):
        """IntegerField has correct tag."""
        field = IntegerField()
        assert field._tag == "vaadin-integer-field"

    def test_set_value_integer(self, tree):
        """set_value stores integer value."""
        field = IntegerField("Count")
        field._attach(tree)

        field.set_value(42)
        assert field.get_value() == 42
        assert isinstance(field.get_value(), int)

    def test_handle_change_integer(self, tree):
        """Handle change converts to integer."""
        field = IntegerField("Count")
        field._attach(tree)

        # Even if client sends float string, we convert to int
        field._handle_change({"value": "42.9"})

        assert field.get_value() == 42
        assert isinstance(field.get_value(), int)

    def test_sync_property_integer(self, tree):
        """_sync_property converts to integer."""
        field = IntegerField("Count")
        field._attach(tree)

        field._sync_property("value", "123.7")
        assert field.get_value() == 123
        assert isinstance(field.get_value(), int)

    def test_value_none(self, tree):
        """Empty value results in None."""
        field = IntegerField("Count")
        field._attach(tree)

        field.set_value(42)
        field._handle_change({"value": ""})

        assert field.get_value() is None
