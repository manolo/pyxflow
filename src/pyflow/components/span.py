"""Span component."""

from typing import TYPE_CHECKING

from pyflow.core.component import Component
from pyflow.core.state_node import Feature

if TYPE_CHECKING:
    from pyflow.core.state_tree import StateTree


class Span(Component):
    """A span component for displaying text."""

    _tag = "span"

    def __init__(self, text: str = ""):
        super().__init__()
        self._text = text
        self._text_node = None

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._text:
            self._create_text_node(tree, self._text)

    def _create_text_node(self, tree: "StateTree", text: str):
        """Create a text node child."""
        self._text_node = tree.create_node()
        self._text_node.attach()
        self._text_node.put(Feature.TEXT_NODE, "text", text)
        self.element.node.add_child(self._text_node)

    def set_text(self, text: str):
        """Set the span text."""
        self._text = text
        if self._text_node:
            self._text_node.put(Feature.TEXT_NODE, "text", text)
        elif self._element:
            self._create_text_node(self._element._tree, text)

    def get_text(self) -> str:
        """Get the span text."""
        return self._text
