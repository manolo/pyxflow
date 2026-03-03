"""Tests for @ColorScheme decorator and HTML/runtime color scheme support."""

import pytest

from pyxflow.router import ColorScheme, AppShell, clear_app_shell
from pyxflow.server.http_server import get_index_html
from pyxflow.core.state_tree import StateTree
from pyxflow.core.component import UI


class TestColorSchemeDecorator:
    """Test @ColorScheme decorator."""

    def test_dark(self):
        """@ColorScheme('dark') should set _color_scheme='dark'."""
        @ColorScheme("dark")
        class MyShell:
            pass

        assert MyShell._color_scheme == "dark"

    def test_light(self):
        """@ColorScheme('light') should set _color_scheme='light'."""
        @ColorScheme("light")
        class MyShell:
            pass

        assert MyShell._color_scheme == "light"

    def test_light_dark(self):
        """@ColorScheme('light dark') should set _color_scheme='light dark'."""
        @ColorScheme("light dark")
        class MyShell:
            pass

        assert MyShell._color_scheme == "light dark"

    def test_dark_light(self):
        """@ColorScheme('dark light') should set _color_scheme='dark light'."""
        @ColorScheme("dark light")
        class MyShell:
            pass

        assert MyShell._color_scheme == "dark light"

    def test_system_alias(self):
        """@ColorScheme('system') should resolve to 'light dark'."""
        @ColorScheme("system")
        class MyShell:
            pass

        assert MyShell._color_scheme == "light dark"

    def test_normal(self):
        """@ColorScheme('normal') should set _color_scheme='normal'."""
        @ColorScheme("normal")
        class MyShell:
            pass

        assert MyShell._color_scheme == "normal"

    def test_preserves_class(self):
        """@ColorScheme should return the same class."""
        @ColorScheme("dark")
        class MyShell:
            pass

        assert MyShell.__name__ == "MyShell"


class TestColorSchemeHtml:
    """Test that @ColorScheme modifies index.html."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_app_shell()
        yield
        clear_app_shell()

    def test_dark_html(self):
        """@ColorScheme('dark') should add theme='dark' and color-scheme: dark."""
        @AppShell
        @ColorScheme("dark")
        class MyShell:
            pass

        html = get_index_html()
        assert 'theme="dark"' in html
        assert 'color-scheme: dark;' in html

    def test_light_html(self):
        """@ColorScheme('light') should add theme='light' and color-scheme: light."""
        @AppShell
        @ColorScheme("light")
        class MyShell:
            pass

        html = get_index_html()
        assert 'theme="light"' in html
        assert 'color-scheme: light;' in html

    def test_light_dark_html(self):
        """@ColorScheme('light dark') should use theme='light-dark'."""
        @AppShell
        @ColorScheme("light dark")
        class MyShell:
            pass

        html = get_index_html()
        assert 'theme="light-dark"' in html
        assert 'color-scheme: light dark;' in html

    def test_system_html(self):
        """@ColorScheme('system') should resolve to light-dark theme attr."""
        @AppShell
        @ColorScheme("system")
        class MyShell:
            pass

        html = get_index_html()
        assert 'theme="light-dark"' in html
        assert 'color-scheme: light dark;' in html

    def test_normal_no_attributes(self):
        """@ColorScheme('normal') should not add theme/color-scheme attributes."""
        @AppShell
        @ColorScheme("normal")
        class MyShell:
            pass

        html = get_index_html()
        # Should not have theme= or color-scheme on <html>
        assert 'theme="' not in html or 'theme="dark"' not in html

    def test_no_app_shell_no_attributes(self):
        """Without @AppShell, no color scheme attributes should be added."""
        html = get_index_html()
        # The <html> tag should not have a theme attribute injected
        assert '<html theme=' not in html


class TestUISetColorScheme:
    """Test UI.set_color_scheme() runtime method."""

    def test_set_dark(self):
        """set_color_scheme('dark') should queue JS with theme='dark'."""
        tree = StateTree()
        ui = UI(tree)
        ui.set_color_scheme("dark")

        execute = tree._pending_execute
        assert len(execute) == 1
        cmd = execute[0]
        # Should have: [theme_attr, value, js_script]
        assert cmd[0] == "dark"
        assert cmd[1] == "dark"
        assert "setAttribute" in cmd[2]

    def test_set_light_dark(self):
        """set_color_scheme('light dark') should use theme attr 'light-dark'."""
        tree = StateTree()
        ui = UI(tree)
        ui.set_color_scheme("light dark")

        cmd = tree._pending_execute[0]
        assert cmd[0] == "light-dark"
        assert cmd[1] == "light dark"

    def test_set_system(self):
        """set_color_scheme('system') should resolve to 'light dark'."""
        tree = StateTree()
        ui = UI(tree)
        ui.set_color_scheme("system")

        cmd = tree._pending_execute[0]
        assert cmd[0] == "light-dark"
        assert cmd[1] == "light dark"

    def test_set_normal_removes(self):
        """set_color_scheme('normal') should queue JS that removes attributes."""
        tree = StateTree()
        ui = UI(tree)
        ui.set_color_scheme("normal")

        execute = tree._pending_execute
        assert len(execute) == 1
        cmd = execute[0]
        # Should be just [js_script] with removeAttribute
        assert "removeAttribute" in cmd[0]
