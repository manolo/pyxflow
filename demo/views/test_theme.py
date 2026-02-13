"""Test View 25: Theme Switching & Styles — /test/theme"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, RouterLink, Span, VerticalLayout,
)


@Route("test/theme", page_title="Test: Theme")
class TestThemeView(VerticalLayout):
    def __init__(self):
        theme_status = Span("light")
        theme_status.set_id("theme-status")

        # --- Switch to dark ---
        btn_dark = Button("Dark mode")
        btn_dark.set_id("btn-dark")

        def _set_dark(e):
            ui = self.get_ui()
            if ui:
                ui.set_theme_variant("dark")
                theme_status.set_text("dark")

        btn_dark.add_click_listener(_set_dark)

        # --- Switch to light ---
        btn_light = Button("Light mode")
        btn_light.set_id("btn-light")

        def _set_light(e):
            ui = self.get_ui()
            if ui:
                ui.set_theme_variant("light")
                theme_status.set_text("light")

        btn_light.add_click_listener(_set_light)

        # --- Switch to Aura ---
        btn_aura = Button("Aura theme")
        btn_aura.set_id("btn-aura")

        def _set_aura(e):
            ui = self.get_ui()
            if ui:
                ui.set_theme("aura", "light")
                theme_status.set_text("aura-light")

        btn_aura.add_click_listener(_set_aura)

        # --- Switch to Aura dark ---
        btn_aura_dark = Button("Aura dark")
        btn_aura_dark.set_id("btn-aura-dark")

        def _set_aura_dark(e):
            ui = self.get_ui()
            if ui:
                ui.set_theme("aura", "dark")
                theme_status.set_text("aura-dark")

        btn_aura_dark.add_click_listener(_set_aura_dark)

        # --- CSS class for style test ---
        styled_btn = Button("Custom styled")
        styled_btn.set_id("styled-btn")
        styled_btn.add_class_name("custom-btn")

        # --- Nav link ---
        nav_link = RouterLink("Next: ClientCallable", "test/client-callable")
        nav_link.set_id("nav-next")

        self.add(
            theme_status,
            btn_dark, btn_light,
            btn_aura, btn_aura_dark,
            styled_btn,
            nav_link,
        )
