"""Tests for Details component."""

import pytest
from pyxflow.components import Details, Span, VerticalLayout
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature


@pytest.fixture
def tree():
    return StateTree()


class TestDetails:
    def test_tag(self, tree):
        d = Details("Summary")
        d._attach(tree)
        assert d.element.node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-details"

    def test_opened_default_false(self, tree):
        d = Details("Summary")
        d._attach(tree)
        assert d.is_opened() is False
        assert d.element.get_property("opened") is False

    def test_set_opened(self, tree):
        d = Details("Summary")
        d.set_opened(True)
        d._attach(tree)
        assert d.is_opened() is True
        assert d.element.get_property("opened") is True

    def test_set_opened_after_attach(self, tree):
        d = Details("Summary")
        d._attach(tree)
        d.set_opened(True)
        assert d.element.get_property("opened") is True

    def test_summary_text(self, tree):
        d = Details("My Summary")
        d._attach(tree)
        # Summary text creates a <vaadin-details-summary slot="summary"> child
        children = d.element.node._children
        assert len(children) >= 1
        span_node = children[0]
        assert span_node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-details-summary"
        assert span_node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot") == "summary"
        # Text node child
        text_node = span_node._children[0]
        assert text_node.get(Feature.TEXT_NODE, "text") == "My Summary"

    def test_summary_component(self, tree):
        summary = Span("Rich summary")
        d = Details(summary)
        d._attach(tree)
        # Summary component gets slot="summary"
        children = d.element.node._children
        assert len(children) >= 1
        assert summary.element.get_attribute("slot") == "summary"

    def test_content_children(self, tree):
        content = Span("Content text")
        d = Details("Summary", content)
        d._attach(tree)
        # Content child is added (after summary span)
        assert content._element is not None
        assert content._parent is d

    def test_add_content_after_attach(self, tree):
        d = Details("Summary")
        d._attach(tree)
        extra = Span("Extra")
        d.add_content(extra)
        assert extra._element is not None
        assert extra._parent is d

    def test_multiple_content(self, tree):
        c1 = Span("One")
        c2 = Span("Two")
        d = Details("Summary", c1, c2)
        d._attach(tree)
        assert c1._element is not None
        assert c2._element is not None

    def test_get_summary_text(self):
        d = Details("Hello")
        assert d.get_summary_text() == "Hello"

    def test_get_summary_text_none_for_component(self):
        d = Details(Span("x"))
        assert d.get_summary_text() is None

    def test_opened_change_listener(self, tree):
        d = Details("Summary")
        d._attach(tree)
        events = []
        d.add_opened_change_listener(lambda e: events.append(e))
        d._sync_property("opened", True)
        assert len(events) == 1
        assert events[0]["opened"] is True

    def test_sync_property_no_change(self, tree):
        d = Details("Summary")
        d._attach(tree)
        events = []
        d.add_opened_change_listener(lambda e: events.append(e))
        d._sync_property("opened", False)  # Already false
        assert len(events) == 0

    def test_no_summary(self, tree):
        d = Details()
        d._attach(tree)
        # No summary, no error
        assert d.element is not None

    def test_enabled_disabled(self, tree):
        d = Details("Summary")
        d._attach(tree)
        d.set_enabled(False)
        assert d.element.get_attribute("disabled") == ""
        d.set_enabled(True)
        assert d.element.get_attribute("disabled") is None
