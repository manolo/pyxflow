"""UI Tests -- View 34: execute_js during before_enter (/test/before-enter-js)

Verifies that execute_js() called inside before_enter runs correctly and does
not trigger a client resync.  The fix ensures serverConnected is the last
execute command in the navigation response, so component JS runs first.
"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/before-enter-js", "#bej-status")
    yield shared_page


class TestBeforeEnterJsBasic:
    @pytest.mark.spec("V34.01")
    def test_initial_before_enter_updates_status(self, view_page: Page):
        """First navigation calls before_enter which updates the counter."""
        expect(view_page.locator("#bej-status")).to_have_text("count:1")

    @pytest.mark.spec("V34.02")
    def test_initial_before_enter_updates_target(self, view_page: Page):
        """First navigation sets the target text via server-side set_text."""
        expect(view_page.locator("#bej-js-target")).to_have_text("py:default")

    @pytest.mark.spec("V34.03")
    def test_initial_execute_js_sets_data_attribute(self, view_page: Page):
        """execute_js in before_enter sets a data attribute on the target element."""
        value = view_page.locator("#bej-js-target").get_attribute("data-from-js")
        assert value == "js:default", f"Expected 'js:default', got '{value}'"


class TestReenterExecuteJs:
    @pytest.mark.spec("V34.04")
    def test_reenter_execute_js_no_resync(self, view_page: Page):
        """Clicking Navigate triggers reenter with execute_js -- no resync.

        Before the fix, serverConnected fired before the component's
        execute_js, causing the client to consider navigation "done" too
        early and trigger a resync.
        """
        view_page.locator("#bej-navigate").click()
        expect(view_page.locator("#bej-status")).to_have_text("count:2", timeout=5000)
        expect(view_page.locator("#bej-js-target")).to_have_text("py:click-1")

    @pytest.mark.spec("V34.05")
    def test_reenter_execute_js_sets_data_attribute(self, view_page: Page):
        """Reenter execute_js updates the data attribute."""
        value = view_page.locator("#bej-js-target").get_attribute("data-from-js")
        assert value == "js:click-1", f"Expected 'js:click-1', got '{value}'"

    @pytest.mark.spec("V34.06")
    def test_multiple_reenters(self, view_page: Page):
        """Multiple consecutive reenters all work without resync."""
        view_page.locator("#bej-navigate").click()
        expect(view_page.locator("#bej-status")).to_have_text("count:3", timeout=5000)

        view_page.locator("#bej-navigate").click()
        expect(view_page.locator("#bej-status")).to_have_text("count:4", timeout=5000)


class TestDirectUrlExecuteJs:
    @pytest.mark.spec("V34.07")
    def test_direct_url_with_param(self, view_page: Page, base_url):
        """Direct navigation to URL with param calls before_enter with execute_js."""
        view_page.goto(f"{base_url}/test/before-enter-js/hello")
        expect(view_page.locator("#bej-status")).to_have_text("count:1", timeout=5000)
        expect(view_page.locator("#bej-js-target")).to_have_text("py:hello")

    @pytest.mark.spec("V34.08")
    def test_no_console_errors_during_reenter(self, browser, base_url):
        """No JS errors or resync warnings during reenter navigation."""
        ctx = browser.new_context(viewport={"width": 1280, "height": 720})
        page = ctx.new_page()
        errors = []
        page.on("console", lambda msg: errors.append(msg.text)
                if msg.type == "error" else None)
        try:
            page.goto(f"{base_url}/test/before-enter-js")
            expect(page.locator("#bej-status")).to_have_text("count:1", timeout=5000)

            # Trigger reenter
            page.locator("#bej-navigate").click()
            expect(page.locator("#bej-status")).to_have_text("count:2", timeout=5000)

            # Filter out irrelevant errors (e.g. favicon 404)
            resync_errors = [e for e in errors if "resync" in e.lower()
                             or "Gave up" in e or "unexpected" in e.lower()]
            assert resync_errors == [], f"Console errors during navigation: {resync_errors}"
        finally:
            ctx.close()
