"""UI Tests — View 2: Text Inputs (/test/text-inputs)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    """Single page for the whole module — navigate once."""
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/text-inputs")
    p.wait_for_selector("vaadin-text-field", timeout=15000)
    yield p
    ctx.close()


def _type_in_field(page: Page, selector: str, text: str):
    """Click a field, type text, then Tab to trigger change event."""
    page.locator(selector).click()
    page.keyboard.type(text)
    page.keyboard.press("Tab")


class TestTextField:
    @pytest.mark.spec("V02.01")
    def test_renders_with_label(self, view_page: Page):
        tf = view_page.locator("#tf1")
        expect(tf).to_have_js_property("label", "Name")

    @pytest.mark.spec("V02.02")
    def test_type_and_read_value(self, view_page: Page):
        _type_in_field(view_page, "#tf1", "hello")
        expect(view_page.locator("#tf1-val")).to_have_text("hello")

    @pytest.mark.spec("V02.03")
    def test_set_value_programmatic(self, view_page: Page):
        tf = view_page.locator("#tf-preset")
        expect(tf).to_have_js_property("value", "preset")

    @pytest.mark.spec("V02.04")
    def test_placeholder(self, view_page: Page):
        tf = view_page.locator("#tf-ph")
        expect(tf).to_have_attribute("placeholder", "Enter name...")

    @pytest.mark.spec("V02.05")
    def test_clear_button_visible(self, view_page: Page):
        tf = view_page.locator("#tf-clear")
        expect(tf).to_have_attribute("clear-button-visible", "")

    @pytest.mark.spec("V02.06")
    def test_max_length(self, view_page: Page):
        tf = view_page.locator("#tf-max")
        expect(tf).to_have_js_property("maxlength", 5)

    @pytest.mark.spec("V02.07")
    def test_pattern(self, view_page: Page):
        tf = view_page.locator("#tf-pat")
        expect(tf).to_have_js_property("pattern", "[0-9]+")

    @pytest.mark.spec("V02.08")
    def test_allowed_char_pattern(self, view_page: Page):
        tf = view_page.locator("#tf-acp")
        expect(tf).to_have_js_property("allowedCharPattern", "[0-9]")

    @pytest.mark.spec("V02.09")
    def test_prefix_suffix(self, view_page: Page):
        tf = view_page.locator("#tf-fix")
        expect(tf.locator("vaadin-icon[slot='prefix']")).to_be_visible()
        expect(tf.locator("span[slot='suffix']")).to_be_visible()

    @pytest.mark.spec("V02.23")
    def test_helper_text(self, view_page: Page):
        tf = view_page.locator("#tf-help")
        expect(tf).to_have_js_property("helperText", "Min 3 chars")

    @pytest.mark.spec("V02.26")
    def test_set_label_dynamic(self, view_page: Page):
        view_page.locator("#btn-lbl").click()
        expect(view_page.locator("#tf-lbl")).to_have_js_property("label", "New")


class TestTextArea:
    @pytest.mark.spec("V02.11")
    def test_renders_with_label(self, view_page: Page):
        ta = view_page.locator("#ta1")
        expect(ta).to_have_js_property("label", "Bio")

    @pytest.mark.spec("V02.12")
    def test_type_and_read(self, view_page: Page):
        _type_in_field(view_page, "#ta1", "line1")
        expect(view_page.locator("#ta1-val")).to_have_text("line1")

    @pytest.mark.spec("V02.14")
    def test_clear_button(self, view_page: Page):
        ta = view_page.locator("#ta-clear")
        expect(ta).to_have_attribute("clear-button-visible", "")


class TestPasswordField:
    @pytest.mark.spec("V02.15")
    def test_renders(self, view_page: Page):
        expect(view_page.locator("#pf1")).to_be_visible()

    @pytest.mark.spec("V02.16")
    def test_type_and_read(self, view_page: Page):
        _type_in_field(view_page, "#pf1", "secret123")
        expect(view_page.locator("#pf1-val")).to_have_text("secret123")

    @pytest.mark.spec("V02.18")
    def test_reveal_button_hidden(self, view_page: Page):
        pf = view_page.locator("#pf-noreveal")
        expect(pf).to_have_js_property("revealButtonHidden", True)


class TestEmailField:
    @pytest.mark.spec("V02.19")
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#ef1")).to_have_js_property("label", "Email")

    @pytest.mark.spec("V02.22")
    def test_type_and_read(self, view_page: Page):
        _type_in_field(view_page, "#ef1", "a@b.com")
        expect(view_page.locator("#ef1-val")).to_have_text("a@b.com")


class TestNavigation:
    @pytest.mark.spec("V02.28")
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/number-inputs"), timeout=5000)
