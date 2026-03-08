"""Test View 34: execute_js during before_enter -- /test/before-enter-js/:msg?

Verifies that execute_js() called inside before_enter does not cause a resync.
The view uses server-side property updates and execute_js (without component
refs, which aren't available during the initial _create_view path) to prove
that JS commands run before serverConnected.
"""

from pyxflow import Route, BeforeEnterEvent
from pyxflow.components import Button, Span, VerticalLayout
from pyxflow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/before-enter-js/:msg?", page_title="Test: BeforeEnter JS",
       layout=TestMainLayout)
@Menu(title="34 BeforeEnter JS", order=34)
class TestBeforeEnterJsView(VerticalLayout):
    """View that calls execute_js inside before_enter.

    - On each before_enter, increments a counter and calls execute_js to
      set a data attribute on the view element itself.
    - A "Navigate" button re-navigates to the same route with a different
      param, triggering the reenter path.
    """

    def __init__(self):
        self._enter_count = 0

        self._status = Span("count:0")
        self._status.set_id("bej-status")

        self._js_target = Span("no-js-yet")
        self._js_target.set_id("bej-js-target")

        nav_btn = Button("Navigate")
        nav_btn.set_id("bej-navigate")
        nav_btn.add_click_listener(self._on_navigate)

        self.add(self._status, self._js_target, nav_btn)

    def before_enter(self, event: BeforeEnterEvent):
        self._enter_count += 1
        msg = event.get("msg", "default")
        self._status.set_text(f"count:{self._enter_count}")
        self._js_target.set_text(f"py:{msg}")
        # execute_js that sets a data attribute on our own element.
        # On initial navigation this is buffered; on reenter it goes to the tree.
        # Either way it must run BEFORE serverConnected.
        self.execute_js(
            "document.getElementById('bej-js-target').dataset.fromJs = $1",
            f"js:{msg}"
        )

    def _on_navigate(self, event):
        ui = self.get_ui()
        if ui:
            ui.navigate(f"test/before-enter-js/click-{self._enter_count}")
