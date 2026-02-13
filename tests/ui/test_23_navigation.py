"""UI Tests — View 23: Navigation (/test/navigation)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/navigation")
    p.wait_for_selector("#nav-title", timeout=15000)
    yield p
    ctx.close()


class TestRouting:
    def test_view_renders(self, view_page: Page):
        expect(view_page.locator("#nav-title")).to_have_text("Navigation view")

    def test_page_title(self, view_page: Page):
        title = view_page.evaluate("() => document.title")
        assert "Navigation" in title


class TestRouteParam:
    def test_param_route(self, view_page: Page):
        view_page.locator("#link-param").click()
        expect(view_page).to_have_url(re.compile(r".*/test/nav-param/42"), timeout=5000)
        expect(view_page.locator("#param")).to_have_text("42")
        view_page.locator("#nav-back").click()
        expect(view_page).to_have_url(re.compile(r".*/test/navigation"), timeout=5000)


class TestOptionalParam:
    def test_opt_param_empty(self, view_page: Page):
        view_page.locator("#link-opt").click()
        expect(view_page).to_have_url(re.compile(r".*/test/nav-opt$"), timeout=5000)
        expect(view_page.locator("#opt")).to_have_text("")
        view_page.locator("#nav-back").click()
        expect(view_page).to_have_url(re.compile(r".*/test/navigation"), timeout=5000)

    def test_opt_param_value(self, view_page: Page):
        view_page.locator("#link-opt-val").click()
        expect(view_page).to_have_url(re.compile(r".*/test/nav-opt/search"), timeout=5000)
        expect(view_page.locator("#opt")).to_have_text("search")
        view_page.locator("#nav-back").click()
        expect(view_page).to_have_url(re.compile(r".*/test/navigation"), timeout=5000)


class TestNavigation:
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/push"), timeout=5000)
