"""MessageList component."""

from typing import TYPE_CHECKING

from pyxflow.core.component import Component

if TYPE_CHECKING:
    from pyxflow.core.state_tree import StateTree


class MessageListItem:
    """Data class for MessageList items.

    Usage::

        item = MessageListItem("Hello!", "2025-01-01T12:00:00", "Alice")
    """

    def __init__(self, text: str = "", time: str | None = None,
                 user_name: str = "", user_abbr: str = "",
                 user_img: str = "", user_color_index: int | None = None,
                 theme: str | None = None):
        self.text = text
        self.time = time
        self.user_name = user_name
        self.user_abbr = user_abbr
        self.user_img = user_img
        self.user_color_index = user_color_index
        self.theme = theme
        self._message_list: "MessageList | None" = None

    def append_text(self, text: str):
        """Append text to this item and update the parent MessageList."""
        self.text += text
        if self._message_list:
            self._message_list._push_items()

    def to_dict(self) -> dict:
        d: dict = {}
        if self.text:
            d["text"] = self.text
        if self.time is not None:
            d["time"] = self.time
        if self.user_name:
            d["userName"] = self.user_name
        if self.user_abbr:
            d["userAbbr"] = self.user_abbr
        if self.user_img:
            d["userImg"] = self.user_img
        if self.user_color_index is not None:
            d["userColorIndex"] = self.user_color_index
        if self.theme:
            d["theme"] = self.theme
        return d


class MessageList(Component):
    """A component for displaying a list of messages.

    Messages are displayed as a read-only list, typically used for chat UIs.
    Items are pushed as a JSON array to the ``items`` property.

    Usage::

        ml = MessageList()
        ml.set_items(
            MessageListItem("Hello!", user_name="Alice"),
            MessageListItem("Hi there!", user_name="Bob"),
        )
    """

    _v_fqcn = "com.vaadin.flow.component.messages.MessageList"
    _tag = "vaadin-message-list"

    def __init__(self):
        self._items: list[MessageListItem] = []
        self._markdown: bool = False

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._markdown:
            self.element.set_property("markdown", True)
        self._push_items()

    def _push_items(self):
        """Push the items list as a JSON property."""
        if self._element:
            items_json = [item.to_dict() for item in self._items]
            self.element.set_property("items", items_json)

    def set_items(self, *items: MessageListItem):
        """Set the message items."""
        # Support both set_items(item1, item2) and set_items([item1, item2])
        if len(items) == 1 and isinstance(items[0], (list, tuple)):
            items = items[0]
        self._items = list(items)
        for item in self._items:
            item._message_list = self
        self._push_items()

    def get_items(self) -> list[MessageListItem]:
        return list(self._items)

    def set_markdown(self, enabled: bool):
        """Enable or disable markdown rendering in messages."""
        self._markdown = enabled
        if self._element:
            self.element.set_property("markdown", enabled)
