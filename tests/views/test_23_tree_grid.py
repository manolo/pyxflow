"""Test View 10: TreeGrid — /test/tree-grid"""

from pyflow import Route
from pyflow.components import (
    Button, SelectionMode, Span, TreeGrid, VerticalLayout,
)
from pyflow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


ROOT1_CHILDREN = [
    {"name": "Child1A", "children": []},
    {"name": "Child1B", "children": []},
]
GC2A1 = {"name": "GC2A1", "children": []}
CHILD2A = {"name": "Child2A", "children": [GC2A1]}
ROOT2_CHILDREN = [CHILD2A]

ROOT1 = {"name": "Root1", "children": ROOT1_CHILDREN}
ROOT2 = {"name": "Root2", "children": ROOT2_CHILDREN}
TREE_DATA = [ROOT1, ROOT2]


def _get_children(item):
    return item.get("children", [])


@Route("test/tree-grid", page_title="Test: TreeGrid", layout=TestMainLayout)
@Menu(title="23 TreeGrid", order=23)
class TestTreeGridView(VerticalLayout):
    def __init__(self):
        tg = TreeGrid()
        tg.set_id("tg1")
        tg.add_hierarchy_column(lambda item: item["name"], header="Name")
        tg.set_items(TREE_DATA, _get_children)
        tg.set_selection_mode(SelectionMode.SINGLE)

        sel_val = Span("")
        sel_val.set_id("tg1-sel")
        tg.add_selection_listener(
            lambda e: sel_val.set_text(
                ",".join(item["name"] for item in tg.get_selected_items())
            )
        )

        # --- Programmatic expand/collapse ---
        btn_expand = Button("Expand Root1")
        btn_expand.set_id("btn-expand")
        btn_expand.add_click_listener(lambda e: tg.expand(ROOT1))

        btn_collapse = Button("Collapse Root1")
        btn_collapse.set_id("btn-collapse")
        btn_collapse.add_click_listener(lambda e: tg.collapse(ROOT1))

        # --- TreeGrid with dynamic children provider (new objects each call) ---
        dyn_roots = [
            {"name": "DirA", "type": "dir"},
            {"name": "FileB", "type": "file"},
        ]

        def dynamic_provider(item):
            if item["name"] == "DirA":
                return [
                    {"name": "SubA1", "type": "dir"},
                    {"name": "FileA2", "type": "file"},
                ]
            if item["name"] == "SubA1":
                return [{"name": "Deep1", "type": "file"}]
            return []

        tg2 = TreeGrid()
        tg2.set_id("tg2")
        tg2.add_hierarchy_column(lambda item: item["name"], header="Name")
        tg2.set_items(dyn_roots, dynamic_provider)

        btn_expand_a = Button("Expand DirA")
        btn_expand_a.set_id("btn-expand-a")
        btn_expand_a.add_click_listener(lambda e: tg2.expand(dyn_roots[0]))

        self.add(tg, sel_val, btn_expand, btn_collapse, tg2, btn_expand_a)
