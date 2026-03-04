# MultiSelectComboBox

**Category:** Input | Multi-value searchable dropdown

## Constructor

```python
MultiSelectComboBox(label: str = "")
```

**Mixins:** HasReadOnly, HasValidation, HasRequired

Mixin methods: `set_read_only(bool)`, `is_read_only()`, `set_invalid(bool)`, `is_invalid()`, `set_error_message(str)`, `get_error_message()`, `set_required_indicator_visible(bool)`, `is_required_indicator_visible()`

## Methods

| Method | Description |
|--------|-------------|
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.MultiSelectCombo...` | Add theme variants to the multi-select combo box. |
| `add_value_change_listener(listener: Callable)` |  |
| `blur()` | Remove focus from this component. |
| `confirm_update(update_id: int)` |  |
| `deselect(*items: ~T)` | Remove items from the selection. |
| `deselect_all()` | Deselect all items. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_auto_expand()` |  |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_error_message() -> str` | Get the error message. |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_items() -> list[~T]` |  |
| `get_label() -> str` |  |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_value() -> Set[~T]` |  |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_clear_button_visible() -> bool` |  |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_invalid() -> bool` | Get whether the field is currently in an invalid state. |
| `is_keep_filter() -> bool` |  |
| `is_read_only() -> bool` | Get whether the field is read-only. |
| `is_required_indicator_visible() -> bool` | Get whether the required indicator is visible. |
| `is_selected_items_on_top() -> bool` |  |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.MultiSelectCombo...` | Remove theme variants from the multi-select combo box. |
| `reset_data_communicator()` |  |
| `select(*items: ~T)` | Add items to the selection. |
| `set_allow_custom_value(allow: bool)` | Set whether custom values are allowed. |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_auto_expand(mode: 'AutoExpandMode')` | Set how the field expands when chips don't fit. |
| `set_auto_open(auto_open: bool)` |  |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_clear_button_visible(visible: bool)` |  |
| `set_data_provider(provider: pyxflow.data.provider.DataProvider)` |  |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_error_message(message: str) -> None` | Set the error message shown when the field is invalid. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_invalid(invalid: bool) -> None` | Set whether the field is currently in an invalid state. |
| `set_item_label_generator(generator: Callable[[~T], str])` |  |
| `set_items(*items: ~T)` |  |
| `set_keep_filter(enabled: bool)` | Set whether filter text persists after selecting an item. |
| `set_label(label: str)` |  |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_page_size(page_size: int)` |  |
| `set_placeholder(placeholder: str)` |  |
| `set_read_only(read_only: bool) -> None` | Set whether the field is read-only. |
| `set_required(required: bool)` |  |
| `set_required_indicator_visible(required: bool) -> None` | Set whether the required indicator is visible. |
| `set_selected_items_on_top(enabled: bool)` | Set whether selected items appear at the top of the dropdown. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_value(value: Set[~T])` |  |
| `set_viewport_range(start: int, length: int, filter_text: str = '')` |  |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

## Theme Variants

```python
from pyxflow.components import MultiSelectComboBoxVariant
```

| Variant | Value |
|---------|-------|
| `MultiSelectComboBoxVariant.LUMO_SMALL` | `"small"` |
| `MultiSelectComboBoxVariant.LUMO_ALIGN_LEFT` | `"align-left"` |
| `MultiSelectComboBoxVariant.LUMO_ALIGN_CENTER` | `"align-center"` |
| `MultiSelectComboBoxVariant.LUMO_ALIGN_RIGHT` | `"align-right"` |
| `MultiSelectComboBoxVariant.LUMO_HELPER_ABOVE_FIELD` | `"helper-above-field"` |
| `MultiSelectComboBoxVariant.AURA_ALIGN_START` | `"align-start"` |
| `MultiSelectComboBoxVariant.AURA_ALIGN_END` | `"align-end"` |
