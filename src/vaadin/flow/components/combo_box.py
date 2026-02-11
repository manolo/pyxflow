"""ComboBox component."""

from typing import Callable, Generic, TypeVar, Optional, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature
from vaadin.flow.data.provider import DataProvider, Query

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree

T = TypeVar('T')


class ComboBox(Component, Generic[T]):
    """A combo box component with filtering support.

    Allows users to select a value from a filtered dropdown list.
    Items are pushed to the client via the comboBoxConnector, similar to Grid.
    """

    _tag = "vaadin-combo-box"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._items: list[T] = []
        self._value: Optional[T] = None
        self._placeholder = ""
        self._page_size = 50
        self._allow_custom_value = False
        self._required = False
        self._item_label_generator: Optional[Callable[[T], str]] = None
        self._change_listeners: list[Callable] = []
        self._custom_value_listeners: list[Callable] = []
        self._update_id = 0
        self._provider: DataProvider | None = None
        self._provider_listener_unsub: Callable | None = None

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        self.element.set_property("invalid", False)
        if self._label:
            self.element.set_property("label", self._label)
        if self._placeholder:
            self.element.set_property("placeholder", self._placeholder)
        self.element.set_property("pageSize", self._page_size)
        self.element.set_property("itemIdPath", "key")
        self.element.set_property("itemValuePath", "key")
        self.element.set_property("itemLabelPath", "label")
        if self._allow_custom_value:
            self.element.set_property("allowCustomValue", True)
        if self._required:
            self.element.set_property("required", True)
        # Register client-callable methods via Feature 19
        tree.add_change({
            "node": self.element.node_id,
            "type": "splice",
            "feat": Feature.CLIENT_DELEGATE_HANDLERS,
            "index": 0,
            "add": ["setViewportRange", "resetDataCommunicator", "confirmUpdate"],
        })

        # Init connector
        el_ref = {"@v-node": self.element.node_id}
        tree.queue_execute([
            el_ref,
            "return window.Vaadin.Flow.comboBoxConnector.initLazy($0)"
        ])

        # Register change listener for value selection
        self.element.add_event_listener("change", self._handle_change)

        # Register in tree._components so publishedEventHandler dispatch works
        tree._components[self.element.node_id] = self

        # Push initial data if available
        if self._items:
            self._push_data("")

        # Set selected value if any
        if self._value is not None:
            key = self._find_key_for_item(self._value)
            if key is not None:
                self.element.set_property("selectedItem", {"key": key, "label": self._get_item_label(self._value)})
                self.element.set_property("value", key)

    def _get_item_label(self, item: T) -> str:
        if self._item_label_generator:
            return self._item_label_generator(item)
        return str(item)

    def _find_key_for_item(self, item: T) -> Optional[str]:
        for i, it in enumerate(self._items):
            if it == item:
                return str(i)
        return None

    def _push_data(self, filter_text: str):
        """Push filtered items to the client via connector."""
        if not self._element:
            return
        tree = self._element._tree
        el_ref = {"@v-node": self.element.node_id}

        if self._provider:
            # Use DataProvider — fetch with filter as string
            query = Query(offset=0, limit=self._provider.size(Query(filter=filter_text)), filter=filter_text)
            provider_items = self._provider.fetch(query)
            # Build connector items from provider results
            connector_items = []
            for i, item in enumerate(provider_items):
                connector_items.append({
                    "key": str(i),
                    "label": self._get_item_label(item),
                })
            # Store provider items so value selection works
            self._items = provider_items
        else:
            # Filter items from internal list
            if filter_text:
                filtered = [
                    (i, item) for i, item in enumerate(self._items)
                    if filter_text.lower() in self._get_item_label(item).lower()
                ]
            else:
                filtered = list(enumerate(self._items))

            # Build connector items
            connector_items = []
            for i, item in filtered:
                connector_items.append({
                    "key": str(i),
                    "label": self._get_item_label(item),
                })

        size = len(connector_items)

        # updateSize
        tree.queue_execute([
            el_ref, size,
            "return $0.$connector.updateSize($1)",
        ])

        # set items at index 0
        tree.queue_execute([
            el_ref, 0, connector_items, filter_text,
            "return $0.$connector.set($1, $2, $3)",
        ])

        # confirm update
        self._update_id += 1
        tree.queue_execute([
            el_ref, self._update_id, filter_text,
            "return $0.$connector.confirm($1, $2)",
        ])

        # Update size property
        self.element.set_property("size", size)

    def set_items(self, *items: T):
        """Set the items for the combo box."""
        self._clear_provider()
        self._items = list(items)
        if self._element:
            self._push_data("")

    def set_data_provider(self, provider: DataProvider):
        """Set a DataProvider for the combo box.

        The provider's fetch/size will be used instead of the internal items list.
        """
        self._clear_provider()
        self._provider = provider
        self._provider_listener_unsub = provider.add_data_provider_listener(
            lambda e: self._push_data("")
        )
        if self._element:
            self._push_data("")

    def _clear_provider(self):
        """Unsubscribe from previous DataProvider."""
        if self._provider_listener_unsub:
            self._provider_listener_unsub()
            self._provider_listener_unsub = None
        self._provider = None

    def get_items(self) -> list[T]:
        return self._items.copy()

    def get_value(self) -> Optional[T]:
        return self._value

    def set_value(self, value: Optional[T]):
        self._value = value
        if self._element:
            if value is not None:
                key = self._find_key_for_item(value)
                if key is not None:
                    self.element.set_property("selectedItem", {"key": key, "label": self._get_item_label(value)})
                    self.element.set_property("value", key)
            else:
                self.element.set_property("selectedItem", None)
                self.element.set_property("value", "")

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

    def set_page_size(self, page_size: int):
        self._page_size = page_size
        if self._element:
            self.element.set_property("pageSize", page_size)

    def set_allow_custom_value(self, allow: bool):
        self._allow_custom_value = allow
        if self._element:
            self.element.set_property("allowCustomValue", allow)

    def set_required(self, required: bool):
        self._required = required
        if self._element:
            self.element.set_property("required", required)

    def set_item_label_generator(self, generator: Callable[[T], str]):
        self._item_label_generator = generator

    def add_value_change_listener(self, listener: Callable):
        self._change_listeners.append(listener)

    def add_custom_value_set_listener(self, listener: Callable):
        self._custom_value_listeners.append(listener)

    def _handle_change(self, event_data: dict):
        value_str = event_data.get("value", "")
        if value_str:
            try:
                idx = int(value_str)
                if 0 <= idx < len(self._items):
                    self._value = self._items[idx]
                else:
                    self._value = None
            except (ValueError, IndexError):
                self._value = None
        else:
            self._value = None
        for listener in self._change_listeners:
            listener(event_data)

    # --- Client-callable methods (publishedEventHandler RPC) ---

    def set_viewport_range(self, start: int, length: int, filter_text: str = ""):
        """Called by client when the dropdown viewport changes or user types a filter."""
        self._push_data(filter_text)

    def reset_data_communicator(self):
        """Called by client to reset the data communicator."""
        pass

    def confirm_update(self, update_id: int):
        """Called by client to confirm a data update was applied."""
        pass

    def _sync_property(self, name: str, value):
        if name == "value":
            if value:
                try:
                    idx = int(value)
                    if 0 <= idx < len(self._items):
                        self._value = self._items[idx]
                    else:
                        self._value = None
                except (ValueError, IndexError):
                    self._value = None
            else:
                self._value = None
