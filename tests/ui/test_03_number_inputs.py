"""UI Tests — View 3: Number Inputs (/test/number-inputs)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/number-inputs", "vaadin-number-field")
    yield shared_page


def _type_in_field(page: Page, selector: str, text: str):
    page.locator(selector).click()
    page.keyboard.type(text)
    page.keyboard.press("Tab")


class TestNumberField:
    @pytest.mark.spec("V03.01")
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#nf1")).to_have_js_property("label", "Price")

    @pytest.mark.spec("V03.02")
    def test_type_value(self, view_page: Page):
        _type_in_field(view_page, "#nf1", "42.5")
        expect(view_page.locator("#nf1-val")).to_have_text("42.5")

    @pytest.mark.spec("V03.03")
    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#nf-pre")).to_have_js_property("value", "99.9")

    @pytest.mark.spec("V03.04")
    def test_min_max(self, view_page: Page):
        nf = view_page.locator("#nf-range")
        expect(nf).to_have_js_property("min", 0)
        expect(nf).to_have_js_property("max", 100)

    @pytest.mark.spec("V03.05")
    def test_step(self, view_page: Page):
        expect(view_page.locator("#nf-step")).to_have_js_property("step", 0.5)

    @pytest.mark.spec("V03.06")
    def test_step_buttons_visible(self, view_page: Page):
        expect(view_page.locator("#nf-step")).to_have_js_property(
            "stepButtonsVisible", True
        )

    @pytest.mark.spec("V03.07")
    def test_clear_button(self, view_page: Page):
        expect(view_page.locator("#nf-clear")).to_have_js_property(
            "clearButtonVisible", True
        )

    @pytest.mark.spec("V03.08")
    def test_prefix_suffix(self, view_page: Page):
        nf = view_page.locator("#nf-fix")
        expect(nf.locator("vaadin-icon[slot='prefix']")).to_be_visible()
        expect(nf.locator("span[slot='suffix']")).to_be_visible()


class TestIntegerField:
    @pytest.mark.spec("V03.09")
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#if1")).to_have_js_property("label", "Qty")

    @pytest.mark.spec("V03.10")
    def test_type_integer(self, view_page: Page):
        _type_in_field(view_page, "#if1", "42")
        expect(view_page.locator("#if1-val")).to_have_text("42")

    @pytest.mark.spec("V03.12")
    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#if-pre")).to_have_js_property("value", "7")

    @pytest.mark.spec("V03.13")
    def test_step_buttons(self, view_page: Page):
        expect(view_page.locator("#if-step")).to_have_js_property(
            "stepButtonsVisible", True
        )

    @pytest.mark.spec("V03.14")
    def test_min_max(self, view_page: Page):
        nf = view_page.locator("#if-range")
        expect(nf).to_have_js_property("min", 1)
        expect(nf).to_have_js_property("max", 10)


class TestNavigation:
    @pytest.mark.spec("V03.15")
    def test_nav_to_next(self, shared_page: Page, base_url):
        """Navigate to next view (not yet in layout, use goto)."""
        shared_page.goto(f"{base_url}/test/checkbox-radio")
        expect(shared_page).to_have_url(re.compile(r".*/test/checkbox-radio"), timeout=5000)
