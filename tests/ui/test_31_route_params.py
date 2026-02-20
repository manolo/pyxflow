"""UI Tests -- View 31: Enhanced Route Parameters"""

import pytest
from playwright.sync_api import Page, expect


class TestWildcardRoute:
    """V31.01: Wildcard parameter matching."""

    @pytest.mark.spec("V31.01")
    def test_wildcard_single_segment(self, shared_page: Page, base_url):
        shared_page.goto(f"{base_url}/test/files/readme.txt")
        expect(shared_page.locator("#wildcard-path")).to_have_text("readme.txt", timeout=5000)
        expect(shared_page.locator("#wildcard-segments")).to_have_text("readme.txt")

    @pytest.mark.spec("V31.01")
    def test_wildcard_multiple_segments(self, shared_page: Page, base_url):
        shared_page.goto(f"{base_url}/test/files/docs/api/v2/spec.json")
        expect(shared_page.locator("#wildcard-path")).to_have_text("docs/api/v2/spec.json", timeout=5000)
        expect(shared_page.locator("#wildcard-segments")).to_have_text("docs,api,v2,spec.json")

    @pytest.mark.spec("V31.01")
    def test_wildcard_no_segments(self, shared_page: Page, base_url):
        shared_page.goto(f"{base_url}/test/files")
        expect(shared_page.locator("#wildcard-path")).to_have_text("", timeout=5000)
        expect(shared_page.locator("#wildcard-segments")).to_have_text("")


class TestMidPositionOptional:
    """V31.02: Mid-position optional parameter."""

    @pytest.mark.spec("V31.02")
    def test_mid_optional_present(self, shared_page: Page, base_url):
        shared_page.goto(f"{base_url}/test/user/42/profile")
        expect(shared_page.locator("#mid-opt-id")).to_have_text("42", timeout=5000)
        expect(shared_page.locator("#mid-opt-has-id")).to_have_text("yes")

    @pytest.mark.spec("V31.02")
    def test_mid_optional_absent(self, shared_page: Page, base_url):
        shared_page.goto(f"{base_url}/test/user/profile")
        expect(shared_page.locator("#mid-opt-id")).to_have_text("", timeout=5000)
        expect(shared_page.locator("#mid-opt-has-id")).to_have_text("no")


class TestQueryParameters:
    """V31.03: Query parameter parsing via BeforeEnterEvent."""

    @pytest.mark.spec("V31.03")
    def test_query_params_parsed(self, shared_page: Page, base_url):
        shared_page.goto(f"{base_url}/test/search-params?q=hello&sort=name")
        expect(shared_page.locator("#search-q")).to_have_text("hello", timeout=5000)
        expect(shared_page.locator("#search-sort")).to_have_text("name")
        expect(shared_page.locator("#search-path")).to_have_text("test/search-params")

    @pytest.mark.spec("V31.03")
    def test_no_query_params(self, shared_page: Page, base_url):
        shared_page.goto(f"{base_url}/test/search-params")
        expect(shared_page.locator("#search-q")).to_have_text("", timeout=5000)
        expect(shared_page.locator("#search-sort")).to_have_text("")


class TestBeforeEnterEventCompat:
    """V31.04: BeforeEnterEvent dict-compatibility."""

    @pytest.mark.spec("V31.04")
    def test_event_dict_access(self, shared_page: Page, base_url):
        shared_page.goto(f"{base_url}/test/event-compat/99")
        expect(shared_page.locator("#compat-id")).to_have_text("99", timeout=5000)
        expect(shared_page.locator("#compat-has-event")).to_have_text("yes")
        expect(shared_page.locator("#compat-int-id")).to_have_text("99")
