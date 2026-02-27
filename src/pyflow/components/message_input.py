"""MessageInput component."""

import json
from typing import Callable, TYPE_CHECKING

from pyflow.core.component import Component
from pyflow.components.constants import MessageInputVariant
from pyflow.server.uidl_handler import _SUBMIT_HASH

if TYPE_CHECKING:
    from pyflow.core.state_tree import StateTree


class MessageInput(Component):
    """A text input with a send button for chat-like interfaces.

    Fires a submit event when the user clicks send or presses Enter.
    The message text is available in ``event.detail.value``.

    Usage::

        mi = MessageInput()
        mi.add_submit_listener(lambda e: print(e["value"]))
    """

    _v_fqcn = "com.vaadin.flow.component.messages.MessageInput"
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

    def set_i18n(self, i18n: dict):
        """Set the i18n localization object (button label, placeholder, etc.)."""
        self._i18n = i18n
        self.execute_js(f"return (function(){{$0.i18n = Object.assign({{}}, $0.i18n, {json.dumps(i18n)})}}).call(null)")

    def get_i18n(self) -> dict | None:
        return getattr(self, "_i18n", None)

    def _on_submit(self, event_data: dict):
        """Handle submit event from client."""
        # event.detail.value contains the message text
        value = event_data.get("event.detail.value", "")
        for listener in self._submit_listeners:
            listener({"value": value})

    def add_theme_variants(self, *variants: MessageInputVariant):
        """Add theme variants to the message input."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: MessageInputVariant):
        """Remove theme variants from the message input."""
        self.remove_theme_name(*variants)
