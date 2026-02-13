"""UI Tests — View 19: HTML Elements (/test/html-elements)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/html-elements")
    p.wait_for_selector("#h1", timeout=15000)
    yield p
    ctx.close()


class TestHeadings:
    def test_h1(self, view_page: Page):
        expect(view_page.locator("#h1")).to_have_text("Title")

    def test_h2(self, view_page: Page):
        expect(view_page.locator("#h2")).to_have_text("Subtitle")

    def test_h3(self, view_page: Page):
        expect(view_page.locator("#h3")).to_have_text("H3")

    def test_h4(self, view_page: Page):
        expect(view_page.locator("#h4")).to_have_text("H4")

    def test_h5(self, view_page: Page):
        expect(view_page.locator("#h5")).to_have_text("H5")

    def test_h6(self, view_page: Page):
        expect(view_page.locator("#h6")).to_have_text("H6")


class TestTextElements:
    def test_paragraph(self, view_page: Page):
        expect(view_page.locator("#p1")).to_have_text("Lorem ipsum")

    def test_span(self, view_page: Page):
        expect(view_page.locator("#sp1")).to_have_text("inline")

    def test_div_children(self, view_page: Page):
        div = view_page.locator("#div1")
        expect(div).to_contain_text("child1")
        expect(div).to_contain_text("child2")

    def test_div_text(self, view_page: Page):
        expect(view_page.locator("#div-text")).to_have_text("text content")

    def test_pre(self, view_page: Page):
        expect(view_page.locator("#pre1")).to_have_text("code block")


class TestLinks:
    def test_anchor(self, view_page: Page):
        a = view_page.locator("#a1")
        expect(a).to_have_text("Link")
        expect(a).to_have_attribute("href", "https://example.com")

    def test_anchor_target(self, view_page: Page):
        expect(view_page.locator("#a-target")).to_have_attribute("target", "_blank")


class TestMedia:
    def test_iframe(self, view_page: Page):
        expect(view_page.locator("#iframe1")).to_have_attribute("src", "about:blank")

    def test_image(self, view_page: Page):
        img = view_page.locator("#img1")
        expect(img).to_have_attribute("alt", "Logo")

    def test_hr(self, view_page: Page):
        expect(view_page.locator("#hr1")).to_be_visible()


class TestLabels:
    def test_native_label(self, view_page: Page):
        expect(view_page.locator("#lbl1")).to_have_text("Field label")


class TestSemanticContainers:
    def test_header(self, view_page: Page):
        expect(view_page.locator("#header1")).to_contain_text("header")

    def test_footer(self, view_page: Page):
        expect(view_page.locator("#footer1")).to_contain_text("footer")

    def test_section(self, view_page: Page):
        expect(view_page.locator("#section1")).to_contain_text("section")


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/component-api"), timeout=5000)
