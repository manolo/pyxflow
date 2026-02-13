"""UI Tests — View 17: Upload (/test/upload)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/upload")
    p.wait_for_selector("vaadin-upload", timeout=15000)
    yield p
    ctx.close()


class TestUpload:
    def test_renders(self, view_page: Page):
        upload = view_page.locator("#upload1")
        expect(upload).to_be_visible()

    def test_max_files(self, view_page: Page):
        upload = view_page.locator("#upload1")
        expect(upload).to_have_js_property("maxFiles", 2)

    def test_accepted_file_types(self, view_page: Page):
        upload = view_page.locator("#upload1")
        expect(upload).to_have_js_property("accept", ".txt,.csv")

    def test_auto_upload_disabled(self, view_page: Page):
        upload = view_page.locator("#upload-manual")
        expect(upload).to_have_js_property("noAuto", True)


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/display"), timeout=5000)
