"""Field component mixins: HasValidation, HasRequired."""


class HasValidation:
    """Mixin providing validation API (invalid state + error message).

    Uses _pending_properties for buffering before attach, matching the
    pattern used by Component.set_helper_text() and set_tooltip_text().
    """

    _invalid: bool = False
    _error_message: str = ""

    def set_invalid(self, invalid: bool) -> None:
        """Set whether the field is currently in an invalid state."""
        self._invalid = invalid
        if self._element is not None:
            self.element.set_property("invalid", invalid)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["invalid"] = invalid

    def is_invalid(self) -> bool:
        """Get whether the field is currently in an invalid state."""
        return self._invalid

    def set_error_message(self, message: str) -> None:
        """Set the error message shown when the field is invalid."""
        self._error_message = message
        if self._element is not None:
            self.element.set_property("errorMessage", message)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["errorMessage"] = message

    def get_error_message(self) -> str:
        """Get the error message."""
        return self._error_message


class HasRequired:
    """Mixin providing required indicator API.

    Maps to the 'required' property on the web component, which
    controls the required indicator visibility.
    """

    _required_indicator_visible: bool = False

    def set_required_indicator_visible(self, required: bool) -> None:
        """Set whether the required indicator is visible."""
        self._required_indicator_visible = required
        if self._element is not None:
            self.element.set_property("required", required)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["required"] = required

    def is_required_indicator_visible(self) -> bool:
        """Get whether the required indicator is visible."""
        return self._required_indicator_visible
