"""Tests for Popover component."""

import pytest
from pyxflow.components import Popover, PopoverPosition, Button, Span
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature


@pytest.fixture
def tree():
    return StateTree()


class TestPopover:
    def test_tag(self, tree):
        p = Popover()
        p._attach(tree)
        assert p.element.node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-popover"

    def test_defaults(self):
        p = Popover()
        assert p.is_opened() is False
        assert p.is_modal() is False
        assert p.get_position() == PopoverPosition.BOTTOM
        assert p.is_open_on_click() is True
        assert p.is_open_on_hover() is False
        assert p.is_open_on_focus() is False
        assert p.is_close_on_esc() is True
        assert p.is_close_on_outside_click() is True

    def test_open_close(self, tree):
        p = Popover()
        p._attach(tree)
        p.open()
        assert p.is_opened() is True
        p.close()
        assert p.is_opened() is False

    def test_set_opened(self, tree):
        p = Popover()
        p._attach(tree)
        p.set_opened(True)
        assert p.is_opened() is True
        p.set_opened(False)
        assert p.is_opened() is False

    def test_set_position(self, tree):
        p = Popover()
        p._attach(tree)
        p.set_position(PopoverPosition.TOP_START)
        assert p.get_position() == PopoverPosition.TOP_START
        assert p.element.get_property("position") == "top-start"

    def test_initial_position(self, tree):
        p = Popover()
        p._attach(tree)
        assert p.element.get_property("position") == "bottom"

    def test_set_modal(self, tree):
        p = Popover()
        p._attach(tree)
        p.set_modal(True)
        assert p.is_modal() is True
        assert p.element.get_property("modal") is True

    def test_set_target_queues_execute(self, tree):
        btn = Button("Target")
        btn._attach(tree)
        p = Popover()
        p.set_target(btn)
        p._attach(tree)
        # Target should be set via execute command
        execute_cmds = tree.collect_execute()
        target_cmds = [c for c in execute_cmds if "target" in c[-1]]
        assert len(target_cmds) == 1
        assert target_cmds[0][0] == {"@v-node": p.element.node_id}
        assert target_cmds[0][1] == {"@v-node": btn.element.node_id}

    def test_set_target_after_attach(self, tree):
        btn = Button("Target")
        btn._attach(tree)
        p = Popover()
        p._attach(tree)
        tree.collect_execute()  # clear pending
        p.set_target(btn)
        execute_cmds = tree.collect_execute()
        target_cmds = [c for c in execute_cmds if "target" in c[-1]]
        assert len(target_cmds) == 1

    def test_add_children(self, tree):
        p = Popover()
        s1 = Span("A")
        s2 = Span("B")
        p.add(s1, s2)
        p._attach(tree)
        assert len(p._children) == 2
        assert s1._element is not None
        assert s2._element is not None

    def test_add_children_after_attach(self, tree):
        p = Popover()
        p._attach(tree)
        s = Span("Late")
        p.add(s)
        assert s._element is not None
        assert len(p._children) == 1

    def test_children_are_regular_children(self, tree):
        p = Popover()
        s = Span("Content")
        p.add(s)
        p._attach(tree)
        # Children should be regular children (not virtual)
        assert len(p.element.node._children) == 1

    def test_trigger_property_default(self, tree):
        p = Popover()
        p._attach(tree)
        # Default: open on click only
        assert p.element.get_property("trigger") == ["click"]

    def test_trigger_property_hover_focus(self, tree):
        p = Popover()
        p._attach(tree)
        p.set_open_on_click(False)
        p.set_open_on_hover(True)
        p.set_open_on_focus(True)
        assert p.element.get_property("trigger") == ["hover", "focus"]

    def test_trigger_property_all(self, tree):
        p = Popover()
        p._attach(tree)
        p.set_open_on_hover(True)
        p.set_open_on_focus(True)
        assert p.element.get_property("trigger") == ["click", "hover", "focus"]

    def test_open_on_click(self, tree):
        p = Popover()
        p._attach(tree)
        p.set_open_on_click(False)
        assert p.is_open_on_click() is False
        assert "click" not in p.element.get_property("trigger")

    def test_open_on_hover(self, tree):
        p = Popover()
        p._attach(tree)
        p.set_open_on_hover(True)
        assert p.is_open_on_hover() is True
        assert "hover" in p.element.get_property("trigger")

    def test_open_on_focus(self, tree):
        p = Popover()
        p._attach(tree)
        p.set_open_on_focus(True)
        assert p.is_open_on_focus() is True
        assert "focus" in p.element.get_property("trigger")

    def test_close_on_esc(self, tree):
        p = Popover()
        p._attach(tree)
        p.set_close_on_esc(False)
        assert p.is_close_on_esc() is False
        assert p.element.get_property("noCloseOnEsc") is True

    def test_close_on_outside_click(self, tree):
        p = Popover()
        p._attach(tree)
        p.set_close_on_outside_click(False)
        assert p.is_close_on_outside_click() is False
        assert p.element.get_property("noCloseOnOutsideClick") is True

    def test_open_listener(self, tree):
        p = Popover()
        p._attach(tree)
        events = []
        p.add_open_listener(lambda e: events.append("open"))
        p.open()
        assert len(events) == 1

    def test_sync_property_opened(self, tree):
        p = Popover()
        p._attach(tree)
        p._sync_property("opened", True)
        assert p.is_opened() is True

    def test_sync_property_fires_open_listener(self, tree):
        p = Popover()
        p._attach(tree)
        events = []
        p.add_open_listener(lambda e: events.append("open"))
        p._sync_property("opened", True)
        assert len(events) == 1

    def test_sync_property_fires_close_listener(self, tree):
        p = Popover()
        p._attach(tree)
        p._opened = True  # simulate already open
        events = []
        p.add_close_listener(lambda e: events.append("close"))
        p._sync_property("opened", False)
        assert len(events) == 1

    def test_sync_property_no_duplicate_listener(self, tree):
        """Same value should not fire listeners."""
        p = Popover()
        p._attach(tree)
        events = []
        p.add_open_listener(lambda e: events.append("open"))
        p._sync_property("opened", False)  # already False
        assert len(events) == 0

    def test_opened_changed_is_noop(self, tree):
        """opened-changed handler is a no-op; sync is via _sync_property."""
        p = Popover()
        p._attach(tree)
        p._handle_opened_changed({})
        assert p.is_opened() is False  # no toggle

    def test_position_enum_values(self):
        assert PopoverPosition.BOTTOM.value == "bottom"
        assert PopoverPosition.BOTTOM_START.value == "bottom-start"
        assert PopoverPosition.TOP.value == "top"
        assert PopoverPosition.END.value == "end"
        assert PopoverPosition.START_BOTTOM.value == "start-bottom"

    def test_no_close_on_esc_default(self, tree):
        """By default, close on Esc is enabled (noCloseOnEsc not set)."""
        p = Popover()
        p._attach(tree)
        # noCloseOnEsc should not be set for the default
        assert p.element.get_property("noCloseOnEsc") is None

    def test_no_close_on_outside_click_default(self, tree):
        """By default, close on outside click is enabled (noCloseOnOutsideClick not set)."""
        p = Popover()
        p._attach(tree)
        assert p.element.get_property("noCloseOnOutsideClick") is None
