"""Tests for VirtualList component."""

import pytest

from pyflow.components.virtual_list import VirtualList
from pyflow.components.renderer import LitRenderer, ComponentRenderer
from pyflow.components.button import Button
from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature


class TestVirtualList:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        vl = VirtualList()
        assert vl._tag == "vaadin-virtual-list"

    def test_create(self):
        vl = VirtualList()
        assert vl._items == []
        assert vl._renderer is None

    def test_attach(self, tree):
        vl = VirtualList()
        vl._attach(tree)
        assert vl._element is not None

    def test_attach_registers_feature_19(self, tree):
        vl = VirtualList()
        vl._attach(tree)

        changes = tree.collect_changes()
        f19 = [c for c in changes if c.get("feat") == Feature.CLIENT_DELEGATE_HANDLERS]
        assert len(f19) == 1
        assert "setViewportRange" in f19[0]["add"]

    def test_attach_inits_connector(self, tree):
        vl = VirtualList()
        vl._attach(tree)

        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("virtualListConnector.initLazy" in js for js in js_strings)

    def test_set_items(self):
        vl = VirtualList()
        vl.set_items(["A", "B", "C"])
        assert vl._items == ["A", "B", "C"]

    def test_get_items(self):
        vl = VirtualList()
        vl.set_items(["A", "B"])
        items = vl.get_items()
        assert items == ["A", "B"]
        items.append("C")
        assert vl._items == ["A", "B"]

    def test_set_items_pushes_data(self, tree):
        vl = VirtualList()
        vl._attach(tree)
        tree.collect_execute()

        vl.set_items(["X", "Y"])
        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("updateSize" in js for js in js_strings)
        assert any("$connector.set(" in js for js in js_strings)

    def test_data_push_format(self, tree):
        vl = VirtualList()
        vl.set_renderer(
            LitRenderer.of("<div>${item.name}</div>")
            .with_property("name", lambda x: x)
        )
        vl.set_items(["Alice", "Bob"])
        vl._attach(tree)

        execute = tree.collect_execute()
        update_size = [cmd for cmd in execute if "updateSize" in cmd[-1]]
        assert len(update_size) > 0
        # The second arg should be 2
        assert update_size[-1][1] == 2

    def test_lit_renderer_setup(self, tree):
        vl = VirtualList()
        renderer = LitRenderer.of("<div>${item.name}</div>").with_property("name", lambda x: x)
        vl.set_renderer(renderer)
        vl._attach(tree)

        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("setLitRenderer" in js for js in js_strings)

    def test_lit_renderer_with_function(self, tree):
        vl = VirtualList()
        calls = []
        renderer = (
            LitRenderer.of('<button @click="${handleClick}">${item.name}</button>')
            .with_property("name", lambda x: x)
            .with_function("handleClick", lambda x: calls.append(x))
        )
        vl.set_renderer(renderer)
        vl._attach(tree)

        # Should have registered return channel
        assert len(tree._return_channels) > 0

    def test_renderer_data_in_items(self, tree):
        vl = VirtualList()
        renderer = (
            LitRenderer.of("<div>${item.label}</div>")
            .with_property("label", lambda x: x.upper())
        )
        vl.set_renderer(renderer)
        vl.set_items(["hello", "world"])
        vl._attach(tree)

        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]]
        assert len(set_cmd) > 0
        items = set_cmd[-1][2]  # third arg is the items array
        ns = renderer._namespace
        assert items[0][ns + "label"] == "HELLO"
        assert items[1][ns + "label"] == "WORLD"

    def test_set_viewport_range(self, tree):
        vl = VirtualList()
        vl.set_renderer(
            LitRenderer.of("<div>${item.name}</div>")
            .with_property("name", lambda x: x)
        )
        vl.set_items(["A", "B", "C", "D", "E"])
        vl._attach(tree)
        tree.collect_execute()

        vl.set_viewport_range(2, 2)
        execute = tree.collect_execute()
        update_size = [cmd for cmd in execute if "updateSize" in cmd[-1]]
        set_items = [cmd for cmd in execute if "$connector.set(" in cmd[-1]]
        assert len(update_size) > 0
        assert len(set_items) > 0
        # Items should start from offset 2 with limit 2
        items = set_items[-1][2]
        assert len(items) == 2
        assert items[0]["key"] == "2"
        assert items[1]["key"] == "3"

    def test_register_in_tree_components(self, tree):
        vl = VirtualList()
        vl._attach(tree)
        assert tree._components[vl.element.node_id] is vl

    def test_key_to_item_mapping(self, tree):
        vl = VirtualList()
        vl.set_renderer(
            LitRenderer.of("<div>${item.name}</div>")
            .with_property("name", lambda x: x)
        )
        vl.set_items(["A", "B", "C"])
        vl._attach(tree)

        assert vl._key_to_item["0"] == "A"
        assert vl._key_to_item["1"] == "B"
        assert vl._key_to_item["2"] == "C"

    def test_renderer_callback(self, tree):
        vl = VirtualList()
        calls = []
        renderer = (
            LitRenderer.of('<button @click="${handleClick}">${item.name}</button>')
            .with_property("name", lambda x: x)
            .with_function("handleClick", lambda x: calls.append(x))
        )
        vl.set_renderer(renderer)
        vl.set_items(["Alice", "Bob"])
        vl._attach(tree)

        # Simulate callback
        vl._handle_renderer_callback(["handleClick", "0"], renderer)
        assert len(calls) == 1
        assert calls[0] == "Alice"

    def test_renderer_callback_unknown_key(self, tree):
        vl = VirtualList()
        calls = []
        renderer = (
            LitRenderer.of('<button @click="${handleClick}">${item.name}</button>')
            .with_property("name", lambda x: x)
            .with_function("handleClick", lambda x: calls.append(x))
        )
        vl.set_renderer(renderer)
        vl.set_items(["Alice"])
        vl._attach(tree)

        # Unknown key should not call handler
        vl._handle_renderer_callback(["handleClick", "99"], renderer)
        assert len(calls) == 0

    def test_component_renderer(self, tree):
        vl = VirtualList()
        renderer = ComponentRenderer(lambda item: Button(str(item)))
        vl.set_renderer(renderer)
        vl.set_items(["A", "B"])
        vl._attach(tree)

        changes = tree.collect_changes()
        # Should have created virtual child container
        virtual_splices = [c for c in changes if c.get("feat") == Feature.VIRTUAL_CHILDREN_LIST]
        assert len(virtual_splices) > 0

        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        # Should have set up FlowComponentHost
        assert any("FlowComponentHost" in js for js in js_strings)

    def test_no_confirm_in_data_push(self, tree):
        """VirtualList does NOT use $connector.confirm() unlike Grid/ComboBox."""
        vl = VirtualList()
        vl.set_renderer(
            LitRenderer.of("<div>${item.name}</div>")
            .with_property("name", lambda x: x)
        )
        vl.set_items(["A"])
        vl._attach(tree)

        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        confirm_execs = [js for js in js_strings if "confirm" in js]
        assert len(confirm_execs) == 0

    def test_items_before_renderer(self, tree):
        vl = VirtualList()
        vl.set_items(["A", "B"])
        vl.set_renderer(
            LitRenderer.of("<div>${item.name}</div>")
            .with_property("name", lambda x: x)
        )
        vl._attach(tree)

        execute = tree.collect_execute()
        set_items = [cmd for cmd in execute if "$connector.set(" in cmd[-1]]
        assert len(set_items) > 0

    def test_set_height(self, tree):
        vl = VirtualList()
        vl.set_height("300px")
        vl._attach(tree)

        changes = tree.collect_changes()
        style_changes = [
            c for c in changes
            if c.get("key") == "height" and c.get("feat") == Feature.INLINE_STYLE_PROPERTY_MAP
        ]
        assert any(c["value"] == "300px" for c in style_changes)

    def test_update_size_correct_count(self, tree):
        vl = VirtualList()
        vl.set_items(["A", "B", "C"])
        vl._attach(tree)

        execute = tree.collect_execute()
        size_cmd = [cmd for cmd in execute if "updateSize" in cmd[-1]][0]
        assert size_cmd[1] == 3

    def test_empty_items(self, tree):
        """Empty items list should not push any data."""
        vl = VirtualList()
        vl._attach(tree)

        execute = tree.collect_execute()
        set_items = [cmd for cmd in execute if "$connector.set(" in cmd[-1]]
        assert len(set_items) == 0
