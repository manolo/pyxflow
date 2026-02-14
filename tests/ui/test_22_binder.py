"""UI Tests — View 22: Binder (/test/binder)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/binder", "vaadin-text-field")
    yield shared_page


def _type_in_field(page: Page, selector: str, text: str):
    """Click a field, clear it, type new text, then Tab to trigger change event."""
    page.locator(selector).click()
    page.keyboard.press("Meta+a")
    page.keyboard.press("Backspace")
    if text:
        page.keyboard.type(text)
    page.keyboard.press("Tab")
    page.wait_for_timeout(70)


class TestReadBean:
    @pytest.mark.spec("V22.01")
    def test_populates_fields(self, view_page: Page):
        expect(view_page.locator("#name")).to_have_js_property("value", "Alice")
        expect(view_page.locator("#email")).to_have_js_property("value", "alice@x.com")
        expect(view_page.locator("#age")).to_have_js_property("value", "30")

    @pytest.mark.spec("V22.02")
    def test_read_bean_none_clears_fields(self, view_page: Page):
        """read_bean(None) should clear all fields."""
        view_page.locator("#clear").click()
        view_page.wait_for_timeout(200)
        expect(view_page.locator("#name")).to_have_js_property("value", "")
        expect(view_page.locator("#email")).to_have_js_property("value", "")
        expect(view_page.locator("#age")).to_have_js_property("value", "")
        # Restore for subsequent tests
        view_page.locator("#reread").click()
        view_page.wait_for_timeout(200)


class TestWriteBean:
    @pytest.mark.spec("V22.03")
    def test_writes_form_to_object(self, view_page: Page):
        _type_in_field(view_page, "#name", "Bob")
        _type_in_field(view_page, "#email", "bob@x.com")
        _type_in_field(view_page, "#age", "25")
        view_page.locator("#save").click()
        expect(view_page.locator("#binder-result")).to_have_text(
            re.compile(r"Bob,bob@x\.com,25"), timeout=3000
        )


class TestValidation:
    @pytest.mark.spec("V22.04")
    def test_required_blocks_save(self, view_page: Page):
        _type_in_field(view_page, "#name", "")
        view_page.locator("#save").click()
        expect(view_page.locator("#name")).to_have_js_property("invalid", True)

    @pytest.mark.spec("V22.05")
    def test_email_pattern_validator(self, view_page: Page):
        """Invalid email should show error."""
        _type_in_field(view_page, "#name", "Test")
        _type_in_field(view_page, "#email", "not-email")
        view_page.locator("#save").click()
        expect(view_page.locator("#email")).to_have_js_property("invalid", True)

    @pytest.mark.spec("V22.06")
    def test_age_range_validator(self, view_page: Page):
        """Age out of range should show error."""
        _type_in_field(view_page, "#name", "Test")
        _type_in_field(view_page, "#email", "t@x.com")
        _type_in_field(view_page, "#age", "200")
        view_page.locator("#save").click()
        expect(view_page.locator("#age")).to_have_js_property("invalid", True)

    @pytest.mark.spec("V22.07")
    def test_valid_saves(self, view_page: Page):
        _type_in_field(view_page, "#name", "Valid")
        _type_in_field(view_page, "#email", "v@x.com")
        _type_in_field(view_page, "#age", "20")
        view_page.locator("#save").click()
        expect(view_page.locator("#binder-result")).to_have_text(
            re.compile(r"Valid,v@x\.com,20"), timeout=3000
        )

    @pytest.mark.spec("V22.14")
    def test_multiple_validation_errors(self, view_page: Page):
        """All fields invalid at once shows multiple errors."""
        _type_in_field(view_page, "#name", "")
        _type_in_field(view_page, "#email", "bad")
        _type_in_field(view_page, "#age", "999")
        view_page.locator("#save").click()
        expect(view_page.locator("#name")).to_have_js_property("invalid", True)
        expect(view_page.locator("#email")).to_have_js_property("invalid", True)
        expect(view_page.locator("#age")).to_have_js_property("invalid", True)


class TestConverter:
    @pytest.mark.spec("V22.08")
    def test_string_to_int_converter_error(self, view_page: Page):
        """Non-numeric age should show conversion error."""
        _type_in_field(view_page, "#name", "Test")
        _type_in_field(view_page, "#email", "t@x.com")
        _type_in_field(view_page, "#age", "abc")
        view_page.locator("#save").click()
        expect(view_page.locator("#age")).to_have_js_property("invalid", True)


class TestDirtyTracking:
    @pytest.mark.spec("V22.09")
    def test_dirty_after_change(self, view_page: Page):
        # First re-read to reset state
        view_page.locator("#reread").click()
        view_page.wait_for_timeout(200)
        _type_in_field(view_page, "#name", "Changed")
        expect(view_page.locator("#dirty")).to_have_text("true")

    @pytest.mark.spec("V22.10")
    def test_not_dirty_after_read_bean(self, view_page: Page):
        """After read_bean, is_dirty should be false."""
        view_page.locator("#reread").click()
        view_page.wait_for_timeout(200)
        expect(view_page.locator("#dirty")).to_have_text("false")


class TestSetBean:
    @pytest.mark.spec("V22.11")
    def test_auto_sync(self, view_page: Page):
        """set_bean enables automatic sync to the bean object."""
        _type_in_field(view_page, "#auto-name", "New Name")
        expect(view_page.locator("#auto-sync")).to_have_text("New Name", timeout=3000)


class TestBinderFieldTypes:
    """Test that Binder saves correct values for non-text fields (mSync regression)."""

    @pytest.mark.spec("V22.15")
    def test_datepicker_saves(self, view_page: Page):
        """DatePicker value should survive binder read_bean."""
        # Re-read to populate fields from Zara (has birthday=1995-06-20)
        view_page.locator("#reread").click()
        view_page.wait_for_timeout(200)
        dp = view_page.locator("#bind-dp")
        expect(dp).to_have_js_property("value", "1995-06-20", timeout=3000)

    @pytest.mark.spec("V22.16")
    def test_timepicker_saves(self, view_page: Page):
        """TimePicker value should survive binder read_bean."""
        tp = view_page.locator("#bind-tp")
        expect(tp).to_have_js_property("value", "14:30", timeout=3000)

    @pytest.mark.spec("V22.18")
    def test_select_saves(self, view_page: Page):
        """Select value via binder write_bean."""
        # Re-read to set country=UK
        view_page.locator("#reread").click()
        view_page.wait_for_timeout(200)
        # Set valid text fields
        _type_in_field(view_page, "#name", "Test")
        _type_in_field(view_page, "#email", "t@x.com")
        _type_in_field(view_page, "#age", "40")
        view_page.locator("#save").click()
        # Result should contain the country value (UK)
        expect(view_page.locator("#binder-result")).to_have_text(
            re.compile(r"Test,t@x\.com,40,.*,.*,UK"), timeout=3000
        )

    @pytest.mark.spec("V22.19")
    def test_combobox_saves(self, view_page: Page):
        """ComboBox value via binder write_bean."""
        # Re-read to get Zara's data (city=London)
        view_page.locator("#reread").click()
        view_page.wait_for_timeout(200)
        # Save — city should be London from Zara's data
        _type_in_field(view_page, "#name", "Test")
        _type_in_field(view_page, "#email", "t@x.com")
        _type_in_field(view_page, "#age", "25")
        view_page.locator("#save").click()
        expect(view_page.locator("#binder-result")).to_have_text(
            re.compile(r"London"), timeout=3000
        )


class TestBinderReread:
    @pytest.mark.spec("V22.20")
    def test_read_bean_after_write(self, view_page: Page):
        """After write_bean, read_bean with different person updates fields."""
        # First fill and save
        _type_in_field(view_page, "#name", "First")
        _type_in_field(view_page, "#email", "f@x.com")
        _type_in_field(view_page, "#age", "20")
        view_page.locator("#save").click()
        view_page.wait_for_timeout(200)
        # Now re-read with different person
        view_page.locator("#reread").click()
        view_page.wait_for_timeout(200)
        expect(view_page.locator("#name")).to_have_js_property("value", "Zara")
        expect(view_page.locator("#email")).to_have_js_property("value", "zara@x.com")
        expect(view_page.locator("#age")).to_have_js_property("value", "40")

    @pytest.mark.spec("V22.21")
    def test_clear_all_via_read_bean_none(self, view_page: Page):
        """read_bean(None) clears all fields and dirty is false."""
        # First make dirty
        _type_in_field(view_page, "#name", "Dirty")
        # Clear
        view_page.locator("#clear").click()
        view_page.wait_for_timeout(200)
        expect(view_page.locator("#name")).to_have_js_property("value", "")
        expect(view_page.locator("#email")).to_have_js_property("value", "")
        expect(view_page.locator("#age")).to_have_js_property("value", "")
        # Restore for nav test
        view_page.locator("#reread").click()
        view_page.wait_for_timeout(200)


class TestRemoveBinding:
    """Runs AFTER field type and re-read tests since it permanently removes a binding."""

    @pytest.mark.spec("V22.13")
    def test_remove_binding(self, view_page: Page):
        """After removing name binding, name changes are NOT written to bean."""
        # Re-read to reset
        view_page.locator("#reread").click()
        view_page.wait_for_timeout(200)
        # Remove the name binding
        view_page.locator("#remove-binding").click()
        view_page.wait_for_timeout(100)
        # Change name to something different
        _type_in_field(view_page, "#name", "Ignored")
        # Fill valid data for other fields
        _type_in_field(view_page, "#email", "z@x.com")
        _type_in_field(view_page, "#age", "40")
        view_page.locator("#save").click()
        # Name should NOT be "Ignored" — binding was removed, write_bean skips it
        result = view_page.locator("#binder-result")
        expect(result).not_to_have_text(re.compile(r"^Ignored,"), timeout=3000)


class TestNavigation:
    @pytest.mark.spec("V22.23")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/navigation']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/navigation"), timeout=5000)
