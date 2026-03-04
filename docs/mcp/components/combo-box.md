# ComboBox

**Category:** Input | Searchable dropdown with type-ahead

## Constructor

```python
ComboBox(label: str = "")
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
| `add_custom_value_set_listener(listener: Callable)` |  |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.ComboBoxVariant)` | Add theme variants to the combo box. |
| `add_value_change_listener(listener: Callable)` |  |
| `blur()` | Remove focus from this component. |
| `confirm_update(update_id: int)` | Called by client to confirm a data update was applied. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
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
| `get_value() -> ~T | None` |  |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_clear_button_visible() -> bool` |  |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_invalid() -> bool` | Get whether the field is currently in an invalid state. |
| `is_read_only() -> bool` | Get whether the field is read-only. |
| `is_required_indicator_visible() -> bool` | Get whether the required indicator is visible. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.ComboBoxVariant)` | Remove theme variants from the combo box. |
| `reset_data_communicator()` | Called by client to reset the data communicator. |
| `set_allow_custom_value(allow: bool)` |  |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_auto_open(auto_open: bool)` |  |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_class_name_generator(generator: Callable[[~T], str | None])` | Set a function that generates CSS class names for dropdown items. |
| `set_clear_button_visible(visible: bool)` |  |
| `set_data_provider(provider: pyxflow.data.provider.DataProvider)` | Set a DataProvider for the combo box. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_error_message(message: str) -> None` | Set the error message shown when the field is invalid. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_invalid(invalid: bool) -> None` | Set whether the field is currently in an invalid state. |
| `set_item_label_generator(generator: Callable[[~T], str])` |  |
| `set_items(*items: ~T)` | Set the items for the combo box. |
| `set_label(label: str)` |  |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_overlay_width(width: str)` | Set the overlay width (e.g. '300px'). |
| `set_page_size(page_size: int)` |  |
| `set_placeholder(placeholder: str)` |  |
| `set_prefix_component(component: pyxflow.core.component.Component)` | Set a prefix component (e.g. Icon) in the 'prefix' slot. |
| `set_read_only(read_only: bool) -> None` | Set whether the field is read-only. |
| `set_required(required: bool)` |  |
| `set_required_indicator_visible(required: bool) -> None` | Set whether the required indicator is visible. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_value(value: ~T | None)` |  |
| `set_viewport_range(start: int, length: int, filter_text: str = '')` | Called by client when the dropdown viewport changes or user types a filter. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

## Theme Variants

```python
from pyxflow.components import ComboBoxVariant
```

| Variant | Value |
|---------|-------|
| `ComboBoxVariant.LUMO_SMALL` | `"small"` |
| `ComboBoxVariant.LUMO_ALIGN_LEFT` | `"align-left"` |
| `ComboBoxVariant.LUMO_ALIGN_CENTER` | `"align-center"` |
| `ComboBoxVariant.LUMO_ALIGN_RIGHT` | `"align-right"` |
| `ComboBoxVariant.LUMO_HELPER_ABOVE_FIELD` | `"helper-above-field"` |
| `ComboBoxVariant.AURA_ALIGN_START` | `"align-start"` |
| `ComboBoxVariant.AURA_ALIGN_END` | `"align-end"` |
