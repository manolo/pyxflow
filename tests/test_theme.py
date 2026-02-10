"""Tests for UI.set_theme() and UI.set_theme_variant()."""

from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.component import UI


class TestSetTheme:
    """Test UI.set_theme() generates correct execute commands."""

    def _make_ui(self):
        tree = StateTree()
        return UI(tree), tree

    def test_set_lumo_light(self):
        ui, tree = self._make_ui()
        ui.set_theme("lumo")
        cmd = tree.collect_execute()[0]
        assert cmd[0] == "aura/aura.css"
        assert cmd[1] == "lumo/lumo.css"
        assert cmd[2] == ""

    def test_set_aura_dark(self):
        ui, tree = self._make_ui()
        ui.set_theme("aura", "dark")
        cmd = tree.collect_execute()[0]
        assert cmd[0] == "lumo/lumo.css"
        assert cmd[1] == "aura/aura.css"
        assert cmd[2] == "dark"

    def test_set_lumo_dark(self):
        ui, tree = self._make_ui()
        ui.set_theme("lumo", "dark")
        cmd = tree.collect_execute()[0]
        assert cmd[0] == "aura/aura.css"
        assert cmd[1] == "lumo/lumo.css"
        assert cmd[2] == "dark"

    def test_set_aura_light(self):
        ui, tree = self._make_ui()
        ui.set_theme("aura", "light")
        cmd = tree.collect_execute()[0]
        assert cmd[0] == "lumo/lumo.css"
        assert cmd[1] == "aura/aura.css"
        assert cmd[2] == ""


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
