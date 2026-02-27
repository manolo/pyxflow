"""Tests for enhanced route parameter support: data classes, wildcards, mid-optionals, query params."""

import pytest

from pyflow.router import (
    BeforeEnterEvent,
    Location,
    QueryParameters,
    Route,
    RouteParameters,
    clear_routes,
    match_route,
)
from pyflow.components import VerticalLayout


# ---------------------------------------------------------------------------
# QueryParameters
# ---------------------------------------------------------------------------

class TestQueryParameters:
    def test_from_string_single(self):
        qp = QueryParameters.from_string("key=val")
        assert qp.get_single_parameter("key") == "val"

    def test_from_string_multiple_values(self):
        qp = QueryParameters.from_string("tag=a&tag=b&tag=c")
        assert qp.get_parameters("tag") == ["a", "b", "c"]
        assert qp.get_single_parameter("tag") == "a"

    def test_from_string_multiple_keys(self):
        qp = QueryParameters.from_string("name=foo&age=30")
        assert qp.get_single_parameter("name") == "foo"
        assert qp.get_single_parameter("age") == "30"

    def test_missing_key_returns_none(self):
        qp = QueryParameters.from_string("x=1")
        assert qp.get_single_parameter("y") is None
        assert qp.get_parameters("y") == []

    def test_empty_string(self):
        qp = QueryParameters.from_string("")
        assert not qp
        assert qp.get_parameter_names() == set()

    def test_empty_factory(self):
        qp = QueryParameters.empty()
        assert not qp

    def test_blank_value(self):
        qp = QueryParameters.from_string("key=")
        assert qp.get_single_parameter("key") == ""

    def test_parameter_names(self):
        qp = QueryParameters.from_string("a=1&b=2&c=3")
        assert qp.get_parameter_names() == {"a", "b", "c"}

    def test_equality(self):
        a = QueryParameters.from_string("x=1&y=2")
        b = QueryParameters.from_string("x=1&y=2")
        assert a == b

    def test_truthiness(self):
        assert not QueryParameters.empty()
        assert QueryParameters.from_string("x=1")

    def test_repr(self):
        qp = QueryParameters.from_string("k=v")
        assert "QueryParameters" in repr(qp)


# ---------------------------------------------------------------------------
# RouteParameters
# ---------------------------------------------------------------------------

class TestRouteParameters:
    def test_get(self):
        rp = RouteParameters({"id": "42", "name": "alice"})
        assert rp.get("id") == "42"
        assert rp.get("missing") is None

    def test_get_integer(self):
        rp = RouteParameters({"id": "42", "slug": "abc"})
        assert rp.get_integer("id") == 42
        assert rp.get_integer("slug") is None
        assert rp.get_integer("missing") is None

    def test_get_wildcard(self):
        rp = RouteParameters({"path": "a/b/c"})
        assert rp.get_wildcard("path") == ["a", "b", "c"]

    def test_get_wildcard_empty(self):
        rp = RouteParameters({})
        assert rp.get_wildcard("path") == []

    def test_get_wildcard_single(self):
        rp = RouteParameters({"path": "readme.txt"})
        assert rp.get_wildcard("path") == ["readme.txt"]

    def test_dict_like_access(self):
        rp = RouteParameters({"id": "42"})
        assert rp["id"] == "42"
        assert "id" in rp
        assert "missing" not in rp
        assert list(rp.keys()) == ["id"]
        assert list(rp.values()) == ["42"]
        assert list(rp.items()) == [("id", "42")]

    def test_dict_like_keyerror(self):
        rp = RouteParameters({})
        with pytest.raises(KeyError):
            _ = rp["missing"]

    def test_equality(self):
        assert RouteParameters({"a": "1"}) == RouteParameters({"a": "1"})
        assert RouteParameters({"a": "1"}) != RouteParameters({"a": "2"})

    def test_parameter_names(self):
        rp = RouteParameters({"id": "1", "name": "foo"})
        assert rp.get_parameter_names() == {"id", "name"}

    def test_truthiness(self):
        assert not RouteParameters({})
        assert RouteParameters({"id": "1"})


# ---------------------------------------------------------------------------
# Location
# ---------------------------------------------------------------------------

class TestLocation:
    def test_path_and_segments(self):
        loc = Location("users/42/edit")
        assert loc.path == "users/42/edit"
        assert loc.segments == ["users", "42", "edit"]

    def test_empty_path(self):
        loc = Location("")
        assert loc.path == ""
        assert loc.segments == []

    def test_first_segment(self):
        assert Location("users/42").first_segment == "users"
        assert Location("").first_segment == ""

    def test_query_parameters(self):
        qp = QueryParameters.from_string("sort=name")
        loc = Location("users", qp)
        assert loc.query_parameters.get_single_parameter("sort") == "name"

    def test_default_empty_query(self):
        loc = Location("users")
        assert not loc.query_parameters

    def test_strips_slashes(self):
        loc = Location("/users/")
        assert loc.path == "users"

    def test_equality(self):
        a = Location("users", QueryParameters.from_string("x=1"))
        b = Location("users", QueryParameters.from_string("x=1"))
        assert a == b


# ---------------------------------------------------------------------------
# BeforeEnterEvent
# ---------------------------------------------------------------------------

class TestBeforeEnterEvent:
    def _make_event(self, params=None, query="", path="test"):
        rp = RouteParameters(params or {})
        qp = QueryParameters.from_string(query)
        loc = Location(path, qp)
        return BeforeEnterEvent(location=loc, route_parameters=rp)

    def test_dict_compat_getitem(self):
        event = self._make_event({"id": "42"})
        assert event["id"] == "42"

    def test_dict_compat_get(self):
        event = self._make_event({"id": "42"})
        assert event.get("id") == "42"
        assert event.get("missing") is None
        assert event.get("missing", "default") == "default"

    def test_dict_compat_contains(self):
        event = self._make_event({"id": "42"})
        assert "id" in event
        assert "missing" not in event

    def test_dict_compat_keys(self):
        event = self._make_event({"id": "42", "name": "foo"})
        assert set(event.keys()) == {"id", "name"}

    def test_location_access(self):
        event = self._make_event(query="sort=name", path="users")
        assert event.location.path == "users"
        assert event.location.query_parameters.get_single_parameter("sort") == "name"

    def test_route_parameters_access(self):
        event = self._make_event({"id": "42"})
        assert event.route_parameters.get("id") == "42"
        assert event.route_parameters.get_integer("id") == 42

    def test_always_truthy(self):
        """BeforeEnterEvent is always truthy (unlike empty dict)."""
        event = self._make_event()
        assert event

    def test_properties(self):
        event = self._make_event()
        assert event.trigger == "router"
        assert event.navigation_target is None
        assert event.ui is None


# ---------------------------------------------------------------------------
# Wildcard routes
# ---------------------------------------------------------------------------

class TestWildcardRoutes:
    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        yield
        clear_routes()

    def test_wildcard_matches_no_segments(self):
        @Route("files/:path*")
        class FilesView(VerticalLayout):
            pass

        result = match_route("files")
        assert result is not None
        assert result[0] is FilesView
        assert result[2] == {}  # no path captured

    def test_wildcard_matches_one_segment(self):
        @Route("files/:path*")
        class FilesView(VerticalLayout):
            pass

        result = match_route("files/readme.txt")
        assert result is not None
        assert result[2] == {"path": "readme.txt"}

    def test_wildcard_matches_multiple_segments(self):
        @Route("files/:path*")
        class FilesView(VerticalLayout):
            pass

        result = match_route("files/docs/api/v2/spec.json")
        assert result is not None
        assert result[2] == {"path": "docs/api/v2/spec.json"}

    def test_wildcard_with_required_prefix(self):
        @Route("repo/:owner/:name/tree/:path*")
        class TreeView(VerticalLayout):
            pass

        result = match_route("repo/alice/mylib/tree/src/main/java")
        assert result is not None
        assert result[2] == {"owner": "alice", "name": "mylib", "path": "src/main/java"}

    def test_wildcard_must_be_last(self):
        with pytest.raises(ValueError, match="must be the last segment"):
            @Route("files/:path*/extra")
            class BadView(VerticalLayout):
                pass

    def test_wildcard_no_match(self):
        @Route("files/:path*")
        class FilesView(VerticalLayout):
            pass

        assert match_route("other") is None
        assert match_route("file") is None


# ---------------------------------------------------------------------------
# Mid-position optional parameters
# ---------------------------------------------------------------------------

class TestMidPositionOptionals:
    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        yield
        clear_routes()

    def test_mid_optional_present(self):
        @Route("user/:id?/contact")
        class ContactView(VerticalLayout):
            pass

        result = match_route("user/123/contact")
        assert result is not None
        assert result[0] is ContactView
        assert result[2] == {"id": "123"}

    def test_mid_optional_absent(self):
        @Route("user/:id?/contact")
        class ContactView(VerticalLayout):
            pass

        result = match_route("user/contact")
        assert result is not None
        assert result[0] is ContactView
        assert result[2] == {}  # id not present

    def test_trailing_optional_still_works(self):
        @Route("search/:q?")
        class SearchView(VerticalLayout):
            pass

        result_with = match_route("search/hello")
        assert result_with is not None
        assert result_with[2] == {"q": "hello"}

        result_without = match_route("search")
        assert result_without is not None
        assert result_without[2] == {}

    def test_multiple_mid_optionals(self):
        @Route("a/:x?/b/:y?/c")
        class MultiView(VerticalLayout):
            pass

        # Both present
        result = match_route("a/1/b/2/c")
        assert result is not None
        assert result[2] == {"x": "1", "y": "2"}

        # First absent
        result = match_route("a/b/2/c")
        assert result is not None
        assert result[2] == {"y": "2"}

        # Second absent
        result = match_route("a/1/b/c")
        assert result is not None
        assert result[2] == {"x": "1"}

        # Both absent
        result = match_route("a/b/c")
        assert result is not None
        assert result[2] == {}

    def test_required_params_still_work(self):
        """Required params should not be affected by the rewrite."""
        @Route("user/:id")
        class UserView(VerticalLayout):
            pass

        result = match_route("user/42")
        assert result is not None
        assert result[2] == {"id": "42"}

        assert match_route("user") is None

    def test_multi_segment_required(self):
        @Route("org/:org/team/:team/member/:id")
        class MemberView(VerticalLayout):
            pass

        result = match_route("org/acme/team/eng/member/42")
        assert result is not None
        assert result[2] == {"org": "acme", "team": "eng", "id": "42"}

    def test_max_optionals_exceeded(self):
        with pytest.raises(ValueError, match="Max 4 optional"):
            @Route("a/:a?/b/:b?/c/:c?/d/:d?/e/:e?")
            class TooManyView(VerticalLayout):
                pass
