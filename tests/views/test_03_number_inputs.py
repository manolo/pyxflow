"""Test View 3: Number Input Fields — /test/number-inputs"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, Icon, IntegerField, NumberField, Span, VerticalLayout,
)
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/number-inputs", page_title="Test: Number Inputs", layout=TestMainLayout)
@Menu(title="03 Number Inputs", order=3)
class TestNumberInputsView(VerticalLayout):
    def __init__(self):
        # --- NumberField renders with label ---
        nf1 = NumberField("Price")
        nf1.set_id("nf1")
        nf1_val = Span("")
        nf1_val.set_id("nf1-val")
        nf1.add_value_change_listener(
            lambda e: nf1_val.set_text(str(e.get("value", "")))
        )

        # --- NumberField set_value programmatic ---
        nf_pre = NumberField("Preset")
        nf_pre.set_id("nf-pre")
        nf_pre.set_value(99.9)

        # --- NumberField min/max ---
        nf_range = NumberField("Range 0-100")
        nf_range.set_id("nf-range")
        nf_range.set_min(0)
        nf_range.set_max(100)

        # --- NumberField step ---
        nf_step = NumberField("Step")
        nf_step.set_id("nf-step")
        nf_step.set_step(0.5)
        nf_step.set_step_buttons_visible(True)
        nf_step.set_value(5.0)
        nf_step_val = Span("5.0")
        nf_step_val.set_id("nf-step-val")
        nf_step.add_value_change_listener(
            lambda e: nf_step_val.set_text(str(e.get("value", "")))
        )

        # --- NumberField clear button ---
        nf_clear = NumberField("Clearable")
        nf_clear.set_id("nf-clear")
        nf_clear.set_value(42.0)
        nf_clear.set_clear_button_visible(True)

        # --- NumberField prefix/suffix ---
        nf_fix = NumberField("Amount")
        nf_fix.set_id("nf-fix")
        nf_fix.set_prefix_component(Icon("lumo:plus"))
        nf_fix.set_suffix_component(Span("USD"))

        # --- IntegerField renders ---
        if1 = IntegerField("Qty")
        if1.set_id("if1")
        if1_val = Span("")
        if1_val.set_id("if1-val")
        if1.add_value_change_listener(
            lambda e: if1_val.set_text(str(e.get("value", "")))
        )

        # --- IntegerField set_value programmatic ---
        if_pre = IntegerField("Preset Int")
        if_pre.set_id("if-pre")
        if_pre.set_value(7)

        # --- IntegerField step buttons ---
        if_step = IntegerField("Step Int")
        if_step.set_id("if-step")
        if_step.set_step(2)
        if_step.set_step_buttons_visible(True)
        if_step.set_value(0)
        if_step_val = Span("0")
        if_step_val.set_id("if-step-val")
        if_step.add_value_change_listener(
            lambda e: if_step_val.set_text(str(e.get("value", "")))
        )

        # --- IntegerField min/max ---
        if_range = IntegerField("Range 1-10")
        if_range.set_id("if-range")
        if_range.set_min(1)
        if_range.set_max(10)

        self.add(
            nf1, nf1_val,
            nf_pre,
            nf_range,
            nf_step, nf_step_val,
            nf_clear,
            nf_fix,
            if1, if1_val,
            if_pre,
            if_step, if_step_val,
            if_range,
        )
