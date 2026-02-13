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
    @pytest.mark.spec("V21.01")
    def test_textfield_readonly(self, view_page: Page):
        view_page.locator("#btn-ro-on").click()
        expect(view_page.locator("#mix-tf")).to_have_js_property("readonly", True)

    @pytest.mark.spec("V21.04")
    def test_textfield_readonly_off(self, view_page: Page):
        view_page.locator("#btn-ro-off").click()
        expect(view_page.locator("#mix-tf")).to_have_js_property("readonly", False)

    @pytest.mark.spec("V21.02")
    def test_select_readonly(self, view_page: Page):
        view_page.locator("#btn-sel-ro").click()
        expect(view_page.locator("#mix-sel")).to_have_js_property("readonly", True)

    @pytest.mark.spec("V21.03")
    def test_datepicker_readonly(self, view_page: Page):
        view_page.locator("#btn-dp-ro").click()
        expect(view_page.locator("#mix-dp")).to_have_js_property("readonly", True)


class TestHasValidation:
    @pytest.mark.spec("V21.05", "V21.06")
    def test_textfield_invalid(self, view_page: Page):
        view_page.locator("#btn-invalid").click()
        expect(view_page.locator("#mix-tf")).to_have_js_property("invalid", True)
        expect(view_page.locator("#mix-tf")).to_have_js_property("errorMessage", "Required field")

    @pytest.mark.spec("V21.09")
    def test_clear_invalid(self, view_page: Page):
        view_page.locator("#btn-valid").click()
        expect(view_page.locator("#mix-tf")).to_have_js_property("invalid", False)

    @pytest.mark.spec("V21.07")
    def test_select_invalid(self, view_page: Page):
        view_page.locator("#btn-sel-inv").click()
        expect(view_page.locator("#mix-sel")).to_have_js_property("invalid", True)

    @pytest.mark.spec("V21.08")
    def test_combobox_invalid(self, view_page: Page):
        view_page.locator("#btn-cb-inv").click()
        expect(view_page.locator("#mix-cb")).to_have_js_property("invalid", True)


class TestHasRequired:
    @pytest.mark.spec("V21.10")
    def test_textfield_required(self, view_page: Page):
        view_page.locator("#btn-req").click()
        expect(view_page.locator("#mix-tf")).to_have_js_property("required", True)

    @pytest.mark.spec("V21.11")
    def test_select_required(self, view_page: Page):
        view_page.locator("#btn-sel-req").click()
        expect(view_page.locator("#mix-sel")).to_have_js_property("required", True)

    @pytest.mark.spec("V21.12")
    def test_combobox_required(self, view_page: Page):
        view_page.locator("#btn-cb-req").click()
        expect(view_page.locator("#mix-cb")).to_have_js_property("required", True)

    @pytest.mark.spec("V21.13")
    def test_datepicker_required(self, view_page: Page):
        view_page.locator("#btn-dp-req").click()
        expect(view_page.locator("#mix-dp")).to_have_js_property("required", True)


class TestNavigation:
    @pytest.mark.spec("V21.17")
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/binder"), timeout=5000)
