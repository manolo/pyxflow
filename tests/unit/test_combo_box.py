"""Tests for ComboBox component."""

import pytest

from vaadin.flow.components.combo_box import ComboBox
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestComboBox:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create(self):
        cb = ComboBox()
        assert cb._tag == "vaadin-combo-box"
        assert cb.get_value() is None
        assert cb.get_items() == []

    def test_create_with_label(self):
        cb = ComboBox("Country")
        assert cb.get_label() == "Country"

    def test_set_items_before_attach(self):
        cb = ComboBox()
        cb.set_items("A", "B", "C")
        assert cb.get_items() == ["A", "B", "C"]

    def test_attach_sets_properties(self, tree):
        cb = ComboBox("Browser")
        cb.set_placeholder("Select")
        cb._attach(tree)

        changes = tree.collect_changes()
        labels = [c for c in changes if c.get("key") == "label"]
        assert any(c["value"] == "Browser" for c in labels)

        ph = [c for c in changes if c.get("key") == "placeholder"]
        assert any(c["value"] == "Select" for c in ph)

        page_size = [c for c in changes if c.get("key") == "pageSize"]
        assert any(c["value"] == 50 for c in page_size)

        item_id = [c for c in changes if c.get("key") == "itemIdPath"]
        assert any(c["value"] == "key" for c in item_id)

        item_label = [c for c in changes if c.get("key") == "itemLabelPath"]
        assert any(c["value"] == "label" for c in item_label)

    def test_connector_init(self, tree):
        cb = ComboBox()
        cb._attach(tree)

        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("comboBoxConnector.initLazy" in js for js in js_strings)

    def test_feature_19_methods(self, tree):
        cb = ComboBox()
        cb._attach(tree)

        changes = tree.collect_changes()
        f19 = [c for c in changes if c.get("feat") == Feature.CLIENT_DELEGATE_HANDLERS]
        assert len(f19) == 1
        assert "setViewportRange" in f19[0]["add"]
        assert "resetDataCommunicator" in f19[0]["add"]
        assert "confirmUpdate" in f19[0]["add"]

    def test_data_push_on_attach(self, tree):
        cb = ComboBox()
        cb.set_items("Firefox", "Chrome", "Safari")
        cb._attach(tree)

        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("updateSize" in js for js in js_strings)
        assert any("$connector.set(" in js for js in js_strings)
        assert any("$connector.confirm(" in js for js in js_strings)

    def test_data_format(self, tree):
        cb = ComboBox()
        cb.set_items("Firefox", "Chrome")
        cb._attach(tree)

        execute = tree.collect_execute()
        # Find the $connector.set command
        set_cmd = None
        for cmd in execute:
            if "$connector.set(" in cmd[-1]:
                set_cmd = cmd
                break
        assert set_cmd is not None

        items = set_cmd[2]
        assert len(items) == 2
        assert items[0] == {"key": "0", "label": "Firefox"}
        assert items[1] == {"key": "1", "label": "Chrome"}

    def test_update_size(self, tree):
        cb = ComboBox()
        cb.set_items("A", "B", "C")
        cb._attach(tree)

        execute = tree.collect_execute()
        size_cmd = [cmd for cmd in execute if "updateSize" in cmd[-1]][0]
        assert size_cmd[1] == 3

    def test_set_items_after_attach(self, tree):
        cb = ComboBox()
        cb._attach(tree)
        tree.collect_execute()

        cb.set_items("X", "Y")
        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("updateSize" in js for js in js_strings)
        assert any("$connector.set(" in js for js in js_strings)

    def test_value_selection_by_change(self, tree):
        cb = ComboBox()
        cb.set_items("Firefox", "Chrome", "Safari")
        cb._attach(tree)

        events = []
        cb.add_value_change_listener(lambda e: events.append(e))

        cb._handle_change({"value": "1"})
        assert cb.get_value() == "Chrome"
        assert len(events) == 1

    def test_value_selection_empty(self, tree):
        cb = ComboBox()
        cb.set_items("A", "B")
        cb._attach(tree)

        cb._handle_change({"value": "0"})
        assert cb.get_value() == "A"

        cb._handle_change({"value": ""})
        assert cb.get_value() is None

    def test_set_value_programmatic(self, tree):
        cb = ComboBox()
        cb.set_items("Firefox", "Chrome", "Safari")
        cb._attach(tree)
        tree.collect_changes()

        cb.set_value("Chrome")
        changes = tree.collect_changes()
        value_changes = [c for c in changes if c.get("key") == "value"]
        assert any(c["value"] == "1" for c in value_changes)

        selected = [c for c in changes if c.get("key") == "selectedItem"]
        assert any(c["value"] == {"key": "1", "label": "Chrome"} for c in selected)

    def test_set_value_none(self, tree):
        cb = ComboBox()
        cb.set_items("A", "B")
        cb.set_value("A")
        cb._attach(tree)
        tree.collect_changes()

        cb.set_value(None)
        changes = tree.collect_changes()
        value_changes = [c for c in changes if c.get("key") == "value"]
        assert any(c["value"] == "" for c in value_changes)

    def test_filtering(self, tree):
        cb = ComboBox()
        cb.set_items("Firefox", "Chrome", "Safari", "Edge")
        cb._attach(tree)
        tree.collect_execute()

        # Simulate client filtering
        cb.set_viewport_range(0, 50, "fire")
        execute = tree.collect_execute()

        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert len(items) == 1
        assert items[0]["label"] == "Firefox"

    def test_filtering_case_insensitive(self, tree):
        cb = ComboBox()
        cb.set_items("Firefox", "Chrome", "Safari")
        cb._attach(tree)
        tree.collect_execute()

        cb.set_viewport_range(0, 50, "CHROME")
        execute = tree.collect_execute()

        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert len(items) == 1
        assert items[0]["label"] == "Chrome"

    def test_filtering_empty_returns_all(self, tree):
        cb = ComboBox()
        cb.set_items("A", "B", "C")
        cb._attach(tree)
        tree.collect_execute()

        cb.set_viewport_range(0, 50, "")
        execute = tree.collect_execute()

        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert len(items) == 3

    def test_item_label_generator(self, tree):
        cb = ComboBox()
        cb.set_item_label_generator(lambda x: x.upper())
        cb.set_items("firefox", "chrome")
        cb._attach(tree)

        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert items[0]["label"] == "FIREFOX"
        assert items[1]["label"] == "CHROME"

    def test_sync_property_value(self, tree):
        cb = ComboBox()
        cb.set_items("A", "B", "C")
        cb._attach(tree)

        cb._sync_property("value", "2")
        assert cb.get_value() == "C"

    def test_sync_property_empty(self, tree):
        cb = ComboBox()
        cb.set_items("A", "B")
        cb._attach(tree)

        cb._sync_property("value", "")
        assert cb.get_value() is None

    def test_set_allow_custom_value(self, tree):
        cb = ComboBox()
        cb.set_allow_custom_value(True)
        cb._attach(tree)

        changes = tree.collect_changes()
        acv = [c for c in changes if c.get("key") == "allowCustomValue"]
        assert any(c["value"] is True for c in acv)

    def test_set_page_size(self, tree):
        cb = ComboBox()
        cb.set_page_size(100)
        cb._attach(tree)

        changes = tree.collect_changes()
        ps = [c for c in changes if c.get("key") == "pageSize"]
        assert any(c["value"] == 100 for c in ps)

    def test_set_required(self, tree):
        cb = ComboBox()
        cb.set_required(True)
        cb._attach(tree)

        changes = tree.collect_changes()
        req = [c for c in changes if c.get("key") == "required"]
        assert any(c["value"] is True for c in req)

    def test_registered_in_tree_components(self, tree):
        cb = ComboBox()
        cb._attach(tree)
        assert tree._components[cb.element.node_id] is cb

    def test_set_label_after_attach(self, tree):
        cb = ComboBox()
        cb._attach(tree)
        tree.collect_changes()

        cb.set_label("New Label")
        changes = tree.collect_changes()
        labels = [c for c in changes if c.get("key") == "label"]
        assert any(c["value"] == "New Label" for c in labels)

    def test_set_placeholder_after_attach(self, tree):
        cb = ComboBox()
        cb._attach(tree)
        tree.collect_changes()

        cb.set_placeholder("Type here")
        changes = tree.collect_changes()
        ph = [c for c in changes if c.get("key") == "placeholder"]
        assert any(c["value"] == "Type here" for c in ph)

    def test_confirm_update_noop(self, tree):
        cb = ComboBox()
        cb._attach(tree)
        # Should not raise
        cb.confirm_update(1)

    def test_reset_data_communicator_noop(self, tree):
        cb = ComboBox()
        cb._attach(tree)
        # Should not raise
        cb.reset_data_communicator()

    def test_get_items_returns_copy(self):
        cb = ComboBox()
        cb.set_items("A", "B")
        items = cb.get_items()
        items.append("C")
        assert len(cb.get_items()) == 2


class TestComboBoxClassNameGenerator:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_set_class_name_generator(self, tree):
        """Setting a class name generator includes className in connector items."""
        cb = ComboBox()
        cb.set_class_name_generator(lambda item: "highlight" if item == "Chrome" else None)
        cb.set_items("Firefox", "Chrome", "Safari")
        cb._attach(tree)

        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        # Chrome should have className
        chrome_item = [it for it in items if it["label"] == "Chrome"][0]
        assert chrome_item["className"] == "highlight"
        # Firefox should NOT have className
        firefox_item = [it for it in items if it["label"] == "Firefox"][0]
        assert "className" not in firefox_item

    def test_class_name_generator_returns_none(self, tree):
        """When generator returns None for all items, no className keys appear."""
        cb = ComboBox()
        cb.set_class_name_generator(lambda item: None)
        cb.set_items("A", "B")
        cb._attach(tree)

        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        for it in items:
            assert "className" not in it

    def test_class_name_generator_all_items(self, tree):
        """When generator returns a value for all items, every item has className."""
        cb = ComboBox()
        cb.set_class_name_generator(lambda item: "bold")
        cb.set_items("X", "Y")
        cb._attach(tree)

        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        for it in items:
            assert it["className"] == "bold"

    def test_class_name_generator_with_filter(self, tree):
        """Class name generator is applied to filtered results too."""
        cb = ComboBox()
        cb.set_class_name_generator(lambda item: "special" if "fire" in item.lower() else None)
        cb.set_items("Firefox", "Chrome", "Safari")
        cb._attach(tree)
        tree.collect_execute()

        cb.set_viewport_range(0, 50, "fire")
        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert len(items) == 1
        assert items[0]["className"] == "special"


class TestComboBoxPrefixComponent:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_set_prefix_component_before_attach(self, tree):
        """Prefix component set before attach is attached during ComboBox attach."""
        from vaadin.flow.components.icon import Icon
        cb = ComboBox()
        icon = Icon("search")
        cb.set_prefix_component(icon)
        cb._attach(tree)

        # Icon should be attached
        assert icon._element is not None
        # Icon should have slot="prefix"
        changes = tree.collect_changes()
        attr_changes = [
            c for c in changes
            if c.get("key") == "slot" and c.get("node") == icon.element.node_id
        ]
        assert any(c["value"] == "prefix" for c in attr_changes)

    def test_set_prefix_component_after_attach(self, tree):
        """Prefix component set after attach is attached immediately."""
        from vaadin.flow.components.span import Span
        cb = ComboBox()
        cb._attach(tree)
        tree.collect_changes()

        span = Span("$")
        cb.set_prefix_component(span)

        assert span._element is not None
        changes = tree.collect_changes()
        attr_changes = [
            c for c in changes
            if c.get("key") == "slot" and c.get("node") == span.element.node_id
        ]
        assert any(c["value"] == "prefix" for c in attr_changes)

    def test_prefix_component_becomes_child(self, tree):
        """Prefix component is added as child of the combo box element."""
        from vaadin.flow.components.icon import Icon
        cb = ComboBox()
        icon = Icon("search")
        cb.set_prefix_component(icon)
        cb._attach(tree)

        # Verify a splice change added the icon node as child of the combo box node
        changes = tree.collect_changes()
        splice_changes = [
            c for c in changes
            if c.get("type") == "splice"
            and c.get("feat") == Feature.ELEMENT_CHILDREN_LIST
            and c.get("node") == cb.element.node_id
        ]
        # At least one splice should reference the icon node
        added_node_ids = []
        for sc in splice_changes:
            added_node_ids.extend(sc.get("addNodes", []))
        assert icon.element.node_id in added_node_ids


class TestComboBoxOverlayWidth:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_set_overlay_width_before_attach(self, tree):
        """Overlay width set before attach is applied during attach."""
        cb = ComboBox()
        cb.set_overlay_width("300px")
        cb._attach(tree)

        changes = tree.collect_changes()
        ow = [c for c in changes if c.get("key") == "overlayWidth"]
        assert any(c["value"] == "300px" for c in ow)

    def test_set_overlay_width_after_attach(self, tree):
        """Overlay width set after attach is applied immediately."""
        cb = ComboBox()
        cb._attach(tree)
        tree.collect_changes()

        cb.set_overlay_width("400px")
        changes = tree.collect_changes()
        ow = [c for c in changes if c.get("key") == "overlayWidth"]
        assert any(c["value"] == "400px" for c in ow)

    def test_overlay_width_not_set_by_default(self, tree):
        """No overlayWidth property when not explicitly set."""
        cb = ComboBox()
        cb._attach(tree)

        changes = tree.collect_changes()
        ow = [c for c in changes if c.get("key") == "overlayWidth"]
        assert len(ow) == 0
