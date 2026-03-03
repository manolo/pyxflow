"""Test View 33: Grid Editor -- Inline Row Editing -- /test/grid-editor"""

from dataclasses import dataclass

from pyxflow import Route
from pyxflow.components import (
    Button, Grid, IntegerField, Span, TextField, VerticalLayout,
)
from pyxflow.data.binder import Binder
from pyxflow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@dataclass
class Person:
    name: str
    age: int
    email: str


PEOPLE_DATA = [
    Person("Alice", 30, "alice@example.com"),
    Person("Bob", 25, "bob@example.com"),
    Person("Charlie", 35, "charlie@example.com"),
    Person("Diana", 28, "diana@example.com"),
    Person("Eve", 32, "eve@example.com"),
]


def _to_dict(p: Person) -> dict:
    return {"name": p.name, "age": p.age, "email": p.email}


@Route("test/grid-editor", page_title="Test: Grid Editor", layout=TestMainLayout)
@Menu(title="33 Grid Editor", order=33)
class TestGridEditorView(VerticalLayout):
    def __init__(self):
        # --- Status labels ---
        self.status_buffered = Span("")
        self.status_buffered.set_id("status-buffered")
        self.status_unbuffered = Span("")
        self.status_unbuffered.set_id("status-unbuffered")

        # ========== BUFFERED EDITOR ==========
        self.items_buffered = [_to_dict(p) for p in PEOPLE_DATA]

        grid_buf = Grid()
        grid_buf.set_id("grid-buffered")
        name_col = grid_buf.add_column("name", header="Name")
        age_col = grid_buf.add_column("age", header="Age")
        email_col = grid_buf.add_column("email", header="Email")
        grid_buf.set_all_rows_visible(True)

        # Editor fields
        name_field = TextField()
        name_field.set_id("editor-name")
        age_field = IntegerField()
        age_field.set_id("editor-age")
        email_field = TextField()
        email_field.set_id("editor-email")

        # Set editor components on columns
        name_col.set_editor_component(name_field)
        age_col.set_editor_component(age_field)
        email_col.set_editor_component(email_field)

        # Binder
        binder = Binder()
        binder.for_field(name_field).bind(
            lambda item: item.get("name", ""),
            lambda item, val: item.__setitem__("name", val),
        )
        binder.for_field(age_field).bind(
            lambda item: item.get("age", 0),
            lambda item, val: item.__setitem__("age", val),
        )
        binder.for_field(email_field).bind(
            lambda item: item.get("email", ""),
            lambda item, val: item.__setitem__("email", val),
        )

        # Configure editor
        editor_buf = grid_buf.get_editor()
        editor_buf.set_binder(binder)
        editor_buf.set_buffered(True)

        # Open editor on double-click
        grid_buf.add_item_double_click_listener(
            lambda e: editor_buf.edit_item(e["item"])
        )

        # Save/Cancel buttons
        btn_save = Button("Save")
        btn_save.set_id("btn-save")
        btn_save.add_click_listener(lambda e: editor_buf.save())

        btn_cancel = Button("Cancel")
        btn_cancel.set_id("btn-cancel")
        btn_cancel.add_click_listener(lambda e: editor_buf.cancel())

        # Listeners
        editor_buf.add_save_listener(
            lambda e: self.status_buffered.set_text(f"Saved: {e.item.get('name', '')}")
        )
        editor_buf.add_cancel_listener(
            lambda e: self.status_buffered.set_text("Cancelled")
        )

        grid_buf.set_items(self.items_buffered)

        # ========== UNBUFFERED EDITOR ==========
        self.items_unbuffered = [_to_dict(p) for p in PEOPLE_DATA[:3]]

        grid_unbuf = Grid()
        grid_unbuf.set_id("grid-unbuffered")
        unbuf_name_col = grid_unbuf.add_column("name", header="Name")
        unbuf_age_col = grid_unbuf.add_column("age", header="Age")
        grid_unbuf.set_all_rows_visible(True)

        unbuf_name_field = TextField()
        unbuf_name_field.set_id("unbuf-editor-name")
        unbuf_age_field = IntegerField()
        unbuf_age_field.set_id("unbuf-editor-age")

        unbuf_name_col.set_editor_component(unbuf_name_field)
        unbuf_age_col.set_editor_component(unbuf_age_field)

        unbuf_binder = Binder()
        unbuf_binder.for_field(unbuf_name_field).bind(
            lambda item: item.get("name", ""),
            lambda item, val: item.__setitem__("name", val),
        )
        unbuf_binder.for_field(unbuf_age_field).bind(
            lambda item: item.get("age", 0),
            lambda item, val: item.__setitem__("age", val),
        )

        editor_unbuf = grid_unbuf.get_editor()
        editor_unbuf.set_binder(unbuf_binder)
        # Unbuffered is the default (buffered=False)

        # Open on single click
        grid_unbuf.add_item_click_listener(
            lambda e: editor_unbuf.edit_item(e["item"])
        )

        editor_unbuf.add_open_listener(
            lambda e: self.status_unbuffered.set_text(f"Editing: {e.item.get('name', '')}")
        )
        editor_unbuf.add_close_listener(
            lambda e: self.status_unbuffered.set_text(f"Closed: {e.item.get('name', '')}")
        )

        grid_unbuf.set_items(self.items_unbuffered)

        self.add(
            Span("Buffered Editor (double-click to edit):"),
            grid_buf, btn_save, btn_cancel, self.status_buffered,
            Span("Unbuffered Editor (click to edit):"),
            grid_unbuf, self.status_unbuffered,
        )
