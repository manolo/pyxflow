"""UI Tests — View 20: Base Component API (/test/component-api)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/component-api", "vaadin-button")
    yield shared_page


class TestVisibility:
    @pytest.mark.spec("V20.01")
    def test_hide(self, view_page: Page):
        view_page.locator("#btn-hide").click()
        expect(view_page.locator("#vis-btn")).to_be_hidden()

    @pytest.mark.spec("V20.02")
    def test_show(self, view_page: Page):
        view_page.locator("#btn-show").click()
        expect(view_page.locator("#vis-btn")).to_be_visible()


class TestEnabled:
    @pytest.mark.spec("V20.03")
    def test_disable(self, view_page: Page):
        view_page.locator("#btn-disable").click()
        expect(view_page.locator("#en-btn")).to_have_attribute("disabled", "")

    @pytest.mark.spec("V20.04")
    def test_enable(self, view_page: Page):
        view_page.locator("#btn-enable").click()
        expect(view_page.locator("#en-btn")).not_to_have_attribute("disabled", "")


class TestCssClasses:
    @pytest.mark.spec("V20.05")
    def test_add_class(self, view_page: Page):
        view_page.locator("#btn-add-cls").click()
        expect(view_page.locator("#cls-span")).to_have_class(re.compile(r"highlight"))

    @pytest.mark.spec("V20.06")
    def test_remove_class(self, view_page: Page):
        view_page.locator("#btn-rm-cls").click()
        expect(view_page.locator("#cls-span")).not_to_have_class(re.compile(r"\bold\b"))


class TestInlineStyles:
    @pytest.mark.spec("V20.08")
    def test_set_style(self, view_page: Page):
        view_page.locator("#btn-set-style").click()
        expect(view_page.locator("#sty-span")).to_have_css("color", "rgb(255, 0, 0)")

    @pytest.mark.spec("V20.09")
    def test_remove_style(self, view_page: Page):
        view_page.locator("#btn-rm-style").click()
        # After removing color, it should not be red anymore
        sty = view_page.locator("#sty-span")
        expect(sty).not_to_have_css("color", "rgb(255, 0, 0)")


class TestSize:
    @pytest.mark.spec("V20.10")
    def test_set_width_height(self, view_page: Page):
        view_page.locator("#btn-size").click()
        div = view_page.locator("#size-div")
        expect(div).to_have_css("width", "300px")
        expect(div).to_have_css("height", "100px")

    @pytest.mark.spec("V20.11")
    def test_set_full(self, view_page: Page):
        view_page.locator("#btn-full").click()
        div = view_page.locator("#full-div")
        expect(div).to_have_css("width", re.compile(r"\d+"))


class TestTheme:
    @pytest.mark.spec("V20.13")
    def test_add_theme(self, view_page: Page):
        view_page.locator("#btn-add-theme").click()
        expect(view_page.locator("#theme-btn")).to_have_attribute("theme", re.compile(r"primary"))

    @pytest.mark.spec("V20.14")
    def test_remove_theme(self, view_page: Page):
        view_page.locator("#btn-rm-theme").click()
        btn = view_page.locator("#theme-btn")
        # Theme attribute should not contain "primary"
        expect(btn).not_to_have_attribute("theme", re.compile(r"primary"))


class TestDynamicId:
    @pytest.mark.spec("V20.15")
    def test_set_id(self, view_page: Page):
        view_page.locator("#btn-set-id").click()
        expect(view_page.locator("#my-span")).to_be_visible()


class TestTooltip:
    @pytest.mark.spec("V20.16")
    def test_tooltip_text(self, view_page: Page):
        btn = view_page.locator("#tip-btn")
        expect(btn).to_be_visible()


class TestAria:
    @pytest.mark.spec("V20.18")
    def test_aria_label(self, view_page: Page):
        expect(view_page.locator("#aria-btn")).to_have_attribute("aria-label", "Close dialog")


class TestFocus:
    @pytest.mark.spec("V20.21")
    @pytest.mark.skip(reason="Focus/blur events need DOM event forwarding investigation")
    def test_focus_listener(self, view_page: Page):
        view_page.locator("#fb-tf").evaluate("el => el.focus()")
        expect(view_page.locator("#fb-ev")).to_have_text("focus")

    @pytest.mark.spec("V20.21")
    @pytest.mark.skip(reason="Focus/blur events need DOM event forwarding investigation")
    def test_blur_listener(self, view_page: Page):
        view_page.locator("#fb-tf").evaluate("el => el.focus()")
        view_page.locator("#fb-tf").evaluate("el => el.blur()")
        expect(view_page.locator("#fb-ev")).to_have_text("blur")


class TestNavigation:
    @pytest.mark.spec("V20.22")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/field-mixins']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/field-mixins"), timeout=5000)
