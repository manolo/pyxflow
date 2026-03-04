# FlexLayout

**Category:** Layout | Flexible CSS layout

## Constructor

```python
FlexLayout(children: Component)
```

## Methods

| Method | Description |
|--------|-------------|
| `add(*components: pyxflow.core.component.Component)` | Add components to the layout. |
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_component_at_index(index: int, component: pyxflow.core.component.Component)` | Add a component at a specific index. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `blur()` | Remove focus from this component. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `expand(*components: pyxflow.core.component.Component)` | Set flex-grow to 1 on the given components. |
| `focus()` | Focus this component. |
| `get_align_content() -> pyxflow.components.constants.ContentAlignment` | Get the align-content value. Default is STRETCH. |
| `get_align_items() -> pyxflow.components.constants.Alignment` | Get the align-items value. Default is STRETCH. |
| `get_align_self(component: pyxflow.core.component.Component) -> pyxflow....` | Get align-self for a component. Default is AUTO. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_flex_basis(component: pyxflow.core.component.Component) -> str | None` | Get flex-basis for a component. |
| `get_flex_direction() -> pyxflow.components.constants.FlexDirection` | Get the flex-direction. Default is ROW. |
| `get_flex_grow(component: pyxflow.core.component.Component) -> float` | Get flex-grow for a component. Default is 0. |
| `get_flex_shrink(component: pyxflow.core.component.Component) -> float` | Get flex-shrink for a component. Default is 1. |
| `get_flex_wrap() -> pyxflow.components.constants.FlexWrap` | Get the flex-wrap. Default is NOWRAP. |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_justify_content_mode() -> pyxflow.components.constants.JustifyContentMode` | Get the justify-content mode. Default is START. |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_order(component: pyxflow.core.component.Component) -> int` | Get the order for a component. Default is 0. |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `remove(*components: pyxflow.core.component.Component)` | Remove components from the layout. |
| `remove_all()` | Remove all child components. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `replace(old_component: pyxflow.core.component.Component, new_com...` | Replace an existing component with a new one. |
| `set_align_content(alignment: pyxflow.components.constants.ContentAlignment...` | Set the align-content CSS property (multi-line cross-axis alignment). |
| `set_align_items(alignment: pyxflow.components.constants.Alignment | None)` | Set the align-items CSS property (cross-axis alignment for all children). |
| `set_align_self(alignment: pyxflow.components.constants.Alignment | None...` | Set align-self on individual components. |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_flex_basis(width: str | None, *components: pyxflow.core.component.C...` | Set flex-basis on components. |
| `set_flex_direction(direction: pyxflow.components.constants.FlexDirection | ...` | Set the flex-direction CSS property. |
| `set_flex_grow(flex_grow: float, *components: pyxflow.core.component.Co...` | Set flex-grow on components. |
| `set_flex_shrink(flex_shrink: float, *components: pyxflow.core.component....` | Set flex-shrink on components. |
| `set_flex_wrap(wrap: pyxflow.components.constants.FlexWrap)` | Set the flex-wrap CSS property. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_justify_content_mode(mode: pyxflow.components.constants.JustifyContentMode)` | Set the justify-content CSS property. |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_order(order: int, component: pyxflow.core.component.Component)` | Set the order CSS property on a component. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |
