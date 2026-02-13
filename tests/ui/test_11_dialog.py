"""UI Tests — View 11: Dialog & ConfirmDialog (/test/dialog)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/dialog")
    p.wait_for_selector("vaadin-button", timeout=15000)
    yield p
    ctx.close()


def _close_dialog(page: Page, dialog_id: str):
    """Close a specific dialog by pressing Escape."""
    dlg = page.locator(f"#{dialog_id}[opened]")
    if dlg.count() > 0:
        page.keyboard.press("Escape")
        page.wait_for_timeout(500)


class TestDialog:
    @pytest.mark.spec("V11.01")
    def test_open_close(self, view_page: Page):
        view_page.locator("#btn-open").click()
        dlg = view_page.locator("#dlg1")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        expect(dlg).to_contain_text("Hello")
        view_page.keyboard.press("Escape")
        view_page.wait_for_timeout(500)

    @pytest.mark.spec("V11.02")
    def test_header_title(self, view_page: Page):
        _close_dialog(view_page, "dlg1")
        view_page.locator("#btn-title").click()
        dlg = view_page.locator("#dlg-title")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        # header title is set as aria-label
        expect(dlg).to_have_attribute("aria-label", "My Dialog")
        view_page.keyboard.press("Escape")
        view_page.wait_for_timeout(500)

    @pytest.mark.spec("V11.03")
    def test_header_footer(self, view_page: Page):
        _close_dialog(view_page, "dlg-title")
        view_page.locator("#btn-hf").click()
        dlg = view_page.locator("#dlg-hf")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        expect(dlg).to_contain_text("Body")
        # Close via footer button inside the dialog
        view_page.locator("#dlg-hf vaadin-button").filter(has_text="Close").click()
        view_page.wait_for_timeout(500)

    @pytest.mark.spec("V11.05")
    def test_draggable(self, view_page: Page):
        _close_dialog(view_page, "dlg-hf")
        view_page.locator("#btn-drag").click()
        dlg = view_page.locator("#dlg-drag")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        view_page.keyboard.press("Escape")
        view_page.wait_for_timeout(500)

    @pytest.mark.spec("V11.06")
    def test_resizable(self, view_page: Page):
        _close_dialog(view_page, "dlg-drag")
        view_page.locator("#btn-resize").click()
        dlg = view_page.locator("#dlg-resize")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        view_page.keyboard.press("Escape")
        view_page.wait_for_timeout(500)

    @pytest.mark.spec("V11.11")
    def test_close_listener(self, view_page: Page):
        _close_dialog(view_page, "dlg-resize")
        view_page.locator("#btn-cls").click()
        dlg = view_page.locator("#dlg-cls")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        view_page.keyboard.press("Escape")
        expect(view_page.locator("#dlg-closed")).to_have_text("closed", timeout=3000)


class TestConfirmDialog:
    @pytest.mark.spec("V11.13")
    def test_confirm(self, view_page: Page):
        view_page.locator("#btn-cd").click()
        dlg = view_page.locator("#cd1[opened]")
        expect(dlg).to_contain_text("Are you sure?", timeout=3000)
        # Click confirm button inside the confirm dialog
        dlg.locator("vaadin-button").filter(has_text="Yes").click()
        expect(view_page.locator("#cd-result")).to_have_text("confirmed", timeout=3000)

    @pytest.mark.spec("V11.14")
    def test_cancel(self, view_page: Page):
        view_page.locator("#btn-cd-cancel").click()
        dlg = view_page.locator("#cd-cancel[opened]")
        expect(dlg).to_contain_text("Proceed?", timeout=3000)
        dlg.locator("vaadin-button").filter(has_text="No").click()
        expect(view_page.locator("#cd-cancel-result")).to_have_text("cancelled", timeout=3000)

    @pytest.mark.spec("V11.15")
    def test_reject(self, view_page: Page):
        view_page.locator("#btn-cd-reject").click()
        dlg = view_page.locator("#cd-reject[opened]")
        expect(dlg).to_contain_text("This is permanent.", timeout=3000)
        dlg.locator("vaadin-button").filter(has_text="Never").click()
        expect(view_page.locator("#cd-reject-result")).to_have_text("rejected", timeout=3000)

    @pytest.mark.spec("V11.17")
    def test_reopen(self, view_page: Page):
        view_page.locator("#btn-cd-reopen").click()
        dlg = view_page.locator("#cd-reopen[opened]")
        expect(dlg).to_contain_text("Can reopen?", timeout=3000)
        dlg.locator("vaadin-button").filter(has_text="OK").click()
        expect(view_page.locator("#cd-reopen-count")).to_have_text("1", timeout=3000)
        # Open again
        view_page.locator("#btn-cd-reopen").click()
        dlg = view_page.locator("#cd-reopen[opened]")
        expect(dlg).to_contain_text("Can reopen?", timeout=3000)
        dlg.locator("vaadin-button").filter(has_text="OK").click()
        expect(view_page.locator("#cd-reopen-count")).to_have_text("2", timeout=3000)


class TestNavigation:
    @pytest.mark.spec("V11.18")
    def test_nav_to_next(self, view_page: Page):
        for _ in range(3):
            view_page.keyboard.press("Escape")
            view_page.wait_for_timeout(300)
        view_page.locator("#nav-next").evaluate("el => el.click()")
        expect(view_page).to_have_url(
            re.compile(r".*/test/notification-popover"), timeout=5000
        )
