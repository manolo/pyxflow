"""Test View 30: Server Error Handling — /test/server-errors"""

from datetime import date, datetime

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, DatePicker, DateTimePicker, Span, TextField, VerticalLayout,
)
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/server-errors", page_title="Test: Server Errors", layout=TestMainLayout)
@Menu(title="Server Errors", order=30)
class TestServerErrorsView(VerticalLayout):
    def __init__(self):
        # --- V30.01: Click handler that raises ---
        btn_err = Button("Raise error")
        btn_err.set_id("err-click")

        def _raise_click(e):
            raise RuntimeError("Test error")

        btn_err.add_click_listener(_raise_click)

        # --- V30.02: Value-change handler that raises ---
        tf_err = TextField("Error field")
        tf_err.set_id("err-tf")

        def _raise_change(e):
            raise ValueError("Value change error")

        tf_err.add_value_change_listener(_raise_change)

        # --- V30.03: Healthy button (partial RPC - second RPC succeeds) ---
        healthy_result = Span("")
        healthy_result.set_id("result")
        btn_healthy = Button("Healthy click")
        btn_healthy.set_id("healthy")
        btn_healthy.add_click_listener(lambda e: healthy_result.set_text("ok"))

        # --- V30.06: Date serialization ---
        dp = DatePicker("Date")
        dp.set_id("ser-dp")
        dp.set_value(date(2025, 6, 15))

        dtp = DateTimePicker("DateTime")
        dtp.set_id("ser-dtp")
        dtp.set_value(datetime(2025, 6, 15, 14, 30))

        # --- V30.08: Rapid click counter ---
        self._rapid_count = 0
        rapid_val = Span("0")
        rapid_val.set_id("rapid-count")
        btn_rapid = Button("Rapid click")
        btn_rapid.set_id("rapid")

        def _rapid_click(e):
            self._rapid_count += 1
            rapid_val.set_text(str(self._rapid_count))

        btn_rapid.add_click_listener(_rapid_click)

        # --- All done (last view) ---
        all_done = Span("All UI test views visited")
        all_done.set_id("all-done")

        self.add(
            btn_err,
            tf_err,
            btn_healthy, healthy_result,
            dp, dtp,
            btn_rapid, rapid_val,
            all_done,
        )
