"""Test View 13: Tabs, TabSheet, Accordion, Details — /test/tabs-accordion"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Accordion, Button, Details, Span, Tab, TabSheet, Tabs,
    VerticalLayout,
)
from vaadin.flow.menu import Menu
from demo.views.test_main_layout import TestMainLayout


@Route("test/tabs-accordion", page_title="Test: Tabs & Accordion", layout=TestMainLayout)
@Menu(title="Tabs & Accordion", order=13)
class TestTabsAccordionView(VerticalLayout):
    def __init__(self):
        # --- Tabs render ---
        tabs1 = Tabs(Tab("One"), Tab("Two"), Tab("Three"))
        tabs1.set_id("tabs1")
        tabs1_val = Span("")
        tabs1_val.set_id("tabs1-val")
        tabs1.add_selected_change_listener(
            lambda e: tabs1_val.set_text(str(tabs1.get_selected_index()))
        )

        # --- Tabs set_selected_index ---
        btn_tab = Button("Select Three")
        btn_tab.set_id("btn-tab3")
        btn_tab.add_click_listener(lambda e: tabs1.set_selected_index(2))

        # --- Tabs add tab dynamically ---
        btn_add_tab = Button("Add tab")
        btn_add_tab.set_id("btn-add-tab")
        btn_add_tab.add_click_listener(lambda e: tabs1.add(Tab("Four")))

        # --- Tabs orientation ---
        tabs_vert = Tabs(Tab("A"), Tab("B"))
        tabs_vert.set_id("tabs-vert")
        tabs_vert.set_orientation("vertical")

        # --- TabSheet ---
        ts = TabSheet()
        ts.set_id("ts1")
        ts.add("Info", Span("Info content"))
        ts.add("Settings", Span("Settings content"))
        ts_val = Span("")
        ts_val.set_id("ts-val")
        ts.add_selected_change_listener(
            lambda e: ts_val.set_text(str(ts.get_selected_index()))
        )

        # --- Accordion ---
        acc = Accordion()
        acc.set_id("acc1")
        acc.add("Panel 1", Span("Content 1"))
        acc.add("Panel 2", Span("Content 2"))
        acc_val = Span("")
        acc_val.set_id("acc-val")
        acc.add_opened_change_listener(
            lambda e: acc_val.set_text(str(acc.get_opened_index()))
        )

        # --- Accordion open/close programmatic ---
        btn_acc_open = Button("Open Panel 2")
        btn_acc_open.set_id("btn-acc-open")
        btn_acc_open.add_click_listener(lambda e: acc.open(1))

        btn_acc_close = Button("Close all")
        btn_acc_close.set_id("btn-acc-close")
        btn_acc_close.add_click_listener(lambda e: acc.close())

        # --- Details ---
        det = Details("More info", Span("Hidden content"))
        det.set_id("det1")
        det_val = Span("")
        det_val.set_id("det-val")
        det.add_opened_change_listener(
            lambda e: det_val.set_text(str(det.is_opened()))
        )

        # --- Details set_opened programmatic ---
        btn_det = Button("Open details")
        btn_det.set_id("btn-det-open")
        btn_det.add_click_listener(lambda e: det.set_opened(True))

        # --- Details set_summary_text ---
        det_sum = Details("Old summary", Span("Body"))
        det_sum.set_id("det-sum")
        btn_sum = Button("Change summary")
        btn_sum.set_id("btn-det-sum")
        btn_sum.add_click_listener(lambda e: det_sum.set_summary_text("New summary"))

        self.add(
            tabs1, tabs1_val, btn_tab, btn_add_tab,
            tabs_vert,
            ts, ts_val,
            acc, acc_val, btn_acc_open, btn_acc_close,
            det, det_val, btn_det,
            det_sum, btn_sum,
        )
