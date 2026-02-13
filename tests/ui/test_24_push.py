"""UI Tests — View 24: WebSocket Push (/test/push)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/push", "vaadin-button")
    yield shared_page


class TestPush:
    @pytest.mark.spec("V24.01")
    def test_single_push(self, view_page: Page):
        view_page.locator("#start").click()
        expect(view_page.locator("#push-result")).to_have_text("done", timeout=5000)

    @pytest.mark.spec("V24.02")
    def test_multiple_push(self, view_page: Page):
        view_page.locator("#multi").click()
        expect(view_page.locator("#push-count")).to_have_text("3", timeout=5000)

    @pytest.mark.spec("V24.03")
    def test_progress_bar(self, view_page: Page):
        view_page.locator("#progress").click()
        expect(view_page.locator("#push-pb")).to_have_js_property("value", 1.0, timeout=5000)

    @pytest.mark.spec("V24.04")
    def test_ui_access(self, view_page: Page):
        view_page.locator("#access").click()
        expect(view_page.locator("#push-access")).to_have_text("accessed", timeout=5000)


class TestNavigation:
    @pytest.mark.spec("V24.08")
    def test_nav_to_next(self, browser, base_url):
        """Use fresh context — push WS state blocks SPA nav on reused page."""
        ctx = browser.new_context(viewport={"width": 1280, "height": 720})
        page = ctx.new_page()
        page.goto(f"{base_url}/test/push")
        page.wait_for_selector("vaadin-button", timeout=15000)
        page.locator("vaadin-side-nav-item[path='/test/theme']").click()
        expect(page).to_have_url(re.compile(r".*/test/theme"), timeout=5000)
        ctx.close()
