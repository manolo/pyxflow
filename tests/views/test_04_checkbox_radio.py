"""Test View 4: Checkbox & RadioButtonGroup — /test/checkbox-radio"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, Checkbox, CheckboxGroup, RadioButtonGroup, Span,
    VerticalLayout,
)
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/checkbox-radio", page_title="Test: Checkbox & Radio", layout=TestMainLayout)
@Menu(title="04 Checkbox & Radio", order=4)
class TestCheckboxRadioView(VerticalLayout):
    def __init__(self):
        # --- Checkbox renders with label ---
        cb1 = Checkbox("Accept terms")
        cb1.set_id("cb1")
        cb1_val = Span("")
        cb1_val.set_id("cb1-val")
        cb1.add_value_change_listener(
            lambda e: cb1_val.set_text(str(e.get("value", "")))
        )

        # --- Checkbox set_value programmatic ---
        cb_pre = Checkbox("Preset")
        cb_pre.set_id("cb-pre")
        cb_pre.set_value(True)

        # --- Checkbox indeterminate ---
        cb_ind = Checkbox("Indeterminate")
        cb_ind.set_id("cb-ind")
        cb_ind.set_indeterminate(True)

        # --- Checkbox set_label dynamic ---
        cb_lbl = Checkbox("Old")
        cb_lbl.set_id("cb-lbl")
        btn_lbl = Button("Change label")
        btn_lbl.set_id("btn-cb-lbl")
        btn_lbl.add_click_listener(lambda e: cb_lbl.set_label("New"))

        # --- Checkbox read_only ---
        cb_ro = Checkbox("ReadOnly")
        cb_ro.set_id("cb-ro")
        cb_ro.set_value(True)
        cb_ro.set_read_only(True)

        # --- Checkbox required ---
        cb_req = Checkbox("Required")
        cb_req.set_id("cb-req")
        cb_req.set_required_indicator_visible(True)

        # --- CheckboxGroup renders items ---
        cbg1 = CheckboxGroup("Colors")
        cbg1.set_id("cbg1")
        cbg1.set_items("Red", "Green", "Blue")
        cbg1_val = Span("")
        cbg1_val.set_id("cbg1-val")
        cbg1.add_value_change_listener(
            lambda e: cbg1_val.set_text(
                ",".join(sorted(e.get("value", set())))
            )
        )

        # --- CheckboxGroup set_value programmatic ---
        cbg_pre = CheckboxGroup("Preset")
        cbg_pre.set_id("cbg-pre")
        cbg_pre.set_items("A", "B", "C")
        cbg_pre.set_value({"A", "C"})

        # --- CheckboxGroup item_label_generator ---
        cbg_gen = CheckboxGroup("Generated")
        cbg_gen.set_id("cbg-gen")
        cbg_gen.set_items(1, 2, 3)
        cbg_gen.set_item_label_generator(lambda x: f"Item {x}")

        # --- CheckboxGroup select method ---
        cbg_sel = CheckboxGroup("Selectable")
        cbg_sel.set_id("cbg-sel")
        cbg_sel.set_items("Red", "Green", "Blue")
        btn_sel = Button("Select Red")
        btn_sel.set_id("btn-cbg-sel")
        btn_sel.add_click_listener(lambda e: cbg_sel.select("Red"))

        # --- RadioButtonGroup renders items ---
        rbg1 = RadioButtonGroup("Size")
        rbg1.set_id("rbg1")
        rbg1.set_items("S", "M", "L")
        rbg1_val = Span("")
        rbg1_val.set_id("rbg1-val")
        rbg1.add_value_change_listener(
            lambda e: rbg1_val.set_text(str(e.get("value", "")))
        )

        # --- RadioButtonGroup set_value programmatic ---
        rbg_pre = RadioButtonGroup("Preset")
        rbg_pre.set_id("rbg-pre")
        rbg_pre.set_items("X", "Y", "Z")
        rbg_pre.set_value("Y")

        # --- RadioButtonGroup item_label_generator ---
        rbg_gen = RadioButtonGroup("Generated")
        rbg_gen.set_id("rbg-gen")
        rbg_gen.set_items("sm", "md", "lg")
        rbg_gen.set_item_label_generator(
            {"sm": "Small", "md": "Medium", "lg": "Large"}.get
        )

        # --- RadioButtonGroup read_only ---
        rbg_ro = RadioButtonGroup("ReadOnly")
        rbg_ro.set_id("rbg-ro")
        rbg_ro.set_items("A", "B")
        rbg_ro.set_value("A")
        rbg_ro.set_read_only(True)

        # --- RadioButtonGroup required ---
        rbg_req = RadioButtonGroup("Required")
        rbg_req.set_id("rbg-req")
        rbg_req.set_items("Yes", "No")
        rbg_req.set_required_indicator_visible(True)

        self.add(
            cb1, cb1_val,
            cb_pre,
            cb_ind,
            cb_lbl, btn_lbl,
            cb_ro,
            cb_req,
            cbg1, cbg1_val,
            cbg_pre,
            cbg_gen,
            cbg_sel, btn_sel,
            rbg1, rbg1_val,
            rbg_pre,
            rbg_gen,
            rbg_ro,
            rbg_req,
        )
