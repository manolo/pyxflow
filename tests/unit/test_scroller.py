"""Tests for Scroller component."""

import pytest
from pyflow.components import Scroller, ScrollDirection, Span, VerticalLayout
from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature


@pytest.fixture
def tree():
    return StateTree()


class TestScroller:
    def test_tag(self, tree):
        s = Scroller()
        s._attach(tree)
        assert s.element.node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-scroller"

    def test_default_scroll_direction(self):
        s = Scroller()
        assert s.get_scroll_direction() == ScrollDirection.BOTH

    def test_custom_scroll_direction(self, tree):
        s = Scroller(scroll_direction=ScrollDirection.VERTICAL)
        s._attach(tree)
        assert s.get_scroll_direction() == ScrollDirection.VERTICAL
        assert s.element.get_property("scrollDirection") == "vertical"

    def test_default_direction_not_set_explicitly(self, tree):
        s = Scroller()
        s._attach(tree)
        changes = tree.collect_changes()
        dir_changes = [c for c in changes if c.get("key") == "scrollDirection"]
        assert len(dir_changes) == 0

    def test_set_scroll_direction_after_attach(self, tree):
        s = Scroller()
        s._attach(tree)
        s.set_scroll_direction(ScrollDirection.HORIZONTAL)
        assert s.element.get_property("scrollDirection") == "horizontal"

    def test_children_in_constructor(self, tree):
        child1 = Span("A")
        child2 = Span("B")
        s = Scroller(child1, child2)
        s._attach(tree)
        assert child1._element is not None
        assert child2._element is not None
        assert child1._parent is s
        assert child2._parent is s

    def test_add_after_attach(self, tree):
        s = Scroller()
        s._attach(tree)
        child = Span("Added")
        s.add(child)
        assert child._element is not None
        assert child._parent is s

    def test_set_content_replaces(self, tree):
        old = Span("Old")
        s = Scroller(old)
        s._attach(tree)
        new = Span("New")
        s.set_content(new)
        assert new._element is not None
        assert new._parent is s

    def test_scroll_direction_enum_values(self):
        assert ScrollDirection.VERTICAL.value == "vertical"
        assert ScrollDirection.HORIZONTAL.value == "horizontal"
        assert ScrollDirection.BOTH.value == "both"
        assert ScrollDirection.NONE.value == "none"

    def test_set_height_width(self, tree):
        s = Scroller()
        s.set_height("200px")
        s.set_width("300px")
        s._attach(tree)
        # Should not raise
        assert s._element is not None

    def test_add_multiple(self, tree):
        s = Scroller()
        s._attach(tree)
        s.add(Span("X"), Span("Y"))
        assert len(s._children) == 2
