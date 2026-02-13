"""Test View 2: Text Input Fields — /test/text-inputs"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, EmailField, Icon, PasswordField, Span,
    TextArea, TextField, VerticalLayout,
)
from vaadin.flow.components.value_change_mode import ValueChangeMode
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/text-inputs", page_title="Test: Text Inputs", layout=TestMainLayout)
@Menu(title="Text Inputs", order=2)
class TestTextInputsView(VerticalLayout):
    def __init__(self):
        # --- TextField renders with label ---
        tf1 = TextField("Name")
        tf1.set_id("tf1")
        tf1_val = Span("")
        tf1_val.set_id("tf1-val")
        tf1.add_value_change_listener(lambda e: tf1_val.set_text(str(e.get("value", ""))))

        # --- TextField set_value programmatic ---
        tf_preset = TextField("Preset")
        tf_preset.set_id("tf-preset")
        tf_preset.set_value("preset")

        # --- TextField set_placeholder ---
        tf_ph = TextField("With placeholder")
        tf_ph.set_id("tf-ph")
        tf_ph.set_placeholder("Enter name...")

        # --- TextField clear button ---
        tf_clear = TextField("Clearable")
        tf_clear.set_id("tf-clear")
        tf_clear.set_value("abc")
        tf_clear.set_clear_button_visible(True)
        tf_clear_val = Span("abc")
        tf_clear_val.set_id("tf-clear-val")
        tf_clear.add_value_change_listener(lambda e: tf_clear_val.set_text(str(e.get("value", ""))))

        # --- TextField max_length ---
        tf_max = TextField("Max 5")
        tf_max.set_id("tf-max")
        tf_max.set_max_length(5)

        # --- TextField pattern (client validation) ---
        tf_pat = TextField("Numbers only")
        tf_pat.set_id("tf-pat")
        tf_pat.set_pattern("[0-9]+")

        # --- TextField allowed_char_pattern ---
        tf_acp = TextField("Digits only")
        tf_acp.set_id("tf-acp")
        tf_acp.set_allowed_char_pattern("[0-9]")

        # --- TextField prefix/suffix ---
        tf_fix = TextField("Search")
        tf_fix.set_id("tf-fix")
        tf_fix.set_prefix_component(Icon("lumo:search"))
        tf_fix.set_suffix_component(Span("kg"))

        # --- TextField EAGER mode ---
        tf_eager = TextField("Eager")
        tf_eager.set_id("tf-eager")
        tf_eager.set_value_change_mode(ValueChangeMode.EAGER)
        tf_eager_val = Span("")
        tf_eager_val.set_id("tf-eager-val")
        tf_eager.add_value_change_listener(lambda e: tf_eager_val.set_text(str(e.get("value", ""))))

        # --- TextField helper text ---
        tf_help = TextField("Helper")
        tf_help.set_id("tf-help")
        tf_help.set_helper_text("Min 3 chars")

        # --- TextField tooltip ---
        tf_tip = TextField("Tooltip")
        tf_tip.set_id("tf-tip")
        tf_tip.set_tooltip_text("Full name")

        # --- TextField set_label dynamically ---
        tf_lbl = TextField("Old")
        tf_lbl.set_id("tf-lbl")
        btn_lbl = Button("Change label")
        btn_lbl.set_id("btn-lbl")
        btn_lbl.add_click_listener(lambda e: tf_lbl.set_label("New"))

        # --- TextArea renders ---
        ta1 = TextArea("Bio")
        ta1.set_id("ta1")
        ta1_val = Span("")
        ta1_val.set_id("ta1-val")
        ta1.add_value_change_listener(lambda e: ta1_val.set_text(str(e.get("value", ""))))

        # --- TextArea clear button ---
        ta_clear = TextArea("Clearable area")
        ta_clear.set_id("ta-clear")
        ta_clear.set_value("some text")
        ta_clear.set_clear_button_visible(True)
        ta_clear_val = Span("some text")
        ta_clear_val.set_id("ta-clear-val")
        ta_clear.add_value_change_listener(lambda e: ta_clear_val.set_text(str(e.get("value", ""))))

        # --- PasswordField ---
        pf1 = PasswordField("Password")
        pf1.set_id("pf1")
        pf1_val = Span("")
        pf1_val.set_id("pf1-val")
        pf1.add_value_change_listener(lambda e: pf1_val.set_text(str(e.get("value", ""))))

        # --- PasswordField reveal button hidden ---
        pf_noreveal = PasswordField("No reveal")
        pf_noreveal.set_id("pf-noreveal")
        pf_noreveal.set_reveal_button_visible(False)

        # --- EmailField ---
        ef1 = EmailField("Email")
        ef1.set_id("ef1")
        ef1_val = Span("")
        ef1_val.set_id("ef1-val")
        ef1.add_value_change_listener(lambda e: ef1_val.set_text(str(e.get("value", ""))))

        self.add(
            tf1, tf1_val,
            tf_preset,
            tf_ph,
            tf_clear, tf_clear_val,
            tf_max,
            tf_pat,
            tf_acp,
            tf_fix,
            tf_eager, tf_eager_val,
            tf_help,
            tf_tip,
            tf_lbl, btn_lbl,
            ta1, ta1_val,
            ta_clear, ta_clear_val,
            pf1, pf1_val,
            pf_noreveal,
            ef1, ef1_val,
        )
