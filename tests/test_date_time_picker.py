"""Tests for DateTimePicker component."""

import datetime

import pytest
from vaadin.flow.components import DateTimePicker
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


@pytest.fixture
def tree():
    return StateTree()


class TestDateTimePicker:
    def test_tag(self, tree):
        dtp = DateTimePicker()
        dtp._attach(tree)
        assert dtp.element.node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-date-time-picker"

    def test_label(self, tree):
        dtp = DateTimePicker("Meeting")
        dtp._attach(tree)
        assert dtp.element.get_property("label") == "Meeting"
        assert dtp.get_label() == "Meeting"

    def test_set_label(self, tree):
        dtp = DateTimePicker()
        dtp._attach(tree)
        dtp.set_label("Appointment")
        assert dtp.element.get_property("label") == "Appointment"

    def test_value(self, tree):
        dt = datetime.datetime(2025, 6, 15, 14, 30)
        dtp = DateTimePicker()
        dtp.set_value(dt)
        dtp._attach(tree)
        assert dtp.get_value() == dt
        assert dtp.element.get_property("value") == "2025-06-15T14:30"

    def test_value_with_seconds(self, tree):
        dt = datetime.datetime(2025, 6, 15, 14, 30, 45)
        dtp = DateTimePicker()
        dtp.set_value(dt)
        dtp._attach(tree)
        assert dtp.element.get_property("value") == "2025-06-15T14:30:45"

    def test_set_value_after_attach(self, tree):
        dtp = DateTimePicker()
        dtp._attach(tree)
        dt = datetime.datetime(2025, 1, 1, 9, 0)
        dtp.set_value(dt)
        assert dtp.element.get_property("value") == "2025-01-01T09:00"

    def test_min_max(self, tree):
        min_dt = datetime.datetime(2025, 1, 1, 0, 0)
        max_dt = datetime.datetime(2025, 12, 31, 23, 59)
        dtp = DateTimePicker()
        dtp.set_min(min_dt)
        dtp.set_max(max_dt)
        dtp._attach(tree)
        assert dtp.element.get_property("min") == "2025-01-01T00:00"
        assert dtp.element.get_property("max") == "2025-12-31T23:59"

    def test_step(self, tree):
        dtp = DateTimePicker()
        dtp.set_step(1800)  # 30 minutes
        dtp._attach(tree)
        assert dtp.element.get_property("step") == 1800

    def test_required(self, tree):
        dtp = DateTimePicker()
        dtp.set_required(True)
        dtp._attach(tree)
        assert dtp.element.get_property("required") is True

    def test_placeholders(self, tree):
        dtp = DateTimePicker()
        dtp.set_date_placeholder("Pick date")
        dtp.set_time_placeholder("Pick time")
        dtp._attach(tree)
        assert dtp.element.get_property("datePlaceholder") == "Pick date"
        assert dtp.element.get_property("timePlaceholder") == "Pick time"

    def test_value_change_listener(self, tree):
        dtp = DateTimePicker()
        dtp._attach(tree)
        events = []
        dtp.add_value_change_listener(lambda e: events.append(e))
        dtp._handle_change({"value": "2025-06-15T14:30"})
        assert len(events) == 1
        assert dtp.get_value() == datetime.datetime(2025, 6, 15, 14, 30)

    def test_handle_change_empty(self, tree):
        dtp = DateTimePicker()
        dtp._attach(tree)
        dtp._handle_change({"value": ""})
        assert dtp.get_value() is None

    def test_sync_property(self, tree):
        dtp = DateTimePicker()
        dtp._attach(tree)
        dtp._sync_property("value", "2025-03-01T08:15")
        assert dtp.get_value() == datetime.datetime(2025, 3, 1, 8, 15)

    def test_sync_property_empty(self, tree):
        dtp = DateTimePicker()
        dtp._attach(tree)
        dtp._sync_property("value", "")
        assert dtp.get_value() is None

    def test_default_value_none(self, tree):
        dtp = DateTimePicker()
        dtp._attach(tree)
        assert dtp.get_value() is None
        assert dtp.element.get_property("value") == ""

    def test_connector_init(self, tree):
        """DateTimePicker initializes both datepicker and timepicker connectors."""
        dtp = DateTimePicker()
        dtp._attach(tree)
        executes = tree._pending_execute
        connector_calls = [e for e in executes if "Connector.initLazy" in str(e)]
        assert len(connector_calls) == 2

    def test_property_value(self, tree):
        dt = datetime.datetime(2025, 6, 15, 14, 30)
        dtp = DateTimePicker()
        dtp._attach(tree)
        dtp.value = dt
        assert dtp.value == dt


class TestDateTimePickerWeekNumbers:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_default_week_numbers_not_visible(self):
        """Week numbers are not visible by default."""
        dtp = DateTimePicker()
        assert dtp.is_week_numbers_visible() is False

    def test_set_week_numbers_visible(self):
        """set_week_numbers_visible updates internal state."""
        dtp = DateTimePicker()
        dtp.set_week_numbers_visible(True)
        assert dtp.is_week_numbers_visible() is True

    def test_set_week_numbers_visible_false(self):
        """Setting False after True returns to False."""
        dtp = DateTimePicker()
        dtp.set_week_numbers_visible(True)
        dtp.set_week_numbers_visible(False)
        assert dtp.is_week_numbers_visible() is False

    def test_set_week_numbers_after_attach(self, tree):
        """Setting after attach executes JS on the internal date picker."""
        dtp = DateTimePicker()
        dtp._attach(tree)
        tree._pending_execute.clear()

        dtp.set_week_numbers_visible(True)
        # Should have queued a JS execution for the sub-field
        execute = tree._pending_execute
        js_strings = [cmd[-1] for cmd in execute]
        assert any("showWeekNumbers" in js and "true" in js for js in js_strings)
