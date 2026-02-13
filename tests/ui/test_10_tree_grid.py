"""UI Tests — View 10: TreeGrid (/test/tree-grid)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/tree-grid", "vaadin-grid")
    yield shared_page


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
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/push']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/push"), timeout=5000)
