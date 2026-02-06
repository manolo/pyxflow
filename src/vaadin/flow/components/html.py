"""HTML components (headings, paragraphs, etc.)."""

from typing import TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class _TextComponent(Component):
    """Base for simple HTML text components."""

    def __init__(self, text: str = ""):
        super().__init__()
        self._text = text
        self._text_node = None

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._text:
            self._create_text_node(tree, self._text)

    def _create_text_node(self, tree: "StateTree", text: str):
        self._text_node = tree.create_node()
        self._text_node.attach()
        self._text_node.put(Feature.TEXT_NODE, "text", text)
        self.element.node.add_child(self._text_node)

    def set_text(self, text: str):
        self._text = text
        if self._text_node:
            self._text_node.put(Feature.TEXT_NODE, "text", text)

    def get_text(self) -> str:
        return self._text


class H1(_TextComponent):
    _tag = "h1"


class H2(_TextComponent):
    _tag = "h2"


class H3(_TextComponent):
    _tag = "h3"


class H4(_TextComponent):
    _tag = "h4"


class Paragraph(_TextComponent):
    _tag = "p"
