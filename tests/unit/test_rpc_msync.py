"""Tests for mSync RPC handling (property synchronization).

Based on Java Flow's MapSyncRpcHandlerTest.java patterns.
Tests property sync from client to server.
"""

import pytest

from pyflow.server.uidl_handler import UidlHandler
from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature


class TestPropertySync:
    """Test property synchronization via mSync."""

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

    def test_property_sync_updates_component(self, session_with_view):
        """mSync should update component's property."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": "TestValue"
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)

        # mSync should complete without error
        assert "syncId" in response
        assert response["syncId"] > session["sync_id"]

    def test_value_sync_on_textfield(self, session_with_view):
        """TextField value should sync correctly."""
        session = session_with_view
        assert session["tf_node_id"] is not None
        assert session["button_node_id"] is not None

        # Sync the value
        sync_payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": "SyncedName"
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        sync_response = session["handler"].handle_uidl(sync_payload)

        # Click to trigger handler that uses the value
        click_payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": session["button_node_id"],
                "event": "click",
                "data": {}
            }],
            "syncId": sync_response["syncId"],
            "clientId": session["client_id"] + 1,
        }
        click_response = session["handler"].handle_uidl(click_payload)
        changes = click_response.get("changes", [])

        # The notification text should contain the synced name
        text = next(
            (c for c in changes
             if c.get("key") == "text" and
             c.get("feat") == Feature.ELEMENT_PROPERTY_MAP and
             "SyncedName" in str(c.get("value", ""))),
            None
        )
        assert text is not None, "Notification text should contain synced value"

    def test_sync_on_nonexistent_node_ignored(self, session_with_view):
        """mSync on non-existent node should be ignored."""
        session = session_with_view

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": 99999,  # Non-existent node
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": "Test"
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        # Should not raise
        response = session["handler"].handle_uidl(payload)
        assert "syncId" in response

    def test_sync_updates_internal_state(self, session_with_view):
        """mSync should update the node's internal state."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": "InternalState"
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        session["handler"].handle_uidl(payload)

        # Check that node state was updated
        node = session["tree"].get_node(session["tf_node_id"])
        assert node is not None
        value = node.get(Feature.ELEMENT_PROPERTY_MAP, "value")
        assert value == "InternalState"

    def test_sync_does_not_generate_change(self, session_with_view):
        """mSync should not generate a change back to client."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": "NoChangeBack"
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)
        changes = response.get("changes", [])

        # Should not have a change for the same property
        value_change = next(
            (c for c in changes
             if c.get("node") == session["tf_node_id"] and
             c.get("key") == "value" and
             c.get("feat") == Feature.ELEMENT_PROPERTY_MAP),
            None
        )
        assert value_change is None, "mSync should not echo the change back"


class TestMultipleSyncs:
    """Test multiple property syncs."""

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
            "tree": tree,
            "csrf": csrf,
            "sync_id": nav_response["syncId"],
            "client_id": nav_response.get("clientId", 0),
            "tf_node_id": tf_node_id,
        }

    def test_multiple_syncs_in_one_request(self, session_with_view):
        """Multiple mSync calls in one request should all be processed."""
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
                    "value": "Value1"
                },
                {
                    "type": "mSync",
                    "node": session["tf_node_id"],
                    "feature": Feature.ELEMENT_PROPERTY_MAP,
                    "property": "value",
                    "value": "Value2"
                },
            ],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        session["handler"].handle_uidl(payload)

        # Last value should win
        node = session["tree"].get_node(session["tf_node_id"])
        value = node.get(Feature.ELEMENT_PROPERTY_MAP, "value")
        assert value == "Value2"

    def test_sequential_syncs_across_requests(self, session_with_view):
        """Sequential syncs across requests should update correctly."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        # First sync
        payload1 = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": "First"
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response1 = session["handler"].handle_uidl(payload1)

        # Verify first value
        node = session["tree"].get_node(session["tf_node_id"])
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "value") == "First"

        # Second sync
        payload2 = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": "Second"
            }],
            "syncId": response1["syncId"],
            "clientId": session["client_id"] + 1,
        }
        session["handler"].handle_uidl(payload2)

        # Verify second value
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "value") == "Second"


class TestSyncWithDifferentFeatures:
    """Test mSync with different feature types."""

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
            "tree": tree,
            "csrf": csrf,
            "sync_id": nav_response["syncId"],
            "client_id": nav_response.get("clientId", 0),
            "tf_node_id": tf_node_id,
        }

    def test_sync_only_handles_property_map(self, session_with_view):
        """mSync should only process ELEMENT_PROPERTY_MAP feature."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        # Try to sync with wrong feature (should be ignored)
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_ATTRIBUTE_MAP,  # Wrong feature
                "property": "value",
                "value": "Test"
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        session["handler"].handle_uidl(payload)

        # Should not have updated ELEMENT_PROPERTY_MAP
        node = session["tree"].get_node(session["tf_node_id"])
        # The value should not be set via wrong feature
        value = node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "value")
        # This should be None since we don't process attribute map syncs
        assert value is None


class TestSyncEdgeCases:
    """Test edge cases in mSync handling."""

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
            "tree": tree,
            "csrf": csrf,
            "sync_id": nav_response["syncId"],
            "client_id": nav_response.get("clientId", 0),
            "tf_node_id": tf_node_id,
        }

    def test_sync_empty_string(self, session_with_view):
        """mSync with empty string should update correctly."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        # First set a value
        payload1 = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": "Initial"
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response1 = session["handler"].handle_uidl(payload1)

        # Now set to empty string
        payload2 = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": ""
            }],
            "syncId": response1["syncId"],
            "clientId": session["client_id"] + 1,
        }
        session["handler"].handle_uidl(payload2)

        node = session["tree"].get_node(session["tf_node_id"])
        value = node.get(Feature.ELEMENT_PROPERTY_MAP, "value")
        assert value == ""

    def test_sync_null_value(self, session_with_view):
        """mSync with None/null value should update correctly."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": None
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        session["handler"].handle_uidl(payload)

        node = session["tree"].get_node(session["tf_node_id"])
        value = node.get(Feature.ELEMENT_PROPERTY_MAP, "value")
        assert value is None

    def test_sync_boolean_value(self, session_with_view):
        """mSync with boolean value should work."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "invalid",
                "value": True
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        session["handler"].handle_uidl(payload)

        node = session["tree"].get_node(session["tf_node_id"])
        value = node.get(Feature.ELEMENT_PROPERTY_MAP, "invalid")
        assert value is True

    def test_sync_numeric_value(self, session_with_view):
        """mSync with numeric value should work."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "maxlength",
                "value": 100
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        session["handler"].handle_uidl(payload)

        node = session["tree"].get_node(session["tf_node_id"])
        value = node.get(Feature.ELEMENT_PROPERTY_MAP, "maxlength")
        assert value == 100
