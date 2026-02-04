"""UIDL Protocol Handler."""

import base64
import hashlib
import json
import random
import secrets
from typing import TYPE_CHECKING, Any

from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


# Event listener configurations with their Base64 hashes
# These must match Java Flow's hash generation
_CLICK_CONFIG = {
    "event.shiftKey": False,
    "event.metaKey": False,
    "event.detail": False,
    "event.ctrlKey": False,
    "event.clientX": False,
    "event.clientY": False,
    "event.altKey": False,
    "event.button": False,
    "event.screenY": False,
    "event.screenX": False
}

_CHANGE_CONFIG = {
    "}value": False
}

_KEYDOWN_CONFIG = {
    "event.shiftKey": False,
    "event.metaKey": False,
    "event.code": False,
    "event.key": False,
    "event.isComposing": False,
    "(['Enter'].indexOf(event.code) !== -1 || ['Enter'].indexOf(event.key) !== -1) && !event.getModifierState('Shift') && !event.getModifierState('Control') && !event.getModifierState('Alt') && !event.getModifierState('AltGraph') && !event.getModifierState('Meta') && (event.stopPropagation() || true)": True,
    "event.ctrlKey": False,
    "event.repeat": False,
    "event.location": False,
    "event.altKey": False
}


def _generate_hash(config: dict) -> str:
    """Generate Base64 hash for event listener config."""
    # Create a deterministic string from the config
    config_str = json.dumps(config, sort_keys=True, separators=(",", ":"))
    hash_bytes = hashlib.sha256(config_str.encode()).digest()[:8]
    return base64.b64encode(hash_bytes).decode()


# Pre-compute hashes for known event types
_CLICK_HASH = _generate_hash(_CLICK_CONFIG)
_CHANGE_HASH = _generate_hash(_CHANGE_CONFIG)
_KEYDOWN_HASH = _generate_hash(_KEYDOWN_CONFIG)


class UidlHandler:
    """Handles UIDL protocol messages."""

    def __init__(self, tree: "StateTree"):
        self._tree = tree
        self._sync_id = 0
        self._client_id = 0
        self._csrf_token = secrets.token_hex(16)
        self._app_id = f"ROOT-{random.randint(1000000, 9999999)}"
        self._initialized = False
        self._view = None

        # Node references
        self._body_node = None
        self._container_node = None
        self._pending_execute: list = []  # Execute commands for next response
        self._last_client_id = 0  # Track client's message counter

    def handle_init(self, browser_details: dict, initial_route: str = "") -> dict:
        """Handle init request.

        Returns appConfig with initial UIDL.
        Each init creates a fresh UI (handles page reload).

        Args:
            browser_details: Browser details from client
            initial_route: The route from the request path (e.g., "about" for /about)
        """
        # Reset state for fresh UI (handles page reload)
        self._tree.reset()
        self._sync_id = 0
        self._client_id = 0
        self._view = None
        self._body_node = None
        self._container_node = None
        self._pending_execute = []
        self._last_client_id = 0
        self._initial_route = initial_route  # Store for use in navigation

        self._create_initial_nodes()
        self._initialized = True

        changes = self._tree.collect_changes()

        # Constants define event debounce/sync settings
        constants = {
            "c0": {"route": False, "appShellTitle": False, "query": False, "trigger": False, "historyState": False},
            "c1": {"route": False, "query": False},
            "c2": {"fullRefresh": False},
        }

        return {
            "appConfig": {
                "productionMode": True,
                "v-uiId": 0,
                "appId": self._app_id,
                "contextRootUrl": "/",
                "heartbeatInterval": 300,
                "maxMessageSuspendTimeout": 5000,
                "sessExpMsg": {"caption": None, "message": None, "url": None},
                "uidl": {
                    "clientId": self._client_id,
                    "syncId": self._sync_id,
                    "Vaadin-Security-Key": self._csrf_token,
                    "Vaadin-Push-ID": secrets.token_hex(16),
                    "constants": constants,
                    "changes": changes,
                },
            },
            "errors": None,
        }

    def _create_initial_nodes(self):
        """Create the initial node structure matching Java Flow exactly."""
        app_num = self._app_id.split("-")[1]

        # Node 1: body (UI root) - no attach for root node
        self._body_node = self._tree.create_node()
        # Don't call attach() - body is implicit root

        # Build changes manually to match exact order from Java
        changes = []

        # Node 1 tag
        changes.append({"node": 1, "type": "put", "key": "tag", "feat": 0, "value": "body"})

        # Node 1 listeners (using constant references)
        changes.append({"node": 1, "type": "put", "key": "ui-navigate", "feat": 4, "value": "c0"})
        changes.append({"node": 1, "type": "put", "key": "ui-leave-navigation", "feat": 4, "value": "c1"})
        changes.append({"node": 1, "type": "put", "key": "ui-refresh", "feat": 4, "value": "c2"})

        # Node 1 virtual children splice (node 3)
        changes.append({"node": 1, "type": "splice", "feat": 24, "index": 0, "addNodes": [3]})

        # Node 1 push config
        changes.append({"node": 1, "type": "put", "key": "pushServletMapping", "feat": 5, "value": "/"})
        changes.append({"node": 1, "type": "put", "key": "alwaysXhrToServer", "feat": 5, "value": True})
        changes.append({"node": 1, "type": "put", "key": "pushMode", "feat": 5, "value": "DISABLED"})
        changes.append({"node": 1, "type": "put", "key": "parameters", "feat": 5, "nodeValue": 2})

        # Node 2: push parameters
        params_node = self._tree.create_node()  # This will be node 2
        changes.append({"node": 2, "type": "attach"})
        changes.append({"node": 2, "type": "put", "key": "fallbackTransport", "feat": 6, "value": "long-polling"})
        changes.append({"node": 2, "type": "put", "key": "transport", "feat": 6, "value": "websocket"})

        # Node 3: flow-container
        self._container_node = self._tree.create_node()  # This will be node 3
        changes.append({"node": 3, "type": "attach"})
        changes.append({"node": 3, "type": "put", "key": "payload", "feat": 0, "value": {"type": "@id", "payload": self._app_id}})
        changes.append({"node": 3, "type": "put", "key": "tag", "feat": 0, "value": f"flow-container-root-{app_num}"})

        # Add all changes
        for change in changes:
            self._tree.add_change(change)

    def handle_uidl(self, payload: dict) -> dict:
        """Handle UIDL request.

        Returns UIDL response with changes.
        """
        # Validate syncId - client should send the last syncId it received
        client_sync_id = payload.get("syncId", 0)
        client_client_id = payload.get("clientId", 0)

        # Track the client's message count
        self._last_client_id = client_client_id

        # Process RPC calls
        rpc_list = payload.get("rpc", [])
        self._process_rpc(rpc_list)

        # Collect changes and build response
        return self._build_response()

    def _process_rpc(self, rpc_list: list[dict]):
        """Process RPC calls from client."""
        for rpc in rpc_list:
            rpc_type = rpc.get("type")
            if rpc_type == "event":
                self._handle_event(rpc)
            elif rpc_type == "mSync":
                self._handle_msync(rpc)

    def _handle_event(self, rpc: dict):
        """Handle event RPC."""
        node_id = rpc.get("node")
        event_type = rpc.get("event")
        event_data = rpc.get("data", {})

        if event_type == "ui-navigate":
            self._handle_navigation(event_data)
        elif event_type == "click":
            self._handle_click(node_id, event_data)
        elif event_type == "change":
            self._handle_change(node_id, event_data)

    def _handle_navigation(self, event_data: dict):
        """Handle navigation event - create the view."""
        # Only create view once
        if self._view is not None:
            return

        route = event_data.get("route", "")

        # Normalize route - strip leading/trailing slashes
        route = route.strip("/")

        # Use initial_route from request path if client sent empty or root route
        # This handles the case where the client's contextRootUrl calculation is wrong
        if not route and hasattr(self, "_initial_route") and self._initial_route:
            route = self._initial_route

        # Use router to find view class
        from vaadin.flow.router import get_view_class, get_page_title

        view_class = get_view_class(route)

        if view_class is None:
            # Fallback to http_server._view_class for backwards compatibility
            from vaadin.flow.server.http_server import _view_class
            if _view_class is not None:
                view_class = _view_class
            else:
                # No route found, return 404-like behavior
                # For now, just return without creating a view
                return

        # Get page title
        page_title = get_page_title(route) or "PyFlow"

        # Create the view
        from vaadin.flow.core.component import UI
        ui = UI(self._tree)
        self._view = view_class()
        self._view._ui = ui
        self._view._attach(self._tree)

        # Add view to container
        self._container_node.add_child(self._view.element.node)

        # Add keydown listener to body for Enter key handling
        self._tree.add_change({
            "node": self._body_node.id,
            "type": "put",
            "key": "keydown",
            "feat": Feature.ELEMENT_LISTENER_MAP,
            "value": _KEYDOWN_HASH
        })

        # Find TextField nodes to add execute command for invalid property
        self._pending_execute = [
            [page_title, "document.title = $0"],
        ]

        # Add execute command for each TextField's invalid property
        textfield_nodes = self._find_textfield_nodes()
        for tf_node_id in textfield_nodes:
            self._pending_execute.append(
                [False, {"@v-node": tf_node_id}, "return (async function() { this.invalid = $0}).apply($1)"]
            )

        # Add serverConnected execute command
        self._pending_execute.append(
            [False, {"@v-node": self._container_node.id}, "return (async function() { this.serverConnected($0)}).apply($1)"]
        )

    def _find_textfield_nodes(self) -> list[int]:
        """Find all TextField node IDs in the current view."""
        textfield_nodes = []
        for node_id, node in self._tree._nodes.items():
            tag = node.get(Feature.ELEMENT_DATA, "tag")
            if tag == "vaadin-text-field":
                textfield_nodes.append(node_id)
        return textfield_nodes

    def _handle_click(self, node_id: int, event_data: dict):
        """Handle click event."""
        element = self._tree.get_element(node_id)
        if element:
            element.fire_event("click", event_data)

    def _handle_change(self, node_id: int, event_data: dict):
        """Handle change event."""
        pass

    def _handle_msync(self, rpc: dict):
        """Handle property sync RPC."""
        node_id = rpc.get("node")
        feature = rpc.get("feature")
        prop = rpc.get("property")
        value = rpc.get("value")

        node = self._tree.get_node(node_id)
        if node and feature == Feature.ELEMENT_PROPERTY_MAP:
            # Update the node's property (without generating a change back)
            if feature not in node._features:
                node._features[feature] = {}
            node._features[feature][prop] = value

            # Also update the component's internal state
            component = self._tree.get_component(node_id)
            if component:
                component._sync_property(prop, value)

    def _build_response(self) -> dict:
        """Build UIDL response."""
        changes = self._tree.collect_changes()
        self._sync_id += 1
        # clientId reflects the last client message we processed
        self._client_id = self._last_client_id + 1

        # Build constants dict with Base64 hashes
        # Only include constants that are actually used in changes
        constants = {}
        used_event_types = set()

        # Scan changes to find which event types are used
        for change in changes:
            if change.get("feat") == Feature.ELEMENT_LISTENER_MAP and change.get("value") is True:
                used_event_types.add(change.get("key"))

        # Map event types to their hashes and configs
        event_configs = {
            "click": (_CLICK_HASH, _CLICK_CONFIG),
            "change": (_CHANGE_HASH, _CHANGE_CONFIG),
            "keydown": (_KEYDOWN_HASH, _KEYDOWN_CONFIG),
        }

        # Add used constants and replace values with hash references
        for change in changes:
            if change.get("feat") == Feature.ELEMENT_LISTENER_MAP and change.get("value") is True:
                event_type = change.get("key")
                if event_type in event_configs:
                    hash_key, config = event_configs[event_type]
                    constants[hash_key] = config
                    change["value"] = hash_key

        # Also check for keydown hash already in changes (added by _handle_navigation)
        for change in changes:
            if change.get("feat") == Feature.ELEMENT_LISTENER_MAP:
                value = change.get("value")
                if value == _KEYDOWN_HASH:
                    constants[_KEYDOWN_HASH] = _KEYDOWN_CONFIG

        response = {
            "syncId": self._sync_id,
            "clientId": self._client_id,
            "constants": constants,
            "changes": changes,
        }
        # Add execute commands if any
        if self._pending_execute:
            response["execute"] = self._pending_execute
            self._pending_execute = []
        return response
