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

        # invalid=False is no longer sent (web component default is already False)

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

        # Real protocol: mSync sets value first, then change event fires listeners
        dp._sync_property("value", "2025-06-15")
        dp._handle_change({})
        assert len(events) == 1
        assert dp.value == datetime.date(2025, 6, 15)

    def test_change_listener_empty(self, tree):
        dp = DatePicker()
        dp.set_value(datetime.date(2025, 1, 1))
        dp._attach(tree)

        # Real protocol: mSync clears value first
        dp._sync_property("value", "")
        dp._handle_change({})
        assert dp.value is None

    def test_change_listener_invalid(self, tree):
        dp = DatePicker()
        dp._attach(tree)

        dp._sync_property("value", "not-a-date")
        dp._handle_change({})
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


class TestDatePickerWeekNumbers:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_default_week_numbers_not_visible(self):
        """Week numbers are not visible by default."""
        dp = DatePicker()
        assert dp.is_week_numbers_visible() is False

    def test_set_week_numbers_visible_before_attach(self, tree):
        """Setting before attach applies showWeekNumbers on attach."""
        dp = DatePicker()
        dp.set_week_numbers_visible(True)
        dp._attach(tree)

        changes = tree.collect_changes()
        wn = [c for c in changes if c.get("key") == "showWeekNumbers"]
        assert any(c["value"] is True for c in wn)

    def test_set_week_numbers_visible_after_attach(self, tree):
        """Setting after attach updates property immediately."""
        dp = DatePicker()
        dp._attach(tree)
        tree.collect_changes()

        dp.set_week_numbers_visible(True)
        changes = tree.collect_changes()
        wn = [c for c in changes if c.get("key") == "showWeekNumbers"]
        assert any(c["value"] is True for c in wn)

    def test_is_week_numbers_visible(self):
        """Getter returns what was set."""
        dp = DatePicker()
        dp.set_week_numbers_visible(True)
        assert dp.is_week_numbers_visible() is True

    def test_week_numbers_not_set_by_default_on_attach(self, tree):
        """showWeekNumbers property not set when not explicitly enabled."""
        dp = DatePicker()
        dp._attach(tree)

        changes = tree.collect_changes()
        wn = [c for c in changes if c.get("key") == "showWeekNumbers"]
        assert len(wn) == 0


class TestDatePickerInitialPosition:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_default_initial_position(self):
        """Default initial position is None."""
        dp = DatePicker()
        assert dp.get_initial_position() is None

    def test_set_initial_position_before_attach(self, tree):
        """Setting before attach applies initialPosition on attach."""
        dp = DatePicker()
        dp.set_initial_position(datetime.date(2025, 6, 1))
        dp._attach(tree)

        changes = tree.collect_changes()
        ip = [c for c in changes if c.get("key") == "initialPosition"]
        assert any(c["value"] == "2025-06-01" for c in ip)

    def test_set_initial_position_after_attach(self, tree):
        """Setting after attach updates property immediately."""
        dp = DatePicker()
        dp._attach(tree)
        tree.collect_changes()

        dp.set_initial_position(datetime.date(2025, 3, 15))
        changes = tree.collect_changes()
        ip = [c for c in changes if c.get("key") == "initialPosition"]
        assert any(c["value"] == "2025-03-15" for c in ip)

    def test_set_initial_position_none(self, tree):
        """Setting None after a value clears the position."""
        dp = DatePicker()
        dp.set_initial_position(datetime.date(2025, 1, 1))
        dp._attach(tree)
        tree.collect_changes()

        dp.set_initial_position(None)
        changes = tree.collect_changes()
        ip = [c for c in changes if c.get("key") == "initialPosition"]
        assert any(c["value"] == "" for c in ip)

    def test_get_initial_position(self):
        """Getter returns what was set."""
        dp = DatePicker()
        dp.set_initial_position(datetime.date(2025, 9, 1))
        assert dp.get_initial_position() == datetime.date(2025, 9, 1)

    def test_initial_position_not_set_by_default(self, tree):
        """initialPosition property not set when not explicitly set."""
        dp = DatePicker()
        dp._attach(tree)

        changes = tree.collect_changes()
        ip = [c for c in changes if c.get("key") == "initialPosition"]
        assert len(ip) == 0


class TestDatePickerOpenClose:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_open_after_attach(self, tree):
        """open() sets opened=True."""
        dp = DatePicker()
        dp._attach(tree)
        tree.collect_changes()

        dp.open()
        changes = tree.collect_changes()
        opened = [c for c in changes if c.get("key") == "opened"]
        assert any(c["value"] is True for c in opened)

    def test_close_after_attach(self, tree):
        """close() sets opened=False."""
        dp = DatePicker()
        dp._attach(tree)
        tree.collect_changes()

        dp.open()
        tree.collect_changes()

        dp.close()
        changes = tree.collect_changes()
        opened = [c for c in changes if c.get("key") == "opened"]
        assert any(c["value"] is False for c in opened)

    def test_open_before_attach_is_noop(self):
        """open() before attach does nothing (no crash)."""
        dp = DatePicker()
        dp.open()  # should not raise

    def test_close_before_attach_is_noop(self):
        """close() before attach does nothing (no crash)."""
        dp = DatePicker()
        dp.close()  # should not raise


class TestDatePickerOpenedChangeListener:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_add_opened_change_listener_before_attach(self, tree):
        """Listener added before attach is registered during attach."""
        dp = DatePicker()
        events = []
        dp.add_opened_change_listener(lambda e: events.append(e))
        dp._attach(tree)

        # Simulate opened-changed event
        dp._handle_opened_changed({"value": True})
        assert len(events) == 1
        assert events[0]["value"] is True

    def test_add_opened_change_listener_after_attach(self, tree):
        """Listener added after attach is registered immediately."""
        dp = DatePicker()
        dp._attach(tree)

        events = []
        dp.add_opened_change_listener(lambda e: events.append(e))

        # Event listener should be registered on the element
        assert "opened-changed" in dp.element._listeners

        dp._handle_opened_changed({"value": False})
        assert len(events) == 1
        assert events[0]["value"] is False

    def test_multiple_opened_change_listeners(self, tree):
        """Multiple listeners all receive events."""
        dp = DatePicker()
        dp._attach(tree)

        events1 = []
        events2 = []
        dp.add_opened_change_listener(lambda e: events1.append(e))
        dp.add_opened_change_listener(lambda e: events2.append(e))

        dp._handle_opened_changed({"value": True})
        assert len(events1) == 1
        assert len(events2) == 1
