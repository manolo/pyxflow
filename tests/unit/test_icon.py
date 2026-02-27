"""Tests for Icon component."""

import pytest

from pyflow.components.icon import Icon
from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature


class TestIcon:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        icon = Icon()
        assert icon._tag == "vaadin-icon"

    def test_auto_prefix_vaadin(self):
        icon = Icon("home")
        assert icon.get_icon() == "vaadin:home"

    def test_explicit_collection(self):
        icon = Icon("lumo:angle-right")
        assert icon.get_icon() == "lumo:angle-right"

    def test_vaadin_prefix_not_doubled(self):
        icon = Icon("vaadin:home")
        assert icon.get_icon() == "vaadin:home"

    def test_empty_icon(self):
        icon = Icon()
        assert icon.get_icon() == ""

    def test_attach_sets_attribute(self, tree):
        icon = Icon("vaadin:home")
        icon._attach(tree)

        attr = icon.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "icon")
        assert attr == "vaadin:home"

    def test_attach_no_attribute_when_empty(self, tree):
        icon = Icon()
        icon._attach(tree)

        attr = icon.element.node.get(Feature.ELEMENT_ATTRIBUTE_MAP, "icon")
        assert attr is None

    def test_set_icon_after_attach(self, tree):
        icon = Icon()
        icon._attach(tree)
        tree.collect_changes()

        icon.set_icon("check")
        changes = tree.collect_changes()
        attr_changes = [c for c in changes if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP and c.get("key") == "icon"]
        assert any(c["value"] == "vaadin:check" for c in attr_changes)

    def test_set_color(self, tree):
        icon = Icon("home")
        icon._attach(tree)
        icon.set_color("red")

        style = icon.element.node.get(Feature.INLINE_STYLE_PROPERTY_MAP, "fill")
        assert style == "red"

    def test_set_size(self, tree):
        icon = Icon("home")
        icon._attach(tree)
        icon.set_size("24px")

        w = icon.element.node.get(Feature.INLINE_STYLE_PROPERTY_MAP, "width")
        h = icon.element.node.get(Feature.INLINE_STYLE_PROPERTY_MAP, "height")
        assert w == "24px"
        assert h == "24px"
