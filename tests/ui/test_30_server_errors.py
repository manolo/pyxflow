"""UI Tests — View 30: Server Error Handling (/test/server-errors)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/server-errors", "#err-click")
    yield shared_page


class TestErrorHandling:
    @pytest.mark.spec("V30.01")
    def test_click_error_shows_notification(self, view_page: Page):
        """Click handler exception shows error notification."""
        view_page.locator("#err-click").click()
        notif = view_page.locator("vaadin-notification-card")
        expect(notif).to_be_visible(timeout=3000)

    @pytest.mark.spec("V30.02")
    def test_value_change_error_notification(self, view_page: Page):
        """Value-change handler exception shows error notification."""
        tf = view_page.locator("#err-tf")
        tf.click()
        view_page.keyboard.type("test")
        view_page.keyboard.press("Tab")
        view_page.wait_for_timeout(500)
        # May have leftover notification from prior test; check latest
        notif = view_page.locator("vaadin-notification-card").last
        expect(notif).to_be_visible(timeout=3000)

    @pytest.mark.spec("V30.03")
    def test_partial_rpc_failure(self, view_page: Page):
        """First RPC fails but second succeeds — healthy button works."""
        view_page.locator("#healthy").click()
        expect(view_page.locator("#result")).to_have_text("ok", timeout=3000)


class TestDateSerialization:
    @pytest.mark.spec("V30.06")
    def test_date_picker_serialization(self, view_page: Page):
        """DatePicker with set_value(date) renders correctly."""
        dp = view_page.locator("#ser-dp")
        expect(dp).to_have_js_property("value", "2025-06-15")

    @pytest.mark.spec("V30.06")
    def test_datetime_picker_serialization(self, view_page: Page):
        """DateTimePicker with set_value(datetime) renders correctly."""
        dtp = view_page.locator("#ser-dtp")
        expect(dtp).to_have_js_property("value", "2025-06-15T14:30")


class TestSessionResilience:
    @pytest.mark.spec("V30.08")
    def test_rapid_clicks(self, view_page: Page):
        """Multiple rapid clicks all get processed."""
        btn = view_page.locator("#rapid")
        for _ in range(10):
            btn.click()
        expect(view_page.locator("#rapid-count")).to_have_text("10", timeout=5000)

    @pytest.mark.spec("V30.09")
    def test_navigation_after_error(self, view_page: Page):
        """Navigation still works after an error notification."""
        # Trigger an error
        view_page.locator("#err-click").click()
        view_page.wait_for_timeout(500)
        # Navigate to another view and back
        view_page.locator("vaadin-side-nav-item[path='/test/login']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/login"), timeout=5000)
        view_page.locator("vaadin-side-nav-item[path='/test/server-errors']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/server-errors"), timeout=5000)


class TestAllDone:
    @pytest.mark.spec("V30.13")
    def test_all_views_visited(self, view_page: Page):
        expect(view_page.locator("#all-done")).to_have_text("All UI test views visited")
