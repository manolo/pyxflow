"""UI Tests — View 21: Field Mixins (/test/field-mixins)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/field-mixins")
    p.wait_for_selector("vaadin-text-field", timeout=15000)
    yield p
    ctx.close()


class TestHasReadOnly:
    def test_textfield_readonly(self, view_page: Page):
        view_page.locator("#btn-ro-on").click()
        expect(view_page.locator("#mix-tf")).to_have_js_property("readonly", True)

    def test_textfield_readonly_off(self, view_page: Page):
        view_page.locator("#btn-ro-off").click()
        expect(view_page.locator("#mix-tf")).to_have_js_property("readonly", False)

    def test_select_readonly(self, view_page: Page):
        view_page.locator("#btn-sel-ro").click()
        expect(view_page.locator("#mix-sel")).to_have_js_property("readonly", True)

    def test_datepicker_readonly(self, view_page: Page):
        view_page.locator("#btn-dp-ro").click()
        expect(view_page.locator("#mix-dp")).to_have_js_property("readonly", True)


class TestHasValidation:
    def test_textfield_invalid(self, view_page: Page):
        view_page.locator("#btn-invalid").click()
        expect(view_page.locator("#mix-tf")).to_have_js_property("invalid", True)
        expect(view_page.locator("#mix-tf")).to_have_js_property("errorMessage", "Required field")

    def test_clear_invalid(self, view_page: Page):
        view_page.locator("#btn-valid").click()
        expect(view_page.locator("#mix-tf")).to_have_js_property("invalid", False)

    def test_select_invalid(self, view_page: Page):
        view_page.locator("#btn-sel-inv").click()
        expect(view_page.locator("#mix-sel")).to_have_js_property("invalid", True)

    def test_combobox_invalid(self, view_page: Page):
        view_page.locator("#btn-cb-inv").click()
        expect(view_page.locator("#mix-cb")).to_have_js_property("invalid", True)


class TestHasRequired:
    def test_textfield_required(self, view_page: Page):
        view_page.locator("#btn-req").click()
        expect(view_page.locator("#mix-tf")).to_have_js_property("required", True)

    def test_select_required(self, view_page: Page):
        view_page.locator("#btn-sel-req").click()
        expect(view_page.locator("#mix-sel")).to_have_js_property("required", True)

    def test_combobox_required(self, view_page: Page):
        view_page.locator("#btn-cb-req").click()
        expect(view_page.locator("#mix-cb")).to_have_js_property("required", True)

    def test_datepicker_required(self, view_page: Page):
        view_page.locator("#btn-dp-req").click()
        expect(view_page.locator("#mix-dp")).to_have_js_property("required", True)


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/binder"), timeout=5000)
