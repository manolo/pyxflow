"""MultiSelectComboBox component."""

from typing import Callable, Generic, TypeVar, Optional, Set, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.components.mixins import HasValidation, HasRequired
from vaadin.flow.core.state_node import Feature
from vaadin.flow.data.provider import DataProvider, Query

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree

T = TypeVar('T')


class MultiSelectComboBox(HasValidation, HasRequired, Component, Generic[T]):
    """A combo box with multi-select support.

    Allows users to select multiple values from a filtered dropdown.
    Selected items appear as chips in the input field.
    Uses the same comboBoxConnector as ComboBox.

    Usage::

        cb = MultiSelectComboBox("Skills")
        cb.set_items("Java", "Python", "JavaScript")
        cb.add_value_change_listener(lambda e: print(e))
    """

    _v_fqcn = "com.vaadin.flow.component.combobox.MultiSelectComboBox"
    _tag = "vaadin-multi-select-combo-box"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._items: list[T] = []
        self._value: Set[T] = set()
        self._placeholder = ""
        self._page_size = 50
        self._item_label_generator: Optional[Callable[[T], str]] = None
        self._change_listeners: list[Callable] = []
        self._update_id = 0
        self._provider: DataProvider | None = None
        self._provider_listener_unsub: Callable | None = None

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        if self._label:
            self.element.set_property("label", self._label)
        if self._placeholder:
            self.element.set_property("placeholder", self._placeholder)
        self.element.set_property("pageSize", self._page_size)
        self.element.set_property("itemIdPath", "key")
        self.element.set_property("itemValuePath", "key")
        self.element.set_property("itemLabelPath", "label")

        # Register client-callable methods via Feature 19
        tree.add_change({
            "node": self.element.node_id,
            "type": "splice",
            "feat": Feature.CLIENT_DELEGATE_HANDLERS,
            "index": 0,
            "add": ["setViewportRange", "resetDataCommunicator", "confirmUpdate"],
        })

        # Init connector (same as ComboBox)
        el_ref = {"@v-node": self.element.node_id}
        tree.queue_execute([
            el_ref,
            "return window.Vaadin.Flow.comboBoxConnector.initLazy($0)"
        ])

        # Register change listener for value selection
        self.element.add_event_listener("selected-items-changed", self._handle_selection_changed)

        # Register in tree._components for publishedEventHandler dispatch
        tree._components[self.element.node_id] = self

        # Push initial data
        if self._items:
            self._push_data("")

        # Set initial selected items
        if self._value:
            self._push_selected_items()

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
            query = Query(offset=0, limit=self._provider.size(Query(filter=filter_text)), filter=filter_text)
            provider_items = self._provider.fetch(query)
            connector_items = []
            for i, item in enumerate(provider_items):
                connector_items.append({
                    "key": str(i),
                    "label": self._get_item_label(item),
                })
            self._items = provider_items
        else:
            if filter_text:
                filtered = [
                    (i, item) for i, item in enumerate(self._items)
                    if filter_text.lower() in self._get_item_label(item).lower()
                ]
            else:
                filtered = list(enumerate(self._items))

            connector_items = []
            for i, item in filtered:
                connector_items.append({
                    "key": str(i),
                    "label": self._get_item_label(item),
                })

        size = len(connector_items)

        tree.queue_execute([
            el_ref, size,
            "return $0.$connector.updateSize($1)",
        ])
        tree.queue_execute([
            el_ref, 0, connector_items, filter_text,
            "return $0.$connector.set($1, $2, $3)",
        ])
        self._update_id += 1
        tree.queue_execute([
            el_ref, self._update_id, filter_text,
            "return $0.$connector.confirm($1, $2)",
        ])
        self.element.set_property("size", size)

    def _push_selected_items(self):
        """Push the selectedItems property."""
        if not self._element:
            return
        selected = []
        for item in self._value:
            key = self._find_key_for_item(item)
            if key is not None:
                selected.append({"key": key, "label": self._get_item_label(item)})
        self.element.set_property("selectedItems", selected)

    def set_items(self, *items: T):
        self._clear_provider()
        self._items = list(items)
        if self._element:
            self._push_data("")

    def set_data_provider(self, provider: DataProvider):
        self._clear_provider()
        self._provider = provider
        self._provider_listener_unsub = provider.add_data_provider_listener(
            lambda e: self._push_data("")
        )
        if self._element:
            self._push_data("")

    def _clear_provider(self):
        if self._provider_listener_unsub:
            self._provider_listener_unsub()
            self._provider_listener_unsub = None
        self._provider = None

    def get_items(self) -> list[T]:
        return self._items.copy()

    def get_value(self) -> Set[T]:
        return self._value.copy()

    def set_value(self, value: Set[T]):
        self._value = set(value)
        if self._element:
            self._push_selected_items()

    def select(self, *items: T):
        """Add items to the selection."""
        self._value.update(items)
        if self._element:
            self._push_selected_items()

    def deselect(self, *items: T):
        """Remove items from the selection."""
        self._value -= set(items)
        if self._element:
            self._push_selected_items()

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

    def set_required(self, required: bool):
        self.set_required_indicator_visible(required)

    def set_item_label_generator(self, generator: Callable[[T], str]):
        self._item_label_generator = generator

    def add_value_change_listener(self, listener: Callable):
        self._change_listeners.append(listener)

    def _handle_selection_changed(self, event_data: dict):
        """Handle selected-items-changed from client."""
        # The client sends selected items as JSON array
        selected_items = event_data.get("value", [])
        self._value = set()
        if isinstance(selected_items, list):
            for si in selected_items:
                if isinstance(si, dict):
                    key = si.get("key", "")
                    try:
                        idx = int(key)
                        if 0 <= idx < len(self._items):
                            self._value.add(self._items[idx])
                    except (ValueError, IndexError):
                        pass
        for listener in self._change_listeners:
            listener({"value": self._value})

    # --- Client-callable methods (publishedEventHandler RPC) ---

    def set_viewport_range(self, start: int, length: int, filter_text: str = ""):
        self._push_data(filter_text)

    def reset_data_communicator(self):
        pass

    def confirm_update(self, update_id: int):
        pass

    def _sync_property(self, name: str, value):
        if name == "selectedItems":
            self._value = set()
            if isinstance(value, list):
                for si in value:
                    if isinstance(si, dict):
                        key = si.get("key", "")
                        try:
                            idx = int(key)
                            if 0 <= idx < len(self._items):
                                self._value.add(self._items[idx])
                        except (ValueError, IndexError):
                            pass
