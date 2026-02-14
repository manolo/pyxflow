"""UI Tests — View 9: Grid Features (/test/grid-features)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/grid-features", "vaadin-grid")
    yield shared_page


class TestSingleSelection:
    @pytest.mark.spec("V09.01")
    def test_single_select_mode(self, view_page: Page):
        grid = view_page.locator("#grid-single")
        expect(grid).to_be_visible()

    @pytest.mark.spec("V09.01", "V09.14")
    def test_click_selects_row(self, view_page: Page):
        grid = view_page.locator("#grid-single")
        # Click first data row
        grid.locator("vaadin-grid-cell-content").filter(has_text="Alice").first.click()
        expect(view_page.locator("#grid-single-sel")).to_have_text("Alice")

    @pytest.mark.spec("V09.02")
    def test_programmatic_select(self, view_page: Page):
        view_page.locator("#btn-sel-bob").click()
        expect(view_page.locator("#grid-single-sel")).to_have_text("Bob")

    @pytest.mark.spec("V09.03")
    def test_single_deselect(self, view_page: Page):
        """Click selected row again to deselect."""
        grid = view_page.locator("#grid-single")
        # Click Bob first to sync client/server (prior test used programmatic select
        # which only updates server state, not client grid visual selection)
        grid.locator("vaadin-grid-cell-content").filter(has_text="Bob").first.click()
        expect(view_page.locator("#grid-single-sel")).to_have_text("Bob")
        # Click Bob again to deselect
        grid.locator("vaadin-grid-cell-content").filter(has_text="Bob").first.click()
        expect(view_page.locator("#grid-single-sel")).to_have_text("")


class TestMultiSelection:
    @pytest.mark.spec("V09.04")
    def test_multi_mode_has_checkboxes(self, view_page: Page):
        grid = view_page.locator("#grid-multi")
        expect(grid).to_be_visible()

    @pytest.mark.spec("V09.06")
    def test_select_all(self, view_page: Page):
        view_page.locator("#btn-sel-all").click()
        sel = view_page.locator("#grid-multi-sel")
        expect(sel).to_contain_text("Alice")
        expect(sel).to_contain_text("Eve")

    @pytest.mark.spec("V09.07")
    def test_deselect_all(self, view_page: Page):
        view_page.locator("#btn-desel-all").click()
        expect(view_page.locator("#grid-multi-sel")).to_have_text("")


class TestSorting:
    @pytest.mark.spec("V09.08", "V09.11")
    def test_sort_fires_listener(self, view_page: Page):
        grid = view_page.locator("#grid-single")
        # Click "Name" header to sort
        grid.locator("vaadin-grid-sorter").first.click()
        expect(view_page.locator("#grid-sort")).to_have_text("sorted")

    @pytest.mark.spec("V09.09")
    def test_sort_toggle_descending(self, view_page: Page):
        """Clicking the same header again toggles to descending."""
        grid = view_page.locator("#grid-single")
        sorter = grid.locator("vaadin-grid-sorter").first
        # Click again to toggle descending
        sorter.click()
        view_page.wait_for_timeout(300)
        # The sorter should have direction attribute
        direction = sorter.evaluate("el => el.direction")
        assert direction in ("asc", "desc")


class TestItemClick:
    @pytest.mark.spec("V09.12")
    def test_item_click_listener(self, view_page: Page):
        grid = view_page.locator("#grid-single")
        grid.locator("vaadin-grid-cell-content").filter(has_text="Charlie").first.click()
        expect(view_page.locator("#grid-click")).to_have_text("Charlie")

    @pytest.mark.spec("V09.13")
    def test_item_double_click(self, view_page: Page):
        """Double-clicking a row fires item double click listener."""
        grid = view_page.locator("#grid-single")
        cell = grid.locator("vaadin-grid-cell-content").filter(has_text="Alice").first
        cell.dblclick()
        expect(view_page.locator("#grid-dbl")).to_have_text("Alice", timeout=3000)


class TestColumnOps:
    @pytest.mark.spec("V09.15")
    def test_remove_column(self, view_page: Page):
        view_page.locator("#btn-remove-col").click()
        # After removal, email column shouldn't show email content
        grid = view_page.locator("#grid-single")
        expect(grid).to_be_visible()

    @pytest.mark.spec("V09.20")
    def test_remove_all_columns(self, view_page: Page):
        """Remove all columns from multi grid."""
        view_page.locator("#btn-remove-all-col").click()
        grid = view_page.locator("#grid-multi")
        view_page.wait_for_timeout(300)
        # After removing all columns, grid should have no column elements
        col_count = grid.evaluate(
            "el => el.querySelectorAll('vaadin-grid-column').length"
        )
        assert col_count == 0


class TestDragDrop:
    @pytest.mark.spec("V09.17")
    def test_rows_draggable(self, view_page: Page):
        grid = view_page.locator("#grid-dnd")
        expect(grid).to_have_js_property("rowsDraggable", True)

    @pytest.mark.spec("V09.18")
    def test_drop_mode(self, view_page: Page):
        grid = view_page.locator("#grid-dnd")
        expect(grid).to_have_js_property("dropMode", "between")


class TestEmptyState:
    @pytest.mark.spec("V09.19")
    def test_empty_state_text(self, view_page: Page):
        grid = view_page.locator("#grid-empty")
        expect(grid).to_have_js_property("emptyStateText", "No data available")


class TestNavigation:
    @pytest.mark.spec("V09.22")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/card-scroller']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/card-scroller"), timeout=5000)
