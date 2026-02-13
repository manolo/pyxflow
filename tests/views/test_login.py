"""Test View 29: LoginForm & LoginOverlay — /test/login"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, LoginForm, LoginOverlay, Span, VerticalLayout,
)
from vaadin.flow.menu import Menu
from demo.views.test_main_layout import TestMainLayout


@Route("test/login", page_title="Test: Login", layout=TestMainLayout)
@Menu(title="Login", order=29)
class TestLoginView(VerticalLayout):
    def __init__(self):
        # --- LoginForm ---
        lf_result = Span("")
        lf_result.set_id("lf-result")

        lf = LoginForm()
        lf.set_id("lf1")
        lf.add_login_listener(
            lambda e: lf_result.set_text(
                f"{e.get('username', '')}:{e.get('password', '')}"
            )
        )

        # --- LoginForm forgot password ---
        lf_forgot = Span("")
        lf_forgot.set_id("lf-forgot")
        lf.add_forgot_password_listener(
            lambda e: lf_forgot.set_text("forgot")
        )

        # --- LoginOverlay ---
        lo = LoginOverlay()
        lo.set_id("lo1")
        lo.set_title("Test App")
        lo.set_description("Enter credentials")

        lo_result = Span("")
        lo_result.set_id("lo-result")
        lo.add_login_listener(
            lambda e: lo_result.set_text(
                f"{e.get('username', '')}:{e.get('password', '')}"
            )
        )

        btn_lo = Button("Open login overlay")
        btn_lo.set_id("btn-lo")
        btn_lo.add_click_listener(lambda e: lo.open())

        btn_lo_close = Button("Close login overlay")
        btn_lo_close.set_id("btn-lo-close")
        btn_lo_close.add_click_listener(lambda e: lo.close())

        # --- All done ---
        all_done = Span("All UI test views visited")
        all_done.set_id("all-done")

        # --- No nav link (last view) ---
        self.add(
            lf, lf_result, lf_forgot,
            btn_lo, lo, lo_result, btn_lo_close,
            all_done,
        )
