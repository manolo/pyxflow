"""CustomField component."""

from typing import Callable, Optional, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasValidation, HasRequired

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class CustomField(HasValidation, HasRequired, Component):
    """A field wrapper that composes a value from its children.

    CustomField allows you to group multiple input fields into a single
    logical field with a combined value. The value is a tab-separated
    string of the children's values by default.

    Usage::

        cf = CustomField("Phone")
        prefix = Select()
        prefix.set_items("+1", "+44")
        number = TextField()
        cf.add(prefix, number)
    """

    _v_fqcn = "com.vaadin.flow.component.customfield.CustomField"
    _tag = "vaadin-custom-field"

    def __init__(self, label: str = ""):
        self._label = label
        self._children: list[Component] = []
        self._value: str = ""
        self._change_listeners: list[Callable] = []
        self._helper_text_val = ""

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)
        if self._helper_text_val:
            self.element.set_property("helperText", self._helper_text_val)

        # Attach children
        for child in self._children:
            child._attach(tree)
            self.element.node.add_child(child.element.node)

        # Listen for change events
        self.element.add_event_listener("change", self._handle_change)

    def add(self, *components: Component):
        """Add child components to the custom field."""
        for component in components:
            self._children.append(component)
            if self._element:
                component._attach(self._element._tree)
                self.element.node.add_child(component.element.node)

    def set_label(self, label: str):
        self._label = label
        if self._element:
            self.element.set_property("label", label)

    def get_label(self) -> str:
        return self._label

    def set_helper_text(self, text: str):
        self._helper_text_val = text
        if self._element:
            self.element.set_property("helperText", text)

    def get_helper_text(self) -> str:
        return self._helper_text_val

    def get_value(self) -> str:
        return self._value

    def set_value(self, value: str):
        old_value = self._value
        self._value = value
        if self._element:
            self.element.set_property("value", value)
        if value != old_value:
            for listener in self._change_listeners:
                listener({"value": value, "from_client": False})

    def add_value_change_listener(self, listener: Callable):
        self._change_listeners.append(listener)

    def _handle_change(self, event_data: dict):
        value = event_data.get("value", "")
        self._value = value
        for listener in self._change_listeners:
            listener({"value": value})

    def _sync_property(self, name: str, value):
        if name == "value":
            self._value = value or ""
