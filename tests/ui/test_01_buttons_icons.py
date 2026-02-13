"""UI Tests — View 1: Buttons & Icons (/test/buttons-icons)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    """Single page for the whole module — navigate once."""
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/buttons-icons")
    p.wait_for_selector("vaadin-button", timeout=15000)
    yield p
    ctx.close()


class TestButton:
    def test_renders_with_text(self, view_page: Page):
        expect(view_page.locator("#btn1")).to_contain_text("Click me")

    def test_click_fires_listener(self, view_page: Page):
        view_page.locator("#btn-click").click()
        expect(view_page.locator("#result")).to_have_text("clicked")

    def test_set_text_updates(self, view_page: Page):
        btn = view_page.locator("#btn-text")
        expect(btn).to_contain_text("Old")
        btn.click()
        expect(btn).to_contain_text("New")

    def test_disabled_state(self, view_page: Page):
        expect(view_page.locator("#btn-dis")).to_have_attribute("disabled", "")

    def test_disable_on_click(self, view_page: Page):
        btn = view_page.locator("#btn-doc")
        btn.click()
        expect(view_page.locator("#result2")).to_have_text("clicked")
        expect(btn).to_have_attribute("disabled", "")

    def test_programmatic_click(self, view_page: Page):
        view_page.locator("#trigger").click()
        expect(view_page.locator("#result3")).to_have_text("prog")


class TestIcon:
    def test_renders(self, view_page: Page):
        expect(view_page.locator("#icon1")).to_be_visible()

    def test_color(self, view_page: Page):
        icon = view_page.locator("#icon-color")
        expect(icon).to_have_css("fill", "rgb(255, 0, 0)")

    def test_size(self, view_page: Page):
        icon = view_page.locator("#icon-size")
        expect(icon).to_have_css("width", "32px")
        expect(icon).to_have_css("height", "32px")


class TestButtonIcon:
    def test_icon_prefix(self, view_page: Page):
        btn = view_page.locator("#btn-icon")
        expect(btn.locator("vaadin-icon")).to_be_visible()
        expect(btn.locator("vaadin-icon")).to_have_attribute("slot", "prefix")

    def test_icon_after_text(self, view_page: Page):
        btn = view_page.locator("#btn-icon-after")
        expect(btn.locator("vaadin-icon")).to_have_attribute("slot", "suffix")

    def test_icon_only(self, view_page: Page):
        btn = view_page.locator("#btn-icononly")
        expect(btn).to_have_attribute("theme", "icon")


class TestClickShortcut:
    def test_enter_shortcut(self, view_page: Page):
        # Click body to clear focus from previously clicked elements
        view_page.locator("body").click()
        view_page.keyboard.press("Enter")
        expect(view_page.locator("#result4")).to_have_text("shortcut")


class TestDrawerToggle:
    def test_renders(self, view_page: Page):
        expect(view_page.locator("#toggle1")).to_be_visible()

    def test_click_fires(self, view_page: Page):
        view_page.locator("#toggle1").click()
        expect(view_page.locator("#result5")).to_have_text("toggled")


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/text-inputs"), timeout=5000)
