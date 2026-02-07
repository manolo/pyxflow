"""Tests for DatePicker component."""

import datetime

import pytest

from vaadin.flow.components.date_picker import DatePicker
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestDatePicker:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create(self):
        dp = DatePicker()
        assert dp._tag == "vaadin-date-picker"
        assert dp.value is None
        assert dp._label == ""

    def test_create_with_label(self):
        dp = DatePicker("Birthday")
        assert dp._label == "Birthday"

    def test_set_value_before_attach(self):
        dp = DatePicker()
        dp.set_value(datetime.date(2025, 6, 15))
        assert dp.value == datetime.date(2025, 6, 15)

    def test_set_value_after_attach(self, tree):
        dp = DatePicker()
        dp._attach(tree)
        tree.collect_changes()

        dp.set_value(datetime.date(2025, 6, 15))
        changes = tree.collect_changes()
        value_changes = [c for c in changes if c.get("key") == "value"]
        assert any(c["value"] == "2025-06-15" for c in value_changes)

    def test_set_none_value(self, tree):
        dp = DatePicker()
        dp.set_value(datetime.date(2025, 1, 1))
        dp._attach(tree)
        tree.collect_changes()

        dp.set_value(None)
        changes = tree.collect_changes()
        value_changes = [c for c in changes if c.get("key") == "value"]
        assert any(c["value"] == "" for c in value_changes)

    def test_attach_sets_properties(self, tree):
        dp = DatePicker("Date")
        dp.set_value(datetime.date(2025, 3, 14))
        dp._attach(tree)

        changes = tree.collect_changes()
        labels = [c for c in changes if c.get("key") == "label"]
        assert any(c["value"] == "Date" for c in labels)

        values = [c for c in changes if c.get("key") == "value"]
        assert any(c["value"] == "2025-03-14" for c in values)

        invalid = [c for c in changes if c.get("key") == "invalid"]
        assert any(c["value"] is False for c in invalid)

        manual_val = [c for c in changes if c.get("key") == "manualValidation"]
        assert any(c["value"] is True for c in manual_val)

    def test_connector_init(self, tree):
        dp = DatePicker()
        dp._attach(tree)

        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("datepickerConnector.initLazy" in js for js in js_strings)

    def test_change_listener(self, tree):
        dp = DatePicker()
        dp._attach(tree)

        events = []
        dp.add_value_change_listener(lambda e: events.append(e))

        dp._handle_change({"value": "2025-06-15"})
        assert len(events) == 1
        assert dp.value == datetime.date(2025, 6, 15)

    def test_change_listener_empty(self, tree):
        dp = DatePicker()
        dp.set_value(datetime.date(2025, 1, 1))
        dp._attach(tree)

        dp._handle_change({"value": ""})
        assert dp.value is None

    def test_change_listener_invalid(self, tree):
        dp = DatePicker()
        dp._attach(tree)

        dp._handle_change({"value": "not-a-date"})
        assert dp.value is None

    def test_sync_property(self, tree):
        dp = DatePicker()
        dp._attach(tree)

        dp._sync_property("value", "2025-12-25")
        assert dp.value == datetime.date(2025, 12, 25)

    def test_sync_property_empty(self, tree):
        dp = DatePicker()
        dp.set_value(datetime.date(2025, 1, 1))
        dp._attach(tree)

        dp._sync_property("value", "")
        assert dp.value is None

    def test_set_min_max(self, tree):
        dp = DatePicker()
        dp.set_min(datetime.date(2025, 1, 1))
        dp.set_max(datetime.date(2025, 12, 31))
        dp._attach(tree)

        changes = tree.collect_changes()
        mins = [c for c in changes if c.get("key") == "min"]
        assert any(c["value"] == "2025-01-01" for c in mins)
        maxs = [c for c in changes if c.get("key") == "max"]
        assert any(c["value"] == "2025-12-31" for c in maxs)

    def test_set_min_max_after_attach(self, tree):
        dp = DatePicker()
        dp._attach(tree)
        tree.collect_changes()

        dp.set_min(datetime.date(2025, 1, 1))
        dp.set_max(datetime.date(2025, 12, 31))
        changes = tree.collect_changes()
        mins = [c for c in changes if c.get("key") == "min"]
        assert any(c["value"] == "2025-01-01" for c in mins)

    def test_set_placeholder(self, tree):
        dp = DatePicker()
        dp.set_placeholder("Select a date")
        dp._attach(tree)

        changes = tree.collect_changes()
        ph = [c for c in changes if c.get("key") == "placeholder"]
        assert any(c["value"] == "Select a date" for c in ph)

    def test_set_required(self, tree):
        dp = DatePicker()
        dp.set_required(True)
        dp._attach(tree)

        changes = tree.collect_changes()
        req = [c for c in changes if c.get("key") == "required"]
        assert any(c["value"] is True for c in req)

    def test_value_property_setter(self):
        dp = DatePicker()
        dp.value = datetime.date(2025, 7, 4)
        assert dp.value == datetime.date(2025, 7, 4)

    def test_set_label_after_attach(self, tree):
        dp = DatePicker()
        dp._attach(tree)
        tree.collect_changes()

        dp.set_label("New Label")
        changes = tree.collect_changes()
        labels = [c for c in changes if c.get("key") == "label"]
        assert any(c["value"] == "New Label" for c in labels)

    def test_get_label(self):
        dp = DatePicker("Test")
        assert dp.get_label() == "Test"
