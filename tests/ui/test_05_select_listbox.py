"""UI Tests — View 5: Select & ListBox (/test/select-listbox)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/select-listbox")
    p.wait_for_selector("vaadin-select", timeout=15000)
    yield p
    ctx.close()


class TestSelect:
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#sel1")).to_have_js_property("label", "Country")

    def test_choose_item(self, view_page: Page):
        sel = view_page.locator("#sel1")
        sel.click()
        # Items are in the Select's light DOM (rendered by selectConnector)
        sel.locator("vaadin-select-item").nth(1).click()
        expect(view_page.locator("#sel1-val")).to_have_text("UK")

    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#sel-pre")).to_have_js_property("value", "DE")

    def test_placeholder(self, view_page: Page):
        expect(view_page.locator("#sel-ph")).to_have_js_property("placeholder", "Choose...")

    def test_read_only(self, view_page: Page):
        expect(view_page.locator("#sel-ro")).to_have_js_property("readonly", True)


class TestListBox:
    def test_renders_items(self, view_page: Page):
        lb = view_page.locator("#lb1")
        expect(lb.locator("vaadin-item")).to_have_count(3)

    def test_select_item(self, view_page: Page):
        lb = view_page.locator("#lb1")
        lb.locator("vaadin-item").nth(1).click()  # B
        expect(view_page.locator("#lb1-val")).to_have_text("B")

    def test_set_value_programmatic(self, view_page: Page):
        lb = view_page.locator("#lb-pre")
        expect(lb.locator("vaadin-item").nth(1)).to_have_attribute("selected", "")

    def test_item_label_generator(self, view_page: Page):
        lb = view_page.locator("#lb-gen")
        expect(lb.locator("vaadin-item").nth(0)).to_contain_text("#1")


class TestMultiSelectListBox:
    def test_renders_items(self, view_page: Page):
        mslb = view_page.locator("#mslb1")
        expect(mslb.locator("vaadin-item")).to_have_count(3)

    def test_select_multiple(self, view_page: Page):
        mslb = view_page.locator("#mslb1")
        mslb.locator("vaadin-item").nth(0).click()  # X
        mslb.locator("vaadin-item").nth(2).click()  # Z
        expect(view_page.locator("#mslb1-val")).to_contain_text("X")
        expect(view_page.locator("#mslb1-val")).to_contain_text("Z")

    def test_set_value_programmatic(self, view_page: Page):
        mslb = view_page.locator("#mslb-pre")
        expect(mslb.locator("vaadin-item").nth(0)).to_have_attribute("selected", "")
        expect(mslb.locator("vaadin-item").nth(2)).to_have_attribute("selected", "")

    def test_deselect_all(self, view_page: Page):
        view_page.locator("#btn-mslb-des").click()
        mslb = view_page.locator("#mslb-des")
        for i in range(3):
            expect(mslb.locator("vaadin-item").nth(i)).not_to_have_attribute("selected", "")

    def test_read_only(self, view_page: Page):
        expect(view_page.locator("#mslb-ro")).to_have_js_property("readonly", True)


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/combo-box"), timeout=5000)
