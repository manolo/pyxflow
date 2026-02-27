"""Tests for MessageList component."""

import pytest

from pyflow.components.message_list import MessageList, MessageListItem
from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature


class TestMessageListItem:

    def test_defaults(self):
        item = MessageListItem()
        assert item.text == ""
        assert item.time is None
        assert item.user_name == ""
        assert item.user_abbr == ""
        assert item.user_img == ""
        assert item.user_color_index is None
        assert item.theme is None

    def test_constructor(self):
        item = MessageListItem("Hello", "2025-01-01T12:00:00", "Alice")
        assert item.text == "Hello"
        assert item.time == "2025-01-01T12:00:00"
        assert item.user_name == "Alice"

    def test_to_dict_full(self):
        item = MessageListItem(
            text="Hello", time="2025-01-01T12:00:00",
            user_name="Alice", user_abbr="A",
            user_img="https://example.com/img.png",
            user_color_index=3, theme="badge"
        )
        d = item.to_dict()
        assert d["text"] == "Hello"
        assert d["time"] == "2025-01-01T12:00:00"
        assert d["userName"] == "Alice"
        assert d["userAbbr"] == "A"
        assert d["userImg"] == "https://example.com/img.png"
        assert d["userColorIndex"] == 3
        assert d["theme"] == "badge"

    def test_to_dict_minimal(self):
        item = MessageListItem("Hi")
        d = item.to_dict()
        assert d == {"text": "Hi"}

    def test_to_dict_empty(self):
        item = MessageListItem()
        d = item.to_dict()
        assert d == {}

    def test_to_dict_with_time_only(self):
        item = MessageListItem(time="2025-06-15T10:30:00")
        d = item.to_dict()
        assert d == {"time": "2025-06-15T10:30:00"}

    def test_to_dict_with_user_color_index_zero(self):
        """user_color_index=0 should be included (it's not None)."""
        item = MessageListItem(user_color_index=0)
        d = item.to_dict()
        assert d == {"userColorIndex": 0}


class TestMessageList:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        ml = MessageList()
        assert ml._tag == "vaadin-message-list"

    def test_create(self):
        ml = MessageList()
        assert ml._items == []

    def test_set_items(self):
        ml = MessageList()
        items = [MessageListItem("Hello"), MessageListItem("World")]
        ml.set_items(*items)
        assert len(ml._items) == 2

    def test_get_items(self):
        ml = MessageList()
        items = [MessageListItem("Hello")]
        ml.set_items(*items)
        result = ml.get_items()
        assert len(result) == 1
        # Verify it's a copy
        result.append(MessageListItem("extra"))
        assert len(ml._items) == 1

    def test_attach_pushes_items(self, tree):
        ml = MessageList()
        ml.set_items(MessageListItem("Hello", user_name="Alice"))
        ml._attach(tree)

        changes = tree.collect_changes()
        items_changes = [
            c for c in changes
            if c.get("key") == "items" and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP
        ]
        assert len(items_changes) == 1
        items_json = items_changes[0]["value"]
        assert len(items_json) == 1
        assert items_json[0]["text"] == "Hello"
        assert items_json[0]["userName"] == "Alice"

    def test_set_items_after_attach(self, tree):
        ml = MessageList()
        ml._attach(tree)
        tree.collect_changes()

        ml.set_items(MessageListItem("New message"))
        changes = tree.collect_changes()
        items_changes = [
            c for c in changes
            if c.get("key") == "items" and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP
        ]
        assert len(items_changes) == 1
        assert len(items_changes[0]["value"]) == 1
        assert items_changes[0]["value"][0]["text"] == "New message"

    def test_empty_items(self, tree):
        ml = MessageList()
        ml._attach(tree)
        tree.collect_changes()

        ml.set_items()
        changes = tree.collect_changes()
        items_changes = [
            c for c in changes
            if c.get("key") == "items" and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP
        ]
        assert len(items_changes) == 1
        assert items_changes[0]["value"] == []

    def test_multiple_items_with_all_fields(self, tree):
        ml = MessageList()
        ml.set_items(
            MessageListItem("Hi", "2025-01-01T12:00:00", "Alice", user_abbr="A"),
            MessageListItem("Hello", "2025-01-01T12:01:00", "Bob", user_color_index=2),
        )
        ml._attach(tree)

        changes = tree.collect_changes()
        items_changes = [
            c for c in changes
            if c.get("key") == "items" and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP
        ]
        items_json = items_changes[0]["value"]
        assert len(items_json) == 2
        assert items_json[0]["userName"] == "Alice"
        assert items_json[0]["userAbbr"] == "A"
        assert items_json[1]["userName"] == "Bob"
        assert items_json[1]["userColorIndex"] == 2
