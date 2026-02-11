"""Select component."""

from typing import Callable, Generic, TypeVar, Optional

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasValidation, HasRequired
from vaadin.flow.core.state_node import Feature

T = TypeVar('T')


class Select(HasValidation, HasRequired, Component, Generic[T]):
    """A select dropdown component.

    Allows users to choose a single value from a list of options
    presented in an overlay.
    """

    _tag = "vaadin-select"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._items: list[T] = []
        self._value: Optional[T] = None
        self._placeholder = ""
        self._item_label_generator: Optional[Callable[[T], str]] = None
        self._change_listeners: list[Callable] = []
        self._list_box = None

    def _attach(self, tree):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)
        if self._placeholder:
            self.element.set_property("placeholder", self._placeholder)

        # Create the list-box for items
        self._create_list_box(tree)

        # Initialize the selectConnector (moves list-box into overlay)
        el_ref = {"@v-node": self.element.node.id}
        tree.queue_execute([
            el_ref,
            "return window.Vaadin.Flow.selectConnector.initLazy($0)"
        ])

        # Register value change listener
        self.element.add_event_listener("value-changed", self._handle_value_changed)

    def _create_list_box(self, tree):
        """Create the list-box element with items."""
        if not self._items:
            return

        # Create vaadin-select-list-box element
        list_box_node = tree.create_node()
        list_box_node.attach()
        list_box_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-select-list-box")

        # Add items to the list box
        for i, item in enumerate(self._items):
            item_node = tree.create_node()
            item_node.attach()
            item_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-select-item")

            # Create text node for the item label
            text_node = tree.create_node()
            text_node.attach()
            label = self._get_item_label(item)
            text_node.put(Feature.TEXT_NODE, "text", label)

            # Add text to item
            item_node.add_child(text_node)

            # Add item to list box
            list_box_node.add_child(item_node)

        # Add list-box as child of select
        self.element.node.add_child(list_box_node)
        self._list_box = list_box_node

        # Set selected value if any
        if self._value is not None:
            try:
                index = self._items.index(self._value)
                self.element.set_property("value", self._get_item_label(self._value))
            except ValueError:
                pass

    def _get_item_label(self, item: T) -> str:
        """Get the label for an item."""
        if self._item_label_generator:
            return self._item_label_generator(item)
        return str(item)

    def set_items(self, *items: T):
        """Set the items for the select."""
        self._items = list(items)
        if self._element and self._element._tree:
            tree = self._element._tree
            # Re-create list box with new items
            self._create_list_box(tree)
            # Tell the client to re-render the overlay content
            el_ref = {"@v-node": self.element.node.id}
            tree.queue_execute([
                el_ref,
                "return $0.requestContentUpdate()"
            ])

    def get_items(self) -> list[T]:
        """Get the items."""
        return self._items.copy()

    def get_value(self) -> Optional[T]:
        """Get the selected value."""
        return self._value

    def set_value(self, value: Optional[T]):
        """Set the selected value."""
        self._value = value
        if self._element and value is not None:
            self.element.set_property("value", self._get_item_label(value))
        elif self._element:
            self.element.set_property("value", "")

    def set_label(self, label: str):
        """Set the label."""
        self._label = label
        if self._element:
            self.element.set_property("label", label)

    def get_label(self) -> str:
        """Get the label."""
        return self._label

    def set_placeholder(self, placeholder: str):
        """Set the placeholder text."""
        self._placeholder = placeholder
        if self._element:
            self.element.set_property("placeholder", placeholder)

    def get_placeholder(self) -> str:
        """Get the placeholder text."""
        return self._placeholder

    def set_item_label_generator(self, generator: Callable[[T], str]):
        """Set a function to generate labels for items."""
        self._item_label_generator = generator

    def add_value_change_listener(self, listener: Callable):
        """Add a value change listener."""
        self._change_listeners.append(listener)

    def _handle_value_changed(self, event_data: dict):
        """Handle value-changed event from client.

        Value arrives via _sync_property (mSync), not event_data.
        This handler is a no-op — change listeners fire from _sync_property.
        """
        pass

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "value":
            old_value = self._value
            # Find the item that matches this label
            matched = None
            for item in self._items:
                if self._get_item_label(item) == value:
                    matched = item
                    break
            # If no item matched and value is empty, preserve "" (deselected)
            # to stay consistent with Binding.clear() which sets value to "".
            self._value = matched if matched is not None else (value if value == "" else None)
            # Fire change listeners
            if self._value != old_value:
                for listener in self._change_listeners:
                    listener({"value": self._value})
