"""UI Tests — View 19: HTML Elements (/test/html-elements)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/html-elements", "#h1")
    yield shared_page


class TestHeadings:
    @pytest.mark.spec("V19.01")
    def test_h1(self, view_page: Page):
        expect(view_page.locator("#h1")).to_have_text("Title")

    @pytest.mark.spec("V19.02")
    def test_h2(self, view_page: Page):
        expect(view_page.locator("#h2")).to_have_text("Subtitle")

    @pytest.mark.spec("V19.03")
    def test_h3(self, view_page: Page):
        expect(view_page.locator("#h3")).to_have_text("H3")

    @pytest.mark.spec("V19.03")
    def test_h4(self, view_page: Page):
        expect(view_page.locator("#h4")).to_have_text("H4")

    @pytest.mark.spec("V19.03")
    def test_h5(self, view_page: Page):
        expect(view_page.locator("#h5")).to_have_text("H5")

    @pytest.mark.spec("V19.03")
    def test_h6(self, view_page: Page):
        expect(view_page.locator("#h6")).to_have_text("H6")


class TestTextElements:
    @pytest.mark.spec("V19.04")
    def test_paragraph(self, view_page: Page):
        expect(view_page.locator("#p1")).to_have_text("Lorem ipsum")

    @pytest.mark.spec("V19.05")
    def test_span(self, view_page: Page):
        expect(view_page.locator("#sp1")).to_have_text("inline")

    @pytest.mark.spec("V19.06")
    def test_div_children(self, view_page: Page):
        div = view_page.locator("#div1")
        expect(div).to_contain_text("child1")
        expect(div).to_contain_text("child2")

    @pytest.mark.spec("V19.07")
    def test_div_text(self, view_page: Page):
        expect(view_page.locator("#div-text")).to_have_text("text content")

    @pytest.mark.spec("V19.12")
    def test_pre(self, view_page: Page):
        expect(view_page.locator("#pre1")).to_have_text("code block")


class TestLinks:
    @pytest.mark.spec("V19.08")
    def test_anchor(self, view_page: Page):
        a = view_page.locator("#a1")
        expect(a).to_have_text("Link")
        expect(a).to_have_attribute("href", "https://example.com")

    @pytest.mark.spec("V19.09")
    def test_anchor_target(self, view_page: Page):
        expect(view_page.locator("#a-target")).to_have_attribute("target", "_blank")


class TestMedia:
    @pytest.mark.spec("V19.10")
    def test_iframe(self, view_page: Page):
        expect(view_page.locator("#iframe1")).to_have_attribute("src", "about:blank")

    @pytest.mark.spec("V19.13")
    def test_image(self, view_page: Page):
        img = view_page.locator("#img1")
        expect(img).to_have_attribute("alt", "Logo")

    @pytest.mark.spec("V19.11")
    def test_hr(self, view_page: Page):
        expect(view_page.locator("#hr1")).to_be_visible()


class TestLabels:
    @pytest.mark.spec("V19.14")
    def test_native_label(self, view_page: Page):
        expect(view_page.locator("#lbl1")).to_have_text("Field label")


class TestSemanticContainers:
    @pytest.mark.spec("V19.15")
    def test_header(self, view_page: Page):
        expect(view_page.locator("#header1")).to_contain_text("header")

    @pytest.mark.spec("V19.15")
    def test_footer(self, view_page: Page):
        expect(view_page.locator("#footer1")).to_contain_text("footer")

    @pytest.mark.spec("V19.15")
    def test_section(self, view_page: Page):
        expect(view_page.locator("#section1")).to_contain_text("section")


class TestNavigation:
    @pytest.mark.spec("V19.16")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/component-api']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/component-api"), timeout=5000)
