"""Tests for @StyleSheet decorator and EAGER dependency loading."""

import pytest

from vaadin.flow.router import Route, StyleSheet, clear_routes
from vaadin.flow.components import VerticalLayout
from vaadin.flow.server.uidl_handler import UidlHandler
from vaadin.flow.core.state_tree import StateTree


class TestStyleSheetDecorator:
    """Test @StyleSheet decorator."""

    def test_single_stylesheet(self):
        """@StyleSheet should store URL on class."""
        @StyleSheet("styles/test.css")
        class MyView(VerticalLayout):
            pass

        assert MyView._stylesheets == ["styles/test.css"]

    def test_multiple_urls_in_one_decorator(self):
        """@StyleSheet with multiple args should store all URLs."""
        @StyleSheet("styles/a.css", "styles/b.css")
        class MyView(VerticalLayout):
            pass

        assert MyView._stylesheets == ["styles/a.css", "styles/b.css"]

    def test_stacked_decorators(self):
        """Multiple @StyleSheet decorators should accumulate."""
        @StyleSheet("styles/first.css")
        @StyleSheet("styles/second.css")
        class MyView(VerticalLayout):
            pass

        assert "styles/first.css" in MyView._stylesheets
        assert "styles/second.css" in MyView._stylesheets

    def test_no_stylesheet(self):
        """Class without @StyleSheet should not have _stylesheets."""
        class PlainView(VerticalLayout):
            pass

        assert not hasattr(PlainView, '_stylesheets')

    def test_decorator_preserves_class(self):
        """@StyleSheet should return the same class."""
        @StyleSheet("styles/test.css")
        class MyView(VerticalLayout):
            pass

        assert MyView.__name__ == "MyView"


class TestStyleSheetUidl:
    """Test that stylesheets appear as EAGER dependencies in UIDL responses."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        yield
        clear_routes()

    def _make_session(self):
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return handler, csrf

    def _navigate(self, handler, csrf, route=""):
        payload = {
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": route},
            }],
            "syncId": 0,
            "clientId": 0,
        }
        return handler.handle_uidl(payload)

    def test_eager_deps_in_navigation_response(self):
        """Navigation to view with @StyleSheet should include EAGER deps."""
        @Route("")
        @StyleSheet("styles/test.css")
        class StyledView(VerticalLayout):
            pass

        handler, csrf = self._make_session()
        response = self._navigate(handler, csrf)

        assert "EAGER" in response
        assert len(response["EAGER"]) == 1
        dep = response["EAGER"][0]
        assert dep["type"] == "STYLESHEET"
        assert dep["url"] == "styles/test.css"
        assert dep["loadMode"] == "EAGER"

    def test_no_eager_without_stylesheet(self):
        """Navigation to view without @StyleSheet should not have EAGER."""
        @Route("")
        class PlainView(VerticalLayout):
            pass

        handler, csrf = self._make_session()
        response = self._navigate(handler, csrf)

        assert "EAGER" not in response

    def test_stylesheets_not_resent(self):
        """Same stylesheet should not be sent twice."""
        @Route("")
        @StyleSheet("styles/test.css")
        class ViewA(VerticalLayout):
            pass

        @Route("other")
        @StyleSheet("styles/test.css")
        class ViewB(VerticalLayout):
            pass

        handler, csrf = self._make_session()
        resp1 = self._navigate(handler, csrf, "")
        assert "EAGER" in resp1

        # Navigate to second view with same stylesheet
        resp2 = self._navigate(handler, csrf, "other")
        # Should not resend
        assert "EAGER" not in resp2

    def test_layout_stylesheets_included(self):
        """Stylesheets from layout class should be included."""
        @StyleSheet("styles/layout.css")
        class MyLayout(VerticalLayout):
            def show_router_layout_content(self, view):
                self.add(view)
            def remove_router_layout_content(self, view):
                self.remove(view)

        @Route("", layout=MyLayout)
        @StyleSheet("styles/view.css")
        class StyledView(VerticalLayout):
            pass

        handler, csrf = self._make_session()
        response = self._navigate(handler, csrf)

        assert "EAGER" in response
        urls = [d["url"] for d in response["EAGER"]]
        assert "styles/layout.css" in urls
        assert "styles/view.css" in urls
