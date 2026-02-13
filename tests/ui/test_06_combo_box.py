"""UI Tests — View 6: ComboBox & MultiSelectComboBox (/test/combo-box)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/combo-box")
    p.wait_for_selector("vaadin-combo-box", timeout=15000)
    yield p
    ctx.close()


class TestComboBox:
    @pytest.mark.spec("V06.01")
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#cb1")).to_have_js_property("label", "Fruit")

    @pytest.mark.spec("V06.03")
    def test_set_value_programmatic(self, view_page: Page):
        cb = view_page.locator("#cb-pre")
        expect(cb).to_have_js_property("value", "2")  # key for Cherry (index 2)

    @pytest.mark.spec("V06.05")
    def test_placeholder(self, view_page: Page):
        expect(view_page.locator("#cb-ph")).to_have_js_property("placeholder", "Search...")

    @pytest.mark.spec("V06.06")
    def test_clear_button(self, view_page: Page):
        expect(view_page.locator("#cb-clear")).to_have_js_property("clearButtonVisible", True)

    @pytest.mark.spec("V06.10")
    def test_auto_open_disabled(self, view_page: Page):
        expect(view_page.locator("#cb-noauto")).to_have_js_property("autoOpenDisabled", True)

    @pytest.mark.spec("V06.02")
    def test_open_and_select(self, view_page: Page):
        """Test selecting an item — run last so overlay doesn't interfere."""
        cb = view_page.locator("#cb1")
        cb.click()
        # Wait for overlay, then click the option directly
        view_page.locator("vaadin-combo-box-item").filter(has_text="Banana").click()
        expect(view_page.locator("#cb1-val")).to_have_text("Banana", timeout=5000)


class TestMultiSelectComboBox:
    @pytest.mark.spec("V06.11")
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#mscb1")).to_have_js_property("label", "Tags")

    @pytest.mark.spec("V06.13")
    def test_set_value_programmatic(self, view_page: Page):
        count = view_page.evaluate("document.querySelector('#mscb-pre').selectedItems.length")
        assert count == 2

    @pytest.mark.spec("V06.16")
    def test_clear_button(self, view_page: Page):
        expect(view_page.locator("#mscb-clr")).to_have_js_property("clearButtonVisible", True)

    @pytest.mark.spec("V06.19")
    def test_read_only(self, view_page: Page):
        expect(view_page.locator("#mscb-ro")).to_have_js_property("readonly", True)

    @pytest.mark.spec("V06.15")
    def test_deselect_all(self, view_page: Page):
        """Test deselect — run last since it modifies state."""
        view_page.locator("#btn-mscb-des").click()
        mscb = view_page.locator("#mscb-des")
        expect(mscb).to_have_js_property("selectedItems", [])


class TestNavigation:
    @pytest.mark.spec("V06.20")
    def test_nav_to_next(self, view_page: Page):
        # Ensure no overlay is blocking
        view_page.keyboard.press("Escape")
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/date-time"), timeout=5000)
