"""TextArea component."""

from typing import Callable

from vaadin.flow.core.component import Component


class TextArea(Component):
    """A multi-line text input component."""

    _tag = "vaadin-text-area"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._value = ""
        self._placeholder = ""
        self._change_listeners: list[Callable] = []

    def _attach(self, tree):
        super()._attach(tree)
        # Set properties in the order expected by Java Flow
        self.element.set_property("invalid", False)
        if self._label:
            self.element.set_property("label", self._label)
        if self._placeholder:
            self.element.set_property("placeholder", self._placeholder)
        self.element.set_property("value", self._value)
        self.element.set_property("manualValidation", True)
        self.element.add_event_listener("change", self._handle_change)

    @property
    def value(self) -> str:
        """Get the current value."""
        return self._value

    @value.setter
    def value(self, val: str):
        """Set the value."""
        self._value = val
        if self._element:
            self.element.set_property("value", val)

    def get_value(self) -> str:
        """Get the current value."""
        return self._value

    def set_value(self, value: str):
        """Set the value."""
        self.value = value

    def get_label(self) -> str:
        """Get the label."""
        return self._label

    def set_label(self, label: str):
        """Set the label."""
        self._label = label
        if self._element:
            self.element.set_property("label", label)

    def get_placeholder(self) -> str:
        """Get the placeholder text."""
        return self._placeholder

    def set_placeholder(self, placeholder: str):
        """Set the placeholder text."""
        self._placeholder = placeholder
        if self._element:
            self.element.set_property("placeholder", placeholder)

    def set_max_length(self, max_length: int):
        """Set the maximum number of characters."""
        if self._element:
            self.element.set_property("maxlength", max_length)

    def set_min_length(self, min_length: int):
        """Set the minimum number of characters."""
        if self._element:
            self.element.set_property("minlength", min_length)

    def set_min_height(self, min_height: str | None):
        """Set minimum height (e.g., '100px')."""
        if self._element and min_height:
            self.element.get_style().set("min-height", min_height)

    def set_max_height(self, max_height: str | None):
        """Set maximum height (e.g., '200px')."""
        if self._element and max_height:
            self.element.get_style().set("max-height", max_height)

    def add_value_change_listener(self, listener: Callable):
        """Add a value change listener."""
        self._change_listeners.append(listener)

    def _handle_change(self, event_data: dict):
        """Handle change event."""
        self._value = event_data.get("value", self._value)
        for listener in self._change_listeners:
            listener(event_data)

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "value":
            self._value = value
