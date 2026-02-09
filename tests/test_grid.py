"""Tests for Grid component."""

import json
import pytest

from vaadin.flow.components.grid import (
    Grid, Column, SortDirection, GridSortOrder, SelectionMode, _GridSelectionColumn,
)
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
        assert col.get_header() == "Email"

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

    def test_set_resizable(self):
        col = Column("col0", "name", "Name")
        result = col.set_resizable(True)
        assert result is col
        assert col._resizable is True

    def test_resizable_on_element(self):
        tree = StateTree()
        col = Column("col0", "name", "Name")
        col.set_resizable(True)
        node = col._create_element(tree)
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "resizable") is True

    def test_resizable_after_attach(self):
        tree = StateTree()
        col = Column("col0", "name", "Name")
        node = col._create_element(tree)
        tree.collect_changes()

        col.set_resizable(True)
        changes = tree.collect_changes()
        resizable = [c for c in changes if c.get("key") == "resizable"]
        assert len(resizable) == 1
        assert resizable[0]["value"] is True

    def test_set_sortable(self):
        col = Column("col0", "name", "Name")
        result = col.set_sortable(True)
        assert result is col
        assert col._sortable is True


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


class TestColumnReordering:
    """Test column reordering and resizing."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_column_reordering_allowed(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_column_reordering_allowed(True)
        grid._attach(tree)

        changes = tree.collect_changes()
        reorder = [c for c in changes if c.get("key") == "columnReorderingAllowed"]
        assert len(reorder) == 1
        assert reorder[0]["value"] is True

    def test_column_reordering_after_attach(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid._attach(tree)
        tree.collect_changes()

        grid.set_column_reordering_allowed(True)
        changes = tree.collect_changes()
        reorder = [c for c in changes if c.get("key") == "columnReorderingAllowed"]
        assert len(reorder) == 1
        assert reorder[0]["value"] is True


class TestSorting:
    """Test grid sorting."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_sortable_column_header(self, tree):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        col.set_sortable(True)
        grid._attach(tree)

        execute = tree.collect_execute()
        header_cmds = [cmd for cmd in execute if "setHeaderRenderer" in cmd[-1]]
        assert len(header_cmds) == 1
        assert "showSorter: true" in header_cmds[0][-1]
        assert "sorterPath: 'col0'" in header_cmds[0][-1]

    def test_non_sortable_column_header(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid._attach(tree)

        execute = tree.collect_execute()
        header_cmds = [cmd for cmd in execute if "setHeaderRenderer" in cmd[-1]]
        assert "showSorter: false" in header_cmds[0][-1]
        assert "sorterPath: null" in header_cmds[0][-1]

    def test_sorters_changed_ascending(self, tree):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        col.set_sortable(True)
        grid.set_items([{"name": "Charlie"}, {"name": "Alice"}, {"name": "Bob"}])
        grid._attach(tree)
        tree.collect_execute()

        grid.sorters_changed(json.dumps([{"path": "col0", "direction": "asc"}]))
        execute = tree.collect_execute()

        # Find the set command to check sorted order
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert items[0]["col0"] == "Alice"
        assert items[1]["col0"] == "Bob"
        assert items[2]["col0"] == "Charlie"

    def test_sorters_changed_descending(self, tree):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        col.set_sortable(True)
        grid.set_items([{"name": "Alice"}, {"name": "Charlie"}, {"name": "Bob"}])
        grid._attach(tree)
        tree.collect_execute()

        grid.sorters_changed([{"path": "col0", "direction": "desc"}])
        execute = tree.collect_execute()

        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert items[0]["col0"] == "Charlie"
        assert items[1]["col0"] == "Bob"
        assert items[2]["col0"] == "Alice"

    def test_sort_listener(self, tree):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        col.set_sortable(True)
        grid.set_items([{"name": "A"}])
        grid._attach(tree)
        tree.collect_execute()

        events = []
        grid.add_sort_listener(lambda orders: events.append(orders))

        grid.sorters_changed([{"path": "col0", "direction": "asc"}])
        assert len(events) == 1
        assert len(events[0]) == 1
        assert events[0][0].column is col
        assert events[0][0].direction == SortDirection.ASCENDING

    def test_set_sort_order_programmatic(self, tree):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        col.set_sortable(True)
        grid.set_items([{"name": "B"}, {"name": "A"}])
        grid._attach(tree)
        tree.collect_execute()

        grid.set_sort_order([GridSortOrder(col, SortDirection.ASCENDING)])
        execute = tree.collect_execute()

        # Should have data push + setSorterDirections
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert items[0]["col0"] == "A"
        assert items[1]["col0"] == "B"

        dir_cmd = [cmd for cmd in execute if "setSorterDirections" in cmd[-1]][0]
        assert dir_cmd[1] == [{"column": "col0", "direction": "asc"}]

    def test_multi_sort(self, tree):
        grid = Grid()
        col_name = grid.add_column("name", header="Name")
        col_city = grid.add_column("city", header="City")
        col_name.set_sortable(True)
        col_city.set_sortable(True)
        grid.set_multi_sort(True)
        grid.set_items([
            {"name": "Alice", "city": "Berlin"},
            {"name": "Bob", "city": "Amsterdam"},
            {"name": "Alice", "city": "Amsterdam"},
        ])
        grid._attach(tree)
        tree.collect_execute()

        # Sort by name asc, then city asc
        grid.sorters_changed([
            {"path": "col0", "direction": "asc"},
            {"path": "col1", "direction": "asc"},
        ])
        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        # Primary sort: name asc, secondary: city asc
        assert items[0]["col0"] == "Alice"
        assert items[0]["col1"] == "Amsterdam"
        assert items[1]["col0"] == "Alice"
        assert items[1]["col1"] == "Berlin"
        assert items[2]["col0"] == "Bob"
        assert items[2]["col1"] == "Amsterdam"

    def test_multi_sort_property(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_multi_sort(True)
        grid._attach(tree)

        changes = tree.collect_changes()
        ms = [c for c in changes if c.get("key") == "multiSort"]
        assert len(ms) == 1
        assert ms[0]["value"] is True

    def test_sorters_changed_clears_on_empty(self, tree):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        col.set_sortable(True)
        grid.set_items([{"name": "B"}, {"name": "A"}])
        grid._attach(tree)
        tree.collect_execute()

        # Sort, then clear
        grid.sorters_changed([{"path": "col0", "direction": "asc"}])
        tree.collect_execute()
        grid.sorters_changed([])
        execute = tree.collect_execute()

        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        # Back to original order
        assert items[0]["col0"] == "B"
        assert items[1]["col0"] == "A"


class TestMultiSelect:
    """Test multi-select mode."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_multi_select_creates_selection_column(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_selection_mode(SelectionMode.MULTI)
        grid._attach(tree)

        changes = tree.collect_changes()
        sel_col_tags = [c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-grid-flow-selection-column"]
        assert len(sel_col_tags) == 1

    def test_multi_select_mode_in_execute(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_selection_mode(SelectionMode.MULTI)
        grid._attach(tree)

        execute = tree.collect_execute()
        mode_cmds = [cmd for cmd in execute if "setSelectionMode" in cmd[-1]]
        assert len(mode_cmds) == 1
        assert "'MULTI'" in mode_cmds[0][-1]

    def test_multi_select_individual(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_selection_mode(SelectionMode.MULTI)
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}])
        grid._attach(tree)
        tree.collect_execute()

        events = []
        grid.add_selection_listener(lambda e: events.append(e))

        grid.select("0")
        grid.select("2")
        assert len(events) == 2
        selected = events[1]["selected_items"]
        names = sorted(item["name"] for item in selected)
        assert names == ["Alice", "Charlie"]

    def test_multi_deselect(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_selection_mode(SelectionMode.MULTI)
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}])
        grid._attach(tree)

        grid.select("0")
        grid.select("1")
        grid.deselect("0")

        selected = grid.get_selected_items()
        assert len(selected) == 1
        assert selected[0]["name"] == "Bob"

    def test_select_all(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_selection_mode(SelectionMode.MULTI)
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}])
        grid._attach(tree)
        tree.collect_execute()

        events = []
        grid.add_selection_listener(lambda e: events.append(e))

        grid.select_all()
        assert len(events) == 1
        selected = events[0]["selected_items"]
        assert len(selected) == 3

    def test_deselect_all(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_selection_mode(SelectionMode.MULTI)
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}])
        grid._attach(tree)

        grid.select_all()
        grid.deselect_all()
        assert grid.get_selected_items() == []

    def test_selection_column_select_all_handler(self, tree):
        """Selection column's selectAll method delegates to grid."""
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_selection_mode(SelectionMode.MULTI)
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}])
        grid._attach(tree)

        # Call via selection column (simulates publishedEventHandler)
        grid._selection_column.select_all()
        assert len(grid.get_selected_items()) == 2

    def test_selection_column_registered_in_tree(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_selection_mode(SelectionMode.MULTI)
        grid._attach(tree)

        sel_node_id = grid._selection_column._node.id
        assert sel_node_id in tree._components
        assert tree._components[sel_node_id] is grid._selection_column

    def test_selection_column_feature_19(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_selection_mode(SelectionMode.MULTI)
        grid._attach(tree)

        changes = tree.collect_changes()
        # Find Feature 19 splices - one for grid, one for selection column
        f19 = [c for c in changes if c.get("feat") == Feature.CLIENT_DELEGATE_HANDLERS]
        assert len(f19) == 2  # grid + selection column
        sel_f19 = [c for c in f19 if "selectAll" in c.get("add", [])]
        assert len(sel_f19) == 1
        assert "deselectAll" in sel_f19[0]["add"]

    def test_select_all_checkbox_state(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_selection_mode(SelectionMode.MULTI)
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}])
        grid._attach(tree)
        tree.collect_changes()

        # Select one - should be indeterminate
        grid.select("0")
        changes = tree.collect_changes()
        indet = [c for c in changes if c.get("key") == "_indeterminate"]
        assert any(c["value"] is True for c in indet)

        # Select all - should be checked, not indeterminate
        grid.select("1")
        changes = tree.collect_changes()
        select_all = [c for c in changes if c.get("key") == "selectAll"]
        assert any(c["value"] is True for c in select_all)

    def test_get_selected_items_single_mode(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_items([{"name": "Alice"}])
        grid._attach(tree)

        assert grid.get_selected_items() == []
        grid.select("0")
        items = grid.get_selected_items()
        assert len(items) == 1
        assert items[0]["name"] == "Alice"

    def test_selected_flag_in_pushed_data(self, tree):
        """Items pushed to client should have selected: true/false."""
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_selection_mode(SelectionMode.MULTI)
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}])
        grid._attach(tree)
        tree.collect_execute()

        grid.select("0")
        # select_all_state update triggers _push_data indirectly via _fire_selection_event
        # but select() itself doesn't push data, so let's check via select_all
        grid.select_all()
        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert all(item["selected"] is True for item in items)

    def test_selection_mode_none(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_selection_mode(SelectionMode.NONE)
        grid._attach(tree)

        execute = tree.collect_execute()
        mode_cmds = [cmd for cmd in execute if "setSelectionMode" in cmd[-1]]
        assert "'NONE'" in mode_cmds[0][-1]


class TestLazyLoading:
    """Test lazy loading / DataProvider."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_set_data_provider(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")

        all_data = [{"name": f"Person {i}"} for i in range(100)]

        def fetch(offset, limit, sort_orders):
            return all_data[offset:offset + limit], len(all_data)

        grid.set_data_provider(fetch)
        grid._attach(tree)

        execute = tree.collect_execute()
        size_cmd = [cmd for cmd in execute if "updateSize" in cmd[-1]][0]
        assert size_cmd[1] == 100

        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert len(items) == 50  # page_size default
        assert items[0]["col0"] == "Person 0"
        assert items[49]["col0"] == "Person 49"

    def test_data_provider_set_requested_range(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")

        all_data = [{"name": f"Person {i}"} for i in range(100)]

        def fetch(offset, limit, sort_orders):
            return all_data[offset:offset + limit], len(all_data)

        grid.set_data_provider(fetch)
        grid._attach(tree)
        tree.collect_execute()

        # Simulate client requesting next page
        grid.set_requested_range(50, 50)
        execute = tree.collect_execute()

        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        # Offset should be 50
        assert set_cmd[1] == 50
        items = set_cmd[2]
        assert len(items) == 50
        assert items[0]["key"] == "50"
        assert items[0]["col0"] == "Person 50"

    def test_data_provider_with_sort(self, tree):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        col.set_sortable(True)

        all_data = [{"name": "Charlie"}, {"name": "Alice"}, {"name": "Bob"}]

        def fetch(offset, limit, sort_orders):
            items = all_data[:]
            for order in reversed(sort_orders):
                prop = order.column.property_name
                rev = order.direction == SortDirection.DESCENDING
                items = sorted(items, key=lambda x, p=prop: x.get(p, ""), reverse=rev)
            return items[offset:offset + limit], len(items)

        grid.set_data_provider(fetch)
        grid._attach(tree)
        tree.collect_execute()

        grid.sorters_changed([{"path": "col0", "direction": "asc"}])
        execute = tree.collect_execute()
        set_cmd = [cmd for cmd in execute if "$connector.set(" in cmd[-1]][0]
        items = set_cmd[2]
        assert items[0]["col0"] == "Alice"
        assert items[1]["col0"] == "Bob"
        assert items[2]["col0"] == "Charlie"

    def test_set_items_clears_data_provider(self):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_data_provider(lambda o, l, s: ([], 0))
        grid.set_items([{"name": "Alice"}])
        assert grid._data_provider is None
        assert grid.get_items() == [{"name": "Alice"}]

    def test_set_data_provider_clears_items(self):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_items([{"name": "Alice"}])
        grid.set_data_provider(lambda o, l, s: ([], 0))
        assert grid._items == []

    def test_data_provider_after_attach(self, tree):
        """Setting data provider after attach triggers fetch."""
        grid = Grid()
        grid.add_column("name", header="Name")
        grid._attach(tree)
        tree.collect_execute()

        data = [{"name": "Alice"}]
        grid.set_data_provider(lambda o, l, s: (data, 1))
        execute = tree.collect_execute()
        js_strings = [cmd[-1] for cmd in execute]
        assert any("updateSize" in js for js in js_strings)
        assert any("$connector.set" in js for js in js_strings)

    def test_set_viewport_range_noop_for_inmemory(self, tree):
        """set_viewport_range is a no-op for in-memory data."""
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.set_items([{"name": "A"}])
        grid._attach(tree)
        tree.collect_execute()

        grid.set_viewport_range(0, 10)
        execute = tree.collect_execute()
        assert len(execute) == 0
