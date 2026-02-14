"""Test View 9: Grid — Selection, Sorting, Events — /test/grid-features"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, Grid, GridDropMode, SelectionMode, Span, VerticalLayout,
)
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


ITEMS = [
    {"name": "Alice", "age": 30, "email": "alice@x.com"},
    {"name": "Bob", "age": 25, "email": "bob@x.com"},
    {"name": "Charlie", "age": 35, "email": "charlie@x.com"},
    {"name": "Diana", "age": 28, "email": "diana@x.com"},
    {"name": "Eve", "age": 32, "email": "eve@x.com"},
]


@Route("test/grid-features", page_title="Test: Grid Features", layout=TestMainLayout)
@Menu(title="Grid Features", order=9)
class TestGridFeaturesView(VerticalLayout):
    def __init__(self):
        # --- Single selection grid ---
        grid_single = Grid()
        grid_single.set_id("grid-single")
        grid_single.add_column("name", header="Name").set_sortable(True)
        grid_single.add_column("age", header="Age").set_sortable(True)
        col_email = grid_single.add_column("email", header="Email")
        grid_single.set_items(ITEMS)
        grid_single.set_selection_mode(SelectionMode.SINGLE)
        grid_single.set_all_rows_visible(True)

        sel_val = Span("")
        sel_val.set_id("grid-single-sel")
        grid_single.add_selection_listener(
            lambda e: sel_val.set_text(
                ",".join(item["name"] for item in grid_single.get_selected_items())
            )
        )

        # --- Programmatic select ---
        btn_sel = Button("Select Bob")
        btn_sel.set_id("btn-sel-bob")
        btn_sel.add_click_listener(lambda e: grid_single.select_item(ITEMS[1]))

        # --- Multi selection grid ---
        grid_multi = Grid()
        grid_multi.set_id("grid-multi")
        grid_multi.add_column("name", header="Name")
        grid_multi.add_column("age", header="Age")
        grid_multi.set_items(ITEMS)
        grid_multi.set_selection_mode(SelectionMode.MULTI)
        grid_multi.set_all_rows_visible(True)

        multi_val = Span("")
        multi_val.set_id("grid-multi-sel")
        grid_multi.add_selection_listener(
            lambda e: multi_val.set_text(
                ",".join(sorted(item["name"] for item in grid_multi.get_selected_items()))
            )
        )

        btn_sel_all = Button("Select all")
        btn_sel_all.set_id("btn-sel-all")
        btn_sel_all.add_click_listener(lambda e: grid_multi.select_all())

        btn_desel_all = Button("Deselect all")
        btn_desel_all.set_id("btn-desel-all")
        btn_desel_all.add_click_listener(lambda e: grid_multi.deselect_all())

        # --- Sorting listener ---
        sort_val = Span("")
        sort_val.set_id("grid-sort")
        grid_single.add_sort_listener(
            lambda e: sort_val.set_text("sorted")
        )

        # --- Item click listener ---
        click_val = Span("")
        click_val.set_id("grid-click")
        grid_single.add_item_click_listener(
            lambda e: click_val.set_text(e.get("item", {}).get("name", ""))
        )

        # --- Item double click ---
        dbl_val = Span("")
        dbl_val.set_id("grid-dbl")
        grid_single.add_item_double_click_listener(
            lambda e: dbl_val.set_text(e.get("item", {}).get("name", ""))
        )

        # --- Remove column ---
        btn_remove = Button("Remove email column")
        btn_remove.set_id("btn-remove-col")
        btn_remove.add_click_listener(lambda e: grid_single.remove_column(col_email))

        # --- Drag and drop ---
        grid_dnd = Grid()
        grid_dnd.set_id("grid-dnd")
        grid_dnd.add_column("name", header="Name")
        grid_dnd.add_column("age", header="Age")
        grid_dnd.set_items(ITEMS)
        grid_dnd.set_rows_draggable(True)
        grid_dnd.set_drop_mode(GridDropMode.BETWEEN)
        grid_dnd.set_all_rows_visible(True)

        # --- Empty state text ---
        grid_empty = Grid()
        grid_empty.set_id("grid-empty")
        grid_empty.add_column("name", header="Name")
        grid_empty.set_items([])
        grid_empty.set_empty_state_text("No data available")
        grid_empty.set_all_rows_visible(True)

        # --- Remove all columns ---
        btn_remove_all = Button("Remove all columns")
        btn_remove_all.set_id("btn-remove-all-col")
        btn_remove_all.add_click_listener(lambda e: grid_multi.remove_all_columns())

        self.add(
            grid_single, sel_val, btn_sel,
            sort_val, click_val, dbl_val,
            btn_remove,
            grid_multi, multi_val,
            btn_sel_all, btn_desel_all,
            btn_remove_all,
            grid_dnd,
            grid_empty,
        )
