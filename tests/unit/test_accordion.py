"""Tests for Accordion component."""

import pytest
from pyxflow.components import Accordion, AccordionPanel, Span
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature


@pytest.fixture
def tree():
    return StateTree()


class TestAccordionPanel:
    def test_extends_details(self):
        from pyxflow.components.details import Details
        panel = AccordionPanel("Title", Span("Content"))
        assert isinstance(panel, Details)

    def test_panel_tag(self, tree):
        panel = AccordionPanel("Title")
        panel._attach(tree)
        assert panel.element.node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-details"


class TestAccordion:
    def test_tag(self, tree):
        a = Accordion()
        a._attach(tree)
        assert a.element.node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-accordion"

    def test_add_panel(self, tree):
        a = Accordion()
        a._attach(tree)
        panel = a.add("Section 1", Span("Content 1"))
        assert isinstance(panel, AccordionPanel)
        assert len(a.get_panels()) == 1

    def test_add_multiple_panels(self, tree):
        a = Accordion()
        a.add("One", Span("C1"))
        a.add("Two", Span("C2"))
        a.add("Three", Span("C3"))
        a._attach(tree)
        assert len(a.get_panels()) == 3

    def test_open_panel(self, tree):
        a = Accordion()
        a.add("One", Span("C1"))
        a.add("Two", Span("C2"))
        a._attach(tree)
        a.open(1)
        assert a.get_opened_index() == 1
        assert a.element.get_property("opened") == 1

    def test_close_all(self, tree):
        a = Accordion()
        a.add("One", Span("C1"))
        a._attach(tree)
        a.open(0)
        a.close()
        assert a.get_opened_index() is None

    def test_get_opened_panel(self, tree):
        a = Accordion()
        p1 = a.add("One", Span("C1"))
        p2 = a.add("Two", Span("C2"))
        a._attach(tree)
        a.open(1)
        assert a.get_opened_panel() is p2

    def test_get_opened_panel_none(self, tree):
        a = Accordion()
        a.add("One", Span("C1"))
        a._attach(tree)
        assert a.get_opened_panel() is None

    def test_opened_change_listener(self, tree):
        a = Accordion()
        a.add("One", Span("C1"))
        a.add("Two", Span("C2"))
        a._attach(tree)
        events = []
        a.add_opened_change_listener(lambda e: events.append(e))
        a._sync_property("opened", 1)
        assert len(events) == 1
        assert events[0]["openedIndex"] == 1

    def test_sync_property_no_change(self, tree):
        a = Accordion()
        a._attach(tree)
        events = []
        a.add_opened_change_listener(lambda e: events.append(e))
        a._sync_property("opened", None)  # Already None
        assert len(events) == 0

    def test_add_panel_after_attach(self, tree):
        a = Accordion()
        a._attach(tree)
        panel = a.add("Late", Span("Late content"))
        assert panel._element is not None

    def test_panels_copy(self, tree):
        a = Accordion()
        a.add("One", Span("C1"))
        panels = a.get_panels()
        panels.clear()
        assert len(a.get_panels()) == 1
