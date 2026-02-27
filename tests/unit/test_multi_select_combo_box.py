"""Tests for MultiSelectComboBox component."""

import pytest

from pyflow.components.multi_select_combo_box import MultiSelectComboBox
from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature


class TestMultiSelectComboBox:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        cb = MultiSelectComboBox()
        assert cb._tag == "vaadin-multi-select-combo-box"

    def test_create_default(self):
        cb = MultiSelectComboBox()
        assert cb._label == ""
        assert cb._items == []
        assert cb._value == set()

    def test_create_with_label(self):
        cb = MultiSelectComboBox("Skills")
        assert cb._label == "Skills"

    def test_set_items(self):
        cb = MultiSelectComboBox()
        cb.set_items("Java", "Python", "Go")
        assert cb._items == ["Java", "Python", "Go"]

    def test_get_items(self):
        cb = MultiSelectComboBox()
        cb.set_items("A", "B")
        items = cb.get_items()
        assert items == ["A", "B"]
        items.append("C")
        assert cb._items == ["A", "B"]

    def test_attach(self, tree):
        cb = MultiSelectComboBox("Label")
        cb._attach(tree)
        assert cb._element is not None

    def test_attach_sets_properties(self, tree):
        cb = MultiSelectComboBox("Skills")
        cb._attach(tree)

        changes = tree.collect_changes()
        labels = [c for c in changes if c.get("key") == "label"]
        assert any(c["value"] == "Skills" for c in labels)

        item_id = [c for c in changes if c.get("key") == "itemIdPath"]
        assert any(c["value"] == "key" for c in item_id)

        item_value = [c for c in changes if c.get("key") == "itemValuePath"]
        assert any(c["value"] == "key" for c in item_value)

        item_label = [c for c in changes if c.get("key") == "itemLabelPath"]
        assert any(c["value"] == "label" for c in item_label)

        page_size = [c for c in changes if c.get("key") == "pageSize"]
        assert any(c["value"] == 50 for c in page_size)

    def test_attach_registers_feature_19(self, tree):
        cb = MultiSelectComboBox()
        cb._attach(tree)

        changes = tree.collect_changes()
        f19 = [c for c in changes if c.get("feat") == Feature.CLIENT_DELEGATE_HANDLERS]
        assert len(f19) == 1
        assert "setViewportRange" in f19[0]["add"]
        assert "resetDataCommunicator" in f19[0]["add"]
        assert "confirmUpdate" in f19[0]["add"]

    def test_attach_inits_connector(self, tree):
        cb = MultiSelectComboBox()
        cb._attach(tree)

        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("comboBoxConnector.initLazy" in js for js in js_strings)

    def test_attach_pushes_data(self, tree):
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        cb._attach(tree)

        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("updateSize" in js for js in js_strings)
        assert any("$connector.set(" in js for js in js_strings)
        assert any("$connector.confirm(" in js for js in js_strings)

    def test_data_format(self, tree):
        cb = MultiSelectComboBox()
        cb.set_items("Java", "Python")
        cb._attach(tree)

        execute = tree.collect_execute()
        set_cmd = None
        for cmd in execute:
            if "$connector.set(" in cmd[-1]:
                set_cmd = cmd
                break
        assert set_cmd is not None
        items = set_cmd[2]
        assert len(items) == 2
        assert items[0] == {"key": "0", "label": "Java"}
        assert items[1] == {"key": "1", "label": "Python"}

    def test_update_size(self, tree):
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        cb._attach(tree)

        execute = tree.collect_execute()
        size_cmd = [cmd for cmd in execute if "updateSize" in cmd[-1]][0]
        assert size_cmd[1] == 3

    def test_set_value(self):
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        cb.set_value({"A", "C"})
        assert cb.get_value() == {"A", "C"}

    def test_set_value_after_attach(self, tree):
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        cb._attach(tree)
        tree.collect_changes()

        cb.set_value({"B"})
        changes = tree.collect_changes()
        selected_changes = [c for c in changes if c.get("key") == "selectedItems"]
        assert len(selected_changes) > 0
        last = selected_changes[-1]["value"]
        assert len(last) == 1
        assert last[0]["key"] == "1"
        assert last[0]["label"] == "B"

    def test_get_value_returns_copy(self):
        cb = MultiSelectComboBox()
        cb.set_items("A", "B")
        cb.set_value({"A"})
        v = cb.get_value()
        v.add("B")
        assert cb._value == {"A"}

    def test_select(self):
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        cb.select("A", "C")
        assert cb.get_value() == {"A", "C"}

    def test_deselect(self):
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        cb.set_value({"A", "B", "C"})
        cb.deselect("B")
        assert cb.get_value() == {"A", "C"}

    def test_value_change_listener_from_client(self, tree):
        """Value change fires via mSync (_sync_property), not event handler."""
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        cb._attach(tree)

        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb._sync_property("selectedItems", [{"key": "0"}, {"key": "2"}])
        assert len(events) == 1
        assert events[0]["value"] == {"A", "C"}
        assert events[0]["from_client"] is True

    def test_value_change_listener_no_duplicate(self, tree):
        """Same value synced twice does not fire listener again."""
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        cb._attach(tree)

        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb._sync_property("selectedItems", [{"key": "0"}])
        cb._sync_property("selectedItems", [{"key": "0"}])
        assert len(events) == 1

    def test_sync_property_empty_clears_value(self, tree):
        """Syncing empty selectedItems clears value and fires listener."""
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        cb._attach(tree)
        cb._sync_property("selectedItems", [{"key": "0"}, {"key": "1"}])

        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb._sync_property("selectedItems", [])
        assert cb.get_value() == set()
        assert len(events) == 1
        assert events[0]["value"] == set()

    def test_handle_selection_changed_is_noop(self, tree):
        """_handle_selection_changed is a no-op (value arrives via mSync)."""
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        cb._attach(tree)

        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb._handle_selection_changed({"value": [{"key": "0"}]})
        assert len(events) == 0
        assert cb.get_value() == set()

    def test_set_value_fires_listener_from_server(self):
        """set_value fires listener with from_client=False."""
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")

        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb.set_value({"A", "C"})
        assert len(events) == 1
        assert events[0]["from_client"] is False
        assert events[0]["value"] == {"A", "C"}

    def test_set_value_same_no_fire(self):
        """set_value with same value does not fire listener."""
        cb = MultiSelectComboBox()
        cb.set_items("A", "B")
        cb.set_value({"A"})

        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb.set_value({"A"})
        assert len(events) == 0

    def test_set_placeholder(self):
        cb = MultiSelectComboBox()
        cb.set_placeholder("Select...")
        assert cb._placeholder == "Select..."

    def test_set_placeholder_after_attach(self, tree):
        cb = MultiSelectComboBox()
        cb._attach(tree)
        tree.collect_changes()

        cb.set_placeholder("Choose")
        changes = tree.collect_changes()
        ph_changes = [c for c in changes if c.get("key") == "placeholder"]
        assert any(c["value"] == "Choose" for c in ph_changes)

    def test_set_page_size(self):
        cb = MultiSelectComboBox()
        cb.set_page_size(20)
        assert cb._page_size == 20

    def test_set_required(self):
        cb = MultiSelectComboBox()
        cb.set_required(True)
        assert cb.is_required_indicator_visible() is True

    def test_set_required_on_attach(self, tree):
        cb = MultiSelectComboBox()
        cb.set_required(True)
        cb._attach(tree)

        changes = tree.collect_changes()
        req = [c for c in changes if c.get("key") == "required"]
        assert any(c["value"] is True for c in req)

    def test_item_label_generator(self, tree):
        cb = MultiSelectComboBox()
        cb.set_item_label_generator(lambda x: x.upper())
        cb.set_items("java", "python")
        cb._attach(tree)

        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert items[0]["label"] == "JAVA"
        assert items[1]["label"] == "PYTHON"

    def test_registered_in_tree_components(self, tree):
        cb = MultiSelectComboBox()
        cb._attach(tree)
        assert tree._components[cb.element.node_id] is cb

    def test_set_viewport_range(self, tree):
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        cb._attach(tree)
        tree.collect_execute()

        cb.set_viewport_range(0, 10, "A")
        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("updateSize" in js for js in js_strings)
        assert any("$connector.set(" in js for js in js_strings)

    def test_filter_case_insensitive(self, tree):
        cb = MultiSelectComboBox()
        cb.set_items("Apple", "Banana", "apricot")
        cb._attach(tree)
        tree.collect_execute()

        cb.set_viewport_range(0, 10, "ap")
        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        labels = [it["label"] for it in items]
        assert "Apple" in labels
        assert "apricot" in labels
        assert "Banana" not in labels

    def test_sync_property_selected_items(self):
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        cb._sync_property("selectedItems", [{"key": "0"}, {"key": "1"}])
        assert cb._value == {"A", "B"}

    def test_sync_property_empty(self):
        cb = MultiSelectComboBox()
        cb.set_items("A", "B")
        cb._sync_property("selectedItems", [])
        assert cb._value == set()

    def test_set_label(self):
        cb = MultiSelectComboBox()
        cb.set_label("Languages")
        assert cb.get_label() == "Languages"

    def test_set_label_after_attach(self, tree):
        cb = MultiSelectComboBox()
        cb._attach(tree)
        tree.collect_changes()

        cb.set_label("New Label")
        changes = tree.collect_changes()
        labels = [c for c in changes if c.get("key") == "label"]
        assert any(c["value"] == "New Label" for c in labels)

    def test_selected_items_changed_listener(self, tree):
        cb = MultiSelectComboBox()
        cb._attach(tree)
        assert "selected-items-changed" in cb.element._listeners

    def test_set_items_after_attach(self, tree):
        cb = MultiSelectComboBox()
        cb._attach(tree)
        tree.collect_execute()

        cb.set_items("X", "Y")
        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("updateSize" in js for js in js_strings)
        assert any("$connector.set(" in js for js in js_strings)

    def test_confirm_update_noop(self, tree):
        cb = MultiSelectComboBox()
        cb._attach(tree)
        # Should not raise
        cb.confirm_update(1)

    def test_reset_data_communicator_noop(self, tree):
        cb = MultiSelectComboBox()
        cb._attach(tree)
        # Should not raise
        cb.reset_data_communicator()


class TestMultiSelectComboBoxAutoExpand:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_default_auto_expand(self):
        """Default auto-expand mode is NONE."""
        from pyflow.components.constants import AutoExpandMode
        cb = MultiSelectComboBox()
        assert cb.get_auto_expand() == AutoExpandMode.NONE

    def test_set_auto_expand_horizontal(self, tree):
        """HORIZONTAL mode sets autoExpandHorizontally=true, autoExpandVertically=false."""
        from pyflow.components.constants import AutoExpandMode
        cb = MultiSelectComboBox()
        cb.set_auto_expand(AutoExpandMode.HORIZONTAL)
        cb._attach(tree)

        changes = tree.collect_changes()
        h = [c for c in changes if c.get("key") == "autoExpandHorizontally"]
        v = [c for c in changes if c.get("key") == "autoExpandVertically"]
        assert any(c["value"] is True for c in h)
        assert any(c["value"] is False for c in v)

    def test_set_auto_expand_vertical(self, tree):
        """VERTICAL mode sets autoExpandVertically=true, autoExpandHorizontally=false."""
        from pyflow.components.constants import AutoExpandMode
        cb = MultiSelectComboBox()
        cb.set_auto_expand(AutoExpandMode.VERTICAL)
        cb._attach(tree)

        changes = tree.collect_changes()
        h = [c for c in changes if c.get("key") == "autoExpandHorizontally"]
        v = [c for c in changes if c.get("key") == "autoExpandVertically"]
        assert any(c["value"] is False for c in h)
        assert any(c["value"] is True for c in v)

    def test_set_auto_expand_both(self, tree):
        """BOTH mode sets both properties to true."""
        from pyflow.components.constants import AutoExpandMode
        cb = MultiSelectComboBox()
        cb.set_auto_expand(AutoExpandMode.BOTH)
        cb._attach(tree)

        changes = tree.collect_changes()
        h = [c for c in changes if c.get("key") == "autoExpandHorizontally"]
        v = [c for c in changes if c.get("key") == "autoExpandVertically"]
        assert any(c["value"] is True for c in h)
        assert any(c["value"] is True for c in v)

    def test_set_auto_expand_none_no_properties(self, tree):
        """NONE mode does not set any autoExpand properties on attach."""
        from pyflow.components.constants import AutoExpandMode
        cb = MultiSelectComboBox()
        cb.set_auto_expand(AutoExpandMode.NONE)
        cb._attach(tree)

        changes = tree.collect_changes()
        h = [c for c in changes if c.get("key") == "autoExpandHorizontally"]
        v = [c for c in changes if c.get("key") == "autoExpandVertically"]
        assert len(h) == 0
        assert len(v) == 0

    def test_get_auto_expand(self):
        """get_auto_expand returns the mode that was set."""
        from pyflow.components.constants import AutoExpandMode
        cb = MultiSelectComboBox()
        cb.set_auto_expand(AutoExpandMode.BOTH)
        assert cb.get_auto_expand() == AutoExpandMode.BOTH

    def test_set_auto_expand_after_attach(self, tree):
        """Setting auto-expand after attach updates properties immediately."""
        from pyflow.components.constants import AutoExpandMode
        cb = MultiSelectComboBox()
        cb._attach(tree)
        tree.collect_changes()

        cb.set_auto_expand(AutoExpandMode.HORIZONTAL)
        changes = tree.collect_changes()
        h = [c for c in changes if c.get("key") == "autoExpandHorizontally"]
        v = [c for c in changes if c.get("key") == "autoExpandVertically"]
        assert any(c["value"] is True for c in h)
        assert any(c["value"] is False for c in v)


class TestMultiSelectComboBoxSelectedItemsOnTop:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_default_selected_items_on_top(self):
        """Default is False."""
        cb = MultiSelectComboBox()
        assert cb.is_selected_items_on_top() is False

    def test_set_selected_items_on_top_before_attach(self, tree):
        """Setting before attach applies on attach."""
        cb = MultiSelectComboBox()
        cb.set_selected_items_on_top(True)
        cb._attach(tree)

        changes = tree.collect_changes()
        sot = [c for c in changes if c.get("key") == "selectedItemsOnTop"]
        assert any(c["value"] is True for c in sot)

    def test_set_selected_items_on_top_after_attach(self, tree):
        """Setting after attach updates property immediately."""
        cb = MultiSelectComboBox()
        cb._attach(tree)
        tree.collect_changes()

        cb.set_selected_items_on_top(True)
        changes = tree.collect_changes()
        sot = [c for c in changes if c.get("key") == "selectedItemsOnTop"]
        assert any(c["value"] is True for c in sot)

    def test_is_selected_items_on_top(self):
        """Getter reflects what was set."""
        cb = MultiSelectComboBox()
        cb.set_selected_items_on_top(True)
        assert cb.is_selected_items_on_top() is True


class TestMultiSelectComboBoxKeepFilter:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_default_keep_filter(self):
        """Default is False."""
        cb = MultiSelectComboBox()
        assert cb.is_keep_filter() is False

    def test_set_keep_filter_before_attach(self, tree):
        """Setting before attach applies on attach."""
        cb = MultiSelectComboBox()
        cb.set_keep_filter(True)
        cb._attach(tree)

        changes = tree.collect_changes()
        kf = [c for c in changes if c.get("key") == "keepFilter"]
        assert any(c["value"] is True for c in kf)

    def test_set_keep_filter_after_attach(self, tree):
        """Setting after attach updates property immediately."""
        cb = MultiSelectComboBox()
        cb._attach(tree)
        tree.collect_changes()

        cb.set_keep_filter(True)
        changes = tree.collect_changes()
        kf = [c for c in changes if c.get("key") == "keepFilter"]
        assert any(c["value"] is True for c in kf)

    def test_is_keep_filter(self):
        """Getter reflects what was set."""
        cb = MultiSelectComboBox()
        cb.set_keep_filter(True)
        assert cb.is_keep_filter() is True


class TestMultiSelectComboBoxAllowCustomValue:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_set_allow_custom_value_before_attach(self, tree):
        """Setting before attach applies on attach."""
        cb = MultiSelectComboBox()
        cb.set_allow_custom_value(True)
        cb._attach(tree)

        changes = tree.collect_changes()
        acv = [c for c in changes if c.get("key") == "allowCustomValue"]
        assert any(c["value"] is True for c in acv)

    def test_set_allow_custom_value_after_attach(self, tree):
        """Setting after attach updates property immediately."""
        cb = MultiSelectComboBox()
        cb._attach(tree)
        tree.collect_changes()

        cb.set_allow_custom_value(True)
        changes = tree.collect_changes()
        acv = [c for c in changes if c.get("key") == "allowCustomValue"]
        assert any(c["value"] is True for c in acv)

    def test_allow_custom_value_not_set_by_default(self, tree):
        """No allowCustomValue property when not explicitly set."""
        cb = MultiSelectComboBox()
        cb._attach(tree)

        changes = tree.collect_changes()
        acv = [c for c in changes if c.get("key") == "allowCustomValue"]
        assert len(acv) == 0
