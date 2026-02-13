"""UI Tests — View 17: Upload (/test/upload)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/upload", "vaadin-upload")
    yield shared_page


class TestUpload:
    @pytest.mark.spec("V17.01")
    def test_renders(self, view_page: Page):
        upload = view_page.locator("#upload1")
        expect(upload).to_be_visible()

    @pytest.mark.spec("V17.03")
    def test_max_files(self, view_page: Page):
        upload = view_page.locator("#upload1")
        expect(upload).to_have_js_property("maxFiles", 2)

    @pytest.mark.spec("V17.05")
    def test_accepted_file_types(self, view_page: Page):
        upload = view_page.locator("#upload1")
        expect(upload).to_have_js_property("accept", ".txt,.csv")

    @pytest.mark.spec("V17.06")
    def test_auto_upload_disabled(self, view_page: Page):
        upload = view_page.locator("#upload-manual")
        expect(upload).to_have_js_property("noAuto", True)


class TestNavigation:
    @pytest.mark.spec("V17.10")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/tree-grid']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/tree-grid"), timeout=5000)
