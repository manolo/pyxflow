"""UI Tests — View 26: @ClientCallable (/test/client-callable)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/client-callable")
    p.wait_for_selector("#btn-greet", timeout=15000)
    yield p
    ctx.close()


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
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/custom-field"), timeout=5000)
