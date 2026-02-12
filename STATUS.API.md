# PyFlow API Inventory — Python vs Java Vaadin 25

**Generated: 2026-02-12**
**Python components: 49 | Tests: 1910 | LOC: ~13,800 (core)**

Legend: `[x]` = implemented, `[ ]` = missing

---

## Base Component (inherited by ALL components)

All components inherit from `Component` which provides:

| Method | Status |
|--------|--------|
| `set_visible` / `is_visible` | [x] |
| `set_enabled` / `is_enabled` | [x] |
| `add_class_name` / `remove_class_name` / `has_class_name` / `get_class_names` / `set_class_name` | [x] |
| `set_width` / `get_width` / `set_height` / `get_height` | [x] |
| `set_min_width` / `get_min_width` / `set_max_width` / `get_max_width` | [x] |
| `set_min_height` / `get_min_height` / `set_max_height` / `get_max_height` | [x] |
| `set_size_full` / `set_width_full` / `set_height_full` / `set_size_undefined` | [x] |
| `add_theme_name` / `remove_theme_name` / `has_theme_name` / `get_theme_name` / `set_theme_name` | [x] |
| `set_id` / `get_id` | [x] |
| `set_helper_text` / `get_helper_text` | [x] |
| `set_tooltip_text` / `get_tooltip_text` | [x] |
| `focus` / `blur` | [x] |
| `add_click_listener` / `add_click_shortcut` | [x] |
| `execute_js` (deferred buffering) | [x] |
| `get_element` / `get_ui` / `get_style` | [x] |

**Missing from base vs Java:**
| Method | Status |
|--------|--------|
| `set_aria_label` / `get_aria_label` (HasAriaLabel) | [ ] |
| `set_aria_labelled_by` / `get_aria_labelled_by` | [ ] |
| `add_focus_listener` / `add_blur_listener` (FocusNotifier/BlurNotifier) | [ ] |
| `set_read_only` / `is_read_only` (HasReadOnly) | [x] 18 components |
| `remove_all` (HasComponents) | [x] 10 containers |

## Field Mixins (applied to 15-16 components)

| Mixin | Methods | Applied to |
|-------|---------|-----------|
| **HasReadOnly** | `set_read_only` / `is_read_only` | [x] 16 field + Checkbox + ListBox + MultiSelectListBox (18 total) |
| **HasValidation** | `set_invalid` / `is_invalid` / `set_error_message` / `get_error_message` | [x] All field components except Checkbox (15) |
| **HasRequired** | `set_required_indicator_visible` / `is_required_indicator_visible` | [x] All field components including Checkbox (16) |
| **set_value fires listeners** | `set_value()` fires `{"value": ..., "from_client": False}` on server-side changes | [x] All 18 field components (matches Java `AbstractFieldSupport.setValue()`) |

**Missing field mixins:**
| Feature | Status |
|---------|--------|
| `set_read_only` / `is_read_only` | [x] (HasReadOnly mixin) |
| `set_value_change_mode` / `set_value_change_timeout` | [ ] |
| `set_i18n` / `get_i18n` (per-component validation messages) | [ ] |
| Constructor overloads with initial value + listener | [ ] |

---

## Layout Components

### AppLayout
| Feature | Status |
|---------|--------|
| `add_to_navbar` / `add_to_drawer` / `set_content` / `get_content` | [x] |
| `set_drawer_opened` / `is_drawer_opened` / `set_primary_section` / `get_primary_section` | [x] |
| `show_router_layout_content` / `remove_router_layout_content` | [x] |
| `add_to_navbar(touch_optimized, ...)` | [ ] |
| `is_overlay` | [ ] |
| `remove` / `set_i18n` / `get_i18n` | [ ] |

### VerticalLayout
| Feature | Status |
|---------|--------|
| `add` / `remove` / `expand` | [x] |
| `set_spacing` / `set_padding` / `set_margin` | [x] |
| `set_default_horizontal_component_alignment` | [x] |
| `set_horizontal_component_alignment` | [x] |
| `remove_all` | [x] |
| `set_justify_content_mode` / `get_justify_content_mode` | [ ] |
| `set_align_items` / `get_align_items` | [ ] |
| `set_flex_grow` / `get_flex_grow` / `set_flex_shrink` | [ ] |
| `add_and_expand` / `replace` / `add_component_at_index` | [ ] |
| `set_wrap` / `is_wrap` / `set_box_sizing` | [ ] |

### HorizontalLayout
| Feature | Status |
|---------|--------|
| `add` / `remove` / `expand` | [x] |
| `set_spacing` / `set_margin` | [x] |
| `set_default_vertical_component_alignment` | [x] |
| `set_vertical_component_alignment` | [x] |
| `set_padding` | [ ] |
| `remove_all` | [x] |
| `set_justify_content_mode` / `set_align_items` | [ ] |
| `set_flex_grow` / `set_flex_shrink` | [ ] |
| `add_to_start` / `add_to_middle` / `add_to_end` | [ ] |
| `replace` / `add_component_at_index` / `set_box_sizing` | [ ] |

### FlexLayout
| Feature | Status |
|---------|--------|
| `add` / `remove` / `expand` | [x] |
| `set_flex_direction` / `set_flex_wrap` | [x] |
| `set_justify_content_mode` / `set_align_items` / `set_align_content` | [x] |
| `set_align_self` / `set_flex_grow` / `set_flex_shrink` / `set_flex_basis` | [x] |
| `set_order` / `get_order` | [x] |
| `remove_all` | [x] |
| `replace` / `add_component_at_index` | [ ] |

### FormLayout
| Feature | Status |
|---------|--------|
| `add` / `add_with_colspan` / `remove` | [x] |
| `set_responsive_steps` / `add_form_item` / `add_form_row` | [x] |
| `set_auto_responsive` / `set_auto_rows` / `set_column_width` | [x] |
| `set_max_columns` / `set_min_columns` / `set_expand_columns` / `set_expand_fields` | [x] |
| `set_labels_aside` / `set_label_width` / `set_label_spacing` | [x] |
| `set_column_spacing` / `set_row_spacing` / `set_colspan` | [x] |
| `ResponsiveStep` / `FormItem` / `FormRow` (helper classes) | [x] |
| FormItem: `remove_all` | [x] |

### SplitLayout
| Feature | Status |
|---------|--------|
| `add_to_primary` / `add_to_secondary` | [x] |
| `get_primary_component` / `get_secondary_component` | [x] |
| `set_orientation` / `get_orientation` / `set_splitter_position` / `get_splitter_position` | [x] |
| `set_primary_style` / `set_secondary_style` / `remove_all` | [x] |
| `add_splitter_drag_end_listener` | [x] |
| `remove(component)` | [ ] |

### Scroller
| Feature | Status |
|---------|--------|
| `add` / `set_content` / `get_content` | [x] |
| `set_scroll_direction` / `get_scroll_direction` | [x] |
| `remove_all` | [x] |

### Card
| Feature | Status |
|---------|--------|
| `add` / `set_title` / `get_title` / `set_subtitle` / `get_subtitle` | [x] |
| `set_media` / `set_header` / `set_header_prefix` / `set_header_suffix` | [x] |
| `add_to_footer` | [x] |
| `get_media` / `get_header` / `get_header_prefix` / `get_header_suffix` | [x] |
| `remove_all` | [x] |
| `set_title_heading_level` / `remove` | [ ] |

---

## Field Components

### Common Field Gaps (missing across most/all fields)
| Feature | Status |
|---------|--------|
| `set_read_only` / `is_read_only` | [x] (HasReadOnly mixin) |
| `set_i18n` / `get_i18n` (validation messages) | [ ] |
| `set_value_change_mode` / `set_value_change_timeout` | [ ] |
| `set_aria_label` / `set_aria_labelled_by` | [ ] |
| `add_focus_listener` / `add_blur_listener` | [ ] |

### TextField
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` / `get_placeholder` | [x] |
| `set_clear_button_visible` / `set_prefix_component` | [x] |
| `set_pattern` / `set_allowed_char_pattern` | [x] |
| `set_error_message` / `get_error_message` (HasValidation) | [x] |
| `set_invalid` / `is_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` / `is_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` | [x] |
| `set_max_length` / `get_max_length` / `set_min_length` / `get_min_length` | [ ] |
| `set_suffix_component` / `get_suffix_component` | [ ] |
| `set_autoselect` / `is_autoselect` | [ ] |

### TextArea
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` / `get_placeholder` | [x] |
| `set_max_length` / `set_min_length` / `set_min_rows` / `set_max_rows` | [x] |
| `set_min_height` / `set_max_height` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` | [x] |
| `set_clear_button_visible` | [ ] |
| `set_prefix_component` / `set_suffix_component` | [ ] |
| `set_pattern` | [ ] |

### EmailField
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` / `get_placeholder` | [x] |
| `set_clear_button_visible` / `is_clear_button_visible` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` | [x] |
| `set_pattern` / `set_min_length` / `set_max_length` | [ ] |
| `set_prefix_component` / `set_suffix_component` | [ ] |

### PasswordField
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` / `get_placeholder` | [x] |
| `set_reveal_button_visible` / `is_reveal_button_visible` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` | [x] |
| `set_clear_button_visible` / `set_pattern` | [ ] |
| `set_min_length` / `set_max_length` / `set_prefix_component` | [ ] |

### NumberField / IntegerField
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` / `get_placeholder` | [x] |
| `set_min` / `get_min` / `set_max` / `get_max` / `set_step` / `get_step` | [x] |
| `set_step_buttons_visible` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` | [x] |
| `set_clear_button_visible` | [ ] |
| `set_prefix_component` / `set_suffix_component` | [ ] |

### DatePicker
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` | [x] |
| `set_min` / `set_max` / `set_required` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` | [x] |
| `set_clear_button_visible` / `set_auto_open` | [ ] |
| `set_locale` / `set_week_numbers_visible` / `set_initial_position` | [ ] |
| `open` / `close` / `add_opened_change_listener` | [ ] |

### TimePicker
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` | [x] |
| `set_min` / `set_max` / `set_step` / `set_required` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` | [x] |
| `set_clear_button_visible` / `set_auto_open` | [ ] |
| `add_opened_change_listener` | [ ] |

### DateTimePicker
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` | [x] |
| `set_date_placeholder` / `set_time_placeholder` | [x] |
| `set_min` / `set_max` / `set_step` / `set_required` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` | [x] |
| `set_auto_open` / `set_week_numbers_visible` | [ ] |

### CustomField
| Feature | Status |
|---------|--------|
| `add` / `set_label` / `get_label` | [x] |
| `set_helper_text` / `get_helper_text` | [x] |
| `set_value` / `get_value` / `add_value_change_listener` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `remove_all` | [x] |

---

## Selection Components

### ComboBox
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_value` / `get_value` | [x] |
| `set_label` / `get_label` / `set_placeholder` | [x] |
| `set_page_size` / `set_allow_custom_value` / `set_required` | [x] |
| `set_item_label_generator` / `set_data_provider` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` / `add_custom_value_set_listener` | [x] |
| `set_clear_button_visible` / `set_auto_open` | [ ] |
| `set_renderer` / `set_class_name_generator` | [ ] |
| `set_prefix_component` / `set_overlay_width` | [ ] |

### Select
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_value` / `get_value` | [x] |
| `set_label` / `get_label` / `set_placeholder` / `get_placeholder` | [x] |
| `set_item_label_generator` / `add_value_change_listener` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `set_empty_selection_allowed` / `set_empty_selection_caption` | [ ] |
| `set_renderer` / `set_item_enabled_provider` | [ ] |
| `set_prefix_component` / `set_overlay_width` | [ ] |

### MultiSelectComboBox
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_value` / `get_value` | [x] |
| `select` / `deselect` | [x] |
| `set_label` / `get_label` / `set_placeholder` / `set_page_size` | [x] |
| `set_required` / `set_item_label_generator` / `set_data_provider` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` | [x] |
| `set_clear_button_visible` / `set_auto_open` / `set_allow_custom_value` | [ ] |
| `set_renderer` / `set_auto_expand` / `set_selected_items_on_top` | [ ] |
| `deselect_all` | [ ] |

### ListBox
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_value` / `get_value` | [x] |
| `set_item_label_generator` / `set_item_enabled_provider` | [x] |
| `add_value_change_listener` | [x] |
| `set_renderer` / `add_components` (dividers) | [ ] |

### MultiSelectListBox
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_value` / `get_value` | [x] |
| `set_item_label_generator` / `set_item_enabled_provider` | [x] |
| `add_value_change_listener` | [x] |
| `select` / `deselect` / `deselect_all` | [ ] |
| `set_renderer` / `add_components` (dividers) | [ ] |

### Checkbox
| Feature | Status |
|---------|--------|
| `set_checked` / `is_checked` / `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` | [x] |
| `set_indeterminate` / `is_indeterminate` | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` | [x] |
| `set_label_component` / `set_autofocus` | [ ] |

### CheckboxGroup
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_value` / `get_value` | [x] |
| `set_label` / `get_label` / `set_item_label_generator` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` | [x] |
| `select` / `deselect` / `deselect_all` | [ ] |
| `set_item_enabled_provider` / `set_renderer` | [ ] |
| `add_theme_variants` (LUMO_VERTICAL) | [ ] |

### RadioButtonGroup
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_value` / `get_value` | [x] |
| `set_label` / `get_label` / `set_item_label_generator` | [x] |
| `set_error_message` / `set_invalid` (HasValidation) | [x] |
| `set_required_indicator_visible` (HasRequired) | [x] |
| `add_value_change_listener` | [x] |
| `set_item_enabled_provider` / `set_renderer` | [ ] |
| `add_theme_variants` (LUMO_VERTICAL) | [ ] |

---

## Complex Components

### Grid
| Feature | Status |
|---------|--------|
| `add_column` (property / Renderer) / `set_columns` / `columns` property | [x] |
| `set_items` / `get_items` / `set_data_provider` | [x] |
| `set_page_size` / `set_column_reordering_allowed` / `set_multi_sort` | [x] |
| `set_sort_order` / `add_sort_listener` | [x] |
| `set_selection_mode` / `get_selected_items` / `select_all` / `deselect_all` | [x] |
| `select` / `deselect` (@ClientCallable) | [x] |
| `add_selection_listener` | [x] |
| `prepend_header_row` / `HeaderRow.join` → ColumnGroup | [x] |
| Column: `set_header` / `get_header` / `set_width` / `set_flex_grow` | [x] |
| Column: `set_auto_width` / `set_resizable` / `set_sortable` / `set_text_align` | [x] |
| Column: `set_renderer` / `set_footer_text` | [x] |
| `ComponentRenderer` / `LitRenderer` / `TextRenderer` | [x] |
| `add_item_click_listener` / `add_item_double_click_listener` | [x] |
| `add_component_column` (shortcut) | [ ] |
| `scroll_to_index` / `scroll_to_item` / `recalculate_column_widths` | [ ] |
| Column: `frozen` / `frozen_to_end` / `visible` / `key` | [ ] |
| `get_column_by_key` / `remove_column` / `remove_all_columns` | [ ] |
| `set_item_details_renderer` / `set_details_visible_on_click` | [ ] |
| `append_header_row` / `append_footer_row` / `get_header_rows` | [ ] |
| `set_all_rows_visible` | [ ] |
| Editor API (`get_editor`) | [ ] |
| Drag/drop (`set_rows_draggable` / `set_drop_mode` / listeners) | [ ] |
| `set_empty_state_text` / `set_empty_state_component` | [ ] |

### Dialog
| Feature | Status |
|---------|--------|
| `add` / `open` / `close` / `is_opened` / `set_opened` | [x] |
| `set_modal` / `is_modal` / `set_draggable` / `is_draggable` | [x] |
| `set_resizable` / `is_resizable` | [x] |
| `set_header_title` / `get_header_title` | [x] |
| `set_width` / `set_height` | [x] |
| `set_close_on_esc` / `is_close_on_esc` / `set_close_on_outside_click` / `is_close_on_outside_click` | [x] |
| `add_open_listener` / `add_close_listener` | [x] |
| `get_header` / `get_footer` (section components for buttons) | [x] |
| `remove_all` | [x] |
| `get_width` / `get_height` / `set_min_width` / `set_max_width` etc. | [ ] |
| `set_top` / `set_left` (positioning) | [ ] |
| `remove` | [ ] |
| `add_resize_listener` / `add_dragged_listener` | [ ] |

### ConfirmDialog
| Feature | Status |
|---------|--------|
| `open` / `close` / `is_opened` | [x] |
| `set_header` / `get_header` / `set_text` / `get_text` | [x] |
| `set_confirm_text` / `get_confirm_text` / `set_confirm_button_theme` | [x] |
| `set_cancelable` / `is_cancelable` / `set_cancel_text` / `set_cancel_button_theme` | [x] |
| `set_rejectable` / `is_rejectable` / `set_reject_text` / `set_reject_button_theme` | [x] |
| `add_confirm_listener` / `add_cancel_listener` / `add_reject_listener` | [x] |
| `set_close_on_esc` | [ ] |
| Rich content (Component in header/text) | [ ] |
| `add_opened_change_listener` | [ ] |

### Notification
| Feature | Status |
|---------|--------|
| `open` / `close` / `is_opened` / `set_opened` | [x] |
| `text` / `duration` / `position` / `assertive` (properties) | [x] |
| `add` (component content) / `show` (static) | [x] |
| `add_theme_variants` / `remove_theme_variants` | [x] |
| `add_open_listener` / `add_close_listener` | [x] |
| `remove_all` | [x] |
| `remove` | [ ] |

### Upload
| Feature | Status |
|---------|--------|
| `set_receiver` / `set_max_files` / `get_max_files` | [x] |
| `set_max_file_size` / `get_max_file_size` | [x] |
| `set_auto_upload` / `is_auto_upload` / `set_drop_allowed` / `is_drop_allowed` | [x] |
| `set_accepted_file_types` / `get_accepted_file_types` | [x] |
| `add_succeeded_listener` / `add_failed_listener` | [x] |
| `add_file_rejected_listener` / `add_file_removed_listener` | [x] |
| `set_upload_button` / `set_drop_label` / `set_drop_label_icon` | [ ] |
| `clear_file_list` / `interrupt_upload` | [ ] |
| `set_i18n` / progress / started / all-finished listeners | [ ] |

### LoginForm
| Feature | Status |
|---------|--------|
| `add_login_listener` / `add_forgot_password_listener` | [x] |
| `set_error` / `is_error` | [x] |
| `set_forgot_password_button_visible` / `set_no_autofocus` / `set_action` | [x] |
| `set_i18n` / `set_enabled` | [ ] |

### LoginOverlay
| Feature | Status |
|---------|--------|
| `open` / `close` / `is_opened` | [x] |
| `set_title` / `get_title` / `set_description` / `get_description` | [x] |
| `set_error` / `is_error` / `set_forgot_password_button_visible` | [x] |
| `add_login_listener` / `add_forgot_password_listener` | [x] |
| `set_i18n` / `set_action` / `set_no_autofocus` | [ ] |
| `get_custom_form_area` / `get_footer` | [ ] |

### Popover
| Feature | Status |
|---------|--------|
| `add` / `open` / `close` / `is_opened` / `set_opened` | [x] |
| `set_target` / `get_target` / `set_position` / `get_position` | [x] |
| `set_modal` / `is_modal` | [x] |
| `set_open_on_click` / `set_open_on_hover` / `set_open_on_focus` | [x] |
| `is_open_on_click` / `is_open_on_hover` / `is_open_on_focus` | [x] |
| `set_close_on_esc` / `is_close_on_esc` | [x] |
| `set_close_on_outside_click` / `is_close_on_outside_click` | [x] |
| `add_open_listener` / `add_close_listener` | [x] |
| `set_autofocus` / `set_backdrop_visible` | [ ] |
| `set_hover_delay` / `set_focus_delay` / `set_hide_delay` | [ ] |
| `set_role` / `add_theme_variants` (ARROW, NO_PADDING) | [ ] |
| `remove_all` | [x] |
| `remove` | [ ] |

---

## Navigation & Display Components

### Tabs
| Feature | Status |
|---------|--------|
| `add` / `remove` | [x] |
| `get_selected_tab` / `set_selected_tab` / `get_selected_index` / `set_selected_index` | [x] |
| `get_tab_count` / `set_orientation` / `get_orientation` | [x] |
| `set_autoselect` / `is_autoselect` / `add_selected_change_listener` | [x] |
| `remove_all` | [x] |
| `add_tab_at_index` / `add_tab_as_first` | [ ] |
| `set_flex_grow_for_enclosed_tabs` | [ ] |
| `add_theme_variants` (TabsVariant) | [ ] |

### Tab
| Feature | Status |
|---------|--------|
| `set_label` / `get_label` / `is_selected` | [x] |
| `set_selected` / `set_flex_grow` / `set_enabled` | [ ] |
| `add_theme_variants` (TabVariant) | [ ] |

### TabSheet
| Feature | Status |
|---------|--------|
| `add(label_or_tab, content)` / `remove(tab)` | [x] |
| `get_selected_tab` / `set_selected_tab` / `get_selected_index` / `set_selected_index` | [x] |
| `add_selected_change_listener` | [x] |
| `get_tab_count` / `get_tab_at` / `get_index_of` | [x] |
| `get_tab(content)` / `get_component(tab)` | [ ] |
| `set_prefix_component` (HasPrefix) | [ ] |

### SideNav
| Feature | Status |
|---------|--------|
| `add_item` / `set_label` / `get_label` / `set_collapsible` / `is_collapsible` | [x] |
| `is_expanded` / `set_expanded` | [ ] |
| `set_auto_expand` / `is_auto_expand` | [ ] |
| `get_items` / `remove` / `remove_all` | [ ] |

### SideNavItem
| Feature | Status |
|---------|--------|
| `add_item` / `set_path` / `get_path` / `set_label` / `get_label` | [x] |
| `set_expanded` / `is_expanded` / `set_prefix_component` | [x] |
| `set_match_nested` / `set_router_ignore` | [ ] |
| `set_suffix_component` / `get_items` / `remove` / `remove_all` | [ ] |

### Details
| Feature | Status |
|---------|--------|
| `set_summary_text` / `get_summary_text` / `set_summary` | [x] |
| `set_opened` / `is_opened` / `add_content` | [x] |
| `add_opened_change_listener` | [x] |
| `get_summary` (Component) / `get_content` (Stream) | [ ] |
| `remove` / `remove_all` / `add_component_at_index` | [ ] |
| `add_theme_variants` (DetailsVariant) | [ ] |

### Accordion
| Feature | Status |
|---------|--------|
| `add(summary, content)` / `open(index)` / `close` | [x] |
| `get_opened_index` / `get_opened_panel` / `get_panels` | [x] |
| `add_opened_change_listener` | [x] |
| `add(AccordionPanel)` / `remove(panel)` / `open(panel)` | [ ] |

### MenuBar
| Feature | Status |
|---------|--------|
| `add_item(text, listener)` / `get_items` | [x] |
| `set_open_on_hover` / `is_open_on_hover` | [x] |
| MenuItem: `get_sub_menu` / `set_enabled` / `set_text` / `set_checkable` / `set_checked` | [x] |
| MenuItem: `is_parent_item` / `add_click_listener` | [x] |
| `add_item(Component)` / `remove` / `remove_all` / `close` | [ ] |
| MenuItem: `set_keep_open` / `set_disable_on_click` / `set_aria_label` | [ ] |
| SubMenu: `add_separator` / `remove` / `remove_all` | [ ] |

### ContextMenu
| Feature | Status |
|---------|--------|
| `add_item(text, listener)` / `add_separator` / `get_items` | [x] |
| `set_target` / `get_target` / `set_open_on_click` / `is_open_on_click` | [x] |
| ContextMenuItem: `get_sub_menu` / `set_text` / `set_enabled` / `set_checkable` / `set_checked` | [x] |
| ContextSubMenu: `add_item` / `add_separator` / `get_items` | [x] |
| `add_item(Component)` / `remove` / `remove_all` | [ ] |
| `is_opened` | [ ] |
| `add_opened_change_listener` | [ ] |

### MasterDetailLayout
| Feature | Status |
|---------|--------|
| `set_master` / `get_master` / `set_detail` / `get_detail` | [x] |
| `set_detail_size` / `set_master_min_size` | [x] |
| `set_animation_enabled` / `is_animation_enabled` | [x] |
| `set_overlay_mode` / `set_force_overlay` | [x] |
| `set_orientation` / `get_orientation` / `set_containment` | [ ] |
| `get_detail_size` / `get_master_min_size` / `set_detail_min_size` | [ ] |
| `add_backdrop_click_listener` / `add_detail_escape_press_listener` | [ ] |

---

## Other Components

### Button
| Feature | Status |
|---------|--------|
| `set_text` / `get_text` / `set_icon` | [x] |
| `set_icon_after_text` / `is_icon_after_text` | [x] |
| `add_click_listener` | [x] |
| `set_disable_on_click` / `is_disable_on_click` | [x] |
| `set_autofocus` / `is_autofocus` | [ ] |
| `click` (server-side) / `click_in_client` | [ ] |
| `add_theme_variants` (ButtonVariant) | [ ] |
| `add_focus_listener` / `add_blur_listener` | [ ] |

### Icon
| Feature | Status |
|---------|--------|
| `set_icon` / `get_icon` / `set_color` / `get_color` / `set_size` | [x] |
| `set_icon(collection, icon)` / `get_collection` | [ ] |

### Span (100% complete)
| Feature | Status |
|---------|--------|
| `set_text` / `get_text` | [x] |

### Avatar
| Feature | Status |
|---------|--------|
| `set_name` / `get_name` / `set_abbreviation` / `get_abbreviation` | [x] |
| `set_image` / `get_image` / `set_color_index` / `get_color_index` | [x] |
| AvatarGroup: `set_items` / `get_items` / `set_max_items_visible` / `get_max_items_visible` | [x] |
| `set_image_handler` / `set_i18n` | [ ] |

### ProgressBar (100% complete)
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `set_min` / `get_min` / `set_max` / `get_max` | [x] |
| `set_indeterminate` / `is_indeterminate` | [x] |

### MessageInput
| Feature | Status |
|---------|--------|
| `add_submit_listener` | [x] |
| `set_i18n` | [ ] |

### MessageList (100% complete)
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `add_item` / `append` / `set_markdown` / `is_markdown` | [x] |
| MessageListItem: text, time, userName, userAbbr, userImg, userColorIndex, theme | [x] |

### VirtualList
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_renderer` | [x] |
| `set_data_provider` (lazy loading) | [ ] |

### Markdown (100% complete)
| Feature | Status |
|---------|--------|
| `set_content` / `get_content` / `append_content` | [x] |

### RouterLink
| Feature | Status |
|---------|--------|
| `set_text` / `get_text` / `set_href` / `get_href` | [x] |
| `set_route(view_class)` / `set_query_parameters` | [ ] |

### DrawerToggle (inherits Button — 100%)
| Feature | Status |
|---------|--------|
| Inherits all from Button | [x] |

### HTML Components
| Feature | Status |
|---------|--------|
| H1, H2, H3, H4, Paragraph, Div, Span, Header, Footer | [x] |
| H5, H6, Anchor, NativeLabel, Hr, Pre, IFrame | [ ] |
| Section, Nav, Main, Article, Aside | [ ] |

### Renderer
| Feature | Status |
|---------|--------|
| LitRenderer (`of`, `with_property`, `with_function`) | [x] |
| TextRenderer / ComponentRenderer | [x] |
| NumberRenderer / LocalDateRenderer / LocalDateTimeRenderer | [ ] |
| NativeButtonRenderer / IconRenderer | [ ] |

---

## Data Layer

### Binder
| Feature | Status |
|---------|--------|
| `for_field` / `read_bean` / `write_bean` / `write_bean_if_valid` | [x] |
| `set_bean` / `get_bean` / `is_valid` / `validate` / `is_dirty` | [x] |
| `with_validator` (bean-level cross-field validation) | [x] |
| `add_status_change_listener` | [x] |
| BindingBuilder: `as_required` / `with_validator` / `with_converter` / `bind` | [x] |
| Binding: `clear` / `read` / `validate` / `write` | [x] |
| Validators (StringLength, Email, Regex, Range, Custom) | [x] |
| Converters (StringToInteger, StringToDouble) | [x] |
| `remove_binding` / `remove_bean` | [ ] |

### DataProvider
| Feature | Status |
|---------|--------|
| `ListDataProvider` (in-memory) | [x] |
| `CallbackDataProvider` (lazy) | [x] |
| Filtering / sorting callbacks | [x] |
| `ConfigurableFilterDataProvider` | [ ] |

---

## Events Inventory

### Implemented Events

| Component | Event | Listener Method |
|-----------|-------|-----------------|
| Button | click | `add_click_listener` |
| TextField | value-change | `add_value_change_listener` |
| TextArea | value-change | `add_value_change_listener` |
| EmailField | value-change | `add_value_change_listener` |
| PasswordField | value-change | `add_value_change_listener` |
| NumberField / IntegerField | value-change | `add_value_change_listener` |
| DatePicker | value-change | `add_value_change_listener` |
| TimePicker | value-change | `add_value_change_listener` |
| DateTimePicker | value-change | `add_value_change_listener` |
| CustomField | value-change | `add_value_change_listener` |
| ComboBox | value-change, custom-value-set | `add_value_change_listener`, `add_custom_value_set_listener` |
| Select | value-change | `add_value_change_listener` |
| MultiSelectComboBox | value-change | `add_value_change_listener` |
| ListBox | value-change | `add_value_change_listener` |
| MultiSelectListBox | value-change | `add_value_change_listener` |
| Checkbox | value-change | `add_value_change_listener` |
| CheckboxGroup | value-change | `add_value_change_listener` |
| RadioButtonGroup | value-change | `add_value_change_listener` |
| Grid | selection-change, sort-change | `add_selection_listener`, `add_sort_listener` |
| Dialog | opened-changed | `add_open_listener` / `add_close_listener` |
| ConfirmDialog | confirm, cancel, reject | `add_confirm_listener` / `add_cancel_listener` / `add_reject_listener` |
| Notification | opened-changed | `add_open_listener` / `add_close_listener` |
| Upload | success, error, file-reject, file-remove | 4 listeners |
| LoginForm / LoginOverlay | login, forgot-password | `add_login_listener` / `add_forgot_password_listener` |
| Popover | opened-changed | `add_open_listener` / `add_close_listener` |
| Tabs / TabSheet | selected-changed | `add_selected_change_listener` |
| Details / Accordion | opened-changed | `add_opened_change_listener` |
| SplitLayout | splitter-dragend | `add_splitter_drag_end_listener` |
| MenuBar | item-click | via MenuItem `add_click_listener` |
| ContextMenu | item-click | via ContextMenuItem click handler |
| MessageInput | submit | `add_submit_listener` |
| Grid | item-click | `add_item_click_listener` |
| Grid | item-double-click | `add_item_double_click_listener` |

### Missing Events

#### HIGH Priority

(None — all high-priority events implemented)

#### MEDIUM Priority
| Component | Missing Event | Notes |
|-----------|--------------|-------|
| All fields | focus / blur | `addFocusListener` / `addBlurListener` — validation UX |
| Text fields | key-down | `addKeyDownListener` — Enter-to-submit |
| ComboBox/DatePicker/TimePicker/Select | opened-changed | Overlay open/close tracking |
| Upload | started / progress | Custom progress indicators |
| ConfirmDialog/ContextMenu | opened-changed | Lifecycle tracking |
| Grid | column-resize | Persist column widths |
| MultiSelectComboBox | selection-change | Granular selection info |

#### LOW Priority
| Component | Missing Event | Notes |
|-----------|--------------|-------|
| Grid | cell-focus / column-reorder / drag-drop | Rarely needed |
| Dialog | resize / dragged | Rarely needed |
| Button | focus / blur | Very rare for buttons |

---

## Summary by Completeness

| Category | Components | Count |
|----------|-----------|-------|
| **100%** | ProgressBar, Span, Markdown, MessageList, DrawerToggle | 5 |
| **90-99%** | FormLayout, SplitLayout, FlexLayout, ConfirmDialog, Notification, Avatar, LoginForm, MessageInput, Popover, Accordion, Details, MasterDetailLayout, CustomField, Card, Scroller, Icon, Tabs, TabSheet, Dialog, Grid, Button | 21 |
| **70-89%** | TextField, TextArea, EmailField, PasswordField, NumberField, DatePicker, TimePicker, DateTimePicker, ComboBox, Select, MultiSelectComboBox, Checkbox, CheckboxGroup, RadioButtonGroup, ListBox, MultiSelectListBox, Upload, VirtualList, AppLayout, MenuBar, ContextMenu, SideNav, SideNavItem, VerticalLayout, HorizontalLayout | 25 |
| **50-69%** | LoginOverlay, RouterLink | 2 |

### Recently Implemented (top 5 gaps closed)

1. ~~`set_read_only` / `is_read_only`~~ — [x] HasReadOnly mixin on 18 components
2. ~~`remove_all`~~ — [x] 10 container components
3. ~~Dialog `get_header` / `get_footer`~~ — [x] _DialogSection with slotted children
4. ~~Button `set_disable_on_click`~~ — [x] Client-side double-click prevention
5. ~~Grid `add_item_click_listener`~~ — [x] Item click + double-click events

### Remaining Priority Gaps

1. **Layout `add_component_at_index` / `replace`** — Basic container operations
2. **TextField `set_max_length` / `set_min_length`** — Input length constraints
3. **Select `set_empty_selection_allowed`** — "-- Select --" placeholder pattern
4. **`set_i18n`** — Missing from all components that support it
5. **`set_value_change_mode` / `set_value_change_timeout`** — Debounced text input
