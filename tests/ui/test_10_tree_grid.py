"""UI Tests — View 10: TreeGrid (/test/tree-grid)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/tree-grid")
    p.wait_for_selector("vaadin-grid", timeout=15000)
    yield p
    ctx.close()


class TestTreeGrid:
    @pytest.mark.spec("V10.01")
    def test_renders_root_items(self, view_page: Page):
        grid = view_page.locator("#tg1")
        expect(grid).to_contain_text("Root1")
        expect(grid).to_contain_text("Root2")

    @pytest.mark.spec("V10.05")
    def test_expand_programmatic(self, view_page: Page):
        view_page.locator("#btn-expand").click()
        grid = view_page.locator("#tg1")
        expect(grid).to_contain_text("Child1A")
        expect(grid).to_contain_text("Child1B")

    @pytest.mark.spec("V10.06")
    def test_collapse_programmatic(self, view_page: Page):
        view_page.locator("#btn-collapse").click()
        grid = view_page.locator("#tg1")
        # After collapse, children should not be visible
        expect(grid.locator("vaadin-grid-cell-content").filter(has_text="Child1A")).to_have_count(0)

    @pytest.mark.spec("V10.02", "V10.03")
    def test_expand_collapse_flow(self, view_page: Page):
        # Expand again to verify toggle works
        view_page.locator("#btn-expand").click()
        grid = view_page.locator("#tg1")
        expect(grid).to_contain_text("Child1A")


class TestNavigation:
    @pytest.mark.spec("V10.10")
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/dialog"), timeout=5000)
