"""UI Tests — View 11: Dialog & ConfirmDialog (/test/dialog)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/dialog", "vaadin-button")
    yield shared_page


def _close_dialog(page: Page, dialog_id: str):
    """Close a specific dialog by pressing Escape and waiting for it to close."""
    dlg = page.locator(f"#{dialog_id}[opened]")
    if dlg.count() > 0:
        page.keyboard.press("Escape")
        expect(page.locator(f"#{dialog_id}")).not_to_have_attribute("opened", "")


class TestDialog:
    @pytest.mark.spec("V11.01")
    def test_open_close(self, view_page: Page):
        view_page.locator("#btn-open").click()
        dlg = view_page.locator("#dlg1")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        expect(dlg).to_contain_text("Hello")
        view_page.keyboard.press("Escape")
        expect(dlg).not_to_have_attribute("opened", "")

    @pytest.mark.spec("V11.02")
    def test_header_title(self, view_page: Page):
        _close_dialog(view_page, "dlg1")
        view_page.locator("#btn-title").click()
        dlg = view_page.locator("#dlg-title")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        expect(dlg).to_have_attribute("aria-label", "My Dialog")
        view_page.keyboard.press("Escape")
        expect(dlg).not_to_have_attribute("opened", "")

    @pytest.mark.spec("V11.03")
    def test_header_footer(self, view_page: Page):
        _close_dialog(view_page, "dlg-title")
        view_page.locator("#btn-hf").click()
        dlg = view_page.locator("#dlg-hf")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        expect(dlg).to_contain_text("Body")
        view_page.locator("#dlg-hf vaadin-button").filter(has_text="Close").click()
        expect(dlg).not_to_have_attribute("opened", "")

    @pytest.mark.spec("V11.05")
    def test_draggable(self, view_page: Page):
        _close_dialog(view_page, "dlg-hf")
        view_page.locator("#btn-drag").click()
        dlg = view_page.locator("#dlg-drag")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        view_page.keyboard.press("Escape")
        expect(dlg).not_to_have_attribute("opened", "")

    @pytest.mark.spec("V11.06")
    def test_resizable(self, view_page: Page):
        _close_dialog(view_page, "dlg-drag")
        view_page.locator("#btn-resize").click()
        dlg = view_page.locator("#dlg-resize")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        view_page.keyboard.press("Escape")
        expect(dlg).not_to_have_attribute("opened", "")

    @pytest.mark.spec("V11.09")
    def test_set_width_height(self, view_page: Page):
        """Dialog with set_width/set_height uses element properties."""
        _close_dialog(view_page, "dlg-resize")
        view_page.locator("#btn-size").click()
        dlg = view_page.locator("#dlg-size")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        # Width/height are element properties (not CSS custom properties)
        expect(dlg).to_have_js_property("width", "600px")
        expect(dlg).to_have_js_property("height", "400px")
        view_page.keyboard.press("Escape")
        expect(dlg).not_to_have_attribute("opened", "")

    @pytest.mark.spec("V11.10")
    def test_set_min_max_dimensions(self, view_page: Page):
        """Dialog min/max width/height applied on overlay via JS."""
        _close_dialog(view_page, "dlg-size")
        view_page.locator("#btn-minmax").click()
        dlg = view_page.locator("#dlg-minmax")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        expect(dlg).to_contain_text("MinMax")
        # Min/max are set as inline styles on the overlay's inner overlay
        overlay = dlg.locator("vaadin-dialog-overlay")
        style = overlay.evaluate("el => el.$.overlay.style.cssText")
        assert "min-width: 300px" in style
        assert "max-width: 800px" in style
        assert "min-height: 200px" in style
        assert "max-height: 600px" in style
        view_page.keyboard.press("Escape")
        expect(dlg).not_to_have_attribute("opened", "")

    @pytest.mark.spec("V11.11")
    def test_close_listener(self, view_page: Page):
        _close_dialog(view_page, "dlg-minmax")
        view_page.locator("#btn-cls").click()
        dlg = view_page.locator("#dlg-cls")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        view_page.keyboard.press("Escape")
        expect(view_page.locator("#dlg-closed")).to_have_text("closed", timeout=3000)


class TestDialogResizeListener:
    @pytest.mark.spec("V11.12")
    def test_resize_listener_dialog_opens(self, view_page: Page):
        view_page.locator("#btn-resize-listen").click()
        dlg = view_page.locator("#dlg-resize-listen")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        expect(dlg).to_have_js_property("resizable", True)
        view_page.keyboard.press("Escape")
        expect(dlg).not_to_have_attribute("opened", "")


class TestConfirmDialog:
    @pytest.mark.spec("V11.13")
    def test_confirm(self, view_page: Page):
        view_page.locator("#btn-cd").click()
        dlg = view_page.locator("#cd1[opened]")
        expect(dlg).to_contain_text("Are you sure?", timeout=3000)
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

    @pytest.mark.spec("V11.16")
    def test_confirm_dialog_button_themes(self, view_page: Page):
        """ConfirmDialog with themed buttons."""
        view_page.locator("#btn-cd-reject").click()
        dlg = view_page.locator("#cd-reject[opened]")
        expect(dlg).to_have_attribute("opened", "", timeout=3000)
        # Verify the confirm-button has theme "primary error"
        expect(dlg).to_have_js_property("confirmTheme", "primary error")
        # Close
        dlg.locator("vaadin-button").filter(has_text="Delete").click()
        view_page.wait_for_timeout(200)

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
    @pytest.mark.spec("V11.22")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        for _ in range(3):
            view_page.keyboard.press("Escape")
        view_page.locator("vaadin-side-nav-item[path='/test/notification-popover']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/notification-popover"), timeout=5000)
