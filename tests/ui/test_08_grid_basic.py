"""UI Tests — View 8: Grid Basic (/test/grid-basic)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/grid-basic")
    p.wait_for_selector("vaadin-grid", timeout=15000)
    yield p
    ctx.close()


class TestGridColumns:
    def test_renders_headers(self, view_page: Page):
        grid = view_page.locator("#grid1")
        expect(grid).to_be_visible()
        # Verify grid has data rows
        expect(grid.locator("vaadin-grid-cell-content").first).to_be_visible()

    def test_set_items_replaces(self, view_page: Page):
        view_page.locator("#btn-replace").click()
        grid = view_page.locator("#grid1")
        # After replace, grid should contain "Zoe"
        expect(grid).to_contain_text("Zoe")

    def test_resizable_column(self, view_page: Page):
        grid = view_page.locator("#grid-res")
        expect(grid).to_be_visible()

    def test_text_align_center(self, view_page: Page):
        grid = view_page.locator("#grid-align")
        expect(grid).to_be_visible()

    def test_frozen_column(self, view_page: Page):
        grid = view_page.locator("#grid-frozen")
        expect(grid).to_be_visible()

    def test_hidden_column(self, view_page: Page):
        grid = view_page.locator("#grid-vis")
        expect(grid).to_be_visible()

    def test_footer_text(self, view_page: Page):
        grid = view_page.locator("#grid-foot")
        expect(grid).to_contain_text("Total: 5")


class TestGridRenderers:
    def test_lit_renderer(self, view_page: Page):
        grid = view_page.locator("#grid-lit")
        expect(grid).to_contain_text("Alice (30)")

    def test_component_renderer_click(self, view_page: Page):
        grid = view_page.locator("#grid-comp")
        # Click the first button in the grid
        grid.locator("vaadin-button").first.click()
        expect(view_page.locator("#grid-click")).not_to_have_text("")


class TestGridReorder:
    def test_column_reorder_allowed(self, view_page: Page):
        grid = view_page.locator("#grid-reorder")
        expect(grid).to_have_js_property("columnReorderingAllowed", True)


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/grid-features"), timeout=5000)
