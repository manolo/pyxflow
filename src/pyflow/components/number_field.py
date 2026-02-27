"""NumberField component."""

from typing import Callable, Optional

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasReadOnly, HasValidation, HasRequired
from vaadin.flow.components.constants import ValueChangeMode


class NumberField(HasReadOnly, HasValidation, HasRequired, Component):
    """A number input field component."""

    _v_fqcn = "com.vaadin.flow.component.textfield.NumberField"
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
        self._clear_button_visible: bool = False
        self._change_listeners: list[Callable] = []
        self._value_change_mode: ValueChangeMode = ValueChangeMode.ON_CHANGE
        self._value_change_timeout: int = 400

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
        if self._clear_button_visible:
            self.element.set_property("clearButtonVisible", True)
        self.element.add_event_listener(self._get_event_name(), self._handle_change)
        # Flush pending prefix/suffix components
        if hasattr(self, '_prefix_component') and self._prefix_component:
            self.set_prefix_component(self._prefix_component)
        if hasattr(self, '_suffix_component') and self._suffix_component:
            self.set_suffix_component(self._suffix_component)

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
        old_value = self._value
        self.value = value
        if value != old_value:
            for listener in self._change_listeners:
                listener({"value": value, "from_client": False})

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
        """Handle change event from client."""
        value_str = event_data.get("value")
        if value_str is not None:
            if value_str != "":
                try:
                    self._value = float(value_str)
                except (ValueError, TypeError):
                    self._value = None
            else:
                self._value = None
        # If "value" not in event_data, keep self._value (set by mSync)
        for listener in self._change_listeners:
            listener({"value": self._value, "from_client": True})

    def set_clear_button_visible(self, visible: bool):
        self._clear_button_visible = visible
        if self._element:
            self.element.set_property("clearButtonVisible", visible)

    def is_clear_button_visible(self) -> bool:
        return self._clear_button_visible

    def set_prefix_component(self, component):
        """Set a prefix component in the 'prefix' slot."""
        self._prefix_component = component
        if self._element:
            if component and not component._element:
                component._ui = self._ui
                component._parent = self
                component._attach(self._element._tree)
                component.element.set_attribute("slot", "prefix")
                self.element.add_child(component.element)

    def set_suffix_component(self, component):
        """Set a suffix component in the 'suffix' slot."""
        self._suffix_component = component
        if self._element:
            if component and not component._element:
                component._ui = self._ui
                component._parent = self
                component._attach(self._element._tree)
                component.element.set_attribute("slot", "suffix")
                self.element.add_child(component.element)

    def set_value_change_mode(self, mode: ValueChangeMode):
        """Set how eagerly value changes are synced to the server."""
        self._value_change_mode = mode

    def get_value_change_mode(self) -> ValueChangeMode:
        return self._value_change_mode

    def set_value_change_timeout(self, timeout: int):
        """Set the timeout in ms for LAZY/TIMEOUT modes (no effect for now)."""
        self._value_change_timeout = timeout

    def get_value_change_timeout(self) -> int:
        return self._value_change_timeout

    def _get_event_name(self) -> str:
        """Return the DOM event name for the current value change mode."""
        if self._value_change_mode in (ValueChangeMode.EAGER, ValueChangeMode.LAZY, ValueChangeMode.TIMEOUT):
            return "input"
        elif self._value_change_mode == ValueChangeMode.ON_BLUR:
            return "blur"
        return "change"

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

    _v_fqcn = "com.vaadin.flow.component.textfield.IntegerField"
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
        old_value = self._int_value
        self.value = value
        if value != old_value:
            for listener in self._change_listeners:
                listener({"value": value, "from_client": False})

    def _handle_change(self, event_data: dict):
        """Handle change event from client."""
        value_str = event_data.get("value")
        if value_str is not None:
            if value_str != "":
                try:
                    self._value = float(value_str)
                    self._int_value = int(self._value)
                except (ValueError, TypeError):
                    self._value = None
                    self._int_value = None
            else:
                self._value = None
                self._int_value = None
        # If "value" not in event_data, keep self._int_value (set by mSync)
        for listener in self._change_listeners:
            listener({"value": self._int_value, "from_client": True})

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
