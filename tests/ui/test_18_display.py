"""UI Tests — View 18: Display Components (/test/display)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/display")
    p.wait_for_selector("vaadin-progress-bar", timeout=15000)
    yield p
    ctx.close()


class TestProgressBar:
    def test_renders_with_value(self, view_page: Page):
        pb = view_page.locator("#pb1")
        expect(pb).to_have_js_property("value", 0.6)

    def test_update_value(self, view_page: Page):
        view_page.locator("#btn-pb").click()
        expect(view_page.locator("#pb1")).to_have_js_property("value", 0.9)

    def test_indeterminate(self, view_page: Page):
        expect(view_page.locator("#pb-ind")).to_have_js_property("indeterminate", True)

    def test_min_max(self, view_page: Page):
        pb = view_page.locator("#pb-range")
        expect(pb).to_have_js_property("min", 0)
        expect(pb).to_have_js_property("max", 200)
        expect(pb).to_have_js_property("value", 100)


class TestAvatar:
    def test_renders_with_name(self, view_page: Page):
        av = view_page.locator("#av1")
        expect(av).to_have_js_property("name", "Sophia Williams")

    def test_abbreviation(self, view_page: Page):
        expect(view_page.locator("#av-abbr")).to_have_js_property("abbr", "JD")

    def test_color_index(self, view_page: Page):
        expect(view_page.locator("#av-color")).to_have_js_property("colorIndex", 3)


class TestAvatarGroup:
    def test_renders_items(self, view_page: Page):
        ag = view_page.locator("#ag1")
        expect(ag).to_be_visible()

    def test_max_items_visible(self, view_page: Page):
        ag = view_page.locator("#ag-max")
        expect(ag).to_have_js_property("maxItemsVisible", 3)


class TestMarkdown:
    def test_renders_content(self, view_page: Page):
        md = view_page.locator("#md1")
        expect(md).to_contain_text("Hello")

    def test_update_content(self, view_page: Page):
        view_page.locator("#btn-md").click()
        expect(view_page.locator("#md1")).to_contain_text("Updated")


class TestMessageInput:
    def test_renders(self, view_page: Page):
        mi = view_page.locator("#mi1")
        expect(mi).to_be_visible()


class TestMessageList:
    def test_renders_items(self, view_page: Page):
        ml = view_page.locator("#ml1")
        expect(ml).to_contain_text("Hi")
        expect(ml).to_contain_text("Alice")

    def test_multiple_messages(self, view_page: Page):
        ml = view_page.locator("#ml1")
        expect(ml).to_contain_text("Hello")
        expect(ml).to_contain_text("Bob")


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/html-elements"), timeout=5000)
