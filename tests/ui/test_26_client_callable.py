"""UI Tests — View 26: @ClientCallable (/test/client-callable)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/client-callable", "vaadin-button")
    yield shared_page


class TestClientCallable:
    @pytest.mark.spec("V26.01", "V26.05")
    def test_greet(self, view_page: Page):
        view_page.locator("#btn-greet").click()
        expect(view_page.locator("#cc-result")).to_have_text("Hello World", timeout=10000)

    @pytest.mark.spec("V26.03")
    def test_ping(self, view_page: Page):
        view_page.locator("#btn-ping").click()
        expect(view_page.locator("#cc-result")).to_have_text("pong", timeout=10000)


class TestNavigation:
    @pytest.mark.spec("V26.06")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/custom-field']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/custom-field"), timeout=5000)
