"""UI Tests — View 24: WebSocket Push (/test/push)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/push")
    p.wait_for_selector("#start", timeout=15000)
    yield p
    ctx.close()


class TestPush:
    def test_single_push(self, view_page: Page):
        view_page.locator("#start").click()
        expect(view_page.locator("#push-result")).to_have_text("done", timeout=5000)

    def test_multiple_push(self, view_page: Page):
        view_page.locator("#multi").click()
        expect(view_page.locator("#push-count")).to_have_text("3", timeout=5000)

    def test_progress_bar(self, view_page: Page):
        view_page.locator("#progress").click()
        expect(view_page.locator("#push-pb")).to_have_js_property("value", 1.0, timeout=5000)

    def test_ui_access(self, view_page: Page):
        view_page.locator("#access").click()
        expect(view_page.locator("#push-access")).to_have_text("accessed", timeout=5000)


class TestNavigation:
    def test_nav_to_next(self, browser, base_url):
        # Use a fresh page — WS push state on the test page can block SPA nav
        ctx = browser.new_context(viewport={"width": 1280, "height": 720})
        p = ctx.new_page()
        p.goto(f"{base_url}/test/push")
        p.wait_for_selector("#nav-next", timeout=15000)
        p.locator("#nav-next").click()
        expect(p).to_have_url(re.compile(r".*/test/theme"), timeout=5000)
        ctx.close()
