"""Checkbox component."""

from typing import Callable

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasReadOnly, HasRequired
from vaadin.flow.components.constants import CheckboxVariant as CheckboxVariant


class Checkbox(HasReadOnly, HasRequired, Component):
    """A checkbox input component representing a binary choice."""

    _v_fqcn = "com.vaadin.flow.component.checkbox.Checkbox"
    _tag = "vaadin-checkbox"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._checked = False
        self._indeterminate = False
        self._change_listeners: list[Callable] = []

    def _attach(self, tree):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)
        self.element.set_property("checked", self._checked)
        if self._indeterminate:
            self.element.set_property("indeterminate", self._indeterminate)
        self.element.add_event_listener("checked-changed", self._handle_change)

    @property
    def value(self) -> bool:
        """Get the checked state (alias for is_checked)."""
        return self._checked

    @value.setter
    def value(self, val: bool):
        """Set the checked state."""
        self.set_checked(val)

    def is_checked(self) -> bool:
        """Get the checked state."""
        return self._checked

    def set_checked(self, checked: bool):
        """Set the checked state."""
        old_checked = self._checked
        self._checked = checked
        self._indeterminate = False  # Setting checked clears indeterminate
        if self._element:
            self.element.set_property("checked", checked)
            self.element.set_property("indeterminate", False)
        if checked != old_checked:
            for listener in self._change_listeners:
                listener({"value": checked, "from_client": False})

    def get_value(self) -> bool:
        """Get the checked state."""
        return self._checked

    def set_value(self, value: bool):
        """Set the checked state."""
        self.set_checked(value)

    def get_label(self) -> str:
        """Get the label."""
        return self._label

    def set_label(self, label: str):
        """Set the label."""
        self._label = label
        if self._element:
            self.element.set_property("label", label)

    def is_indeterminate(self) -> bool:
        """Get the indeterminate state."""
        return self._indeterminate

    def set_indeterminate(self, indeterminate: bool):
        """Set the indeterminate state.

        The indeterminate state is used for parent checkboxes to show
        a mix of checked and unchecked child items.
        """
        self._indeterminate = indeterminate
        if self._element:
            self.element.set_property("indeterminate", indeterminate)

    def add_value_change_listener(self, listener: Callable):
        """Add a listener for value changes."""
        self._change_listeners.append(listener)

    def _handle_change(self, event_data: dict):
        """Handle checked-changed event from client."""
        if "checked" in event_data:
            self._checked = bool(event_data["checked"])
        self._indeterminate = False  # User interaction clears indeterminate
        for listener in self._change_listeners:
            listener({"value": self._checked, "from_client": True})

    def add_theme_variants(self, *variants: CheckboxVariant):
        """Add theme variants to the checkbox."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: CheckboxVariant):
        """Remove theme variants from the checkbox."""
        self.remove_theme_name(*variants)

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "checked":
            self._checked = value
            self._indeterminate = False
