"""Tests for TabSheet component."""

import pytest

from pyflow.components.tabs import Tab, Tabs
from pyflow.components.tab_sheet import TabSheet
from pyflow.components.span import Span
from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature


class TestTabSheet:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create(self):
        ts = TabSheet()
        assert ts._tag == "vaadin-tabsheet"

    def test_add_with_label(self, tree):
        ts = TabSheet()
        content = Span("Content 1")
        tab = ts.add("Tab 1", content)
        assert isinstance(tab, Tab)
        assert tab.get_label() == "Tab 1"

    def test_add_with_tab_instance(self, tree):
        ts = TabSheet()
        tab = Tab("Custom Tab")
        content = Span("Content")
        result = ts.add(tab, content)
        assert result is tab

    def test_attach_creates_tabs_in_slot(self, tree):
        ts = TabSheet()
        ts.add("Tab 1", Span("Content 1"))
        ts._attach(tree)

        changes = tree.collect_changes()
        # The internal Tabs should have slot="tabs"
        slot_changes = [c for c in changes if c.get("key") == "slot" and c.get("value") == "tabs"]
        assert len(slot_changes) == 1

    def test_attach_creates_tab_children(self, tree):
        ts = TabSheet()
        ts.add("Tab 1", Span("Content 1"))
        ts.add("Tab 2", Span("Content 2"))
        ts._attach(tree)

        changes = tree.collect_changes()
        tag_changes = [c for c in changes if c.get("key") == "tag" and c.get("feat") == Feature.ELEMENT_DATA]
        tags = [c["value"] for c in tag_changes]
        assert "vaadin-tabsheet" in tags
        assert "vaadin-tabs" in tags
        assert tags.count("vaadin-tab") == 2
        assert tags.count("span") == 2

    def test_content_gets_tab_attribute(self, tree):
        ts = TabSheet()
        ts.add("Tab 1", Span("Content 1"))
        ts._attach(tree)

        changes = tree.collect_changes()
        tab_attrs = [c for c in changes if c.get("key") == "tab" and c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP]
        assert len(tab_attrs) >= 1
        # The tab attribute should be a unique ID string
        assert tab_attrs[0]["value"].startswith("tabsheet-tab-")

    def test_get_selected_tab(self, tree):
        ts = TabSheet()
        tab1 = ts.add("Tab 1", Span("C1"))
        tab2 = ts.add("Tab 2", Span("C2"))
        ts._attach(tree)

        assert ts.get_selected_tab() is tab1

    def test_set_selected_tab(self, tree):
        ts = TabSheet()
        tab1 = ts.add("Tab 1", Span("C1"))
        tab2 = ts.add("Tab 2", Span("C2"))
        ts._attach(tree)

        ts.set_selected_tab(tab2)
        assert ts.get_selected_tab() is tab2

    def test_set_selected_index(self, tree):
        ts = TabSheet()
        tab1 = ts.add("Tab 1", Span("C1"))
        tab2 = ts.add("Tab 2", Span("C2"))
        ts._attach(tree)

        ts.set_selected_index(1)
        assert ts.get_selected_index() == 1

    def test_selected_change_listener(self, tree):
        ts = TabSheet()
        ts.add("Tab 1", Span("C1"))
        ts.add("Tab 2", Span("C2"))
        ts._attach(tree)

        events = []
        ts.add_selected_change_listener(lambda e: events.append(e))

        ts.set_selected_index(1)
        assert len(events) == 1

    def test_remove_tab(self, tree):
        ts = TabSheet()
        tab1 = ts.add("Tab 1", Span("C1"))
        tab2 = ts.add("Tab 2", Span("C2"))
        ts._attach(tree)
        tree.collect_changes()

        ts.remove(tab1)
        assert tab1 not in ts._tab_to_content
        changes = tree.collect_changes()
        # Should have remove splice changes
        splice_changes = [c for c in changes if c.get("type") == "splice" and "remove" in c]
        assert len(splice_changes) >= 1
