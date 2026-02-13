"""UI Tests — View 18: Display Components (/test/display)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/display", "vaadin-progress-bar")
    yield shared_page


class TestProgressBar:
    @pytest.mark.spec("V18.01")
    def test_renders_with_value(self, view_page: Page):
        pb = view_page.locator("#pb1")
        expect(pb).to_have_js_property("value", 0.6)

    @pytest.mark.spec("V18.02")
    def test_update_value(self, view_page: Page):
        view_page.locator("#btn-pb").click()
        expect(view_page.locator("#pb1")).to_have_js_property("value", 0.9)

    @pytest.mark.spec("V18.03")
    def test_indeterminate(self, view_page: Page):
        expect(view_page.locator("#pb-ind")).to_have_js_property("indeterminate", True)

    @pytest.mark.spec("V18.04")
    def test_min_max(self, view_page: Page):
        pb = view_page.locator("#pb-range")
        expect(pb).to_have_js_property("min", 0)
        expect(pb).to_have_js_property("max", 200)
        expect(pb).to_have_js_property("value", 100)


class TestAvatar:
    @pytest.mark.spec("V18.05")
    def test_renders_with_name(self, view_page: Page):
        av = view_page.locator("#av1")
        expect(av).to_have_js_property("name", "Sophia Williams")

    @pytest.mark.spec("V18.06")
    def test_abbreviation(self, view_page: Page):
        expect(view_page.locator("#av-abbr")).to_have_js_property("abbr", "JD")

    @pytest.mark.spec("V18.08")
    def test_color_index(self, view_page: Page):
        expect(view_page.locator("#av-color")).to_have_js_property("colorIndex", 3)


class TestAvatarGroup:
    @pytest.mark.spec("V18.09")
    def test_renders_items(self, view_page: Page):
        ag = view_page.locator("#ag1")
        expect(ag).to_be_visible()

    @pytest.mark.spec("V18.10")
    def test_max_items_visible(self, view_page: Page):
        ag = view_page.locator("#ag-max")
        expect(ag).to_have_js_property("maxItemsVisible", 3)


class TestMarkdown:
    @pytest.mark.spec("V18.11")
    def test_renders_content(self, view_page: Page):
        md = view_page.locator("#md1")
        expect(md).to_contain_text("Hello")

    @pytest.mark.spec("V18.12")
    def test_update_content(self, view_page: Page):
        view_page.locator("#btn-md").click()
        expect(view_page.locator("#md1")).to_contain_text("Updated")


class TestMessageInput:
    @pytest.mark.spec("V18.13")
    def test_renders(self, view_page: Page):
        mi = view_page.locator("#mi1")
        expect(mi).to_be_visible()


class TestMessageList:
    @pytest.mark.spec("V18.15")
    def test_renders_items(self, view_page: Page):
        ml = view_page.locator("#ml1")
        expect(ml).to_contain_text("Hi")
        expect(ml).to_contain_text("Alice")

    @pytest.mark.spec("V18.16")
    def test_multiple_messages(self, view_page: Page):
        ml = view_page.locator("#ml1")
        expect(ml).to_contain_text("Hello")
        expect(ml).to_contain_text("Bob")


class TestNavigation:
    @pytest.mark.spec("V18.17")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/layouts']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/layouts"), timeout=5000)
