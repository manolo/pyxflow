"""Dialog component."""

from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class Dialog(Component):
    """A dialog overlay component.

    Dialog is a small window that can be used to present information
    and user interface elements in an overlay.

    The dialog content is rendered using FlowComponentHost which requires
    the flow-component-renderer.js to be in the bundle.
    """

    _tag = "vaadin-dialog"

    def __init__(self):
        super().__init__()
        self._opened = False
        self._modal = True
        self._draggable = False
        self._resizable = False
        self._header_title = ""
        self._width = None
        self._height = None
        self._children: list[Component] = []
        self._open_listeners: list[Callable] = []
        self._close_listeners: list[Callable] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        # Set initial properties
        self.element.set_property("modeless", not self._modal)
        self.element.set_property("draggable", self._draggable)
        self.element.set_property("resizable", self._resizable)
        if self._header_title:
            self.element.set_property("headerTitle", self._header_title)
        if self._width:
            self.element.get_style().set("--vaadin-dialog-overlay-width", self._width)
        if self._height:
            self.element.get_style().set("--vaadin-dialog-overlay-height", self._height)

        # Attach children as regular children of the dialog element
        # (not virtual children - the renderer handles placing them in the overlay)
        for child in self._children:
            child._attach(tree)
            self.element.node.add_child(child.element.node)

        # Update virtualChildNodeIds property
        self._update_virtual_child_node_ids()

        # Register opened-changed listener
        self.element.add_event_listener("opened-changed", self._handle_opened_changed)

    def _update_virtual_child_node_ids(self):
        """Update the virtualChildNodeIds property with child node IDs."""
        if not self._element:
            return
        child_ids = [child.element.node_id for child in self._children if child._element]
        self.element.set_property("virtualChildNodeIds", child_ids)

    def add(self, *components: Component):
        """Add components to the dialog content."""
        for component in components:
            self._children.append(component)
            if self._element:
                component._attach(self._element._tree)
                self.element.node.add_child(component.element.node)
                self._update_virtual_child_node_ids()

    def open(self):
        """Open the dialog."""
        self._opened = True
        if self._element:
            self.element.set_property("opened", True)

    def close(self):
        """Close the dialog."""
        self._opened = False
        if self._element:
            self.element.set_property("opened", False)

    def is_opened(self) -> bool:
        """Check if the dialog is open."""
        return self._opened

    def set_opened(self, opened: bool):
        """Set the opened state."""
        if opened:
            self.open()
        else:
            self.close()

    def set_modal(self, modal: bool):
        """Set whether the dialog is modal."""
        self._modal = modal
        if self._element:
            self.element.set_property("modeless", not modal)

    def is_modal(self) -> bool:
        """Check if the dialog is modal."""
        return self._modal

    def set_draggable(self, draggable: bool):
        """Set whether the dialog can be dragged."""
        self._draggable = draggable
        if self._element:
            self.element.set_property("draggable", draggable)

    def is_draggable(self) -> bool:
        """Check if the dialog is draggable."""
        return self._draggable

    def set_resizable(self, resizable: bool):
        """Set whether the dialog can be resized."""
        self._resizable = resizable
        if self._element:
            self.element.set_property("resizable", resizable)

    def is_resizable(self) -> bool:
        """Check if the dialog is resizable."""
        return self._resizable

    def set_header_title(self, title: str):
        """Set the dialog header title."""
        self._header_title = title
        if self._element:
            self.element.set_property("headerTitle", title)

    def get_header_title(self) -> str:
        """Get the dialog header title."""
        return self._header_title

    def set_width(self, width: str):
        """Set the dialog width (e.g., '400px', '50%')."""
        self._width = width
        if self._element:
            self.element.get_style().set("--vaadin-dialog-overlay-width", width)

    def set_height(self, height: str):
        """Set the dialog height (e.g., '300px', '50%')."""
        self._height = height
        if self._element:
            self.element.get_style().set("--vaadin-dialog-overlay-height", height)

    def add_open_listener(self, listener: Callable):
        """Add a listener for when the dialog opens."""
        self._open_listeners.append(listener)

    def add_close_listener(self, listener: Callable):
        """Add a listener for when the dialog closes."""
        self._close_listeners.append(listener)

    def _handle_opened_changed(self, event_data: dict):
        """Handle opened-changed event from client."""
        opened = event_data.get("opened", self._opened)
        was_opened = self._opened
        self._opened = opened

        if opened and not was_opened:
            for listener in self._open_listeners:
                listener(event_data)
        elif not opened and was_opened:
            for listener in self._close_listeners:
                listener(event_data)

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "opened":
            self._opened = value
