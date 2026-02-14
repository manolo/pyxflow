"""UI Tests — View 23: Navigation (/test/navigation)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/navigation", "#nav-title")
    yield shared_page


class TestRouting:
    @pytest.mark.spec("V23.01")
    def test_view_renders(self, view_page: Page):
        expect(view_page.locator("#nav-title")).to_have_text("Navigation view")

    @pytest.mark.spec("V23.04")
    def test_page_title(self, view_page: Page):
        title = view_page.evaluate("() => document.title")
        assert "Navigation" in title

    @pytest.mark.spec("V23.05")
    def test_route_page_title_param(self, view_page: Page):
        """@Route page_title parameter sets document.title."""
        title = view_page.evaluate("() => document.title")
        assert "Navigation" in title


class TestRouteParam:
    @pytest.mark.spec("V23.02")
    def test_param_route(self, view_page: Page):
        view_page.locator("#link-param").click()
        expect(view_page).to_have_url(re.compile(r".*/test/nav-param/42"), timeout=5000)
        expect(view_page.locator("#param")).to_have_text("42")
        view_page.locator("#nav-back").click()
        expect(view_page).to_have_url(re.compile(r".*/test/navigation"), timeout=5000)


class TestOptionalParam:
    @pytest.mark.spec("V23.03")
    def test_opt_param_empty(self, view_page: Page):
        view_page.locator("#link-opt").click()
        expect(view_page).to_have_url(re.compile(r".*/test/nav-opt$"), timeout=5000)
        expect(view_page.locator("#opt")).to_have_text("")
        view_page.locator("#nav-back").click()
        expect(view_page).to_have_url(re.compile(r".*/test/navigation"), timeout=5000)

    @pytest.mark.spec("V23.03")
    def test_opt_param_value(self, view_page: Page):
        view_page.locator("#link-opt-val").click()
        expect(view_page).to_have_url(re.compile(r".*/test/nav-opt/search"), timeout=5000)
        expect(view_page.locator("#opt")).to_have_text("search")
        view_page.locator("#nav-back").click()
        expect(view_page).to_have_url(re.compile(r".*/test/navigation"), timeout=5000)


class TestRouterLink:
    @pytest.mark.spec("V23.06")
    def test_router_link_navigates_without_reload(self, view_page: Page):
        """RouterLink performs client-side navigation (no full reload)."""
        # Set a marker on window to detect full reload
        view_page.evaluate("window.__nav_test_marker = true")
        view_page.locator("#link-param").click()
        expect(view_page).to_have_url(re.compile(r".*/test/nav-param/42"), timeout=5000)
        # Marker should still exist (no full reload)
        marker = view_page.evaluate("window.__nav_test_marker")
        assert marker is True, "Expected client-side navigation (no reload)"
        view_page.locator("#nav-back").click()
        expect(view_page).to_have_url(re.compile(r".*/test/navigation"), timeout=5000)


class TestSideNav:
    @pytest.mark.spec("V23.11")
    def test_sidenav_renders_items(self, view_page: Page):
        """SideNav renders navigation items."""
        nav = view_page.locator("vaadin-side-nav")
        expect(nav).to_be_visible()
        items = nav.locator("vaadin-side-nav-item")
        # Should have multiple items (one per test view)
        assert items.count() > 10

    @pytest.mark.spec("V23.12")
    def test_sidenav_item_click_navigates(self, view_page: Page):
        """Clicking a SideNav item navigates to that view."""
        view_page.locator("vaadin-side-nav-item[path='/test/binder']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/binder"), timeout=5000)
        # Navigate back
        view_page.locator("vaadin-side-nav-item[path='/test/navigation']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/navigation"), timeout=5000)


class TestNavigation:
    @pytest.mark.spec("V23.14")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/binder']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/binder"), timeout=5000)
