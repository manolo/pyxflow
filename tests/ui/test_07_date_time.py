"""UI Tests — View 7: DatePicker, TimePicker, DateTimePicker (/test/date-time)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/date-time", "vaadin-date-picker")
    yield shared_page


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


class TestDatePickerExtras:
    @pytest.mark.spec("V07.16")
    def test_week_numbers_visible(self, view_page: Page):
        dp = view_page.locator("#dp-weeks")
        expect(dp).to_have_js_property("showWeekNumbers", True)

    @pytest.mark.spec("V07.17")
    def test_initial_position(self, view_page: Page):
        dp = view_page.locator("#dp-init")
        expect(dp).to_have_js_property("initialPosition", "2026-06-01")

    @pytest.mark.spec("V07.25")
    def test_auto_open_disabled(self, view_page: Page):
        expect(view_page.locator("#dp-noauto")).to_have_js_property("autoOpenDisabled", True)

    @pytest.mark.spec("V07.26")
    def test_required(self, view_page: Page):
        expect(view_page.locator("#dp-req")).to_have_js_property("required", True)


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

    @pytest.mark.spec("V07.10")
    def test_min_max(self, view_page: Page):
        tp = view_page.locator("#tp-range")
        expect(tp).to_have_js_property("min", "09:00")
        expect(tp).to_have_js_property("max", "17:00")

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

    @pytest.mark.spec("V07.16")
    def test_min_max(self, view_page: Page):
        dtp = view_page.locator("#dtp-range")
        expect(dtp).to_have_js_property("min", "2025-01-01T00:00")
        expect(dtp).to_have_js_property("max", "2025-12-31T23:59")

    @pytest.mark.spec("V07.33")
    def test_step(self, view_page: Page):
        expect(view_page.locator("#dtp-step")).to_have_js_property("step", 3600)

    @pytest.mark.spec("V07.34")
    def test_required(self, view_page: Page):
        expect(view_page.locator("#dtp-req")).to_have_js_property("required", True)


class TestNavigation:
    @pytest.mark.spec("V07.36")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/grid-basic']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/grid-basic"), timeout=5000)
