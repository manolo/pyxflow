"""UI Tests — View 27: CustomField (/test/custom-field)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/custom-field")
    p.wait_for_selector("vaadin-custom-field", timeout=15000)
    yield p
    ctx.close()


class TestCustomField:
    def test_renders_children(self, view_page: Page):
        cf = view_page.locator("#cf1")
        expect(cf.locator("vaadin-text-field")).to_have_count(2)

    def test_label(self, view_page: Page):
        expect(view_page.locator("#cf1")).to_have_js_property("label", "Full Name")

    def test_read_only(self, view_page: Page):
        expect(view_page.locator("#cf-ro")).to_have_js_property("readonly", True)

    def test_invalid(self, view_page: Page):
        view_page.locator("#btn-cf-inv").click()
        expect(view_page.locator("#cf-inv")).to_have_js_property("invalid", True)
        expect(view_page.locator("#cf-inv")).to_have_js_property(
            "errorMessage", "Invalid name"
        )

    def test_required(self, view_page: Page):
        expect(view_page.locator("#cf-req")).to_have_js_property("required", True)


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/virtual-list"), timeout=5000)
