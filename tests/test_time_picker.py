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

        tp._handle_change({"value": "14:30"})
        assert len(events) == 1
        assert tp.value == datetime.time(14, 30)

    def test_change_listener_with_seconds(self, tree):
        tp = TimePicker()
        tp._attach(tree)

        tp._handle_change({"value": "14:30:45"})
        assert tp.value == datetime.time(14, 30, 45)

    def test_change_listener_empty(self, tree):
        tp = TimePicker()
        tp.set_value(datetime.time(12, 0))
        tp._attach(tree)

        tp._handle_change({"value": ""})
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
