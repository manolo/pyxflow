"""Tests for MasterDetailLayout component."""

import pytest
from vaadin.flow.components import MasterDetailLayout, Span
from vaadin.flow.components.grid import Grid
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


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
        assert detail.element.get_attribute("slot") == "detail"
        assert detail._parent is layout

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
        assert detail.element.get_attribute("slot") == "detail"

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

    def test_both_slots(self, tree):
        layout = MasterDetailLayout()
        master = Span("M")
        detail = Span("D")
        layout.set_master(master)
        layout.set_detail(detail)
        layout._attach(tree)
        assert master.element.get_attribute("slot") is None  # default slot
        assert detail.element.get_attribute("slot") == "detail"
        # Both should be children of the layout
        assert len(layout.element.node._children) == 2

    def test_set_detail_none_hides(self, tree):
        """Setting detail to None removes the detail child."""
        layout = MasterDetailLayout()
        layout._attach(tree)
        detail = Span("Detail")
        layout.set_detail(detail)
        assert layout.get_detail() is detail
        assert len(layout.element.node._children) == 1
        layout.set_detail(None)
        assert layout.get_detail() is None
        assert len(layout.element.node._children) == 0
