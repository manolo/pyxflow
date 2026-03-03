"""Test View 14: MenuBar & ContextMenu — /test/menu"""

from pyxflow import Route
from pyxflow.components import (
    Button, ContextMenu, Div, MenuBar, Span, VerticalLayout,
)
from pyxflow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/menu", page_title="Test: Menu", layout=TestMainLayout)
@Menu(title="19 Menu", order=19)
class TestMenuView(VerticalLayout):
    def __init__(self):
        mb_result = Span("")
        mb_result.set_id("mb-result")

        # --- MenuBar ---
        mb = MenuBar()
        mb.set_id("mb1")
        file_item = mb.add_item("File")
        file_sub = file_item.get_sub_menu()
        file_sub.add_item("New", lambda e: mb_result.set_text("New"))
        open_item = file_sub.add_item("Open", lambda e: mb_result.set_text("Open"))
        open_item.set_enabled(False)

        edit_item = mb.add_item("Edit")
        edit_sub = edit_item.get_sub_menu()
        edit_sub.add_item("Copy", lambda e: mb_result.set_text("Copy"))
        paste_item = edit_sub.add_item("Paste")
        paste_sub = paste_item.get_sub_menu()
        paste_sub.add_item("Paste Special", lambda e: mb_result.set_text("Paste Special"))

        # --- Separator in submenu ---
        edit_sub.add_separator()
        edit_sub.add_item("Select All", lambda e: mb_result.set_text("Select All"))

        # --- MenuBar checkable ---
        bold_item = mb.add_item("Bold")
        bold_item.set_checkable(True)
        bold_item.add_click_listener(lambda e: mb_result.set_text(
            f"Bold:{bold_item.is_checked()}"
        ))

        # --- MenuItem aria-label ---
        help_item = mb.add_item("?")
        help_item.set_aria_label("Help")
        help_item.add_click_listener(lambda e: mb_result.set_text("Help"))

        # --- MenuBar open_on_hover ---
        mb_hover = MenuBar()
        mb_hover.set_id("mb-hover")
        mb_hover.set_open_on_hover(True)
        mb_hover.add_item("Hover me")

        # --- ContextMenu ---
        ctx_result = Span("")
        ctx_result.set_id("ctx-result")

        ctx_target = Div("Right-click me")
        ctx_target.set_id("ctx-target")
        ctx = ContextMenu(ctx_target)
        ctx.set_id("ctx1")
        ctx.add_item("Cut", lambda e: ctx_result.set_text("Cut"))
        ctx.add_item("Copy", lambda e: ctx_result.set_text("Copy"))
        ctx.add_item("Paste", lambda e: ctx_result.set_text("Paste"))

        # --- ContextMenu open_on_click ---
        ctx_target2 = Div("Left-click me")
        ctx_target2.set_id("ctx-target2")
        ctx2 = ContextMenu(ctx_target2)
        ctx2.set_id("ctx2")
        ctx2.set_open_on_click(True)
        ctx2.add_item("Action", lambda e: ctx_result.set_text("Action"))

        self.add(
            mb, mb_result,
            mb_hover,
            ctx, ctx_result,
            ctx2,
        )
