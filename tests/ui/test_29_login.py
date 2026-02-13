"""UI Tests — View 29: LoginForm & LoginOverlay (/test/login)"""

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/login", "vaadin-login-form")
    yield shared_page


class TestLoginForm:
    @pytest.mark.spec("V29.01")
    def test_renders(self, view_page: Page):
        lf = view_page.locator("#lf1")
        expect(lf).to_be_visible()

    @pytest.mark.spec("V29.02")
    def test_submit(self, view_page: Page):
        lf = view_page.locator("#lf1")
        # Type into username/password fields inside login form
        lf.locator("vaadin-text-field").first.click()
        view_page.keyboard.type("admin")
        lf.locator("vaadin-password-field").first.click()
        view_page.keyboard.type("pass123")
        lf.locator("vaadin-button").first.click()
        expect(view_page.locator("#lf-result")).to_have_text("admin:pass123", timeout=5000)


class TestLoginOverlay:
    @pytest.mark.spec("V29.06")
    def test_open(self, view_page: Page):
        view_page.locator("#btn-lo").click()
        overlay = view_page.locator("vaadin-login-overlay-wrapper")
        expect(overlay).to_be_visible()

    @pytest.mark.spec("V29.07")
    def test_title(self, view_page: Page):
        lo = view_page.locator("#lo1")
        expect(lo).to_have_js_property("title", "Test App")

    @pytest.mark.spec("V29.10")
    def test_close(self, view_page: Page):
        # Dismiss the modal overlay first with Escape, then close programmatically
        view_page.keyboard.press("Escape")
        view_page.locator("#btn-lo-close").evaluate("el => el.click()")
        overlay = view_page.locator("vaadin-login-overlay-wrapper")
        expect(overlay).to_be_hidden()


class TestAllDone:
    @pytest.mark.spec("V29.11")
    def test_all_views_visited(self, view_page: Page):
        expect(view_page.locator("#all-done")).to_have_text("All UI test views visited")
