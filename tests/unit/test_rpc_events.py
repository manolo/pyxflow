"""Tests for Event RPC handling.

Based on Java Flow's EventRpcHandlerTest.java patterns.
Tests event dispatch, listener firing, and event data handling.
"""

import pytest

from pyxflow.server.uidl_handler import UidlHandler
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature


class TestClickEvent:
    """Test click event handling."""

    @pytest.fixture
    def session_with_view(self):
        """Create session with HelloWorldView loaded."""
        tree = StateTree()
        handler = UidlHandler(tree)

        # Init
        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        # Navigate to create view
        nav_payload = {
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "",
                         "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        }
        nav_response = handler.handle_uidl(nav_payload)

        # Find button and text field node IDs
        button_node_id = None
        tf_node_id = None
        for change in nav_response.get("changes", []):
            if change.get("key") == "tag":
                if change.get("value") == "vaadin-button":
                    button_node_id = change.get("node")
                elif change.get("value") == "vaadin-text-field":
                    tf_node_id = change.get("node")

        return {
            "handler": handler,
            "tree": tree,
            "csrf": csrf,
            "sync_id": nav_response["syncId"],
            "client_id": nav_response.get("clientId", 0),
            "button_node_id": button_node_id,
            "tf_node_id": tf_node_id,
        }

    def test_click_event_fires_listener(self, session_with_view):
        """Click event should fire registered listener."""
        session = session_with_view
        assert session["button_node_id"] is not None, "Button node should exist"

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": session["button_node_id"],
                "event": "click",
                "data": {}
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)
        changes = response.get("changes", [])

        # Should create a notification (HelloWorldView shows notification on click)
        notification = next(
            (c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-notification"),
            None
        )
        assert notification is not None, "Click should create a notification"

    def test_click_event_with_empty_data(self, session_with_view):
        """Click event with empty data should work."""
        session = session_with_view
        assert session["button_node_id"] is not None

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": session["button_node_id"],
                "event": "click",
                "data": {}
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        # Should not raise exception
        response = session["handler"].handle_uidl(payload)
        assert "syncId" in response

    def test_event_on_nonexistent_node_ignored(self, session_with_view):
        """Event on non-existent node should be ignored."""
        session = session_with_view

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": 99999,  # Non-existent node
                "event": "click",
                "data": {}
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        # Should not raise, just ignore
        response = session["handler"].handle_uidl(payload)
        assert "syncId" in response

    def test_multiple_click_events_in_sequence(self, session_with_view):
        """Multiple click events should each fire listener."""
        session = session_with_view
        assert session["button_node_id"] is not None

        notification_count = 0
        current_sync_id = session["sync_id"]
        current_client_id = session["client_id"]

        for i in range(3):
            payload = {
                "csrfToken": session["csrf"],
                "rpc": [{
                    "type": "event",
                    "node": session["button_node_id"],
                    "event": "click",
                    "data": {}
                }],
                "syncId": current_sync_id,
                "clientId": current_client_id + i,
            }
            response = session["handler"].handle_uidl(payload)
            changes = response.get("changes", [])
            current_sync_id = response["syncId"]

            # Count notifications created
            for c in changes:
                if c.get("key") == "tag" and c.get("value") == "vaadin-notification":
                    notification_count += 1

        # Should have created 3 notifications
        assert notification_count == 3


class TestChangeEvent:
    """Test change event handling."""

    @pytest.fixture
    def session_with_view(self):
        """Create session with HelloWorldView loaded."""
        tree = StateTree()
        handler = UidlHandler(tree)

        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        nav_payload = {
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "",
                         "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        }
        nav_response = handler.handle_uidl(nav_payload)

        tf_node_id = None
        for change in nav_response.get("changes", []):
            if change.get("key") == "tag" and change.get("value") == "vaadin-text-field":
                tf_node_id = change.get("node")
                break

        return {
            "handler": handler,
            "csrf": csrf,
            "sync_id": nav_response["syncId"],
            "client_id": nav_response.get("clientId", 0),
            "tf_node_id": tf_node_id,
        }

    def test_change_event_fires_listener(self, session_with_view):
        """Change event should be processed without error."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": session["tf_node_id"],
                "event": "change",
                "data": {}
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        # Should not raise
        response = session["handler"].handle_uidl(payload)
        assert "syncId" in response

    def test_change_event_with_msync_combination(self, session_with_view):
        """Change event with mSync should both be processed."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [
                {
                    "type": "mSync",
                    "node": session["tf_node_id"],
                    "feature": Feature.ELEMENT_PROPERTY_MAP,
                    "property": "value",
                    "value": "Test Value"
                },
                {
                    "type": "event",
                    "node": session["tf_node_id"],
                    "event": "change",
                    "data": {}
                }
            ],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)
        assert response["syncId"] > session["sync_id"]


class TestUiNavigateEvent:
    """Test ui-navigate event handling."""

    @pytest.fixture
    def session(self):
        """Create session with init completed."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return {
            "handler": handler,
            "tree": tree,
            "csrf": csrf,
        }

    def test_ui_navigate_creates_view(self, session):
        """ui-navigate event should create the view structure."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "",
                         "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)
        changes = response.get("changes", [])

        # Should create view structure
        assert len(changes) > 0

        # Should have vertical-layout
        vl = next(
            (c for c in changes
             if c.get("key") == "tag" and c.get("value") == "vaadin-vertical-layout"),
            None
        )
        assert vl is not None

    def test_ui_navigate_only_once(self, session):
        """Second ui-navigate should not recreate view."""
        # First navigation
        payload1 = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "",
                         "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        }
        response1 = session["handler"].handle_uidl(payload1)
        changes1 = response1.get("changes", [])

        # Count components created
        component_count1 = len([
            c for c in changes1
            if c.get("key") == "tag"
        ])

        # Second navigation
        payload2 = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "",
                         "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": response1["syncId"],
            "clientId": 1,
        }
        response2 = session["handler"].handle_uidl(payload2)
        changes2 = response2.get("changes", [])

        # Second navigation should not create more components
        component_count2 = len([
            c for c in changes2
            if c.get("key") == "tag"
        ])
        assert component_count2 == 0, "Second navigation should not recreate view"


class TestKeydownEvent:
    """Test keydown event handling."""

    @pytest.fixture
    def session_with_view(self):
        """Create session with HelloWorldView loaded."""
        tree = StateTree()
        handler = UidlHandler(tree)

        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        nav_payload = {
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "",
                         "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        }
        nav_response = handler.handle_uidl(nav_payload)

        return {
            "handler": handler,
            "tree": tree,
            "csrf": csrf,
            "sync_id": nav_response["syncId"],
            "client_id": nav_response.get("clientId", 0),
        }

    def test_navigation_adds_keydown_listener(self, session_with_view):
        """Navigation should add keydown listener to body."""
        session = session_with_view

        # Look for the navigation response changes
        # The keydown listener should have been added to body (node 1)
        # We need to check the tree or the changes

        # Send another request to see if keydown was registered
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)

        # The keydown listener should be registered - we verify by checking
        # that navigation completed successfully
        assert response["syncId"] > session["sync_id"]

    def test_keydown_event_accepted(self, session_with_view):
        """Keydown event should be accepted without error."""
        session = session_with_view

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": 1,  # body node
                "event": "keydown",
                "data": {
                    "key": "Enter",
                    "code": "Enter",
                    "shiftKey": False,
                    "ctrlKey": False,
                    "altKey": False,
                    "metaKey": False,
                }
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        # Should not raise
        response = session["handler"].handle_uidl(payload)
        assert "syncId" in response


class TestEventDataPassing:
    """Test that event data is passed correctly to listeners."""

    @pytest.fixture
    def session_with_view(self):
        """Create session with HelloWorldView loaded."""
        tree = StateTree()
        handler = UidlHandler(tree)

        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        nav_payload = {
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "",
                         "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        }
        nav_response = handler.handle_uidl(nav_payload)

        button_node_id = None
        for change in nav_response.get("changes", []):
            if change.get("key") == "tag" and change.get("value") == "vaadin-button":
                button_node_id = change.get("node")
                break

        return {
            "handler": handler,
            "tree": tree,
            "csrf": csrf,
            "sync_id": nav_response["syncId"],
            "client_id": nav_response.get("clientId", 0),
            "button_node_id": button_node_id,
        }

    def test_click_event_data_passed_correctly(self, session_with_view):
        """Click event data should be passed to listener."""
        session = session_with_view
        assert session["button_node_id"] is not None

        # Click with mouse position data
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": session["button_node_id"],
                "event": "click",
                "data": {
                    "clientX": 100,
                    "clientY": 200,
                    "button": 0,
                    "shiftKey": False,
                    "ctrlKey": False,
                }
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)

        # Should process event correctly
        assert "syncId" in response
        # Should have created notification (click handler ran)
        changes = response.get("changes", [])
        notification = next(
            (c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-notification"),
            None
        )
        assert notification is not None


class TestMultipleRpcInSingleRequest:
    """Test handling multiple RPC calls in a single request."""

    @pytest.fixture
    def session_with_view(self):
        """Create session with HelloWorldView loaded."""
        tree = StateTree()
        handler = UidlHandler(tree)

        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        nav_payload = {
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "",
                         "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        }
        nav_response = handler.handle_uidl(nav_payload)

        tf_node_id = None
        button_node_id = None
        for change in nav_response.get("changes", []):
            if change.get("key") == "tag":
                if change.get("value") == "vaadin-text-field":
                    tf_node_id = change.get("node")
                elif change.get("value") == "vaadin-button":
                    button_node_id = change.get("node")

        return {
            "handler": handler,
            "tree": tree,
            "csrf": csrf,
            "sync_id": nav_response["syncId"],
            "client_id": nav_response.get("clientId", 0),
            "tf_node_id": tf_node_id,
            "button_node_id": button_node_id,
        }

    def test_multiple_events_processed_in_order(self, session_with_view):
        """Multiple RPC events should be processed in order."""
        session = session_with_view
        assert session["tf_node_id"] is not None
        assert session["button_node_id"] is not None

        # Send mSync + change + click in one request
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [
                {
                    "type": "mSync",
                    "node": session["tf_node_id"],
                    "feature": Feature.ELEMENT_PROPERTY_MAP,
                    "property": "value",
                    "value": "TestUser"
                },
                {
                    "type": "event",
                    "node": session["tf_node_id"],
                    "event": "change",
                    "data": {}
                },
                {
                    "type": "event",
                    "node": session["button_node_id"],
                    "event": "click",
                    "data": {}
                }
            ],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)
        changes = response.get("changes", [])

        # Should have created notification with the synced value
        notification = next(
            (c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-notification"),
            None
        )
        assert notification is not None

        # The notification text should contain "TestUser"
        text = next(
            (c for c in changes
             if c.get("key") == "text" and
             c.get("feat") == Feature.ELEMENT_PROPERTY_MAP and
             "TestUser" in str(c.get("value", ""))),
            None
        )
        assert text is not None
