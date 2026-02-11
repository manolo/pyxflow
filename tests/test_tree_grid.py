"""Tests for TreeGrid component."""

import pytest

from vaadin.flow.components.grid import TreeGrid, Column
from vaadin.flow.components.renderer import LitRenderer
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


# --- Test data ---

ROOT_ITEMS = [
    {"name": "src", "type": "Folder"},
    {"name": "README.md", "type": "file"},
]

CHILDREN_MAP = {
    "src": [
        {"name": "main.py", "type": "file"},
        {"name": "utils", "type": "Folder"},
    ],
    "utils": [
        {"name": "helpers.py", "type": "file"},
    ],
}


def children_provider(item):
    return CHILDREN_MAP.get(item["name"], [])


class TestTreeGridCreation:

    def test_create_tree_grid(self):
        tg = TreeGrid()
        assert tg._tag == "vaadin-grid"
        assert tg._root_items == []
        assert tg._expanded_item_ids == set()

    def test_add_hierarchy_column(self):
        tg = TreeGrid()
        col = tg.add_hierarchy_column(lambda item: item["name"], header="Name")
        assert isinstance(col, Column)
        assert col._renderer is not None
        assert isinstance(col._renderer, LitRenderer)
        assert tg._hierarchy_column is col

    def test_hierarchy_column_template(self):
        tg = TreeGrid()
        col = tg.add_hierarchy_column(lambda item: item["name"])
        renderer = col._renderer
        assert isinstance(renderer, LitRenderer)
        assert "vaadin-grid-tree-toggle" in renderer._template
        # Uses Lit property bindings (dot prefix)
        assert ".leaf=" in renderer._template
        assert ".expanded=" in renderer._template
        assert ".level=" in renderer._template
        # model.expanded/level come from grid's row model
        assert "model.expanded" in renderer._template
        assert "model.level" in renderer._template


class TestTreeGridFlatten:

    def test_flat_items_no_provider(self):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS)
        assert len(tg._items) == 2
        assert tg._items[0]["name"] == "src"
        assert tg._items[0]["_level"] == 0
        assert tg._items[0]["_has_children"] is False  # No provider
        assert tg._items[1]["name"] == "README.md"

    def test_flat_items_with_provider(self):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)
        # Only root items visible (nothing expanded)
        assert len(tg._items) == 2
        assert tg._items[0]["_has_children"] is True
        assert tg._items[0]["_expanded"] is False
        assert tg._items[1]["_has_children"] is False

    def test_expand_shows_children(self):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)
        # Expand "src"
        tg.expand(ROOT_ITEMS[0])
        assert len(tg._items) == 4  # src, main.py, utils, README.md
        assert tg._items[0]["name"] == "src"
        assert tg._items[0]["_level"] == 0
        assert tg._items[0]["_expanded"] is True
        assert tg._items[1]["name"] == "main.py"
        assert tg._items[1]["_level"] == 1
        assert tg._items[2]["name"] == "utils"
        assert tg._items[2]["_level"] == 1
        assert tg._items[2]["_has_children"] is True
        assert tg._items[3]["name"] == "README.md"
        assert tg._items[3]["_level"] == 0

    def test_expand_nested(self):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)
        tg.expand(ROOT_ITEMS[0])  # expand src
        # Find the "utils" item (the original dict)
        utils_item = CHILDREN_MAP["src"][1]
        tg.expand(utils_item)
        assert len(tg._items) == 5  # src, main.py, utils, helpers.py, README.md
        assert tg._items[3]["name"] == "helpers.py"
        assert tg._items[3]["_level"] == 2

    def test_collapse_hides_children(self):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)
        tg.expand(ROOT_ITEMS[0])
        assert len(tg._items) == 4
        tg.collapse(ROOT_ITEMS[0])
        assert len(tg._items) == 2
        assert tg._items[0]["_expanded"] is False

    def test_collapse_nested_preserves_sub_expansion(self):
        """Collapsing a parent should hide nested children but remember sub-expansion."""
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)
        tg.expand(ROOT_ITEMS[0])
        utils_item = CHILDREN_MAP["src"][1]
        tg.expand(utils_item)
        assert len(tg._items) == 5
        # Collapse src
        tg.collapse(ROOT_ITEMS[0])
        assert len(tg._items) == 2
        # Re-expand src — utils should still be expanded
        tg.expand(ROOT_ITEMS[0])
        assert len(tg._items) == 5
        assert tg._items[2]["_expanded"] is True  # utils still expanded

    def test_level_values(self):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)
        tg.expand(ROOT_ITEMS[0])
        utils_item = CHILDREN_MAP["src"][1]
        tg.expand(utils_item)
        levels = [item["_level"] for item in tg._items]
        assert levels == [0, 1, 1, 2, 0]

    def test_set_items_clears_expansion(self):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)
        tg.expand(ROOT_ITEMS[0])
        assert len(tg._items) == 4
        # Re-set items should clear expansion
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)
        assert len(tg._items) == 2


class TestTreeGridUpdateExpandedState:

    def test_expand_via_server_call(self):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)
        # Simulate client call: $server.updateExpandedState("0", true)
        tg.update_expanded_state("0", True)
        assert len(tg._items) == 4  # src expanded

    def test_collapse_via_server_call(self):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)
        tg.update_expanded_state("0", True)  # expand
        assert len(tg._items) == 4
        tg.update_expanded_state("0", False)  # collapse
        assert len(tg._items) == 2

    def test_invalid_key_is_no_op(self):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)
        # Should not raise
        tg.update_expanded_state("999", True)
        assert len(tg._items) == 2

    def test_expand_already_expanded_is_idempotent(self):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)
        tg.update_expanded_state("0", True)
        tg.update_expanded_state("0", True)  # again
        assert len(tg._items) == 4


class TestTreeGridAttach:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_attach_and_push(self, tree):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.add_column("type", header="Type")
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)

        tg._attach(tree)
        tree.collect_changes()
        executes = tree.collect_execute()

        # Should have: initLazy, setSelectionMode, setHeaderRenderer x2,
        # setLitRenderer (hierarchy col), updateSize, set, confirm,
        # treeGridConnector override JS
        assert len(executes) > 5

        # Check tree override JS was injected
        tree_override_js = [e for e in executes if "__getRowLevel" in str(e)]
        assert len(tree_override_js) == 1
        # expandItem/collapseItem should call $server.updateExpandedState
        js_code = str(tree_override_js[0])
        assert "updateExpandedState" in js_code
        assert "expandItem" in js_code
        assert "collapseItem" in js_code

    def test_push_data_includes_tree_props(self, tree):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)

        tg._attach(tree)
        tree.collect_changes()
        executes = tree.collect_execute()

        # Find the $connector.set($1, $2) call (data push, has 4 elements)
        set_calls = [e for e in executes if "$connector.set($1, $2)" in str(e)]
        assert len(set_calls) == 1
        items_data = set_calls[0][2]
        assert items_data[0]["children"] is True
        assert items_data[0]["expanded"] is False
        assert items_data[0]["level"] == 0
        assert items_data[1]["children"] is False
        assert items_data[1]["level"] == 0

    def test_feature_19_has_grid_and_tree_methods(self, tree):
        """Verify Feature 19 includes standard grid methods + updateExpandedState."""
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)

        tg._attach(tree)
        changes = tree.collect_changes()

        # Find Feature 19 splices
        f19 = [c for c in changes if c.get("feat") == Feature.CLIENT_DELEGATE_HANDLERS]
        assert len(f19) >= 1
        all_methods = []
        for c in f19:
            all_methods.extend(c.get("add", []))
        assert "select" in all_methods
        assert "confirmUpdate" in all_methods
        assert "updateExpandedState" in all_methods

    def test_columns_created(self, tree):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"], header="Name")
        tg.add_column("type", header="Type")
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)

        tg._attach(tree)
        changes = tree.collect_changes()

        # Find column nodes
        col_tags = [c for c in changes
                    if c.get("key") == "tag" and c.get("value") == "vaadin-grid-column"]
        assert len(col_tags) == 2


class TestTreeGridAdditionalColumns:

    def test_non_hierarchy_column_data(self):
        tg = TreeGrid()
        tg.add_hierarchy_column(lambda item: item["name"])
        col = tg.add_column("type", header="Type")
        tg.set_items(ROOT_ITEMS, children_provider=children_provider)

        tree = StateTree()
        tg._attach(tree)
        tree.collect_changes()
        executes = tree.collect_execute()

        set_calls = [e for e in executes if "$connector.set($1, $2)" in str(e)]
        assert len(set_calls) == 1
        items_data = set_calls[0][2]
        # Non-hierarchy column should have its data
        assert items_data[0][col.internal_id] == "Folder"
        assert items_data[1][col.internal_id] == "file"
