"""RadioButtonGroup component."""

from typing import Callable, Generic, TypeVar, Optional

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasValidation, HasRequired
from vaadin.flow.core.state_node import Feature

T = TypeVar('T')


class RadioButtonGroup(HasValidation, HasRequired, Component, Generic[T]):
    """A radio button group component.

    Allows users to select one value among multiple choices.
    """

    _v_fqcn = "com.vaadin.flow.component.radiobutton.RadioButtonGroup"
    _tag = "vaadin-radio-group"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._items: list[T] = []
        self._value: Optional[T] = None
        self._item_label_generator: Optional[Callable[[T], str]] = None
        self._change_listeners: list[Callable] = []
        self._radio_buttons: list = []

    def _attach(self, tree):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)

        # Create radio buttons for items
        self._create_radio_buttons(tree)

        # Register value change listener
        self.element.add_event_listener("value-changed", self._handle_value_changed)

    def _create_radio_buttons(self, tree):
        """Create radio button elements for each item."""
        if not self._items:
            return

        for i, item in enumerate(self._items):
            # Create vaadin-radio-button element
            radio_node = tree.create_node()
            radio_node.attach()
            radio_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-radio-button")

            label = self._get_item_label(item)
            radio_node.put(Feature.ELEMENT_PROPERTY_MAP, "label", label)
            radio_node.put(Feature.ELEMENT_PROPERTY_MAP, "value", label)

            # Check if this is the selected value
            if self._value is not None and item == self._value:
                radio_node.put(Feature.ELEMENT_PROPERTY_MAP, "checked", True)

            # Add radio button to group
            self.element.node.add_child(radio_node)
            self._radio_buttons.append(radio_node)

    def _get_item_label(self, item: T) -> str:
        """Get the label for an item."""
        if self._item_label_generator:
            return self._item_label_generator(item)
        return str(item)

    def set_items(self, *items: T):
        """Set the items for the radio button group."""
        self._items = list(items)
        if self._element and self._element._tree:
            self._create_radio_buttons(self._element._tree)

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
            old_value = self._value
            # Find the item that matches this label
            self._value = None
            for item in self._items:
                if self._get_item_label(item) == value:
                    self._value = item
                    break
            # Fire change listeners
            if self._value != old_value:
                for listener in self._change_listeners:
                    listener({"value": self._value})
