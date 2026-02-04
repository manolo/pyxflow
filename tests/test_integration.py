"""Integration Tests.

These tests verify the complete flow matches the Java reference implementation.
For full integration tests with HTTP and Playwright, use specs/tests/run_tests.py
"""

import pytest


class TestCompleteFlow:
    """Test complete flow from init to click."""

    def test_full_hello_world_flow(self):
        """Test the complete HelloWorld flow."""
        from vaadin.flow.server.uidl_handler import UidlHandler
        from vaadin.flow.core.state_tree import StateTree
        from vaadin.flow.core.state_node import Feature

        # 1. Create handler
        tree = StateTree()
        handler = UidlHandler(tree)

        # 2. Init request
        init = handler.handle_init({})
        assert init["appConfig"]["productionMode"] is True
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]
        assert csrf is not None

        # 3. Navigation request
        nav_response = handler.handle_uidl({
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "", "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        })

        # Verify view was created
        changes = nav_response.get("changes", [])
        tags = [c["value"] for c in changes if c.get("key") == "tag"]
        assert "vaadin-vertical-layout" in tags
        assert "vaadin-horizontal-layout" in tags
        assert "vaadin-text-field" in tags
        assert "vaadin-button" in tags

        # Find node IDs
        tf_node = next(c["node"] for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-text-field")
        btn_node = next(c["node"] for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-button")

        # 4. Set text field value
        sync_id = nav_response["syncId"]
        handler.handle_uidl({
            "csrfToken": csrf,
            "rpc": [
                {"type": "mSync", "node": tf_node, "feature": Feature.ELEMENT_PROPERTY_MAP, "property": "value", "value": "World"},
                {"type": "event", "node": tf_node, "event": "change", "data": {}}
            ],
            "syncId": sync_id,
            "clientId": 0,
        })

        # 5. Click button
        click_response = handler.handle_uidl({
            "csrfToken": csrf,
            "rpc": [{"type": "event", "node": btn_node, "event": "click", "data": {}}],
            "syncId": sync_id + 1,
            "clientId": 0,
        })

        # Verify Span was added
        click_changes = click_response.get("changes", [])
        span_tag = next((c for c in click_changes if c.get("key") == "tag" and c.get("value") == "span"), None)
        assert span_tag is not None, "Click should create a span"

        # Verify text is "Hello World"
        text_node = next(
            (c for c in click_changes if c.get("feat") == Feature.TEXT_NODE and c.get("key") == "text"),
            None
        )
        assert text_node is not None
        assert text_node["value"] == "Hello World"


class TestUidlResponseFormat:
    """Test UIDL response format matches Java."""

    def test_response_has_required_fields(self):
        """Response should have syncId, clientId, changes."""
        from vaadin.flow.server.uidl_handler import UidlHandler
        from vaadin.flow.core.state_tree import StateTree

        tree = StateTree()
        handler = UidlHandler(tree)
        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        response = handler.handle_uidl({
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "", "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        })

        assert "syncId" in response
        assert "changes" in response
        assert isinstance(response["changes"], list)

    def test_change_format(self):
        """Each change should have node, type, and appropriate fields."""
        from vaadin.flow.server.uidl_handler import UidlHandler
        from vaadin.flow.core.state_tree import StateTree

        tree = StateTree()
        handler = UidlHandler(tree)
        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]

        response = handler.handle_uidl({
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": "", "query": "", "appShellTitle": "", "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": 0,
            "clientId": 0,
        })

        for change in response["changes"]:
            assert "node" in change
            assert "type" in change
            assert change["type"] in ["attach", "put", "splice", "detach", "remove", "clear"]

            if change["type"] == "put":
                assert "key" in change
                assert "feat" in change
                assert "value" in change

            if change["type"] == "splice":
                assert "feat" in change
                assert "index" in change
