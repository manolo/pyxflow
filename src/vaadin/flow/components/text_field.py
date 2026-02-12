"""TextField component."""

from typing import TYPE_CHECKING, Callable

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasReadOnly, HasValidation, HasRequired

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class TextField(HasReadOnly, HasValidation, HasRequired, Component):
    """A text field component."""

    _v_fqcn = "com.vaadin.flow.component.textfield.TextField"
    _tag = "vaadin-text-field"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._value = ""
        self._clear_button_visible: bool = False
        self._placeholder: str = ""
        self._pattern: str = ""
        self._allowed_char_pattern: str = ""
        self._prefix_component: Component | None = None
        self._change_listeners: list[Callable] = []

    def _attach(self, tree):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)
        self.element.set_property("value", self._value)
        if self._clear_button_visible:
            self.element.set_property("clearButtonVisible", True)
        if self._placeholder:
            self.element.set_property("placeholder", self._placeholder)
        if self._pattern:
            self.element.set_property("pattern", self._pattern)
        if self._allowed_char_pattern:
            self.element.set_property("allowedCharPattern", self._allowed_char_pattern)
        if self._prefix_component:
            self._attach_prefix(tree)
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

    def set_pattern(self, pattern: str):
        """Set the regular expression pattern for validation."""
        self._pattern = pattern
        if self._element:
            self.element.set_property("pattern", pattern)

    def set_allowed_char_pattern(self, pattern: str):
        """Set the pattern for allowed characters (blocks input of non-matching chars)."""
        self._allowed_char_pattern = pattern
        if self._element:
            self.element.set_property("allowedCharPattern", pattern)

    def add_value_change_listener(self, listener: Callable):
        """Add a value change listener."""
        self._change_listeners.append(listener)

    def _handle_change(self, event_data: dict):
        """Handle change event."""
        self._value = event_data.get("value", self._value)
        for listener in self._change_listeners:
            listener(event_data)

    def set_clear_button_visible(self, visible: bool):
        """Show or hide the clear button."""
        self._clear_button_visible = visible
        if self._element:
            self.element.set_property("clearButtonVisible", visible)

    def set_placeholder(self, text: str):
        """Set the placeholder text."""
        self._placeholder = text
        if self._element:
            self.element.set_property("placeholder", text)

    def get_placeholder(self) -> str:
        """Get the placeholder text."""
        return self._placeholder

    def set_prefix_component(self, component: Component):
        """Set a prefix component (e.g. Icon) in the 'prefix' slot."""
        self._prefix_component = component
        if self._element:
            self._attach_prefix(self._element._tree)

    def _attach_prefix(self, tree: "StateTree"):
        """Attach the prefix component with slot='prefix'."""
        comp = self._prefix_component
        if comp and not comp._element:
            comp._ui = self._ui
            comp._parent = self
            comp._attach(tree)
            comp.element.set_attribute("slot", "prefix")
            self.element.add_child(comp.element)

    def set_suffix_component(self, component: Component):
        """Set a suffix component (e.g. Icon) in the 'suffix' slot."""
        self._suffix_component = component
        if self._element:
            self._attach_suffix(self._element._tree)

    def _attach_suffix(self, tree: "StateTree"):
        comp = self._suffix_component
        if comp and not comp._element:
            comp._ui = self._ui
            comp._parent = self
            comp._attach(tree)
            comp.element.set_attribute("slot", "suffix")
            self.element.add_child(comp.element)

    def set_max_length(self, max_length: int):
        """Set the maximum number of characters."""
        self._max_length = max_length
        if self._element:
            self.element.set_property("maxlength", max_length)

    def get_max_length(self) -> int:
        return getattr(self, "_max_length", 0)

    def set_min_length(self, min_length: int):
        """Set the minimum number of characters."""
        self._min_length = min_length
        if self._element:
            self.element.set_property("minlength", min_length)

    def get_min_length(self) -> int:
        return getattr(self, "_min_length", 0)

    def set_autoselect(self, autoselect: bool):
        """Set whether the text is automatically selected when the field gets focus."""
        self._autoselect = autoselect
        if self._element:
            self.element.set_property("autoselect", autoselect)

    def is_autoselect(self) -> bool:
        return getattr(self, "_autoselect", False)

    def is_clear_button_visible(self) -> bool:
        return self._clear_button_visible

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "value":
            self._value = value
