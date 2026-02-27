"""Test View 26: @ClientCallable — /test/client-callable"""

from pyflow import Route
from pyflow.components import (
    Button, ClientCallable, Span, VerticalLayout,
)
from pyflow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/client-callable", page_title="Test: ClientCallable", layout=TestMainLayout)
@Menu(title="26 ClientCallable", order=26)
class TestClientCallableView(VerticalLayout):
    def __init__(self):
        self._result = Span("")
        self._result.set_id("cc-result")

        # --- Button triggers JS call to server ---
        btn_greet = Button("Greet")
        btn_greet.set_id("btn-greet")
        btn_greet.add_click_listener(
            lambda e: self.execute_js("$0.$server.greet('World')")
        )

        # --- No-args call ---
        btn_ping = Button("Ping")
        btn_ping.set_id("btn-ping")
        btn_ping.add_click_listener(
            lambda e: self.execute_js("$0.$server.ping()")
        )

        self.add(self._result, btn_greet, btn_ping)

    @ClientCallable
    def greet(self, name):
        self._result.set_text(f"Hello {name}")

    @ClientCallable
    def ping(self):
        self._result.set_text("pong")
