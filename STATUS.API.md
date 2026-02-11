# PyFlow API Inventory — Python vs Java Vaadin 25

**Generated: 2026-02-11**
**Python components: 49 | Tests: 1383 | LOC: ~12,000 (core)**

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
| `set_read_only` / `is_read_only` (HasValueAndElement) | [ ] |
| `set_required_indicator_visible` / `is_required_indicator_visible` (HasValue) | [ ] |
| `remove_all` (HasComponents) | [ ] |

---

## Layout Components

### AppLayout
| Feature | Status |
|---------|--------|
| `add_to_navbar` / `add_to_drawer` / `set_content` | [x] |
| `get_content` / `set_drawer_opened` / `is_drawer_opened` | [x] |
| `set_primary_section` / `show_router_layout_content` | [x] |
| `add_to_navbar(touch_optimized, ...)` | [ ] |
| `get_primary_section` / `is_overlay` | [ ] |
| `remove` / `set_i18n` / `get_i18n` | [ ] |

### VerticalLayout
| Feature | Status |
|---------|--------|
| `add` / `remove` / `expand` | [x] |
| `set_spacing` / `set_padding` / `set_margin` | [x] |
| `set_default_horizontal_component_alignment` | [x] |
| `set_horizontal_component_alignment` | [x] |
| `remove_all` | [ ] |
| `set_wrap` / `is_wrap` | [ ] |
| `set_justify_content_mode` / `get_justify_content_mode` | [ ] |
| `set_align_items` / `get_align_items` | [ ] |
| `set_flex_grow` / `get_flex_grow` / `set_flex_shrink` | [ ] |
| `add_and_expand` / `replace` / `add_component_at_index` | [ ] |
| `set_box_sizing` / `get_box_sizing` | [ ] |

### HorizontalLayout
| Feature | Status |
|---------|--------|
| `add` / `remove` / `expand` | [x] |
| `set_spacing` / `set_margin` | [x] |
| `set_default_vertical_component_alignment` | [x] |
| `set_vertical_component_alignment` | [x] |
| `set_padding` | [ ] |
| `remove_all` / `set_wrap` | [ ] |
| `set_justify_content_mode` / `set_align_items` | [ ] |
| `set_flex_grow` / `set_flex_shrink` | [ ] |
| `add_to_start` / `add_to_middle` / `add_to_end` | [ ] |
| `replace` / `add_component_at_index` / `set_box_sizing` | [ ] |

### FlexLayout (~92% complete)
| Feature | Status |
|---------|--------|
| `add` / `remove` / `expand` | [x] |
| `set_flex_direction` / `set_flex_wrap` | [x] |
| `set_justify_content_mode` / `set_align_items` / `set_align_content` | [x] |
| `set_align_self` / `set_flex_grow` / `set_flex_shrink` / `set_flex_basis` | [x] |
| `set_order` / `get_order` | [x] |
| `remove_all` / `replace` / `add_component_at_index` | [ ] |

### FormLayout (~96% complete)
| Feature | Status |
|---------|--------|
| `add` / `add_with_colspan` / `remove` | [x] |
| `set_responsive_steps` / `add_form_item` / `add_form_row` | [x] |
| `set_auto_responsive` / `set_auto_rows` / `set_column_width` | [x] |
| `set_max_columns` / `set_min_columns` / `set_expand_columns` / `set_expand_fields` | [x] |
| `set_labels_aside` / `set_label_width` / `set_label_spacing` | [x] |
| `set_column_spacing` / `set_row_spacing` / `set_colspan` | [x] |
| `ResponsiveStep` / `FormItem` / `FormRow` (helper classes) | [x] |
| `remove_all` | [ ] |

### SplitLayout (~93% complete)
| Feature | Status |
|---------|--------|
| `add_to_primary` / `add_to_secondary` | [x] |
| `get_primary_component` / `get_secondary_component` | [x] |
| `set_orientation` / `set_splitter_position` | [x] |
| `set_primary_style` / `set_secondary_style` / `remove_all` | [x] |
| `add_splitter_drag_end_listener` | [x] |
| `remove(component)` | [ ] |

### Scroller (~80% complete)
| Feature | Status |
|---------|--------|
| `add` / `set_content` | [x] |
| `set_scroll_direction` / `get_scroll_direction` | [x] |
| `get_content` / `remove_all` | [ ] |

### Card (~45% complete)
| Feature | Status |
|---------|--------|
| `add` / `set_title` / `get_title` | [x] |
| `set_subtitle` / `get_subtitle` | [x] |
| `set_media` / `set_header` / `set_header_prefix` / `set_header_suffix` | [x] |
| `add_to_footer` | [x] |
| `get_media` / `get_header` / `get_header_prefix` / `get_header_suffix` | [ ] |
| `get_footer_components` / `get_title_as_text` | [ ] |
| `set_title_heading_level` / `set_aria_role` | [ ] |
| `remove` / `remove_all` | [ ] |

---

## Field Components

### Common Field Gaps (missing across most/all fields)
| Feature | Status |
|---------|--------|
| `set_read_only` / `is_read_only` | [ ] |
| `set_required_indicator_visible` / `is_required_indicator_visible` | [ ] |
| `set_invalid` / `is_invalid` (most fields) | [ ] |
| `set_i18n` / `get_i18n` (validation messages) | [ ] |
| `set_value_change_mode` / `set_value_change_timeout` | [ ] |
| `set_manual_validation` | [ ] |
| `set_aria_label` / `set_aria_labelled_by` | [ ] |
| `add_focus_listener` / `add_blur_listener` | [ ] |
| Constructor overloads with initial value + listener | [ ] |

### TextField
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `set_placeholder` | [x] |
| `set_clear_button_visible` / `set_prefix_component` | [x] |
| `set_pattern` / `set_allowed_char_pattern` | [x] |
| `set_error_message` / `get_error_message` | [x] |
| `add_value_change_listener` | [x] |
| `get_label` / `get_placeholder` | [ ] |
| `set_suffix_component` / `get_suffix_component` | [ ] |
| `set_min_length` / `set_max_length` | [ ] |
| `set_autoselect` / `is_autoselect` | [ ] |

### TextArea
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` / `get_placeholder` | [x] |
| `set_max_length` / `set_min_length` / `set_min_rows` / `set_max_rows` | [x] |
| `add_value_change_listener` | [x] |
| `set_clear_button_visible` / `set_pattern` | [ ] |
| `set_error_message` / `set_prefix_component` / `set_suffix_component` | [ ] |

### EmailField
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` / `get_placeholder` | [x] |
| `set_error_message` / `get_error_message` / `set_clear_button_visible` | [x] |
| `add_value_change_listener` | [x] |
| `set_pattern` / `set_min_length` / `set_max_length` | [ ] |
| `set_prefix_component` / `set_suffix_component` | [ ] |

### PasswordField
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` / `get_placeholder` | [x] |
| `set_reveal_button_visible` / `is_reveal_button_visible` | [x] |
| `add_value_change_listener` | [x] |
| `set_clear_button_visible` / `set_pattern` / `set_error_message` | [ ] |
| `set_min_length` / `set_max_length` / `set_prefix_component` | [ ] |

### NumberField / IntegerField
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` / `get_placeholder` | [x] |
| `set_min` / `get_min` / `set_max` / `get_max` / `set_step` / `get_step` | [x] |
| `set_step_buttons_visible` | [x] |
| `add_value_change_listener` | [x] |
| `set_clear_button_visible` / `set_error_message` | [ ] |
| `set_prefix_component` / `set_suffix_component` | [ ] |

### DatePicker
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` | [x] |
| `set_min` / `set_max` / `set_required` | [x] |
| `add_value_change_listener` | [x] |
| `set_clear_button_visible` / `set_error_message` | [ ] |
| `set_auto_open` / `set_week_numbers_visible` / `set_initial_position` | [ ] |
| `open` / `close` / `add_opened_change_listener` | [ ] |

### TimePicker
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` / `set_placeholder` | [x] |
| `set_min` / `set_max` / `set_step` / `set_required` | [x] |
| `add_value_change_listener` | [x] |
| `set_clear_button_visible` / `set_error_message` | [ ] |
| `set_auto_open` / `add_opened_change_listener` | [ ] |

### DateTimePicker
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `value` property | [x] |
| `set_label` / `get_label` | [x] |
| `set_date_placeholder` / `set_time_placeholder` | [x] |
| `set_min` / `set_max` / `set_step` / `set_required` | [x] |
| `add_value_change_listener` | [x] |
| `set_error_message` / `set_auto_open` / `set_week_numbers_visible` | [ ] |

### CustomField
| Feature | Status |
|---------|--------|
| `add` / `set_label` / `get_label` | [x] |
| `set_helper_text` / `set_error_message` / `set_invalid` / `is_invalid` | [x] |
| `set_value` / `get_value` / `add_value_change_listener` | [x] |
| Generic value type (Python uses string only) | [ ] |

---

## Selection Components

### ComboBox
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_value` / `get_value` | [x] |
| `set_label` / `get_label` / `set_placeholder` | [x] |
| `set_page_size` / `set_allow_custom_value` / `set_required` | [x] |
| `set_item_label_generator` / `set_data_provider` | [x] |
| `add_value_change_listener` / `add_custom_value_set_listener` | [x] |
| `set_clear_button_visible` / `set_auto_open` | [ ] |
| `set_renderer` / `set_class_name_generator` | [ ] |
| `set_prefix_component` / `set_overlay_width` | [ ] |
| `set_error_message` / `set_invalid` / `is_invalid` | [ ] |

### Select
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_value` / `get_value` | [x] |
| `set_label` / `get_label` / `set_placeholder` / `get_placeholder` | [x] |
| `set_item_label_generator` / `add_value_change_listener` | [x] |
| `set_empty_selection_allowed` / `set_empty_selection_caption` | [ ] |
| `set_renderer` / `set_item_enabled_provider` | [ ] |
| `set_prefix_component` / `set_overlay_width` | [ ] |
| `set_error_message` / `set_invalid` / `set_required` | [ ] |

### MultiSelectComboBox
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_value` / `get_value` | [x] |
| `select` / `deselect` | [x] |
| `set_label` / `get_label` / `set_placeholder` / `set_page_size` | [x] |
| `set_required` / `set_item_label_generator` / `set_data_provider` | [x] |
| `add_value_change_listener` | [x] |
| `set_clear_button_visible` / `set_auto_open` / `set_allow_custom_value` | [ ] |
| `set_renderer` / `set_class_name_generator` | [ ] |
| `set_auto_expand` / `set_selected_items_on_top` | [ ] |
| `deselect_all` / `set_error_message` | [ ] |

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
| `set_checked` / `is_checked` / `set_value` / `get_value` | [x] |
| `set_label` / `get_label` | [x] |
| `set_indeterminate` / `is_indeterminate` | [x] |
| `add_value_change_listener` | [x] |
| `set_required` | [ ] |

### CheckboxGroup
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_value` / `get_value` | [x] |
| `set_label` / `get_label` / `set_item_label_generator` | [x] |
| `add_value_change_listener` | [x] |
| `select` / `deselect` / `deselect_all` | [ ] |
| `set_item_enabled_provider` / `set_renderer` | [ ] |
| `set_error_message` / `set_invalid` / `set_required` | [ ] |
| `add_theme_variants` (LUMO_VERTICAL) | [ ] |

### RadioButtonGroup
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_value` / `get_value` | [x] |
| `set_label` / `get_label` / `set_item_label_generator` | [x] |
| `add_value_change_listener` | [x] |
| `set_item_enabled_provider` / `set_renderer` | [ ] |
| `set_error_message` / `set_invalid` / `set_required` | [ ] |
| `add_theme_variants` (LUMO_VERTICAL) | [ ] |

---

## Complex Components

### Grid
| Feature | Status |
|---------|--------|
| `set_columns` / `add_column` / `set_items` / `get_items` | [x] |
| `set_page_size` / `set_column_reordering_allowed` / `set_multi_sort` | [x] |
| `set_sort_order` / `set_selection_mode` / `get_selected_items` | [x] |
| `select_all` / `deselect_all` / `set_data_provider` | [x] |
| `add_selection_listener` / `add_sort_listener` | [x] |
| Column: `width` / `flex_grow` / `auto_width` / `resizable` / `header` / `sortable` | [x] |
| Column: `set_footer_text` | [x] |
| `ComponentRenderer` / `LitRenderer` / `TextRenderer` | [x] |
| `columns` property / `prepend_header_row` | [x] |
| `HeaderRow.join(*columns)` → `ColumnGroup` / `HeaderCell.set_text` | [x] |
| `set_all_rows_visible` | [ ] |
| Column: `frozen` / `frozen_to_end` / `text_align` / `visible` / `key` | [ ] |
| `get_column_by_key` / `remove_column` | [ ] |
| `set_item_details_renderer` / `set_details_visible` | [ ] |
| `append_header_row` / `append_footer_row` / `get_header_rows` | [ ] |
| `add_item_click_listener` / `add_item_double_click_listener` | [ ] |
| `add_cell_focus_listener` / `add_column_reorder_listener` / `add_column_resize_listener` | [ ] |
| `set_empty_state_text` / `set_empty_state_component` | [ ] |
| `scroll_to_index` / `scroll_to_item` / `recalculate_column_widths` | [ ] |
| Column: `set_tooltip_generator` | [ ] |

### Dialog
| Feature | Status |
|---------|--------|
| `add` / `open` / `close` / `is_opened` / `set_opened` | [x] |
| `set_modal` / `is_modal` / `set_draggable` / `is_draggable` | [x] |
| `set_resizable` / `is_resizable` | [x] |
| `set_header_title` / `get_header_title` | [x] |
| `set_width` / `set_height` (CSS custom properties) | [x] |
| `add_open_listener` / `add_close_listener` | [x] |
| `get_header` / `get_footer` (section components) | [ ] |
| `set_close_on_esc` / `set_close_on_outside_click` | [ ] |
| `set_top` / `set_left` (positioning) | [ ] |
| `remove` / `remove_all` / `add_resize_listener` | [ ] |

### ConfirmDialog (~90% complete)
| Feature | Status |
|---------|--------|
| `open` / `close` / `is_opened` | [x] |
| `set_header` / `get_header` / `set_text` / `get_text` | [x] |
| `set_confirm_text` / `set_confirm_button_theme` | [x] |
| `set_cancelable` / `set_cancel_text` / `set_cancel_button_theme` | [x] |
| `set_rejectable` / `set_reject_text` / `set_reject_button_theme` | [x] |
| `add_confirm_listener` / `add_cancel_listener` / `add_reject_listener` | [x] |
| `set_close_on_esc` | [ ] |
| Rich content (Component in header/text) | [ ] |
| `add_opened_change_listener` | [ ] |

### Notification (~95% complete)
| Feature | Status |
|---------|--------|
| `open` / `close` / `is_opened` / `set_opened` | [x] |
| `text` / `duration` / `position` (properties) | [x] |
| `add` (component content) / `show` (static) | [x] |
| `add_theme_variants` / `remove_theme_variants` | [x] |
| `add_open_listener` / `add_close_listener` | [x] |
| `remove` / `remove_all` | [ ] |

### Upload
| Feature | Status |
|---------|--------|
| `set_receiver` / `set_max_files` / `set_max_file_size` | [x] |
| `set_auto_upload` / `set_drop_allowed` / `set_accepted_file_types` | [x] |
| `add_succeeded_listener` / `add_failed_listener` | [x] |
| `add_file_rejected_listener` / `add_file_removed_listener` | [x] |
| `set_i18n` / `set_upload_button` / `set_drop_label` | [ ] |
| `clear_file_list` / `interrupt_upload` | [ ] |
| Progress/started/all-finished listeners | [ ] |

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
| `set_title` / `set_description` / `set_error` | [x] |
| `add_login_listener` / `add_forgot_password_listener` | [x] |
| `set_forgot_password_button_visible` | [x] |
| `set_i18n` / `set_action` / `set_no_autofocus` | [ ] |
| `get_custom_form_area` / `get_footer` | [ ] |

### Popover
| Feature | Status |
|---------|--------|
| `add` / `open` / `close` / `is_opened` / `set_opened` | [x] |
| `set_target` / `get_target` / `set_position` / `get_position` | [x] |
| `set_modal` / `is_modal` | [x] |
| `set_open_on_click` / `set_open_on_hover` / `set_open_on_focus` | [x] |
| `set_close_on_esc` / `set_close_on_outside_click` | [x] |
| `add_open_listener` / `add_close_listener` | [x] |
| `set_autofocus` / `set_backdrop_visible` | [ ] |
| `set_hover_delay` / `set_focus_delay` / `set_hide_delay` | [ ] |
| `set_role` / `set_aria_label` / `set_aria_labelled_by` | [ ] |
| `add_theme_variants` (ARROW, NO_PADDING) | [ ] |
| `remove` / `remove_all` | [ ] |

---

## Navigation & Display Components

### Tabs
| Feature | Status |
|---------|--------|
| `add` / `remove` | [x] |
| `get_selected_tab` / `set_selected_tab` / `get_selected_index` / `set_selected_index` | [x] |
| `get_tab_count` / `set_orientation` / `set_autoselect` | [x] |
| `add_selected_change_listener` | [x] |
| `remove_all` / `add_tab_at_index` / `add_tab_as_first` | [ ] |
| `get_orientation` / `is_autoselect` | [ ] |
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
| `get_tab_count` / `get_tab_at` / `get_index_of` | [ ] |
| `get_tab(content)` / `get_component(tab)` | [ ] |
| `set_prefix_component` (HasPrefix) | [ ] |

### SideNav
| Feature | Status |
|---------|--------|
| `add_item` / `set_label` / `get_label` / `set_collapsible` | [x] |
| `is_collapsible` / `is_expanded` / `set_expanded` | [ ] |
| `set_auto_expand` / `is_auto_expand` | [ ] |
| `set_i18n` / `get_items` / `remove` / `remove_all` | [ ] |

### SideNavItem
| Feature | Status |
|---------|--------|
| `add_item` / `set_path` / `get_path` / `set_label` / `get_label` | [x] |
| `set_expanded` / `set_prefix_component` | [x] |
| `is_expanded` / `set_match_nested` / `set_router_ignore` | [ ] |
| `set_target` / `set_open_in_new_browser_tab` | [ ] |
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

### Accordion (~70% complete)
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
| `add_item(Component)` / `remove` / `remove_all` / `close` | [ ] |
| `set_reverse_collapse_order` / `set_tab_navigation` | [ ] |
| `set_i18n` / `add_theme_variants` (MenuBarVariant) | [ ] |
| MenuItem: `set_keep_open` / `set_disable_on_click` / `set_aria_label` | [ ] |
| SubMenu: `add_separator` / `remove` / `remove_all` | [ ] |

### ContextMenu
| Feature | Status |
|---------|--------|
| `add_item(text, listener)` / `add_separator` / `get_items` | [x] |
| `set_target` / `set_open_on_click` | [x] |
| ContextMenuItem: `get_sub_menu` / `set_text` / `set_enabled` / `set_checkable` / `set_checked` | [x] |
| ContextSubMenu: `add_item` / `add_separator` / `get_items` | [x] |
| `add_item(Component)` / `remove` / `remove_all` | [ ] |
| `get_target` / `is_open_on_click` / `is_opened` | [ ] |
| `set_position` / `add_opened_change_listener` | [ ] |
| ContextMenuItem: `set_keep_open` / `set_disable_on_click` | [ ] |

### MasterDetailLayout (~33% complete)
| Feature | Status |
|---------|--------|
| `set_master` / `get_master` / `set_detail` / `get_detail` | [x] |
| `set_detail_size` / `set_master_min_size` | [x] |
| `set_orientation` / `get_orientation` | [ ] |
| `set_containment` / `set_overlay_mode` / `set_force_overlay` | [ ] |
| `set_animation_enabled` / `is_animation_enabled` | [ ] |
| `get_detail_size` / `get_master_min_size` / `set_detail_min_size` | [ ] |
| `add_backdrop_click_listener` / `add_detail_escape_press_listener` | [ ] |

---

## Other Components

### Button
| Feature | Status |
|---------|--------|
| `set_text` / `get_text` / `set_icon` | [x] |
| `add_click_listener` | [x] |
| `get_icon` / `set_icon_after_text` | [ ] |
| `set_autofocus` / `set_disable_on_click` | [ ] |
| `click` (server-side) / `click_in_client` | [ ] |
| `add_theme_variants` (ButtonVariant) | [ ] |

### Icon (~80% complete)
| Feature | Status |
|---------|--------|
| `set_icon` / `get_icon` / `set_color` / `set_size` | [x] |
| `get_color` / `set_icon(collection, icon)` / `get_collection` | [ ] |

### Span (100% complete)
| Feature | Status |
|---------|--------|
| `set_text` / `get_text` | [x] |

### Avatar (~90% complete)
| Feature | Status |
|---------|--------|
| `set_name` / `get_name` / `set_abbreviation` / `get_abbreviation` | [x] |
| `set_image` / `get_image` / `set_color_index` / `get_color_index` | [x] |
| AvatarGroup: `set_items` / `set_max_items_visible` | [x] |
| `set_image_handler` / `set_i18n` | [ ] |

### ProgressBar (100% complete)
| Feature | Status |
|---------|--------|
| `set_value` / `get_value` / `set_min` / `get_min` / `set_max` / `get_max` | [x] |
| `set_indeterminate` / `is_indeterminate` | [x] |

### MessageInput (~90% complete)
| Feature | Status |
|---------|--------|
| `add_submit_listener` | [x] |
| `set_i18n` | [ ] |

### MessageList (100% complete)
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_markdown` | [x] |
| MessageListItem: text, time, userName, userAbbr, userImg, userColorIndex, theme | [x] |

### VirtualList (~85% complete)
| Feature | Status |
|---------|--------|
| `set_items` / `get_items` / `set_renderer` | [x] |
| `set_data_provider` (lazy loading) | [ ] |

### Markdown (100% complete)
| Feature | Status |
|---------|--------|
| `set_content` / `get_content` | [x] |

### RouterLink (~50% complete)
| Feature | Status |
|---------|--------|
| `set_text` / `get_text` / `set_href` / `get_href` | [x] |
| `set_route(view_class)` / `set_query_parameters` | [ ] |
| `set_highlight_condition` / `set_highlight_action` | [ ] |

### DrawerToggle (~95% complete)
| Feature | Status |
|---------|--------|
| Inherits all from Button | [x] |

### HTML Components (~70%)
| Feature | Status |
|---------|--------|
| H1, H2, H3, H4, Paragraph, Div, Header, Footer, Image | [x] |
| H5, H6, Anchor, NativeLabel, Hr, Pre, IFrame | [ ] |
| Section, Nav, Main, Article, Aside | [ ] |

### Renderer (~70%)
| Feature | Status |
|---------|--------|
| LitRenderer (of, with_property, with_function) | [x] |
| TextRenderer / ComponentRenderer | [x] |
| NumberRenderer / LocalDateRenderer / LocalDateTimeRenderer | [ ] |
| NativeButtonRenderer / IconRenderer | [ ] |

---

## Data Layer

### Binder
| Feature | Status |
|---------|--------|
| `bind` / `for_field` / `read_bean` / `write_bean` | [x] |
| `set_bean` / `get_bean` / `is_valid` / `validate` | [x] |
| `add_value_change_listener` / `add_status_change_listener` | [x] |
| Validators (StringLength, Email, Regex, Range, Custom) | [x] |
| Converters (StringToInteger, StringToDouble) | [x] |
| `remove_binding` / `remove_bean` | [ ] |
| Cross-field validation | [ ] |

### DataProvider
| Feature | Status |
|---------|--------|
| `ListDataProvider` (in-memory) | [x] |
| `CallbackDataProvider` (lazy) | [x] |
| Filtering / sorting callbacks | [x] |
| `ConfigurableFilterDataProvider` | [ ] |

---

## Events Inventory

### Implemented Events (per component)

| Component | Event | Listener Method |
|-----------|-------|-----------------|
| Button | click | `add_click_listener` |
| TextField | value-change | `add_value_change_listener` |
| TextArea | value-change | `add_value_change_listener` |
| EmailField | value-change | `add_value_change_listener` |
| PasswordField | value-change | `add_value_change_listener` |
| NumberField | value-change | `add_value_change_listener` |
| IntegerField | value-change | `add_value_change_listener` |
| DatePicker | value-change | `add_value_change_listener` |
| TimePicker | value-change | `add_value_change_listener` |
| DateTimePicker | value-change | `add_value_change_listener` |
| CustomField | value-change | `add_value_change_listener` |
| ComboBox | value-change | `add_value_change_listener` |
| ComboBox | custom-value-set | `add_custom_value_set_listener` |
| Select | value-change | `add_value_change_listener` |
| MultiSelectComboBox | value-change | `add_value_change_listener` |
| ListBox | value-change | `add_value_change_listener` |
| MultiSelectListBox | value-change | `add_value_change_listener` |
| Checkbox | value-change | `add_value_change_listener` |
| CheckboxGroup | value-change | `add_value_change_listener` |
| RadioButtonGroup | value-change | `add_value_change_listener` |
| Grid | selection-change | `add_selection_listener` |
| Grid | sort-change | `add_sort_listener` |
| Dialog | opened-changed | `add_open_listener` / `add_close_listener` |
| ConfirmDialog | confirm | `add_confirm_listener` |
| ConfirmDialog | cancel | `add_cancel_listener` |
| ConfirmDialog | reject | `add_reject_listener` |
| Notification | opened-changed | `add_open_listener` / `add_close_listener` |
| Upload | upload-success | `add_succeeded_listener` |
| Upload | upload-error | `add_failed_listener` |
| Upload | file-reject | `add_file_rejected_listener` |
| Upload | file-remove | `add_file_removed_listener` |
| LoginForm | login | `add_login_listener` |
| LoginForm | forgot-password | `add_forgot_password_listener` |
| LoginOverlay | login | `add_login_listener` |
| LoginOverlay | forgot-password | `add_forgot_password_listener` |
| Popover | opened-changed | `add_open_listener` / `add_close_listener` |
| Tabs | selected-changed | `add_selected_change_listener` |
| TabSheet | selected-changed | `add_selected_change_listener` |
| Details | opened-changed | `add_opened_change_listener` |
| Accordion | opened-changed | `add_opened_change_listener` |
| SplitLayout | splitter-dragend | `add_splitter_drag_end_listener` |
| MenuBar | item-click | via MenuItem `add_click_listener` |
| ContextMenu | item-click | via ContextMenuItem click handler |
| MessageInput | submit | `add_submit_listener` |

### Missing Events

#### HIGH Priority (commonly used in apps)

| Component | Missing Event | Java Method | Notes |
|-----------|--------------|-------------|-------|
| Grid | item-click | `addItemClickListener` | Row click handling — very common |
| Grid | item-double-click | `addItemDoubleClickListener` | Edit-on-double-click pattern |

#### MEDIUM Priority (occasionally useful)

| Component | Missing Event | Java Method | Notes |
|-----------|--------------|-------------|-------|
| TextField | focus | `addFocusListener` (Focusable) | Validation UX |
| TextField | blur | `addBlurListener` (Focusable) | Validation UX |
| TextField | key-down | `addKeyDownListener` (KeyNotifier) | Enter-to-submit pattern |
| TextArea | focus | `addFocusListener` (Focusable) | Validation UX |
| TextArea | blur | `addBlurListener` (Focusable) | Validation UX |
| TextArea | key-down | `addKeyDownListener` (KeyNotifier) | Enter-to-submit pattern |
| EmailField | focus / blur | `addFocusListener` / `addBlurListener` | Validation UX |
| PasswordField | focus / blur | `addFocusListener` / `addBlurListener` | Validation UX |
| NumberField | focus / blur | `addFocusListener` / `addBlurListener` | Validation UX |
| IntegerField | focus / blur | `addFocusListener` / `addBlurListener` | Validation UX |
| ComboBox | focus / blur | `addFocusListener` / `addBlurListener` | |
| ComboBox | opened-changed | `addOpenedChangeListener` | Overlay open/close tracking |
| DatePicker | focus / blur | `addFocusListener` / `addBlurListener` | |
| DatePicker | opened-changed | `addOpenedChangeListener` | Overlay open/close tracking |
| TimePicker | focus / blur | `addFocusListener` / `addBlurListener` | |
| TimePicker | opened-changed | `addOpenedChangeListener` | Overlay open/close tracking |
| Select | focus / blur | `addFocusListener` / `addBlurListener` | |
| Select | opened-changed | `addOpenedChangeListener` | Overlay open/close tracking |
| MultiSelectComboBox | focus / blur | `addFocusListener` / `addBlurListener` | |
| MultiSelectComboBox | selection-change | `addSelectionListener` | Granular selection info |
| Grid | column-resize | `addColumnResizeListener` | Persist column widths |
| ConfirmDialog | opened-changed | `addOpenedChangeListener` | Lifecycle tracking |
| ContextMenu | opened-changed | `addOpenedChangeListener` | Overlay open/close tracking |
| Upload | upload-start | `addStartedListener` | Show progress UI |
| Upload | upload-progress | `addProgressListener` | Custom progress bars |

#### LOW Priority (rarely needed)

| Component | Missing Event | Java Method | Notes |
|-----------|--------------|-------------|-------|
| All fields | invalid-changed | via HasValidation | Rarely used directly |
| All text fields | input | CompositionNotifier | Real-time typing events |
| TextField | key-press / key-up | KeyNotifier | Rarely needed |
| TextArea | key-press / key-up | KeyNotifier | Rarely needed |
| Grid | cell-focus | `addCellFocusListener` | Cell-level focus tracking |
| Grid | column-reorder | `addColumnReorderListener` | Column reorder tracking |
| Grid | drag-start / drag-end / drop | Drag listeners | Row drag-and-drop |
| Dialog | resize | `addResizeListener` | Dialog resize tracking |
| Upload | upload-finished | `addFinishedListener` | Covered by success/error |
| Upload | all-finished | `addAllFinishedListener` | Batch completion |
| Button | focus / blur | `addFocusListener` / `addBlurListener` | Very rare for buttons |
| Checkbox | indeterminate-changed | via HasValue | Rare use case |

### Event Statistics

| Metric | Count |
|--------|-------|
| Total unique event types in Java | ~55 |
| Events implemented in Python | ~30 |
| Events missing from Python | ~25 |
| HIGH priority gaps | 2 |
| MEDIUM priority gaps | ~15 |
| LOW priority gaps | ~8 |

### Recommended Implementation Order

1. **Grid `item-click` / `item-double-click`** — Most impactful, very commonly used
2. **Focus/Blur mixin** — A base `Focusable` mixin would cover ~10 field components at once
3. **KeyDown on text fields** — Needed for Enter-to-submit patterns
4. **Upload started/progress** — Useful for custom upload progress indicators
5. **Opened-changed on overlay fields** (ComboBox, DatePicker, TimePicker, Select, ContextMenu) — Occasionally useful
6. **Grid column-resize** — Useful for persisting user column width preferences
7. **ConfirmDialog opened-changed** — Lifecycle tracking

---

## Summary by Completeness

| Category | Components | Avg Coverage |
|----------|-----------|-------------|
| **100% complete** | ProgressBar, Span, Markdown, MessageList | 4 |
| **90-99%** | FormLayout, SplitLayout, FlexLayout, ConfirmDialog, Notification, DrawerToggle, Avatar, LoginForm, MessageInput | 9 |
| **70-89%** | Scroller, Accordion, Upload, Icon, VirtualList, Details | 6 |
| **50-69%** | TextField, TextArea, EmailField, PasswordField, NumberField, DatePicker, TimePicker, DateTimePicker, ComboBox, Select, MultiSelectComboBox, Checkbox, ListBox, MultiSelectListBox, Grid, Dialog, Popover, Tabs, TabSheet, Button, RouterLink | 21 |
| **30-49%** | VerticalLayout, HorizontalLayout, Card, SideNav, SideNavItem, MenuBar, ContextMenu, CheckboxGroup, RadioButtonGroup, MasterDetailLayout, LoginOverlay | 11 |

### Top Priority Gaps (cross-cutting)

1. **`setReadOnly` / `isReadOnly`** — Missing from all field/selection components
2. **`setRequiredIndicatorVisible`** — Missing from all fields
3. **`setInvalid` / `isInvalid` / `setErrorMessage`** — Missing from most fields
4. **`removeAll`** — Missing from most container components
5. **`setI18n`** — Missing from all components that support it
6. **Focus/Blur events** — Missing from all components
7. **ARIA accessibility** (`setAriaLabel`, `setAriaLabelledBy`) — Missing everywhere
8. **`setValueChangeMode`** — Missing from all text-based fields
9. **`setClearButtonVisible`** — Missing from several fields
10. **`setPrefixComponent` / `setSuffixComponent`** — Missing from most fields
