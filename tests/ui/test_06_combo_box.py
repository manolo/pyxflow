"""UI Tests — View 6: ComboBox & MultiSelectComboBox (/test/combo-box)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/combo-box", "vaadin-combo-box")
    yield shared_page


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
        view_page.locator("vaadin-combo-box-item").filter(has_text="Banana").click()
        expect(view_page.locator("#cb1-val")).to_have_text("Banana", timeout=5000)
        view_page.keyboard.press("Escape")


class TestComboBoxFiltering:
    @pytest.mark.spec("V06.04")
    def test_type_to_filter(self, view_page: Page):
        """Typing in ComboBox filters the dropdown items."""
        view_page.keyboard.press("Escape")
        cb = view_page.locator("#cb1")
        cb.click()
        # Clear any existing value, then type filter text
        view_page.keyboard.press("Meta+a")
        view_page.keyboard.type("Ban")
        # Verify filtered result — get_by_role ignores hidden overlay items
        expect(view_page.get_by_role("option", name="Banana")).to_be_visible()
        view_page.keyboard.press("Escape")

    @pytest.mark.spec("V06.08")
    def test_item_label_generator(self, view_page: Page):
        """ComboBox with item_label_generator displays custom labels."""
        view_page.keyboard.press("Escape")
        cb = view_page.locator("#cb-gen")
        cb.click()
        # get_by_role ignores hidden overlay items from other combo-boxes
        expect(view_page.get_by_role("option", name="Apple")).to_be_visible()
        view_page.keyboard.press("Escape")


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
        view_page.keyboard.press("Escape")
        view_page.locator("#btn-mscb-des").click()
        mscb = view_page.locator("#mscb-des")
        expect(mscb).to_have_js_property("selectedItems", [])


class TestMultiSelectComboBoxValueChange:
    """Value change listener fires from both client selection and server set_value."""

    @pytest.mark.spec("V06.12")
    def test_client_select_fires_listener(self, view_page: Page):
        """Selecting an item in the dropdown fires value change listener."""
        view_page.keyboard.press("Escape")
        mscb = view_page.locator("#mscb1")
        mscb.locator("input").click()
        view_page.keyboard.type("A")
        view_page.locator("vaadin-multi-select-combo-box-item").first.click()
        expect(view_page.locator("#mscb1-val")).to_have_text("A", timeout=5000)
        view_page.keyboard.press("Escape")

    @pytest.mark.spec("V06.14")
    def test_server_set_value_fires_listener(self, view_page: Page):
        """Clicking Set A,C button calls set_value which fires listener."""
        view_page.keyboard.press("Escape")
        view_page.locator("#btn-mscb-set").click()
        expect(view_page.locator("#mscb1-val")).to_have_text("A,C", timeout=5000)

    @pytest.mark.spec("V06.26")
    def test_client_select_updates_chips(self, view_page: Page):
        """After client selection, chips appear in the combo box."""
        mscb = view_page.locator("#mscb1")
        count = view_page.evaluate("document.querySelector('#mscb1').selectedItems.length")
        assert count >= 1


class TestComboBoxPrefix:
    @pytest.mark.spec("V06.21")
    def test_prefix_icon_rendered(self, view_page: Page):
        cb = view_page.locator("#cb-prefix")
        icon = cb.locator('vaadin-icon[slot="prefix"]')
        expect(icon).to_have_count(1)


class TestComboBoxOverlayWidth:
    @pytest.mark.spec("V06.22")
    def test_overlay_width(self, view_page: Page):
        cb = view_page.locator("#cb-ow")
        expect(cb).to_have_js_property("overlayWidth", "400px")


class TestMultiSelectComboBoxExtras:
    @pytest.mark.spec("V06.23")
    def test_selected_items_on_top(self, view_page: Page):
        mscb = view_page.locator("#mscb-top")
        expect(mscb).to_have_js_property("selectedItemsOnTop", True)

    @pytest.mark.spec("V06.24")
    def test_keep_filter(self, view_page: Page):
        mscb = view_page.locator("#mscb-kf")
        expect(mscb).to_have_js_property("keepFilter", True)


class TestNavigation:
    @pytest.mark.spec("V06.25")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.keyboard.press("Escape")
        view_page.locator("vaadin-side-nav-item[path='/test/date-time']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/date-time"), timeout=5000)
