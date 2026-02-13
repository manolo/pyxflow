"""Test View 27: CustomField — /test/custom-field"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, CustomField, RouterLink, Span, TextField, VerticalLayout,
)


@Route("test/custom-field", page_title="Test: CustomField")
class TestCustomFieldView(VerticalLayout):
    def __init__(self):
        # --- CustomField with child fields ---
        cf = CustomField("Full Name")
        cf.set_id("cf1")
        first = TextField("First")
        first.set_id("cf-first")
        last = TextField("Last")
        last.set_id("cf-last")
        cf.add(first, last)

        cf_val = Span("")
        cf_val.set_id("cf-val")
        cf.add_value_change_listener(
            lambda e: cf_val.set_text(str(e.get("value", "")))
        )

        # --- CustomField read_only ---
        cf_ro = CustomField("Read Only")
        cf_ro.set_id("cf-ro")
        cf_ro.add(TextField("RO Field"))
        cf_ro.set_read_only(True)

        # --- CustomField invalid ---
        cf_inv = CustomField("With Error")
        cf_inv.set_id("cf-inv")
        cf_inv.add(TextField("Err Field"))
        btn_inv = Button("Set invalid")
        btn_inv.set_id("btn-cf-inv")

        def _set_inv(e):
            cf_inv.set_error_message("Invalid name")
            cf_inv.set_invalid(True)

        btn_inv.add_click_listener(_set_inv)

        # --- CustomField required ---
        cf_req = CustomField("Required")
        cf_req.set_id("cf-req")
        cf_req.add(TextField("Req Field"))
        cf_req.set_required_indicator_visible(True)

        # --- Nav link ---
        nav_link = RouterLink("Next: VirtualList", "test/virtual-list")
        nav_link.set_id("nav-next")

        self.add(
            cf, cf_val,
            cf_ro,
            cf_inv, btn_inv,
            cf_req,
            nav_link,
        )
