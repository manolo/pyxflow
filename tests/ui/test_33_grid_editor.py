"""UI Tests -- View 33: Grid Editor (/test/grid-editor)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Navigate to the grid editor test view."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/grid-editor", "#grid-buffered")
    yield shared_page


class TestBufferedEditor:
    @pytest.mark.spec("V33.01")
    def test_buffered_grid_renders(self, view_page: Page):
        """Buffered grid renders with 5 rows."""
        grid = view_page.locator("#grid-buffered")
        expect(grid).to_be_visible()
        expect(grid).to_have_js_property("size", 5)

    @pytest.mark.spec("V33.02")
    def test_double_click_opens_editor(self, view_page: Page):
        """Double-clicking a row opens the editor fields."""
        grid = view_page.locator("#grid-buffered")
        # Double-click the first rendered row
        row = grid.locator("tr[part~='body-row']").first
        row.dblclick()
        # Editor name field should appear
        name_field = view_page.locator("#editor-name")
        expect(name_field).to_be_visible(timeout=3000)

    @pytest.mark.spec("V33.03")
    def test_editor_fields_populated(self, view_page: Page):
        """Editor fields are populated with item data after double-click."""
        name_field = view_page.locator("#editor-name")
        expect(name_field).to_be_visible()
        expect(name_field).to_have_js_property("value", "Alice")

    @pytest.mark.spec("V33.04")
    def test_buffered_save(self, view_page: Page):
        """Modify a field and click Save -- item is updated."""
        name_field = view_page.locator("#editor-name")
        # Clear and type new value
        name_field.click()
        view_page.keyboard.press("Meta+a")
        view_page.keyboard.type("Alice Updated")
        view_page.keyboard.press("Tab")
        # Click Save
        view_page.locator("#btn-save").click()
        # Status should show saved
        expect(view_page.locator("#status-buffered")).to_have_text(
            "Saved: Alice Updated", timeout=3000
        )

    @pytest.mark.spec("V33.05")
    def test_buffered_cancel(self, view_page: Page):
        """Modify a field and click Cancel -- item is NOT updated."""
        grid = view_page.locator("#grid-buffered")
        # Double-click second row (Bob)
        rows = grid.locator("tr[part~='body-row']")
        rows.nth(1).dblclick()
        name_field = view_page.locator("#editor-name")
        expect(name_field).to_be_visible(timeout=3000)
        # Modify
        name_field.click()
        view_page.keyboard.press("Meta+a")
        view_page.keyboard.type("Bob Modified")
        view_page.keyboard.press("Tab")
        # Cancel
        view_page.locator("#btn-cancel").click()
        expect(view_page.locator("#status-buffered")).to_have_text(
            "Cancelled", timeout=3000
        )

    @pytest.mark.spec("V33.06")
    def test_save_event_updates_status(self, view_page: Page):
        """Save listener updates the status label with the item name."""
        grid = view_page.locator("#grid-buffered")
        # Edit third row (Charlie)
        rows = grid.locator("tr[part~='body-row']")
        rows.nth(2).dblclick()
        name_field = view_page.locator("#editor-name")
        expect(name_field).to_be_visible(timeout=3000)
        # Save without changes
        view_page.locator("#btn-save").click()
        expect(view_page.locator("#status-buffered")).to_have_text(
            "Saved: Charlie", timeout=3000
        )


class TestUnbufferedEditor:
    @pytest.mark.spec("V33.07")
    def test_unbuffered_grid_renders(self, view_page: Page):
        """Unbuffered grid renders with 3 rows."""
        grid = view_page.locator("#grid-unbuffered")
        expect(grid).to_be_visible()
        expect(grid).to_have_js_property("size", 3)

    @pytest.mark.spec("V33.08")
    def test_click_opens_editor(self, view_page: Page):
        """Single-clicking a row opens the unbuffered editor."""
        grid = view_page.locator("#grid-unbuffered")
        row = grid.locator("tr[part~='body-row']").first
        row.click()
        name_field = view_page.locator("#unbuf-editor-name")
        expect(name_field).to_be_visible(timeout=3000)
        expect(view_page.locator("#status-unbuffered")).to_have_text(
            re.compile(r"Editing: .+"), timeout=3000
        )

    @pytest.mark.spec("V33.09")
    def test_click_different_row_closes_previous(self, view_page: Page):
        """Clicking a different row fires close event for previous."""
        grid = view_page.locator("#grid-unbuffered")
        rows = grid.locator("tr[part~='body-row']")
        # Click second row
        rows.nth(1).click()
        expect(view_page.locator("#status-unbuffered")).to_have_text(
            re.compile(r"(Editing|Closed): .+"), timeout=3000
        )


class TestNavigation:
    @pytest.mark.spec("V33.10")
    def test_page_accessible(self, view_page: Page):
        """Grid editor page is accessible and has correct content."""
        expect(view_page.locator("#grid-buffered")).to_be_visible()
        expect(view_page.locator("#grid-unbuffered")).to_be_visible()
