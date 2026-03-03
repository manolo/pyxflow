"""Tests for Tab and Tabs components."""

import pytest

from pyxflow.components.tabs import Tab, Tabs
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature


class TestTab:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create(self):
        tab = Tab()
        assert tab._tag == "vaadin-tab"
        assert tab.get_label() == ""

    def test_create_with_label(self):
        tab = Tab("Settings")
        assert tab.get_label() == "Settings"

    def test_attach_creates_text_node(self, tree):
        tab = Tab("Home")
        tab._attach(tree)

        changes = tree.collect_changes()
        text_changes = [c for c in changes if c.get("feat") == Feature.TEXT_NODE]
        assert any(c["value"] == "Home" for c in text_changes)

    def test_attach_no_text_node_when_empty(self, tree):
        tab = Tab()
        tab._attach(tree)

        changes = tree.collect_changes()
        text_changes = [c for c in changes if c.get("feat") == Feature.TEXT_NODE]
        assert len(text_changes) == 0

    def test_set_label_after_attach(self, tree):
        tab = Tab("Old")
        tab._attach(tree)
        tree.collect_changes()

        tab.set_label("New")
        changes = tree.collect_changes()
        text_changes = [c for c in changes if c.get("feat") == Feature.TEXT_NODE]
        assert any(c["value"] == "New" for c in text_changes)

    def test_selected_state(self):
        tab = Tab("Test")
        assert not tab.is_selected()
        tab._selected = True
        assert tab.is_selected()


class TestTabs:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_empty(self):
        tabs = Tabs()
        assert tabs._tag == "vaadin-tabs"
        assert tabs.get_selected_index() == -1
        assert tabs.get_tab_count() == 0

    def test_create_with_tabs(self):
        t1 = Tab("A")
        t2 = Tab("B")
        tabs = Tabs(t1, t2)
        assert tabs.get_tab_count() == 2
        assert tabs.get_selected_index() == 0

    def test_attach_sets_selected(self, tree):
        t1 = Tab("A")
        t2 = Tab("B")
        tabs = Tabs(t1, t2)
        tabs._attach(tree)

        changes = tree.collect_changes()
        selected = [c for c in changes if c.get("key") == "selected"]
        assert any(c["value"] == 0 for c in selected)

    def test_attach_creates_tab_children(self, tree):
        t1 = Tab("A")
        t2 = Tab("B")
        tabs = Tabs(t1, t2)
        tabs._attach(tree)

        changes = tree.collect_changes()
        tag_changes = [c for c in changes if c.get("key") == "tag" and c.get("feat") == Feature.ELEMENT_DATA]
        tags = [c["value"] for c in tag_changes]
        assert "vaadin-tabs" in tags
        assert tags.count("vaadin-tab") == 2

    def test_selected_changed_listener(self, tree):
        tabs = Tabs(Tab("A"), Tab("B"))
        tabs._attach(tree)

        changes = tree.collect_changes()
        listener_changes = [c for c in changes if c.get("feat") == Feature.ELEMENT_LISTENER_MAP]
        event_keys = [c["key"] for c in listener_changes]
        assert "selected-changed" in event_keys

    def test_feature_19_update_selected_tab(self, tree):
        tabs = Tabs(Tab("A"), Tab("B"))
        tabs._attach(tree)

        changes = tree.collect_changes()
        f19 = [c for c in changes if c.get("feat") == Feature.CLIENT_DELEGATE_HANDLERS]
        assert len(f19) == 1
        assert "updateSelectedTab" in f19[0]["add"]

    def test_set_selected_index(self, tree):
        t1 = Tab("A")
        t2 = Tab("B")
        tabs = Tabs(t1, t2)
        tabs._attach(tree)
        tree.collect_changes()

        tabs.set_selected_index(1)
        changes = tree.collect_changes()
        selected = [c for c in changes if c.get("key") == "selected"]
        assert any(c["value"] == 1 for c in selected)
        assert tabs.get_selected_tab() is t2
        assert t2.is_selected()
        assert not t1.is_selected()

    def test_set_selected_tab(self, tree):
        t1 = Tab("A")
        t2 = Tab("B")
        tabs = Tabs(t1, t2)
        tabs._attach(tree)
        tree.collect_changes()

        tabs.set_selected_tab(t2)
        assert tabs.get_selected_index() == 1

    def test_add_tabs_after_attach(self, tree):
        tabs = Tabs()
        tabs._attach(tree)
        tree.collect_changes()

        t1 = Tab("A")
        tabs.add(t1)
        changes = tree.collect_changes()

        # Should auto-select first tab
        selected = [c for c in changes if c.get("key") == "selected"]
        assert any(c["value"] == 0 for c in selected)
        assert tabs.get_selected_tab() is t1

    def test_add_tab_no_autoselect(self, tree):
        tabs = Tabs()
        tabs.set_autoselect(False)
        tabs._attach(tree)
        tree.collect_changes()

        tabs.add(Tab("A"))
        assert tabs.get_selected_index() == -1

    def test_remove_tab(self, tree):
        t1 = Tab("A")
        t2 = Tab("B")
        t3 = Tab("C")
        tabs = Tabs(t1, t2, t3)
        tabs._attach(tree)
        tree.collect_changes()

        tabs.remove(t1)
        assert tabs.get_tab_count() == 2
        # Selected index should decrease since removed tab was before it
        assert tabs.get_selected_index() == -1 or tabs.get_selected_index() == 0

    def test_selection_change_listener(self, tree):
        t1 = Tab("A")
        t2 = Tab("B")
        tabs = Tabs(t1, t2)
        tabs._attach(tree)

        events = []
        tabs.add_selected_change_listener(lambda e: events.append(e))

        tabs.set_selected_index(1)
        assert len(events) == 1
        assert events[0]["selectedIndex"] == 1
        assert events[0]["previousIndex"] == 0

    def test_set_orientation(self, tree):
        tabs = Tabs(Tab("A"))
        tabs._attach(tree)
        tree.collect_changes()

        tabs.set_orientation("vertical")
        changes = tree.collect_changes()
        orient = [c for c in changes if c.get("key") == "orientation"]
        assert any(c["value"] == "vertical" for c in orient)

    def test_sync_property_selected(self, tree):
        t1 = Tab("A")
        t2 = Tab("B")
        tabs = Tabs(t1, t2)
        tabs._attach(tree)

        events = []
        tabs.add_selected_change_listener(lambda e: events.append(e))

        tabs._sync_property("selected", 1)
        assert tabs.get_selected_index() == 1
        assert tabs.get_selected_tab() is t2
        assert len(events) == 1

    def test_update_selected_tab_client_callable(self, tree):
        t1 = Tab("A")
        t2 = Tab("B")
        tabs = Tabs(t1, t2)
        tabs._attach(tree)

        # Simulate client syncing selected property
        tabs._sync_property("selected", 1)
        events = []
        tabs.add_selected_change_listener(lambda e: events.append(e))
        tabs.update_selected_tab(True)
        # No change expected since already at 1
        assert len(events) == 0

    def test_get_selected_tab_none(self):
        tabs = Tabs()
        assert tabs.get_selected_tab() is None

    def test_registered_in_tree_components(self, tree):
        tabs = Tabs(Tab("A"))
        tabs._attach(tree)
        assert tree._components[tabs.element.node_id] is tabs
