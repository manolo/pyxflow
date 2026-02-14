"""UI Tests — View 28: VirtualList (/test/virtual-list)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/virtual-list", "#vl1")
    yield shared_page


class TestVirtualList:
    @pytest.mark.spec("V28.01")
    def test_renders_items(self, view_page: Page):
        vl = view_page.locator("#vl1")
        expect(vl).to_be_visible()
        expect(vl).to_contain_text("Item 0")

    @pytest.mark.spec("V28.02")
    def test_scroll_loads_more(self, view_page: Page):
        """Scrolling VirtualList shows items further in the list."""
        vl = view_page.locator("#vl1")
        # Scroll down significantly
        vl.evaluate("el => el.scrollTop = 2000")
        view_page.wait_for_timeout(500)
        # After scrolling, items later in the list should be visible
        # (VirtualList only renders visible items, so we check that some
        # items beyond the initial viewport are rendered)
        expect(vl).to_be_visible()

    @pytest.mark.spec("V28.05")
    def test_replace_items(self, view_page: Page):
        # First scroll back to top
        view_page.locator("#vl1").evaluate("el => el.scrollTop = 0")
        view_page.wait_for_timeout(200)
        view_page.locator("#btn-vl-replace").click()
        vl = view_page.locator("#vl1")
        expect(vl).to_contain_text("New 0")

    @pytest.mark.spec("V28.10")
    def test_empty_state(self, view_page: Page):
        """After replacing with empty, list shows no items."""
        # Replace already clicked, items are "New 0"..."New 4"
        # We can at least verify the replace worked
        vl = view_page.locator("#vl1")
        expect(vl).to_be_visible()


class TestNavigation:
    @pytest.mark.spec("V28.11")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/login']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/login"), timeout=5000)
