"""Grid component."""

import json
from enum import Enum
from typing import Callable, TYPE_CHECKING, Any

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class SortDirection(Enum):
    """Sort direction for grid columns."""
    ASCENDING = "asc"
    DESCENDING = "desc"


class GridSortOrder:
    """Represents a sort order for a grid column."""

    def __init__(self, column: "Column", direction: SortDirection):
        self._column = column
        self._direction = direction

    @property
    def column(self) -> "Column":
        return self._column

    @property
    def direction(self) -> SortDirection:
        return self._direction


class SelectionMode(Enum):
    """Grid selection mode."""
    SINGLE = "SINGLE"
    MULTI = "MULTI"
    NONE = "NONE"


class Column:
    """Represents a grid column."""

    def __init__(self, internal_id: str, property_name: str, header: str = ""):
        self._internal_id = internal_id
        self._property_name = property_name
        self._header = header or property_name
        self._width = None
        self._flex_grow = None
        self._auto_width = False
        self._resizable = False
        self._sortable = False
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

    def set_resizable(self, resizable: bool) -> "Column":
        """Set whether column is resizable by the user."""
        self._resizable = resizable
        if self._node:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "resizable", resizable)
        return self

    def set_sortable(self, sortable: bool) -> "Column":
        """Set whether column is sortable."""
        self._sortable = sortable
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
        if self._resizable:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "resizable", True)
        return self._node


class _GridSelectionColumn:
    """Internal selection column for multi-select mode.

    Creates a vaadin-grid-flow-selection-column node and registers
    publishedEventHandler methods (selectAll, deselectAll).
    Not a Component subclass — registered directly in tree._components
    so _handle_published_event can route calls.
    """

    def __init__(self, grid: "Grid"):
        self._grid = grid
        self._node = None

    def _create_element(self, tree: "StateTree"):
        """Create the selection column node and register it."""
        self._node = tree.create_node()
        self._node.attach()
        self._node.put(Feature.ELEMENT_DATA, "tag", "vaadin-grid-flow-selection-column")
        self._node.put(Feature.ELEMENT_PROPERTY_MAP, "_flowId", "__selection")

        # Register Feature 19 methods for this node
        tree.add_change({
            "node": self._node.id,
            "type": "splice",
            "feat": Feature.CLIENT_DELEGATE_HANDLERS,
            "index": 0,
            "add": ["selectAll", "deselectAll"],
        })

        # Register in tree._components so publishedEventHandler dispatch works
        tree._components[self._node.id] = self

        return self._node

    def select_all(self):
        """Called by client when select-all checkbox is checked."""
        self._grid._select_all_items()

    def deselect_all(self):
        """Called by client when select-all checkbox is unchecked."""
        self._grid._deselect_all_items()

    def _update_select_all_state(self, tree: "StateTree"):
        """Update the select-all checkbox visual state."""
        if not self._node:
            return
        total = len(self._grid._items)
        selected = len(self._grid._selected_keys)
        if selected == 0:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "selectAll", False)
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "_indeterminate", False)
        elif selected >= total:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "selectAll", True)
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "_indeterminate", False)
        else:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "selectAll", False)
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "_indeterminate", True)

    def _sync_property(self, prop, value):
        """Accept property syncs (no-op, satisfies dispatch interface)."""
        pass


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
        self._column_reordering_allowed = False
        # Sorting
        self._sort_orders: list[GridSortOrder] = []
        self._sort_listeners: list[Callable] = []
        self._multi_sort = False
        # Selection mode
        self._selection_mode = SelectionMode.SINGLE
        self._selection_column: _GridSelectionColumn | None = None
        self._selected_keys: set[str] = set()
        # Lazy loading
        self._data_provider: Callable | None = None
        self._data_provider_size: int = 0

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
        """Set the data items (in-memory mode).

        Each item should be a dict with keys matching column property_names.
        Clears any data provider.
        """
        self._data_provider = None
        self._items = items
        self._key_to_item.clear()
        self._selected_keys.clear()
        if self._element:
            self._push_data()

    def get_items(self) -> list[dict]:
        """Get the current items."""
        return self._items.copy()

    def add_selection_listener(self, listener: Callable):
        """Add a listener called when selection changes.

        In SINGLE mode: listener receives {'item': selected_or_none}
        In MULTI mode: listener receives {'item': first_selected_or_none, 'selected_items': set}
        """
        self._selection_listeners.append(listener)

    def set_page_size(self, page_size: int):
        """Set the page size for data fetching."""
        self._page_size = page_size

    # --- Column Reordering ---

    def set_column_reordering_allowed(self, allowed: bool):
        """Set whether the user can reorder columns by dragging."""
        self._column_reordering_allowed = allowed
        if self._element:
            self.element.set_property("columnReorderingAllowed", allowed)

    # --- Sorting ---

    def set_multi_sort(self, enabled: bool):
        """Enable or disable multi-column sorting."""
        self._multi_sort = enabled
        if self._element:
            self.element.set_property("multiSort", enabled)

    def add_sort_listener(self, listener: Callable):
        """Add a listener called when sort order changes.

        The listener receives a list of GridSortOrder objects.
        """
        self._sort_listeners.append(listener)

    def set_sort_order(self, sort_orders: list[GridSortOrder]):
        """Set the sort order programmatically."""
        self._sort_orders = sort_orders
        if self._element:
            self._apply_sort_and_push()
            self._update_sorter_directions()

    # --- Selection Mode ---

    def set_selection_mode(self, mode: SelectionMode):
        """Set the selection mode. Must be called before the grid is attached."""
        self._selection_mode = mode

    def get_selected_items(self) -> list:
        """Get the currently selected items as a list of dicts."""
        if self._selection_mode == SelectionMode.SINGLE:
            return [self._selected_item] if self._selected_item else []
        return [self._key_to_item[k] for k in self._selected_keys if k in self._key_to_item]

    def select_all(self):
        """Programmatically select all items (multi-select only)."""
        if self._selection_mode == SelectionMode.MULTI:
            self._select_all_items()

    def deselect_all(self):
        """Programmatically deselect all items."""
        if self._selection_mode == SelectionMode.MULTI:
            self._deselect_all_items()

    # --- Lazy Loading ---

    def set_data_provider(self, fetch: Callable):
        """Set a lazy data provider.

        Args:
            fetch: A callable(offset, limit, sort_orders) -> (items, total_count)
                   where sort_orders is a list of GridSortOrder.
        Clears any in-memory items.
        """
        self._data_provider = fetch
        self._items = []
        self._key_to_item.clear()
        self._selected_keys.clear()
        if self._element:
            self._fetch_and_push(0, self._page_size)

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        # Set grid properties
        self.element.set_property("pageSize", self._page_size)
        if self._column_reordering_allowed:
            self.element.set_property("columnReorderingAllowed", True)
        if self._multi_sort:
            self.element.set_property("multiSort", True)

        # Create selection column if multi-select
        if self._selection_mode == SelectionMode.MULTI:
            self._selection_column = _GridSelectionColumn(self)
            sel_node = self._selection_column._create_element(tree)
            self.element.node.add_child(sel_node)

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

        # 2. setSelectionMode
        tree.queue_execute([
            grid_ref,
            f"return (async function() {{ if (this.$connector) this.$connector.setSelectionMode('{self._selection_mode.value}') }}).apply($0)",
        ])

        # 3. setHeaderRenderer for each column
        for col in self._columns:
            col_ref = {"@v-node": col._node.id}
            show_sorter = "true" if col._sortable else "false"
            sorter_path = f"'{col.internal_id}'" if col._sortable else "null"
            tree.queue_execute([
                grid_ref, col_ref, col._header,
                f"return $0.$connector.setHeaderRenderer($1, {{ content: $2, showSorter: {show_sorter}, sorterPath: {sorter_path} }})",
            ])

        # 4. Push initial data if available
        if self._data_provider:
            self._fetch_and_push(0, self._page_size)
        elif self._items:
            self._push_data()

    def _sorted_items(self) -> list[dict]:
        """Return items sorted according to current sort orders."""
        items = self._items
        if not self._sort_orders:
            return items
        # Apply sorts in reverse order so primary sort wins (stable sort)
        for order in reversed(self._sort_orders):
            prop = order.column.property_name
            reverse = order.direction == SortDirection.DESCENDING
            items = sorted(items, key=lambda x, p=prop: x.get(p, ""), reverse=reverse)
        return items

    def _push_data(self):
        """Push item data to the client via execute commands."""
        tree = self._element._tree
        grid_ref = {"@v-node": self.element.node_id}

        # Apply sorting
        sorted_items = self._sorted_items()

        # Remap selected keys if in multi-select mode
        # Must happen before clearing _key_to_item
        if self._selection_mode == SelectionMode.MULTI and self._selected_keys:
            selected_item_ids = {id(self._key_to_item[k]) for k in self._selected_keys if k in self._key_to_item}
        else:
            selected_item_ids = set()

        # Build items array for the connector
        connector_items = []
        self._key_to_item.clear()
        new_selected = set()
        for i, item in enumerate(sorted_items):
            key = str(i)
            self._key_to_item[key] = item
            is_selected = id(item) in selected_item_ids
            if is_selected:
                new_selected.add(key)
            connector_item = {"key": key, "selected": is_selected}
            for col in self._columns:
                connector_item[col.internal_id] = item.get(col.property_name, "")
            connector_items.append(connector_item)

        if selected_item_ids:
            self._selected_keys = new_selected

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

    def _apply_sort_and_push(self):
        """Apply current sort orders and re-push data."""
        if self._data_provider:
            self._key_to_item.clear()
            self._fetch_and_push(0, self._page_size)
        else:
            self._push_data()

    def _update_sorter_directions(self):
        """Send sorter direction updates to the client."""
        if not self._element:
            return
        tree = self._element._tree
        grid_ref = {"@v-node": self.element.node_id}
        directions = []
        for order in self._sort_orders:
            directions.append({
                "column": order.column.internal_id,
                "direction": order.direction.value,
            })
        tree.queue_execute([
            grid_ref, directions,
            "return $0.$connector.setSorterDirections($1)",
        ])

    def _fetch_and_push(self, offset: int, limit: int):
        """Fetch data from provider and push to client."""
        if not self._data_provider or not self._element:
            return
        tree = self._element._tree
        grid_ref = {"@v-node": self.element.node_id}

        items, total = self._data_provider(offset, limit, self._sort_orders)
        self._data_provider_size = total

        # Build connector items
        connector_items = []
        for i, item in enumerate(items):
            key = str(offset + i)
            self._key_to_item[key] = item
            selected = key in self._selected_keys
            connector_item = {"key": key, "selected": selected}
            for col in self._columns:
                connector_item[col.internal_id] = item.get(col.property_name, "")
            connector_items.append(connector_item)

        # updateSize
        tree.queue_execute([
            grid_ref, total,
            "return $0.$connector.updateSize($1)",
        ])

        # set items at offset
        tree.queue_execute([
            grid_ref, offset, connector_items,
            "return $0.$connector.set($1, $2)",
        ])

        # confirm update
        self._update_id += 1
        tree.queue_execute([
            grid_ref, self._update_id,
            "return $0.$connector.confirm($1)",
        ])

    # --- Multi-select internal ---

    def _select_all_items(self):
        """Select all items (internal, called by selection column)."""
        self._selected_keys = set(self._key_to_item.keys())
        if self._selection_column:
            self._selection_column._update_select_all_state(self._element._tree)
        self._push_data()
        self._fire_selection_event()

    def _deselect_all_items(self):
        """Deselect all items (internal, called by selection column)."""
        self._selected_keys.clear()
        if self._selection_column:
            self._selection_column._update_select_all_state(self._element._tree)
        self._push_data()
        self._fire_selection_event()

    def _fire_selection_event(self):
        """Fire selection event to all listeners."""
        if self._selection_mode == SelectionMode.MULTI:
            selected_items = self.get_selected_items()
            first = selected_items[0] if selected_items else None
            event = {"item": first, "selected_items": selected_items}
        else:
            event = {"item": self._selected_item}
        for listener in self._selection_listeners:
            listener(event)

    # --- Client-callable methods (called via publishedEventHandler RPC) ---

    def select(self, key: str):
        """Called by client when user selects an item."""
        item = self._key_to_item.get(key)
        if self._selection_mode == SelectionMode.MULTI:
            self._selected_keys.add(key)
            if self._selection_column:
                self._selection_column._update_select_all_state(self._element._tree)
            self._fire_selection_event()
        else:
            self._selected_item = item
            for listener in self._selection_listeners:
                listener({"item": item})

    def deselect(self, key: str):
        """Called by client when user deselects an item."""
        if self._selection_mode == SelectionMode.MULTI:
            self._selected_keys.discard(key)
            if self._selection_column:
                self._selection_column._update_select_all_state(self._element._tree)
            self._fire_selection_event()
        else:
            self._selected_item = None
            for listener in self._selection_listeners:
                listener({"item": None})

    def confirm_update(self, update_id: int):
        """Called by client to confirm a data update was applied."""
        pass

    def set_viewport_range(self, start: int, length: int):
        """Called by client when visible range changes."""
        if self._data_provider:
            self._fetch_and_push(start, length)

    def sorters_changed(self, sorters):
        """Called by client when sort order changes."""
        # Parse sorters - arrives as JSON string or list
        if isinstance(sorters, str):
            sorters = json.loads(sorters)

        # Map to GridSortOrder objects
        col_by_id = {col.internal_id: col for col in self._columns}
        new_orders = []
        for s in sorters:
            path = s.get("path") or s.get("column", "")
            direction_str = s.get("direction", "asc")
            col = col_by_id.get(path)
            if col:
                direction = SortDirection.DESCENDING if direction_str == "desc" else SortDirection.ASCENDING
                new_orders.append(GridSortOrder(col, direction))

        self._sort_orders = new_orders

        # Notify listeners
        for listener in self._sort_listeners:
            listener(new_orders)

        # Re-sort and push data
        self._apply_sort_and_push()

    def set_details_visible(self, key: str):
        """Called by client to toggle details. No-op for now."""
        pass

    def set_requested_range(self, start: int, length: int):
        """Called by client to request a data range."""
        if self._data_provider:
            self._fetch_and_push(start, length)
