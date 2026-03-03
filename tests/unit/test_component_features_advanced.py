"""Tests for advanced Component features: id, helperText, focus, blur, tooltip, shortcuts."""

import pytest

from pyxflow.components import Button, TextField, Span
from pyxflow.core.keys import Key
from pyxflow.core.state_node import Feature
from pyxflow.core.state_tree import StateTree


class TestSetId:
    """Test setId / getId."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_set_id_on_attached(self, tree):
        btn = Button("Click")
        btn._attach(tree)
        tree.collect_changes()

        btn.set_id("my-button")
        assert btn.get_id() == "my-button"

        changes = tree.collect_changes()
        id_change = next(
            (c for c in changes if c.get("key") == "id" and c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP),
            None,
        )
        assert id_change is not None
        assert id_change["value"] == "my-button"

    def test_set_id_before_attach(self, tree):
        btn = Button("Click")
        btn.set_id("early-id")
        assert btn.get_id() == "early-id"

        btn._attach(tree)
        assert btn.get_id() == "early-id"

        changes = tree.collect_changes()
        id_change = next(
            (c for c in changes if c.get("key") == "id" and c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP),
            None,
        )
        assert id_change is not None
        assert id_change["value"] == "early-id"

    def test_get_id_none_by_default(self):
        btn = Button("Click")
        assert btn.get_id() is None


class TestHelperText:
    """Test setHelperText / getHelperText."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_set_helper_text_on_attached(self, tree):
        tf = TextField("Name")
        tf._attach(tree)
        tree.collect_changes()

        tf.set_helper_text("Enter your full name")
        assert tf.get_helper_text() == "Enter your full name"

        changes = tree.collect_changes()
        helper_change = next(
            (c for c in changes if c.get("key") == "helperText" and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP),
            None,
        )
        assert helper_change is not None
        assert helper_change["value"] == "Enter your full name"

    def test_set_helper_text_before_attach(self, tree):
        tf = TextField("Name")
        tf.set_helper_text("Help!")
        assert tf.get_helper_text() == "Help!"

        tf._attach(tree)
        assert tf.get_helper_text() == "Help!"

    def test_get_helper_text_empty_default(self):
        tf = TextField("Name")
        assert tf.get_helper_text() == ""


class TestFocusBlur:
    """Test focus() and blur() generate execute commands."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_focus_generates_execute(self, tree):
        btn = Button("Focus me")
        btn._attach(tree)
        tree.collect_changes()
        tree.collect_execute()

        btn.focus()
        commands = tree.collect_execute()
        assert len(commands) == 1
        cmd = commands[0]
        # Should reference the node and contain focus()
        assert {"@v-node": btn.element.node_id} in cmd
        assert "focus()" in cmd[-1]

    def test_blur_generates_execute(self, tree):
        btn = Button("Blur me")
        btn._attach(tree)
        tree.collect_changes()
        tree.collect_execute()

        btn.blur()
        commands = tree.collect_execute()
        assert len(commands) == 1
        cmd = commands[0]
        assert {"@v-node": btn.element.node_id} in cmd
        assert "blur()" in cmd[-1]

    def test_focus_noop_before_attach(self):
        btn = Button("Not attached")
        # Should not raise
        btn.focus()
        btn.blur()


class TestTooltip:
    """Test setTooltipText / getTooltipText."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_set_tooltip_creates_child(self, tree):
        btn = Button("Hover me")
        btn._attach(tree)
        tree.collect_changes()

        btn.set_tooltip_text("My tooltip")
        assert btn.get_tooltip_text() == "My tooltip"

        changes = tree.collect_changes()
        # Should have created a vaadin-tooltip child node
        tag_change = next(
            (c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-tooltip"),
            None,
        )
        assert tag_change is not None

        # Check slot attribute
        slot_change = next(
            (c for c in changes if c.get("key") == "slot" and c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP),
            None,
        )
        assert slot_change is not None
        assert slot_change["value"] == "tooltip"

        # Check text property
        text_change = next(
            (c for c in changes if c.get("key") == "text" and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP),
            None,
        )
        assert text_change is not None
        assert text_change["value"] == "My tooltip"

    def test_set_tooltip_updates_existing(self, tree):
        btn = Button("Hover me")
        btn._attach(tree)
        btn.set_tooltip_text("First")
        tree.collect_changes()

        btn.set_tooltip_text("Updated")
        assert btn.get_tooltip_text() == "Updated"

        changes = tree.collect_changes()
        # Should NOT create a new tag (reuses existing tooltip element)
        tag_changes = [c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-tooltip"]
        assert len(tag_changes) == 0

        # Should update text property
        text_change = next(
            (c for c in changes if c.get("key") == "text" and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP),
            None,
        )
        assert text_change is not None
        assert text_change["value"] == "Updated"

    def test_set_tooltip_before_attach(self, tree):
        btn = Button("Hover me")
        btn.set_tooltip_text("Deferred tooltip")
        assert btn.get_tooltip_text() == "Deferred tooltip"

        btn._attach(tree)
        assert btn.get_tooltip_text() == "Deferred tooltip"

    def test_get_tooltip_none_by_default(self):
        btn = Button("No tooltip")
        assert btn.get_tooltip_text() is None


class TestClickShortcut:
    """Test addClickShortcut."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_add_click_shortcut_registers_keydown(self, tree):
        btn = Button("Submit")
        btn._attach(tree)
        tree.collect_changes()

        btn.add_click_shortcut(Key.ENTER)
        assert btn._click_shortcut_registered is True

        changes = tree.collect_changes()
        keydown_change = next(
            (c for c in changes if c.get("key") == "keydown" and c.get("feat") == Feature.ELEMENT_LISTENER_MAP),
            None,
        )
        assert keydown_change is not None

    def test_add_click_shortcut_before_attach(self, tree):
        btn = Button("Submit")
        btn.add_click_shortcut(Key.ENTER)
        assert btn._click_shortcut_registered is True

        btn._attach(tree)
        changes = tree.collect_changes()
        keydown_change = next(
            (c for c in changes if c.get("key") == "keydown" and c.get("feat") == Feature.ELEMENT_LISTENER_MAP),
            None,
        )
        assert keydown_change is not None

    def test_click_shortcut_dispatches_click(self, tree):
        """When keydown arrives for a component with click shortcut, click listeners fire."""
        btn = Button("Submit")
        btn._attach(tree)
        btn.add_click_shortcut(Key.ENTER)

        clicked = []
        btn.add_click_listener(lambda e: clicked.append(True))

        # Simulate keydown dispatch
        from pyxflow.server.uidl_handler import UidlHandler
        handler = UidlHandler(tree)
        handler._handle_keydown(btn.element.node_id, {"event.key": "Enter"})

        assert len(clicked) == 1

    def test_duplicate_shortcut_ignored(self, tree):
        btn = Button("Submit")
        btn._attach(tree)
        btn.add_click_shortcut(Key.ENTER)
        tree.collect_changes()

        btn.add_click_shortcut(Key.ENTER)
        changes = tree.collect_changes()
        # No new keydown listener registered
        keydown_changes = [c for c in changes if c.get("key") == "keydown"]
        assert len(keydown_changes) == 0


class TestKeyEnum:
    """Test Key enum values."""

    def test_enter_value(self):
        assert Key.ENTER.value == "Enter"

    def test_escape_value(self):
        assert Key.ESCAPE.value == "Escape"

    def test_space_value(self):
        assert Key.SPACE.value == " "

    def test_tab_value(self):
        assert Key.TAB.value == "Tab"

    def test_arrow_keys(self):
        assert Key.ARROW_DOWN.value == "ArrowDown"
        assert Key.ARROW_UP.value == "ArrowUp"
        assert Key.ARROW_LEFT.value == "ArrowLeft"
        assert Key.ARROW_RIGHT.value == "ArrowRight"
