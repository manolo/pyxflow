"""Tests for @ClientCallable decorator.

Tests that:
- Decorator marks methods correctly
- Feature 19 splice emitted on attach
- RPC dispatch calls the method with args
- Promise resolution sends return value via execute_js
- Promise rejection on exception
- camelCase → snake_case conversion
- Methods across class hierarchy (inheritance)
"""

import pytest

from pyxflow.core.component import Component, ClientCallable
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature
from pyxflow.server.uidl_handler import UidlHandler


class MyComponent(Component):
    _tag = "div"

    def __init__(self):
        self.greet_called = False
        self.greet_args = None
        self.add_called = False
        self.add_args = None

    @ClientCallable
    def greet(self, name):
        self.greet_called = True
        self.greet_args = (name,)
        return f"Hello, {name}!"

    @ClientCallable
    def add_numbers(self, a, b):
        self.add_called = True
        self.add_args = (a, b)
        return a + b

    def not_callable_from_client(self):
        pass


class ChildComponent(MyComponent):
    _tag = "span"

    @ClientCallable
    def child_method(self):
        return "from child"


class FailingComponent(Component):
    _tag = "div"

    @ClientCallable
    def failing_method(self):
        raise ValueError("test error")


class TestClientCallableDecorator:
    """Test that @ClientCallable marks methods correctly."""

    def test_decorator_sets_flag(self):
        assert getattr(MyComponent.greet, '_client_callable', False) is True

    def test_unmarked_method_has_no_flag(self):
        assert getattr(MyComponent.not_callable_from_client, '_client_callable', False) is False

    def test_decorator_preserves_function(self):
        comp = MyComponent()
        result = comp.greet("World")
        assert result == "Hello, World!"


class TestFeature19Registration:
    """Test that Feature 19 splice is emitted on attach."""

    def test_client_callable_registered_on_attach(self):
        tree = StateTree()
        comp = MyComponent()
        comp._attach(tree)

        changes = tree.collect_changes()
        feat19_splices = [
            c for c in changes
            if c.get("feat") == Feature.CLIENT_DELEGATE_HANDLERS
            and c.get("type") == "splice"
            and c.get("node") == comp.element.node_id
        ]
        assert len(feat19_splices) == 1
        splice = feat19_splices[0]
        assert "greet" in splice["add"]
        assert "add_numbers" in splice["add"]
        assert "not_callable_from_client" not in splice["add"]

    def test_inherited_methods_registered(self):
        tree = StateTree()
        comp = ChildComponent()
        comp._attach(tree)

        changes = tree.collect_changes()
        feat19_splices = [
            c for c in changes
            if c.get("feat") == Feature.CLIENT_DELEGATE_HANDLERS
            and c.get("type") == "splice"
            and c.get("node") == comp.element.node_id
        ]
        assert len(feat19_splices) == 1
        methods = feat19_splices[0]["add"]
        assert "child_method" in methods
        assert "greet" in methods
        assert "add_numbers" in methods

    def test_no_splice_when_no_client_callable(self):
        class PlainComponent(Component):
            _tag = "div"

        tree = StateTree()
        comp = PlainComponent()
        comp._attach(tree)

        changes = tree.collect_changes()
        feat19_splices = [
            c for c in changes
            if c.get("feat") == Feature.CLIENT_DELEGATE_HANDLERS
            and c.get("type") == "splice"
            and c.get("node") == comp.element.node_id
        ]
        assert len(feat19_splices) == 0


class TestRPCDispatch:
    """Test that publishedEventHandler RPCs call the right method."""

    def _setup_component(self):
        tree = StateTree()
        handler = UidlHandler(tree)
        handler.handle_init({})

        comp = MyComponent()
        comp._attach(tree)
        tree.collect_changes()  # Clear changes from attach

        return tree, handler, comp

    def test_dispatch_fire_and_forget(self):
        tree, handler, comp = self._setup_component()

        rpc = {
            "type": "publishedEventHandler",
            "node": comp.element.node_id,
            "templateEventMethodName": "greet",
            "templateEventMethodArgs": ["World"],
        }
        handler._handle_published_event(rpc)
        assert comp.greet_called
        assert comp.greet_args == ("World",)

    def test_dispatch_camel_case_to_snake_case(self):
        tree, handler, comp = self._setup_component()

        rpc = {
            "type": "publishedEventHandler",
            "node": comp.element.node_id,
            "templateEventMethodName": "addNumbers",
            "templateEventMethodArgs": [3, 4],
        }
        handler._handle_published_event(rpc)
        assert comp.add_called
        assert comp.add_args == (3, 4)

    def test_dispatch_with_multiple_args(self):
        tree, handler, comp = self._setup_component()

        rpc = {
            "type": "publishedEventHandler",
            "node": comp.element.node_id,
            "templateEventMethodName": "addNumbers",
            "templateEventMethodArgs": [10, 20],
        }
        handler._handle_published_event(rpc)
        assert comp.add_args == (10, 20)


class TestPromiseResolution:
    """Test that promise IDs trigger return value resolution."""

    def _setup_component(self, comp_class=MyComponent):
        tree = StateTree()
        handler = UidlHandler(tree)
        handler.handle_init({})

        comp = comp_class()
        comp._attach(tree)
        tree.collect_changes()  # Clear

        return tree, handler, comp

    def test_promise_resolve_sends_execute_js(self):
        tree, handler, comp = self._setup_component()

        rpc = {
            "type": "publishedEventHandler",
            "node": comp.element.node_id,
            "templateEventMethodName": "greet",
            "templateEventMethodArgs": ["Alice"],
            "promise": 42,
        }
        handler._handle_published_event(rpc)

        # element.execute_js queues execute commands via tree.queue_execute()
        execute_cmds = tree.collect_execute()
        promise_cmds = [
            cmd for cmd in execute_cmds
            if any("}p" in str(item) for item in cmd)
        ]
        assert len(promise_cmds) == 1
        cmd = promise_cmds[0]
        script = cmd[-1]  # Script is always last element
        assert "true" in script  # resolve, not reject
        assert 42 in cmd
        assert "Hello, Alice!" in cmd

    def test_promise_resolve_uses_element_ref_not_this(self):
        """Ensure promise resolution uses $0.$server (element) not this.$server.

        In execute commands, `this` is the FlowClient context object (getNode,
        $appId, registry...), NOT the element.  The element is `$0`.  Using
        `this.$server` causes TypeError because contextObject.$server is undefined.
        """
        tree, handler, comp = self._setup_component()

        rpc = {
            "type": "publishedEventHandler",
            "node": comp.element.node_id,
            "templateEventMethodName": "greet",
            "templateEventMethodArgs": ["Test"],
            "promise": 0,
        }
        handler._handle_published_event(rpc)

        execute_cmds = tree.collect_execute()
        promise_cmds = [
            cmd for cmd in execute_cmds
            if any("}p" in str(item) for item in cmd)
        ]
        assert len(promise_cmds) == 1
        script = promise_cmds[0][-1]
        # Must use $0.$server (element), never this.$server (context object)
        assert "$0.$server" in script
        assert "this.$server" not in script

    def test_promise_reject_on_exception(self):
        tree, handler, comp = self._setup_component(FailingComponent)

        rpc = {
            "type": "publishedEventHandler",
            "node": comp.element.node_id,
            "templateEventMethodName": "failingMethod",
            "templateEventMethodArgs": [],
            "promise": 7,
        }
        with pytest.raises(ValueError, match="test error"):
            handler._handle_published_event(rpc)

        # Even on exception, the rejection should have been queued
        execute_cmds = tree.collect_execute()
        promise_cmds = [
            cmd for cmd in execute_cmds
            if any("}p" in str(item) for item in cmd)
        ]
        assert len(promise_cmds) == 1
        cmd = promise_cmds[0]
        script = cmd[-1]  # Script is always last element
        assert "false" in script  # reject
        assert 7 in cmd

    def test_promise_reject_uses_element_ref_not_this(self):
        """Rejection must also use $0.$server, not this.$server."""
        tree, handler, comp = self._setup_component(FailingComponent)

        rpc = {
            "type": "publishedEventHandler",
            "node": comp.element.node_id,
            "templateEventMethodName": "failingMethod",
            "templateEventMethodArgs": [],
            "promise": 5,
        }
        with pytest.raises(ValueError):
            handler._handle_published_event(rpc)

        execute_cmds = tree.collect_execute()
        promise_cmds = [
            cmd for cmd in execute_cmds
            if any("}p" in str(item) for item in cmd)
        ]
        script = promise_cmds[0][-1]
        assert "$0.$server" in script
        assert "this.$server" not in script

    def test_promise_minus_one_is_fire_and_forget(self):
        tree, handler, comp = self._setup_component()

        rpc = {
            "type": "publishedEventHandler",
            "node": comp.element.node_id,
            "templateEventMethodName": "greet",
            "templateEventMethodArgs": ["Bob"],
            "promise": -1,
        }
        handler._handle_published_event(rpc)

        execute_cmds = tree.collect_execute()
        promise_cmds = [
            cmd for cmd in execute_cmds
            if any("}p" in str(item) for item in cmd)
        ]
        assert len(promise_cmds) == 0

    def test_no_promise_field_is_fire_and_forget(self):
        tree, handler, comp = self._setup_component()

        rpc = {
            "type": "publishedEventHandler",
            "node": comp.element.node_id,
            "templateEventMethodName": "greet",
            "templateEventMethodArgs": ["Charlie"],
        }
        handler._handle_published_event(rpc)

        execute_cmds = tree.collect_execute()
        promise_cmds = [
            cmd for cmd in execute_cmds
            if any("}p" in str(item) for item in cmd)
        ]
        assert len(promise_cmds) == 0


class TestExport:
    """Test that ClientCallable is properly exported."""

    def test_import_from_components(self):
        from pyxflow.components import ClientCallable as CC
        assert CC is ClientCallable
