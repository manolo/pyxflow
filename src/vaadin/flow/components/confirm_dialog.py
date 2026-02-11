"""ConfirmDialog component."""

from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.server.uidl_handler import _CLOSED_HASH

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class ConfirmDialog(Component):
    """A dialog for asking the user to confirm or cancel an action.

    ConfirmDialog is a modal dialog that presents a header, message, and
    up to three buttons: confirm, reject, and cancel. Unlike Dialog, it
    does not use FlowComponentHost or virtual children — all content is
    controlled via properties.
    """

    _tag = "vaadin-confirm-dialog"

    def __init__(self, header: str = "", text: str = "", confirm_text: str = "Confirm"):
        super().__init__()
        self._header = header
        self._message = text
        self._confirm_text = confirm_text
        self._cancel_text = "Cancel"
        self._reject_text = ""
        self._cancelable = False
        self._rejectable = False
        self._confirm_theme = ""
        self._cancel_theme = ""
        self._reject_theme = ""
        self._opened = False
        self._confirm_listeners: list[Callable] = []
        self._cancel_listeners: list[Callable] = []
        self._reject_listeners: list[Callable] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        # Set initial properties
        if self._header:
            self.element.set_property("header", self._header)
        if self._message:
            self.element.set_property("message", self._message)
        if self._confirm_text:
            self.element.set_property("confirmText", self._confirm_text)
        if self._confirm_theme:
            self.element.set_property("confirmTheme", self._confirm_theme)

        self.element.set_property("cancelButtonVisible", self._cancelable)
        if self._cancel_text:
            self.element.set_property("cancelText", self._cancel_text)
        if self._cancel_theme:
            self.element.set_property("cancelTheme", self._cancel_theme)

        self.element.set_property("rejectButtonVisible", self._rejectable)
        if self._reject_text:
            self.element.set_property("rejectText", self._reject_text)
        if self._reject_theme:
            self.element.set_property("rejectTheme", self._reject_theme)

        # Register event listeners with explicit hash (empty config)
        self.element.add_event_listener("confirm", self._on_confirm, _CLOSED_HASH)
        self.element.add_event_listener("cancel", self._on_cancel, _CLOSED_HASH)
        self.element.add_event_listener("reject", self._on_reject, _CLOSED_HASH)

    def open(self):
        """Open the confirm dialog."""
        self._opened = True
        if self._element:
            self.element.set_property("opened", True)

    def close(self):
        """Close the confirm dialog."""
        self._opened = False
        if self._element:
            self.element.set_property("opened", False)

    def is_opened(self) -> bool:
        """Check if the dialog is open."""
        return self._opened

    def set_header(self, header: str):
        """Set the dialog header text."""
        self._header = header
        if self._element:
            self.element.set_property("header", header)

    def get_header(self) -> str:
        """Get the dialog header text."""
        return self._header

    def set_text(self, message: str):
        """Set the dialog message text."""
        self._message = message
        if self._element:
            self.element.set_property("message", message)

    def get_text(self) -> str:
        """Get the dialog message text."""
        return self._message

    def set_confirm_text(self, text: str):
        """Set the confirm button text."""
        self._confirm_text = text
        if self._element:
            self.element.set_property("confirmText", text)

    def get_confirm_text(self) -> str:
        """Get the confirm button text."""
        return self._confirm_text

    def set_confirm_button_theme(self, theme: str):
        """Set the confirm button theme (e.g., 'error primary')."""
        self._confirm_theme = theme
        if self._element:
            self.element.set_property("confirmTheme", theme)

    def set_cancelable(self, cancelable: bool):
        """Set whether the cancel button is visible."""
        self._cancelable = cancelable
        if self._element:
            self.element.set_property("cancelButtonVisible", cancelable)

    def is_cancelable(self) -> bool:
        """Check if the cancel button is visible."""
        return self._cancelable

    def set_cancel_text(self, text: str):
        """Set the cancel button text."""
        self._cancel_text = text
        if self._element:
            self.element.set_property("cancelText", text)

    def get_cancel_text(self) -> str:
        """Get the cancel button text."""
        return self._cancel_text

    def set_cancel_button_theme(self, theme: str):
        """Set the cancel button theme."""
        self._cancel_theme = theme
        if self._element:
            self.element.set_property("cancelTheme", theme)

    def set_rejectable(self, rejectable: bool):
        """Set whether the reject button is visible."""
        self._rejectable = rejectable
        if self._element:
            self.element.set_property("rejectButtonVisible", rejectable)

    def is_rejectable(self) -> bool:
        """Check if the reject button is visible."""
        return self._rejectable

    def set_reject_text(self, text: str):
        """Set the reject button text."""
        self._reject_text = text
        if self._element:
            self.element.set_property("rejectText", text)

    def get_reject_text(self) -> str:
        """Get the reject button text."""
        return self._reject_text

    def set_reject_button_theme(self, theme: str):
        """Set the reject button theme."""
        self._reject_theme = theme
        if self._element:
            self.element.set_property("rejectTheme", theme)

    def add_confirm_listener(self, listener: Callable):
        """Add a listener called when the confirm button is clicked."""
        self._confirm_listeners.append(listener)

    def add_cancel_listener(self, listener: Callable):
        """Add a listener called when the cancel button is clicked."""
        self._cancel_listeners.append(listener)

    def add_reject_listener(self, listener: Callable):
        """Add a listener called when the reject button is clicked."""
        self._reject_listeners.append(listener)

    def _on_confirm(self, event_data: dict):
        """Handle confirm event from client."""
        self._opened = False
        if self._element:
            self.element.set_property("opened", False)
        for listener in self._confirm_listeners:
            listener(event_data)

    def _on_cancel(self, event_data: dict):
        """Handle cancel event from client."""
        self._opened = False
        if self._element:
            self.element.set_property("opened", False)
        for listener in self._cancel_listeners:
            listener(event_data)

    def _on_reject(self, event_data: dict):
        """Handle reject event from client."""
        self._opened = False
        if self._element:
            self.element.set_property("opened", False)
        for listener in self._reject_listeners:
            listener(event_data)

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "opened":
            self._opened = value
