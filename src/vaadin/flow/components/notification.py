"""Notification component."""

from enum import Enum
from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class NotificationPosition(Enum):
    """Notification display positions."""
    TOP_STRETCH = "top-stretch"
    TOP_START = "top-start"
    TOP_CENTER = "top-center"
    TOP_END = "top-end"
    MIDDLE = "middle"
    BOTTOM_START = "bottom-start"
    BOTTOM_CENTER = "bottom-center"
    BOTTOM_END = "bottom-end"
    BOTTOM_STRETCH = "bottom-stretch"


class NotificationVariant(Enum):
    """Notification theme variants."""
    LUMO_PRIMARY = "primary"
    LUMO_CONTRAST = "contrast"
    LUMO_SUCCESS = "success"
    LUMO_ERROR = "error"
    LUMO_WARNING = "warning"


class Notification(Component):
    """A notification overlay component.

    Notification is used to provide feedback to the user about activities,
    processes, or events in the application.
    """

    _tag = "vaadin-notification"

    def __init__(self, text: str = "", duration: int = 5000):
        """Create a notification.

        Args:
            text: The text content of the notification.
            duration: Duration in milliseconds. 0 means no auto-close.
        """
        super().__init__()
        self._text = text
        self._duration = duration
        self._position = NotificationPosition.BOTTOM_START
        self._opened = False
        self._theme_variants: set[str] = set()
        self._children: list[Component] = []
        self._open_listeners: list[Callable] = []
        self._close_listeners: list[Callable] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        # Set initial properties
        self.element.set_property("duration", self._duration)
        self.element.set_property("position", self._position.value)

        # Create card node for notification content
        self._card_node = tree.create_node()
        self._card_node.attach()
        self._card_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-notification-card")

        # Apply theme variants to card
        if self._theme_variants:
            self._card_node.put(Feature.ELEMENT_ATTRIBUTE_MAP, "theme",
                               " ".join(self._theme_variants))

        # Link card to notification
        self.element.node.put(Feature.VIRTUAL_CHILDREN_LIST, "0", self._card_node.id)
        tree.add_change({
            "node": self.element.node_id,
            "type": "splice",
            "feat": Feature.VIRTUAL_CHILDREN_LIST,
            "index": 0,
            "addNodes": [self._card_node.id]
        })

        # If there's text, create a text node in the card
        if self._text and not self._children:
            text_node = tree.create_node()
            text_node.attach()
            text_node.put(Feature.TEXT_NODE, "text", self._text)
            self._card_node.add_child(text_node)

        # Attach custom children to card
        for child in self._children:
            child._attach(tree)
            self._card_node.add_child(child.element.node)

        # Register opened-changed listener
        self.element.add_event_listener("opened-changed", self._handle_opened_changed)

    def open(self):
        """Open the notification."""
        self._opened = True
        if self._element:
            self.element.set_property("opened", True)

    def close(self):
        """Close the notification."""
        self._opened = False
        if self._element:
            self.element.set_property("opened", False)

    def is_opened(self) -> bool:
        """Check if the notification is open."""
        return self._opened

    def set_opened(self, opened: bool):
        """Set the opened state."""
        if opened:
            self.open()
        else:
            self.close()

    def set_text(self, text: str):
        """Set the notification text."""
        self._text = text
        if self._element and hasattr(self, "_card_node"):
            # Update or create text node
            # For simplicity, we recreate the text content
            # In a full implementation, we'd track the text node
            pass

    def get_text(self) -> str:
        """Get the notification text."""
        return self._text

    def set_duration(self, duration: int):
        """Set the duration in milliseconds.

        Args:
            duration: Duration in ms. 0 means no auto-close.
        """
        self._duration = duration
        if self._element:
            self.element.set_property("duration", duration)

    def get_duration(self) -> int:
        """Get the duration in milliseconds."""
        return self._duration

    def set_position(self, position: NotificationPosition):
        """Set the notification position."""
        self._position = position
        if self._element:
            self.element.set_property("position", position.value)

    def get_position(self) -> NotificationPosition:
        """Get the notification position."""
        return self._position

    def add_theme_variants(self, *variants: NotificationVariant):
        """Add theme variants to the notification."""
        for variant in variants:
            self._theme_variants.add(variant.value)
        if self._element and hasattr(self, "_card_node"):
            self._card_node.put(Feature.ELEMENT_ATTRIBUTE_MAP, "theme",
                               " ".join(self._theme_variants))

    def remove_theme_variants(self, *variants: NotificationVariant):
        """Remove theme variants from the notification."""
        for variant in variants:
            self._theme_variants.discard(variant.value)
        if self._element and hasattr(self, "_card_node"):
            if self._theme_variants:
                self._card_node.put(Feature.ELEMENT_ATTRIBUTE_MAP, "theme",
                                   " ".join(self._theme_variants))
            else:
                self._card_node.remove(Feature.ELEMENT_ATTRIBUTE_MAP, "theme")

    def add(self, *components: Component):
        """Add components to the notification content."""
        for component in components:
            self._children.append(component)
            if self._element and hasattr(self, "_card_node"):
                component._attach(self._element._tree)
                self._card_node.add_child(component.element.node)

    def add_open_listener(self, listener: Callable):
        """Add a listener for when the notification opens."""
        self._open_listeners.append(listener)

    def add_close_listener(self, listener: Callable):
        """Add a listener for when the notification closes."""
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

    @staticmethod
    def show(text: str, duration: int = 5000,
             position: NotificationPosition = NotificationPosition.BOTTOM_START) -> "Notification":
        """Show a simple text notification.

        This is a convenience method for quickly showing notifications.
        Note: The notification must be added to a view to work.

        Args:
            text: The text to show.
            duration: Duration in milliseconds.
            position: The position of the notification.

        Returns:
            The created Notification instance.
        """
        notification = Notification(text, duration)
        notification.set_position(position)
        notification.open()
        return notification
