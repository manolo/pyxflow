"""UI Tests — View 27: CustomField (/test/custom-field)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/custom-field", "vaadin-custom-field")
    yield shared_page


class TestCustomField:
    @pytest.mark.spec("V27.01")
    def test_renders_children(self, view_page: Page):
        cf = view_page.locator("#cf1")
        expect(cf.locator("vaadin-text-field")).to_have_count(2)

    @pytest.mark.spec("V27.02")
    def test_label(self, view_page: Page):
        expect(view_page.locator("#cf1")).to_have_js_property("label", "Full Name")

    @pytest.mark.spec("V27.05")
    def test_read_only(self, view_page: Page):
        expect(view_page.locator("#cf-ro")).to_have_js_property("readonly", True)

    @pytest.mark.spec("V27.06")
    def test_invalid(self, view_page: Page):
        view_page.locator("#btn-cf-inv").click()
        expect(view_page.locator("#cf-inv")).to_have_js_property("invalid", True)
        expect(view_page.locator("#cf-inv")).to_have_js_property(
            "errorMessage", "Invalid name"
        )

    @pytest.mark.spec("V27.07")
    def test_required(self, view_page: Page):
        expect(view_page.locator("#cf-req")).to_have_js_property("required", True)


class TestNavigation:
    @pytest.mark.spec("V27.08")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/virtual-list']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/virtual-list"), timeout=5000)
