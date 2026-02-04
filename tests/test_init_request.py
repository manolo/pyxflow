"""Init Request Tests."""

import pytest
import re


class TestAppConfig:
    """Test appConfig structure from init response."""

    @pytest.fixture
    def init_response(self):
        """Simulated init response for testing."""
        from vaadin.flow.server.uidl_handler import UidlHandler
        from vaadin.flow.core.state_tree import StateTree

        tree = StateTree()
        handler = UidlHandler(tree)
        return handler.handle_init({})

    def test_has_app_config(self, init_response):
        """Response should have appConfig."""
        assert "appConfig" in init_response

    def test_production_mode(self, init_response):
        """appConfig.productionMode should be true."""
        assert init_response["appConfig"]["productionMode"] is True

    def test_ui_id(self, init_response):
        """appConfig.v-uiId should be 0."""
        assert init_response["appConfig"]["v-uiId"] == 0

    def test_app_id_format(self, init_response):
        """appConfig.appId should match ROOT-* pattern."""
        app_id = init_response["appConfig"]["appId"]
        assert re.match(r"ROOT-\d+", app_id)

    def test_has_uidl(self, init_response):
        """appConfig should have uidl."""
        assert "uidl" in init_response["appConfig"]

    def test_uidl_sync_id(self, init_response):
        """uidl.syncId should be 0."""
        assert init_response["appConfig"]["uidl"]["syncId"] == 0

    def test_uidl_client_id(self, init_response):
        """uidl.clientId should be 0."""
        assert init_response["appConfig"]["uidl"]["clientId"] == 0

    def test_uidl_has_csrf(self, init_response):
        """uidl should have Vaadin-Security-Key."""
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
        assert csrf is not None
        assert len(csrf) > 10


class TestInitialNodes:
    """Test initial node structure from init."""

    @pytest.fixture
    def init_changes(self):
        """Get changes from init response."""
        from vaadin.flow.server.uidl_handler import UidlHandler
        from vaadin.flow.core.state_tree import StateTree

        tree = StateTree()
        handler = UidlHandler(tree)
        response = handler.handle_init({})
        return response["appConfig"]["uidl"]["changes"]

    def test_has_body_node(self, init_changes):
        """Should create body node (node 1)."""
        body_tag = next(
            (c for c in init_changes
             if c.get("node") == 1 and c.get("key") == "tag" and c.get("value") == "body"),
            None
        )
        assert body_tag is not None, "Node 1 should have tag 'body'"

    def test_has_flow_container(self, init_changes):
        """Should create flow-container-root-* node."""
        container = next(
            (c for c in init_changes
             if c.get("key") == "tag" and "flow-container-root" in str(c.get("value", ""))),
            None
        )
        assert container is not None, "Should have flow-container-root-* node"

    def test_body_has_ui_navigate_listener(self, init_changes):
        """Body should have ui-navigate event listener."""
        listener = next(
            (c for c in init_changes
             if c.get("node") == 1 and c.get("key") == "ui-navigate" and c.get("feat") == 4),
            None
        )
        assert listener is not None, "Body should have ui-navigate listener"

    def test_push_mode_disabled(self, init_changes):
        """Push mode should be disabled."""
        push = next(
            (c for c in init_changes
             if c.get("key") == "pushMode" and c.get("value") == "DISABLED"),
            None
        )
        assert push is not None, "Push mode should be DISABLED"
