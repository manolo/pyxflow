# Card

**Category:** Layout | Content card with optional media/actions

## Constructor

```python
Card(children: Component)
```

## Methods

| Method | Description |
|--------|-------------|
| `add(*components: pyxflow.core.component.Component)` | Add components to the default (content) slot. |
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.CardVariant)` | Add theme variants to the card. |
| `add_to_footer(*components: pyxflow.core.component.Component)` | Add components to the footer slot. |
| `blur()` | Remove focus from this component. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_header() -> pyxflow.core.component.Component | None` | Get the header component. |
| `get_header_prefix() -> pyxflow.core.component.Component | None` | Get the header prefix component. |
| `get_header_suffix() -> pyxflow.core.component.Component | None` | Get the header suffix component. |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_media() -> pyxflow.core.component.Component | None` | Get the media component. |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_subtitle() -> 'Component | str | None'` |  |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_title() -> 'Component | str | None'` |  |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `remove(*components: pyxflow.core.component.Component)` | Remove specific components from the default content slot. |
| `remove_all()` | Remove all components from the default content slot. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.CardVariant)` | Remove theme variants from the card. |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_header(component: pyxflow.core.component.Component)` | Set the header component (slot='header'). |
| `set_header_prefix(component: pyxflow.core.component.Component)` | Set the header prefix component (slot='header-prefix'). |
| `set_header_suffix(component: pyxflow.core.component.Component)` | Set the header suffix component (slot='header-suffix'). |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_media(component: pyxflow.core.component.Component)` | Set the media component (slot='media'). |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_subtitle(subtitle: 'Component | str')` | Set the subtitle (slot='subtitle'). Can be a string or a Component. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_title(title: 'Component | str')` | Set the title (slot='title'). Can be a string or a Component. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

## Theme Variants

```python
from pyxflow.components import CardVariant
```

| Variant | Value |
|---------|-------|
| `CardVariant.LUMO_ELEVATED` | `"elevated"` |
| `CardVariant.LUMO_OUTLINED` | `"outlined"` |
| `CardVariant.LUMO_HORIZONTAL` | `"horizontal"` |
| `CardVariant.LUMO_STRETCH_MEDIA` | `"stretch-media"` |
| `CardVariant.LUMO_COVER_MEDIA` | `"cover-media"` |
