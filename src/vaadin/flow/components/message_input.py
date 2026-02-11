"""MessageInput component."""

from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.server.uidl_handler import _SUBMIT_HASH

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class MessageInput(Component):
    """A text input with a send button for chat-like interfaces.

    Fires a submit event when the user clicks send or presses Enter.
    The message text is available in ``event.detail.value``.

    Usage::

        mi = MessageInput()
        mi.add_submit_listener(lambda e: print(e["value"]))
    """

    _tag = "vaadin-message-input"

    def __init__(self):
        self._submit_listeners: list[Callable] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        self.element.add_event_listener("submit", self._on_submit, _SUBMIT_HASH)

    def add_submit_listener(self, listener: Callable):
        """Add a listener called when the user submits a message.

        The listener receives a dict with key ``"value"`` containing the message text.
        """
        self._submit_listeners.append(listener)

    def _on_submit(self, event_data: dict):
        """Handle submit event from client."""
        # event.detail.value contains the message text
        value = event_data.get("event.detail.value", "")
        for listener in self._submit_listeners:
            listener({"value": value})
