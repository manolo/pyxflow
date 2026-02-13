"""UI Tests — View 1: Buttons & Icons (/test/buttons-icons)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/buttons-icons", "vaadin-button")
    yield shared_page


class TestButton:
    @pytest.mark.spec("V01.01")
    def test_renders_with_text(self, view_page: Page):
        expect(view_page.locator("#btn1")).to_contain_text("Click me")

    @pytest.mark.spec("V01.02")
    def test_click_fires_listener(self, view_page: Page):
        view_page.locator("#btn-click").click()
        expect(view_page.locator("#result")).to_have_text("clicked")

    @pytest.mark.spec("V01.03")
    def test_set_text_updates(self, view_page: Page):
        btn = view_page.locator("#btn-text")
        expect(btn).to_contain_text("Old")
        btn.click()
        expect(btn).to_contain_text("New")

    @pytest.mark.spec("V01.04")
    def test_disabled_state(self, view_page: Page):
        expect(view_page.locator("#btn-dis")).to_have_attribute("disabled", "")

    @pytest.mark.spec("V01.05")
    def test_disable_on_click(self, view_page: Page):
        btn = view_page.locator("#btn-doc")
        btn.click()
        expect(view_page.locator("#result2")).to_have_text("clicked")
        expect(btn).to_have_attribute("disabled", "")

    @pytest.mark.spec("V01.07")
    def test_programmatic_click(self, view_page: Page):
        view_page.locator("#trigger").click()
        expect(view_page.locator("#result3")).to_have_text("prog")


class TestIcon:
    @pytest.mark.spec("V01.08")
    def test_renders(self, view_page: Page):
        expect(view_page.locator("#icon1")).to_be_visible()

    @pytest.mark.spec("V01.09")
    def test_color(self, view_page: Page):
        icon = view_page.locator("#icon-color")
        expect(icon).to_have_css("fill", "rgb(255, 0, 0)")

    @pytest.mark.spec("V01.10")
    def test_size(self, view_page: Page):
        icon = view_page.locator("#icon-size")
        expect(icon).to_have_css("width", "32px")
        expect(icon).to_have_css("height", "32px")


class TestButtonIcon:
    @pytest.mark.spec("V01.11")
    def test_icon_prefix(self, view_page: Page):
        btn = view_page.locator("#btn-icon")
        expect(btn.locator("vaadin-icon")).to_be_visible()
        expect(btn.locator("vaadin-icon")).to_have_attribute("slot", "prefix")

    @pytest.mark.spec("V01.12")
    def test_icon_after_text(self, view_page: Page):
        btn = view_page.locator("#btn-icon-after")
        expect(btn.locator("vaadin-icon")).to_have_attribute("slot", "suffix")

    @pytest.mark.spec("V01.13")
    def test_icon_only(self, view_page: Page):
        btn = view_page.locator("#btn-icononly")
        expect(btn).to_have_attribute("theme", "icon")


class TestClickShortcut:
    @pytest.mark.spec("V01.14")
    def test_enter_shortcut(self, view_page: Page):
        # Click body to clear focus from previously clicked elements
        view_page.locator("body").click()
        view_page.keyboard.press("Enter")
        expect(view_page.locator("#result4")).to_contain_text("shortcut:")

    @pytest.mark.spec("V01.18")
    def test_shortcut_with_textfield_value(self, view_page: Page):
        """Enter in TextField with Button shortcut must see the typed value.

        Regression: mSync (value sync) must be processed before keydown event.
        """
        field = view_page.locator("#short-field")
        field.click()
        view_page.keyboard.type("hello")
        view_page.keyboard.press("Enter")
        expect(view_page.locator("#result4")).to_contain_text("shortcut:hello:")
        # Second Enter — value unchanged, counter increments
        view_page.keyboard.press("Enter")
        expect(view_page.locator("#result4")).to_contain_text("shortcut:hello:")


class TestDrawerToggle:
    @pytest.mark.spec("V01.15")
    def test_renders(self, view_page: Page):
        expect(view_page.locator("#toggle1")).to_be_visible()

    @pytest.mark.spec("V01.16")
    def test_click_fires(self, view_page: Page):
        view_page.locator("#toggle1").click()
        expect(view_page.locator("#result5")).to_have_text("toggled")


class TestNavigation:
    @pytest.mark.spec("V01.17")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/text-inputs']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/text-inputs"), timeout=5000)
