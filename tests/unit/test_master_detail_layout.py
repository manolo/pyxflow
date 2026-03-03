"""Tests for MasterDetailLayout component."""

import pytest
from pyxflow.components import MasterDetailLayout, Span
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature


@pytest.fixture
def tree():
    return StateTree()


class TestMasterDetailLayout:
    def test_tag(self, tree):
        layout = MasterDetailLayout()
        layout._attach(tree)
        assert layout.element.node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-master-detail-layout"

    def test_empty(self, tree):
        layout = MasterDetailLayout()
        layout._attach(tree)
        assert layout.get_master() is None
        assert layout.get_detail() is None

    def test_set_master(self, tree):
        layout = MasterDetailLayout()
        master = Span("Master content")
        layout.set_master(master)
        layout._attach(tree)
        assert layout.get_master() is master
        assert master._element is not None
        assert master.element.get_attribute("slot") is None  # default slot
        assert master._parent is layout

    def test_set_detail(self, tree):
        layout = MasterDetailLayout()
        detail = Span("Detail content")
        layout.set_detail(detail)
        layout._attach(tree)
        assert layout.get_detail() is detail
        assert detail._element is not None
        assert detail._parent is layout
        # Detail is a virtual child (Feature 24), not a regular child
        assert detail.element.node.get(Feature.ELEMENT_DATA, "payload") == {"type": "inMemory"}

    def test_set_master_after_attach(self, tree):
        layout = MasterDetailLayout()
        layout._attach(tree)
        master = Span("Master")
        layout.set_master(master)
        assert master._element is not None
        assert master.element.get_attribute("slot") is None  # default slot

    def test_set_detail_after_attach(self, tree):
        layout = MasterDetailLayout()
        layout._attach(tree)
        detail = Span("Detail")
        layout.set_detail(detail)
        assert detail._element is not None
        # Virtual child — payload marks it as in-memory
        assert detail.element.node.get(Feature.ELEMENT_DATA, "payload") == {"type": "inMemory"}

    def test_replace_master(self, tree):
        layout = MasterDetailLayout()
        layout._attach(tree)
        old = Span("Old")
        layout.set_master(old)
        new = Span("New")
        layout.set_master(new)
        assert layout.get_master() is new
        assert new._element is not None

    def test_replace_detail(self, tree):
        layout = MasterDetailLayout()
        layout._attach(tree)
        old = Span("Old")
        layout.set_detail(old)
        new = Span("New")
        layout.set_detail(new)
        assert layout.get_detail() is new
        assert new._element is not None
        assert new.element.node.get(Feature.ELEMENT_DATA, "payload") == {"type": "inMemory"}

    def test_both_master_and_detail(self, tree):
        layout = MasterDetailLayout()
        master = Span("M")
        detail = Span("D")
        layout.set_master(master)
        layout.set_detail(detail)
        layout._attach(tree)
        assert master.element.get_attribute("slot") is None  # default slot
        # Master is in Feature 2 (regular child), detail is in Feature 24 (virtual child)
        assert len(layout.element.node._children) == 1  # only master

    def test_set_detail_none_hides(self, tree):
        """Setting detail to None removes the virtual child."""
        layout = MasterDetailLayout()
        layout._attach(tree)
        detail = Span("Detail")
        layout.set_detail(detail)
        assert layout.get_detail() is detail
        layout.set_detail(None)
        assert layout.get_detail() is None

    def test_set_detail_queues_execute(self, tree):
        """_setDetail() is called via execute command for animation."""
        layout = MasterDetailLayout()
        layout._attach(tree)
        tree.collect_execute()  # clear pending

        detail = Span("Detail")
        layout.set_detail(detail)
        execute = tree.collect_execute()
        # Should have a _setDetail call
        assert any("_setDetail" in str(cmd) for cmd in execute)

    def test_initial_attach_with_pre_set_detail_animates(self, tree):
        """When detail is set before attach (e.g. in before_enter), animation is enabled.

        The _attach() method re-queues _update_details() after _has_initialized=True,
        so the dedup replaces the initial skipTransition=true with skipTransition=false.
        """
        layout = MasterDetailLayout()
        detail = Span("Detail")
        layout.set_detail(detail)
        layout._attach(tree)
        execute = tree.collect_execute()
        # Find the _setDetail command
        set_detail_cmd = [cmd for cmd in execute if "_setDetail" in str(cmd)]
        assert len(set_detail_cmd) == 1
        # skipTransition is False (animate) because detail was pre-set
        assert set_detail_cmd[0][2] is False

    def test_initial_attach_without_detail_skips_transition(self, tree):
        """When no detail is pre-set, initial _setDetail(null) uses skipTransition=True."""
        layout = MasterDetailLayout()
        layout._attach(tree)
        execute = tree.collect_execute()
        set_detail_cmd = [cmd for cmd in execute if "_setDetail" in str(cmd)]
        assert len(set_detail_cmd) == 1
        # skipTransition is True (no animation) for null detail on first attach
        assert set_detail_cmd[0][1] is True

    def test_subsequent_set_detail_animates(self, tree):
        """After initial attach, _setDetail uses skipTransition=False."""
        layout = MasterDetailLayout()
        layout._attach(tree)
        tree.collect_execute()  # clear init commands

        detail = Span("Detail")
        layout.set_detail(detail)
        execute = tree.collect_execute()
        set_detail_cmd = [cmd for cmd in execute if "_setDetail" in str(cmd)]
        assert len(set_detail_cmd) == 1
        # skipTransition is the third positional arg (False = animate)
        assert set_detail_cmd[0][2] is False

    def test_set_detail_none_calls_set_detail_null(self, tree):
        """Setting detail to None sends _setDetail(null, ...) for close animation."""
        layout = MasterDetailLayout()
        layout._attach(tree)
        layout.set_detail(Span("Detail"))
        tree.collect_execute()  # clear

        layout.set_detail(None)
        execute = tree.collect_execute()
        set_detail_cmd = [cmd for cmd in execute if "_setDetail" in str(cmd)]
        assert len(set_detail_cmd) == 1
        assert "null" in set_detail_cmd[0][-1]  # script contains null

    def test_default_overlay_mode(self, tree):
        """Default overlay mode is drawer (stackOverlay=False)."""
        layout = MasterDetailLayout()
        layout._attach(tree)
        assert layout.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "stackOverlay") is False

    def test_set_animation_enabled(self, tree):
        layout = MasterDetailLayout()
        layout._attach(tree)
        assert layout.is_animation_enabled()
        layout.set_animation_enabled(False)
        assert not layout.is_animation_enabled()
        assert layout.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "noAnimation") is True

    def test_set_overlay_mode(self, tree):
        layout = MasterDetailLayout()
        layout._attach(tree)
        layout.set_overlay_mode("stack")
        assert layout.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "stackOverlay") is True
        layout.set_overlay_mode("drawer")
        assert layout.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "stackOverlay") is False

    def test_set_detail_size(self, tree):
        layout = MasterDetailLayout()
        layout.set_detail_size("400px")
        layout._attach(tree)
        assert layout.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "detailSize") == "400px"

    def test_set_master_min_size(self, tree):
        layout = MasterDetailLayout()
        layout.set_master_min_size("450px")
        layout._attach(tree)
        assert layout.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "masterMinSize") == "450px"

    def test_set_force_overlay(self, tree):
        layout = MasterDetailLayout()
        layout._attach(tree)
        layout.set_force_overlay(True)
        assert layout.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "forceOverlay") is True

    def test_duplicate_set_detail_deduplicates_execute(self, tree):
        """Multiple set_detail calls in same cycle only send one _setDetail command.

        This matches Java's pendingDetailsUpdate.cancelExecution() behavior.
        Prevents duplicate _setDetail commands from cancelling each other's
        View Transition animation.
        """
        layout = MasterDetailLayout()
        layout._attach(tree)
        layout.set_detail(Span("Detail"))
        tree.collect_execute()  # clear

        # Call set_detail(None) twice (simulates recursive event handler)
        layout.set_detail(None)
        layout.set_detail(None)
        execute = tree.collect_execute()
        set_detail_cmds = [cmd for cmd in execute if "_setDetail" in str(cmd)]
        assert len(set_detail_cmds) == 1  # only one, not two
