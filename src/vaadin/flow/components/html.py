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


class Div(_TextComponent):
    """HTML <div> element — supports both text content and child components."""

    _tag = "div"

    def __init__(self, text: str = ""):
        super().__init__(text)
        self._children: list[Component] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        for child in self._children:
            child._ui = self._ui
            child._parent = self
            child._attach(tree)
        if self._children:
            self.element.add_children([child.element for child in self._children])

    def add(self, *components: Component):
        """Add child components."""
        for component in components:
            self._children.append(component)
            component._parent = self
            component._ui = self._ui
            if self._element:
                component._attach(self._element._tree)
                self.element.add_child(component.element)

    def remove(self, *components: Component):
        """Remove child components."""
        for component in components:
            if component in self._children:
                self._children.remove(component)
                component._parent = None
                if self._element:
                    self.element.remove_child(component.element)
