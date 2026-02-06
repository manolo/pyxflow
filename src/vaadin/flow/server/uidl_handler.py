"""UIDL Protocol Handler."""

import random
import secrets
from typing import TYPE_CHECKING, Any

from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


# =============================================================================
# Event Listener Configurations
# =============================================================================
# These configurations and hashes are captured from Java Flow to ensure
# exact protocol compatibility. The hashes are computed by Java using SHA-256
# of the JSON string representation, taking the first 64 bits and Base64 encoding.
#
# IMPORTANT: The exact hash values from Java are used here instead of computing
# them dynamically, because the JSON serialization order affects the hash.
# =============================================================================

# Click event configuration (for buttons, etc.)
# Hash captured from Java Flow: F8oCtNArLiI=
_CLICK_HASH = "F8oCtNArLiI="
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

# Change event configuration (for text fields, etc.)
# The '}' prefix means "sync this property with server"
# Hash captured from Java Flow: Fg73o1qebBo=
_CHANGE_HASH = "Fg73o1qebBo="
_CHANGE_CONFIG = {
    "}value": False
}

# Opened-changed event configuration (for dialogs, dropdowns)
_OPENED_CHANGED_HASH = "t7mULTj4JVU="  # Placeholder - capture from Java if needed
_OPENED_CHANGED_CONFIG = {
    "}opened": False
}

# Checked-changed event configuration (for checkboxes)
_CHECKED_CHANGED_HASH = "azhwx/bqd+0="  # Placeholder - capture from Java if needed
_CHECKED_CHANGED_CONFIG = {
    "}checked": False
}

# Keydown event configuration (Enter key handling)
# Hash captured from Java Flow: OSoHnU3SjNg=
_KEYDOWN_HASH = "OSoHnU3SjNg="
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

# Notification closed event
# Hash captured from Java Flow: vIpODLLAUDo=
_CLOSED_HASH = "vIpODLLAUDo="
_CLOSED_CONFIG = {}

# Notification opened-changed event (different hash from Dialog's opened-changed)
# Hash captured from Java Flow: uqvzCy8jAQc=
_NOTIFICATION_OPENED_CHANGED_HASH = "uqvzCy8jAQc="
_NOTIFICATION_OPENED_CHANGED_CONFIG = {
    "}opened": False
}

# =============================================================================
# UI Navigation Event Configurations
# =============================================================================
# These are registered on the body element for client-side navigation.

# UI navigate event - triggered when the user navigates to a new route
# Hash captured from Java Flow: msDV4SvCysE=
_UI_NAVIGATE_HASH = "msDV4SvCysE="
_UI_NAVIGATE_CONFIG = {
    "route": False,
    "appShellTitle": False,
    "query": False,
    "trigger": False,
    "historyState": False
}

# UI leave navigation event - triggered when leaving a route
# Hash captured from Java Flow: i2nDWhpwLZE=
_UI_LEAVE_NAVIGATION_HASH = "i2nDWhpwLZE="
_UI_LEAVE_NAVIGATION_CONFIG = {
    "route": False,
    "query": False
}

# UI refresh event - triggered on page refresh
# Hash captured from Java Flow: 18ACma10cDE=
_UI_REFRESH_HASH = "18ACma10cDE="
_UI_REFRESH_CONFIG = {
    "fullRefresh": False
}


# Reverse lookup: hash → config for all known event hashes.
# Used when a component registers a listener with an explicit hash_key
# (value is a string, not True) so we can add the config to constants.
_HASH_TO_CONFIG = {
    _CLICK_HASH: _CLICK_CONFIG,
    _CHANGE_HASH: _CHANGE_CONFIG,
    _OPENED_CHANGED_HASH: _OPENED_CHANGED_CONFIG,
    _CHECKED_CHANGED_HASH: _CHECKED_CHANGED_CONFIG,
    _KEYDOWN_HASH: _KEYDOWN_CONFIG,
    _CLOSED_HASH: _CLOSED_CONFIG,
    _NOTIFICATION_OPENED_CHANGED_HASH: _NOTIFICATION_OPENED_CHANGED_CONFIG,
}


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
        self._sent_constants: set[str] = set()  # Track already-sent constant hashes

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
        self._sent_constants = set()
        self._initial_route = initial_route  # Store for use in navigation

        self._create_initial_nodes()
        self._initialized = True

        changes = self._tree.collect_changes()

        # Constants for UI navigation events (using Java Flow hashes)
        constants = {
            _UI_NAVIGATE_HASH: _UI_NAVIGATE_CONFIG,
            _UI_LEAVE_NAVIGATION_HASH: _UI_LEAVE_NAVIGATION_CONFIG,
            _UI_REFRESH_HASH: _UI_REFRESH_CONFIG,
        }
        # Track these as sent so they won't be resent in UIDL responses
        self._sent_constants.update(constants.keys())

        return {
            "appConfig": {
                "productionMode": True,
                "v-uiId": 0,
                "appId": self._app_id,
                "contextRootUrl": "./",
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

        # Node 1 listeners (using Java Flow hashes as constant references)
        changes.append({"node": 1, "type": "put", "key": "ui-navigate", "feat": 4, "value": _UI_NAVIGATE_HASH})
        changes.append({"node": 1, "type": "put", "key": "ui-leave-navigation", "feat": 4, "value": _UI_LEAVE_NAVIGATION_HASH})
        changes.append({"node": 1, "type": "put", "key": "ui-refresh", "feat": 4, "value": _UI_REFRESH_HASH})

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
        from vaadin.flow.components.notification import _set_current_tree
        _set_current_tree(self._tree)
        try:
            for rpc in rpc_list:
                rpc_type = rpc.get("type")
                if rpc_type == "event":
                    self._handle_event(rpc)
                elif rpc_type == "mSync":
                    self._handle_msync(rpc)
                elif rpc_type == "publishedEventHandler":
                    self._handle_published_event(rpc)
        finally:
            _set_current_tree(None)

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
        else:
            # Generic dispatch for events like opened-changed, closed, etc.
            element = self._tree.get_element(node_id)
            if element:
                element.fire_event(event_type, event_data)

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
        initial_route = getattr(self, "_initial_route", "")
        if not route and initial_route:
            route = initial_route

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

        # Set tree context so Notification.show() works during view construction
        from vaadin.flow.components.notification import _set_current_tree
        _set_current_tree(self._tree)
        try:
            # Create the view
            from vaadin.flow.core.component import UI
            ui = UI(self._tree)
            self._view = view_class()
            self._view._ui = ui
            self._view._attach(self._tree)
        finally:
            _set_current_tree(None)

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

        # Add execute commands for Dialog components (FlowComponentHost renderer)
        dialog_nodes = self._find_dialog_nodes()
        for dialog_node_id in dialog_nodes:
            # Patch the virtual container
            self._pending_execute.append(
                [{"@v-node": dialog_node_id}, "return (async function() { Vaadin.FlowComponentHost.patchVirtualContainer(this) }).apply($0)"]
            )
            # Set up the renderer
            self._pending_execute.append(
                [self._app_id, {"@v-node": dialog_node_id}, "return (async function() { this.renderer = (root) => Vaadin.FlowComponentHost.setChildNodes($0, this.virtualChildNodeIds, root) }).apply($1)"]
            )
            # Request content update
            self._pending_execute.append(
                [{"@v-node": dialog_node_id}, "return (async function() { this.requestContentUpdate() }).apply($0)"]
            )
            # Register overlay close handler (calls $server.handleClientClose)
            self._pending_execute.append(
                [{"@v-node": dialog_node_id},
                 "return (async function() {"
                 "  this.$.overlay.addEventListener('vaadin-overlay-close', () => {"
                 "    document.addEventListener('vaadin-overlay-close', (e) => {"
                 "      if(!e.defaultPrevented && e.detail.overlay === this.$.overlay) {"
                 "        e.preventDefault();"
                 "        this.$server.handleClientClose();"
                 "      }"
                 "    }, {once: true})"
                 "  })"
                 "}).apply($0)"]
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

    def _find_dialog_nodes(self) -> list[int]:
        """Find all Dialog node IDs in the current view."""
        dialog_nodes = []
        for node_id, node in self._tree._nodes.items():
            tag = node.get(Feature.ELEMENT_DATA, "tag")
            if tag == "vaadin-dialog":
                dialog_nodes.append(node_id)
        return dialog_nodes

    def _add_execute_for_new_overlays(self, changes: list[dict]):
        """Add execute commands for newly attached dialog nodes.

        This scans the changes for 'attach' operations and adds FlowComponentHost
        execute commands for any newly attached overlay components.
        """
        # Find newly attached node IDs
        newly_attached = set()
        for change in changes:
            if change.get("type") == "attach":
                newly_attached.add(change.get("node"))

        # Check each newly attached node to see if it's a dialog
        for node_id in newly_attached:
            node = self._tree.get_node(node_id)
            if not node:
                continue
            tag = node.get(Feature.ELEMENT_DATA, "tag")

            if tag == "vaadin-dialog":
                # Patch the virtual container
                self._pending_execute.append(
                    [{"@v-node": node_id}, "return (async function() { Vaadin.FlowComponentHost.patchVirtualContainer(this) }).apply($0)"]
                )
                # Set up the renderer
                self._pending_execute.append(
                    [self._app_id, {"@v-node": node_id}, "return (async function() { this.renderer = (root) => Vaadin.FlowComponentHost.setChildNodes($0, this.virtualChildNodeIds, root) }).apply($1)"]
                )
                # Request content update
                self._pending_execute.append(
                    [{"@v-node": node_id}, "return (async function() { this.requestContentUpdate() }).apply($0)"]
                )
                # Register overlay close handler (calls $server.handleClientClose)
                self._pending_execute.append(
                    [{"@v-node": node_id},
                     "return (async function() {"
                     "  this.$.overlay.addEventListener('vaadin-overlay-close', () => {"
                     "    document.addEventListener('vaadin-overlay-close', (e) => {"
                     "      if(!e.defaultPrevented && e.detail.overlay === this.$.overlay) {"
                     "        e.preventDefault();"
                     "        this.$server.handleClientClose();"
                     "      }"
                     "    }, {once: true})"
                     "  })"
                     "}).apply($0)"]
                )
            elif tag == "vaadin-notification":
                # 1. Request content update BEFORE patching
                self._pending_execute.append(
                    [{"@v-node": node_id}, "return $0.requestContentUpdate()"]
                )
                # 2. Patch virtual container for FlowComponentHost
                self._pending_execute.append(
                    [{"@v-node": node_id}, "return (async function() { Vaadin.FlowComponentHost.patchVirtualContainer(this)}).apply($0)"]
                )
                # 3. Set renderer - uses text property or FlowComponentHost for children
                self._pending_execute.append(
                    [self._app_id, {"@v-node": node_id}, "return (async function() { this.renderer = (root) => {  if (this.text) {    root.textContent = this.text;  } else {    Vaadin.FlowComponentHost.setChildNodes($0, this.virtualChildNodeIds, root)  }}}).apply($1)"]
                )
                # 4. Request content update AFTER setting renderer
                self._pending_execute.append(
                    [{"@v-node": node_id}, "return $0.requestContentUpdate()"]
                )

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

    def _handle_published_event(self, rpc: dict):
        """Handle publishedEventHandler RPC (client-callable methods).

        Dispatches to the component method named by templateEventMethodName.
        Used by Dialog (handleClientClose), Grid (select, deselect, etc.).
        """
        node_id = rpc.get("node")
        method_name = rpc.get("templateEventMethodName")
        args = rpc.get("templateEventMethodArgs", [])

        component = self._tree.get_component(node_id)
        if component and method_name:
            # Convert camelCase to snake_case for Python method lookup
            import re
            py_name = re.sub(r'([A-Z])', r'_\1', method_name).lower().lstrip('_')
            method = getattr(component, py_name, None)
            if method and callable(method):
                method(*args)

    def _build_response(self) -> dict:
        """Build UIDL response."""
        changes = self._tree.collect_changes()
        self._sync_id += 1
        # clientId reflects the last client message we processed
        self._client_id = self._last_client_id + 1

        # Check for newly attached notification or dialog nodes
        # and add execute commands for FlowComponentHost
        self._add_execute_for_new_overlays(changes)

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
            "opened-changed": (_OPENED_CHANGED_HASH, _OPENED_CHANGED_CONFIG),
            "checked-changed": (_CHECKED_CHANGED_HASH, _CHECKED_CHANGED_CONFIG),
            "keydown": (_KEYDOWN_HASH, _KEYDOWN_CONFIG),
        }

        # Add used constants and replace values with hash references.
        # Only send constants that haven't been sent in a previous response,
        # as FlowClient caches them and resending causes processing errors.
        for change in changes:
            if change.get("feat") == Feature.ELEMENT_LISTENER_MAP:
                value = change.get("value")
                if value is True:
                    # Resolve event type → hash via event_configs lookup
                    event_type = change.get("key")
                    if event_type in event_configs:
                        hash_key, config = event_configs[event_type]
                        if hash_key not in self._sent_constants:
                            constants[hash_key] = config
                            self._sent_constants.add(hash_key)
                        change["value"] = hash_key
                elif isinstance(value, str) and value in _HASH_TO_CONFIG:
                    # Explicit hash from component — only send config if new
                    if value not in self._sent_constants:
                        constants[value] = _HASH_TO_CONFIG[value]
                        self._sent_constants.add(value)

        response = {
            "syncId": self._sync_id,
            "clientId": self._client_id,
            "constants": constants,
            "changes": changes,
        }
        # Merge execute commands from both UidlHandler and tree (components)
        tree_execute = self._tree.collect_execute()
        all_execute = self._pending_execute + tree_execute
        if all_execute:
            response["execute"] = all_execute
        self._pending_execute = []
        return response
