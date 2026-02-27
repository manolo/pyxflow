"""Tests for error handling in RPC processing and navigation.

Verifies that user code exceptions (click listeners, view constructors,
property sync callbacks) are caught gracefully and result in an error
notification rather than crashing the server.
"""

import pytest

from pyflow.server.uidl_handler import UidlHandler
from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature
from pyflow.core.component import Component
from pyflow.core.element import Element
from pyflow.components.vertical_layout import VerticalLayout
from pyflow.components.button import Button
from pyflow.components.text_field import TextField
from pyflow.router import Route, clear_routes


def _find_notification_in_changes(changes):
    """Find vaadin-notification node in response changes."""
    for change in changes:
        if change.get("key") == "tag" and change.get("value") == "vaadin-notification":
            return change.get("node")
    return None


def _get_node_properties(changes, node_id):
    """Get all Feature 1 (property) changes for a given node."""
    props = {}
    for change in changes:
        if change.get("node") == node_id and change.get("feat") == Feature.ELEMENT_PROPERTY_MAP:
            props[change["key"]] = change.get("value")
    return props


def _get_node_attributes(changes, node_id):
    """Get all Feature 3 (attribute) changes for a given node."""
    attrs = {}
    for change in changes:
        if change.get("node") == node_id and change.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP:
            attrs[change["key"]] = change.get("value")
    return attrs


class TestClickListenerException:
    """Test that exceptions in click listeners are caught gracefully."""

    @pytest.fixture(autouse=True)
    def setup_routes(self):
        """Register a test view with a broken click listener."""
        clear_routes()

        @Route("error-click")
        class ErrorClickView(VerticalLayout):
            def __init__(self):
                super().__init__()
                btn = Button("Explode")
                btn.add_click_listener(lambda e: (_ for _ in ()).throw(ValueError("boom")))
                # Use a simpler approach
                def explode(e):
                    raise ValueError("boom")
                btn._click_listeners = []
                btn.add_click_listener(explode)
                self.add(btn)

        yield
        clear_routes()

    def _navigate_and_get_session(self):
        tree = StateTree()
        handler = UidlHandler(tree)
        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        nav_payload = {
            "csrfToken": csrf,
            "rpc": [{"type": "event", "node": 1, "event": "ui-navigate",
                      "data": {"route": "error-click", "query": "",
                               "appShellTitle": "", "historyState": {"idx": 0},
                               "trigger": ""}}],
            "syncId": 0, "clientId": 0,
        }
        nav_response = handler.handle_uidl(nav_payload)

        button_node_id = None
        for change in nav_response.get("changes", []):
            if change.get("key") == "tag" and change.get("value") == "vaadin-button":
                button_node_id = change.get("node")

        return {
            "handler": handler, "tree": tree, "csrf": csrf,
            "sync_id": nav_response["syncId"],
            "client_id": nav_response.get("clientId", 0),
            "button_node_id": button_node_id,
        }

    def test_click_listener_exception_does_not_crash(self):
        """Click listener raises -> response still valid (HTTP 200, not 500)."""
        session = self._navigate_and_get_session()
        assert session["button_node_id"] is not None

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{"type": "event", "node": session["button_node_id"],
                      "event": "click", "data": {}}],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        # Should NOT raise — exception is caught internally
        response = session["handler"].handle_uidl(payload)
        assert "syncId" in response
        assert "changes" in response

    def test_click_listener_exception_shows_notification(self):
        """Click listener raises -> response contains notification node."""
        session = self._navigate_and_get_session()
        assert session["button_node_id"] is not None

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{"type": "event", "node": session["button_node_id"],
                      "event": "click", "data": {}}],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)
        changes = response.get("changes", [])

        notification_node = _find_notification_in_changes(changes)
        assert notification_node is not None, "Error notification should be in response"

    def test_error_notification_has_error_theme(self):
        """Error notification should have theme='error'."""
        session = self._navigate_and_get_session()
        assert session["button_node_id"] is not None

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{"type": "event", "node": session["button_node_id"],
                      "event": "click", "data": {}}],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)
        changes = response.get("changes", [])

        notification_node = _find_notification_in_changes(changes)
        assert notification_node is not None

        attrs = _get_node_attributes(changes, notification_node)
        assert "error" in attrs.get("theme", ""), "Notification should have error theme"


class TestNavigationError:
    """Test that exceptions in view constructors show error notification."""

    @pytest.fixture(autouse=True)
    def setup_routes(self):
        clear_routes()

        @Route("error-view")
        class ErrorView(VerticalLayout):
            def __init__(self):
                super().__init__()
                raise RuntimeError("View constructor exploded")

        yield
        clear_routes()

    def test_navigation_error_shows_notification(self):
        """Bad view constructor -> notification in response."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        nav_payload = {
            "csrfToken": csrf,
            "rpc": [{"type": "event", "node": 1, "event": "ui-navigate",
                      "data": {"route": "error-view", "query": "",
                               "appShellTitle": "", "historyState": {"idx": 0},
                               "trigger": ""}}],
            "syncId": 0, "clientId": 0,
        }
        response = handler.handle_uidl(nav_payload)
        changes = response.get("changes", [])

        notification_node = _find_notification_in_changes(changes)
        assert notification_node is not None, "Error notification should appear for broken view"


class TestMSyncException:
    """Test that exceptions in property sync handlers are caught."""

    @pytest.fixture(autouse=True)
    def setup_routes(self):
        clear_routes()

        @Route("error-sync")
        class ErrorSyncView(VerticalLayout):
            def __init__(self):
                super().__init__()
                self.tf = TextField("Name")
                self.tf.add_value_change_listener(self._on_change)
                self.add(self.tf)

            def _on_change(self, event):
                raise RuntimeError("sync handler exploded")

        yield
        clear_routes()

    def test_msync_exception_does_not_crash(self):
        """Property sync handler raises -> response still valid."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        nav_payload = {
            "csrfToken": csrf,
            "rpc": [{"type": "event", "node": 1, "event": "ui-navigate",
                      "data": {"route": "error-sync", "query": "",
                               "appShellTitle": "", "historyState": {"idx": 0},
                               "trigger": ""}}],
            "syncId": 0, "clientId": 0,
        }
        nav_response = handler.handle_uidl(nav_payload)

        # Find the text field node
        tf_node_id = None
        for change in nav_response.get("changes", []):
            if change.get("key") == "tag" and change.get("value") == "vaadin-text-field":
                tf_node_id = change.get("node")
        assert tf_node_id is not None

        # Send mSync with value change
        sync_payload = {
            "csrfToken": csrf,
            "rpc": [{"type": "mSync", "node": tf_node_id,
                      "feature": Feature.ELEMENT_PROPERTY_MAP,
                      "property": "value", "value": "hello"}],
            "syncId": nav_response["syncId"],
            "clientId": nav_response.get("clientId", 0),
        }
        response = handler.handle_uidl(sync_payload)
        assert "syncId" in response
        assert "changes" in response


class TestMultipleRpcsPartialFailure:
    """Test that first RPC failing doesn't prevent second from executing."""

    @pytest.fixture(autouse=True)
    def setup_routes(self):
        clear_routes()
        self.second_executed = False

        @Route("multi-rpc")
        class MultiRpcView(VerticalLayout):
            def __init__(inner_self):
                super(MultiRpcView, inner_self).__init__()
                btn1 = Button("Broken")
                btn2 = Button("Working")

                def explode(e):
                    raise ValueError("first RPC fails")

                outer = self

                def succeed(e):
                    outer.second_executed = True

                btn1.add_click_listener(explode)
                btn2.add_click_listener(succeed)
                inner_self.add(btn1, btn2)

        yield
        clear_routes()

    def test_multiple_rpcs_partial_failure(self):
        """2 RPCs, first throws, second still executes."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        nav_payload = {
            "csrfToken": csrf,
            "rpc": [{"type": "event", "node": 1, "event": "ui-navigate",
                      "data": {"route": "multi-rpc", "query": "",
                               "appShellTitle": "", "historyState": {"idx": 0},
                               "trigger": ""}}],
            "syncId": 0, "clientId": 0,
        }
        nav_response = handler.handle_uidl(nav_payload)

        # Find both button nodes
        button_nodes = []
        for change in nav_response.get("changes", []):
            if change.get("key") == "tag" and change.get("value") == "vaadin-button":
                button_nodes.append(change.get("node"))
        assert len(button_nodes) >= 2, "Should have at least 2 buttons"

        # Send 2 click RPCs in one request — first should fail, second should succeed
        payload = {
            "csrfToken": csrf,
            "rpc": [
                {"type": "event", "node": button_nodes[0], "event": "click", "data": {}},
                {"type": "event", "node": button_nodes[1], "event": "click", "data": {}},
            ],
            "syncId": nav_response["syncId"],
            "clientId": nav_response.get("clientId", 0),
        }
        response = handler.handle_uidl(payload)
        assert "syncId" in response
        assert self.second_executed, "Second RPC should execute even though first failed"
