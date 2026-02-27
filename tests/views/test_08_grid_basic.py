"""Test View 8: Grid — Columns & Data — /test/grid-basic"""

from pyflow import Route
from pyflow.components import (
    Button, ComponentRenderer, Grid, HorizontalLayout, LitRenderer,
    Span, VerticalLayout,
)
from pyflow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


PEOPLE = [
    Person("Alice", 30, "alice@example.com"),
    Person("Bob", 25, "bob@example.com"),
    Person("Charlie", 35, "charlie@example.com"),
    Person("Diana", 28, "diana@example.com"),
    Person("Eve", 32, "eve@example.com"),
]


@Route("test/grid-basic", page_title="Test: Grid Basic", layout=TestMainLayout)
@Menu(title="08 Grid Basic", order=8)
class TestGridBasicView(VerticalLayout):
    def __init__(self):
        # --- Basic grid with columns ---
        grid1 = Grid()
        grid1.set_id("grid1")
        grid1.add_column("name", header="Name").set_auto_width(True).set_key("name-col")
        grid1.add_column("age", header="Age").set_width("100px")
        grid1.add_column("email", header="Email").set_flex_grow(2)
        grid1.set_items([{"name": p.name, "age": p.age, "email": p.email} for p in PEOPLE])
        grid1.set_all_rows_visible(True)

        # --- Grid set_items replaces data ---
        new_data = [{"name": "Zoe", "age": 22, "email": "zoe@example.com"}]
        btn_replace = Button("Replace data")
        btn_replace.set_id("btn-replace")
        btn_replace.add_click_listener(lambda e: grid1.set_items(new_data))

        # --- Column set_resizable ---
        grid_res = Grid()
        grid_res.set_id("grid-res")
        grid_res.add_column("name", header="Resizable Name").set_resizable(True)
        grid_res.add_column("age", header="Age")
        grid_res.set_items([{"name": "Test", "age": 1}])
        grid_res.set_all_rows_visible(True)

        # --- Column set_text_align ---
        grid_align = Grid()
        grid_align.set_id("grid-align")
        grid_align.add_column("name", header="Name")
        grid_align.add_column("age", header="Age (center)").set_text_align("center")
        grid_align.set_items([{"name": "Test", "age": 99}])
        grid_align.set_all_rows_visible(True)

        # --- Column set_frozen / set_frozen_to_end ---
        grid_frozen = Grid()
        grid_frozen.set_id("grid-frozen")
        grid_frozen.add_column("name", header="Frozen").set_frozen(True).set_width("150px")
        grid_frozen.add_column("age", header="Age").set_width("300px")
        grid_frozen.add_column("email", header="Email").set_frozen_to_end(True).set_width("150px")
        grid_frozen.set_items([{"name": "Test", "age": 1, "email": "t@t.com"}])
        grid_frozen.set_all_rows_visible(True)

        # --- Column set_visible(False) ---
        grid_vis = Grid()
        grid_vis.set_id("grid-vis")
        grid_vis.add_column("name", header="Name")
        grid_vis.add_column("age", header="Hidden").set_visible(False)
        grid_vis.add_column("email", header="Email")
        grid_vis.set_items([{"name": "Test", "age": 1, "email": "t@t.com"}])
        grid_vis.set_all_rows_visible(True)

        # --- Column set_footer_text ---
        grid_foot = Grid()
        grid_foot.set_id("grid-foot")
        grid_foot.add_column("name", header="Name").set_footer_text("Total: 5")
        grid_foot.set_items([{"name": p.name} for p in PEOPLE])
        grid_foot.set_all_rows_visible(True)

        # --- LitRenderer ---
        grid_lit = Grid()
        grid_lit.set_id("grid-lit")
        lit_col = grid_lit.add_column(
            LitRenderer("<span>${item.name} (${item.age})</span>")
            .with_property("name", lambda p: p["name"])
            .with_property("age", lambda p: p["age"]),
            header="Lit"
        )
        grid_lit.set_items([{"name": p.name, "age": p.age} for p in PEOPLE[:2]])
        grid_lit.set_all_rows_visible(True)

        # --- ComponentRenderer ---
        grid_comp_result = Span("")
        grid_comp_result.set_id("grid-click")

        def _make_btn(item):
            b = Button(item["name"])
            b.add_click_listener(lambda e, n=item["name"]: grid_comp_result.set_text(n))
            return b

        grid_comp = Grid()
        grid_comp.set_id("grid-comp")
        grid_comp.add_column(ComponentRenderer(_make_btn), header="Action")
        grid_comp.add_column("age", header="Age")
        grid_comp.set_items([{"name": p.name, "age": p.age} for p in PEOPLE[:3]])
        grid_comp.set_all_rows_visible(True)

        # --- Column reorder ---
        grid_reorder = Grid()
        grid_reorder.set_id("grid-reorder")
        grid_reorder.add_column("name", header="Name")
        grid_reorder.add_column("age", header="Age")
        grid_reorder.set_items([{"name": "Test", "age": 1}])
        grid_reorder.set_column_reordering_allowed(True)
        grid_reorder.set_all_rows_visible(True)

        # --- Clear button (empty state test) ---
        btn_clear = Button("Clear data")
        btn_clear.set_id("btn-clear")
        btn_clear.add_click_listener(lambda e: grid1.set_items([]))

        self.add(
            grid1, btn_replace, btn_clear,
            grid_res,
            grid_align,
            grid_frozen,
            grid_vis,
            grid_foot,
            grid_lit,
            grid_comp, grid_comp_result,
            grid_reorder,
        )
