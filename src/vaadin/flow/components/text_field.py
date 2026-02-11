"""TextField component."""

from typing import TYPE_CHECKING, Callable

from vaadin.flow.core.component import Component

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class TextField(Component):
    """A text field component."""

    _tag = "vaadin-text-field"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._value = ""
        self._clear_button_visible: bool = False
        self._placeholder: str = ""
        self._pattern: str = ""
        self._allowed_char_pattern: str = ""
        self._error_message: str = ""
        self._prefix_component: Component | None = None
        self._change_listeners: list[Callable] = []

    def _attach(self, tree):
        super()._attach(tree)
        # Set properties in the order expected by Java Flow
        self.element.set_property("invalid", False)
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
        if self._error_message:
            self.element.set_property("errorMessage", self._error_message)
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
        self.value = value

    def set_label(self, label: str):
        """Set the label."""
        self._label = label
        if self._element:
            self.element.set_property("label", label)

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

    def set_error_message(self, message: str):
        """Set the error message shown when the field is invalid."""
        self._error_message = message
        if self._element:
            self.element.set_property("errorMessage", message)

    def get_error_message(self) -> str:
        """Get the error message."""
        return self._error_message

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

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "value":
            self._value = value
