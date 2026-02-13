"""UI Tests — View 15: Layouts (/test/layouts)"""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def view_page(shared_page, base_url):
    """Reuse shared page — navigate via SideNav or goto fallback."""
    from conftest import navigate_to
    navigate_to(shared_page, base_url, "test/layouts", "vaadin-horizontal-layout")
    yield shared_page


class TestVerticalLayout:
    @pytest.mark.spec("V15.01")
    def test_renders_children(self, view_page: Page):
        vl = view_page.locator("#vl1")
        expect(vl).to_contain_text("A")
        expect(vl).to_contain_text("B")
        expect(vl).to_contain_text("C")

    @pytest.mark.spec("V15.04")
    def test_expand(self, view_page: Page):
        child = view_page.locator("#child-expand")
        expect(child).to_be_visible()

    @pytest.mark.spec("V15.07")
    def test_add_dynamically(self, view_page: Page):
        view_page.locator("#btn-add-span").click()
        vl = view_page.locator("#vl-dyn")
        expect(vl).to_contain_text("New")

    @pytest.mark.spec("V15.08")
    def test_replace(self, view_page: Page):
        view_page.locator("#btn-replace").click()
        vl = view_page.locator("#vl-replace")
        expect(vl).to_contain_text("Replaced")


class TestVerticalLayoutAddFirst:
    @pytest.mark.spec("V15.22")
    def test_add_component_as_first(self, view_page: Page):
        vl = view_page.locator("#vl-first")
        # Initially has "Second" and "Third"
        expect(vl).to_contain_text("Second")
        expect(vl).to_contain_text("Third")
        # Click button to add "First" at index 0
        view_page.locator("#btn-add-first").click()
        expect(vl).to_contain_text("First")
        # Verify "First" appears before "Second" in DOM order
        texts = vl.locator("span").all_text_contents()
        first_idx = texts.index("First") if "First" in texts else -1
        second_idx = texts.index("Second") if "Second" in texts else -1
        assert first_idx < second_idx, f"Expected 'First' before 'Second', got {texts}"


class TestHorizontalLayout:
    @pytest.mark.spec("V15.09")
    def test_renders_children(self, view_page: Page):
        hl = view_page.locator("#hl1")
        expect(hl).to_contain_text("L")
        expect(hl).to_contain_text("R")

    @pytest.mark.spec("V15.10")
    def test_expand(self, view_page: Page):
        expect(view_page.locator("#hl-child")).to_be_visible()


class TestFlexLayout:
    @pytest.mark.spec("V15.13")
    def test_column_direction(self, view_page: Page):
        fl = view_page.locator("#fl1")
        expect(fl).to_be_visible()

    @pytest.mark.spec("V15.14")
    def test_wrap(self, view_page: Page):
        fl = view_page.locator("#fl-wrap")
        expect(fl).to_be_visible()


class TestFormLayout:
    @pytest.mark.spec("V15.16")
    def test_renders_fields(self, view_page: Page):
        form = view_page.locator("#form1")
        expect(form.locator("vaadin-text-field")).to_have_count(4)


class TestSplitLayout:
    @pytest.mark.spec("V15.18")
    def test_renders_panels(self, view_page: Page):
        split = view_page.locator("#split1")
        expect(split).to_contain_text("Primary")
        expect(split).to_contain_text("Secondary")


class TestNavigation:
    @pytest.mark.spec("V15.21")
    def test_nav_via_sidenav(self, view_page: Page):
        """Navigate to next view via SideNav link."""
        view_page.locator("vaadin-side-nav-item[path='/test/html-elements']").click()
        expect(view_page).to_have_url(re.compile(r".*/test/html-elements"), timeout=5000)
