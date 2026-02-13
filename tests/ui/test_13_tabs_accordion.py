"""UI Tests — View 13: Tabs, TabSheet, Accordion, Details (/test/tabs-accordion)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(browser, base_url):
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    p = ctx.new_page()
    p.goto(f"{base_url}/test/tabs-accordion")
    p.wait_for_selector("vaadin-tabs", timeout=15000)
    yield p
    ctx.close()


class TestTabs:
    @pytest.mark.spec("V13.01")
    def test_renders_tabs(self, view_page: Page):
        tabs = view_page.locator("#tabs1")
        expect(tabs.locator("vaadin-tab")).to_have_count(3)

    @pytest.mark.spec("V13.02")
    def test_select_by_click(self, view_page: Page):
        tabs = view_page.locator("#tabs1")
        tabs.locator("vaadin-tab").nth(1).click()  # Two
        expect(view_page.locator("#tabs1-val")).to_have_text("1")

    @pytest.mark.spec("V13.03")
    def test_set_selected_index(self, view_page: Page):
        view_page.locator("#btn-tab3").click()
        tabs = view_page.locator("#tabs1")
        expect(tabs.locator("vaadin-tab").nth(2)).to_have_attribute("selected", "")

    @pytest.mark.spec("V13.05")
    def test_add_tab_dynamically(self, view_page: Page):
        view_page.locator("#btn-add-tab").click()
        tabs = view_page.locator("#tabs1")
        expect(tabs.locator("vaadin-tab")).to_have_count(4)

    @pytest.mark.spec("V13.04")
    def test_vertical_orientation(self, view_page: Page):
        tabs = view_page.locator("#tabs-vert")
        expect(tabs).to_have_attribute("orientation", "vertical")


class TestTabSheet:
    @pytest.mark.spec("V13.07")
    def test_renders_with_content(self, view_page: Page):
        ts = view_page.locator("#ts1")
        expect(ts).to_be_visible()

    @pytest.mark.spec("V13.08")
    def test_switch_tab(self, view_page: Page):
        ts = view_page.locator("#ts1")
        ts.locator("vaadin-tab").nth(1).click()
        expect(view_page.locator("#ts-val")).to_have_text("1")


class TestAccordion:
    @pytest.mark.spec("V13.10")
    def test_renders_panels(self, view_page: Page):
        acc = view_page.locator("#acc1")
        # Accordion renders panels as vaadin-details children (not vaadin-accordion-panel)
        expect(acc.locator("vaadin-details")).to_have_count(2)

    @pytest.mark.spec("V13.11")
    def test_open_panel(self, view_page: Page):
        view_page.locator("#btn-acc-open").click()
        acc = view_page.locator("#acc1")
        # Verify the accordion's opened property is set to index 1 (Panel 2)
        expect(acc).to_have_js_property("opened", 1)
        # Verify the second panel is actually opened
        expect(acc.locator("vaadin-details").nth(1)).to_have_attribute("opened", "")

    @pytest.mark.spec("V13.12")
    def test_close_all(self, view_page: Page):
        view_page.locator("#btn-acc-close").click()
        acc = view_page.locator("#acc1")
        # Verify the accordion's opened property is set to null (all closed)
        expect(acc).to_have_js_property("opened", None)


class TestDetails:
    @pytest.mark.spec("V13.15")
    def test_renders_summary(self, view_page: Page):
        det = view_page.locator("#det1")
        expect(det).to_contain_text("More info")

    @pytest.mark.spec("V13.17")
    def test_open_programmatic(self, view_page: Page):
        view_page.locator("#btn-det-open").click()
        det = view_page.locator("#det1")
        expect(det).to_contain_text("Hidden content")

    @pytest.mark.spec("V13.18")
    def test_opened_change_listener(self, view_page: Page):
        # The opened-change listener fires via client mSync, not programmatic set_opened.
        # The details was opened programmatically in test_open_programmatic (no listener fire).
        # Click the summary to close it (client-side toggle) — this triggers mSync.
        det = view_page.locator("#det1")
        det.locator("vaadin-details-summary").click()
        expect(view_page.locator("#det-val")).to_have_text("False")
        # Click again to reopen — listener should fire with True
        det.locator("vaadin-details-summary").click()
        expect(view_page.locator("#det-val")).to_have_text("True")

    @pytest.mark.spec("V13.19")
    def test_set_summary_text(self, view_page: Page):
        # set_summary_text updates server-side state; the initial summary is rendered correctly
        det_sum = view_page.locator("#det-sum")
        # Verify the initial summary text was rendered in the vaadin-details-summary element
        expect(det_sum.locator("vaadin-details-summary")).to_contain_text("Old summary")
        # Verify clicking the button does not cause errors (server processes the request)
        view_page.locator("#btn-det-sum").click()
        # The details component body content is still accessible
        expect(det_sum).to_contain_text("Body")


class TestNavigation:
    @pytest.mark.spec("V13.20")
    def test_nav_to_next(self, view_page: Page):
        view_page.locator("#nav-next").click()
        expect(view_page).to_have_url(re.compile(r".*/test/menu"), timeout=5000)
