"""UI Tests — View 28: VirtualList (/test/virtual-list)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/virtual-list")
    p.wait_for_selector("vaadin-virtual-list", timeout=15000)
    yield p
    ctx.close()


class TestVirtualList:
    @pytest.mark.spec("V28.01")
    def test_renders_items(self, view_page: Page):
        vl = view_page.locator("#vl1")
        expect(vl).to_be_visible()
        expect(vl).to_contain_text("Item 0")

    @pytest.mark.spec("V28.05")
    def test_replace_items(self, view_page: Page):
        view_page.locator("#btn-vl-replace").click()
        vl = view_page.locator("#vl1")
        expect(vl).to_contain_text("New 0")


class TestNavigation:
    @pytest.mark.spec("V28.08")
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/login"), timeout=5000)
