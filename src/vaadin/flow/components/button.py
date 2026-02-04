"""Button component."""

from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class Button(Component):
    """A button component."""

    _tag = "vaadin-button"

    def __init__(self, text: str = ""):
        super().__init__()
        self._text = text
        self._click_listeners: list[Callable] = []
        self._text_node = None

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._text:
            self._create_text_node(tree, self._text)
        # Register click listener
        self.element.add_event_listener("click", self._handle_click)

    def _create_text_node(self, tree: "StateTree", text: str):
        """Create text node child for button text."""
        self._text_node = tree.create_node()
        self._text_node.attach()
        self._text_node.put(Feature.TEXT_NODE, "text", text)
        # Emit clear before first splice (matches Java Flow behavior)
        self.element.node.clear_children()
        self.element.node.add_child(self._text_node)

    def set_text(self, text: str):
        """Set the button text."""
        self._text = text
        if self._text_node:
            self._text_node.put(Feature.TEXT_NODE, "text", text)

    def get_text(self) -> str:
        """Get the button text."""
        return self._text

    def add_click_listener(self, listener: Callable):
        """Add a click listener."""
        self._click_listeners.append(listener)

    def _handle_click(self, event_data: dict):
        """Handle click event."""
        for listener in self._click_listeners:
            listener(event_data)
