"""Tests for RPC message validation.

Based on Java Flow's ServerRpcHandlerTest.java patterns.
Tests CSRF token validation, clientId sequencing, and message handling.
"""

import pytest

from vaadin.flow.server.uidl_handler import UidlHandler
from vaadin.flow.core.state_tree import StateTree


class TestCsrfValidation:
    """Test CSRF token validation."""

    @pytest.fixture
    def session(self):
        """Create a session with init completed."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return {
            "handler": handler,
            "tree": tree,
            "csrf": csrf,
            "sync_id": 0,
            "client_id": 0,
        }

    def test_valid_csrf_token_accepted(self, session):
        """Valid CSRF token should be accepted."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)

        # Should return valid response with incremented syncId
        assert "syncId" in response
        assert response["syncId"] > session["sync_id"]

    def test_empty_rpc_array_valid(self, session):
        """Empty RPC array (heartbeat) should be valid."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)

        assert "syncId" in response
        assert "changes" in response
        # Empty RPC should still work
        assert isinstance(response["changes"], list)


class TestClientIdSequencing:
    """Test clientId sequential handling."""

    @pytest.fixture
    def session(self):
        """Create a session with init completed."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return {
            "handler": handler,
            "tree": tree,
            "csrf": csrf,
        }

    def test_client_id_starts_at_zero(self, session):
        """First client message should have clientId 0."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)

        # Server should acknowledge with incremented clientId
        assert response["clientId"] == 1

    def test_client_id_increments_sequentially(self, session):
        """ClientId should increment with each message."""
        # First message
        payload1 = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        response1 = session["handler"].handle_uidl(payload1)

        # Second message
        payload2 = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": response1["syncId"],
            "clientId": 1,
        }
        response2 = session["handler"].handle_uidl(payload2)

        # Should have incremented
        assert response2["clientId"] == 2

    def test_multiple_messages_track_client_id(self, session):
        """Multiple sequential messages should track clientId correctly."""
        last_sync_id = 0
        last_client_id = 0

        for i in range(5):
            payload = {
                "csrfToken": session["csrf"],
                "rpc": [],
                "syncId": last_sync_id,
                "clientId": i,
            }
            response = session["handler"].handle_uidl(payload)

            assert response["clientId"] == i + 1
            last_sync_id = response["syncId"]


class TestSyncIdHandling:
    """Test syncId handling."""

    @pytest.fixture
    def session(self):
        """Create a session with init completed."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return {
            "handler": handler,
            "tree": tree,
            "csrf": csrf,
        }

    def test_sync_id_increments_with_each_response(self, session):
        """SyncId should increment with each response."""
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

        # Each syncId should be greater than the previous
        for i in range(1, len(sync_ids)):
            assert sync_ids[i] > sync_ids[i - 1]

    def test_initial_sync_id_is_one(self, session):
        """First response syncId should be 1."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)

        assert response["syncId"] == 1


class TestMessageValidation:
    """Test general message validation."""

    @pytest.fixture
    def session(self):
        """Create a session with init completed."""
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return {
            "handler": handler,
            "tree": tree,
            "csrf": csrf,
        }

    def test_rpc_missing_defaults_to_empty(self, session):
        """Missing rpc field should default to empty list."""
        payload = {
            "csrfToken": session["csrf"],
            "syncId": 0,
            "clientId": 0,
        }
        # Should not raise
        response = session["handler"].handle_uidl(payload)
        assert "syncId" in response

    def test_response_always_has_required_fields(self, session):
        """Response should always have required fields."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [],
            "syncId": 0,
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)

        assert "syncId" in response
        assert "clientId" in response
        assert "changes" in response
        assert "constants" in response


class TestInitResponse:
    """Test init response structure."""

    def test_init_response_has_app_config(self):
        """Init response should have appConfig."""
        tree = StateTree()
        handler = UidlHandler(tree)
        response = handler.handle_init({})

        assert "appConfig" in response

    def test_init_response_has_csrf_token(self):
        """Init response should contain CSRF token."""
        tree = StateTree()
        handler = UidlHandler(tree)
        response = handler.handle_init({})

        csrf = response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        assert csrf is not None
        assert len(csrf) > 0

    def test_init_response_has_initial_sync_id(self):
        """Init response should have syncId 0."""
        tree = StateTree()
        handler = UidlHandler(tree)
        response = handler.handle_init({})

        sync_id = response["appConfig"]["uidl"]["syncId"]
        assert sync_id == 0

    def test_init_response_has_app_id(self):
        """Init response should have appId."""
        tree = StateTree()
        handler = UidlHandler(tree)
        response = handler.handle_init({})

        app_id = response["appConfig"]["appId"]
        assert app_id is not None
        assert app_id.startswith("ROOT-")

    def test_init_response_has_initial_changes(self):
        """Init response should have initial UI structure changes."""
        tree = StateTree()
        handler = UidlHandler(tree)
        response = handler.handle_init({})

        changes = response["appConfig"]["uidl"]["changes"]
        assert len(changes) > 0

        # Should have body node (tag=body)
        body_tag = next(
            (c for c in changes if c.get("key") == "tag" and c.get("value") == "body"),
            None
        )
        assert body_tag is not None

    def test_init_creates_navigation_listeners(self):
        """Init should create ui-navigate listener on body."""
        tree = StateTree()
        handler = UidlHandler(tree)
        response = handler.handle_init({})

        changes = response["appConfig"]["uidl"]["changes"]

        # Should have ui-navigate listener
        nav_listener = next(
            (c for c in changes if c.get("key") == "ui-navigate"),
            None
        )
        assert nav_listener is not None

    def test_init_response_has_constants(self):
        """Init response should have constants for event configs."""
        tree = StateTree()
        handler = UidlHandler(tree)
        response = handler.handle_init({})

        constants = response["appConfig"]["uidl"]["constants"]
        assert constants is not None
        assert isinstance(constants, dict)

    def test_multiple_init_calls_idempotent(self):
        """Multiple init calls should return same structure."""
        tree = StateTree()
        handler = UidlHandler(tree)

        response1 = handler.handle_init({})
        response2 = handler.handle_init({})

        # Should have same CSRF token
        csrf1 = response1["appConfig"]["uidl"]["Vaadin-Security-Key"]
        csrf2 = response2["appConfig"]["uidl"]["Vaadin-Security-Key"]
        assert csrf1 == csrf2

        # Should have same appId
        assert response1["appConfig"]["appId"] == response2["appConfig"]["appId"]
