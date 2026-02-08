"""Tests for RouterLayout integration — layout chain, reuse, and backward compatibility."""

import pytest

from vaadin.flow.components.app_layout import AppLayout
from vaadin.flow.components.html import Div, H1
from vaadin.flow.components.side_nav import SideNav, SideNavItem
from vaadin.flow.components.drawer_toggle import DrawerToggle
from vaadin.flow.components.vertical_layout import VerticalLayout
from vaadin.flow.components.span import Span
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature
from vaadin.flow.router import Route, clear_routes, match_route
from vaadin.flow.server.uidl_handler import UidlHandler


class TestRouteLayoutParam:
    """Test @Route(layout=...) parameter."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        yield
        clear_routes()

    def test_route_stores_layout(self):
        """@Route should store layout class in route registry."""
        class MyLayout(AppLayout):
            pass

        @Route("test", layout=MyLayout)
        class TestView(VerticalLayout):
            pass

        result = match_route("test")
        assert result is not None
        cls, title, params, layout_cls = result
        assert cls == TestView
        assert layout_cls == MyLayout

    def test_route_no_layout(self):
        """@Route without layout should store None."""
        @Route("plain")
        class PlainView(VerticalLayout):
            pass

        result = match_route("plain")
        assert result is not None
        cls, title, params, layout_cls = result
        assert layout_cls is None

    def test_route_layout_on_class(self):
        """Layout should be retrievable for any route."""
        class SharedLayout(AppLayout):
            pass

        @Route("a", layout=SharedLayout)
        class ViewA(VerticalLayout):
            pass

        @Route("b", layout=SharedLayout)
        class ViewB(VerticalLayout):
            pass

        _, _, _, layout_a = match_route("a")
        _, _, _, layout_b = match_route("b")
        assert layout_a is SharedLayout
        assert layout_b is SharedLayout


class TestRouterLayoutNavigation:
    """Test layout chain in navigation."""

    @pytest.fixture(autouse=True)
    def setup(self):
        clear_routes()
        yield
        clear_routes()

    def _make_session(self):
        tree = StateTree()
        handler = UidlHandler(tree)
        init_response = handler.handle_init({})
        csrf = init_response["appConfig"]["uidl"]["Vaadin-Security-Key"]
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

    def test_layout_created_on_first_navigation(self):
        """First navigation to a layout route should create the layout."""
        class TestLayout(AppLayout):
            pass

        @Route("home", layout=TestLayout)
        class HomeView(VerticalLayout):
            pass

        handler, tree, csrf = self._make_session()
        r1 = self._navigate(handler, csrf, "home")

        tags = [c.get("value") for c in r1.get("changes", []) if c.get("key") == "tag"]
        assert "vaadin-app-layout" in tags
        assert "vaadin-vertical-layout" in tags
        assert handler._layout is not None
        assert isinstance(handler._layout, TestLayout)

    def test_layout_reused_on_same_layout_navigation(self):
        """Navigating between views with the same layout should reuse the layout."""
        class SharedLayout(AppLayout):
            pass

        @Route("v1", layout=SharedLayout)
        class View1(VerticalLayout):
            def __init__(self):
                super().__init__()
                self.add(Span("View 1"))

        @Route("v2", layout=SharedLayout)
        class View2(VerticalLayout):
            def __init__(self):
                super().__init__()
                self.add(Span("View 2"))

        handler, tree, csrf = self._make_session()
        r1 = self._navigate(handler, csrf, "v1")
        layout_instance = handler._layout

        # Navigate to v2 with same layout
        r2 = self._navigate(handler, csrf, "v2", sync_id=r1["syncId"], client_id=1)

        # Layout should be reused (same instance)
        assert handler._layout is layout_instance

        # Should NOT create a new app-layout tag
        tags2 = [c.get("value") for c in r2.get("changes", []) if c.get("key") == "tag"]
        assert "vaadin-app-layout" not in tags2, "Layout should be reused, not recreated"

        # Should create the new view
        assert "vaadin-vertical-layout" in tags2

    def test_layout_replaced_when_different(self):
        """Navigating to a different layout should replace the layout."""
        class Layout1(AppLayout):
            pass

        class Layout2(AppLayout):
            pass

        @Route("l1", layout=Layout1)
        class ViewL1(VerticalLayout):
            pass

        @Route("l2", layout=Layout2)
        class ViewL2(VerticalLayout):
            pass

        handler, tree, csrf = self._make_session()
        r1 = self._navigate(handler, csrf, "l1")
        old_layout = handler._layout

        r2 = self._navigate(handler, csrf, "l2", sync_id=r1["syncId"], client_id=1)

        assert handler._layout is not old_layout
        assert isinstance(handler._layout, Layout2)

    def test_no_layout_backward_compat(self):
        """Routes without layout should work as before (view directly in container)."""
        @Route("plain")
        class PlainView(VerticalLayout):
            def __init__(self):
                super().__init__()
                self.add(Span("Plain"))

        handler, tree, csrf = self._make_session()
        r1 = self._navigate(handler, csrf, "plain")

        tags = [c.get("value") for c in r1.get("changes", []) if c.get("key") == "tag"]
        assert "vaadin-vertical-layout" in tags
        assert "vaadin-app-layout" not in tags
        assert handler._layout is None

    def test_layout_to_no_layout(self):
        """Navigating from layout route to no-layout route should remove layout."""
        class TestLayout(AppLayout):
            pass

        @Route("with-layout", layout=TestLayout)
        class LayoutView(VerticalLayout):
            pass

        @Route("no-layout")
        class NoLayoutView(VerticalLayout):
            pass

        handler, tree, csrf = self._make_session()
        r1 = self._navigate(handler, csrf, "with-layout")
        assert handler._layout is not None

        r2 = self._navigate(handler, csrf, "no-layout", sync_id=r1["syncId"], client_id=1)
        assert handler._layout is None

    def test_no_layout_to_layout(self):
        """Navigating from no-layout to layout route should create layout."""
        class TestLayout(AppLayout):
            pass

        @Route("plain")
        class PlainView(VerticalLayout):
            pass

        @Route("fancy", layout=TestLayout)
        class FancyView(VerticalLayout):
            pass

        handler, tree, csrf = self._make_session()
        r1 = self._navigate(handler, csrf, "plain")
        assert handler._layout is None

        r2 = self._navigate(handler, csrf, "fancy", sync_id=r1["syncId"], client_id=1)
        assert handler._layout is not None
        assert isinstance(handler._layout, TestLayout)

    def test_page_title_with_layout(self):
        """Page title should still work with layout routes."""
        class TestLayout(AppLayout):
            pass

        @Route("titled", page_title="My Title", layout=TestLayout)
        class TitledView(VerticalLayout):
            pass

        handler, tree, csrf = self._make_session()
        r1 = self._navigate(handler, csrf, "titled")

        title_cmd = next(
            (cmd for cmd in r1.get("execute", []) if "document.title" in str(cmd)), None
        )
        assert title_cmd is not None
        assert title_cmd[0] == "My Title"

    def test_server_connected_with_layout(self):
        """serverConnected should be sent even with layout routes."""
        class TestLayout(AppLayout):
            pass

        @Route("sc", layout=TestLayout)
        class SCView(VerticalLayout):
            pass

        handler, tree, csrf = self._make_session()
        r1 = self._navigate(handler, csrf, "sc")

        has_sc = any("serverConnected" in str(cmd) for cmd in r1.get("execute", []))
        assert has_sc

    def test_before_leave_with_layout(self):
        """before_leave should work with layout routes."""
        class TestLayout(AppLayout):
            pass

        @Route("stay", layout=TestLayout)
        class StayView(VerticalLayout):
            def before_leave(self):
                return False

        @Route("go", layout=TestLayout)
        class GoView(VerticalLayout):
            pass

        handler, tree, csrf = self._make_session()
        r1 = self._navigate(handler, csrf, "stay")

        r2 = self._navigate(handler, csrf, "go", sync_id=r1["syncId"], client_id=1)
        tags2 = [c.get("value") for c in r2.get("changes", []) if c.get("key") == "tag"]
        assert len(tags2) == 0, "Navigation should be cancelled by before_leave"

    def test_after_navigation_with_layout(self):
        """after_navigation should be called with layout routes."""
        called = []

        class TestLayout(AppLayout):
            pass

        @Route("after", layout=TestLayout)
        class AfterView(VerticalLayout):
            def after_navigation(self):
                called.append(True)

        handler, tree, csrf = self._make_session()
        self._navigate(handler, csrf, "after")
        assert len(called) == 1

    def test_set_parameter_with_layout(self):
        """set_parameter should work with layout routes."""
        received = {}

        class TestLayout(AppLayout):
            pass

        @Route("item/:id", layout=TestLayout)
        class ItemView(VerticalLayout):
            def set_parameter(self, params):
                received.update(params)

        handler, tree, csrf = self._make_session()
        self._navigate(handler, csrf, "item/42")
        assert received == {"id": "42"}

    def test_layout_navbar_persists(self):
        """Navbar components should persist across navigation within same layout."""
        class NavLayout(AppLayout):
            def __init__(self):
                super().__init__()
                self.add_to_navbar(DrawerToggle(), H1("App"))

        @Route("n1", layout=NavLayout)
        class Nav1(VerticalLayout):
            pass

        @Route("n2", layout=NavLayout)
        class Nav2(VerticalLayout):
            pass

        handler, tree, csrf = self._make_session()
        r1 = self._navigate(handler, csrf, "n1")

        # Get navbar node count
        layout = handler._layout
        navbar_count = len(layout._navbar_components)

        r2 = self._navigate(handler, csrf, "n2", sync_id=r1["syncId"], client_id=1)

        # Navbar should still have same components
        assert len(handler._layout._navbar_components) == navbar_count

    def test_content_not_slotted(self):
        """Content set via router should NOT have a slot attribute."""
        class TestLayout(AppLayout):
            pass

        @Route("check", layout=TestLayout)
        class CheckView(VerticalLayout):
            pass

        handler, tree, csrf = self._make_session()
        self._navigate(handler, csrf, "check")

        view = handler._view
        slot = view.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        assert slot is None, "Content children must NOT have slot attribute"

    def test_first_nav_is_first_when_layout(self):
        """First navigation with layout should be treated as first navigation (keydown listener)."""
        class TestLayout(AppLayout):
            pass

        @Route("first", layout=TestLayout)
        class FirstView(VerticalLayout):
            pass

        handler, tree, csrf = self._make_session()
        r1 = self._navigate(handler, csrf, "first")

        # Should have keydown listener on body (first navigation)
        changes = r1.get("changes", [])
        keydown = [c for c in changes if c.get("key") == "keydown" and c.get("feat") == Feature.ELEMENT_LISTENER_MAP]
        assert len(keydown) > 0, "First navigation should register keydown on body"

    def test_second_nav_not_first(self):
        """Second navigation within same layout should NOT be first navigation."""
        class TestLayout(AppLayout):
            pass

        @Route("s1", layout=TestLayout)
        class S1View(VerticalLayout):
            pass

        @Route("s2", layout=TestLayout)
        class S2View(VerticalLayout):
            pass

        handler, tree, csrf = self._make_session()
        r1 = self._navigate(handler, csrf, "s1")

        r2 = self._navigate(handler, csrf, "s2", sync_id=r1["syncId"], client_id=1)

        # Should NOT have keydown listener (not first navigation)
        changes2 = r2.get("changes", [])
        keydown2 = [c for c in changes2 if c.get("key") == "keydown" and c.get("feat") == Feature.ELEMENT_LISTENER_MAP]
        assert len(keydown2) == 0, "Second navigation should NOT register keydown on body"
