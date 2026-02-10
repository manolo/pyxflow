"""Tests for Theme utility."""

from vaadin.flow.theme import Theme
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.component import UI


class TestThemeConstants:
    """Test theme constants."""

    def test_theme_names(self):
        assert Theme.LUMO == "lumo"
        assert Theme.AURA == "aura"

    def test_variant_names(self):
        assert Theme.LIGHT == "light"
        assert Theme.DARK == "dark"

    def test_theme_css_paths(self):
        assert Theme._THEMES[Theme.LUMO] == "lumo/lumo.css"
        assert Theme._THEMES[Theme.AURA] == "aura/aura.css"


class TestThemeSet:
    """Test Theme.set() generates correct execute commands."""

    def _make_ui(self):
        tree = StateTree()
        return UI(tree), tree

    def test_set_lumo_light(self):
        """Switching to Lumo light should search for aura href and replace."""
        ui, tree = self._make_ui()
        Theme.set(ui, Theme.LUMO)
        cmds = tree.collect_execute()

        assert len(cmds) == 1
        cmd = cmds[0]
        # args: other_href, new_href, theme_attr, js
        assert cmd[0] == "aura/aura.css"  # search for the other theme
        assert cmd[1] == "lumo/lumo.css"  # replace with this
        assert cmd[2] == ""  # light = no theme attr
        assert "setAttribute" in cmd[3] or "removeAttribute" in cmd[3]

    def test_set_aura_dark(self):
        """Switching to Aura dark should search for lumo and set theme=dark."""
        ui, tree = self._make_ui()
        Theme.set(ui, Theme.AURA, Theme.DARK)
        cmds = tree.collect_execute()

        cmd = cmds[0]
        assert cmd[0] == "lumo/lumo.css"
        assert cmd[1] == "aura/aura.css"
        assert cmd[2] == "dark"

    def test_set_lumo_dark(self):
        """Switching to Lumo dark."""
        ui, tree = self._make_ui()
        Theme.set(ui, Theme.LUMO, Theme.DARK)
        cmds = tree.collect_execute()

        cmd = cmds[0]
        assert cmd[0] == "aura/aura.css"
        assert cmd[1] == "lumo/lumo.css"
        assert cmd[2] == "dark"

    def test_set_aura_light(self):
        """Switching to Aura light."""
        ui, tree = self._make_ui()
        Theme.set(ui, Theme.AURA, Theme.LIGHT)
        cmds = tree.collect_execute()

        cmd = cmds[0]
        assert cmd[0] == "lumo/lumo.css"
        assert cmd[1] == "aura/aura.css"
        assert cmd[2] == ""


class TestThemeSetVariant:
    """Test Theme.set_variant() generates correct execute commands."""

    def _make_ui(self):
        tree = StateTree()
        return UI(tree), tree

    def test_set_dark(self):
        """set_variant(DARK) should set theme=dark."""
        ui, tree = self._make_ui()
        Theme.set_variant(ui, Theme.DARK)
        cmds = tree.collect_execute()

        assert len(cmds) == 1
        cmd = cmds[0]
        assert cmd[0] == "dark"
        assert "setAttribute" in cmd[1]

    def test_set_light(self):
        """set_variant(LIGHT) should remove theme attribute."""
        ui, tree = self._make_ui()
        Theme.set_variant(ui, Theme.LIGHT)
        cmds = tree.collect_execute()

        cmd = cmds[0]
        assert cmd[0] == ""
        assert "removeAttribute" in cmd[1]
