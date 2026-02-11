"""LoginForm and LoginOverlay components."""

from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.server.uidl_handler import _LOGIN_HASH, _CLOSED_HASH as _FORGOT_PASSWORD_HASH

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class LoginForm(Component):
    """A login form with username and password fields.

    Fires ``login`` event with username and password, and
    ``forgot-password`` event when the forgot password link is clicked.

    Usage::

        form = LoginForm()
        form.add_login_listener(lambda e: print(e["username"], e["password"]))
        form.add_forgot_password_listener(lambda e: print("forgot"))
    """

    _tag = "vaadin-login-form"

    def __init__(self):
        self._error = False
        self._no_forgot_password = False
        self._action = ""
        self._login_listeners: list[Callable] = []
        self._forgot_password_listeners: list[Callable] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        if self._error:
            self.element.set_property("error", True)
        if self._no_forgot_password:
            self.element.set_property("noForgotPassword", True)
        if self._action:
            self.element.set_property("action", self._action)

        self.element.add_event_listener("login", self._on_login, _LOGIN_HASH)
        self.element.add_event_listener("forgot-password", self._on_forgot_password, _FORGOT_PASSWORD_HASH)

    def add_login_listener(self, listener: Callable):
        """Add a listener for the login event.

        Receives dict with ``"username"`` and ``"password"`` keys.
        """
        self._login_listeners.append(listener)

    def add_forgot_password_listener(self, listener: Callable):
        """Add a listener for the forgot password event."""
        self._forgot_password_listeners.append(listener)

    def set_error(self, error: bool):
        """Show or hide the error message."""
        self._error = error
        if self._element:
            self.element.set_property("error", error)

    def is_error(self) -> bool:
        return self._error

    def set_forgot_password_button_visible(self, visible: bool):
        """Set whether the forgot password button is visible."""
        self._no_forgot_password = not visible
        if self._element:
            self.element.set_property("noForgotPassword", not visible)

    def set_action(self, action: str):
        """Set the form action URL."""
        self._action = action
        if self._element:
            self.element.set_property("action", action)

    def _on_login(self, event_data: dict):
        username = event_data.get("event.detail.username", "")
        password = event_data.get("event.detail.password", "")
        # Re-enable the form after login attempt
        if self._element:
            self.element.set_property("disabled", False)
        for listener in self._login_listeners:
            listener({"username": username, "password": password})

    def _on_forgot_password(self, event_data: dict):
        for listener in self._forgot_password_listeners:
            listener(event_data)

    def _sync_property(self, name: str, value):
        if name == "error":
            self._error = bool(value)
        elif name == "disabled":
            self._enabled = not bool(value)


class LoginOverlay(Component):
    """A login form displayed in a modal overlay.

    Same events as LoginForm, plus overlay control (open/close)
    and title/description properties.

    Usage::

        overlay = LoginOverlay()
        overlay.set_title("My App")
        overlay.set_description("Please sign in")
        overlay.add_login_listener(lambda e: print(e))
        overlay.open()
    """

    _tag = "vaadin-login-overlay"

    def __init__(self):
        self._opened = False
        self._title = ""
        self._description = ""
        self._error = False
        self._no_forgot_password = False
        self._login_listeners: list[Callable] = []
        self._forgot_password_listeners: list[Callable] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        if self._title:
            self.element.set_property("title", self._title)
        if self._description:
            self.element.set_property("description", self._description)
        if self._error:
            self.element.set_property("error", True)
        if self._no_forgot_password:
            self.element.set_property("noForgotPassword", True)

        self.element.add_event_listener("login", self._on_login, _LOGIN_HASH)
        self.element.add_event_listener("forgot-password", self._on_forgot_password, _FORGOT_PASSWORD_HASH)

        if self._opened:
            self.element.set_property("opened", True)

    def open(self):
        self._opened = True
        if self._element:
            self.element.set_property("opened", True)

    def close(self):
        self._opened = False
        if self._element:
            self.element.set_property("opened", False)

    def is_opened(self) -> bool:
        return self._opened

    def set_title(self, title: str):
        self._title = title
        if self._element:
            self.element.set_property("title", title)

    def get_title(self) -> str:
        return self._title

    def set_description(self, description: str):
        self._description = description
        if self._element:
            self.element.set_property("description", description)

    def get_description(self) -> str:
        return self._description

    def set_error(self, error: bool):
        self._error = error
        if self._element:
            self.element.set_property("error", error)

    def is_error(self) -> bool:
        return self._error

    def set_forgot_password_button_visible(self, visible: bool):
        self._no_forgot_password = not visible
        if self._element:
            self.element.set_property("noForgotPassword", not visible)

    def add_login_listener(self, listener: Callable):
        """Add a listener for the login event."""
        self._login_listeners.append(listener)

    def add_forgot_password_listener(self, listener: Callable):
        """Add a listener for the forgot password event."""
        self._forgot_password_listeners.append(listener)

    def _on_login(self, event_data: dict):
        username = event_data.get("event.detail.username", "")
        password = event_data.get("event.detail.password", "")
        if self._element:
            self.element.set_property("disabled", False)
        for listener in self._login_listeners:
            listener({"username": username, "password": password})

    def _on_forgot_password(self, event_data: dict):
        for listener in self._forgot_password_listeners:
            listener(event_data)

    def _sync_property(self, name: str, value):
        if name == "opened":
            self._opened = bool(value)
        elif name == "error":
            self._error = bool(value)
