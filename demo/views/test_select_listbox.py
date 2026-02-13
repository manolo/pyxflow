"""Test View 5: Select & ListBox — /test/select-listbox"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, Icon, ListBox, MultiSelectListBox, RouterLink, Select, Span,
    VerticalLayout,
)


@Route("test/select-listbox", page_title="Test: Select & ListBox")
class TestSelectListboxView(VerticalLayout):
    def __init__(self):
        # --- Select renders with label ---
        sel1 = Select("Country")
        sel1.set_id("sel1")
        sel1.set_items("US", "UK", "DE")
        sel1_val = Span("")
        sel1_val.set_id("sel1-val")
        sel1.add_value_change_listener(
            lambda e: sel1_val.set_text(str(e.get("value", "")))
        )

        # --- Select set_value programmatic ---
        sel_pre = Select("Preset")
        sel_pre.set_id("sel-pre")
        sel_pre.set_items("US", "UK", "DE")
        sel_pre.set_value("DE")

        # --- Select placeholder ---
        sel_ph = Select("Placeholder")
        sel_ph.set_id("sel-ph")
        sel_ph.set_items("A", "B", "C")
        sel_ph.set_placeholder("Choose...")

        # --- Select empty_selection_allowed ---
        sel_empty = Select("Empty allowed")
        sel_empty.set_id("sel-empty")
        sel_empty.set_items("US", "UK")
        sel_empty.set_value("US")
        sel_empty.set_empty_selection_allowed(True)

        # --- Select item_label_generator ---
        sel_gen = Select("Generated")
        sel_gen.set_id("sel-gen")
        sel_gen.set_items("us", "uk")
        sel_gen.set_item_label_generator(str.upper)

        # --- Select read_only ---
        sel_ro = Select("ReadOnly")
        sel_ro.set_id("sel-ro")
        sel_ro.set_items("A", "B")
        sel_ro.set_value("A")
        sel_ro.set_read_only(True)

        # --- ListBox renders items ---
        lb1 = ListBox()
        lb1.set_id("lb1")
        lb1.set_items("A", "B", "C")
        lb1_val = Span("")
        lb1_val.set_id("lb1-val")
        lb1.add_value_change_listener(
            lambda e: lb1_val.set_text(str(e.get("value", "")))
        )

        # --- ListBox set_value programmatic ---
        lb_pre = ListBox()
        lb_pre.set_id("lb-pre")
        lb_pre.set_items("X", "Y", "Z")
        lb_pre.set_value("Y")

        # --- ListBox item_label_generator ---
        lb_gen = ListBox()
        lb_gen.set_id("lb-gen")
        lb_gen.set_items(1, 2, 3)
        lb_gen.set_item_label_generator(lambda x: f"#{x}")

        # --- MultiSelectListBox renders ---
        mslb1 = MultiSelectListBox()
        mslb1.set_id("mslb1")
        mslb1.set_items("X", "Y", "Z")
        mslb1_val = Span("")
        mslb1_val.set_id("mslb1-val")
        mslb1.add_value_change_listener(
            lambda e: mslb1_val.set_text(
                ",".join(sorted(e.get("value", set())))
            )
        )

        # --- MultiSelectListBox set_value programmatic ---
        mslb_pre = MultiSelectListBox()
        mslb_pre.set_id("mslb-pre")
        mslb_pre.set_items("A", "B", "C")
        mslb_pre.set_value({"A", "C"})

        # --- MultiSelectListBox deselect_all ---
        mslb_des = MultiSelectListBox()
        mslb_des.set_id("mslb-des")
        mslb_des.set_items("P", "Q", "R")
        mslb_des.set_value({"P", "Q"})
        btn_des = Button("Deselect all")
        btn_des.set_id("btn-mslb-des")
        btn_des.add_click_listener(lambda e: mslb_des.deselect_all())

        # --- MultiSelectListBox read_only ---
        mslb_ro = MultiSelectListBox()
        mslb_ro.set_id("mslb-ro")
        mslb_ro.set_items("A", "B")
        mslb_ro.set_read_only(True)

        # --- Nav link ---
        nav_link = RouterLink("Next: ComboBox", "test/combo-box")
        nav_link.set_id("nav-next")

        self.add(
            sel1, sel1_val,
            sel_pre,
            sel_ph,
            sel_empty,
            sel_gen,
            sel_ro,
            lb1, lb1_val,
            lb_pre,
            lb_gen,
            mslb1, mslb1_val,
            mslb_pre,
            mslb_des, btn_des,
            mslb_ro,
            nav_link,
        )
