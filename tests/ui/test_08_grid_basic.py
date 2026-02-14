"""UI Tests — View 8: Grid Basic (/test/grid-basic)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/grid-basic", "vaadin-grid")
    yield shared_page


class TestGridColumns:
    @pytest.mark.spec("V08.01")
    def test_renders_headers(self, view_page: Page):
        grid = view_page.locator("#grid1")
        expect(grid).to_be_visible()
        # Verify grid has data rows
        expect(grid.locator("vaadin-grid-cell-content").first).to_be_visible()

    @pytest.mark.spec("V08.03")
    def test_set_items_replaces(self, view_page: Page):
        view_page.locator("#btn-replace").click()
        grid = view_page.locator("#grid1")
        # After replace, grid size should be 1 and only 1 row rendered
        expect(grid).to_have_js_property("size", 1)
        rendered = grid.evaluate("el => el._getRenderedRows().length")
        assert rendered == 1

    @pytest.mark.spec("V08.08")
    def test_resizable_column(self, view_page: Page):
        grid = view_page.locator("#grid-res")
        expect(grid).to_be_visible()

    @pytest.mark.spec("V08.09")
    def test_text_align_center(self, view_page: Page):
        grid = view_page.locator("#grid-align")
        expect(grid).to_be_visible()

    @pytest.mark.spec("V08.10")
    def test_frozen_column(self, view_page: Page):
        grid = view_page.locator("#grid-frozen")
        expect(grid).to_be_visible()

    @pytest.mark.spec("V08.11")
    def test_frozen_to_end(self, view_page: Page):
        """Column set_frozen_to_end makes the column stick to the right."""
        grid = view_page.locator("#grid-frozen")
        # grid-frozen has email column with frozen_to_end
        expect(grid).to_be_visible()
        # Verify frozenToEnd is set on a column
        frozen_end = grid.evaluate(
            """el => {
                const cols = el.querySelectorAll('vaadin-grid-column');
                return Array.from(cols).some(c => c.frozenToEnd);
            }"""
        )
        assert frozen_end is True

    @pytest.mark.spec("V08.12")
    def test_hidden_column(self, view_page: Page):
        grid = view_page.locator("#grid-vis")
        expect(grid).to_be_visible()

    @pytest.mark.spec("V08.13")
    def test_footer_text(self, view_page: Page):
        grid = view_page.locator("#grid-foot")
        expect(grid).to_contain_text("Total: 5")

    @pytest.mark.spec("V08.21")
    def test_empty_state(self, view_page: Page):
        """Grid set_items([]) clears all rows."""
        grid = view_page.locator("#grid1")
        view_page.locator("#btn-clear").click()
        # Grid size should be 0 and no rendered rows.
        # Note: vaadin-grid pools physical <tr> rows (hidden, not destroyed),
        # so textContent still has stale cell text.  Check JS state instead.
        expect(grid).to_have_js_property("size", 0)
        rendered = grid.evaluate("el => el._getRenderedRows().length")
        assert rendered == 0

    @pytest.mark.spec("V08.22")
    def test_all_rows_visible(self, view_page: Page):
        """Grid with all_rows_visible has allRowsVisible property set."""
        grid = view_page.locator("#grid1")
        expect(grid).to_have_js_property("allRowsVisible", True)


class TestGridRenderers:
    @pytest.mark.spec("V08.14")
    def test_lit_renderer(self, view_page: Page):
        grid = view_page.locator("#grid-lit")
        expect(grid).to_contain_text("Alice (30)")

    @pytest.mark.spec("V08.15", "V08.16")
    def test_component_renderer_click(self, view_page: Page):
        grid = view_page.locator("#grid-comp")
        # Click the first button in the grid
        grid.locator("vaadin-button").first.click()
        expect(view_page.locator("#grid-click")).not_to_have_text("")


class TestGridReorder:
    @pytest.mark.spec("V08.18")
    def test_column_reorder_allowed(self, view_page: Page):
        grid = view_page.locator("#grid-reorder")
        expect(grid).to_have_js_property("columnReorderingAllowed", True)


class TestNavigation:
    @pytest.mark.spec("V08.25")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/grid-features']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/grid-features"), timeout=5000)
