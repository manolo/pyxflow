# Upload

**Category:** Input | File upload component

## Constructor

```python
Upload()
```

## Methods

| Method | Description |
|--------|-------------|
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_failed_listener(listener: Callable)` | Add a listener for failed uploads. |
| `add_file_rejected_listener(listener: Callable)` | Add a listener for rejected files (client-side validation). |
| `add_file_removed_listener(listener: Callable)` | Add a listener for when a file is removed from the upload list. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_succeeded_listener(listener: Callable)` | Add a listener for successful uploads. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.UploadVariant)` | Add theme variants to the upload. |
| `blur()` | Remove focus from this component. |
| `clear_file_list()` | Clear the file list on the client side. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_accepted_file_types() -> list[str]` |  |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_drop_label() -> pyxflow.core.component.Component | None` |  |
| `get_drop_label_icon() -> pyxflow.core.component.Component | None` |  |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_i18n() -> dict | None` |  |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_max_file_size() -> int` |  |
| `get_max_files() -> int` |  |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_upload_button() -> pyxflow.core.component.Component | None` |  |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_auto_upload() -> bool` |  |
| `is_drop_allowed() -> bool` |  |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.UploadVariant)` | Remove theme variants from the upload. |
| `set_accepted_file_types(*types: str)` | Set accepted file types (MIME types or extensions like '.pdf'). |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_auto_upload(auto: bool)` | Set whether files are uploaded immediately. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_drop_allowed(allowed: bool)` | Set whether drag-and-drop is allowed. |
| `set_drop_label(label: pyxflow.core.component.Component | None)` | Set a custom drop label component. |
| `set_drop_label_icon(icon: pyxflow.core.component.Component | None)` | Set a custom drop label icon component. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_i18n(i18n: dict)` | Set the i18n localization object. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_max_file_size(max_size: int)` | Set maximum file size in bytes (0 = unlimited). |
| `set_max_files(max_files: int)` | Set maximum number of files (0 = unlimited). |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_receiver(callback: Callable)` | Set the receiver callback. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_upload_button(button: pyxflow.core.component.Component | None)` | Set a custom upload button component. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

## Theme Variants

```python
from pyxflow.components import UploadVariant
```

| Variant | Value |
|---------|-------|
| `UploadVariant.AURA_NO_BORDER` | `"no-border"` |
