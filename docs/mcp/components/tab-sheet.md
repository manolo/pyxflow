# TabSheet

**Category:** Layout | Tab-based content switcher

## Constructor

```python
TabSheet()
```

## Methods

| Method | Description |
|--------|-------------|
| `add(label_or_tab, content: pyxflow.core.component.Component)...` | Add a tab with content. |
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_selected_change_listener(listener: Callable)` | Add a listener for tab selection changes. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_theme_variants(*variants: pyxflow.components.constants.TabSheetVariant)` | Add theme variants to the tab sheet. |
| `blur()` | Remove focus from this component. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_component(tab: pyxflow.components.tabs.Tab) -> pyxflow.core.compon...` | Get the content component associated with a tab. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_index_of(tab: pyxflow.components.tabs.Tab) -> int` | Get the index of the given tab, or -1 if not found. |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_selected_index() -> int` | Get the selected tab index. |
| `get_selected_tab() -> pyxflow.components.tabs.Tab | None` | Get the currently selected tab. |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_tab(content: pyxflow.core.component.Component) -> pyxflow.co...` | Get the tab associated with a content component. |
| `get_tab_at(index: int) -> pyxflow.components.tabs.Tab` | Get the tab at the given index. |
| `get_tab_count() -> int` | Get the number of tabs. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `remove(tab: pyxflow.components.tabs.Tab)` | Remove a tab and its content. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `remove_theme_variants(*variants: pyxflow.components.constants.TabSheetVariant)` | Remove theme variants from the tab sheet. |
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
| `set_selected_index(index: int)` | Set the selected tab by index. |
| `set_selected_tab(tab: pyxflow.components.tabs.Tab)` | Set the selected tab. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

## Theme Variants

```python
from pyxflow.components import TabSheetVariant
```

| Variant | Value |
|---------|-------|
| `TabSheetVariant.LUMO_TABS_CENTERED` | `"centered"` |
| `TabSheetVariant.LUMO_TABS_SMALL` | `"small"` |
| `TabSheetVariant.LUMO_TABS_MINIMAL` | `"minimal"` |
| `TabSheetVariant.LUMO_TABS_HIDE_SCROLL_BUTTONS` | `"hide-scroll-buttons"` |
| `TabSheetVariant.LUMO_TABS_EQUAL_WIDTH_TABS` | `"equal-width-tabs"` |
| `TabSheetVariant.LUMO_BORDERED` | `"bordered"` |
| `TabSheetVariant.LUMO_NO_PADDING` | `"no-padding"` |
| `TabSheetVariant.LUMO_TABS_SHOW_SCROLL_BUTTONS` | `"show-scroll-buttons"` |
| `TabSheetVariant.AURA_NO_BORDER` | `"no-border"` |
| `TabSheetVariant.AURA_TABS_FILLED` | `"filled"` |
