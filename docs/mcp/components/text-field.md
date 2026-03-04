# TextField

**Category:** Input | Single-line text input

## Constructor

```python
TextField(label: str = "")
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
| `add_theme_variants(*variants: pyxflow.components.constants.TextFieldVariant)` | Add theme variants to the text field. |
| `add_value_change_listener(listener: Callable)` | Add a value change listener. |
| `blur()` | Remove focus from this component. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_autocomplete() -> str | None` | Get the autocomplete hint. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_error_message() -> str` | Get the error message. |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_label() -> str` | Get the label. |
| `get_max_height() -> 'str | None'` |  |
| `get_max_length() -> int` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_length() -> int` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_placeholder() -> str` | Get the placeholder text. |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_value() -> str` | Get the current value. |
| `get_value_change_mode() -> pyxflow.components.constants.ValueChangeMode` |  |
| `get_value_change_timeout() -> int` |  |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_autoselect() -> bool` |  |
| `is_clear_button_visible() -> bool` |  |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_invalid() -> bool` | Get whether the field is currently in an invalid state. |
| `is_read_only() -> bool` | Get whether the field is read-only. |
| `is_required_indicator_visible() -> bool` | Get whether the required indicator is visible. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.TextFieldVariant)` | Remove theme variants from the text field. |
| `set_allowed_char_pattern(pattern: str)` | Set the pattern for allowed characters (blocks input of non-matching chars). |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_autocomplete(autocomplete: 'Autocomplete | str')` | Set the autocomplete hint for the browser. |
| `set_autoselect(autoselect: bool)` | Set whether the text is automatically selected when the field gets focus. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_clear_button_visible(visible: bool)` | Show or hide the clear button. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_error_message(message: str) -> None` | Set the error message shown when the field is invalid. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_invalid(invalid: bool) -> None` | Set whether the field is currently in an invalid state. |
| `set_label(label: str)` | Set the label. |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_length(max_length: int)` | Set the maximum number of characters. |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_length(min_length: int)` | Set the minimum number of characters. |
| `set_min_width(min_width: 'str | None')` |  |
| `set_pattern(pattern: str)` | Set the regular expression pattern for validation. |
| `set_placeholder(text: str)` | Set the placeholder text. |
| `set_prefix_component(component: pyxflow.core.component.Component)` | Set a prefix component (e.g. Icon) in the 'prefix' slot. |
| `set_read_only(read_only: bool) -> None` | Set whether the field is read-only. |
| `set_required_indicator_visible(required: bool) -> None` | Set whether the required indicator is visible. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_suffix_component(component: pyxflow.core.component.Component)` | Set a suffix component (e.g. Icon) in the 'suffix' slot. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_value(value: str)` | Set the value. |
| `set_value_change_mode(mode: pyxflow.components.constants.ValueChangeMode)` | Set how eagerly value changes are synced to the server. |
| `set_value_change_timeout(timeout: int)` | Set the timeout in ms for LAZY/TIMEOUT modes (no effect for now). |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

## Theme Variants

```python
from pyxflow.components import TextFieldVariant
```

| Variant | Value |
|---------|-------|
| `TextFieldVariant.LUMO_SMALL` | `"small"` |
| `TextFieldVariant.LUMO_ALIGN_CENTER` | `"align-center"` |
| `TextFieldVariant.LUMO_ALIGN_RIGHT` | `"align-right"` |
| `TextFieldVariant.LUMO_HELPER_ABOVE_FIELD` | `"helper-above-field"` |
| `TextFieldVariant.AURA_ALIGN_LEFT` | `"align-left"` |
| `TextFieldVariant.AURA_ALIGN_START` | `"align-start"` |
| `TextFieldVariant.AURA_ALIGN_END` | `"align-end"` |
