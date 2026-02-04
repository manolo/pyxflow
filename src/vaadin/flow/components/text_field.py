"""TextField component."""

from typing import Callable

from vaadin.flow.core.component import Component


class TextField(Component):
    """A text field component."""

    _tag = "vaadin-text-field"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._value = ""
        self._change_listeners: list[Callable] = []

    def _attach(self, tree):
        super()._attach(tree)
        # Set properties in the order expected by Java Flow
        self.element.set_property("invalid", False)
        if self._label:
            self.element.set_property("label", self._label)
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

    def set_label(self, label: str):
        """Set the label."""
        self._label = label
        if self._element:
            self.element.set_property("label", label)

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
