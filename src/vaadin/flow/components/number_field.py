"""NumberField component."""

from typing import Callable, Optional

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasValidation, HasRequired


class NumberField(HasValidation, HasRequired, Component):
    """A number input field component."""

    _tag = "vaadin-number-field"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._value: Optional[float] = None
        self._placeholder = ""
        self._min: Optional[float] = None
        self._max: Optional[float] = None
        self._step: Optional[float] = None
        self._step_buttons_visible: bool = False
        self._change_listeners: list[Callable] = []

    def _attach(self, tree):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)
        if self._placeholder:
            self.element.set_property("placeholder", self._placeholder)
        if self._value is not None:
            self.element.set_property("value", str(self._value))
        if self._min is not None:
            self.element.set_property("min", self._min)
        if self._max is not None:
            self.element.set_property("max", self._max)
        if self._step is not None:
            self.element.set_property("step", self._step)
        if self._step_buttons_visible:
            self.element.set_property("stepButtonsVisible", True)
        self.element.add_event_listener("change", self._handle_change)

    @property
    def value(self) -> Optional[float]:
        """Get the current value."""
        return self._value

    @value.setter
    def value(self, val: Optional[float]):
        """Set the value."""
        self._value = val
        if self._element:
            if val is not None:
                self.element.set_property("value", str(val))
            else:
                self.element.set_property("value", "")

    def get_value(self) -> Optional[float]:
        """Get the current value."""
        return self._value

    def set_value(self, value: Optional[float]):
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

    def get_min(self) -> Optional[float]:
        """Get the minimum value."""
        return self._min

    def set_min(self, min_value: float):
        """Set the minimum value."""
        self._min = min_value
        if self._element:
            self.element.set_property("min", min_value)

    def get_max(self) -> Optional[float]:
        """Get the maximum value."""
        return self._max

    def set_max(self, max_value: float):
        """Set the maximum value."""
        self._max = max_value
        if self._element:
            self.element.set_property("max", max_value)

    def get_step(self) -> Optional[float]:
        """Get the step value."""
        return self._step

    def set_step(self, step: float):
        """Set the step value for increment/decrement."""
        self._step = step
        if self._element:
            self.element.set_property("step", step)

    def set_step_buttons_visible(self, visible: bool):
        """Show or hide the step buttons."""
        self._step_buttons_visible = visible
        if self._element:
            self.element.set_property("stepButtonsVisible", visible)

    def add_value_change_listener(self, listener: Callable):
        """Add a value change listener."""
        self._change_listeners.append(listener)

    def _handle_change(self, event_data: dict):
        """Handle change event."""
        value_str = event_data.get("value", "")
        if value_str == "" or value_str is None:
            self._value = None
        else:
            try:
                self._value = float(value_str)
            except (ValueError, TypeError):
                self._value = None

        for listener in self._change_listeners:
            listener(event_data)

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "value":
            if value == "" or value is None:
                self._value = None
            else:
                try:
                    self._value = float(value)
                except (ValueError, TypeError):
                    self._value = None


class IntegerField(NumberField):
    """An integer-only number input field component."""

    _tag = "vaadin-integer-field"

    def __init__(self, label: str = ""):
        super().__init__(label)
        self._int_value: Optional[int] = None

    def _attach(self, tree):
        # Set _value to int before parent _attach calls str(self._value)
        if self._int_value is not None:
            self._value = self._int_value  # int, not float — so str() gives "42" not "42.0"
        super()._attach(tree)

    @property
    def value(self) -> Optional[int]:  # type: ignore[override]
        """Get the current value as integer."""
        return self._int_value

    @value.setter
    def value(self, val: Optional[int]):  # type: ignore[override]
        """Set the value."""
        self._int_value = val
        self._value = float(val) if val is not None else None
        if self._element:
            if val is not None:
                self.element.set_property("value", str(val))
            else:
                self.element.set_property("value", "")

    def get_value(self) -> Optional[int]:
        """Get the current value as integer."""
        return self._int_value

    def set_value(self, value: Optional[int]):  # type: ignore[override]
        """Set the value."""
        self.value = value

    def _handle_change(self, event_data: dict):
        """Handle change event."""
        value_str = event_data.get("value", "")
        if value_str == "" or value_str is None:
            self._int_value = None
            self._value = None
        else:
            try:
                self._int_value = int(float(value_str))
                self._value = float(self._int_value)
            except (ValueError, TypeError):
                self._int_value = None
                self._value = None

        for listener in self._change_listeners:
            listener(event_data)

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "value":
            if value == "" or value is None:
                self._int_value = None
                self._value = None
            else:
                try:
                    self._int_value = int(float(value))
                    self._value = float(self._int_value)
                except (ValueError, TypeError):
                    self._int_value = None
                    self._value = None
