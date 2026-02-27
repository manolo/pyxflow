"""Test View 32: MasterDetailLayout with navigation -- /test/mdl-nav/:id?"""

from pyflow import Route, BeforeEnterEvent
from pyflow.components import (
    Button, MasterDetailLayout, Span, VerticalLayout,
)
from pyflow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/mdl-nav/:id?", page_title="Test: MDL Nav", layout=TestMainLayout)
@Menu(title="32 MDL Nav", order=32)
class TestMdlNavView(VerticalLayout):
    """MasterDetailLayout with URL-driven detail open/close.

    Routes:
      /test/mdl-nav        -- Grid only, detail hidden
      /test/mdl-nav/new    -- Empty form (detail visible)
      /test/mdl-nav/:id    -- Detail for item :id
    """

    def __init__(self):
        self.set_size_full()

        self._layout = MasterDetailLayout()
        self._layout.set_id("mdl")
        self._layout.set_size_full()
        self._layout.set_detail_size("300px")

        # Status span to track detail state from the outside
        self._status = Span("idle")
        self._status.set_id("mdl-status")

        # Master: list of items + "New" button
        master = VerticalLayout()
        master.set_id("mdl-master")

        new_btn = Button("New")
        new_btn.set_id("mdl-new")
        new_btn.add_theme_name("primary")
        new_btn.add_click_listener(lambda e: self.get_ui().navigate("test/mdl-nav/new"))

        for i in range(1, 4):
            btn = Button(f"Item {i}")
            btn.set_id(f"mdl-sel-{i}")
            def on_click(e, idx=i):
                self._show_detail(str(idx))
                ui = self.get_ui()
                if ui:
                    ui.push_url(f"/test/mdl-nav/{idx}")
            btn.add_click_listener(on_click)
            master.add(btn)

        master.add(new_btn)
        self._layout.set_master(master)

        # Detail: reusable editor panel
        self._detail_panel = VerticalLayout()
        self._detail_panel.set_id("mdl-detail")
        self._detail_label = Span("")
        self._detail_label.set_id("mdl-detail-label")
        self._detail_panel.add(self._detail_label)

        cancel_btn = Button("Cancel")
        cancel_btn.set_id("mdl-cancel")
        cancel_btn.add_click_listener(self._on_cancel)
        self._detail_panel.add(cancel_btn)

        self._layout.add_backdrop_click_listener(self._on_cancel)
        self._layout.add_detail_escape_press_listener(self._on_cancel)

        self.add(self._status, self._layout)

    def before_enter(self, event: BeforeEnterEvent):
        item_id = event.get("id", None)

        if item_id is None:
            # /test/mdl-nav -- hide detail
            self._hide_detail()
            return

        if item_id == "new":
            # /test/mdl-nav/new -- show empty form via navigation (New button path)
            self._show_detail("new")
            return

        # /test/mdl-nav/:id -- show detail for item
        self._show_detail(item_id)

    def _show_detail(self, label: str):
        self._detail_label.set_text(f"Detail: {label}")
        self._layout.set_detail(self._detail_panel)
        self._status.set_text(f"open:{label}")

    def _hide_detail(self):
        self._layout.set_detail(None)
        self._status.set_text("closed")

    def _on_cancel(self, event):
        self._hide_detail()
        ui = self.get_ui()
        if ui:
            ui.navigate("test/mdl-nav")
