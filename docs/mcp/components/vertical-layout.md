# VerticalLayout

**Category:** Layout | Vertical flex container with spacing

## Constructor

```python
VerticalLayout(children: Component)
```

## Methods

| Method | Description |
|--------|-------------|
| `add(*components: pyxflow.core.component.Component)` | Add components to the layout. |
| `add_and_expand(*components: pyxflow.core.component.Component)` | Add components and set them to expand (flex-grow: 1). |
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_component_as_first(component: pyxflow.core.component.Component)` | Add a component as the first child. |
| `add_component_at_index(index: int, component: pyxflow.core.component.Component)` |  |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.VerticalLayoutVa...` | Add theme variants to the vertical layout. |
| `blur()` | Remove focus from this component. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `expand(*components: pyxflow.core.component.Component)` | Set flex-grow to 1 on the given components so they fill available space. |
| `focus()` | Focus this component. |
| `get_align_items() -> pyxflow.components.constants.Alignment | None` |  |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_flex_grow(component: pyxflow.core.component.Component) -> float` | Get the flex-grow value of a component. |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_justify_content_mode() -> pyxflow.components.constants.JustifyContentMode | None` |  |
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
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `is_wrap() -> bool` |  |
| `remove(*components: pyxflow.core.component.Component)` | Remove components from the layout. |
| `remove_all()` | Remove all child components. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.VerticalLayoutVa...` | Remove theme variants from the vertical layout. |
| `replace(old_component: pyxflow.core.component.Component, new_com...` |  |
| `set_align_items(alignment: pyxflow.components.constants.Alignment)` | Set the default alignment perpendicular to the layout direction. |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_box_sizing(box_sizing: str)` |  |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_default_horizontal_component_alignment(alignment: pyxflow.components.constants.Alignment)` | Set default horizontal alignment for all children. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_flex_grow(flex_grow: float, *components: pyxflow.core.component.Co...` |  |
| `set_flex_shrink(flex_shrink: float, *components: pyxflow.core.component....` |  |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_horizontal_component_alignment(alignment: pyxflow.components.constants.Alignment, *comp...` | Set horizontal alignment for specific components. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_justify_content_mode(mode: pyxflow.components.constants.JustifyContentMode)` | Set justify-content-mode on the layout. |
| `set_margin(margin: bool)` | Enable or disable margin. |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_padding(padding: bool)` | Enable or disable padding. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_spacing(spacing: bool)` | Enable or disable spacing. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |
| `set_wrap(wrap: bool)` | Enable or disable wrapping. |

## Theme Variants

```python
from pyxflow.components import VerticalLayoutVariant
```

| Variant | Value |
|---------|-------|
| `VerticalLayoutVariant.LUMO_MARGIN` | `"margin"` |
| `VerticalLayoutVariant.LUMO_PADDING` | `"padding"` |
| `VerticalLayoutVariant.LUMO_SPACING_XS` | `"spacing-xs"` |
| `VerticalLayoutVariant.LUMO_SPACING_S` | `"spacing-s"` |
| `VerticalLayoutVariant.LUMO_SPACING` | `"spacing"` |
| `VerticalLayoutVariant.LUMO_SPACING_L` | `"spacing-l"` |
| `VerticalLayoutVariant.LUMO_SPACING_XL` | `"spacing-xl"` |
| `VerticalLayoutVariant.LUMO_WRAP` | `"wrap"` |
