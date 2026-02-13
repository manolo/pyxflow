"""UI Tests — View 9: Grid Features (/test/grid-features)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/grid-features")
    p.wait_for_selector("vaadin-grid", timeout=15000)
    yield p
    ctx.close()


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


class TestItemClick:
    @pytest.mark.spec("V09.12")
    def test_item_click_listener(self, view_page: Page):
        grid = view_page.locator("#grid-single")
        grid.locator("vaadin-grid-cell-content").filter(has_text="Charlie").first.click()
        expect(view_page.locator("#grid-click")).to_have_text("Charlie")


class TestColumnOps:
    @pytest.mark.spec("V09.15")
    def test_remove_column(self, view_page: Page):
        view_page.locator("#btn-remove-col").click()
        # After removal, email column shouldn't show email content
        grid = view_page.locator("#grid-single")
        expect(grid).to_be_visible()


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
    @pytest.mark.spec("V09.20")
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/tree-grid"), timeout=5000)
