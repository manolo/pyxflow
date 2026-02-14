"""Grid component."""

import json
import re
from typing import Callable, TYPE_CHECKING, Any

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature
from vaadin.flow.components.renderer import Renderer, LitRenderer, ComponentRenderer
from vaadin.flow.components.constants import (
    SortDirection, SelectionMode, ColumnTextAlign, GridVariant, GridDropMode,
)
from vaadin.flow.data.provider import DataProvider, ListDataProvider, Query
from vaadin.flow.server.uidl_handler import _ITEM_CLICK_HASH

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


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


class Column:
    """Represents a grid column."""

    def __init__(self, internal_id: str, property_name: str, header: str = ""):
        self._internal_id = internal_id
        self._property_name = property_name
        self._header = header or self._auto_header(property_name)
        self._width = None
        self._flex_grow = None
        self._auto_width = False
        self._resizable = False
        self._sortable = False
        self._text_align: str | None = None
        self._element = None
        self._node = None
        self._renderer: Renderer | None = None
        self._footer_text: str | None = None
        self._frozen = False
        self._frozen_to_end = False
        self._visible = True
        self._key: str | None = None

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

    @staticmethod
    def _auto_header(name: str) -> str:
        """Generate header from property name: 'firstName' → 'First Name'."""
        spaced = re.sub(r"([a-z])([A-Z])", r"\1 \2", name).replace("_", " ")
        return spaced.title()

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

    def set_text_align(self, align: "ColumnTextAlign | str") -> "Column":
        """Set column text alignment ('start', 'center', 'end')."""
        self._text_align = align
        if self._node:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "textAlign", align)
        return self

    def set_renderer(self, renderer: Renderer) -> "Column":
        """Set a renderer for this column."""
        self._renderer = renderer
        return self

    def set_footer_text(self, text: str) -> "Column":
        """Set the column footer text."""
        self._footer_text = text
        return self

    def set_frozen(self, frozen: bool) -> "Column":
        """Set whether the column is frozen (sticky to start)."""
        self._frozen = frozen
        if self._node:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "frozen", frozen)
        return self

    def set_frozen_to_end(self, frozen: bool) -> "Column":
        """Set whether the column is frozen to the end (sticky to end)."""
        self._frozen_to_end = frozen
        if self._node:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "frozenToEnd", frozen)
        return self

    def set_visible(self, visible: bool) -> "Column":
        """Set column visibility."""
        self._visible = visible
        if self._node:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "hidden", not visible)
        return self

    def is_visible(self) -> bool:
        return self._visible

    def set_key(self, key: str) -> "Column":
        """Set a key for identifying this column."""
        self._key = key
        return self

    def get_key(self) -> str | None:
        return self._key

    def _create_element(self, tree: "StateTree"):
        """Create the vaadin-grid-column state node."""
        self._node = tree.create_node()
        self._node.attach()
        self._node.put(Feature.ELEMENT_DATA, "tag", "vaadin-grid-column")
        # path tells the grid which property on the item to display
        # Skip path when a renderer is used (renderer provides its own content)
        if not self._renderer:
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
        if self._text_align:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "textAlign", self._text_align)
        if self._frozen:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "frozen", True)
        if self._frozen_to_end:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "frozenToEnd", True)
        if not self._visible:
            self._node.put(Feature.ELEMENT_PROPERTY_MAP, "hidden", True)
        return self._node


class ColumnGroup:
    """Wraps columns in <vaadin-grid-column-group> for joined headers."""

    def __init__(self, columns: list[Column]):
        self._columns = columns
        self._header_text: str | None = None
        self._node = None

    def _create_element(self, tree: "StateTree"):
        """Create the vaadin-grid-column-group state node."""
        self._node = tree.create_node()
        self._node.attach()
        self._node.put(Feature.ELEMENT_DATA, "tag", "vaadin-grid-column-group")
        return self._node


class HeaderCell:
    """A cell in a header row, backed by a ColumnGroup."""

    def __init__(self, column_group: ColumnGroup):
        self._column_group = column_group

    def set_text(self, text: str) -> "HeaderCell":
        """Set the text content of this header cell."""
        self._column_group._header_text = text
        return self


class HeaderRow:
    """Extra header row above default column headers."""

    def __init__(self, grid: "Grid"):
        self._grid = grid

    def join(self, *columns: Column) -> HeaderCell:
        """Join columns under a single header cell spanning all of them."""
        group = ColumnGroup(list(columns))
        self._grid._column_groups.append(group)
        return HeaderCell(group)


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
        tree._components[self._node.id] = self  # type: ignore[assignment]

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

    _v_fqcn = "com.vaadin.flow.component.grid.Grid"
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
        # Item click listeners
        self._item_click_listeners: list[Callable] = []
        self._item_double_click_listeners: list[Callable] = []
        # Sorting
        self._sort_orders: list[GridSortOrder] = []
        self._sort_listeners: list[Callable] = []
        self._multi_sort = False
        # Selection mode
        self._selection_mode = SelectionMode.SINGLE
        self._selection_column: _GridSelectionColumn | None = None
        self._selected_keys: set[str] = set()
        # Header rows / column groups
        self._header_rows: list[HeaderRow] = []
        self._column_groups: list[ColumnGroup] = []
        # Lazy loading
        self._data_provider: Callable | None = None
        self._data_provider_obj: DataProvider | None = None
        self._data_provider_listener_unsub: Callable | None = None
        self._data_provider_size: int = 0

    def set_columns(self, *property_names: str) -> list["Column"]:
        """Set columns from property names, auto-generating Title Case headers.

        Removes any existing columns first.

        Usage::

            grid.set_columns("name", "email", "role")
            # equivalent to:
            # grid.add_column("name", header="Name")
            # grid.add_column("email", header="Email")
            # grid.add_column("role", header="Role")
        """
        self._columns.clear()
        columns = [self.add_column(name) for name in property_names]
        for col in columns:
            col.set_auto_width(True)
        return columns

    def add_column(self, arg: "str | Renderer", header: str = "") -> Column:
        """Add a column to the grid.

        Args:
            arg: Either a property name (str) or a Renderer instance.
            header: Column header text. Defaults to property_name for str columns.

        Returns:
            The created Column for further configuration.
        """
        internal_id = f"col{len(self._columns)}"
        if isinstance(arg, Renderer):
            column = Column(internal_id, property_name="", header=header)
            column._renderer = arg
        else:
            column = Column(internal_id, arg, header)
        self._columns.append(column)
        return column

    @property
    def columns(self) -> list[Column]:
        """Get the list of columns."""
        return list(self._columns)

    def prepend_header_row(self) -> HeaderRow:
        """Add an extra header row above the default column headers."""
        row = HeaderRow(self)
        self._header_rows.append(row)
        return row

    def set_items(self, items):
        """Set the data items (in-memory mode).

        Args:
            items: A list of dicts, or a ListDataProvider.
        Clears any data provider.
        """
        if isinstance(items, ListDataProvider):
            self.set_data_provider(items)
            return
        self._data_provider = None
        self._clear_data_provider_obj()
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

    # --- Column Operations ---

    def get_column_by_key(self, key: str) -> Column | None:
        """Get a column by its key."""
        for col in self._columns:
            if col._key == key:
                return col
        return None

    def remove_column(self, column: Column):
        """Remove a column from the grid."""
        if column in self._columns:
            self._columns.remove(column)
            # Clear any sorts on this column
            self._sort_orders = [o for o in self._sort_orders if o.column is not column]
            # Remove from DOM if attached
            if self._element and column._node:
                self.element.node.remove_child(column._node)

    def remove_all_columns(self):
        """Remove all columns from the grid."""
        for col in list(self._columns):
            self.remove_column(col)

    def add_component_column(self, component_provider: Callable) -> Column:
        """Add a column that renders a component for each row.

        Args:
            component_provider: A function that takes an item dict and returns a Component.

        Returns:
            The created Column.
        """
        renderer = ComponentRenderer(component_provider)
        return self.add_column(renderer)

    # --- All Rows Visible ---

    def set_all_rows_visible(self, all_rows_visible: bool):
        """Set whether all rows should be visible (no virtual scrolling)."""
        self._all_rows_visible = all_rows_visible
        if self._element:
            self.element.set_property("allRowsVisible", all_rows_visible)

    def is_all_rows_visible(self) -> bool:
        return getattr(self, "_all_rows_visible", False)

    # --- Scroll ---

    def scroll_to_index(self, index: int):
        """Scroll to a specific row index."""
        if self._element:
            self.element._tree.queue_execute([
                {"@v-node": self.element.node_id}, index,
                "return $0.scrollToIndex($1)",
            ])

    def scroll_to_item(self, item):
        """Scroll to a specific item."""
        for key, it in self._key_to_item.items():
            if it is item or it == item:
                index = int(key)
                if self._element:
                    self.element._tree.queue_execute([
                        {"@v-node": self.element.node_id}, index,
                        "return $0.scrollToIndex($1)",
                    ])
                return

    def recalculate_column_widths(self):
        """Recalculate column widths."""
        if self._element:
            self.element._tree.queue_execute([
                {"@v-node": self.element.node_id},
                "return $0.recalculateColumnWidths()",
            ])

    # --- Header/Footer Rows ---

    def append_header_row(self) -> HeaderRow:
        """Append an extra header row below existing header rows."""
        row = HeaderRow(self)
        self._header_rows.append(row)
        return row

    def append_footer_row(self) -> HeaderRow:
        """Append a footer row."""
        row = HeaderRow(self)
        self._header_rows.append(row)
        return row

    def get_header_rows(self) -> list[HeaderRow]:
        """Get header rows."""
        return self._header_rows

    # --- Empty State ---

    def set_empty_state_text(self, text: str):
        """Set the text to show when the grid has no items."""
        self._empty_state_text = text
        if self._element:
            self.element.set_property("emptyStateText", text)

    def set_empty_state_component(self, component: Component):
        """Set a component to show when the grid has no items."""
        # Store for attach
        self._empty_state_component = component

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

    # --- Item Click ---

    def add_item_click_listener(self, listener: Callable):
        """Add a listener for item click events.

        The listener receives a dict with 'item' key.
        """
        first = not self._item_click_listeners
        self._item_click_listeners.append(listener)
        if first and self._element:
            self.element.add_event_listener("item-click", self._handle_item_click, _ITEM_CLICK_HASH)

    def add_item_double_click_listener(self, listener: Callable):
        """Add a listener for item double-click events.

        The listener receives a dict with 'item' key.
        """
        first = not self._item_double_click_listeners
        self._item_double_click_listeners.append(listener)
        if first and self._element:
            self.element.add_event_listener("item-double-click", self._handle_item_double_click, _ITEM_CLICK_HASH)

    def _handle_item_click(self, event_data: dict):
        """Handle item-click event from grid connector."""
        item = self._resolve_item_from_event(event_data)
        if item is not None:
            for listener in self._item_click_listeners:
                listener({"item": item})

    def _handle_item_double_click(self, event_data: dict):
        """Handle item-double-click event from grid connector."""
        item = self._resolve_item_from_event(event_data)
        if item is not None:
            for listener in self._item_double_click_listeners:
                listener({"item": item})

    def _resolve_item_from_event(self, event_data: dict) -> dict | None:
        """Resolve item from event data containing itemKey."""
        key = event_data.get("event.detail.itemKey")
        if key is not None:
            return self._key_to_item.get(str(key))
        return None

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

    def select_item(self, item):
        """Programmatically select an item by its object reference."""
        for key, it in self._key_to_item.items():
            if it is item or it == item:
                self.select(key)
                return

    # --- Lazy Loading ---

    def set_data_provider(self, provider):
        """Set a data provider.

        Args:
            provider: A DataProvider instance, or a callable(offset, limit, sort_orders) -> (items, total_count).
        Clears any in-memory items.
        """
        self._clear_data_provider_obj()
        if isinstance(provider, DataProvider):
            self._data_provider_obj = provider
            self._data_provider = None
            self._data_provider_listener_unsub = provider.add_data_provider_listener(
                self._on_data_provider_change
            )
        elif callable(provider):
            self._data_provider = provider
            self._data_provider_obj = None
        self._items = []
        self._key_to_item.clear()
        self._selected_keys.clear()
        if self._element:
            self._fetch_and_push(0, self._page_size)

    def _clear_data_provider_obj(self):
        """Unsubscribe from previous DataProvider listener."""
        if self._data_provider_listener_unsub:
            self._data_provider_listener_unsub()
            self._data_provider_listener_unsub = None
        self._data_provider_obj = None

    def _on_data_provider_change(self, event: dict):
        """Called when the DataProvider notifies of a change."""
        if not self._element:
            return
        dp = self._data_provider_obj
        if dp and dp.is_in_memory:
            # Re-fetch all data and push
            query = Query(offset=0, limit=dp.size(Query()), sort_orders=self._sort_orders)
            items = dp.fetch(query)
            self._items = items
            self._push_data()
        else:
            self._fetch_and_push(0, self._page_size)

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        # Set grid properties
        self.element.set_property("pageSize", self._page_size)
        if self._column_reordering_allowed:
            self.element.set_property("columnReorderingAllowed", True)
        if self._multi_sort:
            self.element.set_property("multiSort", True)
        if getattr(self, "_all_rows_visible", False):
            self.element.set_property("allRowsVisible", True)
        if getattr(self, "_rows_draggable", False):
            self.element.set_property("rowsDraggable", True)
        if getattr(self, "_drop_mode", None):
            mode = self._drop_mode
            self.element.set_property("dropMode", mode.value if hasattr(mode, 'value') else mode)
        if getattr(self, "_empty_state_text", None):
            self.element.set_property("emptyStateText", self._empty_state_text)
        if getattr(self, "_details_visible_on_click", True) is False:
            self.element.set_property("__disallowDetailsOnClick", True)

        # Create selection column if multi-select
        if self._selection_mode == SelectionMode.MULTI:
            self._selection_column = _GridSelectionColumn(self)
            sel_node = self._selection_column._create_element(tree)
            self.element.node.add_child(sel_node)

        # Create column elements
        for col in self._columns:
            col._create_element(tree)

        if self._column_groups:
            # Build column-to-group mapping
            col_to_group: dict[int, ColumnGroup] = {}
            for group in self._column_groups:
                for c in group._columns:
                    col_to_group[id(c)] = group

            # Create group nodes and add grouped columns as their children
            for group in self._column_groups:
                group._create_element(tree)
                for c in group._columns:
                    group._node.add_child(c._node)

            # Add groups and ungrouped columns to the grid in column order
            added_groups: set[int] = set()
            for col in self._columns:
                group = col_to_group.get(id(col))
                if group:
                    if id(group) not in added_groups:
                        self.element.node.add_child(group._node)
                        added_groups.add(id(group))
                else:
                    self.element.node.add_child(col._node)
        else:
            # No groups — all columns directly on grid
            for col in self._columns:
                self.element.node.add_child(col._node)

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

        # 3. setHeaderRenderer for column groups (spanning header)
        for group in self._column_groups:
            if group._header_text and group._node:
                group_ref = {"@v-node": group._node.id}
                tree.queue_execute([
                    grid_ref, group_ref, group._header_text,
                    "return $0.$connector.setHeaderRenderer($1, { content: $2 })",
                ])

        # 3a. setHeaderRenderer for each column
        for col in self._columns:
            assert col._node is not None
            col_ref = {"@v-node": col._node.id}
            show_sorter = "true" if col._sortable else "false"
            sorter_path = f"'{col.internal_id}'" if col._sortable else "null"
            tree.queue_execute([
                grid_ref, col_ref, col._header,
                f"return $0.$connector.setHeaderRenderer($1, {{ content: $2, showSorter: {show_sorter}, sorterPath: {sorter_path} }})",
            ])

        # 3b. setFooterRenderer for columns with footer text
        for col in self._columns:
            if col._footer_text:
                col_ref = {"@v-node": col._node.id}
                tree.queue_execute([
                    grid_ref, col_ref, col._footer_text,
                    "return $0.$connector.setFooterRenderer($1, { content: $2 })",
                ])

        # 3c. Set up renderers for columns that have one
        for col in self._columns:
            if col._renderer:
                self._setup_renderer(tree, col)

        # 4. Register item click event listeners
        if self._item_click_listeners:
            self.element.add_event_listener("item-click", self._handle_item_click, _ITEM_CLICK_HASH)
        if self._item_double_click_listeners:
            self.element.add_event_listener("item-double-click", self._handle_item_double_click, _ITEM_CLICK_HASH)

        # 5. Push initial data if available
        if self._data_provider_obj:
            dp = self._data_provider_obj
            if dp.is_in_memory:
                query = Query(offset=0, limit=dp.size(Query()), sort_orders=self._sort_orders)
                self._items = dp.fetch(query)
                self._push_data()
            else:
                self._fetch_and_push(0, self._page_size)
        elif self._data_provider:
            self._fetch_and_push(0, self._page_size)
        elif self._items:
            self._push_data()

    def _setup_renderer(self, tree: "StateTree", col: Column):
        """Set up a renderer on a column (called during _attach)."""
        renderer = col._renderer
        assert col._node is not None
        grid_ref = {"@v-node": self.element.node_id}
        col_ref = {"@v-node": col._node.id}

        if isinstance(renderer, LitRenderer):
            template = renderer._template
            renderer_name = "renderer"

            # Build client-callable function names list
            client_callables = list(renderer._functions.keys())

            # Register return channel for function callbacks
            if client_callables:
                channel_id = tree.register_return_channel(
                    self.element.node_id,
                    lambda args, r=renderer: self._handle_renderer_callback(args, r),
                )
                return_channel = {"@v-return": [self.element.node_id, channel_id]}
            else:
                return_channel = None

            tree.queue_execute([
                col_ref, renderer_name, template,
                return_channel, client_callables,
                renderer._namespace, tree._app_id,
                "return window.Vaadin.setLitRenderer($0, $1, $2, $3, $4, $5, $6)",
            ])

        elif isinstance(renderer, ComponentRenderer):
            template = "${Vaadin.FlowComponentHost.getNode(appId, item.nodeid)}"
            renderer_name = "renderer"
            client_callables = []

            # Create container div — virtual child of the column, regular parent of components
            container_node = tree.create_node()
            container_node.attach()
            container_node.put(Feature.ELEMENT_DATA, "tag", "div")
            # Mark as in-memory virtual child (required by FlowClient)
            container_node.put(Feature.ELEMENT_DATA, "payload", {"type": "inMemory"})
            # Add container as virtual child of the column
            tree.add_change({
                "node": col._node.id,
                "type": "splice",
                "feat": Feature.VIRTUAL_CHILDREN_LIST,
                "index": 0,
                "addNodes": [container_node.id],
            })
            renderer._container_node = container_node  # type: ignore[assignment]

            # appId must match the client registry key ("ROOT"), not the full
            # app ID ("ROOT-NNNNNNN"), because getNode() looks up
            # Vaadin.Flow.clients[appId].getByNodeId(nodeId).
            client_key = tree._app_id.split("-")[0]

            tree.queue_execute([
                col_ref, renderer_name, template,
                None, client_callables,
                renderer._namespace, client_key,
                "return window.Vaadin.setLitRenderer($0, $1, $2, $3, $4, $5, $6)",
            ])

            # Patch virtual container on the CONTAINER div, not the column
            container_ref = {"@v-node": container_node.id}
            tree.queue_execute([
                container_ref,
                "return (async function() { Vaadin.FlowComponentHost.patchVirtualContainer(this) }).apply($0)",
            ])

    def _handle_renderer_callback(self, args: list, renderer: LitRenderer):
        """Handle a return channel callback from a LitRenderer function."""
        if len(args) >= 2:
            handler_name = args[0]
            item_key = str(args[1])
            item = self._key_to_item.get(item_key)
            if item and handler_name in renderer._functions:
                renderer._functions[handler_name](item)

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
        tree = self.element._tree
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
                if col._renderer:
                    self._add_renderer_data(tree, col, connector_item, item, key)
                else:
                    connector_item[col.internal_id] = item.get(col.property_name, "")
            connector_items.append(connector_item)

        if selected_item_ids:
            self._selected_keys = new_selected

        self._update_id += 1

        # Push data as a single atomic script to prevent intermediate renders.
        # reset() clears both the connector page cache AND the DataProvider
        # rootCache.  Combined into one script so the grid can't re-render
        # between reset() and updateSize().
        tree.queue_execute([
            grid_ref, len(connector_items), connector_items, self._update_id,
            "$0.$connector.reset();"
            "$0.$connector.updateSize($1);"
            "if($2.length)$0.$connector.set(0,$2);"
            "$0.$connector.confirm($3)",
        ])

    def _add_renderer_data(self, tree: "StateTree", col: Column, connector_item: dict, item: dict, key: str):
        """Add renderer-specific data to a connector item."""
        renderer = col._renderer
        assert renderer is not None
        ns = renderer._namespace

        if isinstance(renderer, LitRenderer):
            for prop_name, provider in renderer._properties.items():
                connector_item[ns + prop_name] = provider(item)

        elif isinstance(renderer, ComponentRenderer):
            # Create or reuse component for this item
            if key not in renderer._components:
                component = renderer._factory(item)
                component._attach(tree)
                # Add as regular child of the container div
                assert renderer._container_node is not None
                renderer._container_node.add_child(component.element.node)
                renderer._components[key] = component
            component = renderer._components[key]
            connector_item[ns + "nodeid"] = component.element.node_id

    def _apply_sort_and_push(self):
        """Apply current sort orders and re-push data."""
        if self._data_provider_obj:
            dp = self._data_provider_obj
            if dp.is_in_memory:
                query = Query(offset=0, limit=dp.size(Query()), sort_orders=self._sort_orders)
                self._items = dp.fetch(query)
                self._push_data()
            else:
                self._reset_connector()
                self._key_to_item.clear()
                self._fetch_and_push(0, self._page_size)
        elif self._data_provider:
            self._reset_connector()
            self._key_to_item.clear()
            self._fetch_and_push(0, self._page_size)
        else:
            self._push_data()

    def _reset_connector(self):
        """Reset the client-side connector cache so it re-requests data."""
        if not self._element:
            return
        tree = self.element._tree
        grid_ref = {"@v-node": self.element.node_id}
        tree.queue_execute([
            grid_ref,
            "return $0.$connector.reset()",
        ])

    def _update_sorter_directions(self):
        """Send sorter direction updates to the client."""
        if not self._element:
            return
        tree = self.element._tree
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
        if not self._element:
            return
        if not self._data_provider and not self._data_provider_obj:
            return
        tree = self.element._tree
        grid_ref = {"@v-node": self.element.node_id}

        if self._data_provider_obj:
            dp = self._data_provider_obj
            query = Query(offset=offset, limit=limit, sort_orders=self._sort_orders)
            items = dp.fetch(query)
            total = dp.size(Query(sort_orders=self._sort_orders))
        else:
            assert self._data_provider is not None
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
                if col._renderer:
                    self._add_renderer_data(tree, col, connector_item, item, key)
                else:
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
            self._selection_column._update_select_all_state(self.element._tree)
        self._push_data()
        self._fire_selection_event()

    def _deselect_all_items(self):
        """Deselect all items (internal, called by selection column)."""
        self._selected_keys.clear()
        if self._selection_column:
            self._selection_column._update_select_all_state(self.element._tree)
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

    def select(self, key: str | None):
        """Select an item by key, or deselect if None."""
        if key is None:
            self.deselect(None)
            return
        item = self._key_to_item.get(key)
        if self._selection_mode == SelectionMode.MULTI:
            self._selected_keys.add(key)
            if self._selection_column:
                self._selection_column._update_select_all_state(self.element._tree)
            self._fire_selection_event()
        else:
            self._selected_item = item
            for listener in self._selection_listeners:
                listener({"item": item})

    def deselect(self, key: str | None):
        """Called by client when user deselects an item."""
        if self._selection_mode == SelectionMode.MULTI:
            if key is not None:
                self._selected_keys.discard(key)
            if self._selection_column:
                self._selection_column._update_select_all_state(self.element._tree)
            self._fire_selection_event()
        else:
            if self._selected_item is None:
                return  # Already deselected, avoid re-entrant loops
            self._selected_item = None
            for listener in self._selection_listeners:
                listener({"item": None})

    def confirm_update(self, update_id: int):
        """Called by client to confirm a data update was applied."""
        pass

    def set_viewport_range(self, start: int, length: int):
        """Called by client when visible range changes."""
        if self._data_provider or self._data_provider_obj:
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

    def set_details_visible_on_click(self, visible: bool):
        """Set whether item details open when clicking a row."""
        self._details_visible_on_click = visible
        if self._element:
            self.element.set_property("__disallowDetailsOnClick", not visible)

    def set_requested_range(self, start: int, length: int):
        """Called by client to request a data range."""
        if self._data_provider or self._data_provider_obj:
            self._fetch_and_push(start, length)

    # --- Drag and Drop ---

    def set_rows_draggable(self, draggable: bool):
        """Set whether rows can be dragged."""
        self._rows_draggable = draggable
        if self._element:
            self.element.set_property("rowsDraggable", draggable)

    def is_rows_draggable(self) -> bool:
        return getattr(self, "_rows_draggable", False)

    def set_drop_mode(self, mode: "GridDropMode | str | None"):
        """Set the drop mode for drag-and-drop."""
        self._drop_mode = mode
        if self._element:
            self.element.set_property("dropMode", mode.value if hasattr(mode, 'value') else mode)

    def get_drop_mode(self):
        return getattr(self, "_drop_mode", None)

    def add_theme_variants(self, *variants: GridVariant):
        """Add theme variants to the grid."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: GridVariant):
        """Remove theme variants from the grid."""
        self.remove_theme_name(*variants)


class TreeGrid(Grid):
    """A hierarchical data grid that displays tree-structured data.

    Each row can be expanded/collapsed to show/hide child items.
    Uses the same gridConnector as Grid, with tree-level overrides
    injected as inline JS (the treeGridConnector is not in the bundle).
    """

    _v_fqcn = "com.vaadin.flow.component.treegrid.TreeGrid"

    def __init__(self):
        super().__init__()
        self._hierarchy_column: Column | None = None
        self._root_items: list = []
        self._children_provider: Callable | None = None
        self._expanded_item_ids: set[int] = set()  # id(original_item)
        self._key_to_original: dict[str, object] = {}  # key -> original item

    def add_hierarchy_column(self, value_provider: Callable, header: str = "Name") -> Column:
        """Add the hierarchy column with expand/collapse toggles.

        Uses vaadin-grid-tree-toggle with Lit property bindings (dot prefix).
        The @click handler calls the server to toggle expansion — the grid
        web component does NOT auto-detect tree toggles, so this is required
        (matching the Java TreeGrid approach exactly).

        Args:
            value_provider: Function that takes an item and returns the display text.
            header: Column header text.

        Returns:
            The created Column.
        """
        # Use .prop=${} (Lit property binding) — NOT attr="${}" (attribute binding).
        # Attribute "leaf=false" is truthy in HTML; property .leaf=${false} is correct.
        # model.expanded/level come from grid's row model (__getRowLevel, _isExpanded).
        # @click=${onClick} triggers server-side toggle (same as Java TreeGrid).
        template = (
            '<vaadin-grid-tree-toggle '
            '@click=${onClick} '
            '.leaf=${!item.children} '
            '.expanded=${live(model.expanded)} '
            '.level=${model.level}>'
            '${item.name}'
            '</vaadin-grid-tree-toggle>'
        )
        renderer = LitRenderer(template)
        renderer.with_property("name", value_provider)
        renderer.with_property("children", lambda item: item.get("_has_children", False))
        renderer.with_function("onClick", self._on_toggle_click)
        col = self.add_column(renderer, header=header)
        self._hierarchy_column = col
        return col

    def set_items(self, items, children_provider: Callable | None = None):
        """Set tree data with a hierarchy defined by children_provider.

        Args:
            items: Root-level items (list of dicts).
            children_provider: Function(item) -> list[item] for child items.
                If None, items are displayed flat (like a regular Grid).
        """
        self._root_items = items
        self._children_provider = children_provider
        self._expanded_item_ids.clear()
        self._key_to_original.clear()
        self._items = self._flatten_tree()
        self._key_to_item.clear()
        if self._element:
            self._push_data()

    def expand(self, item):
        """Expand a tree item programmatically."""
        self._expanded_item_ids.add(id(item))
        self._refresh_flat_data()

    def collapse(self, item):
        """Collapse a tree item programmatically."""
        self._expanded_item_ids.discard(id(item))
        self._refresh_flat_data()

    def _on_toggle_click(self, item):
        """Handle @click on vaadin-grid-tree-toggle from LitRenderer callback."""
        if not item.get("_has_children", False):
            return
        # Find the key for this item in _key_to_item (same object by identity)
        for key, val in self._key_to_item.items():
            if val is item:
                original = self._key_to_original.get(key)
                if original is not None:
                    item_id = id(original)
                    if item_id in self._expanded_item_ids:
                        self._expanded_item_ids.discard(item_id)
                    else:
                        self._expanded_item_ids.add(item_id)
                    self._refresh_flat_data()
                return

    def update_expanded_state(self, key: str, expanded: bool):
        """Called by client when user clicks a tree toggle.

        Registered in Feature 19 and called via
        grid.$server.updateExpandedState(key, expanded).
        """
        original = self._key_to_original.get(key)
        if original is None:
            return
        if expanded:
            self._expanded_item_ids.add(id(original))
        else:
            self._expanded_item_ids.discard(id(original))
        self._refresh_flat_data()

    def _refresh_flat_data(self):
        """Re-flatten the tree and push to client."""
        self._items = self._flatten_tree()
        self._key_to_item.clear()
        if self._element:
            self._push_data()

    def _flatten_tree(self) -> list[dict]:
        """DFS traversal of visible items, adding _level, _has_children, _expanded."""
        result: list[dict] = []
        self._key_to_original.clear()

        def visit(items, level):
            for item in items:
                children = self._children_provider(item) if self._children_provider else []
                has_children = len(children) > 0
                is_expanded = has_children and id(item) in self._expanded_item_ids

                key = str(len(result))
                self._key_to_original[key] = item

                flat_item = dict(item)
                flat_item["_level"] = level
                flat_item["_has_children"] = has_children
                flat_item["_expanded"] = is_expanded
                result.append(flat_item)

                if is_expanded:
                    visit(children, level + 1)

        visit(self._root_items, 0)
        return result

    def _push_data(self):
        """Push flattened tree data to the client via execute commands."""
        tree = self.element._tree
        grid_ref = {"@v-node": self.element.node_id}

        # Build items array for the connector
        connector_items = []
        self._key_to_item.clear()
        for i, item in enumerate(self._items):
            key = str(i)
            self._key_to_item[key] = item
            connector_item = {"key": key, "selected": False}
            # Add tree properties for the gridConnector
            connector_item["children"] = item.get("_has_children", False)
            connector_item["expanded"] = item.get("_expanded", False)
            connector_item["level"] = item.get("_level", 0)
            for col in self._columns:
                if col._renderer:
                    self._add_renderer_data(tree, col, connector_item, item, key)
                else:
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

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        # Register updateExpandedState in Feature 19 (called by expandItem/collapseItem)
        tree.add_change({
            "node": self.element.node_id,
            "type": "splice",
            "feat": Feature.CLIENT_DELEGATE_HANDLERS,
            "index": 0,
            "add": ["updateExpandedState"],
        })

        # Inject tree grid overrides (treeGridConnector is not in the bundle).
        # expandItem/collapseItem call $server.updateExpandedState(key, expanded)
        # matching the Java treeGridConnector behavior exactly.
        grid_ref = {"@v-node": self.element.node_id}
        tree.queue_execute([
            grid_ref,
            "return (async function() {"
            "  var g = $0;"
            "  g.__getRowLevel = function(row) { return row._item && row._item.level != null ? row._item.level : 0 };"
            "  g._isExpanded = function(item) { return !!(item && item.expanded) };"
            "  g.expandItem = function(item) { if (item !== undefined) g.$server.updateExpandedState(g.getItemId(item), true) };"
            "  g.collapseItem = function(item) { if (item !== undefined) g.$server.updateExpandedState(g.getItemId(item), false) };"
            "}).apply(null, [$0])",
        ])
