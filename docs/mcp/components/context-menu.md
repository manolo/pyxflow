# ContextMenu

**Category:** Navigation | Right-click context menu

## Constructor

```python
ContextMenu(target: Union = None)
```

## Methods

| Method | Description |
|--------|-------------|
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_item(text: str, click_listener: Callable | None = None) -> py...` | Add a root-level menu item. |
| `add_opened_change_listener(listener: Callable)` | Add a listener for opened state changes. |
| `add_separator()` | Add a separator between items. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `blur()` | Remove focus from this component. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_items() -> list[pyxflow.components.context_menu.ContextMenuItem]` |  |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_target() -> pyxflow.core.component.Component | None` | Get the target component. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_open_on_click() -> bool` | Check if the menu opens on left-click. |
| `is_opened() -> bool` | Check if the context menu is currently open. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `remove(*items: pyxflow.components.context_menu.ContextMenuItem)` | Remove root-level menu items. |
| `remove_all()` | Remove all root-level menu items. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_open_on_click(open_on_click: bool)` | Set whether to open on left-click instead of right-click. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_target(target: pyxflow.core.component.Component)` | Set the target component for the context menu. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

## Related Classes

### ContextMenuItem

```python
ContextMenuItem(text: str = "", click_listener: Union = None)
```

| Method | Description |
|--------|-------------|
| `get_sub_menu() -> 'ContextSubMenu'` |  |
| `get_text() -> str` |  |
| `is_checkable() -> bool` |  |
| `is_checked() -> bool` |  |
| `is_enabled() -> bool` |  |
| `set_checkable(checkable: bool)` |  |
| `set_checked(checked: bool)` |  |
| `set_enabled(enabled: bool)` |  |
| `set_text(text: str)` |  |
