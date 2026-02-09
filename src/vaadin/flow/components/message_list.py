"""MessageList component."""

from typing import TYPE_CHECKING

from vaadin.flow.core.component import Component

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


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

    _tag = "vaadin-message-list"

    def __init__(self):
        self._items: list[MessageListItem] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        self._push_items()

    def _push_items(self):
        """Push the items list as a JSON property."""
        if self._element:
            items_json = [item.to_dict() for item in self._items]
            self.element.set_property("items", items_json)

    def set_items(self, *items: MessageListItem):
        """Set the message items."""
        self._items = list(items)
        self._push_items()

    def get_items(self) -> list[MessageListItem]:
        return list(self._items)
