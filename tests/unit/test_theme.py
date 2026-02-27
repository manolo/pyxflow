"""Tests for UI.set_theme(), UI.set_theme_variant(), and UI singleton lifecycle."""

import pytest

from pyflow.core.state_tree import StateTree
from pyflow.core.component import UI
from pyflow.server.uidl_handler import UidlHandler
from pyflow.router import Route, clear_routes
from pyflow.components import VerticalLayout, Span


class TestSetTheme:
    """Test UI.set_theme() generates correct execute commands."""

    def _make_ui(self):
        tree = StateTree()
        return UI(tree), tree

    def test_set_lumo_light(self):
        ui, tree = self._make_ui()
        ui.set_theme("lumo")
        cmd = tree.collect_execute()[0]
        assert cmd[0] == "aura/aura.css"  # other
        assert cmd[1] == "lumo/lumo.css"  # new
        assert cmd[2] == ""               # is_dark
        assert cmd[3] == "1"              # is_lumo

    def test_set_lumo_dark(self):
        ui, tree = self._make_ui()
        ui.set_theme("lumo", "dark")
        cmd = tree.collect_execute()[0]
        assert cmd[0] == "aura/aura.css"
        assert cmd[1] == "lumo/lumo.css"
        assert cmd[2] == "1"              # is_dark
        assert cmd[3] == "1"              # is_lumo
        assert "setAttribute" in cmd[4]

    def test_set_aura_light(self):
        ui, tree = self._make_ui()
        ui.set_theme("aura", "light")
        cmd = tree.collect_execute()[0]
        assert cmd[0] == "lumo/lumo.css"
        assert cmd[1] == "aura/aura.css"
        assert cmd[2] == ""               # is_dark
        assert cmd[3] == ""               # is_lumo (aura)
        assert "colorScheme" in cmd[4]

    def test_set_aura_dark(self):
        ui, tree = self._make_ui()
        ui.set_theme("aura", "dark")
        cmd = tree.collect_execute()[0]
        assert cmd[0] == "lumo/lumo.css"
        assert cmd[1] == "aura/aura.css"
        assert cmd[2] == "1"              # is_dark
        assert cmd[3] == ""               # is_lumo (aura)
        assert "colorScheme" in cmd[4]

    def test_lumo_clears_color_scheme(self):
        """Switching to Lumo should reset color-scheme and use theme attr."""
        ui, tree = self._make_ui()
        ui.set_theme("lumo", "dark")
        cmd = tree.collect_execute()[0]
        js = cmd[4]
        assert "colorScheme = ''" in js
        assert "setAttribute" in js

    def test_aura_clears_theme_attr(self):
        """Switching to Aura should remove theme attr and use color-scheme."""
        ui, tree = self._make_ui()
        ui.set_theme("aura", "dark")
        cmd = tree.collect_execute()[0]
        js = cmd[4]
        assert "removeAttribute('theme')" in js
        assert "colorScheme" in js


class TestSetThemeVariant:
    """Test UI.set_theme_variant() generates correct execute commands."""

    def _make_ui(self):
        tree = StateTree()
        return UI(tree), tree

    def test_set_dark(self):
        ui, tree = self._make_ui()
        ui.set_theme_variant("dark")
        cmd = tree.collect_execute()[0]
        assert cmd[0] == "dark"
        assert "setAttribute" in cmd[1]

    def test_set_light(self):
        ui, tree = self._make_ui()
        ui.set_theme_variant("light")
        cmd = tree.collect_execute()[0]
        assert cmd[0] == ""
        assert "removeAttribute" in cmd[1]


class TestGetTheme:
    """Test UI.get_theme() and UI.get_theme_variant()."""

    @pytest.fixture(autouse=True)
    def _clear_shell(self):
        from pyflow.router import clear_app_shell
        clear_app_shell()
        yield
        clear_app_shell()

    def _make_ui(self):
        tree = StateTree()
        return UI(tree), tree

    def test_defaults(self):
        ui, _ = self._make_ui()
        assert ui.get_theme() == "lumo"
        assert ui.get_theme_variant() == "light"

    def test_after_set_theme_aura_dark(self):
        ui, _ = self._make_ui()
        ui.set_theme("aura", "dark")
        assert ui.get_theme() == "aura"
        assert ui.get_theme_variant() == "dark"

    def test_after_set_theme_lumo_dark(self):
        ui, _ = self._make_ui()
        ui.set_theme("lumo", "dark")
        assert ui.get_theme() == "lumo"
        assert ui.get_theme_variant() == "dark"

    def test_after_set_theme_variant(self):
        ui, _ = self._make_ui()
        ui.set_theme_variant("dark")
        assert ui.get_theme() == "lumo"  # theme unchanged
        assert ui.get_theme_variant() == "dark"

    def test_roundtrip(self):
        ui, _ = self._make_ui()
        ui.set_theme("aura", "dark")
        ui.set_theme("lumo", "light")
        assert ui.get_theme() == "lumo"
        assert ui.get_theme_variant() == "light"

    def test_set_color_scheme_dark(self):
        ui, _ = self._make_ui()
        ui.set_color_scheme("dark")
        assert ui.get_theme_variant() == "dark"

    def test_set_color_scheme_light(self):
        ui, _ = self._make_ui()
        ui.set_color_scheme("dark")
        ui.set_color_scheme("light")
        assert ui.get_theme_variant() == "light"

    def test_set_empty_theme_ignored(self):
        ui, _ = self._make_ui()
        ui.set_theme("aura", "dark")
        ui.set_theme("")  # no-op
        assert ui.get_theme() == "aura"
        assert ui.get_theme_variant() == "dark"

    def test_color_scheme_initializes_variant(self):
        """UI should read @ColorScheme from AppShell on creation."""
        from pyflow.router import AppShell, clear_app_shell
        try:
            @AppShell
            class TestShell:
                pass
            TestShell._color_scheme = "dark"
            ui, _ = self._make_ui()
            assert ui.get_theme_variant() == "dark"
        finally:
            clear_app_shell()


class TestUISingletonPerSession:
    """Test that UI is a singleton per session (like Java Flow)."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        yield
        clear_routes()

    def _make_session(self):
        tree = StateTree()
        handler = UidlHandler(tree)
        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return handler, tree, csrf

    def _navigate(self, handler, csrf, route, sync_id=0, client_id=0):
        payload = {
            "csrfToken": csrf,
            "rpc": [{"type": "event", "node": 1, "event": "ui-navigate",
                      "data": {"route": route, "query": "", "appShellTitle": "",
                               "historyState": {"idx": 0}, "trigger": ""}}],
            "syncId": sync_id, "clientId": client_id,
        }
        return handler.handle_uidl(payload)

    def test_handler_has_ui(self):
        """UidlHandler should create a UI on init."""
        handler, _, _ = self._make_session()
        assert handler._ui is not None
        assert isinstance(handler._ui, UI)

    def test_ui_same_across_navigations(self):
        """Same UI instance should be reused across navigations."""
        @Route("v1")
        class V1(VerticalLayout):
            pass

        @Route("v2")
        class V2(VerticalLayout):
            pass

        handler, _, csrf = self._make_session()
        ui_before = handler._ui

        self._navigate(handler, csrf, "v1")
        assert handler._ui is ui_before

        r1 = handler.handle_uidl({
            "csrfToken": csrf, "rpc": [], "syncId": 1, "clientId": 1,
        })
        self._navigate(handler, csrf, "v2", sync_id=r1["syncId"], client_id=2)
        assert handler._ui is ui_before

    def test_theme_persists_across_navigations(self):
        """Theme set on one view should persist when navigating to another."""
        captured_themes = []

        @Route("t1")
        class T1(VerticalLayout):
            def _attach(self, tree):
                super()._attach(tree)
                ui = self.get_ui()
                captured_themes.append(f"{ui.get_theme()}-{ui.get_theme_variant()}")

        @Route("t2")
        class T2(VerticalLayout):
            def _attach(self, tree):
                super()._attach(tree)
                ui = self.get_ui()
                captured_themes.append(f"{ui.get_theme()}-{ui.get_theme_variant()}")

        handler, _, csrf = self._make_session()

        # Navigate to t1 — default theme
        r1 = self._navigate(handler, csrf, "t1")
        assert captured_themes[-1] == "lumo-light"

        # Change theme
        handler._ui.set_theme("aura", "dark")

        # Navigate to t2 — should see aura-dark
        self._navigate(handler, csrf, "t2", sync_id=r1["syncId"], client_id=1)
        assert captured_themes[-1] == "aura-dark"

    def test_view_get_ui_returns_session_ui(self):
        """Views should get the same UI instance as the handler."""
        captured_ui = []

        @Route("u1")
        class U1(VerticalLayout):
            def _attach(self, tree):
                super()._attach(tree)
                captured_ui.append(self.get_ui())

        handler, _, csrf = self._make_session()
        self._navigate(handler, csrf, "u1")
        assert captured_ui[0] is handler._ui
