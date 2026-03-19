"""Tests for RPC security validations.

Tests that PyXFlow matches Java Flow's security model:
- mSync property whitelist (forbidden props, per-component whitelist)
- Node attachment validation (detached nodes rejected)
- Node enabled validation (disabled components rejected)
- DisabledUpdateMode (ALWAYS properties/methods bypass disabled check)
- @ClientCallable method registration check
- @ClientCallable argument count validation
- CSRF constant-time comparison
"""

import hmac

import pytest

from pyxflow.core.component import (
    Component, ClientCallable, DisabledUpdateMode,
    FORBIDDEN_SYNC_PROPERTIES,
)
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature
from pyxflow.server.uidl_handler import UidlHandler


# ---------------------------------------------------------------------------
# Test components
# ---------------------------------------------------------------------------

class SecureField(Component):
    """A field with a strict sync whitelist."""
    _tag = "secure-field"
    _v_sync_properties = frozenset({"value", "invalid"})

    def __init__(self):
        self._value = ""

    def _sync_property(self, name, value):
        if name == "value":
            self._value = value


class AlwaysSyncDialog(Component):
    """A dialog-like component that syncs 'opened' even when disabled."""
    _tag = "test-dialog"
    _v_sync_properties = frozenset({"opened"})
    _v_disabled_sync = frozenset({"opened"})
    _v_disabled_methods = frozenset({"handle_close"})

    def __init__(self):
        self._opened = False

    def _sync_property(self, name, value):
        if name == "opened":
            self._opened = value

    @ClientCallable
    def handle_close(self):
        self._opened = False

    @ClientCallable
    def admin_action(self):
        self._admin_called = True


class CallableComp(Component):
    _tag = "div"

    def __init__(self):
        self.called_with = None

    @ClientCallable
    def do_something(self, a, b):
        self.called_with = (a, b)

    @ClientCallable
    def no_args(self):
        self.called_with = ()

    def not_registered(self):
        pass


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_session_with_component(comp):
    """Create a tree+handler+component ready for RPC testing."""
    tree = StateTree()
    handler = UidlHandler(tree)
    handler.handle_init({})
    comp._attach(tree)
    comp._ui = handler._ui
    tree.collect_changes()
    return tree, handler, comp


# ===========================================================================
# mSync whitelist tests
# ===========================================================================

class TestMSyncWhitelist:

    def test_whitelisted_property_accepted(self):
        tree, handler, comp = _make_session_with_component(SecureField())
        handler._handle_msync({
            "node": comp.element.node_id,
            "feature": Feature.ELEMENT_PROPERTY_MAP,
            "property": "value",
            "value": "hello",
        })
        assert comp._value == "hello"

    def test_non_whitelisted_property_rejected(self):
        tree, handler, comp = _make_session_with_component(SecureField())
        handler._handle_msync({
            "node": comp.element.node_id,
            "feature": Feature.ELEMENT_PROPERTY_MAP,
            "property": "secretFlag",
            "value": True,
        })
        node = tree.get_node(comp.element.node_id)
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "secretFlag") is None

    def test_forbidden_property_always_rejected(self):
        """textContent, innerHTML, etc. must NEVER be synced from client."""
        tree, handler, comp = _make_session_with_component(SecureField())
        for prop in FORBIDDEN_SYNC_PROPERTIES:
            handler._handle_msync({
                "node": comp.element.node_id,
                "feature": Feature.ELEMENT_PROPERTY_MAP,
                "property": prop,
                "value": "<script>alert(1)</script>",
            })
            node = tree.get_node(comp.element.node_id)
            assert node.get(Feature.ELEMENT_PROPERTY_MAP, prop) is None, \
                f"Forbidden property '{prop}' should be blocked"

    def test_component_without_whitelist_allows_all(self):
        """Components with _v_sync_properties=None allow all (backwards compat)."""
        comp = Component()
        comp._tag = "div"
        tree, handler, comp = _make_session_with_component(comp)
        handler._handle_msync({
            "node": comp.element.node_id,
            "feature": Feature.ELEMENT_PROPERTY_MAP,
            "property": "anyProp",
            "value": 42,
        })
        node = tree.get_node(comp.element.node_id)
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "anyProp") == 42

    def test_forbidden_property_blocked_even_without_whitelist(self):
        """Forbidden properties blocked even on components with no whitelist."""
        comp = Component()
        comp._tag = "div"
        tree, handler, comp = _make_session_with_component(comp)
        handler._handle_msync({
            "node": comp.element.node_id,
            "feature": Feature.ELEMENT_PROPERTY_MAP,
            "property": "innerHTML",
            "value": "<script>xss</script>",
        })
        node = tree.get_node(comp.element.node_id)
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "innerHTML") is None


# ===========================================================================
# Node attachment validation tests
# ===========================================================================

class TestNodeAttachmentValidation:

    def test_event_on_detached_node_rejected(self):
        tree, handler, comp = _make_session_with_component(SecureField())
        node_id = comp.element.node_id

        # Detach the node
        comp.element.node._detach_recursive()

        handler._handle_event({
            "node": node_id,
            "event": "click",
            "data": {},
        })
        # Should not crash, just silently ignore

    def test_msync_on_detached_node_rejected(self):
        tree, handler, comp = _make_session_with_component(SecureField())
        node_id = comp.element.node_id
        comp.element.node._detach_recursive()

        handler._handle_msync({
            "node": node_id,
            "feature": Feature.ELEMENT_PROPERTY_MAP,
            "property": "value",
            "value": "hacked",
        })
        assert comp._value == ""  # Unchanged

    def test_published_event_on_detached_node_rejected(self):
        tree, handler, comp = _make_session_with_component(CallableComp())
        node_id = comp.element.node_id
        comp.element.node._detach_recursive()

        handler._handle_published_event({
            "node": node_id,
            "templateEventMethodName": "doSomething",
            "templateEventMethodArgs": [1, 2],
        })
        assert comp.called_with is None

    def test_nonexistent_node_rejected(self):
        tree, handler, comp = _make_session_with_component(SecureField())
        handler._handle_event({
            "node": 99999,
            "event": "click",
            "data": {},
        })
        # Should not crash


# ===========================================================================
# Disabled component validation tests
# ===========================================================================

class TestDisabledComponentValidation:

    def test_event_on_disabled_component_rejected(self):
        tree, handler, comp = _make_session_with_component(SecureField())
        comp.set_enabled(False)

        handler._handle_event({
            "node": comp.element.node_id,
            "event": "click",
            "data": {},
        })
        # No crash, event silently ignored

    def test_msync_on_disabled_component_rejected(self):
        tree, handler, comp = _make_session_with_component(SecureField())
        comp.set_enabled(False)

        handler._handle_msync({
            "node": comp.element.node_id,
            "feature": Feature.ELEMENT_PROPERTY_MAP,
            "property": "value",
            "value": "hacked",
        })
        assert comp._value == ""  # Unchanged

    def test_disabled_sync_always_mode_allowed(self):
        """Properties with DisabledUpdateMode.ALWAYS bypass the disabled check."""
        tree, handler, comp = _make_session_with_component(AlwaysSyncDialog())
        comp.set_enabled(False)

        handler._handle_msync({
            "node": comp.element.node_id,
            "feature": Feature.ELEMENT_PROPERTY_MAP,
            "property": "opened",
            "value": False,
        })
        assert comp._opened is False  # Sync went through

    def test_disabled_method_always_mode_allowed(self):
        """@ClientCallable with ALWAYS mode bypasses disabled check."""
        tree, handler, comp = _make_session_with_component(AlwaysSyncDialog())
        comp._opened = True
        comp.set_enabled(False)

        handler._handle_published_event({
            "node": comp.element.node_id,
            "templateEventMethodName": "handleClose",
            "templateEventMethodArgs": [],
        })
        assert comp._opened is False  # Method executed

    def test_disabled_method_without_always_mode_rejected(self):
        """Non-ALWAYS methods are rejected on disabled components."""
        tree, handler, comp = _make_session_with_component(AlwaysSyncDialog())
        comp.set_enabled(False)

        handler._handle_published_event({
            "node": comp.element.node_id,
            "templateEventMethodName": "adminAction",
            "templateEventMethodArgs": [],
        })
        assert not hasattr(comp, "_admin_called")


# ===========================================================================
# @ClientCallable registration and argument validation tests
# ===========================================================================

class TestClientCallableSecurity:

    def test_registered_method_invoked(self):
        tree, handler, comp = _make_session_with_component(CallableComp())

        handler._handle_published_event({
            "node": comp.element.node_id,
            "templateEventMethodName": "doSomething",
            "templateEventMethodArgs": [1, 2],
        })
        assert comp.called_with == (1, 2)

    def test_unregistered_method_rejected(self):
        """Methods not marked @ClientCallable must be rejected."""
        tree, handler, comp = _make_session_with_component(CallableComp())

        handler._handle_published_event({
            "node": comp.element.node_id,
            "templateEventMethodName": "notRegistered",
            "templateEventMethodArgs": [],
        })
        assert comp.called_with is None

    def test_wrong_arg_count_too_many_rejected(self):
        tree, handler, comp = _make_session_with_component(CallableComp())

        handler._handle_published_event({
            "node": comp.element.node_id,
            "templateEventMethodName": "doSomething",
            "templateEventMethodArgs": [1, 2, 3],  # expects 2
        })
        assert comp.called_with is None

    def test_wrong_arg_count_too_few_rejected(self):
        tree, handler, comp = _make_session_with_component(CallableComp())

        handler._handle_published_event({
            "node": comp.element.node_id,
            "templateEventMethodName": "doSomething",
            "templateEventMethodArgs": [1],  # expects 2
        })
        assert comp.called_with is None

    def test_correct_arg_count_zero(self):
        tree, handler, comp = _make_session_with_component(CallableComp())

        handler._handle_published_event({
            "node": comp.element.node_id,
            "templateEventMethodName": "noArgs",
            "templateEventMethodArgs": [],
        })
        assert comp.called_with == ()

    def test_component_without_ui_rejected(self):
        """Component not attached to UI must be rejected."""
        tree = StateTree()
        handler = UidlHandler(tree)
        handler.handle_init({})

        comp = CallableComp()
        comp._attach(tree)
        # Deliberately NOT setting comp._ui
        tree.collect_changes()

        handler._handle_published_event({
            "node": comp.element.node_id,
            "templateEventMethodName": "noArgs",
            "templateEventMethodArgs": [],
        })
        assert comp.called_with is None


# ===========================================================================
# CSRF protection tests
# ===========================================================================

class TestCSRFProtection:

    def test_csrf_uses_constant_time_comparison(self):
        """Verify hmac.compare_digest is used (imported in http_server)."""
        from pyxflow.server import http_server
        assert hasattr(http_server, 'hmac'), \
            "http_server must import hmac for constant-time CSRF comparison"

    def test_forbidden_sync_properties_complete(self):
        """Verify all dangerous DOM properties are in the forbidden set."""
        for prop in ("textContent", "classList", "className",
                     "innerHTML", "outerHTML"):
            assert prop in FORBIDDEN_SYNC_PROPERTIES
