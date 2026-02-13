"""Test View 6: ComboBox & MultiSelectComboBox — /test/combo-box"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, ComboBox, MultiSelectComboBox, Span, VerticalLayout,
)
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/combo-box", page_title="Test: ComboBox", layout=TestMainLayout)
@Menu(title="ComboBox", order=6)
class TestComboBoxView(VerticalLayout):
    def __init__(self):
        # --- ComboBox renders with label ---
        cb1 = ComboBox("Fruit")
        cb1.set_id("cb1")
        cb1.set_items("Apple", "Banana", "Cherry")
        cb1_val = Span("")
        cb1_val.set_id("cb1-val")
        cb1.add_value_change_listener(
            lambda e: cb1_val.set_text(str(e.get("value", "")))
        )

        # --- ComboBox set_value programmatic ---
        cb_pre = ComboBox("Preset")
        cb_pre.set_id("cb-pre")
        cb_pre.set_items("Apple", "Banana", "Cherry")
        cb_pre.set_value("Cherry")

        # --- ComboBox placeholder ---
        cb_ph = ComboBox("Placeholder")
        cb_ph.set_id("cb-ph")
        cb_ph.set_items("A", "B")
        cb_ph.set_placeholder("Search...")

        # --- ComboBox clear button ---
        cb_clear = ComboBox("Clearable")
        cb_clear.set_id("cb-clear")
        cb_clear.set_items("A", "B", "C")
        cb_clear.set_value("A")
        cb_clear.set_clear_button_visible(True)

        # --- ComboBox allow_custom_value ---
        cb_cust_val = Span("")
        cb_cust_val.set_id("cb-cust")
        cb_custom = ComboBox("Custom")
        cb_custom.set_id("cb-custom")
        cb_custom.set_items("Apple", "Banana")
        cb_custom.set_allow_custom_value(True)
        cb_custom.add_custom_value_set_listener(
            lambda e: cb_cust_val.set_text(str(e.get("value", e.get("detail", ""))))
        )

        # --- ComboBox item_label_generator ---
        cb_gen = ComboBox("Generated")
        cb_gen.set_id("cb-gen")
        items = [{"id": 1, "name": "Apple"}, {"id": 2, "name": "Banana"}]
        cb_gen.set_items(*items)
        cb_gen.set_item_label_generator(lambda x: x["name"])

        # --- ComboBox auto_open disabled ---
        cb_noauto = ComboBox("No auto-open")
        cb_noauto.set_id("cb-noauto")
        cb_noauto.set_items("X", "Y", "Z")
        cb_noauto.set_auto_open(False)

        # --- MultiSelectComboBox renders ---
        mscb1 = MultiSelectComboBox("Tags")
        mscb1.set_id("mscb1")
        mscb1.set_items("A", "B", "C")
        mscb1_val = Span("")
        mscb1_val.set_id("mscb1-val")
        mscb1.add_value_change_listener(
            lambda e: mscb1_val.set_text(
                ",".join(sorted(e.get("value", set())))
            )
        )

        # --- MultiSelectComboBox set_value programmatic ---
        mscb_pre = MultiSelectComboBox("Preset")
        mscb_pre.set_id("mscb-pre")
        mscb_pre.set_items("X", "Y", "Z")
        mscb_pre.set_value({"X", "Z"})

        # --- MultiSelectComboBox deselect_all ---
        mscb_des = MultiSelectComboBox("Deselectable")
        mscb_des.set_id("mscb-des")
        mscb_des.set_items("P", "Q", "R")
        mscb_des.set_value({"P", "Q"})
        btn_des = Button("Deselect all")
        btn_des.set_id("btn-mscb-des")
        btn_des.add_click_listener(lambda e: mscb_des.deselect_all())

        # --- MultiSelectComboBox clear button ---
        mscb_clr = MultiSelectComboBox("Clearable")
        mscb_clr.set_id("mscb-clr")
        mscb_clr.set_items("A", "B", "C")
        mscb_clr.set_value({"A", "B"})
        mscb_clr.set_clear_button_visible(True)

        # --- MultiSelectComboBox read_only ---
        mscb_ro = MultiSelectComboBox("ReadOnly")
        mscb_ro.set_id("mscb-ro")
        mscb_ro.set_items("A", "B")
        mscb_ro.set_value({"A"})
        mscb_ro.set_read_only(True)

        # --- ComboBox prefix component ---
        from vaadin.flow.components.icon import Icon
        cb_prefix = ComboBox("With icon")
        cb_prefix.set_id("cb-prefix")
        cb_prefix.set_items("Red", "Green", "Blue")
        cb_prefix.set_prefix_component(Icon("lumo:search"))

        # --- ComboBox overlay width ---
        cb_ow = ComboBox("Wide overlay")
        cb_ow.set_id("cb-ow")
        cb_ow.set_items("Short", "Medium", "Long item text")
        cb_ow.set_overlay_width("400px")

        # --- MultiSelectComboBox selected items on top ---
        mscb_top = MultiSelectComboBox("Items on top")
        mscb_top.set_id("mscb-top")
        mscb_top.set_items("A", "B", "C", "D")
        mscb_top.set_selected_items_on_top(True)

        # --- MultiSelectComboBox keep filter ---
        mscb_kf = MultiSelectComboBox("Keep filter")
        mscb_kf.set_id("mscb-kf")
        mscb_kf.set_items("Apple", "Banana", "Cherry")
        mscb_kf.set_keep_filter(True)

        self.add(
            cb1, cb1_val,
            cb_pre,
            cb_ph,
            cb_clear,
            cb_custom, cb_cust_val,
            cb_gen,
            cb_noauto,
            cb_prefix,
            cb_ow,
            mscb1, mscb1_val,
            mscb_pre,
            mscb_des, btn_des,
            mscb_clr,
            mscb_ro,
            mscb_top,
            mscb_kf,
        )
