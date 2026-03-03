"""Select component."""

from typing import Callable, Generic, TypeVar, Optional

from pyxflow.core.component import Component
from pyxflow.components.mixins import HasReadOnly, HasValidation, HasRequired
from pyxflow.components.constants import SelectVariant
from pyxflow.core.state_node import Feature

T = TypeVar('T')


class Select(HasReadOnly, HasValidation, HasRequired, Component, Generic[T]):
    """A select dropdown component.

    Allows users to choose a single value from a list of options
    presented in an overlay.
    """

    _v_fqcn = "com.vaadin.flow.component.select.Select"
    _tag = "vaadin-select"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._items: list[T] = []
        self._value: Optional[T] = None
        self._placeholder = ""
        self._item_label_generator: Optional[Callable[[T], str]] = None
        self._change_listeners: list[Callable] = []
        self._list_box = None
        self._empty_selection_allowed = False
        self._empty_selection_caption = ""
        self._empty_item_node = None
        self._empty_text_node = None

    def _attach(self, tree):
        super()._attach(tree)
        if self._label:
            self.element.set_property("label", self._label)
        if self._placeholder:
            self.element.set_property("placeholder", self._placeholder)

        # Create the list-box for items
        self._create_list_box(tree)

        # Initialize the selectConnector (moves list-box into overlay)
        el_ref = {"@v-node": self.element.node.id}
        tree.queue_execute([
            el_ref,
            "return window.Vaadin.Flow.selectConnector.initLazy($0)"
        ])

        # Register value change listener
        self.element.add_event_listener("value-changed", self._handle_value_changed)

    def _create_list_box(self, tree):
        """Create the list-box element with items."""
        if not self._items and not self._empty_selection_allowed:
            return

        # Create vaadin-select-list-box element
        list_box_node = tree.create_node()
        list_box_node.attach()
        list_box_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-select-list-box")

        # Add empty selection item if allowed
        if self._empty_selection_allowed:
            self._add_empty_item(tree, list_box_node)

        # Add items to the list box
        for i, item in enumerate(self._items):
            item_node = tree.create_node()
            item_node.attach()
            item_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-select-item")

            # Create text node for the item label
            text_node = tree.create_node()
            text_node.attach()
            label = self._get_item_label(item)
            text_node.put(Feature.TEXT_NODE, "text", label)

            # Add text to item
            item_node.add_child(text_node)

            # Add item to list box
            list_box_node.add_child(item_node)

        # Add list-box as child of select
        self.element.node.add_child(list_box_node)
        self._list_box = list_box_node

        # Set selected value if any
        if self._value is not None:
            try:
                index = self._items.index(self._value)
                self.element.set_property("value", self._get_item_label(self._value))
            except ValueError:
                pass

    def _add_empty_item(self, tree, list_box_node):
        """Add an empty selection item as first child of the list-box."""
        item_node = tree.create_node()
        item_node.attach()
        item_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-select-item")
        # Set empty value attribute so selecting it deselects
        item_node.put(Feature.ELEMENT_PROPERTY_MAP, "value", "")

        # Add caption text if any
        text_node = tree.create_node()
        text_node.attach()
        text_node.put(Feature.TEXT_NODE, "text", self._empty_selection_caption or "")
        item_node.add_child(text_node)

        list_box_node.add_child(item_node)
        self._empty_item_node = item_node
        self._empty_text_node = text_node

    def _get_item_label(self, item: T) -> str:
        """Get the label for an item."""
        if self._item_label_generator:
            return self._item_label_generator(item)
        return str(item)

    def set_items(self, *items: T):
        """Set the items for the select."""
        # Support both set_items("a", "b") and set_items(["a", "b"])
        if len(items) == 1 and isinstance(items[0], (list, tuple)):
            items = items[0]
        self._items = list(items)
        if self._element and self._element._tree:
            tree = self._element._tree
            # Re-create list box with new items
            self._create_list_box(tree)
            # Tell the client to re-render the overlay content
            el_ref = {"@v-node": self.element.node.id}
            tree.queue_execute([
                el_ref,
                "return $0.requestContentUpdate()"
            ])

    def get_items(self) -> list[T]:
        """Get the items."""
        return self._items.copy()

    def get_value(self) -> Optional[T]:
        """Get the selected value."""
        return self._value

    def set_value(self, value: Optional[T]):
        """Set the selected value."""
        old_value = self._value
        self._value = value
        if self._element and value is not None:
            self.element.set_property("value", self._get_item_label(value))
        elif self._element:
            self.element.set_property("value", "")
        if value != old_value:
            for listener in self._change_listeners:
                listener({"value": value, "from_client": False})

    def set_label(self, label: str):
        """Set the label."""
        self._label = label
        if self._element:
            self.element.set_property("label", label)

    def get_label(self) -> str:
        """Get the label."""
        return self._label

    def set_placeholder(self, placeholder: str):
        """Set the placeholder text."""
        self._placeholder = placeholder
        if self._element:
            self.element.set_property("placeholder", placeholder)

    def get_placeholder(self) -> str:
        """Get the placeholder text."""
        return self._placeholder

    def set_item_label_generator(self, generator: Callable[[T], str]):
        """Set a function to generate labels for items."""
        self._item_label_generator = generator

    def add_value_change_listener(self, listener: Callable):
        """Add a value change listener."""
        self._change_listeners.append(listener)

    def _handle_value_changed(self, event_data: dict):
        """Handle value-changed event from client.

        Value arrives via _sync_property (mSync), not event_data.
        This handler is a no-op — change listeners fire from _sync_property.
        """
        pass

    def set_empty_selection_allowed(self, allowed: bool):
        """Set whether empty (no) selection is allowed.

        When enabled, an empty item is added as the first option in the
        dropdown, allowing the user to deselect the current value.
        """
        self._empty_selection_allowed = allowed
        if self._element and self._element._tree:
            tree = self._element._tree
            if allowed and self._empty_item_node is None and self._list_box is not None:
                self._add_empty_item(tree, self._list_box)
            elif not allowed and self._empty_item_node is not None and self._list_box is not None:
                self._list_box.remove_child(self._empty_item_node)
                self._empty_item_node = None
                self._empty_text_node = None

    def is_empty_selection_allowed(self) -> bool:
        return self._empty_selection_allowed

    def set_empty_selection_caption(self, caption: str):
        """Set the caption shown when no value is selected."""
        self._empty_selection_caption = caption
        if hasattr(self, "_empty_text_node") and self._empty_text_node is not None:
            self._empty_text_node.put(Feature.TEXT_NODE, "text", caption)

    def set_overlay_width(self, width: str):
        """Set the overlay width (e.g. '300px')."""
        if self._element:
            self.element.set_property("overlayWidth", width)

    def set_prefix_component(self, component: Component):
        """Set a prefix component (e.g. an Icon)."""
        self._prefix_component = component
        if self._element:
            tree = self._element._tree
            component._ui = self._ui
            component._parent = self
            component._attach(tree)
            component.element.set_attribute("slot", "prefix")
            self.element.add_child(component.element)

    def add_theme_variants(self, *variants: SelectVariant):
        """Add theme variants to the select."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: SelectVariant):
        """Remove theme variants from the select."""
        self.remove_theme_name(*variants)

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "value":
            old_value = self._value
            # Find the item that matches this label
            matched = None
            for item in self._items:
                if self._get_item_label(item) == value:
                    matched = item
                    break
            # If no item matched and value is empty, preserve "" (deselected)
            # to stay consistent with Binding.clear() which sets value to "".
            self._value = matched if matched is not None else (value if value == "" else None)
            # Fire change listeners
            if self._value != old_value:
                for listener in self._change_listeners:
                    listener({"value": self._value})
