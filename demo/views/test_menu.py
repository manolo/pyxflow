"""Test View 14: MenuBar & ContextMenu — /test/menu"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, ContextMenu, Div, MenuBar, RouterLink, Span, VerticalLayout,
)


@Route("test/menu", page_title="Test: Menu")
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

        # --- MenuBar checkable ---
        bold_item = mb.add_item("Bold")
        bold_item.set_checkable(True)
        bold_item.add_click_listener(lambda e: mb_result.set_text(
            f"Bold:{bold_item.is_checked()}"
        ))

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

        # --- Nav link ---
        nav_link = RouterLink("Next: Layouts", "test/layouts")
        nav_link.set_id("nav-next")

        self.add(
            mb, mb_result,
            mb_hover,
            ctx, ctx_result,
            ctx2,
            nav_link,
        )
