"""Test View 26: @ClientCallable — /test/client-callable"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, ClientCallable, RouterLink, Span, VerticalLayout,
)


@Route("test/client-callable", page_title="Test: ClientCallable")
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

        # --- Nav link ---
        nav_link = RouterLink("Next: CustomField", "test/custom-field")
        nav_link.set_id("nav-next")

        self.add(self._result, btn_greet, btn_ping, nav_link)

    @ClientCallable
    def greet(self, name):
        self._result.set_text(f"Hello {name}")

    @ClientCallable
    def ping(self):
        self._result.set_text("pong")
