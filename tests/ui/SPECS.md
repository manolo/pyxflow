# UI Test Specifications — PyFlow

## Test Infrastructure

- **Framework:** Playwright (Python)
- **Server:** PyFlow test app at `http://localhost:8088` (`python -m tests`)
- **Layout:** All test views in `tests/views/` share `TestMainLayout` (HorizontalLayout with SideNav + content area)
- **Navigation:** SPA navigation via SideNav clicks; `navigate_to()` helper with `page.goto()` fallback
- **Shared page:** Single browser context reused across all 29 test modules (session-scoped `shared_page` fixture)
- **Fail-fast:** If >4 consecutive tests fail, abort the entire suite
- **Parallelism:** Views are independent; tests within a view run sequentially
- **IDs:** Every testable component gets `set_id("xxx")` for fast `#xxx` selectors

## View Map

| # | Route | Tests | Components |
|---|-------|-------|------------|
| 1 | `/test/buttons-icons` | 17 | Button, Icon, DrawerToggle |
| 2 | `/test/text-inputs` | 26 | TextField, TextArea, PasswordField, EmailField |
| 3 | `/test/number-inputs` | 14 | NumberField, IntegerField |
| 4 | `/test/checkbox-radio` | 21 | Checkbox, CheckboxGroup, RadioButtonGroup |
| 5 | `/test/select-listbox` | 17 | Select, ListBox, MultiSelectListBox |
| 6 | `/test/combo-box` | 16 | ComboBox, MultiSelectComboBox |
| 7 | `/test/date-time` | 20 | DatePicker, TimePicker, DateTimePicker |
| 8 | `/test/grid-basic` | 14 | Grid (columns, data, renderers) |
| 9 | `/test/grid-features` | 17 | Grid (selection, sorting, click, columns ops, details) |
| 10 | `/test/tree-grid` | 5 | TreeGrid |
| 11 | `/test/dialog` | 14 | Dialog, ConfirmDialog |
| 12 | `/test/notification-popover` | 9 | Notification, Popover |
| 13 | `/test/tabs-accordion` | 15 | Tabs, TabSheet, Accordion, Details |
| 14 | `/test/menu` | 10 | MenuBar, ContextMenu |
| 15 | `/test/layouts` | 12 | VerticalLayout, HorizontalLayout, FlexLayout, FormLayout, SplitLayout |
| 16 | `/test/card-scroller` | 11 | Card, Scroller, MasterDetailLayout |
| 17 | `/test/upload` | 5 | Upload |
| 18 | `/test/display` | 15 | ProgressBar, Avatar, AvatarGroup, Markdown, MessageInput, MessageList |
| 19 | `/test/html-elements` | 21 | H1-H6, Paragraph, Span, Div, Anchor, IFrame, Hr, Pre, Image, NativeLabel |
| 20 | `/test/component-api` | 18 | Base Component API (visibility, enabled, classes, styles, size, tooltip, aria, theme) |
| 21 | `/test/field-mixins` | 13 | HasReadOnly, HasValidation, HasRequired |
| 22 | `/test/binder` | 20 | Binder, validators, converters, dirty tracking, field types |
| 23 | `/test/navigation` | 10 | @Route, params, AppLayout, SideNav, RouterLink, page title |
| 24 | `/test/push` | 8 | WebSocket push, UI.access() |
| 25 | `/test/theme` | 8 | Theme switching, @StyleSheet, @ColorScheme |
| 26 | `/test/client-callable` | 3 | @ClientCallable |
| 27 | `/test/custom-field` | 6 | CustomField |
| 28 | `/test/virtual-list` | 5 | VirtualList |
| 29 | `/test/login` | 8 | LoginForm, LoginOverlay |
| 30 | `/test/server-errors` | 8 | Error notification, meta.appError, JSON serialization, session resilience |

**Total: 386 tests across 30 views (386 pass, 0 skip)**

---

## Global: Test Runner Config

```
Rule: Fail-fast on 4+ consecutive failures
  - Track consecutive failure count globally
  - On each pass, reset counter to 0
  - On each fail, increment counter
  - When counter > 4, abort suite with "ABORT: 4+ consecutive failures"
```

---

## View 1: `/test/buttons-icons`

```gherkin
Feature: Button & Icon

  # --- Button basics ---
  Scenario: V01.01 — Button renders with text
    Given Button("Click me") with id="btn1"
    Then "#btn1" text is "Click me"

  Scenario: V01.02 — Button click fires listener
    Given Button with click listener that sets Span#result text to "clicked"
    When click "#btn1"
    Then "#result" text is "clicked"

  Scenario: V01.03 — Button set_text updates label
    Given Button("Old") with click listener calling set_text("New")
    When click "#btn-text"
    Then "#btn-text" text is "New"

  Scenario: V01.04 — Button disabled state
    Given Button with id="btn-dis" set_enabled(False)
    Then "#btn-dis" has attribute "disabled"

  Scenario: V01.05 — Button set_disable_on_click
    Given Button with set_disable_on_click(True), click listener sets Span#result2
    When click "#btn-doc"
    Then "#btn-doc" has attribute "disabled"
    And "#result2" text is "clicked"

  Scenario: V01.06 — Button autofocus
    Given Button with set_autofocus(True)
    Then "#btn-auto" is focused

  Scenario: V01.07 — Button click() programmatic
    Given Button#btn-prog with click listener → Span#result3="prog"
    And a second Button#trigger whose click calls btn_prog.click()
    When click "#trigger"
    Then "#result3" text is "prog"

  # --- Icon ---
  Scenario: V01.08 — Icon renders with vaadin icon
    Given Icon("lumo:plus") with id="icon1"
    Then "#icon1" exists as vaadin-icon

  Scenario: V01.09 — Icon set_color
    Given Icon with set_color("red")
    Then "#icon-color" has style "fill" containing "red" or color is red

  Scenario: V01.10 — Icon set_size
    Given Icon with set_size("32px")
    Then "#icon-size" has style width/height "32px"

  # --- Button + Icon ---
  Scenario: V01.11 — Button with icon in prefix
    Given Button("Save", icon=Icon("lumo:plus"))
    Then "#btn-icon" contains vaadin-icon with slot="prefix"

  Scenario: V01.12 — Button icon after text
    Given Button("Save", icon=Icon("lumo:plus")), set_icon_after_text(True)
    Then icon has slot="suffix"

  Scenario: V01.13 — Button icon-only (no text)
    Given Button(icon=Icon("lumo:plus"))
    Then "#btn-icononly" has theme "icon"

  # --- Click shortcut ---
  Scenario: V01.14 — Button add_click_shortcut
    Given Button#btn-short with add_click_shortcut(Key.ENTER), listener → Span#result4
    When press Enter key
    Then "#result4" text contains "shortcut:"

  Scenario: V01.18 — Button shortcut with TextField value sync
    Given TextField#short-field and Button#btn-field-short with add_click_shortcut(Key.ENTER)
    When type "hello" in "#short-field" and press Enter
    Then "#result6" text contains "filtered:hello:1"
    And pressing Enter again shows counter incremented to 2

  # --- DrawerToggle ---
  Scenario: V01.15 — DrawerToggle renders
    Given DrawerToggle() with id="toggle1"
    Then "#toggle1" is a vaadin-drawer-toggle

  Scenario: V01.16 — DrawerToggle click fires
    Given DrawerToggle with click listener → Span#result5
    When click "#toggle1"
    Then "#result5" text is "toggled"

  # --- Nav link ---
  Scenario: V01.17 — Nav to next view
    When click link "Next: Text Inputs"
    Then URL contains "/test/text-inputs"
```

---

## View 2: `/test/text-inputs`

```gherkin
Feature: Text Input Fields

  # --- TextField ---
  Scenario: V02.01 — TextField renders with label
    Given TextField("Name") with id="tf1"
    Then "#tf1" label is "Name"

  Scenario: V02.02 — TextField type and read value
    When type "hello" into "#tf1"
    Then value-changed event fires with value "hello"
    And Span#tf1-val text is "hello"

  Scenario: V02.03 — TextField set_value programmatic
    Given TextField with set_value("preset")
    Then "#tf-preset" input value is "preset"

  Scenario: V02.04 — TextField set_placeholder
    Given TextField with set_placeholder("Enter name...")
    Then "#tf-ph" has placeholder "Enter name..."

  Scenario: V02.05 — TextField set_clear_button_visible
    Given TextField with value "abc" and set_clear_button_visible(True)
    Then clear button is visible in "#tf-clear"
    When click clear button
    Then value is ""

  Scenario: V02.06 — TextField set_max_length
    Given TextField with set_max_length(5)
    When type "abcdefgh" into "#tf-max"
    Then input value length <= 5

  Scenario: V02.07 — TextField set_pattern (client validation)
    Given TextField with set_pattern("[0-9]+")
    When type "abc" into "#tf-pat" and blur
    Then "#tf-pat" has attribute "invalid"

  Scenario: V02.08 — TextField set_allowed_char_pattern
    Given TextField with set_allowed_char_pattern("[0-9]")
    When type "a1b2" into "#tf-acp"
    Then input value is "12" (letters blocked)

  Scenario: V02.09 — TextField prefix/suffix components
    Given TextField with set_prefix_component(Icon("lumo:search"))
    And set_suffix_component(Span("kg"))
    Then "#tf-fix" contains prefix icon and suffix span

  Scenario: V02.10 — TextField set_value_change_mode EAGER
    Given TextField with ValueChangeMode.EAGER, listener updates Span#tf-eager
    When type "ab" character by character
    Then Span#tf-eager updates after each character

  # --- TextArea ---
  Scenario: V02.11 — TextArea renders with label
    Given TextArea("Bio") with id="ta1"
    Then "#ta1" label is "Bio"

  Scenario: V02.12 — TextArea type and read value
    When type "line1\nline2" into "#ta1"
    Then value contains "line1" and "line2"

  Scenario: V02.13 — TextArea set_min_rows / set_max_rows
    Given TextArea with set_min_rows(3), set_max_rows(6)
    Then textarea renders with minimum 3 rows height

  Scenario: V02.14 — TextArea set_clear_button_visible
    Given TextArea with value, set_clear_button_visible(True)
    When click clear button
    Then value is ""

  # --- PasswordField ---
  Scenario: V02.15 — PasswordField renders
    Given PasswordField("Password") with id="pf1"
    Then "#pf1" input type is "password"

  Scenario: V02.16 — PasswordField type and read
    When type "secret123" into "#pf1"
    Then Span#pf1-val text is "secret123"

  Scenario: V02.17 — PasswordField reveal button
    Given PasswordField with set_reveal_button_visible(True)
    Then reveal button is visible
    When click reveal button
    Then input type changes to "text" (value visible)

  Scenario: V02.18 — PasswordField hide reveal button
    Given PasswordField with set_reveal_button_visible(False)
    Then reveal button is NOT visible

  # --- EmailField ---
  Scenario: V02.19 — EmailField renders with label
    Given EmailField("Email") with id="ef1"
    Then "#ef1" label is "Email"

  Scenario: V02.20 — EmailField client validation
    When type "not-an-email" into "#ef1" and blur
    Then "#ef1" shows invalid state

  Scenario: V02.21 — EmailField valid email
    When type "user@example.com" into "#ef-valid" and blur
    Then "#ef-valid" is NOT invalid

  Scenario: V02.22 — EmailField value-change
    When type "a@b.com" into "#ef1"
    Then Span#ef1-val text is "a@b.com"

  # --- Shared field features ---
  Scenario: V02.23 — TextField helper text
    Given TextField with set_helper_text("Min 3 chars")
    Then "#tf-help" shows helper text "Min 3 chars"

  Scenario: V02.24 — TextField tooltip
    Given TextField with set_tooltip_text("Full name")
    Then "#tf-tip" has tooltip "Full name"

  Scenario: V02.25 — TextField autoselect
    Given TextField with value "hello", set_autoselect(True)
    When click/focus "#tf-sel"
    Then text is selected

  Scenario: V02.26 — TextField set_label changes label
    Given TextField("Old") with Button that calls tf.set_label("New")
    When click button
    Then "#tf-lbl" label is "New"

  # --- Shared text field value_change_timeout ---
  Scenario: V02.27 — TextField value_change_timeout with LAZY mode
    Given TextField, ValueChangeMode.LAZY, timeout=500
    When type "abc" rapidly
    Then only one value-change event fires after 500ms pause

  # --- Value roundtrip (mSync regression) ---
  Scenario: V02.28 — TextField value preserved after focus/blur cycle
    Given TextField#tf-round with value "hello"
    When click "#tf-round" to focus, then click elsewhere to blur
    Then get_value() still returns "hello" (not None)
    And Span#tf-round-val text is "hello"

  Scenario: V02.29 — TextField required client-side validation
    Given TextField#tf-req with set_required_indicator_visible(True)
    When focus "#tf-req", leave empty, blur
    Then "#tf-req" shows invalid state (client validates required)

  Scenario: V02.30 — TextField clear and re-type same value
    Given TextField#tf-same with value "test"
    When clear field, type "test" again, blur
    Then value-change fires and Span#tf-same-val text is "test"

  Scenario: V02.31 — TextArea set_max_length
    Given TextArea with set_max_length(50)
    When type more than 50 characters
    Then input is limited to 50 characters

  Scenario: V02.32 — TextField set_value then user edits
    Given TextField with set_value("initial"), value_change_listener
    When user clears and types "edited"
    Then value-change event has from_client=True and value="edited"

  # --- Nav ---
  Scenario: V02.33 — Nav to next view
    When click link "Next: Number Inputs"
    Then URL contains "/test/number-inputs"
```

---

## View 3: `/test/number-inputs`

```gherkin
Feature: Number & Integer Fields

  # --- NumberField ---
  Scenario: V03.01 — NumberField renders with label
    Given NumberField("Price") with id="nf1"
    Then "#nf1" label is "Price"

  Scenario: V03.02 — NumberField type numeric value
    When type "42.5" into "#nf1"
    Then Span#nf1-val text is "42.5"

  Scenario: V03.03 — NumberField set_value programmatic
    Given NumberField with set_value(99.9)
    Then "#nf-pre" value is "99.9"

  Scenario: V03.04 — NumberField set_min/set_max client validation
    Given NumberField with set_min(0), set_max(100)
    When type "150" and blur
    Then "#nf-range" is invalid

  Scenario: V03.05 — NumberField set_step
    Given NumberField with set_step(0.5)
    Then step attribute is "0.5"

  Scenario: V03.06 — NumberField step buttons visible
    Given NumberField with set_step_buttons_visible(True)
    Then increment/decrement buttons visible in "#nf-step"
    When click increment
    Then value increases by step

  Scenario: V03.07 — NumberField clear button
    Given NumberField with value, set_clear_button_visible(True)
    When click clear
    Then value is None/empty

  Scenario: V03.08 — NumberField prefix/suffix
    Given NumberField with prefix=Icon("lumo:dollar"), suffix=Span("USD")
    Then prefix and suffix render

  # --- IntegerField ---
  Scenario: V03.09 — IntegerField renders
    Given IntegerField("Qty") with id="if1"
    Then "#if1" label is "Qty"

  Scenario: V03.10 — IntegerField accepts only integers
    When type "42" into "#if1"
    Then Span#if1-val text is "42" (int, not float)

  Scenario: V03.11 — IntegerField rejects decimal input
    When type "3.14" into "#if-dec"
    Then only "3" is accepted (client blocks ".")

  Scenario: V03.12 — IntegerField set_value programmatic
    Given IntegerField with set_value(7)
    Then "#if-pre" value is "7"

  Scenario: V03.13 — IntegerField step buttons
    Given IntegerField with set_step(2), set_step_buttons_visible(True)
    When click increment twice
    Then value is initial + 4

  Scenario: V03.14 — IntegerField min/max
    Given IntegerField with set_min(1), set_max(10)
    When type "15" and blur
    Then invalid

  # --- Nav ---
  Scenario: V03.15 — Nav to next view
    When click link "Next: Checkbox & Radio"
    Then URL contains "/test/checkbox-radio"
```

---

## View 4: `/test/checkbox-radio`

```gherkin
Feature: Checkbox & RadioButtonGroup

  # --- Checkbox ---
  Scenario: V04.01 — Checkbox renders with label
    Given Checkbox("Accept terms") with id="cb1"
    Then "#cb1" label is "Accept terms"

  Scenario: V04.02 — Checkbox click toggles value
    When click "#cb1"
    Then Span#cb1-val text is "True"
    When click "#cb1" again
    Then Span#cb1-val text is "False"

  Scenario: V04.03 — Checkbox set_value programmatic
    Given Checkbox with set_value(True)
    Then "#cb-pre" is checked

  Scenario: V04.04 — Checkbox set_indeterminate
    Given Checkbox with set_indeterminate(True)
    Then "#cb-ind" shows indeterminate state

  Scenario: V04.05 — Checkbox set_label changes label
    Given Checkbox("Old"), Button that calls cb.set_label("New")
    When click button
    Then "#cb-lbl" label is "New"

  Scenario: V04.06 — Checkbox set_read_only
    Given Checkbox with set_read_only(True)
    Then "#cb-ro" has readonly attribute
    When click "#cb-ro"
    Then value does NOT change

  Scenario: V04.07 — Checkbox required indicator
    Given Checkbox with set_required_indicator_visible(True)
    Then "#cb-req" shows required indicator

  # --- CheckboxGroup ---
  Scenario: V04.08 — CheckboxGroup renders items
    Given CheckboxGroup("Colors") with set_items("Red", "Green", "Blue")
    Then 3 checkboxes rendered inside "#cbg1"

  Scenario: V04.09 — CheckboxGroup select multiple
    When check "Red" and "Blue"
    Then Span#cbg1-val text contains "Red" and "Blue"

  Scenario: V04.10 — CheckboxGroup set_value programmatic
    Given CheckboxGroup with set_value({"Green", "Blue"})
    Then "Green" and "Blue" are checked

  Scenario: V04.11 — CheckboxGroup set_item_label_generator
    Given CheckboxGroup with items=(1,2,3), generator=lambda x: f"Item {x}"
    Then checkboxes labeled "Item 1", "Item 2", "Item 3"

  Scenario: V04.12 — CheckboxGroup select/deselect methods
    Given CheckboxGroup with items, Button calling cbg.select("Red")
    When click button
    Then "Red" is checked

  # --- RadioButtonGroup ---
  Scenario: V04.13 — RadioButtonGroup renders items
    Given RadioButtonGroup("Size") with set_items("S", "M", "L")
    Then 3 radio buttons in "#rbg1"

  Scenario: V04.14 — RadioButtonGroup select one
    When click "M"
    Then Span#rbg1-val text is "M"

  Scenario: V04.15 — RadioButtonGroup set_value programmatic
    Given RadioButtonGroup with set_value("L")
    Then "L" is selected

  Scenario: V04.16 — RadioButtonGroup change selection
    Given "M" selected
    When click "S"
    Then Span#rbg1-val text is "S" (only one selected)

  Scenario: V04.17 — RadioButtonGroup set_item_label_generator
    Given items=("sm","md","lg"), generator mapping to "Small","Medium","Large"
    Then labels are "Small", "Medium", "Large"

  Scenario: V04.18 — RadioButtonGroup read_only
    Given RadioButtonGroup with set_read_only(True)
    When click any radio
    Then selection does NOT change

  Scenario: V04.19 — RadioButtonGroup required
    Given RadioButtonGroup with set_required_indicator_visible(True)
    Then required indicator visible

  # --- Value roundtrip (mSync regression) ---
  Scenario: V04.20 — CheckboxGroup deselect then re-select same item
    Given CheckboxGroup with "Red" selected
    When uncheck "Red", then check "Red" again
    Then Span#cbg1-val text contains "Red"

  Scenario: V04.21 — RadioButtonGroup value preserved after re-selection
    Given RadioButtonGroup with "M" selected
    When select "L", then select "M" again
    Then Span#rbg1-val text is "M"

  # --- Nav ---
  Scenario: V04.22 — Nav to next view
    When click link "Next: Select & ListBox"
    Then URL contains "/test/select-listbox"
```

---

## View 5: `/test/select-listbox`

```gherkin
Feature: Select & ListBox

  # --- Select ---
  Scenario: V05.01 — Select renders with label
    Given Select("Country") with set_items("US", "UK", "DE"), id="sel1"
    Then "#sel1" label is "Country"

  Scenario: V05.02 — Select choose item
    When open "#sel1" and select "UK"
    Then Span#sel1-val text is "UK"

  Scenario: V05.03 — Select set_value programmatic
    Given Select with set_value("DE")
    Then "#sel-pre" displays "DE"

  Scenario: V05.04 — Select set_placeholder
    Given Select with set_placeholder("Choose...")
    Then "#sel-ph" shows "Choose..." when empty

  Scenario: V05.05 — Select set_empty_selection_allowed
    Given Select with set_empty_selection_allowed(True), initial value="US"
    When select empty option
    Then value is None/empty

  Scenario: V05.06 — Select set_item_label_generator
    Given Select with items=("us","uk"), generator=str.upper
    Then options display "US", "UK"

  Scenario: V05.07 — Select prefix component
    Given Select with set_prefix_component(Icon("lumo:globe"))
    Then prefix icon renders

  Scenario: V05.08 — Select read_only
    Given Select with set_read_only(True)
    Then clicking "#sel-ro" does NOT open dropdown

  # --- ListBox ---
  Scenario: V05.09 — ListBox renders items
    Given ListBox with set_items("A", "B", "C"), id="lb1"
    Then 3 items visible

  Scenario: V05.10 — ListBox select item
    When click "B"
    Then Span#lb1-val text is "B"

  Scenario: V05.11 — ListBox set_value programmatic
    Given ListBox with set_value("C")
    Then "C" is selected

  Scenario: V05.12 — ListBox item_label_generator
    Given ListBox with items=(1,2,3), generator=lambda x: f"#{x}"
    Then items show "#1", "#2", "#3"

  # --- MultiSelectListBox ---
  Scenario: V05.13 — MultiSelectListBox renders
    Given MultiSelectListBox with set_items("X", "Y", "Z"), id="mslb1"
    Then 3 items visible

  Scenario: V05.14 — MultiSelectListBox select multiple
    When click "X" and "Z"
    Then Span#mslb1-val contains "X" and "Z"

  Scenario: V05.15 — MultiSelectListBox set_value programmatic
    Given MultiSelectListBox with set_value({"Y", "Z"})
    Then "Y" and "Z" selected

  Scenario: V05.16 — MultiSelectListBox deselect_all
    Given items selected, Button calling mslb.deselect_all()
    When click button
    Then no items selected

  Scenario: V05.17 — MultiSelectListBox read_only
    Given MultiSelectListBox with set_read_only(True)
    When click item
    Then selection does NOT change

  # --- Value roundtrip (mSync regression) ---
  Scenario: V05.18 — Select change value multiple times
    Given Select#sel-multi with items "US","UK","DE"
    When select "UK", then select "DE", then select "US"
    Then Span#sel-multi-val text is "US" (final value)

  Scenario: V05.19 — Select required validation
    Given Select with set_required_indicator_visible(True), no value selected
    Then required indicator visible
    When select "UK" then clear selection
    Then invalid state shown

  # --- Nav ---
  Scenario: V05.20 — Nav to next view
    When click link "Next: ComboBox"
    Then URL contains "/test/combo-box"
```

---

## View 6: `/test/combo-box`

```gherkin
Feature: ComboBox & MultiSelectComboBox

  # --- ComboBox ---
  Scenario: V06.01 — ComboBox renders with label
    Given ComboBox("Fruit") with set_items("Apple","Banana","Cherry"), id="cb1"
    Then "#cb1" label is "Fruit"

  Scenario: V06.02 — ComboBox open and select
    When click "#cb1" to open dropdown, select "Banana"
    Then Span#cb1-val text is "Banana"

  Scenario: V06.03 — ComboBox set_value programmatic
    Given ComboBox with set_value("Cherry")
    Then "#cb-pre" displays "Cherry"

  Scenario: V06.04 — ComboBox type to filter
    When type "App" into "#cb1"
    Then dropdown shows only "Apple"

  Scenario: V06.05 — ComboBox set_placeholder
    Given ComboBox with set_placeholder("Search...")
    Then "#cb-ph" shows "Search..."

  Scenario: V06.06 — ComboBox clear button
    Given ComboBox with value, set_clear_button_visible(True)
    When click clear
    Then value is None

  Scenario: V06.07 — ComboBox allow_custom_value
    Given ComboBox with set_allow_custom_value(True), custom_value_listener → Span#cb-cust
    When type "Mango" and press Enter
    Then Span#cb-cust text is "Mango"

  Scenario: V06.08 — ComboBox item_label_generator
    Given ComboBox items=({"id":1,"name":"Apple"}, ...), generator=lambda x: x["name"]
    Then dropdown shows "Apple", "Banana", "Cherry"

  Scenario: V06.09 — ComboBox set_page_size
    Given ComboBox with 100 items, set_page_size(20)
    Then lazy loading works (scroll loads more)

  Scenario: V06.10 — ComboBox auto_open disabled
    Given ComboBox with set_auto_open(False)
    When focus "#cb-noauto"
    Then dropdown does NOT open automatically

  # --- MultiSelectComboBox ---
  Scenario: V06.11 — MultiSelectComboBox renders
    Given MultiSelectComboBox("Tags") with set_items("A","B","C"), id="mscb1"
    Then "#mscb1" label is "Tags"

  Scenario: V06.12 — MultiSelectComboBox select multiple
    When open and select "A", then open again and select "C"
    Then Span#mscb1-val contains "A" and "C"
    And chips "A" and "C" visible in input

  Scenario: V06.13 — MultiSelectComboBox set_value programmatic
    Given MultiSelectComboBox with set_value({"B","C"})
    Then "B" and "C" chips visible

  Scenario: V06.14 — MultiSelectComboBox deselect via chip remove
    Given "A","B" selected
    When remove chip "A"
    Then only "B" remains

  Scenario: V06.15 — MultiSelectComboBox deselect_all
    Given items selected, Button calling mscb.deselect_all()
    When click button
    Then no items selected, no chips

  Scenario: V06.16 — MultiSelectComboBox clear button
    Given MultiSelectComboBox with value, set_clear_button_visible(True)
    When click clear
    Then all deselected

  Scenario: V06.17 — MultiSelectComboBox item_label_generator
    Given items=(1,2,3), generator=lambda x: f"Tag-{x}"
    Then chips and dropdown show "Tag-1", "Tag-2", "Tag-3"

  Scenario: V06.18 — MultiSelectComboBox allow_custom_value
    Given set_allow_custom_value(True)
    When type "New" and Enter
    Then custom value event fires

  Scenario: V06.19 — MultiSelectComboBox read_only
    Given set_read_only(True)
    Then cannot open dropdown or modify selection

  # --- Value roundtrip (mSync regression) ---
  Scenario: V06.20 — ComboBox clear and re-select same value
    Given ComboBox#cb-round with value "Apple"
    When click clear button, then re-select "Apple"
    Then Span#cb-round-val text is "Apple" (not None)

  Scenario: V06.21 — ComboBox required validation
    Given ComboBox with set_required_indicator_visible(True), value set
    When clear value and blur
    Then field shows invalid state (required)

  Scenario: V06.22 — ComboBox set_value then user changes
    Given ComboBox with set_value("Banana"), value_change_listener
    When user selects "Cherry"
    Then value-change event fires with value "Cherry" and from_client=True

  Scenario: V06.23 — MultiSelectComboBox value roundtrip
    Given MultiSelectComboBox with set_value({"A","B"})
    When deselect "A", then re-select "A"
    Then value contains "A" and "B"

  # --- Nav ---
  Scenario: V06.24 — Nav to next view
    When click link "Next: Date & Time"
    Then URL contains "/test/date-time"
```

---

## View 7: `/test/date-time`

```gherkin
Feature: DatePicker, TimePicker, DateTimePicker

  # --- DatePicker ---
  Scenario: V07.01 — DatePicker renders with label
    Given DatePicker("Birthday") with id="dp1"
    Then "#dp1" label is "Birthday"

  Scenario: V07.02 — DatePicker set_value and read
    Given DatePicker with set_value(date(2025, 6, 15))
    Then "#dp-pre" displays "6/15/2025" or locale equivalent

  Scenario: V07.03 — DatePicker user input
    When type "2025-01-20" into "#dp1" and blur/close
    Then Span#dp1-val shows "2025-01-20"

  Scenario: V07.04 — DatePicker clear button
    Given DatePicker with value, set_clear_button_visible(True)
    When click clear
    Then value is None

  Scenario: V07.05 — DatePicker min/max validation
    Given DatePicker with set_min(date(2025,1,1)), set_max(date(2025,12,31))
    When type "2024-06-01" and blur
    Then "#dp-range" is invalid

  # --- TimePicker ---
  Scenario: V07.06 — TimePicker renders with label
    Given TimePicker("Meeting time") with id="tp1"
    Then "#tp1" label is "Meeting time"

  Scenario: V07.07 — TimePicker set_value
    Given TimePicker with set_value(time(14, 30))
    Then "#tp-pre" displays "14:30" or locale equivalent

  Scenario: V07.08 — TimePicker user select
    When open "#tp1" and select a time from dropdown
    Then Span#tp1-val shows selected time

  Scenario: V07.09 — TimePicker set_step
    Given TimePicker with set_step(1800) (30 min)
    Then dropdown shows times at 30-min intervals

  Scenario: V07.10 — TimePicker min/max
    Given TimePicker with set_min(time(9,0)), set_max(time(17,0))
    When type "20:00" and blur
    Then invalid

  Scenario: V07.11 — TimePicker clear button
    Given TimePicker with value, set_clear_button_visible(True)
    When click clear
    Then value is None

  # --- DateTimePicker ---
  Scenario: V07.12 — DateTimePicker renders
    Given DateTimePicker("Event") with id="dtp1"
    Then "#dtp1" label is "Event"

  Scenario: V07.13 — DateTimePicker set_value
    Given DateTimePicker with set_value(datetime(2025, 6, 15, 14, 30))
    Then date part shows "6/15/2025", time part shows "14:30"

  Scenario: V07.14 — DateTimePicker user input
    When set date "2025-03-10" and time "09:00"
    Then Span#dtp1-val shows "2025-03-10T09:00"

  Scenario: V07.15 — DateTimePicker date_placeholder / time_placeholder
    Given set_date_placeholder("Pick date"), set_time_placeholder("Pick time")
    Then placeholders visible in each sub-field

  Scenario: V07.16 — DateTimePicker min/max
    Given min=datetime(2025,1,1,0,0), max=datetime(2025,12,31,23,59)
    When enter out-of-range datetime
    Then invalid

  # --- Shared ---
  Scenario: V07.17 — DatePicker set_i18n (localization)
    Given DatePicker with set_i18n({"monthNames": ["Enero",...]})
    When open calendar
    Then month names are localized

  # --- DatePicker value roundtrip (mSync regression — THE BUG) ---
  Scenario: V07.18 — DatePicker value survives mSync+change cycle
    Given DatePicker#dp-round with value_change_listener → Span#dp-round-val
    When type "2025-06-15" into "#dp-round" and blur
    Then Span#dp-round-val text is "2025-06-15"
    And get_value() returns date(2025, 6, 15) (not None)

  Scenario: V07.19 — DatePicker clear then set same value
    Given DatePicker#dp-same with set_value(date(2025, 3, 10))
    When click clear button to clear value
    Then value is None
    When type "2025-03-10" and blur
    Then value is date(2025, 3, 10) again

  Scenario: V07.20 — DatePicker calendar pick preserves value
    Given DatePicker#dp-pick, open calendar
    When click a date cell in the calendar popup
    Then Span#dp-pick-val shows the selected date (not empty/None)

  # --- DatePicker open/close ---
  Scenario: V07.21 — DatePicker open/close programmatic
    Given DatePicker#dp-oc, Button#dp-open calling dp.open(), Button#dp-close calling dp.close()
    When click "#dp-open"
    Then calendar overlay is visible
    When click "#dp-close"
    Then calendar overlay is hidden

  Scenario: V07.22 — DatePicker opened-change listener
    Given DatePicker#dp-ocl with add_opened_change_listener → Span#dp-oc-ev
    When open and close calendar
    Then Span#dp-oc-ev tracks open/close events

  # --- DatePicker extra features ---
  Scenario: V07.23 — DatePicker week numbers
    Given DatePicker#dp-wn with set_week_numbers_visible(True)
    When open calendar
    Then week numbers column visible in calendar

  Scenario: V07.24 — DatePicker initial position
    Given DatePicker#dp-ip with set_initial_position(date(2025, 6, 1)), no value
    When open calendar
    Then calendar opens showing June 2025

  Scenario: V07.25 — DatePicker auto_open disabled
    Given DatePicker#dp-noauto with set_auto_open(False)
    When focus "#dp-noauto"
    Then calendar does NOT open automatically

  Scenario: V07.26 — DatePicker required validation
    Given DatePicker#dp-req with set_required_indicator_visible(True)
    When focus, leave empty, blur
    Then field shows invalid state (client validates required)

  # --- TimePicker value roundtrip (mSync regression) ---
  Scenario: V07.27 — TimePicker value survives mSync+change cycle
    Given TimePicker#tp-round with value_change_listener → Span#tp-round-val
    When type "14:30" into "#tp-round" and blur
    Then Span#tp-round-val text is "14:30"
    And get_value() returns time(14, 30) (not None)

  Scenario: V07.28 — TimePicker clear then re-set same value
    Given TimePicker#tp-same with set_value(time(9, 0))
    When clear, then type "09:00" and blur
    Then value is time(9, 0) again

  # --- TimePicker open/close ---
  Scenario: V07.29 — TimePicker open/close programmatic
    Given TimePicker#tp-oc, Button#tp-open calling tp.open(), Button#tp-close calling tp.close()
    When click "#tp-open"
    Then time dropdown is visible
    When click "#tp-close"
    Then time dropdown is hidden

  Scenario: V07.30 — TimePicker opened-change listener
    Given TimePicker#tp-ocl with add_opened_change_listener → Span#tp-oc-ev
    When open and close
    Then Span#tp-oc-ev tracks open/close events

  # --- DateTimePicker value roundtrip (mSync regression) ---
  Scenario: V07.31 — DateTimePicker value survives mSync+change cycle
    Given DateTimePicker#dtp-round with value_change_listener → Span#dtp-round-val
    When set date "2025-06-15" and time "14:30" and blur
    Then Span#dtp-round-val shows "2025-06-15T14:30"
    And get_value() returns datetime(2025, 6, 15, 14, 30) (not None)

  Scenario: V07.32 — DateTimePicker clear and re-set
    Given DateTimePicker#dtp-same with set_value(datetime(2025, 1, 1, 9, 0))
    When clear date part, then re-enter "2025-01-01" and "09:00"
    Then value is datetime(2025, 1, 1, 9, 0) again

  Scenario: V07.33 — DateTimePicker step precision
    Given DateTimePicker#dtp-step with set_step(3600) (1 hour)
    When open time dropdown
    Then time options are at 1-hour intervals

  Scenario: V07.34 — DateTimePicker required validation
    Given DateTimePicker#dtp-req with set_required_indicator_visible(True)
    When focus, leave empty, blur
    Then field shows invalid state

  Scenario: V07.35 — DateTimePicker week numbers
    Given DateTimePicker#dtp-wn with set_week_numbers_visible(True)
    When open date part calendar
    Then week numbers column visible

  # --- Nav ---
  Scenario: V07.36 — Nav to next view
    When click link "Next: Grid Basic"
    Then URL contains "/test/grid-basic"
```

---

## View 8: `/test/grid-basic`

```gherkin
Feature: Grid — Columns & Data

  Background:
    Given Grid#grid1 with items = list of Person(name, age, email) objects
    And 3 columns: "Name", "Age", "Email"

  # --- Rendering ---
  Scenario: V08.01 — Grid renders with header and data rows
    Then grid has 3 column headers: "Name", "Age", "Email"
    And data rows match item count

  Scenario: V08.02 — Grid add_column with property name
    Given grid.add_column("name", header="Name")
    Then column shows person.name for each row

  Scenario: V08.03 — Grid set_items replaces data
    Given Button that calls grid.set_items(new_list)
    When click button
    Then grid shows new data

  # --- Column properties ---
  Scenario: V08.04 — Column set_header
    Given column with set_header("Full Name")
    Then header text is "Full Name"

  Scenario: V08.05 — Column set_width
    Given column with set_width("200px")
    Then column width is ~200px

  Scenario: V08.06 — Column set_flex_grow
    Given column with set_flex_grow(2)
    Then column takes proportionally more space

  Scenario: V08.07 — Column set_auto_width
    Given column with set_auto_width(True)
    Then column width adjusts to content

  Scenario: V08.08 — Column set_resizable
    Given column with set_resizable(True)
    Then column resize handle is visible

  Scenario: V08.09 — Column set_text_align
    Given column with set_text_align("center")
    Then cell content is centered

  Scenario: V08.10 — Column set_frozen
    Given column with set_frozen(True)
    Then column stays visible on horizontal scroll

  Scenario: V08.11 — Column set_frozen_to_end
    Given column with set_frozen_to_end(True)
    Then column frozen to right edge

  Scenario: V08.12 — Column set_visible(False)
    Given column with set_visible(False)
    Then column is hidden, other columns still show

  Scenario: V08.13 — Column set_footer_text
    Given column with set_footer_text("Total: 10")
    Then footer shows "Total: 10"

  # --- Renderers ---
  Scenario: V08.14 — Grid LitRenderer
    Given column with LitRenderer("<span>${item.name} (${item.age})</span>")
    Then cells show "Alice (30)", "Bob (25)", etc.

  Scenario: V08.15 — Grid ComponentRenderer
    Given column with ComponentRenderer(lambda p: Button(p.name))
    Then each cell contains a Button with person name

  Scenario: V08.16 — Grid ComponentRenderer click
    Given ComponentRenderer Button with click listener → Span#grid-click
    When click button in first row
    Then Span#grid-click text is person name

  # --- Header rows ---
  Scenario: V08.17 — Grid prepend_header_row (column groups)
    Given grid.prepend_header_row() with join on Name+Email columns
    Then merged header cell spans 2 columns

  # --- Column reorder ---
  Scenario: V08.18 — Grid set_column_reorder_allowed
    Given grid.set_column_reorder_allowed(True)
    Then columns can be reordered by drag (verify attribute)

  # --- Data provider ---
  Scenario: V08.19 — Grid with CallbackDataProvider
    Given grid with set_data_provider(callback_provider) for 1000 items
    When scroll down
    Then new rows load lazily

  # --- Data refresh ---
  Scenario: V08.20 — Grid set_items replaces and re-renders
    Given grid with 5 items, Button#refresh calling grid.set_items(new_5_items)
    When click "#refresh"
    Then grid shows new data, old data gone

  Scenario: V08.21 — Grid empty state
    Given grid with items, Button#clear calling grid.set_items([])
    When click "#clear"
    Then grid shows no data rows (empty)

  Scenario: V08.22 — Grid all_rows_visible mode
    Given Grid#grid-arv with set_all_rows_visible(True) and 3 items
    Then grid height fits exactly 3 rows (no scrollbar)

  Scenario: V08.23 — Grid column set_key and get by key
    Given column with set_key("name-col")
    Then grid.get_column_by_key("name-col") returns the column

  Scenario: V08.24 — Grid column set_sortable with data provider
    Given grid with CallbackDataProvider, sortable column
    When click column header to sort
    Then data provider receives sort order, rows re-rendered

  # --- Nav ---
  Scenario: V08.25 — Nav to next view
    When click link "Next: Grid Features"
    Then URL contains "/test/grid-features"
```

---

## View 9: `/test/grid-features`

```gherkin
Feature: Grid — Selection, Sorting, Events

  Background:
    Given Grid#grid2 with 5 Person items and 3 columns

  # --- Selection SINGLE ---
  Scenario: V09.01 — Grid single selection mode
    Given grid.set_selection_mode(SelectionMode.SINGLE)
    When click row "Alice"
    Then Span#grid2-sel text is "Alice"

  Scenario: V09.02 — Grid single select_item programmatic
    Given Button calling grid.select_item(bob)
    When click button
    Then "Bob" row is highlighted

  Scenario: V09.03 — Grid single deselect
    Given "Alice" selected, click "Alice" again
    Then selection is empty

  # --- Selection MULTI ---
  Scenario: V09.04 — Grid multi selection mode
    Given grid.set_selection_mode(SelectionMode.MULTI)
    Then checkbox column appears

  Scenario: V09.05 — Grid multi select multiple
    When check "Alice" and "Charlie"
    Then Span#grid2-sel contains "Alice, Charlie"

  Scenario: V09.06 — Grid multi select_all
    Given Button calling grid.select_all()
    When click button
    Then all rows selected

  Scenario: V09.07 — Grid multi deselect_all
    Given all selected, Button calling grid.deselect_all()
    When click button
    Then no rows selected

  # --- Sorting ---
  Scenario: V09.08 — Grid sortable column
    Given column with set_sortable(True)
    When click "Name" header
    Then rows sorted alphabetically ascending

  Scenario: V09.09 — Grid sort toggle descending
    When click "Name" header again
    Then rows sorted descending

  Scenario: V09.10 — Grid multi_sort
    Given grid.set_multi_sort(True)
    When sort by "Age" then shift-click "Name"
    Then rows sorted by age then name

  Scenario: V09.11 — Grid sort listener
    Given grid.add_sort_listener → Span#grid2-sort
    When click sortable column
    Then Span#grid2-sort shows sort info

  # --- Click events ---
  Scenario: V09.12 — Grid item click
    Given grid.add_item_click_listener → Span#grid2-click
    When click row "Bob"
    Then Span#grid2-click text is "Bob"

  Scenario: V09.13 — Grid item double click
    Given grid.add_item_double_click_listener → Span#grid2-dbl
    When double-click row "Alice"
    Then Span#grid2-dbl text is "Alice"

  # --- Selection listener ---
  Scenario: V09.14 — Grid selection listener
    Given grid.add_selection_listener → Span#grid2-selev
    When select "Charlie"
    Then Span#grid2-selev text is "Charlie"

  # --- Column ops ---
  Scenario: V09.15 — Grid remove_column
    Given Button calling grid.remove_column(email_col)
    When click button
    Then only "Name" and "Age" columns remain

  # --- Details row ---
  Scenario: V09.16 — Grid details row open/close
    Given grid.set_item_details_renderer(LitRenderer("<div>Details: ${item.name}</div>"))
    When click row "Alice"
    Then details row expands showing "Details: Alice"
    When click "Alice" again
    Then details row collapses

  # --- Scroll ---
  Scenario: V09.17 — Grid scroll to index
    Given grid with 100 items
    When grid.scroll_to_index(90) via Button
    Then row 90 is visible in viewport

  # --- Column header component ---
  Scenario: V09.18 — Grid column set_header_component
    Given column with set_header_component(Button("Sort"))
    Then header contains a clickable Button instead of text

  # --- Items with active sort ---
  Scenario: V09.19 — Grid set_items preserves sort
    Given grid sorted by Name ascending
    When grid.set_items(new_items) via Button
    Then new items are displayed sorted by Name ascending

  # --- Remove all columns ---
  Scenario: V09.20 — Grid remove_all_columns
    Given Button calling grid.remove_all_columns()
    When click button
    Then grid has no columns

  # --- Recalculate widths ---
  Scenario: V09.21 — Grid recalculate_column_widths
    Given grid with auto-width columns, Button calling grid.recalculate_column_widths()
    When click button
    Then column widths adjust to current content

  # --- Nav ---
  Scenario: V09.22 — Nav to next view
    When click link "Next: TreeGrid"
    Then URL contains "/test/tree-grid"
```

---

## View 10: `/test/tree-grid`

```gherkin
Feature: TreeGrid

  Background:
    Given TreeGrid#tg1 with hierarchical data:
      - Root1 (children: Child1A, Child1B)
      - Root2 (children: Child2A with grandchild GC2A1)

  Scenario: V10.01 — TreeGrid renders root items
    Then 2 root items visible: "Root1", "Root2"
    And tree toggle (expand arrow) visible on items with children

  Scenario: V10.02 — TreeGrid expand item
    When click expand on "Root1"
    Then "Child1A" and "Child1B" become visible (indented)

  Scenario: V10.03 — TreeGrid collapse item
    Given "Root1" expanded
    When click collapse on "Root1"
    Then children hidden

  Scenario: V10.04 — TreeGrid expand nested
    When expand "Root2", then expand "Child2A"
    Then "GC2A1" visible at level 2

  Scenario: V10.05 — TreeGrid expand_item programmatic
    Given Button calling tg.expand_item(root1)
    When click button
    Then "Root1" children visible

  Scenario: V10.06 — TreeGrid collapse_item programmatic
    Given root1 expanded, Button calling tg.collapse_item(root1)
    When click button
    Then children hidden

  Scenario: V10.07 — TreeGrid column with hierarchy toggle
    Then first column has tree toggle icons
    And other columns render normally

  Scenario: V10.08 — TreeGrid selection works
    Given tg.set_selection_mode(SelectionMode.SINGLE)
    When click "Child1A"
    Then Span#tg1-sel text is "Child1A"

  Scenario: V10.09 — TreeGrid sorting
    Given sortable column
    When click header to sort
    Then root items sorted, children maintain hierarchy

  # --- Nav ---
  Scenario: V10.10 — Nav to next view
    When click link "Next: Dialog"
    Then URL contains "/test/dialog"
```

---

## View 11: `/test/dialog`

```gherkin
Feature: Dialog & ConfirmDialog

  # --- Dialog ---
  Scenario: V11.01 — Dialog open/close
    Given Dialog#dlg1 with content Span("Hello"), Button#open calling dlg.open()
    When click "#open"
    Then dialog overlay visible with "Hello"
    When press Escape
    Then dialog closes

  Scenario: V11.02 — Dialog set_header_title
    Given Dialog with set_header_title("My Dialog")
    When open
    Then header shows "My Dialog"

  Scenario: V11.03 — Dialog header/footer components
    Given Dialog with get_header().add(Button("X")), get_footer().add(Button("OK"))
    When open
    Then "X" in header, "OK" in footer

  Scenario: V11.04 — Dialog set_modal(False)
    Given Dialog with set_modal(False)
    When open
    Then can interact with background (no backdrop overlay)

  Scenario: V11.05 — Dialog set_draggable
    Given Dialog with set_draggable(True)
    When open
    Then dialog can be dragged (draggable attribute set)

  Scenario: V11.06 — Dialog set_resizable
    Given Dialog with set_resizable(True)
    When open
    Then resize handles visible

  Scenario: V11.07 — Dialog set_close_on_esc(False)
    Given Dialog with set_close_on_esc(False)
    When open and press Escape
    Then dialog stays open

  Scenario: V11.08 — Dialog set_close_on_outside_click(False)
    Given Dialog with set_close_on_outside_click(False)
    When open and click outside
    Then dialog stays open

  Scenario: V11.09 — Dialog set_width/set_height
    Given Dialog with set_width("600px"), set_height("400px")
    When open
    Then dialog dimensions are ~600x400

  Scenario: V11.10 — Dialog add/remove content
    Given Dialog with Button("Add") calling dlg.add(Span("new"))
    When open, click "Add"
    Then "new" span appears in dialog

  Scenario: V11.11 — Dialog close listener
    Given Dialog with add_close_listener → Span#dlg-closed
    When open then close
    Then Span#dlg-closed text is "closed"

  # --- ConfirmDialog ---
  Scenario: V11.12 — ConfirmDialog basic
    Given ConfirmDialog with header="Delete?", text="Are you sure?", confirm_text="Yes"
    When open
    Then shows "Delete?", "Are you sure?", "Yes" button

  Scenario: V11.13 — ConfirmDialog confirm
    Given add_confirm_listener → Span#cd-result
    When click "Yes"
    Then Span#cd-result text is "confirmed"
    And dialog closes

  Scenario: V11.14 — ConfirmDialog cancel
    Given set_cancelable(True), set_cancel_text("No"), add_cancel_listener
    When click "No"
    Then Span#cd-result text is "cancelled"

  Scenario: V11.15 — ConfirmDialog reject
    Given set_rejectable(True), set_reject_text("Never"), add_reject_listener
    When click "Never"
    Then Span#cd-result text is "rejected"

  Scenario: V11.16 — ConfirmDialog button themes
    Given set_confirm_button_theme("primary"), set_reject_button_theme("error")
    When open
    Then confirm button has theme "primary", reject has "error"

  Scenario: V11.17 — ConfirmDialog reopen after confirm
    Given confirm listener closes dialog
    When open, confirm, then open again
    Then dialog opens again correctly

  # --- Dialog edge cases ---
  Scenario: V11.18 — Dialog initially opened
    Given Dialog with set_opened(True) during __init__
    Then dialog is visible immediately on view load

  Scenario: V11.19 — Multiple dialogs stacked
    Given Dialog#dlg-a and Dialog#dlg-b, both open
    When open dlg-a, then open dlg-b
    Then both overlays visible, dlg-b on top
    When close dlg-b
    Then dlg-a still visible

  Scenario: V11.20 — ConfirmDialog close on Escape
    Given ConfirmDialog with set_cancelable(True)
    When open then press Escape
    Then cancel listener fires and dialog closes

  Scenario: V11.21 — Dialog add_close_listener detects Esc vs button
    Given Dialog with add_close_listener tracking close action
    When open, press Escape
    Then close event indicates user action (not programmatic)

  # --- Nav ---
  Scenario: V11.22 — Nav to next view
    When click link "Next: Notification & Popover"
    Then URL contains "/test/notification-popover"
```

---

## View 12: `/test/notification-popover`

```gherkin
Feature: Notification & Popover

  # --- Notification ---
  Scenario: V12.01 — Notification.show static
    Given Button calling Notification.show("Saved!", 3000)
    When click button
    Then notification visible with text "Saved!"

  Scenario: V12.02 — Notification auto-close after duration
    Given Notification.show("Quick", 1000)
    When wait 1.5s
    Then notification is gone

  Scenario: V12.03 — Notification position
    Given Notification with position=TOP_CENTER
    When open
    Then notification appears at top center

  Scenario: V12.04 — Notification with components
    Given Notification with add(Span("msg"), Button("Undo"))
    When open
    Then notification shows "msg" and "Undo" button

  Scenario: V12.05 — Notification theme variant
    Given Notification with add_theme_variants(LUMO_SUCCESS)
    When open
    Then notification has success styling (green)

  Scenario: V12.06 — Notification close programmatic
    Given Notification with duration=0 (stays open), Button#close calling notif.close()
    When open, then click "#close"
    Then notification closes

  Scenario: V12.07 — Notification close listener
    Given Notification with add_close_listener → Span#notif-closed
    When open and close
    Then Span#notif-closed text is "closed"

  Scenario: V12.08 — Notification multiple positions
    Given 3 notifications: TOP_START, BOTTOM_END, MIDDLE
    When open all
    Then each appears in correct position

  # --- Popover ---
  Scenario: V12.09 — Popover renders with target
    Given Button#pop-target, Popover with set_target(btn), add(Span("Pop content"))
    When click "#pop-target"
    Then popover opens with "Pop content"

  Scenario: V12.10 — Popover close on outside click
    Given Popover open
    When click outside popover
    Then popover closes

  Scenario: V12.11 — Popover set_position
    Given Popover with set_position(PopoverPosition.TOP)
    When open
    Then popover appears above target

  Scenario: V12.12 — Popover set_modal
    Given Popover with set_modal(True)
    When open
    Then backdrop visible, cannot interact with background

  Scenario: V12.13 — Popover open/close programmatic
    Given Button#pop-open calling popover.open(), Button#pop-close calling popover.close()
    When click "#pop-open"
    Then popover opens
    When click "#pop-close"
    Then popover closes

  Scenario: V12.14 — Popover set_open_on_hover
    Given Popover with set_open_on_hover(True)
    When hover over target
    Then popover opens

  Scenario: V12.15 — Popover close on Esc
    Given Popover open
    When press Escape
    Then popover closes

  Scenario: V12.16 — Popover listeners
    Given add_open_listener → Span#pop-ev, add_close_listener appending
    When open then close
    Then Span#pop-ev tracks "opened,closed"

  # --- Edge cases ---
  Scenario: V12.17 — Multiple simultaneous notifications
    Given Button opening 3 notifications at once (TOP_START, BOTTOM_END, MIDDLE)
    When click button
    Then all 3 notifications visible simultaneously in their positions

  Scenario: V12.18 — Popover with form content
    Given Popover containing TextField + Button, target=Button#pop-form-target
    When open popover, type in TextField, click inner Button
    Then Span#pop-form-val shows typed value (events work inside popover)

  # --- Nav ---
  Scenario: V12.19 — Nav to next view
    When click link "Next: Tabs & Accordion"
    Then URL contains "/test/tabs-accordion"
```

---

## View 13: `/test/tabs-accordion`

```gherkin
Feature: Tabs, TabSheet, Accordion, Details

  # --- Tabs ---
  Scenario: V13.01 — Tabs render
    Given Tabs(Tab("One"), Tab("Two"), Tab("Three")) with id="tabs1"
    Then 3 tabs visible

  Scenario: V13.02 — Tabs select by click
    When click "Two"
    Then Span#tabs1-val text is "1" (index)

  Scenario: V13.03 — Tabs set_selected_index
    Given Button calling tabs.set_selected_index(2)
    When click button
    Then "Three" is selected

  Scenario: V13.04 — Tabs set_orientation vertical
    Given Tabs with set_orientation("vertical")
    Then tabs render vertically

  Scenario: V13.05 — Tabs add tab dynamically
    Given Button calling tabs.add(Tab("Four"))
    When click button
    Then 4 tabs visible

  Scenario: V13.06 — Tabs selected_change_listener
    Given add_selected_change_listener → Span#tabs1-ev
    When click "Three"
    Then Span#tabs1-ev shows "2"

  # --- TabSheet ---
  Scenario: V13.07 — TabSheet renders tabs with content
    Given TabSheet with add_tab(Tab("Info"), Span("Info content"))
    And add_tab(Tab("Settings"), Span("Settings content"))
    Then "Info" tab active, "Info content" visible

  Scenario: V13.08 — TabSheet switch tab
    When click "Settings"
    Then "Settings content" visible, "Info content" hidden

  Scenario: V13.09 — TabSheet selected_change_listener
    Given add_selected_change_listener → Span#ts-ev
    When switch tab
    Then event fires

  # --- Accordion ---
  Scenario: V13.10 — Accordion renders panels
    Given Accordion with add("Panel 1", Span("Content 1")), add("Panel 2", Span("Content 2"))
    Then 2 panels visible, first opened by default

  Scenario: V13.11 — Accordion open panel
    When click "Panel 2" summary
    Then "Content 2" visible, "Content 1" collapsed

  Scenario: V13.12 — Accordion close all
    Given accordion.close()
    Then all panels collapsed

  Scenario: V13.13 — Accordion open by index
    Given accordion.open(1)
    Then "Panel 2" is open

  Scenario: V13.14 — Accordion opened_change_listener
    Given add_opened_change_listener → Span#acc-ev
    When click panel
    Then event fires with index

  # --- Details ---
  Scenario: V13.15 — Details renders with summary
    Given Details("More info", Span("Hidden content"))
    Then summary "More info" visible, content hidden

  Scenario: V13.16 — Details toggle open
    When click summary "More info"
    Then "Hidden content" visible

  Scenario: V13.17 — Details set_opened programmatic
    Given Button calling details.set_opened(True)
    When click button
    Then content visible

  Scenario: V13.18 — Details opened_change_listener
    Given add_opened_change_listener → Span#det-ev
    When toggle
    Then event fires

  Scenario: V13.19 — Details set_summary_text
    Given Details, Button calling details.set_summary_text("New summary")
    When click button
    Then summary text is "New summary"

  # --- Nav ---
  Scenario: V13.20 — Nav to next view
    When click link "Next: Menu"
    Then URL contains "/test/menu"
```

---

## View 14: `/test/menu`

```gherkin
Feature: MenuBar & ContextMenu

  # --- MenuBar ---
  Scenario: V14.01 — MenuBar renders items
    Given MenuBar with items: "File" (sub: "New", "Open"), "Edit" (sub: "Copy", "Paste")
    Then 2 top-level buttons: "File", "Edit"

  Scenario: V14.02 — MenuBar click top item
    When click "File"
    Then submenu opens with "New", "Open"

  Scenario: V14.03 — MenuBar click sub item
    When click "File" → "New"
    Then Span#mb-result text is "New"

  Scenario: V14.04 — MenuBar nested submenu
    Given "Edit" → "Paste" → "Paste Special"
    When click "Edit" → "Paste" → "Paste Special"
    Then Span#mb-result text is "Paste Special"

  Scenario: V14.05 — MenuBar disabled item
    Given MenuItem "Open" with set_enabled(False)
    When click "File"
    Then "Open" appears disabled

  Scenario: V14.06 — MenuBar checkable item
    Given MenuItem "Bold" with set_checkable(True)
    When click "Bold"
    Then item toggles checked state

  Scenario: V14.07 — MenuBar open on hover
    Given MenuBar with set_open_on_hover(True)
    When hover "File"
    Then submenu opens without click

  # --- ContextMenu ---
  Scenario: V14.08 — ContextMenu opens on right-click
    Given Div#ctx-target with ContextMenu, items: "Cut", "Copy", "Paste"
    When right-click "#ctx-target"
    Then context menu opens with 3 items

  Scenario: V14.09 — ContextMenu click item
    When click "Copy"
    Then Span#ctx-result text is "Copy"
    And menu closes

  Scenario: V14.10 — ContextMenu open_on_click
    Given ContextMenu with set_open_on_click(True)
    When left-click "#ctx-target2"
    Then context menu opens

  Scenario: V14.11 — ContextMenu nested items
    Given "Paste" with children "Paste as Text", "Paste Special"
    When open, hover "Paste"
    Then submenu shows

  Scenario: V14.12 — ContextMenu item click fires listener
    Given add_item_click_listener → Span#ctx-ev
    When select item
    Then event fires

  Scenario: V14.13 — ContextMenu disabled item
    Given item "Cut" disabled
    Then "Cut" appears grayed out

  # --- Dynamic items ---
  Scenario: V14.14 — MenuBar add item dynamically
    Given MenuBar, Button#add-menu calling menu_bar.add_item("Help")
    When click "#add-menu"
    Then "Help" button appears in menu bar

  Scenario: V14.15 — MenuBar item visibility toggle
    Given MenuItem "Open" initially visible, Button#toggle-vis calling item.set_visible(False)
    When click "File" → "Open" is visible
    When click "#toggle-vis", then click "File" again
    Then "Open" is NOT in submenu

  Scenario: V14.16 — ContextMenu dynamic items
    Given ContextMenu, Button#add-ctx calling context_menu.add_item("Select All")
    When click "#add-ctx", then right-click target
    Then "Select All" appears in menu

  Scenario: V14.17 — MenuBar overflow into "..." menu
    Given MenuBar with 10 items in narrow container
    Then overflow items grouped under "..." (overflow button)
    When click "..."
    Then hidden items visible in submenu

  # --- Nav ---
  Scenario: V14.18 — Nav to next view
    When click link "Next: Layouts"
    Then URL contains "/test/layouts"
```

---

## View 15: `/test/layouts`

```gherkin
Feature: Layouts

  # --- VerticalLayout ---
  Scenario: V15.01 — VerticalLayout renders children vertically
    Given VerticalLayout(Span("A"), Span("B"), Span("C"))
    Then children are stacked vertically (A above B above C)

  Scenario: V15.02 — VerticalLayout set_spacing
    Given VerticalLayout with set_spacing(False)
    Then no gap between children

  Scenario: V15.03 — VerticalLayout set_padding
    Given VerticalLayout with set_padding(True)
    Then layout has internal padding

  Scenario: V15.04 — VerticalLayout expand
    Given VerticalLayout with 2 children, expand(child2)
    Then child2 takes remaining space (flex-grow: 1)

  Scenario: V15.05 — VerticalLayout set_justify_content_mode CENTER
    Given VerticalLayout with set_justify_content_mode(JustifyContentMode.CENTER)
    Then children centered vertically

  Scenario: V15.06 — VerticalLayout set_align_items CENTER
    Given VerticalLayout with set_align_items(Alignment.CENTER)
    Then children centered horizontally

  Scenario: V15.07 — VerticalLayout add/remove dynamically
    Given Button#add calling layout.add(Span("New"))
    When click "#add"
    Then "New" appears

  Scenario: V15.08 — VerticalLayout replace
    Given layout with Span("Old"), Button calling layout.replace(old, Span("New"))
    When click
    Then "Old" replaced by "New"

  # --- HorizontalLayout ---
  Scenario: V15.09 — HorizontalLayout renders children horizontally
    Given HorizontalLayout(Span("A"), Span("B"), Span("C"))
    Then children are in a row (A left of B left of C)

  Scenario: V15.10 — HorizontalLayout expand
    Given HorizontalLayout, expand(child1)
    Then child1 takes remaining horizontal space

  Scenario: V15.11 — HorizontalLayout set_spacing(False)
    Then no gap between children

  Scenario: V15.12 — HorizontalLayout vertical alignment
    Given set_default_vertical_component_alignment(Alignment.CENTER)
    Then children vertically centered

  # --- FlexLayout ---
  Scenario: V15.13 — FlexLayout set_flex_direction column
    Given FlexLayout with set_flex_direction("column")
    Then children stacked vertically

  Scenario: V15.14 — FlexLayout set_flex_wrap
    Given FlexLayout with set_flex_wrap("wrap"), many children
    Then children wrap to next line when full

  Scenario: V15.15 — FlexLayout per-child flex
    Given FlexLayout, set_flex_grow(2, child1), set_flex_grow(1, child2)
    Then child1 takes 2x space of child2

  # --- FormLayout ---
  Scenario: V15.16 — FormLayout renders fields in columns
    Given FormLayout with 4 TextFields
    Then fields arranged in responsive columns

  Scenario: V15.17 — FormLayout set_responsive_steps
    Given set_responsive_steps(("0", 1), ("600px", 2))
    Then at narrow width: 1 column, at wide: 2 columns

  # --- SplitLayout ---
  Scenario: V15.18 — SplitLayout renders primary/secondary
    Given SplitLayout with add_to_primary(Span("Left")), add_to_secondary(Span("Right"))
    Then "Left" and "Right" side by side with splitter

  Scenario: V15.19 — SplitLayout vertical orientation
    Given set_orientation_vertical(True)
    Then top/bottom layout

  Scenario: V15.20 — SplitLayout splitter position
    Given set_splitter_position("30%")
    Then primary takes ~30% of space

  # --- Nav ---
  Scenario: V15.21 — Nav to next view
    When click link "Next: Card & Scroller"
    Then URL contains "/test/card-scroller"
```

---

## View 16: `/test/card-scroller`

```gherkin
Feature: Card, Scroller, MasterDetailLayout

  # --- Card ---
  Scenario: V16.01 — Card renders with title
    Given Card with set_title("My Card")
    Then title "My Card" visible in title slot

  Scenario: V16.02 — Card subtitle
    Given Card with set_subtitle("Subtitle text")
    Then subtitle visible

  Scenario: V16.03 — Card content
    Given Card with add(Span("Body text"))
    Then "Body text" in default content area

  Scenario: V16.04 — Card footer
    Given Card with add_to_footer(Button("Action"))
    Then "Action" button in footer slot

  Scenario: V16.05 — Card media slot
    Given Card with set_media(Image("photo.jpg"))
    Then image in media slot

  Scenario: V16.06 — Card header prefix/suffix
    Given Card with set_header_prefix(Icon("lumo:star")), set_header_suffix(Button("X"))
    Then icon before title, button after title

  # --- Scroller ---
  Scenario: V16.07 — Scroller renders with content
    Given Scroller(Div("Scrollable content"), scroll_direction=ScrollDirection.VERTICAL)
    Then scroller renders with vertical scrollbar when content overflows

  Scenario: V16.08 — Scroller set_scroll_direction HORIZONTAL
    Given Scroller with set_scroll_direction(ScrollDirection.HORIZONTAL)
    Then horizontal scrollbar, no vertical

  Scenario: V16.09 — Scroller set_content replaces
    Given Scroller with Span("Old"), then set_content(Span("New"))
    Then "New" visible, "Old" gone

  # --- MasterDetailLayout ---
  Scenario: V16.10 — Master buttons visible
    Given MasterDetailLayout with 3 item buttons as master
    Then Item 1, Item 2, Item 3 buttons visible

  Scenario: V16.11 — Open detail
    When click "Item 1" button
    Then detail panel appears with "Detail for item 1"

  Scenario: V16.12 — Close detail
    When click "Close" button in detail panel
    Then detail panel hidden

  Scenario: V16.13 — Switch detail between items
    When click "Item 2", then click "Item 3"
    Then detail content updates, close hides it

  # --- Nav ---
  Scenario: V16.14 — Nav to next view
    When click link "Next: Notification & Popover"
    Then URL contains "/test/notification-popover"
```

---

## View 17: `/test/upload`

```gherkin
Feature: Upload

  Scenario: V17.01 — Upload renders
    Given Upload#upload1 with set_receiver(callback)
    Then upload area visible with button

  Scenario: V17.02 — Upload file succeeds
    Given add_succeeded_listener → Span#upload-result
    When upload a small .txt file
    Then Span#upload-result shows filename

  Scenario: V17.03 — Upload max_files
    Given set_max_files(2)
    Then cannot upload more than 2 files

  Scenario: V17.04 — Upload max_file_size
    Given set_max_file_size(1024) (1KB)
    When try to upload a 2KB file
    Then file is rejected

  Scenario: V17.05 — Upload accepted_file_types
    Given set_accepted_file_types(".txt", ".csv")
    Then file input accept attribute is ".txt,.csv"

  Scenario: V17.06 — Upload auto_upload disabled
    Given set_auto_upload(False)
    When select file
    Then file is listed but NOT uploaded yet

  Scenario: V17.07 — Upload drop_allowed
    Given set_drop_allowed(True)
    Then drop area is visible (no "drop" disabled state)

  Scenario: V17.08 — Upload set_i18n
    Given set_i18n({"uploading": {"status": {"processing": "Procesando..."}}} )
    Then localized strings appear

  Scenario: V17.09 — Upload file_rejected_listener
    Given add_file_rejected_listener → Span#upload-rej, set_max_file_size(100)
    When upload large file
    Then Span#upload-rej shows rejection reason

  # --- Upload edge cases ---
  Scenario: V17.10 — Upload clear_file_list
    Given file already uploaded, Button calling upload.clear_file_list()
    When click button
    Then file list is empty

  Scenario: V17.11 — Upload multiple files sequentially
    Given Upload with set_max_files(3)
    When upload file1, then file2
    Then both files listed as succeeded
    And Span#upload-count text is "2"

  Scenario: V17.12 — Upload started_listener
    Given add_started_listener → Span#upload-start
    When upload a file
    Then Span#upload-start shows filename before upload completes

  # --- Nav ---
  Scenario: V17.13 — Nav to next view
    When click link "Next: Display Components"
    Then URL contains "/test/display"
```

---

## View 18: `/test/display`

```gherkin
Feature: ProgressBar, Avatar, AvatarGroup, Markdown, MessageInput, MessageList

  # --- ProgressBar ---
  Scenario: V18.01 — ProgressBar renders
    Given ProgressBar#pb1 with set_value(0.6)
    Then progress bar at 60%

  Scenario: V18.02 — ProgressBar update value
    Given Button calling pb.set_value(0.9)
    When click button
    Then progress bar at 90%

  Scenario: V18.03 — ProgressBar indeterminate
    Given ProgressBar with set_indeterminate(True)
    Then shows indeterminate animation

  Scenario: V18.04 — ProgressBar min/max
    Given set_min(0), set_max(200), set_value(100)
    Then renders at 50% (100/200)

  # --- Avatar ---
  Scenario: V18.05 — Avatar renders with name
    Given Avatar("Sophia Williams") with id="av1"
    Then avatar shows initials "SW"

  Scenario: V18.06 — Avatar abbreviation
    Given Avatar with set_abbreviation("JD")
    Then shows "JD"

  Scenario: V18.07 — Avatar image
    Given Avatar with set_image("https://example.com/photo.jpg")
    Then avatar shows image

  Scenario: V18.08 — Avatar color_index
    Given Avatar with set_color_index(3)
    Then avatar uses color variant 3

  # --- AvatarGroup ---
  Scenario: V18.09 — AvatarGroup renders items
    Given AvatarGroup with 5 items
    Then 5 avatars visible

  Scenario: V18.10 — AvatarGroup max_items_visible
    Given AvatarGroup with 5 items, set_max_items_visible(3)
    Then 3 avatars + overflow indicator (+2)

  # --- Markdown ---
  Scenario: V18.11 — Markdown renders content
    Given Markdown("# Hello\n**bold** text") with id="md1"
    Then rendered HTML shows h1 "Hello" and bold text

  Scenario: V18.12 — Markdown update content
    Given Button calling md.set_content("## Updated")
    When click
    Then rendered HTML shows h2 "Updated"

  # --- MessageInput ---
  Scenario: V18.13 — MessageInput renders
    Given MessageInput#mi1 with add_submit_listener → Span#mi-result
    Then input field and submit button visible

  Scenario: V18.14 — MessageInput submit
    When type "Hello world" and press Enter (or click submit)
    Then Span#mi-result text is "Hello world"

  # --- MessageList ---
  Scenario: V18.15 — MessageList renders items
    Given MessageList with set_items([{"text":"Hi","userName":"Alice"}])
    Then message "Hi" from "Alice" visible

  Scenario: V18.16 — MessageList multiple items
    Given set_items with 3 messages
    Then 3 messages rendered in order

  # --- Nav ---
  Scenario: V18.17 — Nav to next view
    When click link "Next: HTML Elements"
    Then URL contains "/test/html-elements"
```

---

## View 19: `/test/html-elements`

```gherkin
Feature: HTML Elements

  Scenario: V19.01 — H1 renders
    Given H1("Title") with id="h1"
    Then <h1> with text "Title"

  Scenario: V19.02 — H2 renders
    Given H2("Subtitle") with id="h2"
    Then <h2> with text "Subtitle"

  Scenario: V19.03 — H3-H6 render
    Given H3("H3"), H4("H4"), H5("H5"), H6("H6")
    Then each renders correct heading level

  Scenario: V19.04 — Paragraph renders
    Given Paragraph("Lorem ipsum") with id="p1"
    Then <p> with text "Lorem ipsum"

  Scenario: V19.05 — Span renders
    Given Span("inline") with id="sp1"
    Then <span> with text "inline"

  Scenario: V19.06 — Div renders with children
    Given Div with add(Span("child1"), Span("child2"))
    Then <div> contains 2 <span> children

  Scenario: V19.07 — Div set_text
    Given Div with set_text("text content")
    Then div shows "text content"

  Scenario: V19.08 — Anchor renders
    Given Anchor(href="https://example.com", text="Link")
    Then <a href="https://example.com"> with text "Link"

  Scenario: V19.09 — Anchor set_target
    Given Anchor with set_target("_blank")
    Then target attribute is "_blank"

  Scenario: V19.10 — IFrame renders
    Given IFrame(src="about:blank") with id="iframe1"
    Then <iframe src="about:blank">

  Scenario: V19.11 — Hr renders
    Given Hr()
    Then <hr> element exists

  Scenario: V19.12 — Pre renders
    Given Pre("code block") with id="pre1"
    Then <pre> with text "code block"

  Scenario: V19.13 — Image renders
    Given Image(src="logo.png", alt="Logo") with id="img1"
    Then <img src="logo.png" alt="Logo">

  Scenario: V19.14 — NativeLabel renders
    Given NativeLabel("Field label") with id="lbl1"
    Then <label> with text "Field label"

  Scenario: V19.15 — HTML containers (Header, Footer, Section, Nav, Main)
    Given Header(), Footer(), Section(), Nav(), Main()
    Then each renders its semantic HTML tag

  # --- Nav ---
  Scenario: V19.16 — Nav to next view
    When click link "Next: Component API"
    Then URL contains "/test/component-api"
```

---

## View 20: `/test/component-api`

```gherkin
Feature: Base Component API

  Background:
    Given Button#comp with text "Test" (used for all tests)

  # --- Visibility ---
  Scenario: V20.01 — set_visible(False) hides component
    Given Button#vis-btn, Button#toggle calling vis_btn.set_visible(False)
    When click "#toggle"
    Then "#vis-btn" is not displayed

  Scenario: V20.02 — set_visible(True) shows component
    Given hidden component, toggle calling set_visible(True)
    When click toggle
    Then component visible

  # --- Enabled ---
  Scenario: V20.03 — set_enabled(False) disables
    Given Button#en-btn, Button#toggle-en calling en_btn.set_enabled(False)
    When click "#toggle-en"
    Then "#en-btn" has disabled attribute

  Scenario: V20.04 — set_enabled(True) re-enables
    Given disabled component
    When enable
    Then disabled attribute removed

  # --- CSS Classes ---
  Scenario: V20.05 — add_class_name
    Given Span#cls-span, Button calling span.add_class_name("highlight")
    When click button
    Then "#cls-span" has class "highlight"

  Scenario: V20.06 — remove_class_name
    Given Span with class "old", Button calling remove_class_name("old")
    When click button
    Then class "old" removed

  Scenario: V20.07 — set_class_name toggle
    Given Span, Button calling set_class_name("active", True) then set_class_name("active", False)
    When click twice
    Then class toggled

  # --- Inline Styles ---
  Scenario: V20.08 — get_style().set
    Given Span#sty-span, Button calling span.get_style().set("color", "red")
    When click button
    Then "#sty-span" has inline style color: red

  Scenario: V20.09 — get_style().remove
    Given Span with color:red, Button calling get_style().remove("color")
    When click button
    Then color style removed

  # --- Size ---
  Scenario: V20.10 — set_width / set_height
    Given Div#size-div, Button calling div.set_width("300px"), div.set_height("100px")
    When click button
    Then div is 300x100px

  Scenario: V20.11 — set_size_full
    Given Div#full-div, Button calling div.set_size_full()
    When click button
    Then div width=100%, height=100%

  Scenario: V20.12 — set_min_width / set_max_width
    Given Div, set_min_width("100px"), set_max_width("500px")
    Then min-width and max-width applied

  # --- Themes ---
  Scenario: V20.13 — add_theme_name
    Given Button#theme-btn, Button calling theme_btn.add_theme_name("primary")
    When click
    Then "#theme-btn" has theme="primary"

  Scenario: V20.14 — remove_theme_name
    Given Button with theme "primary error", remove "error"
    Then theme is "primary" only

  # --- ID ---
  Scenario: V20.15 — set_id
    Given Span, Button calling span.set_id("my-span")
    When click button
    Then element has id="my-span"

  # --- Tooltip ---
  Scenario: V20.16 — set_tooltip_text
    Given Button#tip-btn with set_tooltip_text("Click me!")
    When hover over "#tip-btn"
    Then tooltip "Click me!" visible

  # --- Helper text ---
  Scenario: V20.17 — set_helper_text on field
    Given TextField#help-tf with set_helper_text("Enter name")
    Then helper text "Enter name" visible below field

  # --- ARIA ---
  Scenario: V20.18 — set_aria_label
    Given Button#aria-btn with set_aria_label("Close dialog")
    Then aria-label="Close dialog"

  Scenario: V20.19 — set_aria_labelled_by
    Given Span#label-el with "Name", TextField#aria-tf with set_aria_labelled_by("label-el")
    Then aria-labelledby="label-el"

  # --- Focus/Blur ---
  Scenario: V20.20 — focus() programmatic
    Given TextField#focus-tf, Button calling focus_tf.focus()
    When click button
    Then "#focus-tf" is focused

  Scenario: V20.21 — add_focus_listener / add_blur_listener
    Given TextField#fb-tf with add_focus_listener → Span#fb-ev, add_blur_listener appending
    When click "#fb-tf" then click elsewhere
    Then Span#fb-ev tracks "focus,blur"

  # --- Nav ---
  Scenario: V20.22 — Nav to next view
    When click link "Next: Field Mixins"
    Then URL contains "/test/field-mixins"
```

---

## View 21: `/test/field-mixins`

```gherkin
Feature: HasReadOnly, HasValidation, HasRequired

  Background:
    Given TextField#mix-tf, Select#mix-sel, ComboBox#mix-cb, DatePicker#mix-dp
    (Each tests mixins on different field types)

  # --- HasReadOnly ---
  Scenario: V21.01 — TextField set_read_only(True)
    Given Button calling tf.set_read_only(True)
    When click button
    Then "#mix-tf" has readonly attribute
    And cannot type into field

  Scenario: V21.02 — Select set_read_only(True)
    Given Button calling sel.set_read_only(True)
    When click button
    Then "#mix-sel" cannot open dropdown

  Scenario: V21.03 — DatePicker set_read_only
    When set_read_only(True)
    Then cannot open calendar

  Scenario: V21.04 — set_read_only(False) restores
    Given readonly field, Button calling set_read_only(False)
    When click button
    Then field is editable again

  # --- HasValidation ---
  Scenario: V21.05 — TextField set_invalid(True)
    Given Button calling tf.set_invalid(True)
    When click button
    Then "#mix-tf" shows invalid state (red border)

  Scenario: V21.06 — TextField set_error_message
    Given tf.set_error_message("Required field"), tf.set_invalid(True)
    Then error message "Required field" visible below field

  Scenario: V21.07 — Select set_invalid + error_message
    Given sel.set_invalid(True), sel.set_error_message("Choose one")
    Then Select shows "Choose one" error

  Scenario: V21.08 — ComboBox set_invalid + error_message
    Given cb.set_invalid(True), cb.set_error_message("Invalid selection")
    Then ComboBox shows error

  Scenario: V21.09 — set_invalid(False) clears error
    Given invalid field, Button calling set_invalid(False)
    When click button
    Then error state cleared

  # --- HasRequired ---
  Scenario: V21.10 — TextField set_required_indicator_visible(True)
    Given Button calling tf.set_required_indicator_visible(True)
    When click
    Then "#mix-tf" shows required indicator (*)

  Scenario: V21.11 — Select required indicator
    Given sel.set_required_indicator_visible(True)
    Then required indicator visible

  Scenario: V21.12 — ComboBox required indicator
    Given cb.set_required_indicator_visible(True)
    Then required indicator visible

  Scenario: V21.13 — DatePicker required indicator
    Given dp.set_required_indicator_visible(True)
    Then required indicator visible

  Scenario: V21.14 — Client-side required validation
    Given TextField with required=True
    When focus, leave empty, blur
    Then field shows invalid (client validates required)

  # --- Combined mixins ---
  Scenario: V21.15 — Read-only field with error shows error but not editable
    Given tf.set_read_only(True), tf.set_invalid(True), tf.set_error_message("Error")
    Then field shows error but cannot be edited

  Scenario: V21.16 — Required + validation
    Given tf.set_required_indicator_visible(True), type value, clear, blur
    Then client validates and shows required error

  # --- Nav ---
  Scenario: V21.17 — Nav to next view
    When click link "Next: Binder"
    Then URL contains "/test/binder"
```

---

## View 22: `/test/binder`

```gherkin
Feature: Binder — Data Binding & Validation

  Background:
    Given form with TextField#name, EmailField#email, IntegerField#age
    And Binder bound to Person(name, email, age)
    And Button#save calling binder.write_bean(person)
    And Span#binder-result showing result

  # --- read_bean ---
  Scenario: V22.01 — read_bean populates fields
    Given binder.read_bean(Person("Alice", "alice@x.com", 30))
    Then name="Alice", email="alice@x.com", age="30"

  Scenario: V22.02 — read_bean(None) clears fields
    Given fields populated, binder.read_bean(None)
    Then all fields empty

  # --- write_bean ---
  Scenario: V22.03 — write_bean writes form to object
    Given fields filled: name="Bob", email="bob@x.com", age="25"
    When click "#save"
    Then person object has name="Bob", email="bob@x.com", age=25
    And Span#binder-result text is "Bob,bob@x.com,25"

  # --- Validation ---
  Scenario: V22.04 — Required validator blocks save
    Given name field with as_required("Name is required")
    When leave name empty, click "#save"
    Then name field shows error "Name is required"
    And Span#binder-result does NOT update

  Scenario: V22.05 — Pattern validator
    Given email field with with_validator(email_pattern, "Invalid email")
    When type "not-email" in email, click save
    Then email shows "Invalid email"

  Scenario: V22.06 — Value range validator on age
    Given age with with_validator(lambda v: 0 < v < 150, "Invalid age")
    When type "200", click save
    Then age shows error

  Scenario: V22.07 — Valid form saves successfully
    Given all fields valid
    When click "#save"
    Then Span#binder-result shows saved values

  # --- Converters ---
  Scenario: V22.08 — String to int converter
    Given age field with with_converter(string_to_int)
    When type "abc" in age, click save
    Then conversion error shown

  # --- Dirty tracking ---
  Scenario: V22.09 — is_dirty after change
    Given binder.read_bean(person)
    When type in name field
    Then Span#dirty shows "true"

  Scenario: V22.10 — is_dirty false after read_bean
    Given binder.read_bean(person)
    Then Span#dirty shows "false"

  # --- set_bean ---
  Scenario: V22.11 — set_bean enables automatic sync
    Given binder.set_bean(person)
    When type "New Name" in name field
    Then person.name is updated immediately (no save needed)
    And Span#auto-sync shows "New Name"

  # --- Bean-level validation ---
  Scenario: V22.12 — Cross-field validator
    Given binder.with_validator(lambda p: p.age >= 18 if p.name else True, "Must be adult")
    When name="Minor", age=10, click save
    Then bean-level error "Must be adult"

  # --- remove_binding ---
  Scenario: V22.13 — Remove binding
    Given binding for name, Button calling binder.remove_binding(name_binding)
    When click, then modify name, click save
    Then name field changes NOT written to bean

  # --- Multiple fields invalid ---
  Scenario: V22.14 — Multiple validation errors
    Given name required, email pattern, age range
    When all invalid, click save
    Then all 3 fields show errors simultaneously

  # --- Binder with date/time fields (mSync regression — THE BUG) ---
  Scenario: V22.15 — Binder with DatePicker saves correct value
    Given Binder with DatePicker#bind-dp bound to person.birthday
    When type "2025-06-15" in DatePicker and click "#save"
    Then person.birthday is date(2025, 6, 15) (not None)
    And Span#binder-result contains "2025-06-15"

  Scenario: V22.16 — Binder with TimePicker saves correct value
    Given Binder with TimePicker#bind-tp bound to person.start_time
    When type "14:30" in TimePicker and click "#save"
    Then person.start_time is time(14, 30) (not None)
    And Span#binder-result contains "14:30"

  Scenario: V22.17 — Binder with DateTimePicker saves correct value
    Given Binder with DateTimePicker#bind-dtp bound to person.appointment
    When set date "2025-06-15" and time "14:30" and click "#save"
    Then person.appointment is datetime(2025, 6, 15, 14, 30) (not None)

  Scenario: V22.18 — Binder with Select saves correct value
    Given Binder with Select#bind-sel bound to person.country
    When select "UK" and click "#save"
    Then person.country is "UK" (not None)

  Scenario: V22.19 — Binder with ComboBox saves correct value
    Given Binder with ComboBox#bind-cb bound to person.city
    When select "London" and click "#save"
    Then person.city is "London" (not None)

  # --- Binder reset and re-read ---
  Scenario: V22.20 — Binder read_bean after write_bean
    Given form with filled data, binder.write_bean(person)
    When binder.read_bean(other_person)
    Then fields show other_person's values (not previous)

  Scenario: V22.21 — Binder clear all fields via read_bean(None)
    Given form with data populated
    When Button calling binder.read_bean(None)
    Then all fields empty
    And Span#dirty shows "false"

  Scenario: V22.22 — Binder validate_and_save all field types
    Given form with TextField, EmailField, IntegerField, DatePicker, Select
    When fill all fields with valid data and click "#save"
    Then all values saved correctly to bean (none are None)
    And Span#binder-result shows all values

  # --- Nav ---
  Scenario: V22.23 — Nav to next view
    When click link "Next: Navigation"
    Then URL contains "/test/navigation"
```

---

## View 23: `/test/navigation`

```gherkin
Feature: Navigation — Routes, AppLayout, SideNav

  # --- Basic routing ---
  Scenario: V23.01 — @Route registers view
    Given view registered at "/test/navigation"
    Then view renders when navigating to that URL

  Scenario: V23.02 — Route with parameter
    Given @Route("/test/nav-param/:id")
    When navigate to "/test/nav-param/42"
    Then Span#param shows "42"

  Scenario: V23.03 — Route with optional parameter
    Given @Route("/test/nav-opt/:q?")
    When navigate to "/test/nav-opt"
    Then Span#opt shows "" (empty)
    When navigate to "/test/nav-opt/search"
    Then Span#opt shows "search"

  Scenario: V23.04 — @PageTitle sets title
    Given view with @PageTitle("My Page")
    Then document.title is "My Page"

  Scenario: V23.05 — Route page_title param
    Given @Route("/test/nav-title", page_title="Test Title")
    Then document.title is "Test Title"

  # --- RouterLink ---
  Scenario: V23.06 — RouterLink navigates without reload
    Given RouterLink("/test/nav-target", "Go to target")
    When click link
    Then URL changes to "/test/nav-target"
    And page did NOT fully reload (client-side navigation)

  Scenario: V23.07 — RouterLink with components
    Given RouterLink with add(Icon("lumo:arrow-right"), Span("Go"))
    Then link contains icon and text

  # --- AppLayout ---
  Scenario: V23.08 — AppLayout renders navbar + content
    Given layout with set_navbar(H1("App")), content=view
    Then navbar with "App" at top, view content below

  Scenario: V23.09 — AppLayout drawer
    Given layout with set_drawer(SideNav(...))
    Then drawer visible on left

  Scenario: V23.10 — AppLayout drawer toggle
    Given DrawerToggle in navbar
    When click toggle
    Then drawer opens/closes

  # --- SideNav ---
  Scenario: V23.11 — SideNav renders items
    Given SideNav with items: "Home"(/), "Users"(/users), "Settings"(/settings)
    Then 3 nav items visible

  Scenario: V23.12 — SideNav item click navigates
    When click "Users" item
    Then URL changes to "/users"

  Scenario: V23.13 — SideNav nested items
    Given "Settings" with children "General", "Security"
    When expand "Settings"
    Then "General", "Security" visible

  # --- Nav ---
  Scenario: V23.14 — Nav to next view
    When click link "Next: Push"
    Then URL contains "/test/push"
```

---

## View 24: `/test/push`

```gherkin
Feature: WebSocket Push

  Background:
    Given @AppShell @Push enabled app
    And view with Button#start that triggers background task

  Scenario: V24.01 — Push updates UI from background thread
    Given Button#start starts background task: sleep 1s → update Span#push-result
    When click "#start"
    Then within 3s, Span#push-result text is "done"

  Scenario: V24.02 — Multiple push updates
    Given background task sends 3 updates: "1", "2", "3" with 500ms delay each
    When click "#start"
    Then Span#push-count reaches "3" within 3s

  Scenario: V24.03 — Push ProgressBar update
    Given background task updates ProgressBar value from 0 to 1 in steps
    When click "#start"
    Then progress bar reaches 100% within 3s

  Scenario: V24.04 — UI.access runs callback
    Given Button triggering UI.access(lambda: span.set_text("accessed"))
    When click
    Then Span#push-access text is "accessed"

  Scenario: V24.05 — UI.access then async push (regression)
    Given sync ui.access() called in click handler, then async push button
    When click "#access", wait for "accessed", click "#multi"
    Then push-count reaches "3" (syncId not desynchronised)

  Scenario: V24.06 — Two consecutive UI.access calls (regression)
    Given two sync ui.access() calls in sequence
    When click "#access" twice
    Then page still alive (no resync / blank screen)

  Scenario: V24.07 — UI.access then background push (regression)
    Given sync ui.access() then async background task push
    When click "#access", wait for "accessed", click "#start"
    Then push-result shows "done" (no syncId mismatch)

  # --- Nav ---
  Scenario: V24.08 — Nav to next view
    When click link "Next: Theme"
    Then URL contains "/test/theme"
```

---

## View 25: `/test/theme`

```gherkin
Feature: Theme Switching & Styles

  # --- Theme switching ---
  Scenario: V25.01 — Default Lumo light theme
    Then <html> has theme link for Lumo
    And background is light

  Scenario: V25.02 — Switch to dark variant
    Given Button calling UI.set_theme_variant("dark")
    When click
    Then <html> has theme="dark" attribute
    And background is dark

  Scenario: V25.03 — Switch back to light
    Given dark active, Button calling UI.set_theme_variant("light")
    When click
    Then light theme restored

  Scenario: V25.04 — Switch to Aura theme
    Given Button calling UI.set_theme("aura", "light")
    When click
    Then theme link changes to Aura

  Scenario: V25.05 — Switch to Aura dark
    Given Button calling UI.set_theme("aura", "dark")
    When click
    Then Aura dark active, color-scheme: dark applied

  # --- @ColorScheme ---
  Scenario: V25.06 — Initial color scheme from decorator
    Given @ColorScheme("dark") on AppShell
    Then app starts in dark mode

  # --- @StyleSheet ---
  Scenario: V25.07 — Global stylesheet loaded
    Given @StyleSheet("styles/global.css") on @AppShell
    Then CSS from global.css is applied

  Scenario: V25.08 — View-specific stylesheet
    Given @StyleSheet("styles/test-theme.css") on test view
    Then CSS rules from test-theme.css applied

  Scenario: V25.09 — Styles apply to components
    Given CSS rule ".custom-btn { background: green; }" in stylesheet
    And Button with add_class_name("custom-btn")
    Then button has green background

  # --- Nav ---
  Scenario: V25.10 — Nav to next view
    When click link "Next: ClientCallable"
    Then URL contains "/test/client-callable"
```

---

## View 26: `/test/client-callable`

```gherkin
Feature: @ClientCallable

  Scenario: V26.01 — Server method called from client JS
    Given component with @ClientCallable def greet(name): self.result.set_text(f"Hello {name}")
    And Button whose click executes JS: this.$server.greet("World")
    When click button
    Then Span#cc-result text is "Hello World"

  Scenario: V26.02 — @ClientCallable with return value
    Given @ClientCallable def compute(a, b): return a + b
    And JS calling this.$server.compute(3, 4).then(r => display(r))
    When trigger
    Then result shows "7"

  Scenario: V26.03 — @ClientCallable with no args
    Given @ClientCallable def ping(): self.result.set_text("pong")
    When trigger from JS
    Then result is "pong"

  Scenario: V26.04 — @ClientCallable multiple methods
    Given @ClientCallable def method1, def method2
    When call method1 then method2
    Then both execute correctly

  Scenario: V26.05 — @ClientCallable with string arg
    Given @ClientCallable def echo(msg): return msg
    When call with "test string"
    Then returns "test string"

  # --- Nav ---
  Scenario: V26.06 — Nav to next view
    When click link "Next: CustomField"
    Then URL contains "/test/custom-field"
```

---

## View 27: `/test/custom-field`

```gherkin
Feature: CustomField

  Scenario: V27.01 — CustomField renders child fields
    Given CustomField#cf1 containing TextField("First"), TextField("Last")
    Then both text fields visible inside custom field

  Scenario: V27.02 — CustomField label
    Given CustomField with set_label("Full Name")
    Then label "Full Name" visible

  Scenario: V27.03 — CustomField value from children
    When type "John" in first, "Doe" in last
    Then custom field value combines both

  Scenario: V27.04 — CustomField value_change_listener
    Given add_value_change_listener → Span#cf-val
    When modify child fields
    Then event fires

  Scenario: V27.05 — CustomField set_read_only
    Given set_read_only(True)
    Then child fields are read-only

  Scenario: V27.06 — CustomField set_invalid + error_message
    Given set_invalid(True), set_error_message("Invalid name")
    Then error displayed

  Scenario: V27.07 — CustomField required
    Given set_required_indicator_visible(True)
    Then required indicator visible

  # --- Nav ---
  Scenario: V27.08 — Nav to next view
    When click link "Next: VirtualList"
    Then URL contains "/test/virtual-list"
```

---

## View 28: `/test/virtual-list`

```gherkin
Feature: VirtualList

  Scenario: V28.01 — VirtualList renders items
    Given VirtualList#vl1 with set_items(["Item 1", ..., "Item 100"])
    And LitRenderer("<div>${item}</div>")
    Then items render in scrollable list

  Scenario: V28.02 — VirtualList scroll loads more
    Given 1000 items
    When scroll down
    Then more items become visible

  Scenario: V28.03 — VirtualList LitRenderer with properties
    Given items = [Person(name, age)], LitRenderer with with_property("name", lambda p: p.name)
    Then each row shows person name

  Scenario: V28.04 — VirtualList ComponentRenderer
    Given ComponentRenderer(lambda item: HorizontalLayout(Icon("lumo:user"), Span(item.name)))
    Then each row has icon + name

  Scenario: V28.05 — VirtualList set_items replaces
    Given Button calling vl.set_items(new_list)
    When click
    Then new items displayed

  Scenario: V28.06 — VirtualList with DataProvider
    Given CallbackDataProvider for lazy loading
    When scroll
    Then items fetched on demand

  Scenario: V28.07 — VirtualList item_label_generator
    Given set_item_label_generator(lambda x: x.upper())
    Then items displayed in uppercase

  # --- VirtualList edge cases ---
  Scenario: V28.08 — VirtualList scroll to index
    Given VirtualList with 500 items, Button calling vl.scroll_to_index(450)
    When click button
    Then item 450 is visible in viewport

  Scenario: V28.09 — VirtualList data provider refresh
    Given VirtualList with DataProvider, Button calling dp.refresh_all()
    When modify underlying data, click button
    Then list shows updated items

  Scenario: V28.10 — VirtualList empty state
    Given VirtualList with set_items([])
    Then list renders with no visible items (empty)

  # --- Nav ---
  Scenario: V28.11 — Nav to next view
    When click link "Next: Login"
    Then URL contains "/test/login"
```

---

## View 29: `/test/login`

```gherkin
Feature: LoginForm & LoginOverlay

  # --- LoginForm ---
  Scenario: V29.01 — LoginForm renders
    Given LoginForm#lf1
    Then username field, password field, and submit button visible

  Scenario: V29.02 — LoginForm submit
    Given add_login_listener → Span#lf-result
    When type "admin" in username, "pass123" in password, submit
    Then Span#lf-result text is "admin:pass123"

  Scenario: V29.03 — LoginForm error state
    Given login listener calls lf.set_error(True)
    When submit with wrong credentials
    Then error message visible in form

  Scenario: V29.04 — LoginForm forgot_password
    Given add_forgot_password_listener → Span#lf-forgot
    When click "Forgot password?" link
    Then Span#lf-forgot text is "forgot"

  Scenario: V29.05 — LoginForm set_i18n
    Given set_i18n({"form": {"title": "Iniciar sesion"}})
    Then form title is "Iniciar sesion"

  # --- LoginOverlay ---
  Scenario: V29.06 — LoginOverlay renders when opened
    Given LoginOverlay#lo1, set_opened(True)
    Then overlay visible with login form

  Scenario: V29.07 — LoginOverlay set_title
    Given set_title("My App")
    Then overlay shows "My App"

  Scenario: V29.08 — LoginOverlay set_description
    Given set_description("Enter credentials")
    Then description text visible

  Scenario: V29.09 — LoginOverlay submit
    Given add_login_listener → Span#lo-result
    When type credentials and submit
    Then Span#lo-result shows credentials

  Scenario: V29.10 — LoginOverlay close
    Given opened overlay
    When close
    Then overlay hidden

  # --- Login edge cases ---
  Scenario: V29.11 — LoginForm submit via Enter in username field
    Given LoginForm with add_login_listener
    When type "admin" in username, press Enter
    Then login event does NOT fire (need password too)

  Scenario: V29.12 — LoginForm submit via Enter in password field
    Given LoginForm with add_login_listener
    When type "admin" in username, "pass123" in password, press Enter in password field
    Then login event fires with "admin:pass123"

  Scenario: V29.13 — LoginForm set_enabled(False) disables submit
    Given LoginForm with set_enabled(False)
    Then submit button is disabled
    When try to submit
    Then login event does NOT fire

  # --- Nav ---
  Scenario: V29.14 — Nav to next view
    When click link "Next: Server Errors"
    Then URL contains "/test/server-errors"
```

---

## View 30: `/test/server-errors`

```gherkin
Feature: Server Error Handling & Session Resilience

  # --- Error notification via _show_error_notification() ---
  # Per-RPC errors in handle_uidl are caught and shown as a Notification
  # (error theme, position=MIDDLE, 5s duration). Other RPCs in the batch
  # still execute — partial failure, not total failure.

  Scenario: V30.01 — Click handler exception shows error notification
    Given Button#err-click whose click handler raises RuntimeError("Test error")
    When click "#err-click"
    Then vaadin-notification with error theme appears at middle position
    And notification text contains "internal error"
    And app remains functional (not blank screen)

  Scenario: V30.02 — Value-change handler exception shows error notification
    Given TextField#err-tf whose value_change_listener raises Exception
    When type "test" and blur
    Then error notification appears
    And other components still work (click Button#healthy → Span#healthy-result updates)

  Scenario: V30.03 — Partial RPC failure: first RPC fails, second succeeds
    Given TextField#err-tf (value-change raises) and Button#healthy (click → Span#result)
    When type in "#err-tf", blur, then click "#healthy"
    Then error notification from TextField, BUT Span#result updates from Button click
    (Both RPCs processed — error doesn't abort batch)

  Scenario: V30.04 — Navigation error shows notification
    Given SideNav link to /test/broken-init whose __init__ raises Exception
    When click link to broken view
    Then error notification appears (not blank page)
    And SideNav still works (click link to another working view succeeds)

  # --- meta.appError critical error overlay ---
  # Safety net: when handle_uidl() itself throws (e.g., serialization bug AFTER
  # tree changes consumed), returns meta.appError with syncId=-1.
  # Client shows .v-system-error overlay (top-right, red). Click/ESC refreshes page.

  Scenario: V30.05 — meta.appError shows system error overlay
    Given Button#err-fatal that causes unrecoverable error (execute_js injecting bad state)
    When trigger the fatal error
    Then .v-system-error overlay appears (red box, top-right)
    And clicking overlay or pressing Escape refreshes the page

  # --- UIDL JSON serialization (bulletproof _UidlEncoder) ---
  # The encoder must NEVER raise — handles date, datetime, unknown types via str() fallback.
  # A serialization error after tree changes are consumed would leave a blank screen.

  Scenario: V30.06 — Date/datetime values serialize correctly in UIDL
    Given DatePicker#ser-dp with set_value(date(2025,6,15))
    And DateTimePicker#ser-dtp with set_value(datetime(2025,6,15,14,30))
    Then both render correct values (JSON contains ISO format strings)
    And no serialization errors in server logs

  Scenario: V30.07 — Unknown Python types fall back to str() (no crash)
    Given component property set to an unusual Python object (e.g. via execute_js return)
    Then UIDL response is valid JSON (str() fallback used)
    And client renders without error

  # --- Session resilience ---
  Scenario: V30.08 — Multiple rapid clicks don't corrupt state
    Given Button#rapid with click counter → Span#rapid-count
    When click "#rapid" 10 times rapidly
    Then Span#rapid-count text is "10" (all clicks processed, no lost/duplicate)

  Scenario: V30.09 — Navigation works after error notification
    Given error occurred (from V30.01), error notification shown
    When click SideNav link to another test view
    Then navigation succeeds, new view renders correctly

  # --- Push error handling ---
  Scenario: V30.10 — Push callback exception doesn't break session
    Given Button#err-push that triggers UI.access(callback_that_raises)
    When click "#err-push"
    Then error notification appears
    And subsequent push updates still work (click Button#push-ok → Span#push-ok updates via push)

  Scenario: V30.11 — Concurrent push and user RPC don't interfere
    Given push background task updating Span#push-val every 500ms
    And Button#user-click with click listener → Span#click-val
    When click "#user-click" while push is active
    Then both Span#push-val and Span#click-val update correctly

  # --- HasErrorParameter (not yet implemented — future) ---
  # When implemented: route exceptions navigate to error views implementing
  # HasErrorParameter<T>. Until then, generic notification is shown.

  Scenario: V30.12 — HasErrorParameter view catches navigation error
    Given @Route("/test/will-fail") view that raises in __init__
    And ErrorView implementing HasErrorParameter<Exception> registered
    When navigate to /test/will-fail
    Then ErrorView renders with exception message (not generic notification)
    Note: PENDING — requires HasErrorParameter implementation

  # --- Final ---
  Scenario: V30.13 — All tests complete
    Then Span#all-done text is "All UI test views visited"
```

---

## Implementation Notes

### View Structure Pattern
Each view follows this pattern:
```python
@Route("/test/xxx")
class TestXxxView(VerticalLayout):
    def __init__(self):
        super().__init__()
        # Components with set_id() for each testable element
        # Result spans to capture event outputs
        # RouterLink to next view at the bottom
```

### Playwright Test Structure
```python
import pytest
from playwright.sync_api import Page, expect

CONSECUTIVE_FAILURES = 0
MAX_CONSECUTIVE = 4

@pytest.fixture(autouse=True)
def fail_fast():
    global CONSECUTIVE_FAILURES
    if CONSECUTIVE_FAILURES > MAX_CONSECUTIVE:
        pytest.skip("ABORT: 4+ consecutive failures")
    yield
    # Updated in conftest hooks

# Tests navigate once to base URL, then follow RouterLinks
class TestButtonsIcons:
    def test_button_renders(self, page: Page):
        expect(page.locator("#btn1")).to_have_text("Click me")

    def test_button_click(self, page: Page):
        page.click("#btn1")
        expect(page.locator("#result")).to_have_text("clicked")
```

### Performance Optimizations
1. **Single browser session** — reuse page across all tests
2. **Client-side navigation** — RouterLink between views, never full reload
3. **Parallel by view** — views can run in separate browser contexts if needed
4. **Minimal waits** — use `expect()` auto-waiting, not explicit sleeps
5. **Batch assertions** — multiple `expect()` per test where independent
6. **Compact views** — each view loads only its components, no heavy overhead

### Test Execution Order
Views are visited in sequence 1→29 via RouterLinks. Within each view, tests run top-to-bottom. The fail-fast counter spans the entire suite.
