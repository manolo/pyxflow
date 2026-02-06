"""Tests for Grid component."""

import pytest

from vaadin.flow.components.grid import Grid, Column
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestColumn:
    """Test Column configuration."""

    def test_create_column(self):
        col = Column("col0", "name", "Name")
        assert col.internal_id == "col0"
        assert col.property_name == "name"
        assert col.get_header() == "Name"

    def test_default_header(self):
        col = Column("col0", "email")
        assert col.get_header() == "email"

    def test_fluent_api(self):
        col = Column("col0", "name", "Name")
        result = col.set_width("200px").set_flex_grow(2).set_auto_width(True)
        assert result is col
        assert col._width == "200px"
        assert col._flex_grow == 2
        assert col._auto_width is True

    def test_create_element(self):
        tree = StateTree()
        col = Column("col0", "name", "Name")
        col.set_width("100px").set_auto_width(True)
        node = col._create_element(tree)

        assert node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-grid-column"
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "path") == "col0"
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "_flowId") == "col0"
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "width") == "100px"
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "autoWidth") is True


class TestGrid:
    """Test Grid component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_grid(self):
        grid = Grid()
        assert grid._tag == "vaadin-grid"
        assert grid._columns == []
        assert grid._items == []

    def test_add_column(self):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        assert isinstance(col, Column)
        assert col.internal_id == "col0"
        assert col.property_name == "name"
        assert col.get_header() == "Name"

    def test_add_multiple_columns(self):
        grid = Grid()
        col0 = grid.add_column("name", header="Name")
        col1 = grid.add_column("email", header="Email")
        assert col0.internal_id == "col0"
        assert col1.internal_id == "col1"
        assert len(grid._columns) == 2

    def test_set_items(self):
        grid = Grid()
        items = [{"name": "Alice"}, {"name": "Bob"}]
        grid.set_items(items)
        assert grid.get_items() == items
        # get_items returns a copy
        assert grid.get_items() is not grid._items

    def test_attach_creates_changes(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_items([{"name": "Alice"}])
        grid._attach(tree)

        changes = tree.collect_changes()
        # Should have: attach for grid, tag for grid, pageSize property,
        # attach for column, tag/path/_flowId for column,
        # splice to add column as child, Feature 19 splice
        assert len(changes) > 0

        # Find grid tag
        grid_tags = [c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-grid"]
        assert len(grid_tags) == 1

        # Find column tag
        col_tags = [c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-grid-column"]
        assert len(col_tags) == 1

        # Find pageSize property
        page_sizes = [c for c in changes if c.get("key") == "pageSize"]
        assert len(page_sizes) == 1
        assert page_sizes[0]["value"] == 50

    def test_attach_registers_client_methods(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid._attach(tree)

        changes = tree.collect_changes()
        # Find Feature 19 splice
        f19 = [c for c in changes if c.get("feat") == Feature.CLIENT_DELEGATE_HANDLERS]
        assert len(f19) == 1
        assert "select" in f19[0]["add"]
        assert "deselect" in f19[0]["add"]
        assert "confirmUpdate" in f19[0]["add"]

    def test_attach_queues_execute_commands(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_items([{"name": "Alice"}])
        grid._attach(tree)

        execute = tree.collect_execute()
        assert len(execute) > 0

        # First should be initLazy
        js_strings = [cmd[-1] for cmd in execute]
        assert any("gridConnector.initLazy" in js for js in js_strings)
        # Should have setSelectionMode
        assert any("setSelectionMode" in js for js in js_strings)
        # Should have setHeaderRenderer
        assert any("setHeaderRenderer" in js for js in js_strings)
        # Should have updateSize, set, confirm for data push
        assert any("updateSize" in js for js in js_strings)
        assert any("$connector.set" in js for js in js_strings)
        assert any("$connector.confirm" in js for js in js_strings)

    def test_data_format(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.add_column("email", header="Email")
        grid.set_items([
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"},
        ])
        grid._attach(tree)

        execute = tree.collect_execute()
        # Find the $connector.set command (not setSelectionMode/setHeaderRenderer)
        set_cmd = None
        for cmd in execute:
            if "$connector.set(" in cmd[-1]:
                set_cmd = cmd
                break
        assert set_cmd is not None

        # The items array is arg at index 2 (after grid_ref and startIndex)
        items = set_cmd[2]
        assert len(items) == 2
        assert items[0]["key"] == "0"
        assert items[0]["col0"] == "Alice"
        assert items[0]["col1"] == "alice@example.com"
        assert items[1]["key"] == "1"
        assert items[1]["col0"] == "Bob"
        assert items[1]["col1"] == "bob@example.com"

    def test_selection_listener(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}])
        grid._attach(tree)
        tree.collect_changes()
        tree.collect_execute()

        selected = []
        grid.add_selection_listener(lambda e: selected.append(e))

        # Simulate client selecting item "0"
        grid.select("0")
        assert len(selected) == 1
        assert selected[0]["item"]["name"] == "Alice"

    def test_deselection_listener(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_items([{"name": "Alice"}])
        grid._attach(tree)

        selected = []
        grid.add_selection_listener(lambda e: selected.append(e))

        grid.select("0")
        grid.deselect("0")
        assert len(selected) == 2
        assert selected[1]["item"] is None

    def test_missing_property(self, tree):
        """Columns handle missing item properties gracefully."""
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.add_column("email", header="Email")
        grid.set_items([{"name": "Alice"}])  # no email
        grid._attach(tree)

        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert items[0]["col0"] == "Alice"
        assert items[0]["col1"] == ""  # missing = empty string

    def test_set_items_after_attach(self, tree):
        """Setting items after attach triggers data push."""
        grid = Grid()
        grid.add_column("name", header="Name")
        grid._attach(tree)
        tree.collect_execute()  # drain init commands

        grid.set_items([{"name": "Alice"}])
        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("updateSize" in js for js in js_strings)
        assert any("$connector.set" in js for js in js_strings)

    def test_column_width_after_attach(self, tree):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        grid._attach(tree)
        tree.collect_changes()

        col.set_width("200px")
        changes = tree.collect_changes()
        width_changes = [c for c in changes if c.get("key") == "width"]
        assert len(width_changes) == 1
        assert width_changes[0]["value"] == "200px"

    def test_update_size_value(self, tree):
        """updateSize should pass the correct item count."""
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_items([{"name": "A"}, {"name": "B"}, {"name": "C"}])
        grid._attach(tree)

        execute = tree.collect_execute()
        size_cmd = [cmd for cmd in execute if "updateSize" in cmd[-1]][0]
        # size_cmd format: [grid_ref, size, "return ..."]
        assert size_cmd[1] == 3
