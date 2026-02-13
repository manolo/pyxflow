"""Test View 10: TreeGrid — /test/tree-grid"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, RouterLink, SelectionMode, Span, TreeGrid, VerticalLayout,
)


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


@Route("test/tree-grid", page_title="Test: TreeGrid")
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

        # --- Nav link ---
        nav_link = RouterLink("Next: Dialog", "test/dialog")
        nav_link.set_id("nav-next")

        self.add(tg, sel_val, btn_expand, btn_collapse, nav_link)
