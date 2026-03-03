"""EmailField component."""

from typing import Callable

from pyxflow.core.component import Component
from pyxflow.components.mixins import HasReadOnly, HasValidation, HasRequired
from pyxflow.components.constants import ValueChangeMode, Autocomplete


class EmailField(HasReadOnly, HasValidation, HasRequired, Component):
    """An email input field component.

    Email Field is an extension of Text Field that accepts only email
    addresses as input. The validity is checked according to RFC 5322.
    """

    _v_fqcn = "com.vaadin.flow.component.textfield.EmailField"
    _tag = "vaadin-email-field"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._value = ""
        self._placeholder = ""
        self._clear_button_visible = False
        self._change_listeners: list[Callable] = []
        self._value_change_mode: ValueChangeMode = ValueChangeMode.ON_CHANGE
        self._value_change_timeout: int = 400

    def _attach(self, tree):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)
        self.element.set_property("value", self._value)
        if self._placeholder:
            self.element.set_property("placeholder", self._placeholder)
        if self._clear_button_visible:
            self.element.set_property("clearButtonVisible", True)
        self.element.add_event_listener(self._get_event_name(), self._handle_change)

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
        old_value = self._value
        self.value = value
        if value != old_value:
            for listener in self._change_listeners:
                listener({"value": value, "from_client": False})

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

    def set_clear_button_visible(self, visible: bool):
        """Set whether the clear button is visible."""
        self._clear_button_visible = visible
        if self._element:
            self.element.set_property("clearButtonVisible", visible)

    def is_clear_button_visible(self) -> bool:
        """Check if the clear button is visible."""
        return self._clear_button_visible

    def add_value_change_listener(self, listener: Callable):
        """Add a value change listener."""
        self._change_listeners.append(listener)

    def _handle_change(self, event_data: dict):
        """Handle change event.

        Value arrives via mSync (_sync_property), not event_data.
        Construct proper event dict for listeners.
        """
        self._value = event_data.get("value", self._value)
        for listener in self._change_listeners:
            listener({"value": self._value, "from_client": True})

    def set_pattern(self, pattern: str):
        if self._element:
            self.element.set_property("pattern", pattern)

    def set_max_length(self, max_length: int):
        if self._element:
            self.element.set_property("maxlength", max_length)

    def set_min_length(self, min_length: int):
        if self._element:
            self.element.set_property("minlength", min_length)

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

    def set_autocomplete(self, autocomplete: "Autocomplete | str"):
        """Set the autocomplete hint for the browser."""
        self._autocomplete = autocomplete
        if self._element:
            self.element.set_attribute("autocomplete", autocomplete)

    def get_autocomplete(self) -> str | None:
        """Get the autocomplete hint."""
        return getattr(self, "_autocomplete", None)

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "value":
            self._value = value
