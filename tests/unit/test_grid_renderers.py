"""Tests for Grid renderers (LitRenderer, ComponentRenderer)."""

import pytest

from pyflow.components.grid import Grid, Column
from pyflow.components.renderer import LitRenderer, ComponentRenderer
from pyflow.components.button import Button
from pyflow.components.span import Span
from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature


class TestLitRenderer:
    """Test LitRenderer class."""

    def test_of_creates_instance(self):
        r = LitRenderer.of("<span>${item.name}</span>")
        assert isinstance(r, LitRenderer)
        assert r._template == "<span>${item.name}</span>"

    def test_with_property(self):
        r = LitRenderer.of("<span>${item.name}</span>").with_property(
            "name", lambda item: item["name"]
        )
        assert "name" in r._properties
        assert r._properties["name"]({"name": "Alice"}) == "Alice"

    def test_with_function(self):
        called = []
        r = LitRenderer.of("<button @click='${handleClick}'>Click</button>").with_function(
            "handleClick", lambda item: called.append(item)
        )
        assert "handleClick" in r._functions

    def test_fluent_api(self):
        r = (
            LitRenderer.of("<span>${item.a} ${item.b}</span>")
            .with_property("a", lambda i: i["a"])
            .with_property("b", lambda i: i["b"])
            .with_function("click", lambda i: None)
        )
        assert len(r._properties) == 2
        assert len(r._functions) == 1

    def test_namespace_generated(self):
        r1 = LitRenderer.of("a")
        r2 = LitRenderer.of("b")
        assert r1._namespace.startswith("lr_")
        assert r1._namespace.endswith("_")
        assert r1._namespace != r2._namespace


class TestComponentRenderer:
    """Test ComponentRenderer class."""

    def test_factory(self):
        factory = lambda item: Button(item["name"])
        r = ComponentRenderer(factory)
        assert r._factory is factory

    def test_namespace_generated(self):
        r = ComponentRenderer(lambda i: Button("x"))
        assert r._namespace.startswith("lr_")


class TestReturnChannel:
    """Test return channel registration and dispatch."""

    def test_register_return_channel(self):
        tree = StateTree()
        called = []
        channel_id = tree.register_return_channel(10, lambda args: called.append(args))
        assert channel_id == 0

    def test_handle_return_channel(self):
        tree = StateTree()
        called = []
        channel_id = tree.register_return_channel(10, lambda args: called.append(args))
        tree.handle_return_channel(10, channel_id, ["arg1", "arg2"])
        assert called == [["arg1", "arg2"]]

    def test_multiple_channels(self):
        tree = StateTree()
        called_a = []
        called_b = []
        ch_a = tree.register_return_channel(10, lambda args: called_a.append(args))
        ch_b = tree.register_return_channel(10, lambda args: called_b.append(args))
        assert ch_a != ch_b

        tree.handle_return_channel(10, ch_a, ["a"])
        tree.handle_return_channel(10, ch_b, ["b"])
        assert called_a == [["a"]]
        assert called_b == [["b"]]

    def test_unknown_channel_ignored(self):
        tree = StateTree()
        tree.handle_return_channel(99, 99, ["x"])  # no error

    def test_reset_clears_channels(self):
        tree = StateTree()
        called = []
        ch = tree.register_return_channel(10, lambda args: called.append(args))
        tree.reset()
        tree.handle_return_channel(10, ch, ["x"])
        assert called == []

    def test_channel_ids_reset_after_reset(self):
        tree = StateTree()
        tree.register_return_channel(10, lambda a: None)
        tree.register_return_channel(10, lambda a: None)
        tree.reset()
        ch = tree.register_return_channel(10, lambda a: None)
        assert ch == 0


class TestGridWithLitRenderer:
    """Test Grid with LitRenderer columns."""

    @pytest.fixture
    def tree(self):
        tree = StateTree()
        tree._app_id = "ROOT-1234567"
        return tree

    def test_add_column_with_renderer(self, tree):
        grid = Grid()
        renderer = LitRenderer.of("<span>${item.name}</span>").with_property(
            "name", lambda i: i["name"]
        )
        col = grid.add_column(renderer, header="Name")
        assert col._renderer is renderer
        assert col._property_name == ""

    def test_column_no_path_with_renderer(self, tree):
        grid = Grid()
        renderer = LitRenderer.of("<span>${item.name}</span>")
        grid.add_column(renderer, header="Name")
        grid._attach(tree)

        changes = tree.collect_changes()
        # Column should NOT have 'path' property
        col_node_id = grid._columns[0]._node.id
        path_changes = [
            c for c in changes
            if c.get("node") == col_node_id and c.get("key") == "path"
        ]
        assert len(path_changes) == 0

    def test_column_has_flow_id(self, tree):
        grid = Grid()
        renderer = LitRenderer.of("<span>x</span>")
        grid.add_column(renderer, header="Name")
        grid._attach(tree)

        changes = tree.collect_changes()
        col_node_id = grid._columns[0]._node.id
        flow_id = [
            c for c in changes
            if c.get("node") == col_node_id and c.get("key") == "_flowId"
        ]
        assert len(flow_id) == 1
        assert flow_id[0]["value"] == "col0"

    def test_set_lit_renderer_execute(self, tree):
        grid = Grid()
        renderer = LitRenderer.of("<span>${item.name}</span>").with_property(
            "name", lambda i: i["name"]
        )
        grid.add_column(renderer, header="Name")
        grid._attach(tree)

        execute = tree.collect_execute()
        renderer_cmds = [
            cmd for cmd in execute if "setLitRenderer" in cmd[-1]
        ]
        assert len(renderer_cmds) == 1
        cmd = renderer_cmds[0]
        # cmd[0] = col_ref, cmd[1] = renderer_name, cmd[2] = template
        assert cmd[1] == "renderer"
        assert cmd[2] == "<span>${item.name}</span>"
        # cmd[5] = namespace
        assert cmd[5].startswith("lr_")
        # cmd[6] = app_id
        assert cmd[6] == "ROOT-1234567"

    def test_lit_renderer_with_functions_has_return_channel(self, tree):
        grid = Grid()
        renderer = LitRenderer.of("<button @click='${handleClick}'>X</button>").with_function(
            "handleClick", lambda i: None
        )
        grid.add_column(renderer, header="Actions")
        grid._attach(tree)

        execute = tree.collect_execute()
        renderer_cmds = [
            cmd for cmd in execute if "setLitRenderer" in cmd[-1]
        ]
        assert len(renderer_cmds) == 1
        cmd = renderer_cmds[0]
        # cmd[3] = return channel
        assert cmd[3] is not None
        assert "@v-return" in cmd[3]
        # cmd[4] = client callables
        assert cmd[4] == ["handleClick"]

    def test_lit_renderer_without_functions_no_return_channel(self, tree):
        grid = Grid()
        renderer = LitRenderer.of("<span>${item.x}</span>").with_property(
            "x", lambda i: "v"
        )
        grid.add_column(renderer, header="X")
        grid._attach(tree)

        execute = tree.collect_execute()
        renderer_cmds = [
            cmd for cmd in execute if "setLitRenderer" in cmd[-1]
        ]
        cmd = renderer_cmds[0]
        assert cmd[3] is None
        assert cmd[4] == []

    def test_data_push_with_prefixed_properties(self, tree):
        grid = Grid()
        renderer = LitRenderer.of("<span>${item.name}</span>").with_property(
            "name", lambda i: i["name"]
        )
        col = grid.add_column(renderer, header="Name")
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}])
        grid._attach(tree)

        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        ns = renderer._namespace
        assert ns + "name" in items[0]
        assert items[0][ns + "name"] == "Alice"
        assert items[1][ns + "name"] == "Bob"
        # Should NOT have col0 key (no path-based column data)
        assert "col0" not in items[0]

    def test_mixed_columns_path_and_renderer(self, tree):
        grid = Grid()
        grid.add_column("email", header="Email")
        renderer = LitRenderer.of("<strong>${item.name}</strong>").with_property(
            "name", lambda i: i["name"]
        )
        grid.add_column(renderer, header="Name")
        grid.set_items([{"name": "Alice", "email": "alice@x.com"}])
        grid._attach(tree)

        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        # Path column: col0 = email
        assert items[0]["col0"] == "alice@x.com"
        # Renderer column: no col1, but has namespace-prefixed properties
        assert "col1" not in items[0]
        ns = renderer._namespace
        assert items[0][ns + "name"] == "Alice"

    def test_renderer_function_callback(self, tree):
        clicked = []
        grid = Grid()
        renderer = LitRenderer.of("<button @click='${handleClick}'>X</button>").with_function(
            "handleClick", lambda item: clicked.append(item)
        )
        grid.add_column(renderer, header="Actions")
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}])
        grid._attach(tree)
        tree.collect_execute()

        # Simulate return channel callback: [handlerName, itemKey]
        grid._handle_renderer_callback(["handleClick", "1"], renderer)
        assert len(clicked) == 1
        assert clicked[0]["name"] == "Bob"

    def test_renderer_function_callback_unknown_handler(self, tree):
        grid = Grid()
        renderer = LitRenderer.of("<span>x</span>").with_function(
            "handleClick", lambda item: None
        )
        grid.add_column(renderer, header="X")
        grid.set_items([{"name": "Alice"}])
        grid._attach(tree)
        tree.collect_execute()

        # Unknown handler name - should not raise
        grid._handle_renderer_callback(["unknownHandler", "0"], renderer)


class TestGridWithComponentRenderer:
    """Test Grid with ComponentRenderer columns."""

    @pytest.fixture
    def tree(self):
        tree = StateTree()
        tree._app_id = "ROOT-1234567"
        return tree

    def test_component_renderer_creates_components(self, tree):
        grid = Grid()
        renderer = ComponentRenderer(lambda item: Span(item["name"]))
        grid.add_column(renderer, header="Name")
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}])
        grid._attach(tree)

        # Components should be created
        assert len(renderer._components) == 2

    def test_component_renderer_nodeid_in_data(self, tree):
        grid = Grid()
        renderer = ComponentRenderer(lambda item: Span(item["name"]))
        grid.add_column(renderer, header="Name")
        grid.set_items([{"name": "Alice"}])
        grid._attach(tree)

        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        ns = renderer._namespace
        assert ns + "nodeid" in items[0]
        assert isinstance(items[0][ns + "nodeid"], int)

    def test_component_renderer_virtual_children(self, tree):
        grid = Grid()
        renderer = ComponentRenderer(lambda item: Span(item["name"]))
        grid.add_column(renderer, header="Name")
        grid.set_items([{"name": "Alice"}])
        grid._attach(tree)

        changes = tree.collect_changes()
        col_node_id = grid._columns[0]._node.id

        # Column should have exactly 1 virtual child: the container div
        virtual_splices = [
            c for c in changes
            if c.get("node") == col_node_id
            and c.get("feat") == Feature.VIRTUAL_CHILDREN_LIST
        ]
        assert len(virtual_splices) == 1
        container_node_id = virtual_splices[0]["addNodes"][0]
        assert container_node_id == renderer._container_node.id

        # Container should have the component as regular child (Feature 2)
        container_child_splices = [
            c for c in changes
            if c.get("node") == container_node_id
            and c.get("feat") == Feature.ELEMENT_CHILDREN_LIST
        ]
        assert len(container_child_splices) == 1
        component = renderer._components["0"]
        assert component.element.node_id in container_child_splices[0]["addNodes"]

        # Container should have payload marking it as inMemory
        payload_changes = [
            c for c in changes
            if c.get("node") == container_node_id
            and c.get("feat") == Feature.ELEMENT_DATA
            and c.get("key") == "payload"
        ]
        assert len(payload_changes) == 1
        assert payload_changes[0]["value"] == {"type": "inMemory"}

    def test_component_renderer_set_lit_renderer_execute(self, tree):
        grid = Grid()
        renderer = ComponentRenderer(lambda item: Span(item["name"]))
        grid.add_column(renderer, header="Name")
        grid._attach(tree)

        execute = tree.collect_execute()
        renderer_cmds = [
            cmd for cmd in execute if "setLitRenderer" in cmd[-1]
        ]
        assert len(renderer_cmds) == 1
        cmd = renderer_cmds[0]
        assert "FlowComponentHost.getNode" in cmd[2]

    def test_component_renderer_patches_virtual_container(self, tree):
        grid = Grid()
        renderer = ComponentRenderer(lambda item: Span(item["name"]))
        grid.add_column(renderer, header="Name")
        grid._attach(tree)

        execute = tree.collect_execute()
        patch_cmds = [
            cmd for cmd in execute
            if "patchVirtualContainer" in cmd[-1]
        ]
        assert len(patch_cmds) == 1
        # Should target the container div, not the column
        container_ref = {"@v-node": renderer._container_node.id}
        assert patch_cmds[0][0] == container_ref

    def test_component_renderer_reuses_components(self, tree):
        grid = Grid()
        renderer = ComponentRenderer(lambda item: Span(item["name"]))
        grid.add_column(renderer, header="Name")
        grid.set_items([{"name": "Alice"}])
        grid._attach(tree)

        first_component = renderer._components["0"]

        # Push data again (simulates re-push after sort)
        tree.collect_execute()
        grid._push_data()

        # Same component should be reused
        assert renderer._components["0"] is first_component


class TestAddColumnOverload:
    """Test that add_column accepts both str and Renderer."""

    def test_add_column_string(self):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        assert col._property_name == "name"
        assert col._renderer is None

    def test_add_column_renderer(self):
        grid = Grid()
        renderer = LitRenderer.of("<span>x</span>")
        col = grid.add_column(renderer, header="Name")
        assert col._renderer is renderer
        assert col._property_name == ""

    def test_column_set_renderer(self):
        col = Column("col0", "name", "Name")
        renderer = LitRenderer.of("<span>x</span>")
        result = col.set_renderer(renderer)
        assert result is col
        assert col._renderer is renderer
