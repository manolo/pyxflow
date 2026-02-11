"""TimePicker component."""

import datetime
from typing import Callable, Optional

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasValidation, HasRequired


class TimePicker(HasValidation, HasRequired, Component):
    """A time picker component.

    Allows users to select a time from a dropdown overlay.
    The value is a Python datetime.time object.
    """

    _tag = "vaadin-time-picker"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._value: Optional[datetime.time] = None
        self._placeholder = ""
        self._min: Optional[datetime.time] = None
        self._max: Optional[datetime.time] = None
        self._step: Optional[int] = None
        self._change_listeners: list[Callable] = []

    def _attach(self, tree):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)
        if self._placeholder:
            self.element.set_property("placeholder", self._placeholder)
        if self._value is not None:
            self.element.set_property("value", self._format_time(self._value))
        else:
            self.element.set_property("value", "")
        if self._min is not None:
            self.element.set_property("min", self._format_time(self._min))
        if self._max is not None:
            self.element.set_property("max", self._format_time(self._max))
        if self._step is not None:
            self.element.set_property("step", self._step)
        # Init connector
        el_ref = {"@v-node": self.element.node.id}
        tree.queue_execute([
            el_ref,
            "return window.Vaadin.Flow.timepickerConnector.initLazy($0)"
        ])

        # Register change listener
        self.element.add_event_listener("change", self._handle_change)

    @staticmethod
    def _format_time(t: datetime.time) -> str:
        """Format time as HH:mm or HH:mm:ss."""
        if t.second:
            return t.strftime("%H:%M:%S")
        return t.strftime("%H:%M")

    @staticmethod
    def _parse_time(s: str) -> Optional[datetime.time]:
        """Parse time from HH:mm or HH:mm:ss string."""
        if not s:
            return None
        try:
            return datetime.time.fromisoformat(s)
        except ValueError:
            return None

    @property
    def value(self) -> Optional[datetime.time]:
        return self._value

    @value.setter
    def value(self, val: Optional[datetime.time]):
        self._value = val
        if self._element:
            self.element.set_property("value", self._format_time(val) if val else "")

    def get_value(self) -> Optional[datetime.time]:
        return self._value

    def set_value(self, value: Optional[datetime.time]):
        self.value = value

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

    def set_min(self, min_time: Optional[datetime.time]):
        self._min = min_time
        if self._element:
            self.element.set_property("min", self._format_time(min_time) if min_time else "")

    def set_max(self, max_time: Optional[datetime.time]):
        self._max = max_time
        if self._element:
            self.element.set_property("max", self._format_time(max_time) if max_time else "")

    def set_step(self, step: Optional[int]):
        """Set the step in seconds (e.g., 1800 for 30 minutes)."""
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
        self._value = self._parse_time(value_str)
        for listener in self._change_listeners:
            listener(event_data)

    def _sync_property(self, name: str, value):
        if name == "value":
            self._value = self._parse_time(value) if value else None
