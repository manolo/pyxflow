"""UI Tests — View 5: Select & ListBox (/test/select-listbox)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/select-listbox", "vaadin-select")
    yield shared_page


class TestSelect:
    @pytest.mark.spec("V05.01")
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#sel1")).to_have_js_property("label", "Country")

    @pytest.mark.spec("V05.02")
    def test_choose_item(self, view_page: Page):
        sel = view_page.locator("#sel1")
        sel.click()
        sel.locator("vaadin-select-item").nth(1).click()
        expect(view_page.locator("#sel1-val")).to_have_text("UK")

    @pytest.mark.spec("V05.03")
    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#sel-pre")).to_have_js_property("value", "DE")

    @pytest.mark.spec("V05.04")
    def test_placeholder(self, view_page: Page):
        expect(view_page.locator("#sel-ph")).to_have_js_property("placeholder", "Choose...")

    @pytest.mark.spec("V05.06")
    def test_item_label_generator(self, view_page: Page):
        """Select with item_label_generator=str.upper shows uppercase labels."""
        sel = view_page.locator("#sel-gen")
        sel.click()
        view_page.wait_for_timeout(200)
        # Items should show "US", "UK" (uppercased)
        items = sel.locator("vaadin-select-item")
        expect(items.nth(0)).to_contain_text("US")
        expect(items.nth(1)).to_contain_text("UK")
        view_page.keyboard.press("Escape")

    @pytest.mark.spec("V05.08")
    def test_read_only(self, view_page: Page):
        expect(view_page.locator("#sel-ro")).to_have_js_property("readonly", True)

    @pytest.mark.spec("V05.19")
    def test_required(self, view_page: Page):
        expect(view_page.locator("#sel-req")).to_have_js_property("required", True)


class TestListBox:
    @pytest.mark.spec("V05.09")
    def test_renders_items(self, view_page: Page):
        lb = view_page.locator("#lb1")
        expect(lb.locator("vaadin-item")).to_have_count(3)

    @pytest.mark.spec("V05.10")
    def test_select_item(self, view_page: Page):
        lb = view_page.locator("#lb1")
        lb.locator("vaadin-item").nth(1).click()  # B
        expect(view_page.locator("#lb1-val")).to_have_text("B")

    @pytest.mark.spec("V05.11")
    def test_set_value_programmatic(self, view_page: Page):
        lb = view_page.locator("#lb-pre")
        expect(lb.locator("vaadin-item").nth(1)).to_have_attribute("selected", "")

    @pytest.mark.spec("V05.12")
    def test_item_label_generator(self, view_page: Page):
        lb = view_page.locator("#lb-gen")
        expect(lb.locator("vaadin-item").nth(0)).to_contain_text("#1")


class TestMultiSelectListBox:
    @pytest.mark.spec("V05.13")
    def test_renders_items(self, view_page: Page):
        mslb = view_page.locator("#mslb1")
        expect(mslb.locator("vaadin-item")).to_have_count(3)

    @pytest.mark.spec("V05.14")
    def test_select_multiple(self, view_page: Page):
        mslb = view_page.locator("#mslb1")
        mslb.locator("vaadin-item").nth(0).click()  # X
        mslb.locator("vaadin-item").nth(2).click()  # Z
        expect(view_page.locator("#mslb1-val")).to_contain_text("X")
        expect(view_page.locator("#mslb1-val")).to_contain_text("Z")

    @pytest.mark.spec("V05.15")
    def test_set_value_programmatic(self, view_page: Page):
        mslb = view_page.locator("#mslb-pre")
        expect(mslb.locator("vaadin-item").nth(0)).to_have_attribute("selected", "")
        expect(mslb.locator("vaadin-item").nth(2)).to_have_attribute("selected", "")

    @pytest.mark.spec("V05.16")
    def test_deselect_all(self, view_page: Page):
        view_page.locator("#btn-mslb-des").click()
        mslb = view_page.locator("#mslb-des")
        for i in range(3):
            expect(mslb.locator("vaadin-item").nth(i)).not_to_have_attribute("selected", "")

    @pytest.mark.spec("V05.17")
    def test_read_only(self, view_page: Page):
        expect(view_page.locator("#mslb-ro")).to_have_js_property("readonly", True)


class TestNavigation:
    @pytest.mark.spec("V05.20")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/combo-box']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/combo-box"), timeout=5000)
