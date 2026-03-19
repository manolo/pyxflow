"""TextArea component."""

from typing import Callable

from pyxflow.core.component import Component
from pyxflow.components.mixins import HasReadOnly, HasValidation, HasRequired
from pyxflow.components.constants import ValueChangeMode, TextAreaVariant


class TextArea(HasReadOnly, HasValidation, HasRequired, Component):
    """A multi-line text input component."""

    _v_fqcn = "com.vaadin.flow.component.textfield.TextArea"
    _tag = "vaadin-text-area"
    _v_sync_properties = frozenset({"value", "invalid"})

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
        if self._placeholder:
            self.element.set_property("placeholder", self._placeholder)
        self.element.set_property("value", self._value)
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

    def set_min_rows(self, min_rows: int):
        """Set the minimum number of visible rows."""
        if self._element:
            self.element.set_property("minRows", min_rows)

    def set_max_rows(self, max_rows: int):
        """Set the maximum number of visible rows."""
        if self._element:
            self.element.set_property("maxRows", max_rows)

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
        """Handle change event.

        Value arrives via mSync (_sync_property), not event_data.
        Construct proper event dict for listeners.
        """
        self._value = event_data.get("value", self._value)
        for listener in self._change_listeners:
            listener({"value": self._value, "from_client": True})

    def set_clear_button_visible(self, visible: bool):
        """Show or hide the clear button."""
        self._clear_button_visible = visible
        if self._element:
            self.element.set_property("clearButtonVisible", visible)

    def is_clear_button_visible(self) -> bool:
        return self._clear_button_visible

    def set_pattern(self, pattern: str):
        """Set the regular expression pattern for validation."""
        if self._element:
            self.element.set_property("pattern", pattern)

    def set_prefix_component(self, component):
        """Set a prefix component in the 'prefix' slot."""
        self._prefix_component = component
        if self._element:
            self._attach_slot_component(component, "prefix")

    def set_suffix_component(self, component):
        """Set a suffix component in the 'suffix' slot."""
        self._suffix_component = component
        if self._element:
            self._attach_slot_component(component, "suffix")

    def _attach_slot_component(self, component, slot: str):
        if component and not component._element:
            component._ui = self._ui
            component._parent = self
            component._attach(self._element._tree)
            component.element.set_attribute("slot", slot)
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

    def add_theme_variants(self, *variants: TextAreaVariant):
        """Add theme variants to the text area."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: TextAreaVariant):
        """Remove theme variants from the text area."""
        self.remove_theme_name(*variants)

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "value":
            self._value = value
