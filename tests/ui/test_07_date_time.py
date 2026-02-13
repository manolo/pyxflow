"""UI Tests — View 7: DatePicker, TimePicker, DateTimePicker (/test/date-time)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/date-time")
    p.wait_for_selector("vaadin-date-picker", timeout=15000)
    yield p
    ctx.close()


class TestDatePicker:
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#dp1")).to_have_js_property("label", "Birthday")

    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#dp-pre")).to_have_js_property("value", "2025-06-15")

    def test_clear_button(self, view_page: Page):
        expect(view_page.locator("#dp-clear")).to_have_js_property("clearButtonVisible", True)

    def test_min_max(self, view_page: Page):
        dp = view_page.locator("#dp-range")
        expect(dp).to_have_js_property("min", "2025-01-01")
        expect(dp).to_have_js_property("max", "2025-12-31")


class TestTimePicker:
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#tp1")).to_have_js_property("label", "Meeting time")

    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#tp-pre")).to_have_js_property("value", "14:30")

    def test_step(self, view_page: Page):
        expect(view_page.locator("#tp-step")).to_have_js_property("step", 1800)

    def test_clear_button(self, view_page: Page):
        expect(view_page.locator("#tp-clear")).to_have_js_property("clearButtonVisible", True)


class TestDateTimePicker:
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#dtp1")).to_have_js_property("label", "Event")

    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#dtp-pre")).to_have_js_property("value", "2025-06-15T14:30")

    def test_placeholders(self, view_page: Page):
        dtp = view_page.locator("#dtp-ph")
        expect(dtp).to_have_js_property("datePlaceholder", "Pick date")
        expect(dtp).to_have_js_property("timePlaceholder", "Pick time")


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/grid-basic"), timeout=5000)
