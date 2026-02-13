"""Tests for MessageInput component."""

import pytest

from vaadin.flow.components.message_input import MessageInput
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestMessageInput:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        mi = MessageInput()
        assert mi._tag == "vaadin-message-input"

    def test_create(self):
        mi = MessageInput()
        assert mi._submit_listeners == []

    def test_attach(self, tree):
        mi = MessageInput()
        mi._attach(tree)
        assert mi._element is not None

    def test_attach_registers_submit_listener(self, tree):
        mi = MessageInput()
        mi._attach(tree)
        assert "submit" in mi.element._listeners

    def test_attach_submit_event_in_changes(self, tree):
        mi = MessageInput()
        mi._attach(tree)
        changes = tree.collect_changes()
        listener_changes = [
            c for c in changes
            if c.get("key") == "submit" and c.get("feat") == Feature.ELEMENT_LISTENER_MAP
        ]
        assert len(listener_changes) == 1

    def test_add_submit_listener(self):
        mi = MessageInput()
        events = []
        mi.add_submit_listener(lambda e: events.append(e))
        assert len(mi._submit_listeners) == 1

    def test_submit_event_fires_listener(self, tree):
        mi = MessageInput()
        mi._attach(tree)
        events = []
        mi.add_submit_listener(lambda e: events.append(e))
        mi._on_submit({"event.detail.value": "Hello world"})
        assert len(events) == 1
        assert events[0]["value"] == "Hello world"

    def test_submit_event_empty_value(self, tree):
        mi = MessageInput()
        mi._attach(tree)
        events = []
        mi.add_submit_listener(lambda e: events.append(e))
        mi._on_submit({})
        assert len(events) == 1
        assert events[0]["value"] == ""

    def test_multiple_submit_listeners(self):
        mi = MessageInput()
        results = []
        mi.add_submit_listener(lambda e: results.append("a"))
        mi.add_submit_listener(lambda e: results.append("b"))
        mi._on_submit({"event.detail.value": "test"})
        assert results == ["a", "b"]

    def test_enabled(self, tree):
        mi = MessageInput()
        mi._attach(tree)
        tree.collect_changes()

        mi.set_enabled(False)
        changes = tree.collect_changes()
        disabled_changes = [
            c for c in changes
            if c.get("key") == "disabled" and c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
        ]
        assert len(disabled_changes) == 1

    def test_set_enabled_true_removes_disabled(self, tree):
        mi = MessageInput()
        mi._attach(tree)
        mi.set_enabled(False)
        tree.collect_changes()

        mi.set_enabled(True)
        changes = tree.collect_changes()
        removed = [c for c in changes if c.get("type") == "remove" and c.get("key") == "disabled"]
        assert len(removed) == 1
