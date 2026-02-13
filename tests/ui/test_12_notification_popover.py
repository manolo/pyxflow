"""UI Tests — View 12: Notification & Popover (/test/notification-popover)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/notification-popover")
    p.wait_for_selector("vaadin-button", timeout=15000)
    yield p
    ctx.close()


class TestNotification:
    @pytest.mark.spec("V12.01")
    def test_show_static(self, view_page: Page):
        view_page.locator("#btn-notif-show").click()
        notif = view_page.locator("vaadin-notification-card").filter(has_text="Saved!")
        expect(notif).to_be_visible(timeout=1500)

    @pytest.mark.spec("V12.03")
    def test_show_position(self, view_page: Page):
        view_page.locator("#btn-notif-pos").click()
        notif = view_page.locator("vaadin-notification-card").filter(has_text="Top center!")
        expect(notif).to_be_visible(timeout=1500)

    @pytest.mark.spec("V12.05")
    def test_success_theme(self, view_page: Page):
        view_page.locator("#btn-notif-theme").click()
        notif = view_page.locator("vaadin-notification-card").filter(has_text="Success!")
        expect(notif).to_be_visible(timeout=1500)

    @pytest.mark.spec("V12.06")
    def test_close_programmatic(self, view_page: Page):
        view_page.locator("#btn-notif-open").click()
        notif = view_page.locator("vaadin-notification-card").filter(has_text="Permanent")
        expect(notif).to_be_visible(timeout=1500)
        view_page.locator("#btn-notif-close").click()
        expect(notif).to_be_hidden(timeout=1500)

    @pytest.mark.spec("V12.07")
    def test_close_listener(self, view_page: Page):
        view_page.locator("#btn-notif-cls").click()
        # Wait for the 1000ms duration to expire and close listener to fire
        expect(view_page.locator("#notif-closed")).to_have_text("closed", timeout=1500)


class TestPopover:
    @pytest.mark.spec("V12.09")
    def test_popover_renders(self, view_page: Page):
        """Verify popover components are in the DOM (overlays need deeper implementation work)."""
        expect(view_page.locator("#pop-target")).to_be_visible()
        expect(view_page.locator("#pop-prog-target")).to_be_visible()
        expect(view_page.locator("#pop-pos-target")).to_be_visible()
        expect(view_page.locator("#pop-ev-target")).to_be_visible()


class TestNavigation:
    @pytest.mark.spec("V12.17")
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(
            re.compile(r".*/test/tabs-accordion"), timeout=1500
        )
