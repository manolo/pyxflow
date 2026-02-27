"""Regression tests for bugs discovered during UI testing.

Each test targets a specific bug that was only caught by Playwright UI tests.
These unit tests ensure the fixes don't regress.
"""

import pytest

from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature


@pytest.fixture
def tree():
    return StateTree()


# ── Bug 1: Checkbox._handle_change must normalize event format ──────────────


class TestCheckboxHandleChange:
    """Checkbox._handle_change must:
    - Cast value to bool (not trust raw event_data type)
    - Fire listeners with {"value": bool, "from_client": True}
    """

    def test_listener_receives_normalized_event(self, tree):
        from pyflow.components import Checkbox

        cb = Checkbox("Accept")
        cb._attach(tree)

        events = []
        cb.add_value_change_listener(events.append)

        cb._handle_change({"checked": True})

        assert len(events) == 1
        assert events[0]["value"] is True
        assert events[0]["from_client"] is True

    def test_handle_change_casts_to_bool(self, tree):
        """Truthy non-bool values (e.g. 1) must be cast to bool."""
        from pyflow.components import Checkbox

        cb = Checkbox("Accept")
        cb._attach(tree)

        cb._handle_change({"checked": 1})
        assert cb.is_checked() is True
        assert isinstance(cb.is_checked(), bool)

    def test_handle_change_without_checked_key(self, tree):
        """If event_data has no 'checked' key, don't clobber current value."""
        from pyflow.components import Checkbox

        cb = Checkbox("Accept")
        cb._attach(tree)
        cb._sync_property("checked", True)

        cb._handle_change({})  # mSync already set value; event has no data

        assert cb.is_checked() is True  # Must NOT reset to False


# ── Bug 2: CheckboxGroup._attach must sync initial value ────────────────────


class TestCheckboxGroupInitialValue:
    """CheckboxGroup._attach must set the group value property
    when items are pre-selected before attach."""

    def test_initial_value_synced_on_attach(self, tree):
        from pyflow.components import CheckboxGroup

        group = CheckboxGroup()
        group.set_items("A", "B", "C")
        group.set_value({"A", "C"})
        group._attach(tree)

        changes = tree.collect_changes()
        value_changes = [
            c for c in changes
            if c.get("key") == "value"
            and c.get("node") == group.element.node_id
        ]
        assert len(value_changes) >= 1
        # Value should contain labels of selected items
        val = value_changes[-1]["value"]
        assert "A" in val
        assert "C" in val


# ── Bug 3: ComboBox._handle_change must not clobber mSync value ─────────────


class TestComboBoxHandleChangeMSync:
    """When RPC batch has mSync + event, _handle_change receives event_data
    WITHOUT "value" key (mSync already set it). Must NOT reset to None."""

    def test_no_value_key_preserves_msync(self, tree):
        from pyflow.components import ComboBox

        cb = ComboBox()
        cb.set_items("Firefox", "Chrome", "Safari")
        cb._attach(tree)

        # Simulate mSync arriving first
        cb._sync_property("value", "1")
        assert cb.get_value() == "Chrome"

        # Then event arrives without value key
        cb._handle_change({})

        assert cb.get_value() == "Chrome"  # Must NOT become None

    def test_listener_receives_normalized_event(self, tree):
        from pyflow.components import ComboBox

        cb = ComboBox()
        cb.set_items("A", "B")
        cb._attach(tree)

        events = []
        cb.add_value_change_listener(events.append)

        cb._handle_change({"value": "0"})

        assert events[0]["value"] == "A"
        assert events[0]["from_client"] is True


# ── Bug 4: ComboBox._sync_property must fire change listeners ───────────────


class TestComboBoxSyncPropertyListeners:
    """ComboBox._sync_property must fire value change listeners,
    same as the selected-changed pattern used by Tabs/ListBox."""

    def test_sync_property_fires_listener(self, tree):
        from pyflow.components import ComboBox

        cb = ComboBox()
        cb.set_items("A", "B", "C")
        cb._attach(tree)

        events = []
        cb.add_value_change_listener(events.append)

        cb._sync_property("value", "2")

        assert len(events) == 1
        assert events[0]["value"] == "C"

    def test_sync_property_no_event_if_same_value(self, tree):
        """Don't fire listener if value didn't actually change."""
        from pyflow.components import ComboBox

        cb = ComboBox()
        cb.set_items("A", "B")
        cb._attach(tree)
        cb._sync_property("value", "0")  # Set to A

        events = []
        cb.add_value_change_listener(events.append)

        cb._sync_property("value", "0")  # Same value again

        assert len(events) == 0


# ── Bug 5: ComboBox.set_auto_open must buffer before attach ─────────────────


class TestComboBoxAutoOpenBuffering:
    """set_auto_open(False) called before _attach must set
    autoOpenDisabled property when the component is attached."""

    def test_auto_open_disabled_before_attach(self, tree):
        from pyflow.components import ComboBox

        cb = ComboBox()
        cb.set_auto_open(False)
        cb._attach(tree)

        changes = tree.collect_changes()
        auto_open_changes = [
            c for c in changes
            if c.get("key") == "autoOpenDisabled"
        ]
        assert any(c["value"] is True for c in auto_open_changes)


# ── Bug 6: NumberField._handle_change must not clobber mSync value ──────────


class TestNumberFieldHandleChangeMSync:
    """Same pattern as ComboBox: event_data without "value" key
    must not reset the value that mSync already set."""

    def test_no_value_key_preserves_msync(self, tree):
        from pyflow.components import NumberField

        field = NumberField("Amount")
        field._attach(tree)

        field._sync_property("value", "42.5")
        assert field.get_value() == 42.5

        field._handle_change({})  # Event without value key

        assert field.get_value() == 42.5  # Must NOT become None

    def test_listener_receives_normalized_event(self, tree):
        from pyflow.components import NumberField

        field = NumberField("Amount")
        field._attach(tree)

        events = []
        field.add_value_change_listener(events.append)

        field._handle_change({"value": "3.14"})

        assert events[0]["value"] == 3.14
        assert events[0]["from_client"] is True


# ── Bug 7: IntegerField._handle_change must not clobber mSync value ─────────


class TestIntegerFieldHandleChangeMSync:
    """Same pattern as NumberField."""

    def test_no_value_key_preserves_msync(self, tree):
        from pyflow.components import IntegerField

        field = IntegerField("Count")
        field._attach(tree)

        field._sync_property("value", "7")
        assert field.get_value() == 7

        field._handle_change({})

        assert field.get_value() == 7  # Must NOT become None

    def test_listener_receives_normalized_event(self, tree):
        from pyflow.components import IntegerField

        field = IntegerField("Count")
        field._attach(tree)

        events = []
        field.add_value_change_listener(events.append)

        field._handle_change({"value": "42"})

        assert events[0]["value"] == 42
        assert events[0]["from_client"] is True
        assert isinstance(events[0]["value"], int)


# ── Bug 8: Grid.select_item(item) convenience method ────────────────────────


class TestGridSelectItem:
    """Grid.select_item(item) selects by object reference,
    not by string key."""

    def test_select_item_by_reference(self, tree):
        from pyflow.components import Grid

        grid = Grid()
        grid.add_column("name", header="Name")
        items = [{"name": "Alice"}, {"name": "Bob"}]
        grid.set_items(items)
        grid._attach(tree)
        tree.collect_changes()

        grid.select_item(items[1])

        assert grid.get_selected_items() == [items[1]]

    def test_select_item_by_equality(self, tree):
        from pyflow.components import Grid

        grid = Grid()
        grid.add_column("name", header="Name")
        items = [{"name": "Alice"}, {"name": "Bob"}]
        grid.set_items(items)
        grid._attach(tree)

        # Select by equal dict (not same object)
        grid.select_item({"name": "Bob"})

        assert grid.get_selected_items() == [items[1]]


# ── Bug 9: Popover missing super().__init__() ───────────────────────────────


class TestPopoverInit:
    """Popover.__init__ must call super().__init__() so that
    Component base class attributes (_element, etc.) are initialized."""

    def test_has_element_attribute(self):
        from pyflow.components import Popover

        p = Popover()
        assert hasattr(p, "_element")
        assert p._element is None

    def test_attach_works(self, tree):
        from pyflow.components import Popover

        p = Popover()
        p._attach(tree)
        assert p._element is not None


# ── Bug 10: Notification.open() body attachment (not _attach) ───────────────


class TestNotificationBodyAttachment:
    """Notification.open() must attach to body node (node 1).
    But _attach() alone must NOT — when a layout calls add(notification),
    the layout handles parenting."""

    def test_attach_alone_does_not_add_to_body(self, tree):
        """_attach() must NOT add to body — that's for open() only."""
        from pyflow.components import Notification

        n = Notification("Test")
        n._attach(tree)

        changes = tree.collect_changes()
        body_splices = [
            c for c in changes
            if c.get("node") == 1
            and c.get("type") == "splice"
            and c.get("feat") == Feature.ELEMENT_CHILDREN_LIST
        ]
        # The notification node should NOT appear in body children
        for splice in body_splices:
            assert n.element.node_id not in splice.get("addNodes", [])

    def test_open_attaches_to_body(self, tree):
        """open() with tree context must add to body node."""
        from pyflow.components.notification import (
            Notification,
            _set_current_tree,
        )

        _set_current_tree(tree)
        try:
            n = Notification("Test")
            n.open()

            changes = tree.collect_changes()
            body_splice = next(
                (
                    c
                    for c in changes
                    if c.get("node") == 1
                    and c.get("type") == "splice"
                    and c.get("feat") == Feature.ELEMENT_CHILDREN_LIST
                ),
                None,
            )
            assert body_splice is not None
            assert n.element.node_id in body_splice["addNodes"]
        finally:
            _set_current_tree(None)


# ── Bug 11: element.execute_js uses queue_execute, not property change ──────


class TestElementExecuteJsFormat:
    """element.execute_js must produce execute commands via
    tree.queue_execute(), not property changes in tree.add_change()."""

    def test_execute_js_goes_to_execute_queue(self, tree):
        from pyflow.components import Button

        btn = Button("Test")
        btn._attach(tree)
        tree.collect_changes()
        tree.collect_execute()

        btn.element.execute_js("$0.focus()")

        # Must appear in execute queue
        cmds = tree.collect_execute()
        assert len(cmds) == 1
        assert "$0.focus()" in cmds[0][-1]  # Script is wrapped in try/catch
        assert cmds[0][0] == {"@v-node": btn.element.node_id}

    def test_execute_js_not_in_changes(self, tree):
        from pyflow.components import Button

        btn = Button("Test")
        btn._attach(tree)
        tree.collect_changes()

        btn.element.execute_js("$0.focus()")

        # Must NOT appear in changes
        changes = tree.collect_changes()
        exec_changes = [c for c in changes if c.get("key") == "execute"]
        assert len(exec_changes) == 0

    def test_execute_js_element_ref_args(self, tree):
        """Element arguments are converted to @v-node references."""
        from pyflow.components import Button, Span

        btn = Button("Test")
        span = Span("Target")
        btn._attach(tree)
        span._attach(tree)
        tree.collect_execute()

        btn.element.execute_js("$0.appendChild($1)", span.element)

        cmds = tree.collect_execute()
        assert len(cmds) == 1
        cmd = cmds[0]
        assert cmd[0] == {"@v-node": btn.element.node_id}
        assert cmd[1] == {"@v-node": span.element.node_id}
        assert "$0.appendChild($1)" in cmd[2]  # Script is wrapped in try/catch


# ── Bug 12: DatePicker/TimePicker/MultiSelectComboBox clear button ──────────


class TestClearButtonBuffering:
    """set_clear_button_visible(True) called before attach must be
    flushed as a property on attach."""

    def test_date_picker_clear_button_before_attach(self, tree):
        from pyflow.components import DatePicker

        dp = DatePicker()
        dp.set_clear_button_visible(True)
        dp._attach(tree)

        changes = tree.collect_changes()
        cbv = [c for c in changes if c.get("key") == "clearButtonVisible"]
        assert any(c["value"] is True for c in cbv)

    def test_time_picker_clear_button_before_attach(self, tree):
        from pyflow.components import TimePicker

        tp = TimePicker()
        tp.set_clear_button_visible(True)
        tp._attach(tree)

        changes = tree.collect_changes()
        cbv = [c for c in changes if c.get("key") == "clearButtonVisible"]
        assert any(c["value"] is True for c in cbv)

    def test_multi_select_combo_box_clear_button_before_attach(self, tree):
        from pyflow.components import MultiSelectComboBox

        mscb = MultiSelectComboBox()
        mscb.set_clear_button_visible(True)
        mscb._attach(tree)

        changes = tree.collect_changes()
        cbv = [c for c in changes if c.get("key") == "clearButtonVisible"]
        assert any(c["value"] is True for c in cbv)


# ── Bug 13: mSync must be processed before events in RPC batch ───────────


class TestMSyncBeforeEvents:
    """Java Flow's ServerRpcHandler.handleInvocations() processes all mSync
    RPCs before events. When Enter is pressed in a TextField with a Button
    click shortcut, the client sends [keydown, mSync, change]. Without
    reordering, the click handler sees an empty text field value."""

    def test_msync_processed_before_keydown(self, tree):
        """Simulate an RPC batch where keydown arrives before mSync.
        The click handler must see the synced value."""
        from pyflow.components import Button, TextField, VerticalLayout
        from pyflow.core.keys import Key
        from pyflow.server.uidl_handler import UidlHandler

        layout = VerticalLayout()
        tf = TextField("Filter")
        results = []
        btn = Button("Go", lambda e: results.append(tf.get_value()))
        btn.add_click_shortcut(Key.ENTER)
        layout.add(tf, btn)
        layout._attach(tree)
        tree.collect_changes()

        # Build RPC batch in client order: keydown, mSync, change
        # body_node is node 1 (the first node created by UidlHandler)
        body_node = tree._nodes[1]
        handler = UidlHandler.__new__(UidlHandler)
        handler._tree = tree
        handler._body_node = body_node
        rpc_list = [
            {"type": "event", "node": body_node.id, "event": "keydown", "data": {}},
            {"type": "mSync", "node": tf.element.node_id,
             "feature": 1, "property": "value", "value": "hello"},
            {"type": "event", "node": tf.element.node_id, "event": "change", "data": {}},
        ]

        handler._process_rpc(rpc_list)

        # The click handler must have seen "hello", not ""
        assert len(results) == 1
        assert results[0] == "hello"

    def test_msync_order_preserved_for_multiple_syncs(self, tree):
        """Multiple mSync RPCs should all be processed before any event."""
        from pyflow.components import Button, TextField, VerticalLayout
        from pyflow.core.keys import Key
        from pyflow.server.uidl_handler import UidlHandler

        layout = VerticalLayout()
        tf1 = TextField("A")
        tf2 = TextField("B")
        results = []

        def on_click(e):
            results.append((tf1.get_value(), tf2.get_value()))

        btn = Button("Go", on_click)
        btn.add_click_shortcut(Key.ENTER)
        layout.add(tf1, tf2, btn)
        layout._attach(tree)
        tree.collect_changes()

        body_node = tree._nodes[1]
        handler = UidlHandler.__new__(UidlHandler)
        handler._tree = tree
        handler._body_node = body_node
        rpc_list = [
            {"type": "mSync", "node": tf1.element.node_id,
             "feature": 1, "property": "value", "value": "aaa"},
            {"type": "event", "node": body_node.id, "event": "keydown", "data": {}},
            {"type": "mSync", "node": tf2.element.node_id,
             "feature": 1, "property": "value", "value": "bbb"},
        ]

        handler._process_rpc(rpc_list)

        assert len(results) == 1
        assert results[0] == ("aaa", "bbb")
