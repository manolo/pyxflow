"""UI Tests — View 15: Layouts (/test/layouts)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/layouts")
    p.wait_for_selector("vaadin-vertical-layout", timeout=15000)
    yield p
    ctx.close()


class TestVerticalLayout:
    def test_renders_children(self, view_page: Page):
        vl = view_page.locator("#vl1")
        expect(vl).to_contain_text("A")
        expect(vl).to_contain_text("B")
        expect(vl).to_contain_text("C")

    def test_expand(self, view_page: Page):
        child = view_page.locator("#child-expand")
        expect(child).to_be_visible()

    def test_add_dynamically(self, view_page: Page):
        view_page.locator("#btn-add-span").click()
        vl = view_page.locator("#vl-dyn")
        expect(vl).to_contain_text("New")

    def test_replace(self, view_page: Page):
        view_page.locator("#btn-replace").click()
        vl = view_page.locator("#vl-replace")
        expect(vl).to_contain_text("Replaced")


class TestHorizontalLayout:
    def test_renders_children(self, view_page: Page):
        hl = view_page.locator("#hl1")
        expect(hl).to_contain_text("L")
        expect(hl).to_contain_text("R")

    def test_expand(self, view_page: Page):
        expect(view_page.locator("#hl-child")).to_be_visible()


class TestFlexLayout:
    def test_column_direction(self, view_page: Page):
        fl = view_page.locator("#fl1")
        expect(fl).to_be_visible()

    def test_wrap(self, view_page: Page):
        fl = view_page.locator("#fl-wrap")
        expect(fl).to_be_visible()


class TestFormLayout:
    def test_renders_fields(self, view_page: Page):
        form = view_page.locator("#form1")
        expect(form.locator("vaadin-text-field")).to_have_count(4)


class TestSplitLayout:
    def test_renders_panels(self, view_page: Page):
        split = view_page.locator("#split1")
        expect(split).to_contain_text("Primary")
        expect(split).to_contain_text("Secondary")


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/card-scroller"), timeout=5000)
