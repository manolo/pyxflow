"""Test View 7: DatePicker, TimePicker, DateTimePicker — /test/date-time"""

from datetime import date, time, datetime

from pyflow import Route
from pyflow.components import (
    Button, DatePicker, DateTimePicker, Span, TimePicker,
    VerticalLayout,
)
from pyflow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/date-time", page_title="Test: Date & Time", layout=TestMainLayout)
@Menu(title="07 Date & Time", order=7)
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

        # --- DatePicker value roundtrip (mSync regression) ---
        dp_round = DatePicker("Roundtrip")
        dp_round.set_id("dp-round")
        dp_round_val = Span("")
        dp_round_val.set_id("dp-round-val")
        dp_round.add_value_change_listener(
            lambda e: dp_round_val.set_text(str(e.get("value", "")))
        )

        # --- DatePicker calendar pick ---
        dp_pick = DatePicker("Calendar pick")
        dp_pick.set_id("dp-pick")
        dp_pick_val = Span("")
        dp_pick_val.set_id("dp-pick-val")
        dp_pick.add_value_change_listener(
            lambda e: dp_pick_val.set_text(str(e.get("value", "")))
        )

        # --- DatePicker auto-open disabled ---
        dp_noauto = DatePicker("No auto-open")
        dp_noauto.set_id("dp-noauto")
        dp_noauto.set_auto_open(False)

        # --- DatePicker required ---
        dp_req = DatePicker("Required")
        dp_req.set_id("dp-req")
        dp_req.set_required_indicator_visible(True)

        # --- TimePicker value roundtrip (mSync regression) ---
        tp_round = TimePicker("Roundtrip")
        tp_round.set_id("tp-round")
        tp_round_val = Span("")
        tp_round_val.set_id("tp-round-val")
        tp_round.add_value_change_listener(
            lambda e: tp_round_val.set_text(str(e.get("value", "")))
        )

        # --- TimePicker min/max ---
        tp_range = TimePicker("Range")
        tp_range.set_id("tp-range")
        tp_range.set_min(time(9, 0))
        tp_range.set_max(time(17, 0))

        # --- DateTimePicker value roundtrip (mSync regression) ---
        dtp_round = DateTimePicker("Roundtrip")
        dtp_round.set_id("dtp-round")
        dtp_round_val = Span("")
        dtp_round_val.set_id("dtp-round-val")
        dtp_round.add_value_change_listener(
            lambda e: dtp_round_val.set_text(str(e.get("value", "")))
        )

        # --- DateTimePicker step ---
        dtp_step = DateTimePicker("Step")
        dtp_step.set_id("dtp-step")
        dtp_step.set_step(3600)

        # --- DateTimePicker required ---
        dtp_req = DateTimePicker("Required")
        dtp_req.set_id("dtp-req")
        dtp_req.set_required_indicator_visible(True)

        # --- DateTimePicker min/max ---
        dtp_range = DateTimePicker("Range")
        dtp_range.set_id("dtp-range")
        dtp_range.set_min(datetime(2025, 1, 1, 0, 0))
        dtp_range.set_max(datetime(2025, 12, 31, 23, 59))

        self.add(
            dp1, dp1_val,
            dp_pre,
            dp_clear,
            dp_range,
            dp_weeks,
            dp_init,
            dp_round, dp_round_val,
            dp_pick, dp_pick_val,
            dp_noauto,
            dp_req,
            tp1, tp1_val,
            tp_pre,
            tp_step,
            tp_clear,
            tp_round, tp_round_val,
            tp_range,
            dtp1, dtp1_val,
            dtp_pre,
            dtp_ph,
            dtp_round, dtp_round_val,
            dtp_step,
            dtp_req,
            dtp_range,
        )
