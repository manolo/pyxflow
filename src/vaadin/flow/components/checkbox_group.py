"""CheckboxGroup component."""

from typing import Callable, Generic, TypeVar, Set, Optional

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasValidation, HasRequired
from vaadin.flow.core.state_node import Feature

T = TypeVar('T')


class CheckboxGroup(HasValidation, HasRequired, Component, Generic[T]):
    """A checkbox group component.

    Allows users to select multiple values from a list of options.
    """

    _tag = "vaadin-checkbox-group"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._items: list[T] = []
        self._value: Set[T] = set()
        self._item_label_generator: Optional[Callable[[T], str]] = None
        self._change_listeners: list[Callable] = []
        self._checkboxes: list = []

    def _attach(self, tree):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)

        # Create checkboxes for items
        self._create_checkboxes(tree)

        # Register value change listener
        self.element.add_event_listener("value-changed", self._handle_value_changed)

    def _create_checkboxes(self, tree):
        """Create checkbox elements for each item."""
        if not self._items:
            return

        for i, item in enumerate(self._items):
            # Create vaadin-checkbox element
            checkbox_node = tree.create_node()
            checkbox_node.attach()
            checkbox_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-checkbox")

            label = self._get_item_label(item)
            checkbox_node.put(Feature.ELEMENT_PROPERTY_MAP, "label", label)
            checkbox_node.put(Feature.ELEMENT_PROPERTY_MAP, "value", label)

            # Check if this item is in the selected values
            if item in self._value:
                checkbox_node.put(Feature.ELEMENT_PROPERTY_MAP, "checked", True)

            # Add checkbox to group
            self.element.node.add_child(checkbox_node)
            self._checkboxes.append(checkbox_node)

    def _get_item_label(self, item: T) -> str:
        """Get the label for an item."""
        if self._item_label_generator:
            return self._item_label_generator(item)
        return str(item)

    def set_items(self, *items: T):
        """Set the items for the checkbox group."""
        self._items = list(items)
        if self._element and self._element._tree:
            self._create_checkboxes(self._element._tree)

    def get_items(self) -> list[T]:
        """Get the items."""
        return self._items.copy()

    def get_value(self) -> Set[T]:
        """Get the selected values."""
        return self._value.copy()

    def set_value(self, value: Set[T]):
        """Set the selected values."""
        self._value = set(value)
        if self._element:
            # Set the value property as a list of labels
            labels = [self._get_item_label(item) for item in self._value]
            self.element.set_property("value", labels)

    def set_label(self, label: str):
        """Set the label."""
        self._label = label
        if self._element:
            self.element.set_property("label", label)

    def get_label(self) -> str:
        """Get the label."""
        return self._label

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
            old_value = self._value.copy()
            # value is a list of labels
            self._value = set()
            if isinstance(value, list):
                for value_str in value:
                    for item in self._items:
                        if self._get_item_label(item) == value_str:
                            self._value.add(item)
                            break
            # Fire change listeners
            if self._value != old_value:
                for listener in self._change_listeners:
                    listener({"value": self._value})
