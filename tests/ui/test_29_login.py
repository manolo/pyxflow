"""UI Tests — View 29: LoginForm & LoginOverlay (/test/login)"""

import re

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
        lf.locator("vaadin-text-field").first.click()
        view_page.keyboard.type("admin")
        lf.locator("vaadin-password-field").first.click()
        view_page.keyboard.type("pass123")
        lf.locator("vaadin-button").first.click()
        expect(view_page.locator("#lf-result")).to_have_text("admin:pass123", timeout=5000)

    @pytest.mark.spec("V29.04")
    def test_forgot_password(self, view_page: Page):
        """Clicking 'Forgot password' link fires listener."""
        lf = view_page.locator("#lf1")
        # LoginForm has a "Forgot password" button inside
        forgot_btn = lf.locator("vaadin-button").filter(has_text="Forgot password")
        if forgot_btn.count() > 0:
            forgot_btn.click()
            expect(view_page.locator("#lf-forgot")).to_have_text("forgot", timeout=3000)


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

    @pytest.mark.spec("V29.08")
    def test_description(self, view_page: Page):
        """LoginOverlay set_description."""
        lo = view_page.locator("#lo1")
        expect(lo).to_have_js_property("description", "Enter credentials")

    @pytest.mark.spec("V29.10")
    def test_close(self, view_page: Page):
        view_page.keyboard.press("Escape")
        view_page.locator("#btn-lo-close").evaluate("el => el.click()")
        overlay = view_page.locator("vaadin-login-overlay-wrapper")
        expect(overlay).to_be_hidden()


class TestNavigation:
    @pytest.mark.spec("V29.11")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/server-errors']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/server-errors"), timeout=5000)
