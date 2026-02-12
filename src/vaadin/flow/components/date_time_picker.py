"""DateTimePicker component — combined date and time selection."""

import datetime
from typing import Callable, Optional

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasReadOnly, HasValidation, HasRequired


class DateTimePicker(HasReadOnly, HasValidation, HasRequired, Component):
    """A date-time picker component.

    Combines DatePicker and TimePicker into a single field.
    Value is a Python datetime.datetime object.
    Internally uses datepickerConnector and timepickerConnector for the sub-fields.
    """

    _v_fqcn = "com.vaadin.flow.component.datetimepicker.DateTimePicker"
    _tag = "vaadin-date-time-picker"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._value: Optional[datetime.datetime] = None
        self._date_placeholder = ""
        self._time_placeholder = ""
        self._min: Optional[datetime.datetime] = None
        self._max: Optional[datetime.datetime] = None
        self._step: Optional[int] = None
        self._change_listeners: list[Callable] = []

    def _attach(self, tree):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)
        if self._date_placeholder:
            self.element.set_property("datePlaceholder", self._date_placeholder)
        if self._time_placeholder:
            self.element.set_property("timePlaceholder", self._time_placeholder)
        if self._value is not None:
            self.element.set_property("value", self._format_datetime(self._value))
        else:
            self.element.set_property("value", "")
        if self._min is not None:
            self.element.set_property("min", self._format_datetime(self._min))
        if self._max is not None:
            self.element.set_property("max", self._format_datetime(self._max))
        if self._step is not None:
            self.element.set_property("step", self._step)
        # Init connectors for internal date-picker and time-picker sub-fields
        el_ref = {"@v-node": self.element.node.id}
        tree.queue_execute([
            el_ref,
            "return window.Vaadin.Flow.datepickerConnector.initLazy($0.querySelector('[slot=date-picker]'))"
        ])
        tree.queue_execute([
            el_ref,
            "return window.Vaadin.Flow.timepickerConnector.initLazy($0.querySelector('[slot=time-picker]'))"
        ])

        self.element.add_event_listener("change", self._handle_change)

    @staticmethod
    def _format_datetime(dt: datetime.datetime) -> str:
        """Format as ISO string: 'YYYY-MM-DDTHH:MM' or 'YYYY-MM-DDTHH:MM:SS'."""
        if dt.second:
            return dt.strftime("%Y-%m-%dT%H:%M:%S")
        return dt.strftime("%Y-%m-%dT%H:%M")

    @staticmethod
    def _parse_datetime(s: str) -> Optional[datetime.datetime]:
        if not s:
            return None
        try:
            return datetime.datetime.fromisoformat(s)
        except ValueError:
            return None

    @property
    def value(self) -> Optional[datetime.datetime]:
        return self._value

    @value.setter
    def value(self, val: Optional[datetime.datetime]):
        self._value = val
        if self._element:
            self.element.set_property("value", self._format_datetime(val) if val else "")

    def get_value(self) -> Optional[datetime.datetime]:
        return self._value

    def set_value(self, value: Optional[datetime.datetime]):
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

    def set_date_placeholder(self, placeholder: str):
        self._date_placeholder = placeholder
        if self._element:
            self.element.set_property("datePlaceholder", placeholder)

    def set_time_placeholder(self, placeholder: str):
        self._time_placeholder = placeholder
        if self._element:
            self.element.set_property("timePlaceholder", placeholder)

    def set_min(self, min_dt: Optional[datetime.datetime]):
        self._min = min_dt
        if self._element:
            self.element.set_property("min", self._format_datetime(min_dt) if min_dt else "")

    def set_max(self, max_dt: Optional[datetime.datetime]):
        self._max = max_dt
        if self._element:
            self.element.set_property("max", self._format_datetime(max_dt) if max_dt else "")

    def set_step(self, step: Optional[int]):
        """Set the time step in seconds (e.g., 1800 for 30 minutes)."""
        self._step = step
        if self._element:
            if step is not None:
                self.element.set_property("step", step)

    def set_required(self, required: bool):
        self.set_required_indicator_visible(required)

    def add_value_change_listener(self, listener: Callable):
        self._change_listeners.append(listener)

    def _handle_change(self, event_data: dict):
        value_str = event_data.get("value", "")
        self._value = self._parse_datetime(value_str)
        for listener in self._change_listeners:
            listener(event_data)

    def set_auto_open(self, auto_open: bool):
        if self._element:
            self.element.set_property("autoOpenDisabled", not auto_open)

    def _sync_property(self, name: str, value):
        if name == "value":
            self._value = self._parse_datetime(value) if value else None
