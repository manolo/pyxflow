"""Tests for UIDL response format.

Based on Java Flow's UidlWriterTest.java patterns.
Tests response structure, changes format, and constants handling.
"""

import pytest

from vaadin.flow.server.uidl_handler import UidlHandler
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


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

        # Should have navigation event constants
        assert "c0" in constants  # ui-navigate config
        assert "c1" in constants  # ui-leave-navigation config
        assert "c2" in constants  # ui-refresh config

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
