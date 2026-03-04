# ConfirmDialog

**Category:** Overlay | Pre-built confirmation dialog

## Constructor

```python
ConfirmDialog(header: str = "", text: str = "", confirm_text: str = "Confirm")
```

## Methods

| Method | Description |
|--------|-------------|
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_cancel_listener(listener: Callable)` | Add a listener called when the cancel button is clicked. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_confirm_listener(listener: Callable)` | Add a listener called when the confirm button is clicked. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_opened_change_listener(listener: Callable)` | Add a listener for opened state changes. |
| `add_reject_listener(listener: Callable)` | Add a listener called when the reject button is clicked. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.DialogVariant)` | Add theme variants to the confirm dialog. |
| `blur()` | Remove focus from this component. |
| `close()` | Close the confirm dialog. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_cancel_text() -> str` | Get the cancel button text. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_confirm_text() -> str` | Get the confirm button text. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_header() -> str` | Get the dialog header text. |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_reject_text() -> str` | Get the reject button text. |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_text() -> str` | Get the dialog message text. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_cancelable() -> bool` | Check if the cancel button is visible. |
| `is_close_on_esc() -> bool` |  |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_opened() -> bool` | Check if the dialog is open. |
| `is_rejectable() -> bool` | Check if the reject button is visible. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `open()` | Open the confirm dialog. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.DialogVariant)` | Remove theme variants from the confirm dialog. |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_cancel_button_theme(theme: str)` | Set the cancel button theme. |
| `set_cancel_text(text: str)` | Set the cancel button text. |
| `set_cancelable(cancelable: bool)` | Set whether the cancel button is visible. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_close_on_esc(close_on_esc: bool)` | Set whether the dialog closes on Escape key. |
| `set_confirm_button_theme(theme: str)` | Set the confirm button theme (e.g., 'error primary'). |
| `set_confirm_text(text: str)` | Set the confirm button text. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_header(header: str)` | Set the dialog header text. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_reject_button_theme(theme: str)` | Set the reject button theme. |
| `set_reject_text(text: str)` | Set the reject button text. |
| `set_rejectable(rejectable: bool)` | Set whether the reject button is visible. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_text(message: str)` | Set the dialog message text. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |
