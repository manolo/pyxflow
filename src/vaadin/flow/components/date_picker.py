"""DatePicker component."""

import datetime
from typing import Callable, Optional

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasReadOnly, HasValidation, HasRequired


class DatePicker(HasReadOnly, HasValidation, HasRequired, Component):
    """A date picker component.

    Allows users to select a date from a calendar overlay.
    The value is a Python datetime.date object.
    """

    _v_fqcn = "com.vaadin.flow.component.datepicker.DatePicker"
    _tag = "vaadin-date-picker"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._value: Optional[datetime.date] = None
        self._placeholder = ""
        self._min: Optional[datetime.date] = None
        self._max: Optional[datetime.date] = None
        self._change_listeners: list[Callable] = []

    def _attach(self, tree):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)
        if self._placeholder:
            self.element.set_property("placeholder", self._placeholder)
        if self._value is not None:
            self.element.set_property("value", self._value.isoformat())
        else:
            self.element.set_property("value", "")
        if self._min is not None:
            self.element.set_property("min", self._min.isoformat())
        if self._max is not None:
            self.element.set_property("max", self._max.isoformat())
        # Init connector
        el_ref = {"@v-node": self.element.node.id}
        tree.queue_execute([
            el_ref,
            "return window.Vaadin.Flow.datepickerConnector.initLazy($0)"
        ])

        # Register change listener
        self.element.add_event_listener("change", self._handle_change)

    @property
    def value(self) -> Optional[datetime.date]:
        return self._value

    @value.setter
    def value(self, val: Optional[datetime.date]):
        self._value = val
        if self._element:
            self.element.set_property("value", val.isoformat() if val else "")

    def get_value(self) -> Optional[datetime.date]:
        return self._value

    def set_value(self, value: Optional[datetime.date]):
        old_value = self._value
        self.value = value
        if value != old_value:
            for listener in self._change_listeners:
                listener({"value": value, "from_client": False})

    def set_label(self, label: str):
        self._label = label
        if self._element:
            self.element.set_property("label", label)

    def get_label(self) -> str:
        return self._label

    def set_placeholder(self, placeholder: str):
        self._placeholder = placeholder
        if self._element:
            self.element.set_property("placeholder", placeholder)

    def set_min(self, min_date: Optional[datetime.date]):
        self._min = min_date
        if self._element:
            self.element.set_property("min", min_date.isoformat() if min_date else "")

    def set_max(self, max_date: Optional[datetime.date]):
        self._max = max_date
        if self._element:
            self.element.set_property("max", max_date.isoformat() if max_date else "")

    def set_required(self, required: bool):
        self.set_required_indicator_visible(required)

    def add_value_change_listener(self, listener: Callable):
        self._change_listeners.append(listener)

    def _handle_change(self, event_data: dict):
        value_str = event_data.get("value", "")
        if value_str:
            try:
                self._value = datetime.date.fromisoformat(value_str)
            except ValueError:
                self._value = None
        else:
            self._value = None
        for listener in self._change_listeners:
            listener(event_data)

    def _sync_property(self, name: str, value):
        if name == "value":
            if value:
                try:
                    self._value = datetime.date.fromisoformat(value)
                except ValueError:
                    self._value = None
            else:
                self._value = None
