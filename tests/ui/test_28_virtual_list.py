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

    @pytest.mark.spec("V28.05")
    def test_replace_items(self, view_page: Page):
        view_page.locator("#btn-vl-replace").click()
        vl = view_page.locator("#vl1")
        expect(vl).to_contain_text("New 0")


class TestNavigation:
    @pytest.mark.spec("V28.08")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/login']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/login"), timeout=5000)
