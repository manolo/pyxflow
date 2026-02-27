"""Event Handling Tests."""

import pytest

from pyflow.core.state_node import Feature


class TestClickEvent:
    """Test click event handling."""

    @pytest.fixture
    def session_with_view(self):
        """Create session with HelloWorldView loaded."""
        from pyflow.server.uidl_handler import UidlHandler
        from pyflow.core.state_tree import StateTree

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
                "data": {"route": "", "query": "", "appShellTitle": "", "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        }
        nav_response = handler.handle_uidl(nav_payload)

        # Find button node ID
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

    def test_click_adds_notification(self, session_with_view):
        """Click on button should show a Notification."""
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

        # Should create a notification
        notification = next(
            (c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-notification"),
            None
        )
        assert notification is not None, "Click should create a notification"


class TestValueSync:
    """Test mSync (property sync) handling."""

    @pytest.fixture
    def session_with_view(self):
        """Create session with HelloWorldView loaded."""
        from pyflow.server.uidl_handler import UidlHandler
        from pyflow.core.state_tree import StateTree

        tree = StateTree()
        handler = UidlHandler(tree)

        # Init
        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        # Navigate
        nav_payload = {
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "", "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        }
        nav_response = handler.handle_uidl(nav_payload)

        # Find text field node ID
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

    def test_msync_updates_value(self, session_with_view):
        """mSync should update TextField value."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        # Send mSync to update value
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": "World"
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        session["handler"].handle_uidl(payload)

        # Now click should use the value
        click_payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": session["button_node_id"],
                "event": "click",
                "data": {}
            }],
            "syncId": session["sync_id"] + 1,
            "clientId": session["client_id"] + 1,
        }
        response = session["handler"].handle_uidl(click_payload)
        changes = response.get("changes", [])

        # Should have notification with text "Hello World"
        text = next(
            (c for c in changes
             if c.get("key") == "text" and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP and "World" in str(c.get("value", ""))),
            None
        )
        assert text is not None, "Notification text should contain 'World'"


class TestChangeEvent:
    """Test change event handling."""

    @pytest.fixture
    def session_with_view(self):
        """Create session with HelloWorldView loaded."""
        from pyflow.server.uidl_handler import UidlHandler
        from pyflow.core.state_tree import StateTree

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
                "data": {"route": "", "query": "", "appShellTitle": "", "historyState": {"idx": 0}, "trigger": ""}
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

    def test_change_event_accepted(self, session_with_view):
        """Change event should be accepted."""
        session = session_with_view

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [
                {
                    "type": "mSync",
                    "node": session["tf_node_id"],
                    "feature": Feature.ELEMENT_PROPERTY_MAP,
                    "property": "value",
                    "value": "Test"
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

        # Should not error, syncId should increment
        assert response["syncId"] > session["sync_id"]
