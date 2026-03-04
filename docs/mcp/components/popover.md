# Popover

**Category:** Layout | Popup content anchored to a target

## Constructor

```python
Popover()
```

## Methods

| Method | Description |
|--------|-------------|
| `add(*components: pyxflow.core.component.Component)` | Add components to the popover content. |
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_close_listener(listener: Callable)` | Add a listener for when the popover closes. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_open_listener(listener: Callable)` | Add a listener for when the popover opens. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.PopoverVariant)` | Add theme variants to the popover. |
| `blur()` | Remove focus from this component. |
| `close()` | Close the popover. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_position() -> pyxflow.components.constants.PopoverPosition` |  |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_target() -> pyxflow.core.component.Component | None` |  |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_close_on_esc() -> bool` |  |
| `is_close_on_outside_click() -> bool` |  |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_modal() -> bool` |  |
| `is_open_on_click() -> bool` |  |
| `is_open_on_focus() -> bool` |  |
| `is_open_on_hover() -> bool` |  |
| `is_opened() -> bool` |  |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `open()` | Open the popover. |
| `remove(*components: pyxflow.core.component.Component)` | Remove specific components from the popover. |
| `remove_all()` | Remove all components from the popover. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.PopoverVariant)` | Remove theme variants from the popover. |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_autofocus(autofocus: bool)` | Set whether to auto-focus the first focusable element. |
| `set_backdrop_visible(visible: bool)` | Set whether the backdrop is visible when modal. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_close_on_esc(enabled: bool)` | Set whether the popover closes on Escape key. |
| `set_close_on_outside_click(enabled: bool)` | Set whether the popover closes on outside click. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_focus_delay(delay: int)` | Set focus delay in milliseconds. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_hide_delay(delay: int)` | Set hide delay in milliseconds. |
| `set_hover_delay(delay: int)` | Set hover delay in milliseconds. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_modal(modal: bool)` | Set whether the popover is modal. |
| `set_open_on_click(enabled: bool)` | Set whether the popover opens on click. |
| `set_open_on_focus(enabled: bool)` | Set whether the popover opens on focus. |
| `set_open_on_hover(enabled: bool)` | Set whether the popover opens on hover. |
| `set_opened(opened: bool)` |  |
| `set_position(position: pyxflow.components.constants.PopoverPosition)` | Set the popover position relative to the target. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_target(component: pyxflow.core.component.Component)` | Set the target component the popover is anchored to. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

## Theme Variants

```python
from pyxflow.components import PopoverVariant
```

| Variant | Value |
|---------|-------|
| `PopoverVariant.LUMO_NO_PADDING` | `"no-padding"` |
| `PopoverVariant.LUMO_ARROW` | `"arrow"` |
