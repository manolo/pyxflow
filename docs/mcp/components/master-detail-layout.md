# MasterDetailLayout

**Category:** Layout | Responsive master-detail with drawer

## Constructor

```python
MasterDetailLayout()
```

## Methods

| Method | Description |
|--------|-------------|
| `add_backdrop_click_listener(listener: Callable)` | Add a listener for backdrop click events (when overlay detail is dismissed). |
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_detail_escape_press_listener(listener: Callable)` | Add a listener for Escape key press in the detail area. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.MasterDetailLayo...` | Add theme variants to the master detail layout. |
| `blur()` | Remove focus from this component. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_detail() -> pyxflow.core.component.Component | None` |  |
| `get_detail_size() -> str | None` | Get the detail area size. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_master() -> pyxflow.core.component.Component | None` |  |
| `get_master_min_size() -> str | None` | Get the minimum master area size. |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_orientation() -> str` | Get orientation (default: 'horizontal'). |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_animation_enabled() -> bool` | Check if layout animation is enabled (default: True). |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.MasterDetailLayo...` | Remove theme variants from the master detail layout. |
| `set_animation_enabled(enabled: bool)` | Set whether layout animation is enabled. |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_containment(containment: str)` | Set containment mode ('layout' or 'viewport'). |
| `set_detail(component: pyxflow.core.component.Component | None)` | Set the detail component. Pass None to hide the detail area. |
| `set_detail_min_size(size: str)` | Set the minimum detail area size (e.g., '200px'). |
| `set_detail_size(size: str)` | Set the detail area size (e.g., '400px', '250px'). |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_force_overlay(force: bool)` | Set whether overlay mode is enforced. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_master(component: pyxflow.core.component.Component)` | Set the master (list/overview) component. |
| `set_master_min_size(size: str)` | Set the minimum master area size (e.g., '450px'). |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_orientation(orientation: str)` | Set orientation ('horizontal' or 'vertical'). |
| `set_overlay_mode(mode: str)` | Set the overlay mode ('drawer' or 'stack'). |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

## Theme Variants

```python
from pyxflow.components import MasterDetailLayoutVariant
```

| Variant | Value |
|---------|-------|
| `MasterDetailLayoutVariant.AURA_INSET_DRAWER` | `"inset-drawer"` |
