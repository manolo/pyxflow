"""UI Tests — View 16: Card, Scroller, MasterDetailLayout (/test/card-scroller)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/card-scroller", "vaadin-horizontal-layout")
    yield shared_page


class TestCard:
    @pytest.mark.spec("V16.01")
    def test_renders_title(self, view_page: Page):
        card = view_page.locator("#card1")
        expect(card).to_contain_text("My Card")

    @pytest.mark.spec("V16.02")
    def test_subtitle(self, view_page: Page):
        card = view_page.locator("#card1")
        expect(card).to_contain_text("Subtitle text")

    @pytest.mark.spec("V16.03")
    def test_body_content(self, view_page: Page):
        card = view_page.locator("#card1")
        expect(card).to_contain_text("Body text")

    @pytest.mark.spec("V16.04")
    def test_footer(self, view_page: Page):
        card = view_page.locator("#card1")
        expect(card.locator("vaadin-button")).to_contain_text("Action")


class TestScroller:
    @pytest.mark.spec("V16.07")
    def test_renders_content(self, view_page: Page):
        scroller = view_page.locator("#scroller1")
        expect(scroller).to_be_visible()
        expect(scroller).to_contain_text("Line 0")

    @pytest.mark.spec("V16.08")
    def test_horizontal_scroller(self, view_page: Page):
        scroller = view_page.locator("#scroller-h")
        expect(scroller).to_be_visible()


class TestMasterDetailLayout:
    @pytest.mark.spec("V16.10")
    def test_master_visible(self, view_page: Page):
        mdl = view_page.locator("#mdl1")
        expect(mdl.locator("#mdl-item-1")).to_be_visible()
        expect(mdl.locator("#mdl-item-2")).to_be_visible()

    @pytest.mark.spec("V16.11")
    def test_open_detail(self, view_page: Page):
        view_page.locator("#mdl-item-1").click()
        detail = view_page.locator("#mdl-detail")
        expect(detail).to_be_visible(timeout=5000)
        expect(detail).to_contain_text("Detail for item 1")

    @pytest.mark.spec("V16.12")
    def test_close_detail(self, view_page: Page):
        # Detail should still be open from previous test
        expect(view_page.locator("#mdl-detail")).to_be_visible()
        view_page.locator("#mdl-close").click()
        expect(view_page.locator("#mdl-detail")).to_be_hidden(timeout=5000)

    @pytest.mark.spec("V16.13")
    def test_switch_detail(self, view_page: Page):
        # Open item 2
        view_page.locator("#mdl-item-2").click()
        detail = view_page.locator("#mdl-detail")
        expect(detail).to_be_visible(timeout=5000)
        expect(detail).to_contain_text("Detail for item 2")
        # Switch to item 3
        view_page.locator("#mdl-item-3").click()
        expect(detail).to_contain_text("Detail for item 3", timeout=5000)
        # Close
        view_page.locator("#mdl-close").click()
        expect(detail).to_be_hidden(timeout=5000)


class TestNavigation:
    @pytest.mark.spec("V16.14")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/notification-popover']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/notification-popover"), timeout=5000)
