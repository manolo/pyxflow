"""ListBox and MultiSelectListBox components."""

from typing import Callable, Generic, TypeVar, Optional, Set, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree

T = TypeVar('T')


class ListBox(Component, Generic[T]):
    """A single-select list box component.

    Items are rendered as ``vaadin-item`` child elements.
    Selection is tracked via the ``selected`` property (0-based index).

    Usage::

        lb = ListBox()
        lb.set_items("Item 1", "Item 2", "Item 3")
        lb.add_value_change_listener(lambda e: print(e))
    """

    _v_fqcn = "com.vaadin.flow.component.listbox.ListBox"
    _tag = "vaadin-list-box"

    def __init__(self):
        self._items: list[T] = []
        self._value: Optional[T] = None
        self._item_label_generator: Optional[Callable[[T], str]] = None
        self._item_enabled_provider: Optional[Callable[[T], bool]] = None
        self._change_listeners: list[Callable] = []
        self._item_nodes: list = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        self._create_items(tree)
        self.element.add_event_listener("selected-changed", self._handle_selected_changed)

    def _get_item_label(self, item: T) -> str:
        if self._item_label_generator:
            return self._item_label_generator(item)
        return str(item)

    def _create_items(self, tree: "StateTree"):
        """Create vaadin-item child elements."""
        if not self._items:
            return
        for i, item in enumerate(self._items):
            item_node = tree.create_node()
            item_node.attach()
            item_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-item")

            label = self._get_item_label(item)

            # Add text child node
            text_node = tree.create_node()
            text_node.attach()
            text_node.put(Feature.TEXT_NODE, "text", label)
            item_node.add_child(text_node)

            # Check enabled state
            if self._item_enabled_provider and not self._item_enabled_provider(item):
                item_node.put(Feature.ELEMENT_ATTRIBUTE_MAP, "disabled", "")

            self.element.node.add_child(item_node)
            self._item_nodes.append(item_node)

        # Set selected index if value is set
        if self._value is not None:
            idx = self._find_index(self._value)
            if idx is not None:
                self.element.set_property("selected", idx)

    def _find_index(self, item: T) -> Optional[int]:
        for i, it in enumerate(self._items):
            if it == item:
                return i
        return None

    def set_items(self, *items: T):
        """Set the items for the list box."""
        self._items = list(items)
        if self._element and self._element._tree:
            self._create_items(self._element._tree)

    def get_items(self) -> list[T]:
        return self._items.copy()

    def get_value(self) -> Optional[T]:
        return self._value

    def set_value(self, value: Optional[T]):
        self._value = value
        if self._element:
            if value is not None:
                idx = self._find_index(value)
                if idx is not None:
                    self.element.set_property("selected", idx)
            else:
                self.element.set_property("selected", -1)

    def set_item_label_generator(self, generator: Callable[[T], str]):
        self._item_label_generator = generator

    def set_item_enabled_provider(self, provider: Callable[[T], bool]):
        self._item_enabled_provider = provider

    def add_value_change_listener(self, listener: Callable):
        self._change_listeners.append(listener)

    def _handle_selected_changed(self, event_data: dict):
        """Handle selected-changed event from client.

        The selected property is synced via mSync (_sync_property),
        so this handler is a no-op.
        """
        pass

    def _sync_property(self, name: str, value):
        if name == "selected":
            old_value = self._value
            if value is not None and isinstance(value, (int, float)):
                idx = int(value)
                if 0 <= idx < len(self._items):
                    self._value = self._items[idx]
                else:
                    self._value = None
            else:
                self._value = None
            if self._value != old_value:
                for listener in self._change_listeners:
                    listener({"value": self._value})


class MultiSelectListBox(Component, Generic[T]):
    """A multi-select list box component.

    Items are rendered as ``vaadin-item`` child elements.
    Selection is tracked via the ``selectedValues`` property (array of indices).

    Usage::

        lb = MultiSelectListBox()
        lb.set_items("A", "B", "C")
        lb.add_value_change_listener(lambda e: print(e))
    """

    _v_fqcn = "com.vaadin.flow.component.listbox.MultiSelectListBox"
    _tag = "vaadin-list-box"

    def __init__(self):
        self._items: list[T] = []
        self._value: Set[T] = set()
        self._item_label_generator: Optional[Callable[[T], str]] = None
        self._item_enabled_provider: Optional[Callable[[T], bool]] = None
        self._change_listeners: list[Callable] = []
        self._item_nodes: list = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        self.element.set_property("multiple", True)
        self._create_items(tree)
        self.element.add_event_listener("selected-values-changed", self._handle_selected_changed)

    def _get_item_label(self, item: T) -> str:
        if self._item_label_generator:
            return self._item_label_generator(item)
        return str(item)

    def _create_items(self, tree: "StateTree"):
        """Create vaadin-item child elements."""
        if not self._items:
            return
        for i, item in enumerate(self._items):
            item_node = tree.create_node()
            item_node.attach()
            item_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-item")

            label = self._get_item_label(item)

            text_node = tree.create_node()
            text_node.attach()
            text_node.put(Feature.TEXT_NODE, "text", label)
            item_node.add_child(text_node)

            if self._item_enabled_provider and not self._item_enabled_provider(item):
                item_node.put(Feature.ELEMENT_ATTRIBUTE_MAP, "disabled", "")

            self.element.node.add_child(item_node)
            self._item_nodes.append(item_node)

        # Set selected values
        if self._value:
            indices = []
            for v in self._value:
                for i, it in enumerate(self._items):
                    if it == v:
                        indices.append(i)
                        break
            self.element.set_property("selectedValues", indices)

    def set_items(self, *items: T):
        self._items = list(items)
        if self._element and self._element._tree:
            self._create_items(self._element._tree)

    def get_items(self) -> list[T]:
        return self._items.copy()

    def get_value(self) -> Set[T]:
        return self._value.copy()

    def set_value(self, value: Set[T]):
        self._value = set(value)
        if self._element:
            indices = []
            for v in self._value:
                for i, it in enumerate(self._items):
                    if it == v:
                        indices.append(i)
                        break
            self.element.set_property("selectedValues", indices)

    def set_item_label_generator(self, generator: Callable[[T], str]):
        self._item_label_generator = generator

    def set_item_enabled_provider(self, provider: Callable[[T], bool]):
        self._item_enabled_provider = provider

    def add_value_change_listener(self, listener: Callable):
        self._change_listeners.append(listener)

    def _handle_selected_changed(self, event_data: dict):
        """Handle selected-values-changed event from client.

        The selectedValues property is synced via mSync (_sync_property),
        so this handler is a no-op.
        """
        pass

    def _sync_property(self, name: str, value):
        if name == "selectedValues":
            old_value = self._value.copy()
            self._value = set()
            if isinstance(value, list):
                for idx in value:
                    if isinstance(idx, (int, float)):
                        i = int(idx)
                        if 0 <= i < len(self._items):
                            self._value.add(self._items[i])
            if self._value != old_value:
                for listener in self._change_listeners:
                    listener({"value": self._value})
