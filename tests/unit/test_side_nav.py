"""Tests for SideNav and SideNavItem components."""

import pytest

from vaadin.flow.components.side_nav import SideNav, SideNavItem
from vaadin.flow.components.icon import Icon
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestSideNavItem:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        item = SideNavItem()
        assert item._tag == "vaadin-side-nav-item"

    def test_create_with_label(self):
        item = SideNavItem("Home")
        assert item.get_label() == "Home"

    def test_create_with_path(self):
        item = SideNavItem("Home", "/")
        assert item.get_path() == "/"

    def test_attach_creates_text_node(self, tree):
        item = SideNavItem("Home")
        item._attach(tree)

        changes = tree.collect_changes()
        text_changes = [c for c in changes if c.get("feat") == Feature.TEXT_NODE]
        assert any(c["value"] == "Home" for c in text_changes)

    def test_attach_sets_path_attribute(self, tree):
        item = SideNavItem("Home", "/")
        item._attach(tree)

        attr = item.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "path")
        assert attr == "/"

    def test_no_path_attribute_when_none(self, tree):
        item = SideNavItem("Label")
        item._attach(tree)

        attr = item.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "path")
        assert attr is None

    def test_icon_gets_prefix_slot(self, tree):
        icon = Icon("vaadin:home")
        item = SideNavItem("Home", "/", icon)
        item._attach(tree)

        slot = icon.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        assert slot == "prefix"

    def test_icon_is_child(self, tree):
        icon = Icon("vaadin:home")
        item = SideNavItem("Home", "/", icon)
        item._attach(tree)

        children = item.element.node._children
        # text node + icon
        assert len(children) == 2
        icon_tag = children[1].get(Feature.ELEMENT_DATA, "tag")
        assert icon_tag == "vaadin-icon"

    def test_nested_items_get_children_slot(self, tree):
        parent = SideNavItem("Settings")
        child1 = SideNavItem("General", "/settings/general")
        child2 = SideNavItem("Security", "/settings/security")
        parent.add_item(child1, child2)
        parent._attach(tree)

        # Children should have slot="children"
        slot1 = child1.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        slot2 = child2.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        assert slot1 == "children"
        assert slot2 == "children"

    def test_set_label_after_attach(self, tree):
        item = SideNavItem("Old")
        item._attach(tree)
        tree.collect_changes()

        item.set_label("New")
        changes = tree.collect_changes()
        text_changes = [c for c in changes if c.get("feat") == Feature.TEXT_NODE]
        assert any(c["value"] == "New" for c in text_changes)

    def test_set_path_after_attach(self, tree):
        item = SideNavItem("Home")
        item._attach(tree)
        tree.collect_changes()

        item.set_path("/home")
        changes = tree.collect_changes()
        path_changes = [c for c in changes if c.get("key") == "path" and c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP]
        assert any(c["value"] == "/home" for c in path_changes)

    def test_set_expanded(self, tree):
        item = SideNavItem("Settings")
        item._attach(tree)
        tree.collect_changes()

        item.set_expanded(True)
        changes = tree.collect_changes()
        prop_changes = [c for c in changes if c.get("key") == "expanded" and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert any(c["value"] is True for c in prop_changes)

    def test_add_item_after_attach(self, tree):
        parent = SideNavItem("Menu")
        parent._attach(tree)
        tree.collect_changes()

        child = SideNavItem("Sub", "/sub")
        parent.add_item(child)

        changes = tree.collect_changes()
        # Should have attached the child with slot="children"
        tags = [c.get("value") for c in changes if c.get("key") == "tag"]
        assert "vaadin-side-nav-item" in tags
        slot = child.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        assert slot == "children"

    def test_set_prefix_component(self, tree):
        item = SideNavItem("Home", "/")
        item._attach(tree)
        tree.collect_changes()

        icon = Icon("vaadin:cog")
        item.set_prefix_component(icon)

        slot = icon.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot")
        assert slot == "prefix"

    def test_no_text_node_when_empty(self, tree):
        item = SideNavItem()
        item._attach(tree)

        changes = tree.collect_changes()
        text_changes = [c for c in changes if c.get("feat") == Feature.TEXT_NODE]
        assert len(text_changes) == 0


class TestSideNav:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        nav = SideNav()
        assert nav._tag == "vaadin-side-nav"

    def test_attach_basic(self, tree):
        nav = SideNav()
        nav._attach(tree)

        tag = nav.element.node.get(Feature.ELEMENT_DATA, "tag")
        assert tag == "vaadin-side-nav"

    def test_label_creates_span(self, tree):
        nav = SideNav()
        nav.set_label("Menu")
        nav._attach(tree)

        changes = tree.collect_changes()
        # Find the span tag
        span_tags = [c for c in changes if c.get("key") == "tag" and c.get("value") == "span"]
        assert len(span_tags) == 1

        # Span should have slot="label"
        slot_changes = [c for c in changes if c.get("key") == "slot" and c.get("value") == "label"]
        assert len(slot_changes) >= 1

    def test_add_items(self, tree):
        nav = SideNav()
        nav.add_item(SideNavItem("A", "/a"), SideNavItem("B", "/b"))
        nav._attach(tree)

        changes = tree.collect_changes()
        item_tags = [c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-side-nav-item"]
        assert len(item_tags) == 2

    def test_add_item_after_attach(self, tree):
        nav = SideNav()
        nav._attach(tree)
        tree.collect_changes()

        nav.add_item(SideNavItem("Late", "/late"))
        changes = tree.collect_changes()
        item_tags = [c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-side-nav-item"]
        assert len(item_tags) == 1

    def test_collapsible_property(self, tree):
        nav = SideNav()
        nav.set_collapsible(True)
        nav._attach(tree)

        prop = nav.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "collapsible")
        assert prop is True

    def test_set_collapsible_after_attach(self, tree):
        nav = SideNav()
        nav._attach(tree)
        tree.collect_changes()

        nav.set_collapsible(True)
        changes = tree.collect_changes()
        prop_changes = [c for c in changes if c.get("key") == "collapsible"]
        assert any(c["value"] is True for c in prop_changes)

    def test_set_label_after_attach(self, tree):
        nav = SideNav()
        nav._attach(tree)
        tree.collect_changes()

        nav.set_label("Navigation")
        changes = tree.collect_changes()
        # Should create a span with slot="label" and text node
        span_tags = [c for c in changes if c.get("key") == "tag" and c.get("value") == "span"]
        assert len(span_tags) == 1
