"""Tests for component state handling with RPC.

Based on Java Flow's AbstractRpcInvocationHandlerTest.java patterns.
Tests component registration, event dispatch, and state updates.
"""

import pytest

from vaadin.flow.server.uidl_handler import UidlHandler
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestComponentAttached:
    """Test events on attached components."""

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

    def test_event_on_attached_component(self, session_with_view):
        """Event on attached component should fire listener."""
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
        response = session["handler"].handle_uidl(payload)
        changes = response.get("changes", [])

        # Click handler should have created a notification
        notification = next(
            (c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-notification"),
            None
        )
        assert notification is not None


class TestComponentRegistration:
    """Test component registration for events."""

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

    def test_component_registered_for_events(self, session_with_view):
        """Component should be registered in tree for event dispatch."""
        session = session_with_view

        # Button should be registered
        element = session["tree"].get_element(session["button_node_id"])
        assert element is not None

    def test_component_can_be_found_by_node_id(self, session_with_view):
        """Component should be findable by node ID."""
        session = session_with_view

        component = session["tree"].get_component(session["button_node_id"])
        assert component is not None


class TestComponentStateUpdates:
    """Test component state updates from events."""

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
        tf_node_id = None
        vl_node_id = None
        for change in nav_response.get("changes", []):
            if change.get("key") == "tag":
                if change.get("value") == "vaadin-button":
                    button_node_id = change.get("node")
                elif change.get("value") == "vaadin-text-field":
                    tf_node_id = change.get("node")
                elif change.get("value") == "vaadin-vertical-layout":
                    vl_node_id = change.get("node")

        return {
            "handler": handler,
            "tree": tree,
            "csrf": csrf,
            "sync_id": nav_response["syncId"],
            "client_id": nav_response.get("clientId", 0),
            "button_node_id": button_node_id,
            "tf_node_id": tf_node_id,
            "vl_node_id": vl_node_id,
        }

    def test_component_state_updated_by_event(self, session_with_view):
        """Event handler can update component state."""
        session = session_with_view
        assert session["button_node_id"] is not None

        # Get initial child count of body node (notifications attach to body)
        body_node = session["tree"].get_node(1)
        initial_children = len(body_node._children)

        # Click shows a notification (attached to body)
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
        session["handler"].handle_uidl(payload)

        # Body should have more children now (notification added)
        assert len(body_node._children) > initial_children


class TestDynamicComponents:
    """Test dynamically added components."""

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

    def test_dynamic_component_created_on_event(self, session_with_view):
        """Dynamic component should be created on event."""
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
        response = session["handler"].handle_uidl(payload)
        changes = response.get("changes", [])

        # Should have created new notification node
        notification = next(
            (c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-notification"),
            None
        )
        assert notification is not None

        # New notification should be attached
        notification_node_id = notification.get("node")
        attach = next(
            (c for c in changes if c.get("node") == notification_node_id and c.get("type") == "attach"),
            None
        )
        assert attach is not None

    def test_dynamic_component_added_to_parent(self, session_with_view):
        """Dynamic component should be added to parent (body for notification)."""
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
        response = session["handler"].handle_uidl(payload)
        changes = response.get("changes", [])

        # Find the notification node
        notification = next(
            (c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-notification"),
            None
        )
        notification_node_id = notification.get("node")

        # Should have splice adding notification to body (node 1)
        splice = next(
            (c for c in changes
             if c.get("type") == "splice" and
             notification_node_id in c.get("addNodes", [])),
            None
        )
        assert splice is not None


class TestPropertySyncUpdatesComponent:
    """Test that mSync updates component internal state."""

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

    def test_sync_updates_component_value(self, session_with_view):
        """mSync should update component's internal value."""
        session = session_with_view
        assert session["tf_node_id"] is not None

        # Sync value
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": "ComponentValue"
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)

        # Get component and verify value was synced
        component = session["tree"].get_component(session["tf_node_id"])
        assert component is not None
        assert component.value == "ComponentValue"

    def test_synced_value_used_in_event_handler(self, session_with_view):
        """Value synced via mSync should be used in event handlers."""
        session = session_with_view
        assert session["tf_node_id"] is not None
        assert session["button_node_id"] is not None

        # Sync value
        sync_payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "mSync",
                "node": session["tf_node_id"],
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": "value",
                "value": "SyncedUser"
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        sync_response = session["handler"].handle_uidl(sync_payload)

        # Click button to trigger handler
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

        # Notification text should contain synced value
        text = next(
            (c for c in changes
             if c.get("key") == "text" and
             c.get("feat") == Feature.ELEMENT_PROPERTY_MAP and
             "SyncedUser" in str(c.get("value", ""))),
            None
        )
        assert text is not None


class TestNodeReferences:
    """Test node reference handling."""

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
            "changes": nav_response.get("changes", []),
        }

    def test_all_nodes_have_unique_ids(self, session_with_view):
        """All created nodes should have unique IDs."""
        changes = session_with_view["changes"]

        node_ids = set()
        for change in changes:
            node_id = change.get("node")
            if change.get("type") == "attach":
                assert node_id not in node_ids, f"Duplicate node ID: {node_id}"
                node_ids.add(node_id)

    def test_splice_references_valid_nodes(self, session_with_view):
        """Splice addNodes should reference valid (attached) nodes."""
        changes = session_with_view["changes"]

        # Get all attached node IDs
        attached = set()
        for change in changes:
            if change.get("type") == "attach":
                attached.add(change.get("node"))

        # Check splice references
        for change in changes:
            if change.get("type") == "splice":
                for node_id in change.get("addNodes", []):
                    # Node should be attached before being added as child
                    # Note: some nodes (like body) are implicit
                    if node_id > 1:  # Skip body node
                        assert node_id in attached, f"Splice references unattached node: {node_id}"

    def test_put_changes_reference_valid_nodes(self, session_with_view):
        """Put changes should reference valid nodes."""
        changes = session_with_view["changes"]

        # Get all node IDs (from attaches or implicit nodes like body)
        all_nodes = {1}  # body is always node 1 (implicit root)
        for change in changes:
            if change.get("type") == "attach":
                all_nodes.add(change.get("node"))

        # Check put references
        for change in changes:
            if change.get("type") == "put":
                node_id = change.get("node")
                assert node_id in all_nodes, f"Put references invalid node: {node_id}"
