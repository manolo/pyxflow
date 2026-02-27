"""Test View 11: Dialog & ConfirmDialog — /test/dialog"""

from pyflow import Route
from pyflow.components import (
    Button, ConfirmDialog, Dialog, Span, VerticalLayout,
)
from pyflow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/dialog", page_title="Test: Dialog", layout=TestMainLayout)
@Menu(title="12 Dialog", order=12)
class TestDialogView(VerticalLayout):
    def __init__(self):
        # --- Dialog open/close ---
        dlg1 = Dialog()
        dlg1.set_id("dlg1")
        dlg1.add(Span("Hello"))
        btn_open = Button("Open dialog")
        btn_open.set_id("btn-open")
        btn_open.add_click_listener(lambda e: dlg1.open())

        # --- Dialog header_title ---
        dlg_title = Dialog()
        dlg_title.set_id("dlg-title")
        dlg_title.set_header_title("My Dialog")
        dlg_title.add(Span("Content"))
        btn_title = Button("Open titled")
        btn_title.set_id("btn-title")
        btn_title.add_click_listener(lambda e: dlg_title.open())

        # --- Dialog header/footer ---
        dlg_hf = Dialog()
        dlg_hf.set_id("dlg-hf")
        dlg_hf.add(Span("Body"))
        btn_close_hf = Button("Close")
        btn_close_hf.add_click_listener(lambda e: dlg_hf.close())
        dlg_hf.get_header().add(Span("Header"))
        dlg_hf.get_footer().add(btn_close_hf)
        btn_hf = Button("Open header/footer")
        btn_hf.set_id("btn-hf")
        btn_hf.add_click_listener(lambda e: dlg_hf.open())

        # --- Dialog set_draggable ---
        dlg_drag = Dialog()
        dlg_drag.set_id("dlg-drag")
        dlg_drag.set_draggable(True)
        dlg_drag.set_header_title("Draggable")
        dlg_drag.add(Span("Drag me"))
        btn_drag = Button("Open draggable")
        btn_drag.set_id("btn-drag")
        btn_drag.add_click_listener(lambda e: dlg_drag.open())

        # --- Dialog set_resizable ---
        dlg_resize = Dialog()
        dlg_resize.set_id("dlg-resize")
        dlg_resize.set_resizable(True)
        dlg_resize.add(Span("Resize me"))
        btn_resize = Button("Open resizable")
        btn_resize.set_id("btn-resize")
        btn_resize.add_click_listener(lambda e: dlg_resize.open())

        # --- Dialog set_width/set_height ---
        dlg_size = Dialog()
        dlg_size.set_id("dlg-size")
        dlg_size.set_width("600px")
        dlg_size.set_height("400px")
        dlg_size.add(Span("Sized"))
        btn_size = Button("Open sized")
        btn_size.set_id("btn-size")
        btn_size.add_click_listener(lambda e: dlg_size.open())

        # --- Dialog min/max width/height ---
        dlg_minmax = Dialog()
        dlg_minmax.set_id("dlg-minmax")
        dlg_minmax.set_min_width("300px")
        dlg_minmax.set_max_width("800px")
        dlg_minmax.set_min_height("200px")
        dlg_minmax.set_max_height("600px")
        dlg_minmax.add(Span("MinMax"))
        btn_minmax = Button("Open minmax")
        btn_minmax.set_id("btn-minmax")
        btn_minmax.add_click_listener(lambda e: dlg_minmax.open())

        # --- Dialog close listener ---
        dlg_cls_val = Span("")
        dlg_cls_val.set_id("dlg-closed")
        dlg_cls = Dialog()
        dlg_cls.set_id("dlg-cls")
        dlg_cls.add(Span("Close me"))
        dlg_cls.add_close_listener(lambda e: dlg_cls_val.set_text("closed"))
        btn_cls = Button("Open closeable")
        btn_cls.set_id("btn-cls")
        btn_cls.add_click_listener(lambda e: dlg_cls.open())

        # --- Dialog resize listener ---
        dlg_resize_val = Span("")
        dlg_resize_val.set_id("dlg-resize-val")
        dlg_resize_listen = Dialog()
        dlg_resize_listen.set_id("dlg-resize-listen")
        dlg_resize_listen.set_resizable(True)
        dlg_resize_listen.set_header_title("Resize me")
        dlg_resize_listen.add(Span("Drag the edges"))
        dlg_resize_listen.add_resize_listener(
            lambda e: dlg_resize_val.set_text("resized")
        )
        btn_resize_listen = Button("Open resize listener")
        btn_resize_listen.set_id("btn-resize-listen")
        btn_resize_listen.add_click_listener(lambda e: dlg_resize_listen.open())

        # --- ConfirmDialog basic ---
        cd_result = Span("")
        cd_result.set_id("cd-result")

        cd1 = ConfirmDialog("Delete?", "Are you sure?", "Yes")
        cd1.set_id("cd1")
        cd1.add_confirm_listener(lambda e: cd_result.set_text("confirmed"))

        btn_cd = Button("Open confirm")
        btn_cd.set_id("btn-cd")
        btn_cd.add_click_listener(lambda e: cd1.open())

        # --- ConfirmDialog with cancel ---
        cd_cancel = ConfirmDialog("Action?", "Proceed?", "OK")
        cd_cancel.set_id("cd-cancel")
        cd_cancel.set_cancelable(True)
        cd_cancel.set_cancel_text("No")
        cd_cancel_result = Span("")
        cd_cancel_result.set_id("cd-cancel-result")
        cd_cancel.add_confirm_listener(lambda e: cd_cancel_result.set_text("confirmed"))
        cd_cancel.add_cancel_listener(lambda e: cd_cancel_result.set_text("cancelled"))
        btn_cd_cancel = Button("Open cancel dialog")
        btn_cd_cancel.set_id("btn-cd-cancel")
        btn_cd_cancel.add_click_listener(lambda e: cd_cancel.open())

        # --- ConfirmDialog with reject ---
        cd_reject = ConfirmDialog("Delete?", "This is permanent.", "Delete")
        cd_reject.set_id("cd-reject")
        cd_reject.set_rejectable(True)
        cd_reject.set_reject_text("Never")
        cd_reject.set_confirm_button_theme("primary error")
        cd_reject.set_reject_button_theme("error tertiary")
        cd_reject_result = Span("")
        cd_reject_result.set_id("cd-reject-result")
        cd_reject.add_confirm_listener(lambda e: cd_reject_result.set_text("confirmed"))
        cd_reject.add_reject_listener(lambda e: cd_reject_result.set_text("rejected"))
        btn_cd_reject = Button("Open reject dialog")
        btn_cd_reject.set_id("btn-cd-reject")
        btn_cd_reject.add_click_listener(lambda e: cd_reject.open())

        # --- ConfirmDialog reopen ---
        cd_reopen = ConfirmDialog("Reopen test", "Can reopen?", "OK")
        cd_reopen.set_id("cd-reopen")
        cd_reopen_count = Span("0")
        cd_reopen_count.set_id("cd-reopen-count")
        self._reopen_n = 0

        def _on_reopen_confirm(e):
            self._reopen_n += 1
            cd_reopen_count.set_text(str(self._reopen_n))

        cd_reopen.add_confirm_listener(_on_reopen_confirm)
        btn_cd_reopen = Button("Open reopen dialog")
        btn_cd_reopen.set_id("btn-cd-reopen")
        btn_cd_reopen.add_click_listener(lambda e: cd_reopen.open())

        self.add(
            btn_open, dlg1,
            btn_title, dlg_title,
            btn_hf, dlg_hf,
            btn_drag, dlg_drag,
            btn_resize, dlg_resize,
            btn_size, dlg_size,
            btn_cls, dlg_cls, dlg_cls_val,
            btn_resize_listen, dlg_resize_listen, dlg_resize_val,
            btn_cd, cd1, cd_result,
            btn_cd_cancel, cd_cancel, cd_cancel_result,
            btn_cd_reject, cd_reject, cd_reject_result,
            btn_minmax, dlg_minmax,
            btn_cd_reopen, cd_reopen, cd_reopen_count,
        )
