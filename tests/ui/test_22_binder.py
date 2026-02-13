"""UI Tests — View 22: Binder (/test/binder)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/binder")
    p.wait_for_selector("vaadin-text-field", timeout=15000)
    yield p
    ctx.close()


def _type_in_field(page: Page, selector: str, text: str):
    """Click a field, clear it, type new text, then Tab to trigger change event."""
    page.locator(selector).click()
    # Select all existing text and delete it first (Meta+a for macOS, Control+a for Linux)
    page.keyboard.press("Meta+a")
    page.keyboard.press("Backspace")
    if text:
        page.keyboard.type(text)
    page.keyboard.press("Tab")
    # Allow mSync round-trip to propagate the value to the server
    page.wait_for_timeout(1000)


class TestReadBean:
    @pytest.mark.spec("V22.01")
    def test_populates_fields(self, view_page: Page):
        expect(view_page.locator("#name")).to_have_js_property("value", "Alice")
        expect(view_page.locator("#email")).to_have_js_property("value", "alice@x.com")
        expect(view_page.locator("#age")).to_have_js_property("value", "30")


class TestWriteBean:
    @pytest.mark.spec("V22.03")
    def test_writes_form_to_object(self, view_page: Page):
        _type_in_field(view_page, "#name", "Bob")
        _type_in_field(view_page, "#email", "bob@x.com")
        _type_in_field(view_page, "#age", "25")
        view_page.locator("#save").click()
        expect(view_page.locator("#binder-result")).to_have_text("Bob,bob@x.com,25")


class TestValidation:
    @pytest.mark.spec("V22.04")
    def test_required_blocks_save(self, view_page: Page):
        _type_in_field(view_page, "#name", "")
        view_page.locator("#save").click()
        expect(view_page.locator("#name")).to_have_js_property("invalid", True)

    @pytest.mark.spec("V22.07")
    def test_valid_saves(self, view_page: Page):
        _type_in_field(view_page, "#name", "Valid")
        _type_in_field(view_page, "#email", "v@x.com")
        _type_in_field(view_page, "#age", "20")
        view_page.locator("#save").click()
        expect(view_page.locator("#binder-result")).to_have_text("Valid,v@x.com,20")


class TestDirtyTracking:
    @pytest.mark.spec("V22.09")
    def test_dirty_after_change(self, view_page: Page):
        _type_in_field(view_page, "#name", "Changed")
        expect(view_page.locator("#dirty")).to_have_text("true")


class TestNavigation:
    @pytest.mark.spec("V22.15")
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/navigation"), timeout=5000)
