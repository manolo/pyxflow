# Dialog

**Category:** Overlay | Modal dialog window

## Constructor

```python
Dialog()
```

## Methods

| Method | Description |
|--------|-------------|
| `add(*components: pyxflow.core.component.Component)` | Add components to the dialog content. |
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_close_listener(listener: Callable)` | Add a listener for when the dialog closes. |
| `add_dragged_listener(listener: Callable)` | Add a listener called when the dialog is dragged. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_open_listener(listener: Callable)` | Add a listener for when the dialog opens. |
| `add_resize_listener(listener: Callable)` | Add a listener called when the dialog is resized. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.DialogVariant)` | Add theme variants to the dialog. |
| `blur()` | Remove focus from this component. |
| `close()` | Close the dialog. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_footer() -> pyxflow.components.dialog._DialogSection` | Get the footer section for adding components to the dialog footer. |
| `get_header() -> pyxflow.components.dialog._DialogSection` | Get the header section for adding components to the dialog header. |
| `get_header_title() -> str` | Get the dialog header title. |
| `get_height() -> str | None` | Get the dialog height. |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_width() -> str | None` | Get the dialog width. |
| `handle_client_close()` | Called when the client reports the dialog was closed. |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_close_on_esc() -> bool` | Check if the dialog closes on Escape key. |
| `is_close_on_outside_click() -> bool` | Check if the dialog closes on outside click. |
| `is_draggable() -> bool` | Check if the dialog is draggable. |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_modal() -> bool` | Check if the dialog is modal. |
| `is_opened() -> bool` | Check if the dialog is open. |
| `is_resizable() -> bool` | Check if the dialog is resizable. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `open()` | Open the dialog. |
| `remove(*components: pyxflow.core.component.Component)` | Remove specific components from the dialog content. |
| `remove_all()` | Remove all components from the dialog content. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.DialogVariant)` | Remove theme variants from the dialog. |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_close_on_esc(close_on_esc: bool)` | Set whether the dialog closes on Escape key. |
| `set_close_on_outside_click(close_on_outside_click: bool)` | Set whether the dialog closes on outside click. |
| `set_draggable(draggable: bool)` | Set whether the dialog can be dragged. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_header_title(title: str)` | Set the dialog header title. |
| `set_height(height: str | None)` | Set the dialog height (e.g., '300px', '50%'). |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_left(left: str)` | Set the dialog left position (e.g., '100px'). |
| `set_max_height(max_height: str | None)` | Set the maximum height of the dialog overlay. |
| `set_max_width(max_width: str | None)` | Set the maximum width of the dialog overlay. |
| `set_min_height(min_height: str | None)` | Set the minimum height of the dialog overlay. |
| `set_min_width(min_width: str | None)` | Set the minimum width of the dialog overlay. |
| `set_modal(modal: bool)` | Set whether the dialog is modal. |
| `set_opened(opened: bool)` | Set the opened state. |
| `set_resizable(resizable: bool)` | Set whether the dialog can be resized. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_top(top: str)` | Set the dialog top position (e.g., '100px'). |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: str | None)` | Set the dialog width (e.g., '400px', '50%'). |
| `set_width_full()` | Set width to 100%. |

## Theme Variants

```python
from pyxflow.components import DialogVariant
```

| Variant | Value |
|---------|-------|
| `DialogVariant.LUMO_NO_PADDING` | `"no-padding"` |
