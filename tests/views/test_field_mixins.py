"""Test View 21: HasReadOnly, HasValidation, HasRequired — /test/field-mixins"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, ComboBox, DatePicker, Select, Span, TextField,
    VerticalLayout,
)
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/field-mixins", page_title="Test: Field Mixins", layout=TestMainLayout)
@Menu(title="18 Field Mixins", order=18)
class TestFieldMixinsView(VerticalLayout):
    def __init__(self):
        # --- HasReadOnly: TextField ---
        mix_tf = TextField("Text")
        mix_tf.set_id("mix-tf")
        btn_ro_on = Button("Set readonly")
        btn_ro_on.set_id("btn-ro-on")
        btn_ro_on.add_click_listener(lambda e: mix_tf.set_read_only(True))
        btn_ro_off = Button("Unset readonly")
        btn_ro_off.set_id("btn-ro-off")
        btn_ro_off.add_click_listener(lambda e: mix_tf.set_read_only(False))

        # --- HasReadOnly: Select ---
        mix_sel = Select("Select")
        mix_sel.set_id("mix-sel")
        mix_sel.set_items("A", "B", "C")
        btn_sel_ro = Button("Select readonly")
        btn_sel_ro.set_id("btn-sel-ro")
        btn_sel_ro.add_click_listener(lambda e: mix_sel.set_read_only(True))

        # --- HasReadOnly: DatePicker ---
        mix_dp = DatePicker("Date")
        mix_dp.set_id("mix-dp")
        btn_dp_ro = Button("DatePicker readonly")
        btn_dp_ro.set_id("btn-dp-ro")
        btn_dp_ro.add_click_listener(lambda e: mix_dp.set_read_only(True))

        # --- HasValidation: TextField ---
        btn_invalid = Button("Set invalid")
        btn_invalid.set_id("btn-invalid")

        def _set_invalid(e):
            mix_tf.set_error_message("Required field")
            mix_tf.set_invalid(True)

        btn_invalid.add_click_listener(_set_invalid)

        btn_valid = Button("Clear invalid")
        btn_valid.set_id("btn-valid")
        btn_valid.add_click_listener(lambda e: mix_tf.set_invalid(False))

        # --- HasValidation: Select ---
        btn_sel_inv = Button("Select invalid")
        btn_sel_inv.set_id("btn-sel-inv")

        def _sel_invalid(e):
            mix_sel.set_error_message("Choose one")
            mix_sel.set_invalid(True)

        btn_sel_inv.add_click_listener(_sel_invalid)

        # --- HasValidation: ComboBox ---
        mix_cb = ComboBox("Combo")
        mix_cb.set_id("mix-cb")
        mix_cb.set_items("X", "Y", "Z")
        btn_cb_inv = Button("ComboBox invalid")
        btn_cb_inv.set_id("btn-cb-inv")

        def _cb_invalid(e):
            mix_cb.set_error_message("Invalid selection")
            mix_cb.set_invalid(True)

        btn_cb_inv.add_click_listener(_cb_invalid)

        # --- HasRequired: TextField ---
        btn_req = Button("Set required")
        btn_req.set_id("btn-req")
        btn_req.add_click_listener(
            lambda e: mix_tf.set_required_indicator_visible(True)
        )

        # --- HasRequired: Select ---
        btn_sel_req = Button("Select required")
        btn_sel_req.set_id("btn-sel-req")
        btn_sel_req.add_click_listener(
            lambda e: mix_sel.set_required_indicator_visible(True)
        )

        # --- HasRequired: ComboBox ---
        btn_cb_req = Button("ComboBox required")
        btn_cb_req.set_id("btn-cb-req")
        btn_cb_req.add_click_listener(
            lambda e: mix_cb.set_required_indicator_visible(True)
        )

        # --- HasRequired: DatePicker ---
        btn_dp_req = Button("DatePicker required")
        btn_dp_req.set_id("btn-dp-req")
        btn_dp_req.add_click_listener(
            lambda e: mix_dp.set_required_indicator_visible(True)
        )

        self.add(
            mix_tf, btn_ro_on, btn_ro_off,
            mix_sel, btn_sel_ro,
            mix_dp, btn_dp_ro,
            btn_invalid, btn_valid,
            btn_sel_inv,
            mix_cb, btn_cb_inv,
            btn_req, btn_sel_req, btn_cb_req, btn_dp_req,
        )
