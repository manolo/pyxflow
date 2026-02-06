"""Grid component."""

import json
from typing import Callable, TYPE_CHECKING, Any

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class Column:
    """Represents a grid column."""

    def __init__(self, internal_id: str, property_name: str, header: str = ""):
        self._internal_id = internal_id
        self._property_name = property_name
        self._header = header or property_name
        self._width = None
        self._flex_grow = None
        self._auto_width = False
        self._element = None
        self._node = None

    @property
    def internal_id(self) -> str:
        return self._internal_id

    @property
    def property_name(self) -> str:
        return self._property_name

    def set_header(self, header: str) -> "Column":
        """Set the column header text."""
        self._header = header
        return self

    def get_header(self) -> str:
        return self._header

    def set_width(self, width: str) -> "Column":
        """Set column width (e.g., '200px')."""
        self._width = width
        if self._node:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "width", width)
        return self

    def set_flex_grow(self, flex_grow: int) -> "Column":
        """Set column flex grow factor."""
        self._flex_grow = flex_grow
        if self._node:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "flexGrow", flex_grow)
        return self

    def set_auto_width(self, auto_width: bool) -> "Column":
        """Set whether column auto-sizes to content."""
        self._auto_width = auto_width
        if self._node:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "autoWidth", auto_width)
        return self

    def _create_element(self, tree: "StateTree"):
        """Create the vaadin-grid-column state node."""
        self._node = tree.create_node()
        self._node.attach()
        self._node.put(Feature.ELEMENT_DATA, "tag", "vaadin-grid-column")
        # path tells the grid which property on the item to display
        self._node.put(Feature.ELEMENT_PROPERTY_MAP, "path", self._internal_id)
        self._node.put(Feature.ELEMENT_PROPERTY_MAP, "_flowId", self._internal_id)
        if self._width:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "width", self._width)
        if self._flex_grow is not None:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "flexGrow", self._flex_grow)
        if self._auto_width:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "autoWidth", True)
        return self._node


class Grid(Component):
    """A data grid component.

    Displays tabular data with columns. Data is pushed to the client
    via the gridConnector's $connector methods.
    """

    _tag = "vaadin-grid"

    def __init__(self):
        super().__init__()
        self._columns: list[Column] = []
        self._items: list[dict] = []
        self._page_size = 50
        self._selection_listeners: list[Callable] = []
        self._selected_item: dict | None = None
        self._key_to_item: dict[str, dict] = {}
        self._update_id = 0

    def add_column(self, property_name: str, header: str = "") -> Column:
        """Add a column to the grid.

        Args:
            property_name: Key in the item dict to display.
            header: Column header text. Defaults to property_name.

        Returns:
            The created Column for further configuration.
        """
        internal_id = f"col{len(self._columns)}"
        column = Column(internal_id, property_name, header)
        self._columns.append(column)
        return column

    def set_items(self, items: list[dict]):
        """Set the data items.

        Each item should be a dict with keys matching column property_names.
        """
        self._items = items
        self._key_to_item.clear()
        if self._element:
            self._push_data()

    def get_items(self) -> list[dict]:
        """Get the current items."""
        return self._items.copy()

    def add_selection_listener(self, listener: Callable):
        """Add a listener called when selection changes.

        The listener receives a dict with 'item' (the selected item or None).
        """
        self._selection_listeners.append(listener)

    def set_page_size(self, page_size: int):
        """Set the page size for data fetching."""
        self._page_size = page_size

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        # Set grid properties
        self.element.set_property("pageSize", self._page_size)

        # Create column elements as children of the grid
        for col in self._columns:
            col_node = col._create_element(tree)
            self.element.node.add_child(col_node)

        # Register client-callable methods via Feature 19
        client_methods = [
            "select", "deselect", "confirmUpdate",
            "setViewportRange", "sortersChanged",
            "setDetailsVisible", "setRequestedRange",
        ]
        tree.add_change({
            "node": self.element.node_id,
            "type": "splice",
            "feat": Feature.CLIENT_DELEGATE_HANDLERS,
            "index": 0,
            "add": client_methods,
        })

        # Queue execute commands for connector initialization
        grid_ref = {"@v-node": self.element.node_id}

        # 1. initLazy
        tree.queue_execute([
            grid_ref,
            "return (async function() { if ($0) window.Vaadin.Flow.gridConnector.initLazy($0) }).apply(null, [$0])",
        ])

        # 2. setSelectionMode to SINGLE
        tree.queue_execute([
            grid_ref,
            "return (async function() { if (this.$connector) this.$connector.setSelectionMode('SINGLE') }).apply($0)",
        ])

        # 3. setHeaderRenderer for each column
        for col in self._columns:
            col_ref = {"@v-node": col._node.id}
            tree.queue_execute([
                grid_ref, col_ref, col._header,
                "return $0.$connector.setHeaderRenderer($1, { content: $2, showSorter: false, sorterPath: null })",
            ])

        # 4. Push initial data if available
        if self._items:
            self._push_data()

    def _push_data(self):
        """Push item data to the client via execute commands."""
        tree = self._element._tree
        grid_ref = {"@v-node": self.element.node_id}

        # Build items array for the connector
        connector_items = []
        self._key_to_item.clear()
        for i, item in enumerate(self._items):
            key = str(i)
            self._key_to_item[key] = item
            connector_item = {"key": key, "selected": False}
            for col in self._columns:
                connector_item[col.internal_id] = item.get(col.property_name, "")
            connector_items.append(connector_item)

        # updateSize
        tree.queue_execute([
            grid_ref, len(connector_items),
            "return $0.$connector.updateSize($1)",
        ])

        # set items (push all at index 0)
        tree.queue_execute([
            grid_ref, 0, connector_items,
            "return $0.$connector.set($1, $2)",
        ])

        # confirm update
        self._update_id += 1
        tree.queue_execute([
            grid_ref, self._update_id,
            "return $0.$connector.confirm($1)",
        ])

    # --- Client-callable methods (called via publishedEventHandler RPC) ---

    def select(self, key: str):
        """Called by client when user selects an item."""
        item = self._key_to_item.get(key)
        self._selected_item = item
        for listener in self._selection_listeners:
            listener({"item": item})

    def deselect(self, key: str):
        """Called by client when user deselects an item."""
        self._selected_item = None
        for listener in self._selection_listeners:
            listener({"item": None})

    def confirm_update(self, update_id: int):
        """Called by client to confirm a data update was applied."""
        pass

    def set_viewport_range(self, start: int, length: int):
        """Called by client when visible range changes. No-op for in-memory data."""
        pass

    def sorters_changed(self, sorters):
        """Called by client when sort order changes. No-op for MVP."""
        pass

    def set_details_visible(self, key: str):
        """Called by client to toggle details. No-op for MVP."""
        pass

    def set_requested_range(self, start: int, length: int):
        """Called by client to request a data range. No-op for in-memory data."""
        pass
