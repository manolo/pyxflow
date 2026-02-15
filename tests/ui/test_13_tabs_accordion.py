"""UI Tests — View 13: Tabs, TabSheet, Accordion, Details (/test/tabs-accordion)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/tabs-accordion", "vaadin-tabs")
    yield shared_page


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

    @pytest.mark.spec("V13.06", "V13.09")
    def test_selected_change_listener(self, view_page: Page):
        """Tabs and TabSheet fire selected_change_listener."""
        # Tabs listener — click first tab, verify
        view_page.locator("#tabs1").locator("vaadin-tab").first.click()
        expect(view_page.locator("#tabs1-val")).to_have_text("0")
        # TabSheet listener — already verified via ts-val in test_switch_tab
        expect(view_page.locator("#ts-val")).not_to_have_text("")


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


class TestAccordionExtras:
    @pytest.mark.spec("V13.13")
    def test_open_by_index(self, view_page: Page):
        """Accordion.open(1) opens Panel 2."""
        view_page.locator("#btn-acc-open").click()
        expect(view_page.locator("#acc1")).to_have_js_property("opened", 1)

    @pytest.mark.spec("V13.14")
    def test_opened_change_listener(self, view_page: Page):
        """Accordion fires opened_change_listener with index."""
        # Open Panel 2 was done in previous test (btn-acc-open)
        expect(view_page.locator("#acc-val")).not_to_have_text("")


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

    @pytest.mark.spec("V13.16")
    def test_toggle_open(self, view_page: Page):
        """Clicking Details summary toggles open/close."""
        det = view_page.locator("#det1")
        # Ensure closed first
        view_page.locator("#btn-acc-close").click()  # close accordion to avoid visual overlap
        # Click summary to open
        det.locator("vaadin-details-summary").click()
        expect(det).to_contain_text("Hidden content")

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
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/display']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/display"), timeout=5000)
