"""Navigation Event Tests."""

import pytest

from vaadin.flow.components import VerticalLayout, Span
from vaadin.flow.router import Route, clear_routes, BeforeEnterEvent


class TestViewReuse:
    """Test that same-route-pattern navigations reuse the view instance."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        yield
        clear_routes()

    def _make_handler(self):
        from vaadin.flow.server.uidl_handler import UidlHandler
        from vaadin.flow.core.state_tree import StateTree

        tree = StateTree()
        handler = UidlHandler(tree)
        init = handler.handle_init({})
        csrf = init["appConfig"]["uidl"]["Vaadin-Security-Key"]
        return handler, tree, csrf

    def _navigate(self, handler, csrf, route, sync_id=0, client_id=0):
        payload = {
            "csrfToken": csrf,
            "rpc": [{
                "type": "event",
                "node": 1,
                "event": "ui-navigate",
                "data": {"route": route, "query": "", "appShellTitle": "",
                         "historyState": {"idx": 0}, "trigger": ""}
            }],
            "syncId": sync_id,
            "clientId": client_id,
        }
        return handler.handle_uidl(payload)

    def test_same_route_pattern_reuses_view(self):
        """Navigating within same route pattern reuses view instance."""
        @Route("test/:id?")
        class MyView(VerticalLayout):
            def __init__(self):
                self.entered = []

            def before_enter(self, event: BeforeEnterEvent):
                self.entered.append(event.get("id", None))

        handler, tree, csrf = self._make_handler()

        # First navigation to /test/1
        self._navigate(handler, csrf, "test/1", sync_id=0, client_id=0)
        view1 = handler._view
        assert view1 is not None
        assert view1.entered == ["1"]

        # Navigate to /test/2 -- same route pattern, should reuse
        self._navigate(handler, csrf, "test/2", sync_id=1, client_id=1)
        view2 = handler._view
        assert view2 is view1, "Should reuse same view instance"
        assert view1.entered == ["1", "2"]

    def test_same_route_pattern_different_params_calls_before_enter(self):
        """Reused view gets before_enter called with new params."""
        @Route("item/:id?")
        class ItemView(VerticalLayout):
            def __init__(self):
                self.last_id = None

            def before_enter(self, event: BeforeEnterEvent):
                self.last_id = event.get("id", None)

        handler, tree, csrf = self._make_handler()
        self._navigate(handler, csrf, "item/1", sync_id=0, client_id=0)
        assert handler._view.last_id == "1"

        self._navigate(handler, csrf, "item", sync_id=1, client_id=1)
        assert handler._view.last_id is None

    def test_different_view_class_creates_new_instance(self):
        """Navigating to a different view class creates a new instance."""
        @Route("view-a")
        class ViewA(VerticalLayout):
            pass

        @Route("view-b")
        class ViewB(VerticalLayout):
            pass

        handler, tree, csrf = self._make_handler()
        self._navigate(handler, csrf, "view-a", sync_id=0, client_id=0)
        view_a = handler._view
        assert isinstance(view_a, ViewA)

        self._navigate(handler, csrf, "view-b", sync_id=1, client_id=1)
        view_b = handler._view
        assert isinstance(view_b, ViewB)
        assert view_b is not view_a

    def test_reuse_preserves_component_state(self):
        """Reused view preserves component state (e.g., added children)."""
        @Route("detail/:id?")
        class DetailView(VerticalLayout):
            def __init__(self):
                self.counter = 0
                self.label = Span("init")
                self.add(self.label)

            def before_enter(self, event: BeforeEnterEvent):
                self.counter += 1
                self.label.set_text(f"visit {self.counter}")

        handler, tree, csrf = self._make_handler()
        self._navigate(handler, csrf, "detail/1", sync_id=0, client_id=0)
        view = handler._view
        assert view.counter == 1

        self._navigate(handler, csrf, "detail/2", sync_id=1, client_id=1)
        assert handler._view is view
        assert view.counter == 2  # reused, before_enter called again

    def test_same_route_string_skips_entirely(self):
        """Navigating to exact same route string is a no-op (existing behavior)."""
        @Route("static")
        class StaticView(VerticalLayout):
            def __init__(self):
                self.enter_count = 0

            def before_enter(self, event):
                self.enter_count += 1

        handler, tree, csrf = self._make_handler()
        self._navigate(handler, csrf, "static", sync_id=0, client_id=0)
        assert handler._view.enter_count == 1

        # Same route string -- skipped at line 579 (route == _current_route)
        self._navigate(handler, csrf, "static", sync_id=1, client_id=1)
        assert handler._view.enter_count == 1  # NOT called again


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
