"""Test View 12: Notification & Popover — /test/notification-popover"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, Notification, NotificationVariant, Popover, PopoverPosition,
    Span, VerticalLayout,
)
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/notification-popover", page_title="Test: Notification & Popover", layout=TestMainLayout)
@Menu(title="11 Notification & Popover", order=11)
class TestNotificationPopoverView(VerticalLayout):
    def __init__(self):
        # --- Notification.show static ---
        btn_show = Button("Show notification")
        btn_show.set_id("btn-notif-show")
        btn_show.add_click_listener(
            lambda e: Notification.show("Saved!", 1000)
        )

        # --- Notification with position ---
        btn_pos = Button("Top center")
        btn_pos.set_id("btn-notif-pos")
        btn_pos.add_click_listener(
            lambda e: Notification.show(
                "Top center!", 1000, position=Notification.Position.TOP_CENTER
            )
        )

        # --- Notification with theme ---
        btn_theme = Button("Success notification")
        btn_theme.set_id("btn-notif-theme")

        def _show_success(e):
            n = Notification("Success!", 1000)
            n.add_theme_variants(NotificationVariant.LUMO_SUCCESS)
            n.open()

        btn_theme.add_click_listener(_show_success)

        # --- Notification close programmatic ---
        notif_perm = Notification("Permanent", 0)
        notif_perm.set_id("notif-perm")
        btn_notif_open = Button("Open permanent")
        btn_notif_open.set_id("btn-notif-open")
        btn_notif_open.add_click_listener(lambda e: notif_perm.open())
        btn_notif_close = Button("Close permanent")
        btn_notif_close.set_id("btn-notif-close")
        btn_notif_close.add_click_listener(lambda e: notif_perm.close())

        # --- Notification close listener ---
        notif_cls_val = Span("")
        notif_cls_val.set_id("notif-closed")
        notif_cls = Notification("Will close", 500)
        notif_cls.add_close_listener(lambda e: notif_cls_val.set_text("closed"))
        btn_notif_cls = Button("Open with close listener")
        btn_notif_cls.set_id("btn-notif-cls")
        btn_notif_cls.add_click_listener(lambda e: notif_cls.open())

        # --- Popover with target ---
        pop_target = Button("Popover target")
        pop_target.set_id("pop-target")
        pop1 = Popover()
        pop1.set_id("pop1")
        pop1.set_target(pop_target)
        pop1.add(Span("Pop content"))

        # --- Popover open/close programmatic ---
        pop_prog = Popover()
        pop_prog.set_id("pop-prog")
        pop_prog_target = Button("Prog target")
        pop_prog_target.set_id("pop-prog-target")
        pop_prog.set_target(pop_prog_target)
        pop_prog.add(Span("Programmatic"))
        btn_pop_open = Button("Open popover")
        btn_pop_open.set_id("btn-pop-open")
        btn_pop_open.add_click_listener(lambda e: pop_prog.open())
        btn_pop_close = Button("Close popover")
        btn_pop_close.set_id("btn-pop-close")
        btn_pop_close.add_click_listener(lambda e: pop_prog.close())

        # --- Popover set_position ---
        pop_pos = Popover()
        pop_pos.set_id("pop-pos")
        pop_pos_target = Button("Position target")
        pop_pos_target.set_id("pop-pos-target")
        pop_pos.set_target(pop_pos_target)
        pop_pos.set_position(PopoverPosition.TOP)
        pop_pos.add(Span("Top position"))

        # --- Popover listeners ---
        pop_ev_val = Span("")
        pop_ev_val.set_id("pop-ev")
        pop_ev = Popover()
        pop_ev.set_id("pop-ev")
        pop_ev_target = Button("Event target")
        pop_ev_target.set_id("pop-ev-target")
        pop_ev.set_target(pop_ev_target)
        pop_ev.add(Span("Events"))
        pop_ev.add_open_listener(lambda e: pop_ev_val.set_text("opened"))
        pop_ev.add_close_listener(lambda e: pop_ev_val.set_text("closed"))

        self.add(
            btn_show,
            btn_pos,
            btn_theme,
            btn_notif_open, btn_notif_close, notif_perm,
            btn_notif_cls, notif_cls, notif_cls_val,
            pop_target, pop1,
            pop_prog_target, pop_prog, btn_pop_open, btn_pop_close,
            pop_pos_target, pop_pos,
            pop_ev_target, pop_ev, pop_ev_val,
        )
