"""Tests for Navigation RPC handling.

Based on Java Flow's NavigationRpcHandlerTest.java patterns.
Tests view creation, execute commands, and navigation behavior.
"""

import pytest

from vaadin.flow.server.uidl_handler import UidlHandler
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestNavigationCreatesView:
    """Test that navigation creates the view structure."""

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

    def test_navigation_creates_view_structure(self, session):
        """Navigation should create complete view structure."""
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

        # Should have multiple components
        tags = [c.get("value") for c in changes if c.get("key") == "tag"]
        assert "vaadin-vertical-layout" in tags
        assert "vaadin-horizontal-layout" in tags
        assert "vaadin-text-field" in tags
        assert "vaadin-button" in tags

    def test_navigation_creates_attach_changes(self, session):
        """Navigation should create attach changes for new nodes."""
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

        # Should have attach changes
        attach_changes = [c for c in changes if c.get("type") == "attach"]
        assert len(attach_changes) > 0

    def test_navigation_creates_splice_changes(self, session):
        """Navigation should create splice changes for children."""
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

        # Should have splice changes for children
        splice_changes = [c for c in changes if c.get("type") == "splice"]
        assert len(splice_changes) > 0


class TestNavigationExecuteCommands:
    """Test execute commands in navigation response."""

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

    def test_navigation_response_has_execute_commands(self, session):
        """Navigation response should include execute commands."""
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

        assert "execute" in response
        assert isinstance(response["execute"], list)
        assert len(response["execute"]) > 0

    def test_navigation_sets_document_title(self, session):
        """Navigation should set document title via execute."""
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

        # Should have title execute command
        title_cmd = next(
            (cmd for cmd in response.get("execute", [])
             if "document.title" in str(cmd)),
            None
        )
        assert title_cmd is not None

    def test_navigation_has_server_connected_command(self, session):
        """Navigation should include serverConnected execute command."""
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

        # Should have serverConnected command
        server_cmd = next(
            (cmd for cmd in response.get("execute", [])
             if "serverConnected" in str(cmd)),
            None
        )
        assert server_cmd is not None


class TestNavigationAddKeydownListener:
    """Test that navigation adds keydown listener."""

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

    def test_navigation_adds_keydown_listener(self, session):
        """Navigation should add keydown listener to body."""
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

        # Should have keydown listener on body (node 1)
        keydown_change = next(
            (c for c in changes
             if c.get("node") == 1 and
             c.get("key") == "keydown" and
             c.get("feat") == Feature.ELEMENT_LISTENER_MAP),
            None
        )
        assert keydown_change is not None


class TestSameRouteNavigationSkipped:
    """Test that same-route navigation doesn't recreate view."""

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

    def test_same_route_navigation_skipped(self, session):
        """Same route navigation should not recreate view."""
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

        # Second navigation
        payload2 = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "",
                         "historyState": {"idx": 1}, "trigger": ""}
            }],
            "syncId": response1["syncId"],
            "clientId": 1,
        }
        response2 = session["handler"].handle_uidl(payload2)

        # Second response should not have new component tags
        tags2 = [
            c.get("value") for c in response2.get("changes", [])
            if c.get("key") == "tag"
        ]
        assert len(tags2) == 0, "Second navigation should not create new components"

    def test_second_navigation_no_execute_commands(self, session):
        """Second navigation should not have execute commands."""
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

        # Second navigation
        payload2 = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "",
                         "historyState": {"idx": 1}, "trigger": ""}
            }],
            "syncId": response1["syncId"],
            "clientId": 1,
        }
        response2 = session["handler"].handle_uidl(payload2)

        # Second response should not have execute commands
        assert "execute" not in response2 or len(response2.get("execute", [])) == 0


class TestNavigationViewComponents:
    """Test specific components in navigation response."""

    @pytest.fixture
    def navigation_response(self):
        """Get navigation response."""
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

    def test_text_field_has_label(self, navigation_response):
        """TextField should have label property."""
        changes = navigation_response.get("changes", [])

        label = next(
            (c for c in changes if c.get("key") == "label"),
            None
        )
        assert label is not None
        assert label.get("value") == "Your name"

    def test_button_has_text_node(self, navigation_response):
        """Button should have text node with 'Say hello'."""
        changes = navigation_response.get("changes", [])

        text = next(
            (c for c in changes
             if c.get("feat") == Feature.TEXT_NODE and
             c.get("key") == "text" and
             c.get("value") == "Say hello"),
            None
        )
        assert text is not None

    def test_vertical_layout_has_theme(self, navigation_response):
        """VerticalLayout should have theme with padding and spacing."""
        changes = navigation_response.get("changes", [])

        theme = next(
            (c for c in changes
             if c.get("key") == "theme" and
             "padding" in str(c.get("value", ""))),
            None
        )
        assert theme is not None

    def test_button_has_click_listener(self, navigation_response):
        """Button should have click listener."""
        changes = navigation_response.get("changes", [])

        click_listener = next(
            (c for c in changes
             if c.get("key") == "click" and
             c.get("feat") == Feature.ELEMENT_LISTENER_MAP),
            None
        )
        assert click_listener is not None


class TestNavigationHistoryState:
    """Test navigation with different history states."""

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

    def test_navigation_with_history_index(self, session):
        """Navigation with history index should work."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {
                    "route": "",
                    "query": "",
                    "appShellTitle": "",
                    "historyState": {"idx": 5},
                    "trigger": ""
                }
            }],
            "syncId": 0,
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)

        assert "syncId" in response
        assert len(response.get("changes", [])) > 0

    def test_navigation_with_trigger(self, session):
        """Navigation with trigger should work."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {
                    "route": "",
                    "query": "",
                    "appShellTitle": "",
                    "historyState": {"idx": 0},
                    "trigger": "popstate"
                }
            }],
            "syncId": 0,
            "clientId": 0,
        }
        response = session["handler"].handle_uidl(payload)

        assert "syncId" in response


class TestNavigationContainerStructure:
    """Test container structure after navigation."""

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

    def test_view_attached_to_container(self, session):
        """View should be attached to flow-container."""
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

        # Should have splice to container node
        container_id = session["handler"]._container_node.id
        container_splice = next(
            (c for c in changes
             if c.get("node") == container_id and
             c.get("type") == "splice" and
             c.get("feat") == Feature.ELEMENT_CHILDREN_LIST),
            None
        )
        assert container_splice is not None
        assert len(container_splice.get("addNodes", [])) > 0
