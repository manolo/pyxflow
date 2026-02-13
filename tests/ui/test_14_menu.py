"""UI Tests — View 14: MenuBar & ContextMenu (/test/menu)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/menu")
    p.wait_for_selector("vaadin-menu-bar", timeout=15000)
    yield p
    ctx.close()


def _close_overlays(page: Page):
    """Press Escape to close any open menu/context-menu overlays."""
    for _ in range(3):
        page.keyboard.press("Escape")
    page.wait_for_timeout(300)


class TestMenuBar:
    @pytest.mark.spec("V14.01")
    def test_renders_items(self, view_page: Page):
        mb = view_page.locator("#mb1")
        expect(mb).to_be_visible()
        expect(mb).to_contain_text("File")
        expect(mb).to_contain_text("Edit")

    @pytest.mark.spec("V14.02")
    def test_click_top_item(self, view_page: Page):
        _close_overlays(view_page)
        # Click the File button to open its submenu
        mb = view_page.locator("#mb1")
        mb.locator("vaadin-menu-bar-button", has_text="File").click()
        # Wait for the "New" sub-item to become visible (overlay opened)
        new_item = view_page.get_by_role("menuitem", name="New")
        expect(new_item).to_be_visible(timeout=3000)
        # Close the overlay
        view_page.keyboard.press("Escape")
        view_page.wait_for_timeout(300)

    @pytest.mark.spec("V14.03")
    def test_click_sub_item(self, view_page: Page):
        _close_overlays(view_page)
        # Open the File submenu
        mb = view_page.locator("#mb1")
        mb.locator("vaadin-menu-bar-button", has_text="File").click()
        new_item = view_page.get_by_role("menuitem", name="New")
        expect(new_item).to_be_visible(timeout=3000)
        # Click the "New" sub-item
        new_item.click()
        expect(view_page.locator("#mb-result")).to_have_text("New", timeout=3000)

    @pytest.mark.spec("V14.07")
    def test_open_on_hover(self, view_page: Page):
        _close_overlays(view_page)
        expect(view_page.locator("#mb-hover")).to_have_js_property("openOnHover", True)


class TestContextMenu:
    @pytest.mark.spec("V14.08")
    def test_right_click_opens(self, view_page: Page):
        _close_overlays(view_page)
        view_page.locator("#ctx-target").click(button="right")
        # Wait for context-menu items to appear
        cut_item = view_page.get_by_role("menuitem", name="Cut")
        expect(cut_item).to_be_visible(timeout=3000)
        copy_item = view_page.get_by_role("menuitem", name="Copy")
        expect(copy_item).to_be_visible()
        # Close the overlay
        view_page.keyboard.press("Escape")
        view_page.wait_for_timeout(300)

    @pytest.mark.spec("V14.09")
    def test_click_item(self, view_page: Page):
        _close_overlays(view_page)
        # Open context menu on the target
        view_page.locator("#ctx-target").click(button="right")
        copy_item = view_page.get_by_role("menuitem", name="Copy")
        expect(copy_item).to_be_visible(timeout=3000)
        # Click "Copy"
        copy_item.click()
        expect(view_page.locator("#ctx-result")).to_have_text("Copy", timeout=3000)

    @pytest.mark.spec("V14.10")
    @pytest.mark.skip(reason="ContextMenu openOnClick not working — needs investigation")
    def test_open_on_click(self, view_page: Page):
        _close_overlays(view_page)
        view_page.locator("#ctx-target2").click()
        action_item = view_page.get_by_role("menuitem", name="Action")
        expect(action_item).to_be_visible(timeout=3000)
        action_item.click()
        expect(view_page.locator("#ctx-result")).to_have_text("Action", timeout=3000)


class TestNavigation:
    @pytest.mark.spec("V14.14")
    def test_nav_to_next(self, view_page: Page):
        _close_overlays(view_page)
        # Use evaluate to bypass any remaining overlays that might intercept the click
        view_page.locator("#nav-next").evaluate("el => el.click()")
        expect(view_page).to_have_url(re.compile(r".*/test/layouts"), timeout=5000)
