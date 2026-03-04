# TreeGrid

**Category:** Data | Hierarchical data grid

## Constructor

```python
TreeGrid()
```

## Methods

| Method | Description |
|--------|-------------|
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_column(arg: 'str | Renderer', header: str = '') -> pyxflow.comp...` | Add a column to the grid. |
| `add_component_column(component_provider: Callable) -> pyxflow.components.grid...` | Add a column that renders a component for each row. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_hierarchy_column(value_provider: Callable, header: str = 'Name') -> pyxfl...` | Add the hierarchy column with expand/collapse toggles. |
| `add_item_click_listener(listener: Callable)` | Add a listener for item click events. |
| `add_item_double_click_listener(listener: Callable)` | Add a listener for item double-click events. |
| `add_selection_listener(listener: Callable)` | Add a listener called when selection changes. |
| `add_sort_listener(listener: Callable)` | Add a listener called when sort order changes. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.GridVariant)` | Add theme variants to the grid. |
| `append_footer_row() -> pyxflow.components.grid.HeaderRow` | Append a footer row. |
| `append_header_row() -> pyxflow.components.grid.HeaderRow` | Append an extra header row below existing header rows. |
| `blur()` | Remove focus from this component. |
| `collapse(item)` | Collapse a tree item programmatically. |
| `confirm_update(update_id: int)` | Called by client to confirm a data update was applied. |
| `deselect(key: str | None)` | Called by client when user deselects an item. |
| `deselect_all()` | Programmatically deselect all items. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `expand(item)` | Expand a tree item programmatically. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_column_by_key(key: str) -> pyxflow.components.grid.Column | None` | Get a column by its key. |
| `get_drop_mode()` |  |
| `get_editor() -> pyxflow.components.grid.EditorImpl` | Get the grid editor (lazily created). |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_header_rows() -> list[pyxflow.components.grid.HeaderRow]` | Get header rows. |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_items() -> list[dict]` | Get the current items. |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_selected_items() -> list` | Get the currently selected items as a list of dicts. |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_all_rows_visible() -> bool` |  |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_rows_draggable() -> bool` |  |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `prepend_header_row() -> pyxflow.components.grid.HeaderRow` | Add an extra header row above the default column headers. |
| `recalculate_column_widths()` | Recalculate column widths. |
| `remove_all_columns()` | Remove all columns from the grid. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_column(column: pyxflow.components.grid.Column)` | Remove a column from the grid. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.GridVariant)` | Remove theme variants from the grid. |
| `scroll_to_index(index: int)` | Scroll to a specific row index. |
| `scroll_to_item(item)` | Scroll to a specific item. |
| `select(key: str | None)` | Select an item by key, or deselect if None. |
| `select_all()` | Programmatically select all items (multi-select only). |
| `select_item(item)` | Programmatically select an item by its object reference. |
| `set_all_rows_visible(all_rows_visible: bool)` | Set whether all rows should be visible (no virtual scrolling). |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_column_reordering_allowed(allowed: bool)` | Set whether the user can reorder columns by dragging. |
| `set_columns(*property_names: str) -> list['Column']` | Set columns from property names, auto-generating Title Case headers. |
| `set_data_provider(provider)` | Set a data provider. |
| `set_details_visible(key: str)` | Called by client to toggle details. No-op for now. |
| `set_details_visible_on_click(visible: bool)` | Set whether item details open when clicking a row. |
| `set_drop_mode(mode: 'GridDropMode | str | None')` | Set the drop mode for drag-and-drop. |
| `set_empty_state_component(component: pyxflow.core.component.Component)` | Set a component to show when the grid has no items. |
| `set_empty_state_text(text: str)` | Set the text to show when the grid has no items. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_items(items, children_provider: Callable | None = None)` | Set tree data with a hierarchy defined by children_provider. |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_multi_sort(enabled: bool)` | Enable or disable multi-column sorting. |
| `set_page_size(page_size: int)` | Set the page size for data fetching. |
| `set_requested_range(start: int, length: int)` | Called by client to request a data range. |
| `set_rows_draggable(draggable: bool)` | Set whether rows can be dragged. |
| `set_selection_mode(mode: pyxflow.components.constants.SelectionMode)` | Set the selection mode. Must be called before the grid is attached. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_sort_order(sort_orders: list[pyxflow.components.grid.GridSortOrder])` | Set the sort order programmatically. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_viewport_range(start: int, length: int)` | Called by client when visible range changes. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |
| `sorters_changed(sorters)` | Called by client when sort order changes. |
| `update_expanded_state(key: str, expanded: bool)` | Called by client when user clicks a tree toggle. |
