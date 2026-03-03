"""Tests for UIDL response format.

Based on Java Flow's UidlWriterTest.java patterns.
Tests response structure, changes format, and constants handling.
"""

import pytest

from pyxflow.server.uidl_handler import UidlHandler
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature


class TestResponseStructure:
    """Test UIDL response structure."""

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

    def test_response_has_sync_id(self, session):
        """Response should have syncId."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)

        assert "syncId" in response
        assert isinstance(response["syncId"], int)

    def test_response_has_client_id(self, session):
        """Response should have clientId."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)

        assert "clientId" in response
        assert isinstance(response["clientId"], int)

    def test_response_has_changes(self, session):
        """Response should have changes array."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)

        assert "changes" in response
        assert isinstance(response["changes"], list)

    def test_response_has_constants(self, session):
        """Response should have constants object."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)

        assert "constants" in response
        assert isinstance(response["constants"], dict)


class TestSyncIdIncrement:
    """Test syncId increment behavior."""

    @pytest.fixture
    def session(self):
        """Create session with init completed."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return {
            "handler": handler,
            "csrf": csrf,
        }

    def test_sync_id_incremented_each_response(self, session):
        """SyncId should increment with each response."""
        last_sync_id = 0

        for i in range(5):
            payload = {
                "csrfToken": session["csrf"],
                "rpc": [],
                "syncId": last_sync_id,
                "clientId": i,
            }
            response = session["handler"].handle_uidl(payload)

            assert response["syncId"] > last_sync_id
            last_sync_id = response["syncId"]

    def test_sync_id_sequential(self, session):
        """SyncId should be sequential (1, 2, 3, ...)."""
        sync_ids = []

        for i in range(3):
            payload = {
                "csrfToken": session["csrf"],
                "rpc": [],
                "syncId": sync_ids[-1] if sync_ids else 0,
                "clientId": i,
            }
            response = session["handler"].handle_uidl(payload)
            sync_ids.append(response["syncId"])

        assert sync_ids == [1, 2, 3]


class TestClientIdTracking:
    """Test clientId tracking in response."""

    @pytest.fixture
    def session(self):
        """Create session with init completed."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return {
            "handler": handler,
            "csrf": csrf,
        }

    def test_client_id_reflects_message_count(self, session):
        """ClientId in response should reflect processed messages."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)

        # First message (clientId 0) should result in clientId 1
        assert response["clientId"] == 1

    def test_client_id_increments_correctly(self, session):
        """ClientId should track incoming message count."""
        for i in range(4):
            payload = {
                "csrfToken": session["csrf"],
                "rpc": [],
                "syncId": i,
                "clientId": i,
            }
            response = session["handler"].handle_uidl(payload)

            # Response clientId should be input + 1
            assert response["clientId"] == i + 1


class TestChangesFormat:
    """Test format of changes in response."""

    @pytest.fixture
    def navigation_response(self):
        """Get navigation response with changes."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]

        payload = {
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
        return handler.handle_uidl(payload)

    def test_change_has_node_id(self, navigation_response):
        """Each change should have node ID."""
        changes = navigation_response.get("changes", [])

        for change in changes:
            assert "node" in change

    def test_change_has_type(self, navigation_response):
        """Each change should have type."""
        changes = navigation_response.get("changes", [])

        for change in changes:
            assert "type" in change

    def test_put_change_has_key_and_value(self, navigation_response):
        """Put changes should have key and value."""
        changes = navigation_response.get("changes", [])
        put_changes = [c for c in changes if c.get("type") == "put"]

        assert len(put_changes) > 0
        for change in put_changes:
            assert "key" in change
            assert "value" in change or "nodeValue" in change

    def test_put_change_has_feat(self, navigation_response):
        """Put changes should have feat (feature ID)."""
        changes = navigation_response.get("changes", [])
        put_changes = [c for c in changes if c.get("type") == "put"]

        for change in put_changes:
            assert "feat" in change

    def test_attach_change_format(self, navigation_response):
        """Attach changes should have correct format."""
        changes = navigation_response.get("changes", [])
        attach_changes = [c for c in changes if c.get("type") == "attach"]

        for change in attach_changes:
            assert "node" in change
            assert change["type"] == "attach"

    def test_splice_change_has_index_and_nodes(self, navigation_response):
        """Splice changes should have index and addNodes."""
        changes = navigation_response.get("changes", [])
        splice_changes = [c for c in changes if c.get("type") == "splice"]

        assert len(splice_changes) > 0
        for change in splice_changes:
            assert "index" in change
            assert "addNodes" in change or "remove" in change


class TestConstantsInResponse:
    """Test constants handling in response."""

    @pytest.fixture
    def navigation_response(self):
        """Get navigation response with constants."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]

        payload = {
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
        return handler.handle_uidl(payload)

    def test_constants_has_event_configs(self, navigation_response):
        """Constants should contain event configurations."""
        constants = navigation_response.get("constants", {})

        # Should have some constants (event listener configs)
        assert len(constants) > 0

    def test_constants_referenced_in_changes(self, navigation_response):
        """Constants should be referenced in listener changes."""
        constants = navigation_response.get("constants", {})
        changes = navigation_response.get("changes", [])

        # Get listener changes
        listener_changes = [
            c for c in changes
            if c.get("feat") == Feature.ELEMENT_LISTENER_MAP
        ]

        # At least one listener should reference a constant
        constant_refs = [
            c.get("value") for c in listener_changes
            if isinstance(c.get("value"), str) and c.get("value") in constants
        ]
        assert len(constant_refs) > 0

    def test_click_constant_has_event_properties(self, navigation_response):
        """Click constant should define event properties to sync."""
        constants = navigation_response.get("constants", {})

        # Find click constant (it's a hash)
        click_constants = [
            v for v in constants.values()
            if isinstance(v, dict) and "event.button" in v
        ]

        if click_constants:
            click_const = click_constants[0]
            assert "event.clientX" in click_const
            assert "event.clientY" in click_const


class TestExecuteCommands:
    """Test execute commands in response."""

    @pytest.fixture
    def navigation_response(self):
        """Get navigation response with execute commands."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]

        payload = {
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
        return handler.handle_uidl(payload)

    def test_execute_commands_format(self, navigation_response):
        """Execute commands should be arrays."""
        execute = navigation_response.get("execute", [])

        assert isinstance(execute, list)
        for cmd in execute:
            assert isinstance(cmd, list)

    def test_execute_commands_have_script(self, navigation_response):
        """Execute commands should have JavaScript code."""
        execute = navigation_response.get("execute", [])

        for cmd in execute:
            # Last element should be the script
            script = cmd[-1]
            assert isinstance(script, str)

    def test_execute_command_node_reference(self, navigation_response):
        """Execute commands can reference nodes."""
        execute = navigation_response.get("execute", [])

        # Some commands should have node references
        node_refs = [
            cmd for cmd in execute
            if any(isinstance(arg, dict) and "@v-node" in arg for arg in cmd[:-1])
        ]
        assert len(node_refs) > 0


class TestResponseWithNoChanges:
    """Test response when there are no changes."""

    @pytest.fixture
    def session(self):
        """Create session with init completed."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return {
            "handler": handler,
            "csrf": csrf,
        }

    def test_empty_changes_valid_response(self, session):
        """Response with no changes should still be valid."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)

        # Should have all required fields
        assert "syncId" in response
        assert "clientId" in response
        assert "changes" in response
        assert "constants" in response

    def test_heartbeat_returns_valid_response(self, session):
        """Heartbeat (empty RPC) should return valid response."""
        # First navigate to create view
        nav_payload = {
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
        nav_response = session["handler"].handle_uidl(nav_payload)

        # Then send heartbeat
        heartbeat = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": nav_response["syncId"],
            "clientId": 1,
        }
        response = session["handler"].handle_uidl(heartbeat)

        # Should still increment syncId
        assert response["syncId"] > nav_response["syncId"]
        assert isinstance(response["changes"], list)


class TestSyncIdValidation:
    """Test SyncId mismatch triggers resync."""

    @pytest.fixture
    def session(self):
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return {"handler": handler, "csrf": csrf}

    def test_wrong_sync_id_triggers_resync(self, session):
        """SyncId mismatch should return resynchronize response."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 999,  # Wrong syncId (expected 0)
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)
        assert response.get("resynchronize") is True

    def test_resync_does_not_increment_sync_id(self, session):
        """Resync response should not change the server's syncId."""
        # Send valid request first
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        resp1 = session["handler"].handle_uidl(payload)
        sync_id_after = resp1["syncId"]  # Should be 1

        # Send with wrong syncId
        payload2 = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 999,
            "clientId": 1,
        }
        resync = session["handler"].handle_uidl(payload2)
        assert resync.get("resynchronize") is True
        assert resync["syncId"] == sync_id_after  # Unchanged


class TestClientIdValidation:
    """Test ClientId validation and duplicate detection."""

    @pytest.fixture
    def session(self):
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return {"handler": handler, "csrf": csrf}

    def test_wrong_client_id_triggers_resync(self, session):
        """ClientId mismatch (not duplicate) should trigger resync."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 5,  # Expected 0
        }
        response = session["handler"].handle_uidl(payload)
        assert response.get("resynchronize") is True

    def test_duplicate_client_id_returns_cached(self, session):
        """Duplicate clientId should return the previous response."""
        # Send first request (clientId 0)
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        resp1 = session["handler"].handle_uidl(payload)
        assert "resynchronize" not in resp1

        # Resend with same clientId (duplicate)
        payload2 = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": resp1["syncId"],
            "clientId": 0,  # Same as before → duplicate
        }
        resp2 = session["handler"].handle_uidl(payload2)
        # Should return cached response, not a resync
        assert resp2 is resp1


class TestResynchronize:
    """Test explicit resynchronize request from client."""

    @pytest.fixture
    def session(self):
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return {"handler": handler, "csrf": csrf}

    def test_client_resync_flag(self, session):
        """Client setting resynchronize=true should get resync response."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
            "resynchronize": True,
        }
        response = session["handler"].handle_uidl(payload)
        assert response.get("resynchronize") is True
        assert response["changes"] == []
        assert response["constants"] == {}

    def test_resync_response_has_correct_ids(self, session):
        """Resync response should have current syncId and expected clientId."""
        # First do a valid request to advance the IDs
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        resp1 = session["handler"].handle_uidl(payload)

        # Request resync
        payload2 = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": resp1["syncId"],
            "clientId": 1,
            "resynchronize": True,
        }
        resync = session["handler"].handle_uidl(payload2)
        assert resync["syncId"] == resp1["syncId"]  # Not incremented
        assert resync.get("resynchronize") is True


class TestOverlayClientKey:
    """Test that overlay execute commands use 'ROOT' (client key), not full appId."""

    @pytest.fixture
    def handler_with_dialog(self):
        """Create handler that navigates to a view with a Dialog."""
        from pyxflow.components.dialog import Dialog
        from pyxflow.components.span import Span
        from pyxflow.components import VerticalLayout
        from pyxflow.router import Route

        # Register a temporary view with a Dialog
        @Route("_test_dialog_key")
        class TestDialogView(VerticalLayout):
            def __init__(self):
                super().__init__()
                self.dialog = Dialog()
                self.dialog.add(Span("Hello"))
                self.dialog.set_opened(True)
                self.add(self.dialog)

        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]

        payload = {
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "_test_dialog_key", "query": "", "appShellTitle": "",
                         "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        }
        response = handler.handle_uidl(payload)

        # Clean up route registry
        from pyxflow.router import _routes
        _routes.pop("_test_dialog_key", None)

        return handler, response

    def test_dialog_setChildNodes_uses_root_key(self, handler_with_dialog):
        """Dialog renderer should pass 'ROOT' to FlowComponentHost.setChildNodes."""
        handler, response = handler_with_dialog
        execute = response.get("execute", [])

        # Find commands with FlowComponentHost.setChildNodes
        fch_cmds = [cmd for cmd in execute if "setChildNodes" in cmd[-1]]
        assert len(fch_cmds) > 0, "Should have FlowComponentHost.setChildNodes commands"

        for cmd in fch_cmds:
            # First arg should be "ROOT" (client key), not "ROOT-1234567"
            assert cmd[0] == "ROOT", f"Expected 'ROOT', got '{cmd[0]}'"
            assert "-" not in cmd[0], "Client key should not contain hyphen"

    @pytest.fixture
    def handler_with_notification(self):
        """Create handler that navigates to a view with a Notification."""
        from pyxflow.components.notification import Notification
        from pyxflow.components.span import Span
        from pyxflow.components import VerticalLayout
        from pyxflow.router import Route

        @Route("_test_notif_key")
        class TestNotifView(VerticalLayout):
            def __init__(self):
                super().__init__()
                self.notif = Notification()
                self.notif.add(Span("Alert"))
                self.notif.set_opened(True)
                self.add(self.notif)

        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]

        payload = {
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "_test_notif_key", "query": "", "appShellTitle": "",
                         "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        }
        response = handler.handle_uidl(payload)

        from pyxflow.router import _routes
        _routes.pop("_test_notif_key", None)

        return handler, response

    def test_notification_setChildNodes_uses_root_key(self, handler_with_notification):
        """Notification renderer should pass 'ROOT' to FlowComponentHost.setChildNodes."""
        handler, response = handler_with_notification
        execute = response.get("execute", [])

        fch_cmds = [cmd for cmd in execute if "setChildNodes" in cmd[-1]]
        assert len(fch_cmds) > 0, "Should have FlowComponentHost.setChildNodes commands"

        for cmd in fch_cmds:
            assert cmd[0] == "ROOT", f"Expected 'ROOT', got '{cmd[0]}'"


class TestInitResponseUidl:
    """Test UIDL structure in init response."""

    def test_init_uidl_has_required_fields(self):
        """Init UIDL should have all required fields."""
        tree = StateTree()
        handler = UidlHandler(tree)
        response = handler.handle_init({})

        uidl = response["appConfig"]["uidl"]

        assert "syncId" in uidl
        assert "clientId" in uidl
        assert "changes" in uidl
        assert "constants" in uidl
        assert "Vaadin-Security-Key" in uidl

    def test_init_uidl_constants_format(self):
        """Init UIDL constants should have proper format."""
        tree = StateTree()
        handler = UidlHandler(tree)
        response = handler.handle_init({})

        constants = response["appConfig"]["uidl"]["constants"]

        # Should have navigation event constants (using Java Flow hashes)
        assert "msDV4SvCysE=" in constants  # ui-navigate config
        assert "i2nDWhpwLZE=" in constants  # ui-leave-navigation config
        assert "18ACma10cDE=" in constants  # ui-refresh config

    def test_init_uidl_changes_create_ui_structure(self):
        """Init UIDL changes should create UI structure."""
        tree = StateTree()
        handler = UidlHandler(tree)
        response = handler.handle_init({})

        changes = response["appConfig"]["uidl"]["changes"]

        # Should create body node
        body_change = next(
            (c for c in changes
             if c.get("key") == "tag" and c.get("value") == "body"),
            None
        )
        assert body_change is not None

        # Should create flow-container
        container_change = next(
            (c for c in changes
             if c.get("key") == "tag" and "flow-container" in str(c.get("value", ""))),
            None
        )
        assert container_change is not None
