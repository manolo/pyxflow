"""Tests for @StyleSheet decorator and EAGER dependency loading."""

import pytest

from pyflow.router import Route, StyleSheet, AppShell, Push, clear_routes, clear_app_shell
from pyflow.components import VerticalLayout
from pyflow.server.uidl_handler import UidlHandler
from pyflow.core.state_tree import StateTree


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
        clear_app_shell()
        yield
        clear_routes()
        clear_app_shell()

    def _make_session(self):
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return handler, csrf, {"sync_id": 0, "client_id": 0}

    def _navigate(self, handler, csrf, route="", state=None):
        sync_id = state["sync_id"] if state else 0
        client_id = state["client_id"] if state else 0
        payload = {
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": route},
            }],
            "syncId": sync_id,
            "clientId": client_id,
        }
        response = handler.handle_uidl(payload)
        if state is not None:
            state["sync_id"] = response["syncId"]
            state["client_id"] = client_id + 1
        return response

    def test_eager_deps_in_navigation_response(self):
        """Navigation to view with @StyleSheet should include EAGER deps."""
        @Route("")
        @StyleSheet("styles/test.css")
        class StyledView(VerticalLayout):
            pass

        handler, csrf, state = self._make_session()
        response = self._navigate(handler, csrf, state=state)

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

        handler, csrf, state = self._make_session()
        response = self._navigate(handler, csrf, state=state)

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

        handler, csrf, state = self._make_session()
        resp1 = self._navigate(handler, csrf, "", state=state)
        assert "EAGER" in resp1

        # Navigate to second view with same stylesheet
        resp2 = self._navigate(handler, csrf, "other", state=state)
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

        handler, csrf, state = self._make_session()
        response = self._navigate(handler, csrf, state=state)

        assert "EAGER" in response
        urls = [d["url"] for d in response["EAGER"]]
        assert "styles/layout.css" in urls
        assert "styles/view.css" in urls


class TestAppShellStylesheets:
    """Test that @AppShell stylesheets appear in init response."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        clear_app_shell()
        yield
        clear_routes()
        clear_app_shell()

    def test_app_shell_stylesheets_in_init(self):
        """@AppShell @StyleSheet should include EAGER deps in init UIDL."""
        @AppShell
        @StyleSheet("styles/global.css")
        class MyShell:
            pass

        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        uidl = init_response["appConfig"]["uidl"]

        assert "EAGER" in uidl
        assert len(uidl["EAGER"]) == 1
        dep = uidl["EAGER"][0]
        assert dep["type"] == "STYLESHEET"
        assert dep["url"] == "styles/global.css"
        assert dep["loadMode"] == "EAGER"

    def test_app_shell_multiple_stylesheets(self):
        """Multiple stylesheets on AppShell should all appear in init."""
        @AppShell
        @StyleSheet("lumo/lumo.css", "styles/app.css")
        class MyShell:
            pass

        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        uidl = init_response["appConfig"]["uidl"]

        assert "EAGER" in uidl
        urls = [d["url"] for d in uidl["EAGER"]]
        assert "lumo/lumo.css" in urls
        assert "styles/app.css" in urls

    def test_app_shell_stylesheets_not_resent_on_navigation(self):
        """Stylesheets sent in init should not be resent on navigation."""
        @AppShell
        @StyleSheet("styles/global.css")
        class MyShell:
            pass

        @Route("")
        @StyleSheet("styles/global.css")  # Same as AppShell
        class MyView(VerticalLayout):
            pass

        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]

        # Navigate — should NOT resend styles/global.css
        payload = {
            "csrfToken": csrf,
            "rpc": [{"type": "event", "node": 1, "event": "ui-navigate", "data": {"route": ""}}],
            "syncId": 0,
            "clientId": 0,
        }
        response = handler.handle_uidl(payload)
        assert "EAGER" not in response

    def test_no_eager_in_init_without_app_shell(self):
        """Init should not have EAGER if no @AppShell is registered."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        uidl = init_response["appConfig"]["uidl"]

        assert "EAGER" not in uidl


class TestConditionalPush:
    """Test that push config is conditional on @AppShell @Push."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        clear_app_shell()
        yield
        clear_routes()
        clear_app_shell()

    def test_no_push_script_without_push(self):
        """Init should not include pushScript without @Push."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})

        assert "pushScript" not in init_response

    def test_push_script_with_push(self):
        """Init should include pushScript with @AppShell @Push."""
        @AppShell
        @Push
        class MyShell:
            pass

        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})

        assert "pushScript" in init_response
        assert init_response["pushScript"] == "VAADIN/static/push/vaadinPush.js"

    def test_push_mode_in_changes_with_push(self):
        """Push mode AUTOMATIC should be in init changes when @Push is set."""
        @AppShell
        @Push
        class MyShell:
            pass

        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        changes = init_response["appConfig"]["uidl"]["changes"]

        push_change = next(
            (c for c in changes if c.get("key") == "pushMode" and c.get("value") == "AUTOMATIC"),
            None
        )
        assert push_change is not None

    def test_no_push_mode_without_push(self):
        """Push mode should NOT be in init changes without @Push."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        changes = init_response["appConfig"]["uidl"]["changes"]

        push_change = next(
            (c for c in changes if c.get("key") == "pushMode"),
            None
        )
        assert push_change is None

    def test_container_node_id_without_push(self):
        """Without push, container should be node 2 (no push params node)."""
        tree = StateTree()
        handler = UidlHandler(tree)
        handler.handle_init({})

        assert handler._container_node.id == 2

    def test_container_node_id_with_push(self):
        """With push, container should be node 3 (push params at node 2)."""
        @AppShell
        @Push
        class MyShell:
            pass

        tree = StateTree()
        handler = UidlHandler(tree)
        handler.handle_init({})

        assert handler._container_node.id == 3
