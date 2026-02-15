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
