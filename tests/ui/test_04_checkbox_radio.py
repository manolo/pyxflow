"""UI Tests — View 4: Checkbox & RadioButtonGroup (/test/checkbox-radio)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/checkbox-radio")
    p.wait_for_selector("vaadin-checkbox", timeout=15000)
    yield p
    ctx.close()


class TestCheckbox:
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#cb1")).to_have_js_property("label", "Accept terms")

    def test_click_toggles(self, view_page: Page):
        view_page.locator("#cb1").click()
        expect(view_page.locator("#cb1-val")).to_have_text("True")
        view_page.locator("#cb1").click()
        expect(view_page.locator("#cb1-val")).to_have_text("False")

    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#cb-pre")).to_have_js_property("checked", True)

    def test_indeterminate(self, view_page: Page):
        expect(view_page.locator("#cb-ind")).to_have_js_property("indeterminate", True)

    def test_set_label_dynamic(self, view_page: Page):
        view_page.locator("#btn-cb-lbl").click()
        expect(view_page.locator("#cb-lbl")).to_have_js_property("label", "New")

    def test_read_only(self, view_page: Page):
        expect(view_page.locator("#cb-ro")).to_have_js_property("readonly", True)

    def test_required(self, view_page: Page):
        expect(view_page.locator("#cb-req")).to_have_js_property("required", True)


class TestCheckboxGroup:
    def test_renders_items(self, view_page: Page):
        group = view_page.locator("#cbg1")
        expect(group.locator("vaadin-checkbox")).to_have_count(3)

    def test_select_multiple(self, view_page: Page):
        group = view_page.locator("#cbg1")
        group.locator("vaadin-checkbox").nth(0).click()  # Red
        group.locator("vaadin-checkbox").nth(2).click()  # Blue
        expect(view_page.locator("#cbg1-val")).to_contain_text("Blue")
        expect(view_page.locator("#cbg1-val")).to_contain_text("Red")

    def test_set_value_programmatic(self, view_page: Page):
        group = view_page.locator("#cbg-pre")
        # A and C should be checked
        expect(group.locator("vaadin-checkbox").nth(0)).to_have_js_property("checked", True)
        expect(group.locator("vaadin-checkbox").nth(2)).to_have_js_property("checked", True)

    def test_item_label_generator(self, view_page: Page):
        group = view_page.locator("#cbg-gen")
        expect(group.locator("vaadin-checkbox").nth(0)).to_have_js_property("label", "Item 1")

    def test_select_method(self, view_page: Page):
        view_page.locator("#btn-cbg-sel").click()
        group = view_page.locator("#cbg-sel")
        expect(group.locator("vaadin-checkbox").nth(0)).to_have_js_property("checked", True)


class TestRadioButtonGroup:
    def test_renders_items(self, view_page: Page):
        group = view_page.locator("#rbg1")
        expect(group.locator("vaadin-radio-button")).to_have_count(3)

    def test_select_one(self, view_page: Page):
        group = view_page.locator("#rbg1")
        group.locator("vaadin-radio-button").nth(1).click()  # M
        expect(view_page.locator("#rbg1-val")).to_have_text("M")

    def test_set_value_programmatic(self, view_page: Page):
        group = view_page.locator("#rbg-pre")
        expect(group.locator("vaadin-radio-button").nth(1)).to_have_js_property("checked", True)

    def test_item_label_generator(self, view_page: Page):
        group = view_page.locator("#rbg-gen")
        expect(group.locator("vaadin-radio-button").nth(0)).to_have_js_property("label", "Small")

    def test_read_only(self, view_page: Page):
        expect(view_page.locator("#rbg-ro")).to_have_js_property("readonly", True)

    def test_required(self, view_page: Page):
        expect(view_page.locator("#rbg-req")).to_have_js_property("required", True)


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/select-listbox"), timeout=5000)
