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


class HtmlContainer(_TextComponent):
    """Base for HTML container elements that support both text and child components."""

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


class Image(Component):
    """HTML <img> element with src and alt attributes."""

    _tag = "img"

    def __init__(self, src: str = "", alt: str = ""):
        super().__init__()
        self._src = src
        self._alt = alt

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._src:
            self.element.set_attribute("src", self._src)
        if self._alt:
            self.element.set_attribute("alt", self._alt)

    def set_src(self, src: str):
        self._src = src
        if self._element:
            self.element.set_attribute("src", src)

    def get_src(self) -> str:
        return self._src

    def set_alt(self, alt: str):
        self._alt = alt
        if self._element:
            self.element.set_attribute("alt", alt)

    def get_alt(self) -> str:
        return self._alt


class Div(HtmlContainer):
    """HTML <div> element — supports both text content and child components."""

    _tag = "div"


class Header(HtmlContainer):
    """HTML <header> element."""

    _tag = "header"


class Footer(HtmlContainer):
    """HTML <footer> element."""

    _tag = "footer"
