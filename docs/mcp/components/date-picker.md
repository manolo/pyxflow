# DatePicker

**Category:** Input | Date selection with calendar popup

## Constructor

```python
DatePicker(label: str = "")
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
| `add_opened_change_listener(listener: Callable)` | Add a listener for when the overlay opens or closes. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.DatePickerVariant)` | Add theme variants to the date picker. |
| `add_value_change_listener(listener: Callable)` |  |
| `blur()` | Remove focus from this component. |
| `close()` | Close the date picker overlay. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_error_message() -> str` | Get the error message. |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_i18n() -> dict | None` |  |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_initial_position()` |  |
| `get_label() -> str` |  |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_value() -> datetime.date | None` |  |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_clear_button_visible() -> bool` |  |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_invalid() -> bool` | Get whether the field is currently in an invalid state. |
| `is_read_only() -> bool` | Get whether the field is read-only. |
| `is_required_indicator_visible() -> bool` | Get whether the required indicator is visible. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `is_week_numbers_visible() -> bool` |  |
| `open()` | Open the date picker overlay. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.DatePickerVariant)` | Remove theme variants from the date picker. |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_auto_open(auto_open: bool)` | Set whether the dropdown opens automatically on focus. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_clear_button_visible(visible: bool)` |  |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_error_message(message: str) -> None` | Set the error message shown when the field is invalid. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_i18n(i18n: dict)` | Set the i18n localization object (month names, weekdays, etc.). |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_initial_position(date: 'datetime.date | None')` | Set the initial calendar position when no value is selected. |
| `set_invalid(invalid: bool) -> None` | Set whether the field is currently in an invalid state. |
| `set_label(label: str)` |  |
| `set_max(max_date: datetime.date | None)` |  |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min(min_date: datetime.date | None)` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_placeholder(placeholder: str)` |  |
| `set_read_only(read_only: bool) -> None` | Set whether the field is read-only. |
| `set_required(required: bool)` |  |
| `set_required_indicator_visible(required: bool) -> None` | Set whether the required indicator is visible. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_value(value: datetime.date | None)` |  |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_week_numbers_visible(visible: bool)` | Set whether ISO week numbers are shown. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

## Theme Variants

```python
from pyxflow.components import DatePickerVariant
```

| Variant | Value |
|---------|-------|
| `DatePickerVariant.LUMO_SMALL` | `"small"` |
| `DatePickerVariant.LUMO_ALIGN_LEFT` | `"align-left"` |
| `DatePickerVariant.LUMO_ALIGN_CENTER` | `"align-center"` |
| `DatePickerVariant.LUMO_ALIGN_RIGHT` | `"align-right"` |
| `DatePickerVariant.LUMO_HELPER_ABOVE_FIELD` | `"helper-above-field"` |
| `DatePickerVariant.AURA_ALIGN_START` | `"align-start"` |
| `DatePickerVariant.AURA_ALIGN_END` | `"align-end"` |
