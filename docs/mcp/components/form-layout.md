# FormLayout

**Category:** Layout | Responsive form layout with label positioning

## Constructor

```python
FormLayout(components: Component)
```

## Methods

| Method | Description |
|--------|-------------|
| `add(*components: pyxflow.core.component.Component)` | Add components to the layout. |
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_form_item(field: pyxflow.core.component.Component, label: str | py...` | Add a field with a label, wrapped in a FormItem. |
| `add_form_row(*components: pyxflow.core.component.Component) -> 'FormRow'` | Add components grouped in a FormRow. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_with_colspan(component: pyxflow.core.component.Component, colspan: int)` | Add a component with a specific column span. |
| `blur()` | Remove focus from this component. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_colspan(component: pyxflow.core.component.Component) -> int` | Get the column span for a component. |
| `get_column_spacing() -> str | None` | Get the column spacing. |
| `get_column_width() -> str | None` |  |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_height() -> 'str | None'` |  |
| `get_helper_text() -> 'str'` | Get the helper text. |
| `get_id() -> 'str | None'` | Get the component's id attribute. |
| `get_label_spacing() -> str | None` | Get the label spacing. |
| `get_label_width() -> str | None` | Get the label width. |
| `get_max_columns() -> int | None` |  |
| `get_max_height() -> 'str | None'` |  |
| `get_max_width() -> 'str | None'` |  |
| `get_min_columns() -> int | None` |  |
| `get_min_height() -> 'str | None'` |  |
| `get_min_width() -> 'str | None'` |  |
| `get_responsive_steps() -> list[pyxflow.components.form_layout.ResponsiveStep]` | Get the current responsive steps. |
| `get_row_spacing() -> str | None` | Get the row spacing. |
| `get_style() -> '_BufferedStyle'` | Get the inline style manager. |
| `get_theme_name() -> 'str | None'` | Get theme names as space-separated string. |
| `get_tooltip_text() -> 'str | None'` | Get the tooltip text. |
| `get_ui() -> "'UI | None'"` | Get the UI this component belongs to. |
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_auto_responsive() -> bool` |  |
| `is_auto_rows() -> bool` |  |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_expand_columns() -> bool` |  |
| `is_expand_fields() -> bool` |  |
| `is_labels_aside() -> bool` |  |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `remove(*components: pyxflow.core.component.Component)` | Remove components from the layout. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_auto_responsive(auto_responsive: bool)` | Enable or disable auto-responsive mode. |
| `set_auto_rows(auto_rows: bool)` | Enable or disable auto-rows mode. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_colspan(component: pyxflow.core.component.Component, colspan: int)` | Set the column span for a component. |
| `set_column_spacing(spacing: str)` | Set the spacing between columns. |
| `set_column_width(width: str)` | Set the column width for auto-responsive mode. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_expand_columns(expand: bool)` | Set whether columns should expand to fill available space. |
| `set_expand_fields(expand: bool)` | Set whether fields should expand within their column. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_label_spacing(spacing: str)` | Set the spacing between label and field. |
| `set_label_width(width: str)` | Set the label width (e.g., '200px', '8em'). |
| `set_labels_aside(aside: bool)` | Set whether labels are positioned beside fields. |
| `set_max_columns(max_columns: int)` | Set the maximum number of columns. |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_columns(min_columns: int)` | Set the minimum number of columns. |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_responsive_steps(*steps: pyxflow.components.form_layout.ResponsiveStep)` | Set the responsive steps for column layout. |
| `set_row_spacing(spacing: str)` | Set the spacing between rows. |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

## Related Classes

### FormItem

```python
FormItem(components: Component)
```

| Method | Description |
|--------|-------------|
| `add(*components: pyxflow.core.component.Component)` | Add components to the form item. |
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_focus_listener(listener)` | Add a focus event listener. |
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
| `remove(*components: pyxflow.core.component.Component)` | Remove components from the form item. |
| `remove_all()` | Remove all components from the form item. |
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
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

### FormRow

```python
FormRow(components: Component)
```

| Method | Description |
|--------|-------------|
| `add(*components: pyxflow.core.component.Component)` | Add components to the row. |
| `add_blur_listener(listener)` | Add a blur event listener. |
| `add_class_name(*class_names: 'str')` | Add one or more CSS class names to the component. |
| `add_click_listener(listener)` | Add a click listener. Works on any component. |
| `add_click_shortcut(key: 'Key')` | Register a keyboard shortcut that triggers click on this component. |
| `add_focus_listener(listener)` | Add a focus event listener. |
| `add_form_item(field: pyxflow.core.component.Component, label: str | py...` | Add a field with a label, wrapped in a FormItem. |
| `add_theme_name(*theme_names: 'str')` | Add one or more theme names. |
| `add_with_colspan(component: pyxflow.core.component.Component, colspan: int)` | Add a component with a specific column span. |
| `blur()` | Remove focus from this component. |
| `execute_js(script: 'str', *args)` | Execute JavaScript on this component's element. |
| `focus()` | Focus this component. |
| `get_aria_label() -> 'str | None'` | Get the aria-label attribute. |
| `get_aria_labelled_by() -> 'str | None'` | Get the aria-labelledby attribute. |
| `get_class_names() -> 'set[str]'` | Get all CSS class names of the component. |
| `get_colspan(component: pyxflow.core.component.Component) -> int` | Get the column span for a component. |
| `get_element() -> 'Element'` | Get the element (public API). |
| `get_height() -> 'str | None'` |  |
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
| `get_width() -> 'str | None'` |  |
| `has_class_name(class_name: 'str') -> 'bool'` | Check if the component has a specific CSS class name. |
| `has_theme_name(theme_name: 'str') -> 'bool'` | Check if the component has a specific theme name. |
| `is_enabled() -> 'bool'` | Check if the component is enabled. |
| `is_visible() -> 'bool'` | Check if the component is visible. |
| `remove_class_name(*class_names: 'str')` | Remove one or more CSS class names from the component. |
| `remove_theme_name(*theme_names: 'str')` | Remove one or more theme names. |
| `set_aria_label(label: 'str | None')` | Set the aria-label attribute. |
| `set_aria_labelled_by(labelled_by: 'str | None')` | Set the aria-labelledby attribute. |
| `set_class_name(class_name: 'str', add: 'bool' = True)` | Add or remove a CSS class name. |
| `set_colspan(component: pyxflow.core.component.Component, colspan: int)` | Set the column span for a component. |
| `set_enabled(enabled: 'bool')` | Set the enabled state of the component. |
| `set_height(height: 'str | None')` | Set height (e.g., '100px', '50%', '10em'). None removes height. |
| `set_height_full()` | Set height to 100%. |
| `set_helper_text(text: 'str')` | Set the helper text shown below the field. |
| `set_id(id: 'str')` | Set the component's id attribute. |
| `set_max_height(max_height: 'str | None')` |  |
| `set_max_width(max_width: 'str | None')` |  |
| `set_min_height(min_height: 'str | None')` |  |
| `set_min_width(min_width: 'str | None')` |  |
| `set_size_full()` | Set both width and height to 100%. |
| `set_size_undefined()` | Remove both width and height. |
| `set_theme_name(theme_name: 'str | None')` | Set theme names, overwriting any previous ones. None removes all. |
| `set_tooltip_text(text: 'str')` | Set the tooltip text. Creates a <vaadin-tooltip> child element. |
| `set_visible(visible: 'bool')` | Set the visibility of the component. |
| `set_width(width: 'str | None')` | Set width (e.g., '100px', '50%', '10em'). None removes width. |
| `set_width_full()` | Set width to 100%. |

### ResponsiveStep

```python
ResponsiveStep(min_width: Union, columns: int, labels_position: ResponsiveStep.LabelsPosition | None = None)
```

| Method | Description |
|--------|-------------|
| `to_json() -> dict` | Serialize to a dict for the responsiveSteps property. |
