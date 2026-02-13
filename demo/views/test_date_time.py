"""Test View 7: DatePicker, TimePicker, DateTimePicker — /test/date-time"""

from datetime import date, time, datetime

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, DatePicker, DateTimePicker, RouterLink, Span, TimePicker,
    VerticalLayout,
)


@Route("test/date-time", page_title="Test: Date & Time")
class TestDateTimeView(VerticalLayout):
    def __init__(self):
        # --- DatePicker renders with label ---
        dp1 = DatePicker("Birthday")
        dp1.set_id("dp1")
        dp1_val = Span("")
        dp1_val.set_id("dp1-val")
        dp1.add_value_change_listener(
            lambda e: dp1_val.set_text(str(e.get("value", "")))
        )

        # --- DatePicker set_value programmatic ---
        dp_pre = DatePicker("Preset")
        dp_pre.set_id("dp-pre")
        dp_pre.set_value(date(2025, 6, 15))

        # --- DatePicker clear button ---
        dp_clear = DatePicker("Clearable")
        dp_clear.set_id("dp-clear")
        dp_clear.set_value(date(2025, 1, 1))
        dp_clear.set_clear_button_visible(True)

        # --- DatePicker min/max ---
        dp_range = DatePicker("Range")
        dp_range.set_id("dp-range")
        dp_range.set_min(date(2025, 1, 1))
        dp_range.set_max(date(2025, 12, 31))

        # --- TimePicker renders with label ---
        tp1 = TimePicker("Meeting time")
        tp1.set_id("tp1")
        tp1_val = Span("")
        tp1_val.set_id("tp1-val")
        tp1.add_value_change_listener(
            lambda e: tp1_val.set_text(str(e.get("value", "")))
        )

        # --- TimePicker set_value programmatic ---
        tp_pre = TimePicker("Preset")
        tp_pre.set_id("tp-pre")
        tp_pre.set_value(time(14, 30))

        # --- TimePicker set_step ---
        tp_step = TimePicker("30-min step")
        tp_step.set_id("tp-step")
        tp_step.set_step(1800)

        # --- TimePicker clear button ---
        tp_clear = TimePicker("Clearable")
        tp_clear.set_id("tp-clear")
        tp_clear.set_value(time(9, 0))
        tp_clear.set_clear_button_visible(True)

        # --- DateTimePicker renders ---
        dtp1 = DateTimePicker("Event")
        dtp1.set_id("dtp1")
        dtp1_val = Span("")
        dtp1_val.set_id("dtp1-val")
        dtp1.add_value_change_listener(
            lambda e: dtp1_val.set_text(str(e.get("value", "")))
        )

        # --- DateTimePicker set_value programmatic ---
        dtp_pre = DateTimePicker("Preset")
        dtp_pre.set_id("dtp-pre")
        dtp_pre.set_value(datetime(2025, 6, 15, 14, 30))

        # --- DateTimePicker placeholders ---
        dtp_ph = DateTimePicker("With placeholders")
        dtp_ph.set_id("dtp-ph")
        dtp_ph.set_date_placeholder("Pick date")
        dtp_ph.set_time_placeholder("Pick time")

        # --- DatePicker week numbers ---
        dp_weeks = DatePicker("Week numbers")
        dp_weeks.set_id("dp-weeks")
        dp_weeks.set_week_numbers_visible(True)

        # --- DatePicker initial position ---
        dp_init = DatePicker("Initial position")
        dp_init.set_id("dp-init")
        dp_init.set_initial_position(date(2026, 6, 1))

        # --- Nav link ---
        nav_link = RouterLink("Next: Grid Basic", "test/grid-basic")
        nav_link.set_id("nav-next")

        self.add(
            dp1, dp1_val,
            dp_pre,
            dp_clear,
            dp_range,
            dp_weeks,
            dp_init,
            tp1, tp1_val,
            tp_pre,
            tp_step,
            tp_clear,
            dtp1, dtp1_val,
            dtp_pre,
            dtp_ph,
            nav_link,
        )
