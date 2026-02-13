"""Navigation Event Tests."""

import pytest


class TestNavigationRequest:
    """Test navigation event handling."""

    @pytest.fixture
    def session(self):
        """Create a session with init completed."""
        from vaadin.flow.server.uidl_handler import UidlHandler
        from vaadin.flow.core.state_tree import StateTree

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

    def test_navigation_returns_uidl(self, session):
        """Navigation should return UIDL response."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "", "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)
        assert "syncId" in response
        assert "changes" in response

    def test_navigation_increments_sync_id(self, session):
        """Navigation should increment syncId."""
        payload = {
            "csrfToken": session["csrf"],
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "", "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": session["sync_id"],
            "clientId": session["client_id"],
        }
        response = session["handler"].handle_uidl(payload)
        assert response["syncId"] > session["sync_id"]


class TestViewCreation:
    """Test that navigation creates the view."""

    @pytest.fixture
    def navigation_changes(self):
        """Get changes from navigation response."""
        from vaadin.flow.server.uidl_handler import UidlHandler
        from vaadin.flow.core.state_tree import StateTree

        tree = StateTree()
        handler = UidlHandler(tree)
        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        payload = {
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
        response = handler.handle_uidl(payload)
        return response.get("changes", [])

    def test_creates_vertical_layout(self, navigation_changes):
        """Should create vaadin-vertical-layout node."""
        vl = next(
            (c for c in navigation_changes
             if c.get("key") == "tag" and c.get("value") == "vaadin-vertical-layout"),
            None
        )
        assert vl is not None, "Should create vaadin-vertical-layout"

    def test_creates_horizontal_layout(self, navigation_changes):
        """Should create vaadin-horizontal-layout node."""
        hl = next(
            (c for c in navigation_changes
             if c.get("key") == "tag" and c.get("value") == "vaadin-horizontal-layout"),
            None
        )
        assert hl is not None, "Should create vaadin-horizontal-layout"

    def test_creates_text_field(self, navigation_changes):
        """Should create vaadin-text-field node."""
        tf = next(
            (c for c in navigation_changes
             if c.get("key") == "tag" and c.get("value") == "vaadin-text-field"),
            None
        )
        assert tf is not None, "Should create vaadin-text-field"

    def test_creates_button(self, navigation_changes):
        """Should create vaadin-button node."""
        btn = next(
            (c for c in navigation_changes
             if c.get("key") == "tag" and c.get("value") == "vaadin-button"),
            None
        )
        assert btn is not None, "Should create vaadin-button"

    def test_text_field_has_label(self, navigation_changes):
        """TextField should have label 'Your name'."""
        label = next(
            (c for c in navigation_changes
             if c.get("key") == "label" and c.get("value") == "Your name"),
            None
        )
        assert label is not None, "TextField should have label 'Your name'"

    def test_button_has_text(self, navigation_changes):
        """Button should have text 'Say hello'."""
        text = next(
            (c for c in navigation_changes
             if c.get("feat") == 7 and c.get("key") == "text" and c.get("value") == "Say hello"),
            None
        )
        assert text is not None, "Button should have text 'Say hello'"

    def test_vertical_layout_has_theme(self, navigation_changes):
        """VerticalLayout should have theme 'padding spacing'."""
        theme = next(
            (c for c in navigation_changes
             if c.get("key") == "theme" and "padding" in str(c.get("value", "")) and "spacing" in str(c.get("value", ""))),
            None
        )
        assert theme is not None, "VerticalLayout should have theme with padding and spacing"
