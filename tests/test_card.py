"""Tests for Card component."""

import pytest
from vaadin.flow.components import Card, Span, Button
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


@pytest.fixture
def tree():
    return StateTree()


class TestCard:
    def test_tag(self, tree):
        c = Card()
        c._attach(tree)
        assert c.element.node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-card"

    def test_default_slot_children(self, tree):
        content = Span("Content")
        c = Card(content)
        c._attach(tree)
        assert content._element is not None
        assert content._parent is c

    def test_add_after_attach(self, tree):
        c = Card()
        c._attach(tree)
        child = Span("Added")
        c.add(child)
        assert child._element is not None
        assert child._parent is c

    def test_set_title_string(self, tree):
        c = Card()
        c.set_title("My Title")
        c._attach(tree)
        # Title creates a Div with slot="title"
        title_nodes = [
            n for n in c.element.node._children
            if n.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot") == "title"
        ]
        assert len(title_nodes) == 1

    def test_set_title_component(self, tree):
        title = Span("Custom Title")
        c = Card()
        c.set_title(title)
        c._attach(tree)
        assert title._element is not None
        assert title.element.get_attribute("slot") == "title"

    def test_set_subtitle_string(self, tree):
        c = Card()
        c.set_subtitle("Sub")
        c._attach(tree)
        sub_nodes = [
            n for n in c.element.node._children
            if n.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot") == "subtitle"
        ]
        assert len(sub_nodes) == 1

    def test_set_subtitle_component(self, tree):
        sub = Span("Custom Sub")
        c = Card()
        c.set_subtitle(sub)
        c._attach(tree)
        assert sub._element is not None
        assert sub.element.get_attribute("slot") == "subtitle"

    def test_set_media(self, tree):
        media = Span("Image placeholder")
        c = Card()
        c.set_media(media)
        c._attach(tree)
        assert media.element.get_attribute("slot") == "media"

    def test_set_header(self, tree):
        header = Span("Header")
        c = Card()
        c.set_header(header)
        c._attach(tree)
        assert header.element.get_attribute("slot") == "header"

    def test_set_header_prefix(self, tree):
        prefix = Span("Prefix")
        c = Card()
        c.set_header_prefix(prefix)
        c._attach(tree)
        assert prefix.element.get_attribute("slot") == "header-prefix"

    def test_set_header_suffix(self, tree):
        suffix = Span("Suffix")
        c = Card()
        c.set_header_suffix(suffix)
        c._attach(tree)
        assert suffix.element.get_attribute("slot") == "header-suffix"

    def test_add_to_footer(self, tree):
        btn = Button("Action")
        c = Card()
        c.add_to_footer(btn)
        c._attach(tree)
        assert btn.element.get_attribute("slot") == "footer"

    def test_multiple_footer(self, tree):
        btn1 = Button("Save")
        btn2 = Button("Cancel")
        c = Card()
        c.add_to_footer(btn1, btn2)
        c._attach(tree)
        assert btn1.element.get_attribute("slot") == "footer"
        assert btn2.element.get_attribute("slot") == "footer"

    def test_all_slots(self, tree):
        c = Card()
        c.set_title("Title")
        c.set_subtitle("Subtitle")
        c.set_media(Span("Media"))
        c.set_header_prefix(Span("Pre"))
        c.set_header_suffix(Span("Suf"))
        c.add(Span("Content"))
        c.add_to_footer(Button("Go"))
        c._attach(tree)
        # Count total children
        assert len(c.element.node._children) == 7

    def test_get_title(self):
        c = Card()
        assert c.get_title() is None
        c.set_title("X")
        assert c.get_title() == "X"

    def test_get_subtitle(self):
        c = Card()
        assert c.get_subtitle() is None
        c.set_subtitle("Y")
        assert c.get_subtitle() == "Y"

    def test_add_footer_after_attach(self, tree):
        c = Card()
        c._attach(tree)
        btn = Button("Late")
        c.add_to_footer(btn)
        assert btn._element is not None
        assert btn.element.get_attribute("slot") == "footer"

    def test_set_title_after_attach(self, tree):
        c = Card()
        c._attach(tree)
        c.set_title("Late Title")
        title_nodes = [
            n for n in c.element.node._children
            if n.get(Feature.ELEMENT_ATTRIBUTE_MAP, "slot") == "title"
        ]
        assert len(title_nodes) == 1
