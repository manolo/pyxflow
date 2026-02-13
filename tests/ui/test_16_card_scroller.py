"""UI Tests — View 16: Card, Scroller, MasterDetailLayout (/test/card-scroller)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/card-scroller")
    p.wait_for_selector("vaadin-card", timeout=15000)
    yield p
    ctx.close()


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
    def test_renders(self, view_page: Page):
        mdl = view_page.locator("#mdl1")
        expect(mdl).to_contain_text("Master panel")


class TestNavigation:
    @pytest.mark.spec("V16.13")
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/upload"), timeout=5000)
