"""Tests for StateTree and StateNode."""

import pytest

from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import StateNode, Feature


class TestStateTree:
    def test_create_node(self):
        tree = StateTree()
        node = tree.create_node()
        assert node.id == 1
        assert tree.get_node(1) is node

    def test_node_ids_increment(self):
        tree = StateTree()
        node1 = tree.create_node()
        node2 = tree.create_node()
        assert node1.id == 1
        assert node2.id == 2

    def test_collect_changes_clears(self):
        tree = StateTree()
        node = tree.create_node()
        node.attach()
        changes = tree.collect_changes()
        assert len(changes) == 1
        assert changes[0]["type"] == "attach"
        # Second collect should be empty
        assert tree.collect_changes() == []


class TestStateNode:
    def test_attach(self):
        tree = StateTree()
        node = tree.create_node()
        node.attach()
        changes = tree.collect_changes()
        assert len(changes) == 1
        assert changes[0] == {"node": 1, "type": "attach"}

    def test_put(self):
        tree = StateTree()
        node = tree.create_node()
        node.put(Feature.ELEMENT_DATA, "tag", "div")
        changes = tree.collect_changes()
        assert len(changes) == 1
        assert changes[0] == {
            "node": 1,
            "type": "put",
            "key": "tag",
            "feat": Feature.ELEMENT_DATA,
            "value": "div",
        }

    def test_get(self):
        tree = StateTree()
        node = tree.create_node()
        node.put(Feature.ELEMENT_PROPERTY_MAP, "value", "hello")
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "value") == "hello"
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "missing") is None
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "missing", "default") == "default"

    def test_add_child(self):
        tree = StateTree()
        parent = tree.create_node()
        child = tree.create_node()
        tree.collect_changes()  # Clear
        parent.add_child(child)
        changes = tree.collect_changes()
        assert len(changes) == 1
        assert changes[0]["type"] == "splice"
        assert changes[0]["addNodes"] == [child.id]
