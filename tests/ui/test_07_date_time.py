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
    @pytest.mark.spec("V07.01")
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#dp1")).to_have_js_property("label", "Birthday")

    @pytest.mark.spec("V07.02")
    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#dp-pre")).to_have_js_property("value", "2025-06-15")

    @pytest.mark.spec("V07.04")
    def test_clear_button(self, view_page: Page):
        expect(view_page.locator("#dp-clear")).to_have_js_property("clearButtonVisible", True)

    @pytest.mark.spec("V07.05")
    def test_min_max(self, view_page: Page):
        dp = view_page.locator("#dp-range")
        expect(dp).to_have_js_property("min", "2025-01-01")
        expect(dp).to_have_js_property("max", "2025-12-31")


class TestTimePicker:
    @pytest.mark.spec("V07.06")
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#tp1")).to_have_js_property("label", "Meeting time")

    @pytest.mark.spec("V07.07")
    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#tp-pre")).to_have_js_property("value", "14:30")

    @pytest.mark.spec("V07.09")
    def test_step(self, view_page: Page):
        expect(view_page.locator("#tp-step")).to_have_js_property("step", 1800)

    @pytest.mark.spec("V07.11")
    def test_clear_button(self, view_page: Page):
        expect(view_page.locator("#tp-clear")).to_have_js_property("clearButtonVisible", True)


class TestDateTimePicker:
    @pytest.mark.spec("V07.12")
    def test_renders_with_label(self, view_page: Page):
        expect(view_page.locator("#dtp1")).to_have_js_property("label", "Event")

    @pytest.mark.spec("V07.13")
    def test_set_value_programmatic(self, view_page: Page):
        expect(view_page.locator("#dtp-pre")).to_have_js_property("value", "2025-06-15T14:30")

    @pytest.mark.spec("V07.15")
    def test_placeholders(self, view_page: Page):
        dtp = view_page.locator("#dtp-ph")
        expect(dtp).to_have_js_property("datePlaceholder", "Pick date")
        expect(dtp).to_have_js_property("timePlaceholder", "Pick time")


class TestDatePickerExtras:
    @pytest.mark.spec("V07.16")
    def test_week_numbers_visible(self, view_page: Page):
        dp = view_page.locator("#dp-weeks")
        expect(dp).to_have_js_property("showWeekNumbers", True)

    @pytest.mark.spec("V07.17")
    def test_initial_position(self, view_page: Page):
        dp = view_page.locator("#dp-init")
        expect(dp).to_have_js_property("initialPosition", "2026-06-01")


class TestNavigation:
    @pytest.mark.spec("V07.18")
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/grid-basic"), timeout=5000)
