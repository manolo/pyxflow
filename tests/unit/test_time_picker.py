"""Tests for TimePicker component."""

import datetime

import pytest

from vaadin.flow.components.time_picker import TimePicker
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestTimePicker:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create(self):
        tp = TimePicker()
        assert tp._tag == "vaadin-time-picker"
        assert tp.value is None
        assert tp._label == ""

    def test_create_with_label(self):
        tp = TimePicker("Start Time")
        assert tp._label == "Start Time"

    def test_set_value_before_attach(self):
        tp = TimePicker()
        tp.set_value(datetime.time(14, 30))
        assert tp.value == datetime.time(14, 30)

    def test_set_value_after_attach(self, tree):
        tp = TimePicker()
        tp._attach(tree)
        tree.collect_changes()

        tp.set_value(datetime.time(14, 30))
        changes = tree.collect_changes()
        value_changes = [c for c in changes if c.get("key") == "value"]
        assert any(c["value"] == "14:30" for c in value_changes)

    def test_set_value_with_seconds(self, tree):
        tp = TimePicker()
        tp._attach(tree)
        tree.collect_changes()

        tp.set_value(datetime.time(14, 30, 45))
        changes = tree.collect_changes()
        value_changes = [c for c in changes if c.get("key") == "value"]
        assert any(c["value"] == "14:30:45" for c in value_changes)

    def test_set_none_value(self, tree):
        tp = TimePicker()
        tp.set_value(datetime.time(12, 0))
        tp._attach(tree)
        tree.collect_changes()

        tp.set_value(None)
        changes = tree.collect_changes()
        value_changes = [c for c in changes if c.get("key") == "value"]
        assert any(c["value"] == "" for c in value_changes)

    def test_attach_sets_properties(self, tree):
        tp = TimePicker("Time")
        tp.set_value(datetime.time(9, 0))
        tp._attach(tree)

        changes = tree.collect_changes()
        labels = [c for c in changes if c.get("key") == "label"]
        assert any(c["value"] == "Time" for c in labels)

        values = [c for c in changes if c.get("key") == "value"]
        assert any(c["value"] == "09:00" for c in values)

    def test_connector_init(self, tree):
        tp = TimePicker()
        tp._attach(tree)

        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("timepickerConnector.initLazy" in js for js in js_strings)

    def test_change_listener(self, tree):
        tp = TimePicker()
        tp._attach(tree)

        events = []
        tp.add_value_change_listener(lambda e: events.append(e))

        # Real protocol: mSync sets value first, then change event fires listeners
        tp._sync_property("value", "14:30")
        tp._handle_change({})
        assert len(events) == 1
        assert tp.value == datetime.time(14, 30)

    def test_change_listener_with_seconds(self, tree):
        tp = TimePicker()
        tp._attach(tree)

        tp._sync_property("value", "14:30:45")
        tp._handle_change({})
        assert tp.value == datetime.time(14, 30, 45)

    def test_change_listener_empty(self, tree):
        tp = TimePicker()
        tp.set_value(datetime.time(12, 0))
        tp._attach(tree)

        tp._sync_property("value", "")
        tp._handle_change({})
        assert tp.value is None

    def test_sync_property(self, tree):
        tp = TimePicker()
        tp._attach(tree)

        tp._sync_property("value", "08:15")
        assert tp.value == datetime.time(8, 15)

    def test_sync_property_empty(self, tree):
        tp = TimePicker()
        tp.set_value(datetime.time(12, 0))
        tp._attach(tree)

        tp._sync_property("value", "")
        assert tp.value is None

    def test_set_min_max(self, tree):
        tp = TimePicker()
        tp.set_min(datetime.time(8, 0))
        tp.set_max(datetime.time(17, 0))
        tp._attach(tree)

        changes = tree.collect_changes()
        mins = [c for c in changes if c.get("key") == "min"]
        assert any(c["value"] == "08:00" for c in mins)
        maxs = [c for c in changes if c.get("key") == "max"]
        assert any(c["value"] == "17:00" for c in maxs)

    def test_set_step(self, tree):
        tp = TimePicker()
        tp.set_step(1800)
        tp._attach(tree)

        changes = tree.collect_changes()
        steps = [c for c in changes if c.get("key") == "step"]
        assert any(c["value"] == 1800 for c in steps)

    def test_set_placeholder(self, tree):
        tp = TimePicker()
        tp.set_placeholder("Select a time")
        tp._attach(tree)

        changes = tree.collect_changes()
        ph = [c for c in changes if c.get("key") == "placeholder"]
        assert any(c["value"] == "Select a time" for c in ph)

    def test_set_required(self, tree):
        tp = TimePicker()
        tp.set_required(True)
        tp._attach(tree)

        changes = tree.collect_changes()
        req = [c for c in changes if c.get("key") == "required"]
        assert any(c["value"] is True for c in req)

    def test_format_time_no_seconds(self):
        assert TimePicker._format_time(datetime.time(14, 30)) == "14:30"

    def test_format_time_with_seconds(self):
        assert TimePicker._format_time(datetime.time(14, 30, 45)) == "14:30:45"

    def test_parse_time(self):
        assert TimePicker._parse_time("14:30") == datetime.time(14, 30)
        assert TimePicker._parse_time("14:30:45") == datetime.time(14, 30, 45)
        assert TimePicker._parse_time("") is None
        assert TimePicker._parse_time("invalid") is None

    def test_value_property_setter(self):
        tp = TimePicker()
        tp.value = datetime.time(15, 45)
        assert tp.value == datetime.time(15, 45)

    def test_set_label_after_attach(self, tree):
        tp = TimePicker()
        tp._attach(tree)
        tree.collect_changes()

        tp.set_label("New Label")
        changes = tree.collect_changes()
        labels = [c for c in changes if c.get("key") == "label"]
        assert any(c["value"] == "New Label" for c in labels)

    def test_get_label(self):
        tp = TimePicker("Test")
        assert tp.get_label() == "Test"


class TestTimePickerOpenClose:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_open_after_attach(self, tree):
        """open() sets opened=True."""
        tp = TimePicker()
        tp._attach(tree)
        tree.collect_changes()

        tp.open()
        changes = tree.collect_changes()
        opened = [c for c in changes if c.get("key") == "opened"]
        assert any(c["value"] is True for c in opened)

    def test_close_after_attach(self, tree):
        """close() sets opened=False."""
        tp = TimePicker()
        tp._attach(tree)
        tree.collect_changes()

        tp.open()
        tree.collect_changes()

        tp.close()
        changes = tree.collect_changes()
        opened = [c for c in changes if c.get("key") == "opened"]
        assert any(c["value"] is False for c in opened)

    def test_open_before_attach_is_noop(self):
        """open() before attach does nothing (no crash)."""
        tp = TimePicker()
        tp.open()  # should not raise

    def test_close_before_attach_is_noop(self):
        """close() before attach does nothing (no crash)."""
        tp = TimePicker()
        tp.close()  # should not raise


class TestTimePickerOpenedChangeListener:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_add_opened_change_listener_before_attach(self, tree):
        """Listener added before attach is registered during attach."""
        tp = TimePicker()
        events = []
        tp.add_opened_change_listener(lambda e: events.append(e))
        tp._attach(tree)

        # Simulate opened-changed event
        tp._handle_opened_changed({"value": True})
        assert len(events) == 1
        assert events[0]["value"] is True

    def test_add_opened_change_listener_after_attach(self, tree):
        """Listener added after attach is registered immediately."""
        tp = TimePicker()
        tp._attach(tree)

        events = []
        tp.add_opened_change_listener(lambda e: events.append(e))

        # Event listener should be registered on the element
        assert "opened-changed" in tp.element._listeners

        tp._handle_opened_changed({"value": False})
        assert len(events) == 1
        assert events[0]["value"] is False

    def test_multiple_opened_change_listeners(self, tree):
        """Multiple listeners all receive events."""
        tp = TimePicker()
        tp._attach(tree)

        events1 = []
        events2 = []
        tp.add_opened_change_listener(lambda e: events1.append(e))
        tp.add_opened_change_listener(lambda e: events2.append(e))

        tp._handle_opened_changed({"value": True})
        assert len(events1) == 1
        assert len(events2) == 1
