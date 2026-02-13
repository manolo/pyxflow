"""UI Tests — View 3: Number Inputs (/test/number-inputs)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/number-inputs")
    p.wait_for_selector("vaadin-number-field", timeout=15000)
    yield p
    ctx.close()


def _type_in_field(page: Page, selector: str, text: str):
    page.locator(selector).click()
    page.keyboard.type(text)
    page.keyboard.press("Tab")


class TestNumberField:
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#nf1")).to_have_js_property("label", "Price")

    def test_type_value(self, view_page: Page):
        _type_in_field(view_page, "#nf1", "42.5")
        expect(view_page.locator("#nf1-val")).to_have_text("42.5")

    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#nf-pre")).to_have_js_property("value", "99.9")

    def test_min_max(self, view_page: Page):
        nf = view_page.locator("#nf-range")
        expect(nf).to_have_js_property("min", 0)
        expect(nf).to_have_js_property("max", 100)

    def test_step(self, view_page: Page):
        expect(view_page.locator("#nf-step")).to_have_js_property("step", 0.5)

    def test_step_buttons_visible(self, view_page: Page):
        expect(view_page.locator("#nf-step")).to_have_js_property(
            "stepButtonsVisible", True
        )

    def test_clear_button(self, view_page: Page):
        expect(view_page.locator("#nf-clear")).to_have_js_property(
            "clearButtonVisible", True
        )

    def test_prefix_suffix(self, view_page: Page):
        nf = view_page.locator("#nf-fix")
        expect(nf.locator("vaadin-icon[slot='prefix']")).to_be_visible()
        expect(nf.locator("span[slot='suffix']")).to_be_visible()


class TestIntegerField:
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#if1")).to_have_js_property("label", "Qty")

    def test_type_integer(self, view_page: Page):
        _type_in_field(view_page, "#if1", "42")
        expect(view_page.locator("#if1-val")).to_have_text("42")

    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#if-pre")).to_have_js_property("value", "7")

    def test_step_buttons(self, view_page: Page):
        expect(view_page.locator("#if-step")).to_have_js_property(
            "stepButtonsVisible", True
        )

    def test_min_max(self, view_page: Page):
        nf = view_page.locator("#if-range")
        expect(nf).to_have_js_property("min", 1)
        expect(nf).to_have_js_property("max", 10)


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/checkbox-radio"), timeout=5000)
