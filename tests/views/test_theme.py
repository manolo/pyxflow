"""Test View 25: Theme Switching & Styles — /test/theme"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, Span, VerticalLayout,
)
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/theme", page_title="Test: Theme", layout=TestMainLayout)
@Menu(title="Theme", order=25)
class TestThemeView(VerticalLayout):
    def __init__(self):
        theme_status = Span()
        theme_status.set_id("theme-status")

        def _update_status():
            ui = self.get_ui()
            if ui:
                t, v = ui.get_theme(), ui.get_theme_variant()
                theme_status.set_text(f"{t}-{v}")

        # Show initial theme on attach
        self._update_status = _update_status

        # --- Switch to dark ---
        btn_dark = Button("Dark mode")
        btn_dark.set_id("btn-dark")

        def _set_dark(e):
            ui = self.get_ui()
            if ui:
                ui.set_theme_variant("dark")
                _update_status()

        btn_dark.add_click_listener(_set_dark)

        # --- Switch to light ---
        btn_light = Button("Light mode")
        btn_light.set_id("btn-light")

        def _set_light(e):
            ui = self.get_ui()
            if ui:
                ui.set_theme_variant("light")
                _update_status()

        btn_light.add_click_listener(_set_light)

        # --- Switch to Aura ---
        btn_aura = Button("Aura theme")
        btn_aura.set_id("btn-aura")

        def _set_aura(e):
            ui = self.get_ui()
            if ui:
                ui.set_theme("aura", "light")
                _update_status()

        btn_aura.add_click_listener(_set_aura)

        # --- Switch to Aura dark ---
        btn_aura_dark = Button("Aura dark")
        btn_aura_dark.set_id("btn-aura-dark")

        def _set_aura_dark(e):
            ui = self.get_ui()
            if ui:
                ui.set_theme("aura", "dark")
                _update_status()

        btn_aura_dark.add_click_listener(_set_aura_dark)

        # --- Reset to initial theme ---
        btn_reset = Button("Reset theme")
        btn_reset.set_id("btn-reset")

        def _reset(e):
            ui = self.get_ui()
            if ui:
                ui.set_theme(self._initial_theme, self._initial_variant)
                _update_status()

        btn_reset.add_click_listener(_reset)

        # --- CSS class for style test ---
        styled_btn = Button("Custom styled")
        styled_btn.set_id("styled-btn")
        styled_btn.add_class_name("custom-btn")

        self.add(
            theme_status,
            btn_dark, btn_light,
            btn_aura, btn_aura_dark,
            btn_reset, styled_btn,
        )

    def _attach(self, tree):
        super()._attach(tree)
        ui = self.get_ui()
        if ui:
            self._initial_theme = ui.get_theme()
            self._initial_variant = ui.get_theme_variant()
            self._update_status()
