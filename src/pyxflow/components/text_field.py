"""TextField component."""

from typing import TYPE_CHECKING, Callable

from pyxflow.core.component import Component
from pyxflow.components.mixins import HasReadOnly, HasValidation, HasRequired
from pyxflow.components.constants import ValueChangeMode, TextFieldVariant, Autocomplete

if TYPE_CHECKING:
    from pyxflow.core.state_tree import StateTree


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
        self._value_change_mode: ValueChangeMode = ValueChangeMode.ON_CHANGE
        self._value_change_timeout: int = 400

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
        if getattr(self, "_max_length", 0):
            self.element.set_property("maxlength", self._max_length)
        if self._prefix_component:
            self._attach_prefix(tree)
        if getattr(self, "_suffix_component", None):
            self._attach_suffix(tree)
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

    def set_value_change_mode(self, mode: ValueChangeMode):
        """Set how eagerly value changes are synced to the server.

        EAGER/LAZY/TIMEOUT use the "input" event (every keystroke).
        ON_BLUR uses the "blur" event (when focus leaves).
        ON_CHANGE uses the "change" event (default, on Enter or blur).
        """
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

    def add_theme_variants(self, *variants: TextFieldVariant):
        """Add theme variants to the text field."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: TextFieldVariant):
        """Remove theme variants from the text field."""
        self.remove_theme_name(*variants)

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "value":
            self._value = value
