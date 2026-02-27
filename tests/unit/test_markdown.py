"""Tests for Markdown component."""

import pytest
from pyflow.components import Markdown
from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature


@pytest.fixture
def tree():
    return StateTree()


class TestMarkdown:
    def test_tag(self, tree):
        md = Markdown()
        md._attach(tree)
        assert md.element.node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-markdown"

    def test_content_in_constructor(self, tree):
        md = Markdown("# Hello")
        md._attach(tree)
        assert md.element.get_property("content") == "# Hello"
        assert md.get_content() == "# Hello"

    def test_set_content(self, tree):
        md = Markdown()
        md._attach(tree)
        md.set_content("**Bold text**")
        assert md.element.get_property("content") == "**Bold text**"

    def test_empty_content(self, tree):
        md = Markdown()
        md._attach(tree)
        assert md.get_content() == ""

    def test_multiline_content(self, tree):
        content = "# Title\n\nParagraph with **bold** and *italic*.\n\n- Item 1\n- Item 2"
        md = Markdown(content)
        md._attach(tree)
        assert md.element.get_property("content") == content

    def test_set_content_before_attach(self, tree):
        md = Markdown()
        md.set_content("Before attach")
        md._attach(tree)
        assert md.element.get_property("content") == "Before attach"

    def test_update_content(self, tree):
        md = Markdown("Initial")
        md._attach(tree)
        md.set_content("Updated")
        assert md.element.get_property("content") == "Updated"
        assert md.get_content() == "Updated"
