"""RouterLink component - navigates between routes without page reload."""

from typing import TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class RouterLink(Component):
    """An anchor tag with router-link attribute for client-side navigation.

    FlowClient intercepts clicks on elements with the 'router-link' attribute
    and sends a 'ui-navigate' event instead of a full page load.
    """

    _tag = "a"

    def __init__(self, text: str = "", href: str = ""):
        super().__init__()
        self._text = text
        self._href = href
        self._text_node = None

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._text:
            self._text_node = tree.create_node()
            self._text_node.attach()
            self._text_node.put(Feature.TEXT_NODE, "text", self._text)
            self.element.node.add_child(self._text_node)
        self.element.set_attribute("href", self._href)
        self.element.set_attribute("router-link", "")

    def set_text(self, text: str):
        """Set the link text."""
        self._text = text
        if self._text_node:
            self._text_node.put(Feature.TEXT_NODE, "text", text)

    def get_text(self) -> str:
        """Get the link text."""
        return self._text

    def set_href(self, href: str):
        """Set the link href."""
        self._href = href
        if self.element and self.element.node._attached:
            self.element.set_attribute("href", href)

    def get_href(self) -> str:
        """Get the link href."""
        return self._href
