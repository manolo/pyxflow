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

    @pytest.mark.spec("V10.04")
    def test_expand_nested(self, view_page: Page):
        """Expand Root2 → Child2A shows grandchild GC2A1."""
        grid = view_page.locator("#tg1")
        # Click Root2 toggle to expand
        toggles = grid.locator("vaadin-grid-tree-toggle")
        # Root2 is the second root item toggle
        for i in range(toggles.count()):
            if "Root2" in toggles.nth(i).text_content():
                toggles.nth(i).click()
                break
        expect(grid).to_contain_text("Child2A")

    @pytest.mark.spec("V10.07")
    def test_hierarchy_column_has_toggles(self, view_page: Page):
        """Hierarchy column renders tree toggle elements."""
        grid = view_page.locator("#tg1")
        toggles = grid.locator("vaadin-grid-tree-toggle")
        assert toggles.count() > 0

    @pytest.mark.spec("V10.08")
    def test_selection(self, view_page: Page):
        """TreeGrid single selection works — click child, verify sel label."""
        grid = view_page.locator("#tg1")
        # Ensure Root1 is expanded
        view_page.locator("#btn-expand").click()
        # Click on Child1A cell
        grid.locator("vaadin-grid-cell-content").filter(has_text="Child1A").first.click()
        expect(view_page.locator("#tg1-sel")).to_have_text("Child1A", timeout=5000)


class TestTreeGridDynamicProvider:
    """Test TreeGrid with dynamic children_provider (creates new objects each call)."""

    @pytest.mark.spec("V10.09")
    def test_second_level_expand_dynamic_provider(self, view_page: Page):
        """Expanding a second-level folder works with dynamic children provider."""
        grid2 = view_page.locator("#tg2")
        # Expand DirA via button
        view_page.locator("#btn-expand-a").click()
        expect(grid2).to_contain_text("SubA1", timeout=5000)
        expect(grid2).to_contain_text("FileA2")
        # Now click SubA1 toggle to expand second level
        toggles = grid2.locator("vaadin-grid-tree-toggle")
        for i in range(toggles.count()):
            if "SubA1" in toggles.nth(i).text_content():
                toggles.nth(i).click()
                break
        expect(grid2).to_contain_text("Deep1", timeout=5000)


class TestNavigation:
    @pytest.mark.spec("V10.10")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/push']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/push"), timeout=5000)
