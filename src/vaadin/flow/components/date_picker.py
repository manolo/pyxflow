"""DatePicker component."""

import datetime
import json
from typing import Callable, Optional

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasReadOnly, HasValidation, HasRequired
from vaadin.flow.components.constants import DatePickerVariant


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
        self._clear_button_visible: bool = False
        self._change_listeners: list[Callable] = []

    def _attach(self, tree):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)
        if self._placeholder:
            self.element.set_property("placeholder", self._placeholder)
        if self._value is not None:
            val_str = self._value.isoformat() if isinstance(self._value, datetime.date) else str(self._value)
            self.element.set_property("value", val_str)
        else:
            self.element.set_property("value", "")
        if self._min is not None:
            self.element.set_property("min", self._min.isoformat())
        if self._max is not None:
            self.element.set_property("max", self._max.isoformat())
        if self._clear_button_visible:
            self.element.set_property("clearButtonVisible", True)
        if getattr(self, "_week_numbers_visible", False):
            self.element.set_property("showWeekNumbers", True)
        if getattr(self, "_initial_position", None):
            self.element.set_property("initialPosition", self._initial_position.isoformat())
        # Init connector
        el_ref = {"@v-node": self.element.node.id}
        tree.queue_execute([
            el_ref,
            "return window.Vaadin.Flow.datepickerConnector.initLazy($0)"
        ])

        # Register change listener
        self.element.add_event_listener("change", self._handle_change)
        if getattr(self, "_opened_change_listeners", None):
            self.element.add_event_listener("opened-changed", self._handle_opened_changed)

    @property
    def value(self) -> Optional[datetime.date]:
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            if val:
                try:
                    self._value = datetime.date.fromisoformat(val)
                except ValueError:
                    self._value = None
            else:
                self._value = None
        else:
            self._value = val
        if self._element:
            self.element.set_property(
                "value",
                self._value.isoformat() if self._value else "",
            )

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
        """Handle change event.

        Value arrives via mSync (_sync_property), not event_data.
        """
        for listener in self._change_listeners:
            listener({"value": self._value, "from_client": True})

    def set_clear_button_visible(self, visible: bool):
        self._clear_button_visible = visible
        if self._element:
            self.element.set_property("clearButtonVisible", visible)

    def is_clear_button_visible(self) -> bool:
        return getattr(self, "_clear_button_visible", False)

    def set_auto_open(self, auto_open: bool):
        """Set whether the dropdown opens automatically on focus."""
        if self._element:
            self.element.set_property("autoOpenDisabled", not auto_open)

    def set_i18n(self, i18n: dict):
        """Set the i18n localization object (month names, weekdays, etc.)."""
        self._i18n = i18n
        self.execute_js(f"return (function(){{$0.i18n = Object.assign({{}}, $0.i18n, {json.dumps(i18n)})}}).call(null)")

    def get_i18n(self) -> dict | None:
        return getattr(self, "_i18n", None)

    def set_week_numbers_visible(self, visible: bool):
        """Set whether ISO week numbers are shown."""
        self._week_numbers_visible = visible
        if self._element:
            self.element.set_property("showWeekNumbers", visible)

    def is_week_numbers_visible(self) -> bool:
        return getattr(self, "_week_numbers_visible", False)

    def set_initial_position(self, date: "datetime.date | None"):
        """Set the initial calendar position when no value is selected."""
        self._initial_position = date
        if self._element:
            self.element.set_property("initialPosition", date.isoformat() if date else "")

    def get_initial_position(self):
        return getattr(self, "_initial_position", None)

    def open(self):
        """Open the date picker overlay."""
        if self._element:
            self.element.set_property("opened", True)

    def close(self):
        """Close the date picker overlay."""
        if self._element:
            self.element.set_property("opened", False)

    def add_opened_change_listener(self, listener: Callable):
        """Add a listener for when the overlay opens or closes."""
        if not hasattr(self, "_opened_change_listeners"):
            self._opened_change_listeners = []
        self._opened_change_listeners.append(listener)
        if self._element and len(self._opened_change_listeners) == 1:
            self.element.add_event_listener("opened-changed", self._handle_opened_changed)

    def _handle_opened_changed(self, event_data: dict):
        """Handle opened-changed event."""
        for listener in getattr(self, "_opened_change_listeners", []):
            listener(event_data)

    def add_theme_variants(self, *variants: DatePickerVariant):
        """Add theme variants to the date picker."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: DatePickerVariant):
        """Remove theme variants from the date picker."""
        self.remove_theme_name(*variants)

    def _sync_property(self, name: str, value):
        if name == "value":
            if value:
                try:
                    self._value = datetime.date.fromisoformat(value)
                except ValueError:
                    self._value = None
            else:
                self._value = None
