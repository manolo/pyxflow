# MenuBar

**Category:** Navigation | Horizontal menu with dropdowns

## Constructor

```python
MenuBar()
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
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.MenuBarVariant)` | Add theme variants to the menu bar. |
| `blur()` | Remove focus from this component. |
| `close()` | Close any open submenus. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_items() -> list[pyxflow.components.menu_bar.MenuItem]` | Get the root-level items. |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_open_on_hover() -> bool` | Check if submenus open on hover. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `remove(*items: pyxflow.components.menu_bar.MenuItem)` | Remove root-level menu items. |
| `remove_all()` | Remove all root-level menu items. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.MenuBarVariant)` | Remove theme variants from the menu bar. |
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
| `set_open_on_hover(open_on_hover: bool)` | Set whether submenus open on hover. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

## Theme Variants

```python
from pyxflow.components import MenuBarVariant
```

| Variant | Value |
|---------|-------|
| `MenuBarVariant.LUMO_SMALL` | `"small"` |
| `MenuBarVariant.LUMO_LARGE` | `"large"` |
| `MenuBarVariant.LUMO_TERTIARY` | `"tertiary"` |
| `MenuBarVariant.LUMO_TERTIARY_INLINE` | `"tertiary-inline"` |
| `MenuBarVariant.LUMO_PRIMARY` | `"primary"` |
| `MenuBarVariant.LUMO_CONTRAST` | `"contrast"` |
| `MenuBarVariant.LUMO_ICON` | `"icon"` |
| `MenuBarVariant.LUMO_END_ALIGNED` | `"end-aligned"` |
| `MenuBarVariant.LUMO_DROPDOWN_INDICATORS` | `"dropdown-indicators"` |

## Related Classes

### MenuItem

```python
MenuItem(text: str = "", click_listener: Union = None)
```

| Method | Description |
|--------|-------------|
| `add_click_listener(listener: Callable)` | Add a click listener. |
| `get_aria_label() -> str | None` |  |
| `get_sub_menu() -> pyxflow.components.menu_bar.SubMenu` | Get the submenu for adding child items. |
| `get_text() -> str` | Get the item text. |
| `is_checkable() -> bool` | Check if the item is checkable. |
| `is_checked() -> bool` | Get the checked state. |
| `is_disable_on_click() -> bool` |  |
| `is_enabled() -> bool` | Check if enabled. |
| `is_keep_open() -> bool` |  |
| `is_parent_item() -> bool` | Check if this item has children (is a parent/submenu trigger). |
| `set_aria_label(label: str)` | Set ARIA label for accessibility. |
| `set_checkable(checkable: bool)` | Set whether the item is checkable. |
| `set_checked(checked: bool)` | Set the checked state. |
| `set_disable_on_click(disable: bool)` | Set whether the item disables itself after click. |
| `set_enabled(enabled: bool)` | Set the enabled state. |
| `set_keep_open(keep_open: bool)` | Set whether clicking this item keeps the menu open. |
| `set_text(text: str)` | Set the item text. |
