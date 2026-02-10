"""Button component."""

from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.components.icon import Icon
    from vaadin.flow.core.state_tree import StateTree


class Button(Component):
    """A button component."""

    _tag = "vaadin-button"

    def __init__(self, text: str = "", icon: "Icon | None" = None):
        super().__init__()
        self._text = text
        self._icon_component: "Icon | None" = icon
        self._click_listeners: list[Callable] = []
        self._text_node = None

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._icon_component:
            self._attach_icon(tree, self._icon_component)
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

    def _attach_icon(self, tree: "StateTree", icon: "Icon"):
        """Attach an icon component as prefix child."""
        icon._ui = self._ui
        icon._parent = self
        icon._attach(tree)
        icon.element.set_attribute("slot", "prefix")
        self.element.add_child(icon.element)

    def set_icon(self, icon: "Icon"):
        """Set the button icon (prefix slot)."""
        self._icon_component = icon
        if self._element:
            self._attach_icon(self._element._tree, icon)

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
