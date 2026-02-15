"""UI Tests — View 25: Theme Switching (/test/theme)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/theme", "vaadin-button")
    yield shared_page


class TestThemeSwitching:
    @pytest.mark.spec("V25.01")
    def test_initial_state(self, view_page: Page):
        expect(view_page.locator("#theme-status")).to_be_visible()
        # Default app theme is Lumo light
        expect(view_page.locator("#theme-status")).to_have_text("lumo-light")

    @pytest.mark.spec("V25.02")
    def test_switch_to_dark(self, view_page: Page):
        view_page.locator("#btn-dark").click()
        expect(view_page.locator("#theme-status")).to_have_text("lumo-dark")

    @pytest.mark.spec("V25.03")
    def test_switch_to_light(self, view_page: Page):
        view_page.locator("#btn-light").click()
        expect(view_page.locator("#theme-status")).to_have_text("lumo-light")

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

    # Restore theme to whatever it was before this test module ran
    @pytest.mark.spec("V25.06")
    def test_reset_theme(self, view_page: Page):
        view_page.locator("#btn-reset").click()
        expect(view_page.locator("#theme-status")).to_have_text("lumo-light")


class TestThemePersistsAcrossNavigation:
    @pytest.mark.spec("V25.11")
    def test_theme_survives_navigation(self, view_page: Page):
        """Theme set on one view should persist when navigating away and back."""
        # Set to Aura light
        view_page.locator("#btn-aura").click()
        expect(view_page.locator("#theme-status")).to_have_text("aura-light")

        # Navigate to another view
        view_page.locator("vaadin-side-nav-item[path='/test/client-callable']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/client-callable"), timeout=5000)

        # Navigate back to theme view
        view_page.locator("vaadin-side-nav-item[path='/test/theme']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/theme"), timeout=5000)

        # Theme should still be aura-light (UI singleton preserves state)
        expect(view_page.locator("#theme-status")).to_have_text("aura-light")

    @pytest.mark.spec("V25.12")
    def test_reset_restores_captured_initial(self, view_page: Page):
        """Reset restores the theme captured at view attach (aura-light after nav back)."""
        # After navigating back with aura-light, _attach captured it as _initial_theme.
        # So reset restores to aura-light, proving the capture works correctly.
        view_page.locator("#btn-reset").click()
        expect(view_page.locator("#theme-status")).to_have_text("aura-light")


class TestNavigation:
    @pytest.mark.spec("V25.10")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/client-callable']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/client-callable"), timeout=5000)
