"""UI Tests — View 25: Theme Switching (/test/theme)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/theme")
    p.wait_for_selector("#btn-dark", timeout=15000)
    yield p
    ctx.close()


class TestThemeSwitching:
    @pytest.mark.spec("V25.01")
    def test_initial_state(self, view_page: Page):
        expect(view_page.locator("#theme-status")).to_be_visible()

    @pytest.mark.spec("V25.02")
    def test_switch_to_dark(self, view_page: Page):
        view_page.locator("#btn-dark").click()
        expect(view_page.locator("#theme-status")).to_have_text("dark")

    @pytest.mark.spec("V25.03")
    def test_switch_to_light(self, view_page: Page):
        view_page.locator("#btn-light").click()
        expect(view_page.locator("#theme-status")).to_have_text("light")

    @pytest.mark.spec("V25.04")
    def test_switch_to_aura(self, view_page: Page):
        view_page.locator("#btn-aura").click()
        expect(view_page.locator("#theme-status")).to_have_text("aura-light")

    @pytest.mark.spec("V25.05")
    def test_switch_to_aura_dark(self, view_page: Page):
        view_page.locator("#btn-aura-dark").click()
        expect(view_page.locator("#theme-status")).to_have_text("aura-dark")

    @pytest.mark.spec("V25.09")
    def test_custom_styled_button(self, view_page: Page):
        expect(view_page.locator("#styled-btn")).to_be_visible()

    # Reset to Lumo light for subsequent tests
    @pytest.mark.spec("V25.03")
    def test_reset_theme(self, view_page: Page):
        view_page.locator("#btn-light").click()
        expect(view_page.locator("#theme-status")).to_have_text("light")


class TestNavigation:
    @pytest.mark.spec("V25.10")
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/client-callable"), timeout=5000)
