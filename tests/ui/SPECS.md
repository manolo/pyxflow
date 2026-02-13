# UI Test Specifications — PyFlow

## Test Infrastructure

- **Framework:** Playwright (Python)
- **Server:** PyFlow demo app at `http://localhost:8088`
- **Navigation:** Each test view has a RouterLink to the next view (client-side nav, no reload)
- **Fail-fast:** If >4 consecutive tests fail, abort the entire suite
- **Parallelism:** Views are independent; tests within a view run sequentially
- **IDs:** Every testable component gets `set_id("xxx")` for fast `#xxx` selectors

## View Map

| # | Route | Tests | Components |
|---|-------|-------|------------|
| 1 | `/test/buttons-icons` | 18 | Button, Icon, DrawerToggle |
| 2 | `/test/text-inputs` | 32 | TextField, TextArea, PasswordField, EmailField |
| 3 | `/test/number-inputs` | 16 | NumberField, IntegerField |
| 4 | `/test/checkbox-radio` | 22 | Checkbox, CheckboxGroup, RadioButtonGroup |
| 5 | `/test/select-listbox` | 20 | Select, ListBox, MultiSelectListBox |
| 6 | `/test/combo-box` | 20 | ComboBox, MultiSelectComboBox |
| 7 | `/test/date-time` | 18 | DatePicker, TimePicker, DateTimePicker |
| 8 | `/test/grid-basic` | 22 | Grid (columns, data, renderers) |
| 9 | `/test/grid-features` | 16 | Grid (selection, sorting, click, columns ops) |
| 10 | `/test/tree-grid` | 10 | TreeGrid |
| 11 | `/test/dialog` | 18 | Dialog, ConfirmDialog |
| 12 | `/test/notification-popover` | 16 | Notification, Popover |
| 13 | `/test/tabs-accordion` | 20 | Tabs, TabSheet, Accordion, Details |
| 14 | `/test/menu` | 14 | MenuBar, ContextMenu |
| 15 | `/test/layouts` | 22 | VerticalLayout, HorizontalLayout, FlexLayout, FormLayout, SplitLayout |
| 16 | `/test/card-scroller` | 12 | Card, Scroller, MasterDetailLayout |
| 17 | `/test/upload` | 10 | Upload |
| 18 | `/test/display` | 18 | ProgressBar, Avatar, AvatarGroup, Markdown, MessageInput, MessageList |
| 19 | `/test/html-elements` | 16 | H1-H6, Paragraph, Span, Div, Anchor, IFrame, Hr, Pre, Image, NativeLabel |
| 20 | `/test/component-api` | 24 | Base Component API (visibility, enabled, classes, styles, size, tooltip, aria, theme) |
| 21 | `/test/field-mixins` | 18 | HasReadOnly, HasValidation, HasRequired |
| 22 | `/test/binder` | 16 | Binder, validators, converters, dirty tracking |
| 23 | `/test/navigation` | 12 | @Route, params, AppLayout, SideNav, RouterLink, page title |
| 24 | `/test/push` | 8 | WebSocket push, UI.access() |
| 25 | `/test/theme` | 10 | Theme switching, @StyleSheet, @ColorScheme |
| 26 | `/test/client-callable` | 6 | @ClientCallable |
| 27 | `/test/custom-field` | 8 | CustomField |
| 28 | `/test/virtual-list` | 8 | VirtualList |
| 29 | `/test/login` | 10 | LoginForm, LoginOverlay |

**Total: ~454 test scenarios across 29 views**

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
  Scenario: Button renders with text
    Given Button("Click me") with id="btn1"
    Then "#btn1" text is "Click me"

  Scenario: Button click fires listener
    Given Button with click listener that sets Span#result text to "clicked"
    When click "#btn1"
    Then "#result" text is "clicked"

  Scenario: Button set_text updates label
    Given Button("Old") with click listener calling set_text("New")
    When click "#btn-text"
    Then "#btn-text" text is "New"

  Scenario: Button disabled state
    Given Button with id="btn-dis" set_enabled(False)
    Then "#btn-dis" has attribute "disabled"

  Scenario: Button set_disable_on_click
    Given Button with set_disable_on_click(True), click listener sets Span#result2
    When click "#btn-doc"
    Then "#btn-doc" has attribute "disabled"
    And "#result2" text is "clicked"

  Scenario: Button autofocus
    Given Button with set_autofocus(True)
    Then "#btn-auto" is focused

  Scenario: Button click() programmatic
    Given Button#btn-prog with click listener → Span#result3="prog"
    And a second Button#trigger whose click calls btn_prog.click()
    When click "#trigger"
    Then "#result3" text is "prog"

  # --- Icon ---
  Scenario: Icon renders with vaadin icon
    Given Icon("lumo:plus") with id="icon1"
    Then "#icon1" exists as vaadin-icon

  Scenario: Icon set_color
    Given Icon with set_color("red")
    Then "#icon-color" has style "fill" containing "red" or color is red

  Scenario: Icon set_size
    Given Icon with set_size("32px")
    Then "#icon-size" has style width/height "32px"

  # --- Button + Icon ---
  Scenario: Button with icon in prefix
    Given Button("Save", icon=Icon("lumo:plus"))
    Then "#btn-icon" contains vaadin-icon with slot="prefix"

  Scenario: Button icon after text
    Given Button("Save", icon=Icon("lumo:plus")), set_icon_after_text(True)
    Then icon has slot="suffix"

  Scenario: Button icon-only (no text)
    Given Button(icon=Icon("lumo:plus"))
    Then "#btn-icononly" has theme "icon"

  # --- Click shortcut ---
  Scenario: Button add_click_shortcut
    Given Button#btn-short with add_click_shortcut(Key.ENTER), listener → Span#result4
    When press Enter key
    Then "#result4" text is "shortcut"

  # --- DrawerToggle ---
  Scenario: DrawerToggle renders
    Given DrawerToggle() with id="toggle1"
    Then "#toggle1" is a vaadin-drawer-toggle

  Scenario: DrawerToggle click fires
    Given DrawerToggle with click listener → Span#result5
    When click "#toggle1"
    Then "#result5" text is "toggled"

  # --- Nav link ---
  Scenario: Nav to next view
    When click link "Next: Text Inputs"
    Then URL contains "/test/text-inputs"
```

---

## View 2: `/test/text-inputs`

```gherkin
Feature: Text Input Fields

  # --- TextField ---
  Scenario: TextField renders with label
    Given TextField("Name") with id="tf1"
    Then "#tf1" label is "Name"

  Scenario: TextField type and read value
    When type "hello" into "#tf1"
    Then value-changed event fires with value "hello"
    And Span#tf1-val text is "hello"

  Scenario: TextField set_value programmatic
    Given TextField with set_value("preset")
    Then "#tf-preset" input value is "preset"

  Scenario: TextField set_placeholder
    Given TextField with set_placeholder("Enter name...")
    Then "#tf-ph" has placeholder "Enter name..."

  Scenario: TextField set_clear_button_visible
    Given TextField with value "abc" and set_clear_button_visible(True)
    Then clear button is visible in "#tf-clear"
    When click clear button
    Then value is ""

  Scenario: TextField set_max_length
    Given TextField with set_max_length(5)
    When type "abcdefgh" into "#tf-max"
    Then input value length <= 5

  Scenario: TextField set_pattern (client validation)
    Given TextField with set_pattern("[0-9]+")
    When type "abc" into "#tf-pat" and blur
    Then "#tf-pat" has attribute "invalid"

  Scenario: TextField set_allowed_char_pattern
    Given TextField with set_allowed_char_pattern("[0-9]")
    When type "a1b2" into "#tf-acp"
    Then input value is "12" (letters blocked)

  Scenario: TextField prefix/suffix components
    Given TextField with set_prefix_component(Icon("lumo:search"))
    And set_suffix_component(Span("kg"))
    Then "#tf-fix" contains prefix icon and suffix span

  Scenario: TextField set_value_change_mode EAGER
    Given TextField with ValueChangeMode.EAGER, listener updates Span#tf-eager
    When type "ab" character by character
    Then Span#tf-eager updates after each character

  # --- TextArea ---
  Scenario: TextArea renders with label
    Given TextArea("Bio") with id="ta1"
    Then "#ta1" label is "Bio"

  Scenario: TextArea type and read value
    When type "line1\nline2" into "#ta1"
    Then value contains "line1" and "line2"

  Scenario: TextArea set_min_rows / set_max_rows
    Given TextArea with set_min_rows(3), set_max_rows(6)
    Then textarea renders with minimum 3 rows height

  Scenario: TextArea set_clear_button_visible
    Given TextArea with value, set_clear_button_visible(True)
    When click clear button
    Then value is ""

  # --- PasswordField ---
  Scenario: PasswordField renders
    Given PasswordField("Password") with id="pf1"
    Then "#pf1" input type is "password"

  Scenario: PasswordField type and read
    When type "secret123" into "#pf1"
    Then Span#pf1-val text is "secret123"

  Scenario: PasswordField reveal button
    Given PasswordField with set_reveal_button_visible(True)
    Then reveal button is visible
    When click reveal button
    Then input type changes to "text" (value visible)

  Scenario: PasswordField hide reveal button
    Given PasswordField with set_reveal_button_visible(False)
    Then reveal button is NOT visible

  # --- EmailField ---
  Scenario: EmailField renders with label
    Given EmailField("Email") with id="ef1"
    Then "#ef1" label is "Email"

  Scenario: EmailField client validation
    When type "not-an-email" into "#ef1" and blur
    Then "#ef1" shows invalid state

  Scenario: EmailField valid email
    When type "user@example.com" into "#ef-valid" and blur
    Then "#ef-valid" is NOT invalid

  Scenario: EmailField value-change
    When type "a@b.com" into "#ef1"
    Then Span#ef1-val text is "a@b.com"

  # --- Shared field features ---
  Scenario: TextField helper text
    Given TextField with set_helper_text("Min 3 chars")
    Then "#tf-help" shows helper text "Min 3 chars"

  Scenario: TextField tooltip
    Given TextField with set_tooltip_text("Full name")
    Then "#tf-tip" has tooltip "Full name"

  Scenario: TextField autoselect
    Given TextField with value "hello", set_autoselect(True)
    When click/focus "#tf-sel"
    Then text is selected

  Scenario: TextField set_label changes label
    Given TextField("Old") with Button that calls tf.set_label("New")
    When click button
    Then "#tf-lbl" label is "New"

  # --- Shared text field value_change_timeout ---
  Scenario: TextField value_change_timeout with LAZY mode
    Given TextField, ValueChangeMode.LAZY, timeout=500
    When type "abc" rapidly
    Then only one value-change event fires after 500ms pause

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Number Inputs"
    Then URL contains "/test/number-inputs"
```

---

## View 3: `/test/number-inputs`

```gherkin
Feature: Number & Integer Fields

  # --- NumberField ---
  Scenario: NumberField renders with label
    Given NumberField("Price") with id="nf1"
    Then "#nf1" label is "Price"

  Scenario: NumberField type numeric value
    When type "42.5" into "#nf1"
    Then Span#nf1-val text is "42.5"

  Scenario: NumberField set_value programmatic
    Given NumberField with set_value(99.9)
    Then "#nf-pre" value is "99.9"

  Scenario: NumberField set_min/set_max client validation
    Given NumberField with set_min(0), set_max(100)
    When type "150" and blur
    Then "#nf-range" is invalid

  Scenario: NumberField set_step
    Given NumberField with set_step(0.5)
    Then step attribute is "0.5"

  Scenario: NumberField step buttons visible
    Given NumberField with set_step_buttons_visible(True)
    Then increment/decrement buttons visible in "#nf-step"
    When click increment
    Then value increases by step

  Scenario: NumberField clear button
    Given NumberField with value, set_clear_button_visible(True)
    When click clear
    Then value is None/empty

  Scenario: NumberField prefix/suffix
    Given NumberField with prefix=Icon("lumo:dollar"), suffix=Span("USD")
    Then prefix and suffix render

  # --- IntegerField ---
  Scenario: IntegerField renders
    Given IntegerField("Qty") with id="if1"
    Then "#if1" label is "Qty"

  Scenario: IntegerField accepts only integers
    When type "42" into "#if1"
    Then Span#if1-val text is "42" (int, not float)

  Scenario: IntegerField rejects decimal input
    When type "3.14" into "#if-dec"
    Then only "3" is accepted (client blocks ".")

  Scenario: IntegerField set_value programmatic
    Given IntegerField with set_value(7)
    Then "#if-pre" value is "7"

  Scenario: IntegerField step buttons
    Given IntegerField with set_step(2), set_step_buttons_visible(True)
    When click increment twice
    Then value is initial + 4

  Scenario: IntegerField min/max
    Given IntegerField with set_min(1), set_max(10)
    When type "15" and blur
    Then invalid

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Checkbox & Radio"
    Then URL contains "/test/checkbox-radio"
```

---

## View 4: `/test/checkbox-radio`

```gherkin
Feature: Checkbox & RadioButtonGroup

  # --- Checkbox ---
  Scenario: Checkbox renders with label
    Given Checkbox("Accept terms") with id="cb1"
    Then "#cb1" label is "Accept terms"

  Scenario: Checkbox click toggles value
    When click "#cb1"
    Then Span#cb1-val text is "True"
    When click "#cb1" again
    Then Span#cb1-val text is "False"

  Scenario: Checkbox set_value programmatic
    Given Checkbox with set_value(True)
    Then "#cb-pre" is checked

  Scenario: Checkbox set_indeterminate
    Given Checkbox with set_indeterminate(True)
    Then "#cb-ind" shows indeterminate state

  Scenario: Checkbox set_label changes label
    Given Checkbox("Old"), Button that calls cb.set_label("New")
    When click button
    Then "#cb-lbl" label is "New"

  Scenario: Checkbox set_read_only
    Given Checkbox with set_read_only(True)
    Then "#cb-ro" has readonly attribute
    When click "#cb-ro"
    Then value does NOT change

  Scenario: Checkbox required indicator
    Given Checkbox with set_required_indicator_visible(True)
    Then "#cb-req" shows required indicator

  # --- CheckboxGroup ---
  Scenario: CheckboxGroup renders items
    Given CheckboxGroup("Colors") with set_items("Red", "Green", "Blue")
    Then 3 checkboxes rendered inside "#cbg1"

  Scenario: CheckboxGroup select multiple
    When check "Red" and "Blue"
    Then Span#cbg1-val text contains "Red" and "Blue"

  Scenario: CheckboxGroup set_value programmatic
    Given CheckboxGroup with set_value({"Green", "Blue"})
    Then "Green" and "Blue" are checked

  Scenario: CheckboxGroup set_item_label_generator
    Given CheckboxGroup with items=(1,2,3), generator=lambda x: f"Item {x}"
    Then checkboxes labeled "Item 1", "Item 2", "Item 3"

  Scenario: CheckboxGroup select/deselect methods
    Given CheckboxGroup with items, Button calling cbg.select("Red")
    When click button
    Then "Red" is checked

  # --- RadioButtonGroup ---
  Scenario: RadioButtonGroup renders items
    Given RadioButtonGroup("Size") with set_items("S", "M", "L")
    Then 3 radio buttons in "#rbg1"

  Scenario: RadioButtonGroup select one
    When click "M"
    Then Span#rbg1-val text is "M"

  Scenario: RadioButtonGroup set_value programmatic
    Given RadioButtonGroup with set_value("L")
    Then "L" is selected

  Scenario: RadioButtonGroup change selection
    Given "M" selected
    When click "S"
    Then Span#rbg1-val text is "S" (only one selected)

  Scenario: RadioButtonGroup set_item_label_generator
    Given items=("sm","md","lg"), generator mapping to "Small","Medium","Large"
    Then labels are "Small", "Medium", "Large"

  Scenario: RadioButtonGroup read_only
    Given RadioButtonGroup with set_read_only(True)
    When click any radio
    Then selection does NOT change

  Scenario: RadioButtonGroup required
    Given RadioButtonGroup with set_required_indicator_visible(True)
    Then required indicator visible

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Select & ListBox"
    Then URL contains "/test/select-listbox"
```

---

## View 5: `/test/select-listbox`

```gherkin
Feature: Select & ListBox

  # --- Select ---
  Scenario: Select renders with label
    Given Select("Country") with set_items("US", "UK", "DE"), id="sel1"
    Then "#sel1" label is "Country"

  Scenario: Select choose item
    When open "#sel1" and select "UK"
    Then Span#sel1-val text is "UK"

  Scenario: Select set_value programmatic
    Given Select with set_value("DE")
    Then "#sel-pre" displays "DE"

  Scenario: Select set_placeholder
    Given Select with set_placeholder("Choose...")
    Then "#sel-ph" shows "Choose..." when empty

  Scenario: Select set_empty_selection_allowed
    Given Select with set_empty_selection_allowed(True), initial value="US"
    When select empty option
    Then value is None/empty

  Scenario: Select set_item_label_generator
    Given Select with items=("us","uk"), generator=str.upper
    Then options display "US", "UK"

  Scenario: Select prefix component
    Given Select with set_prefix_component(Icon("lumo:globe"))
    Then prefix icon renders

  Scenario: Select read_only
    Given Select with set_read_only(True)
    Then clicking "#sel-ro" does NOT open dropdown

  # --- ListBox ---
  Scenario: ListBox renders items
    Given ListBox with set_items("A", "B", "C"), id="lb1"
    Then 3 items visible

  Scenario: ListBox select item
    When click "B"
    Then Span#lb1-val text is "B"

  Scenario: ListBox set_value programmatic
    Given ListBox with set_value("C")
    Then "C" is selected

  Scenario: ListBox item_label_generator
    Given ListBox with items=(1,2,3), generator=lambda x: f"#{x}"
    Then items show "#1", "#2", "#3"

  # --- MultiSelectListBox ---
  Scenario: MultiSelectListBox renders
    Given MultiSelectListBox with set_items("X", "Y", "Z"), id="mslb1"
    Then 3 items visible

  Scenario: MultiSelectListBox select multiple
    When click "X" and "Z"
    Then Span#mslb1-val contains "X" and "Z"

  Scenario: MultiSelectListBox set_value programmatic
    Given MultiSelectListBox with set_value({"Y", "Z"})
    Then "Y" and "Z" selected

  Scenario: MultiSelectListBox deselect_all
    Given items selected, Button calling mslb.deselect_all()
    When click button
    Then no items selected

  Scenario: MultiSelectListBox read_only
    Given MultiSelectListBox with set_read_only(True)
    When click item
    Then selection does NOT change

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: ComboBox"
    Then URL contains "/test/combo-box"
```

---

## View 6: `/test/combo-box`

```gherkin
Feature: ComboBox & MultiSelectComboBox

  # --- ComboBox ---
  Scenario: ComboBox renders with label
    Given ComboBox("Fruit") with set_items("Apple","Banana","Cherry"), id="cb1"
    Then "#cb1" label is "Fruit"

  Scenario: ComboBox open and select
    When click "#cb1" to open dropdown, select "Banana"
    Then Span#cb1-val text is "Banana"

  Scenario: ComboBox set_value programmatic
    Given ComboBox with set_value("Cherry")
    Then "#cb-pre" displays "Cherry"

  Scenario: ComboBox type to filter
    When type "App" into "#cb1"
    Then dropdown shows only "Apple"

  Scenario: ComboBox set_placeholder
    Given ComboBox with set_placeholder("Search...")
    Then "#cb-ph" shows "Search..."

  Scenario: ComboBox clear button
    Given ComboBox with value, set_clear_button_visible(True)
    When click clear
    Then value is None

  Scenario: ComboBox allow_custom_value
    Given ComboBox with set_allow_custom_value(True), custom_value_listener → Span#cb-cust
    When type "Mango" and press Enter
    Then Span#cb-cust text is "Mango"

  Scenario: ComboBox item_label_generator
    Given ComboBox items=({"id":1,"name":"Apple"}, ...), generator=lambda x: x["name"]
    Then dropdown shows "Apple", "Banana", "Cherry"

  Scenario: ComboBox set_page_size
    Given ComboBox with 100 items, set_page_size(20)
    Then lazy loading works (scroll loads more)

  Scenario: ComboBox auto_open disabled
    Given ComboBox with set_auto_open(False)
    When focus "#cb-noauto"
    Then dropdown does NOT open automatically

  # --- MultiSelectComboBox ---
  Scenario: MultiSelectComboBox renders
    Given MultiSelectComboBox("Tags") with set_items("A","B","C"), id="mscb1"
    Then "#mscb1" label is "Tags"

  Scenario: MultiSelectComboBox select multiple
    When open and select "A", then open again and select "C"
    Then Span#mscb1-val contains "A" and "C"
    And chips "A" and "C" visible in input

  Scenario: MultiSelectComboBox set_value programmatic
    Given MultiSelectComboBox with set_value({"B","C"})
    Then "B" and "C" chips visible

  Scenario: MultiSelectComboBox deselect via chip remove
    Given "A","B" selected
    When remove chip "A"
    Then only "B" remains

  Scenario: MultiSelectComboBox deselect_all
    Given items selected, Button calling mscb.deselect_all()
    When click button
    Then no items selected, no chips

  Scenario: MultiSelectComboBox clear button
    Given MultiSelectComboBox with value, set_clear_button_visible(True)
    When click clear
    Then all deselected

  Scenario: MultiSelectComboBox item_label_generator
    Given items=(1,2,3), generator=lambda x: f"Tag-{x}"
    Then chips and dropdown show "Tag-1", "Tag-2", "Tag-3"

  Scenario: MultiSelectComboBox allow_custom_value
    Given set_allow_custom_value(True)
    When type "New" and Enter
    Then custom value event fires

  Scenario: MultiSelectComboBox read_only
    Given set_read_only(True)
    Then cannot open dropdown or modify selection

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Date & Time"
    Then URL contains "/test/date-time"
```

---

## View 7: `/test/date-time`

```gherkin
Feature: DatePicker, TimePicker, DateTimePicker

  # --- DatePicker ---
  Scenario: DatePicker renders with label
    Given DatePicker("Birthday") with id="dp1"
    Then "#dp1" label is "Birthday"

  Scenario: DatePicker set_value and read
    Given DatePicker with set_value(date(2025, 6, 15))
    Then "#dp-pre" displays "6/15/2025" or locale equivalent

  Scenario: DatePicker user input
    When type "2025-01-20" into "#dp1" and blur/close
    Then Span#dp1-val shows "2025-01-20"

  Scenario: DatePicker clear button
    Given DatePicker with value, set_clear_button_visible(True)
    When click clear
    Then value is None

  Scenario: DatePicker min/max validation
    Given DatePicker with set_min(date(2025,1,1)), set_max(date(2025,12,31))
    When type "2024-06-01" and blur
    Then "#dp-range" is invalid

  # --- TimePicker ---
  Scenario: TimePicker renders with label
    Given TimePicker("Meeting time") with id="tp1"
    Then "#tp1" label is "Meeting time"

  Scenario: TimePicker set_value
    Given TimePicker with set_value(time(14, 30))
    Then "#tp-pre" displays "14:30" or locale equivalent

  Scenario: TimePicker user select
    When open "#tp1" and select a time from dropdown
    Then Span#tp1-val shows selected time

  Scenario: TimePicker set_step
    Given TimePicker with set_step(1800) (30 min)
    Then dropdown shows times at 30-min intervals

  Scenario: TimePicker min/max
    Given TimePicker with set_min(time(9,0)), set_max(time(17,0))
    When type "20:00" and blur
    Then invalid

  Scenario: TimePicker clear button
    Given TimePicker with value, set_clear_button_visible(True)
    When click clear
    Then value is None

  # --- DateTimePicker ---
  Scenario: DateTimePicker renders
    Given DateTimePicker("Event") with id="dtp1"
    Then "#dtp1" label is "Event"

  Scenario: DateTimePicker set_value
    Given DateTimePicker with set_value(datetime(2025, 6, 15, 14, 30))
    Then date part shows "6/15/2025", time part shows "14:30"

  Scenario: DateTimePicker user input
    When set date "2025-03-10" and time "09:00"
    Then Span#dtp1-val shows "2025-03-10T09:00"

  Scenario: DateTimePicker date_placeholder / time_placeholder
    Given set_date_placeholder("Pick date"), set_time_placeholder("Pick time")
    Then placeholders visible in each sub-field

  Scenario: DateTimePicker min/max
    Given min=datetime(2025,1,1,0,0), max=datetime(2025,12,31,23,59)
    When enter out-of-range datetime
    Then invalid

  # --- Shared ---
  Scenario: DatePicker set_i18n (localization)
    Given DatePicker with set_i18n({"monthNames": ["Enero",...]})
    When open calendar
    Then month names are localized

  # --- Nav ---
  Scenario: Nav to next view
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
  Scenario: Grid renders with header and data rows
    Then grid has 3 column headers: "Name", "Age", "Email"
    And data rows match item count

  Scenario: Grid add_column with property name
    Given grid.add_column("name", header="Name")
    Then column shows person.name for each row

  Scenario: Grid set_items replaces data
    Given Button that calls grid.set_items(new_list)
    When click button
    Then grid shows new data

  # --- Column properties ---
  Scenario: Column set_header
    Given column with set_header("Full Name")
    Then header text is "Full Name"

  Scenario: Column set_width
    Given column with set_width("200px")
    Then column width is ~200px

  Scenario: Column set_flex_grow
    Given column with set_flex_grow(2)
    Then column takes proportionally more space

  Scenario: Column set_auto_width
    Given column with set_auto_width(True)
    Then column width adjusts to content

  Scenario: Column set_resizable
    Given column with set_resizable(True)
    Then column resize handle is visible

  Scenario: Column set_text_align
    Given column with set_text_align("center")
    Then cell content is centered

  Scenario: Column set_frozen
    Given column with set_frozen(True)
    Then column stays visible on horizontal scroll

  Scenario: Column set_frozen_to_end
    Given column with set_frozen_to_end(True)
    Then column frozen to right edge

  Scenario: Column set_visible(False)
    Given column with set_visible(False)
    Then column is hidden, other columns still show

  Scenario: Column set_footer_text
    Given column with set_footer_text("Total: 10")
    Then footer shows "Total: 10"

  # --- Renderers ---
  Scenario: Grid LitRenderer
    Given column with LitRenderer("<span>${item.name} (${item.age})</span>")
    Then cells show "Alice (30)", "Bob (25)", etc.

  Scenario: Grid ComponentRenderer
    Given column with ComponentRenderer(lambda p: Button(p.name))
    Then each cell contains a Button with person name

  Scenario: Grid ComponentRenderer click
    Given ComponentRenderer Button with click listener → Span#grid-click
    When click button in first row
    Then Span#grid-click text is person name

  # --- Header rows ---
  Scenario: Grid prepend_header_row (column groups)
    Given grid.prepend_header_row() with join on Name+Email columns
    Then merged header cell spans 2 columns

  # --- Column reorder ---
  Scenario: Grid set_column_reorder_allowed
    Given grid.set_column_reorder_allowed(True)
    Then columns can be reordered by drag (verify attribute)

  # --- Data provider ---
  Scenario: Grid with CallbackDataProvider
    Given grid with set_data_provider(callback_provider) for 1000 items
    When scroll down
    Then new rows load lazily

  # --- Nav ---
  Scenario: Nav to next view
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
  Scenario: Grid single selection mode
    Given grid.set_selection_mode(SelectionMode.SINGLE)
    When click row "Alice"
    Then Span#grid2-sel text is "Alice"

  Scenario: Grid single select_item programmatic
    Given Button calling grid.select_item(bob)
    When click button
    Then "Bob" row is highlighted

  Scenario: Grid single deselect
    Given "Alice" selected, click "Alice" again
    Then selection is empty

  # --- Selection MULTI ---
  Scenario: Grid multi selection mode
    Given grid.set_selection_mode(SelectionMode.MULTI)
    Then checkbox column appears

  Scenario: Grid multi select multiple
    When check "Alice" and "Charlie"
    Then Span#grid2-sel contains "Alice, Charlie"

  Scenario: Grid multi select_all
    Given Button calling grid.select_all()
    When click button
    Then all rows selected

  Scenario: Grid multi deselect_all
    Given all selected, Button calling grid.deselect_all()
    When click button
    Then no rows selected

  # --- Sorting ---
  Scenario: Grid sortable column
    Given column with set_sortable(True)
    When click "Name" header
    Then rows sorted alphabetically ascending

  Scenario: Grid sort toggle descending
    When click "Name" header again
    Then rows sorted descending

  Scenario: Grid multi_sort
    Given grid.set_multi_sort(True)
    When sort by "Age" then shift-click "Name"
    Then rows sorted by age then name

  Scenario: Grid sort listener
    Given grid.add_sort_listener → Span#grid2-sort
    When click sortable column
    Then Span#grid2-sort shows sort info

  # --- Click events ---
  Scenario: Grid item click
    Given grid.add_item_click_listener → Span#grid2-click
    When click row "Bob"
    Then Span#grid2-click text is "Bob"

  Scenario: Grid item double click
    Given grid.add_item_double_click_listener → Span#grid2-dbl
    When double-click row "Alice"
    Then Span#grid2-dbl text is "Alice"

  # --- Selection listener ---
  Scenario: Grid selection listener
    Given grid.add_selection_listener → Span#grid2-selev
    When select "Charlie"
    Then Span#grid2-selev text is "Charlie"

  # --- Column ops ---
  Scenario: Grid remove_column
    Given Button calling grid.remove_column(email_col)
    When click button
    Then only "Name" and "Age" columns remain

  # --- Nav ---
  Scenario: Nav to next view
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

  Scenario: TreeGrid renders root items
    Then 2 root items visible: "Root1", "Root2"
    And tree toggle (expand arrow) visible on items with children

  Scenario: TreeGrid expand item
    When click expand on "Root1"
    Then "Child1A" and "Child1B" become visible (indented)

  Scenario: TreeGrid collapse item
    Given "Root1" expanded
    When click collapse on "Root1"
    Then children hidden

  Scenario: TreeGrid expand nested
    When expand "Root2", then expand "Child2A"
    Then "GC2A1" visible at level 2

  Scenario: TreeGrid expand_item programmatic
    Given Button calling tg.expand_item(root1)
    When click button
    Then "Root1" children visible

  Scenario: TreeGrid collapse_item programmatic
    Given root1 expanded, Button calling tg.collapse_item(root1)
    When click button
    Then children hidden

  Scenario: TreeGrid column with hierarchy toggle
    Then first column has tree toggle icons
    And other columns render normally

  Scenario: TreeGrid selection works
    Given tg.set_selection_mode(SelectionMode.SINGLE)
    When click "Child1A"
    Then Span#tg1-sel text is "Child1A"

  Scenario: TreeGrid sorting
    Given sortable column
    When click header to sort
    Then root items sorted, children maintain hierarchy

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Dialog"
    Then URL contains "/test/dialog"
```

---

## View 11: `/test/dialog`

```gherkin
Feature: Dialog & ConfirmDialog

  # --- Dialog ---
  Scenario: Dialog open/close
    Given Dialog#dlg1 with content Span("Hello"), Button#open calling dlg.open()
    When click "#open"
    Then dialog overlay visible with "Hello"
    When press Escape
    Then dialog closes

  Scenario: Dialog set_header_title
    Given Dialog with set_header_title("My Dialog")
    When open
    Then header shows "My Dialog"

  Scenario: Dialog header/footer components
    Given Dialog with get_header().add(Button("X")), get_footer().add(Button("OK"))
    When open
    Then "X" in header, "OK" in footer

  Scenario: Dialog set_modal(False)
    Given Dialog with set_modal(False)
    When open
    Then can interact with background (no backdrop overlay)

  Scenario: Dialog set_draggable
    Given Dialog with set_draggable(True)
    When open
    Then dialog can be dragged (draggable attribute set)

  Scenario: Dialog set_resizable
    Given Dialog with set_resizable(True)
    When open
    Then resize handles visible

  Scenario: Dialog set_close_on_esc(False)
    Given Dialog with set_close_on_esc(False)
    When open and press Escape
    Then dialog stays open

  Scenario: Dialog set_close_on_outside_click(False)
    Given Dialog with set_close_on_outside_click(False)
    When open and click outside
    Then dialog stays open

  Scenario: Dialog set_width/set_height
    Given Dialog with set_width("600px"), set_height("400px")
    When open
    Then dialog dimensions are ~600x400

  Scenario: Dialog add/remove content
    Given Dialog with Button("Add") calling dlg.add(Span("new"))
    When open, click "Add"
    Then "new" span appears in dialog

  Scenario: Dialog close listener
    Given Dialog with add_close_listener → Span#dlg-closed
    When open then close
    Then Span#dlg-closed text is "closed"

  # --- ConfirmDialog ---
  Scenario: ConfirmDialog basic
    Given ConfirmDialog with header="Delete?", text="Are you sure?", confirm_text="Yes"
    When open
    Then shows "Delete?", "Are you sure?", "Yes" button

  Scenario: ConfirmDialog confirm
    Given add_confirm_listener → Span#cd-result
    When click "Yes"
    Then Span#cd-result text is "confirmed"
    And dialog closes

  Scenario: ConfirmDialog cancel
    Given set_cancelable(True), set_cancel_text("No"), add_cancel_listener
    When click "No"
    Then Span#cd-result text is "cancelled"

  Scenario: ConfirmDialog reject
    Given set_rejectable(True), set_reject_text("Never"), add_reject_listener
    When click "Never"
    Then Span#cd-result text is "rejected"

  Scenario: ConfirmDialog button themes
    Given set_confirm_button_theme("primary"), set_reject_button_theme("error")
    When open
    Then confirm button has theme "primary", reject has "error"

  Scenario: ConfirmDialog reopen after confirm
    Given confirm listener closes dialog
    When open, confirm, then open again
    Then dialog opens again correctly

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Notification & Popover"
    Then URL contains "/test/notification-popover"
```

---

## View 12: `/test/notification-popover`

```gherkin
Feature: Notification & Popover

  # --- Notification ---
  Scenario: Notification.show static
    Given Button calling Notification.show("Saved!", 3000)
    When click button
    Then notification visible with text "Saved!"

  Scenario: Notification auto-close after duration
    Given Notification.show("Quick", 1000)
    When wait 1.5s
    Then notification is gone

  Scenario: Notification position
    Given Notification with position=TOP_CENTER
    When open
    Then notification appears at top center

  Scenario: Notification with components
    Given Notification with add(Span("msg"), Button("Undo"))
    When open
    Then notification shows "msg" and "Undo" button

  Scenario: Notification theme variant
    Given Notification with add_theme_variants(LUMO_SUCCESS)
    When open
    Then notification has success styling (green)

  Scenario: Notification close programmatic
    Given Notification with duration=0 (stays open), Button#close calling notif.close()
    When open, then click "#close"
    Then notification closes

  Scenario: Notification close listener
    Given Notification with add_close_listener → Span#notif-closed
    When open and close
    Then Span#notif-closed text is "closed"

  Scenario: Notification multiple positions
    Given 3 notifications: TOP_START, BOTTOM_END, MIDDLE
    When open all
    Then each appears in correct position

  # --- Popover ---
  Scenario: Popover renders with target
    Given Button#pop-target, Popover with set_target(btn), add(Span("Pop content"))
    When click "#pop-target"
    Then popover opens with "Pop content"

  Scenario: Popover close on outside click
    Given Popover open
    When click outside popover
    Then popover closes

  Scenario: Popover set_position
    Given Popover with set_position(PopoverPosition.TOP)
    When open
    Then popover appears above target

  Scenario: Popover set_modal
    Given Popover with set_modal(True)
    When open
    Then backdrop visible, cannot interact with background

  Scenario: Popover open/close programmatic
    Given Button#pop-open calling popover.open(), Button#pop-close calling popover.close()
    When click "#pop-open"
    Then popover opens
    When click "#pop-close"
    Then popover closes

  Scenario: Popover set_open_on_hover
    Given Popover with set_open_on_hover(True)
    When hover over target
    Then popover opens

  Scenario: Popover close on Esc
    Given Popover open
    When press Escape
    Then popover closes

  Scenario: Popover listeners
    Given add_open_listener → Span#pop-ev, add_close_listener appending
    When open then close
    Then Span#pop-ev tracks "opened,closed"

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Tabs & Accordion"
    Then URL contains "/test/tabs-accordion"
```

---

## View 13: `/test/tabs-accordion`

```gherkin
Feature: Tabs, TabSheet, Accordion, Details

  # --- Tabs ---
  Scenario: Tabs render
    Given Tabs(Tab("One"), Tab("Two"), Tab("Three")) with id="tabs1"
    Then 3 tabs visible

  Scenario: Tabs select by click
    When click "Two"
    Then Span#tabs1-val text is "1" (index)

  Scenario: Tabs set_selected_index
    Given Button calling tabs.set_selected_index(2)
    When click button
    Then "Three" is selected

  Scenario: Tabs set_orientation vertical
    Given Tabs with set_orientation("vertical")
    Then tabs render vertically

  Scenario: Tabs add tab dynamically
    Given Button calling tabs.add(Tab("Four"))
    When click button
    Then 4 tabs visible

  Scenario: Tabs selected_change_listener
    Given add_selected_change_listener → Span#tabs1-ev
    When click "Three"
    Then Span#tabs1-ev shows "2"

  # --- TabSheet ---
  Scenario: TabSheet renders tabs with content
    Given TabSheet with add_tab(Tab("Info"), Span("Info content"))
    And add_tab(Tab("Settings"), Span("Settings content"))
    Then "Info" tab active, "Info content" visible

  Scenario: TabSheet switch tab
    When click "Settings"
    Then "Settings content" visible, "Info content" hidden

  Scenario: TabSheet selected_change_listener
    Given add_selected_change_listener → Span#ts-ev
    When switch tab
    Then event fires

  # --- Accordion ---
  Scenario: Accordion renders panels
    Given Accordion with add("Panel 1", Span("Content 1")), add("Panel 2", Span("Content 2"))
    Then 2 panels visible, first opened by default

  Scenario: Accordion open panel
    When click "Panel 2" summary
    Then "Content 2" visible, "Content 1" collapsed

  Scenario: Accordion close all
    Given accordion.close()
    Then all panels collapsed

  Scenario: Accordion open by index
    Given accordion.open(1)
    Then "Panel 2" is open

  Scenario: Accordion opened_change_listener
    Given add_opened_change_listener → Span#acc-ev
    When click panel
    Then event fires with index

  # --- Details ---
  Scenario: Details renders with summary
    Given Details("More info", Span("Hidden content"))
    Then summary "More info" visible, content hidden

  Scenario: Details toggle open
    When click summary "More info"
    Then "Hidden content" visible

  Scenario: Details set_opened programmatic
    Given Button calling details.set_opened(True)
    When click button
    Then content visible

  Scenario: Details opened_change_listener
    Given add_opened_change_listener → Span#det-ev
    When toggle
    Then event fires

  Scenario: Details set_summary_text
    Given Details, Button calling details.set_summary_text("New summary")
    When click button
    Then summary text is "New summary"

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Menu"
    Then URL contains "/test/menu"
```

---

## View 14: `/test/menu`

```gherkin
Feature: MenuBar & ContextMenu

  # --- MenuBar ---
  Scenario: MenuBar renders items
    Given MenuBar with items: "File" (sub: "New", "Open"), "Edit" (sub: "Copy", "Paste")
    Then 2 top-level buttons: "File", "Edit"

  Scenario: MenuBar click top item
    When click "File"
    Then submenu opens with "New", "Open"

  Scenario: MenuBar click sub item
    When click "File" → "New"
    Then Span#mb-result text is "New"

  Scenario: MenuBar nested submenu
    Given "Edit" → "Paste" → "Paste Special"
    When click "Edit" → "Paste" → "Paste Special"
    Then Span#mb-result text is "Paste Special"

  Scenario: MenuBar disabled item
    Given MenuItem "Open" with set_enabled(False)
    When click "File"
    Then "Open" appears disabled

  Scenario: MenuBar checkable item
    Given MenuItem "Bold" with set_checkable(True)
    When click "Bold"
    Then item toggles checked state

  Scenario: MenuBar open on hover
    Given MenuBar with set_open_on_hover(True)
    When hover "File"
    Then submenu opens without click

  # --- ContextMenu ---
  Scenario: ContextMenu opens on right-click
    Given Div#ctx-target with ContextMenu, items: "Cut", "Copy", "Paste"
    When right-click "#ctx-target"
    Then context menu opens with 3 items

  Scenario: ContextMenu click item
    When click "Copy"
    Then Span#ctx-result text is "Copy"
    And menu closes

  Scenario: ContextMenu open_on_click
    Given ContextMenu with set_open_on_click(True)
    When left-click "#ctx-target2"
    Then context menu opens

  Scenario: ContextMenu nested items
    Given "Paste" with children "Paste as Text", "Paste Special"
    When open, hover "Paste"
    Then submenu shows

  Scenario: ContextMenu item click fires listener
    Given add_item_click_listener → Span#ctx-ev
    When select item
    Then event fires

  Scenario: ContextMenu disabled item
    Given item "Cut" disabled
    Then "Cut" appears grayed out

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Layouts"
    Then URL contains "/test/layouts"
```

---

## View 15: `/test/layouts`

```gherkin
Feature: Layouts

  # --- VerticalLayout ---
  Scenario: VerticalLayout renders children vertically
    Given VerticalLayout(Span("A"), Span("B"), Span("C"))
    Then children are stacked vertically (A above B above C)

  Scenario: VerticalLayout set_spacing
    Given VerticalLayout with set_spacing(False)
    Then no gap between children

  Scenario: VerticalLayout set_padding
    Given VerticalLayout with set_padding(True)
    Then layout has internal padding

  Scenario: VerticalLayout expand
    Given VerticalLayout with 2 children, expand(child2)
    Then child2 takes remaining space (flex-grow: 1)

  Scenario: VerticalLayout set_justify_content_mode CENTER
    Given VerticalLayout with set_justify_content_mode(JustifyContentMode.CENTER)
    Then children centered vertically

  Scenario: VerticalLayout set_align_items CENTER
    Given VerticalLayout with set_align_items(Alignment.CENTER)
    Then children centered horizontally

  Scenario: VerticalLayout add/remove dynamically
    Given Button#add calling layout.add(Span("New"))
    When click "#add"
    Then "New" appears

  Scenario: VerticalLayout replace
    Given layout with Span("Old"), Button calling layout.replace(old, Span("New"))
    When click
    Then "Old" replaced by "New"

  # --- HorizontalLayout ---
  Scenario: HorizontalLayout renders children horizontally
    Given HorizontalLayout(Span("A"), Span("B"), Span("C"))
    Then children are in a row (A left of B left of C)

  Scenario: HorizontalLayout expand
    Given HorizontalLayout, expand(child1)
    Then child1 takes remaining horizontal space

  Scenario: HorizontalLayout set_spacing(False)
    Then no gap between children

  Scenario: HorizontalLayout vertical alignment
    Given set_default_vertical_component_alignment(Alignment.CENTER)
    Then children vertically centered

  # --- FlexLayout ---
  Scenario: FlexLayout set_flex_direction column
    Given FlexLayout with set_flex_direction("column")
    Then children stacked vertically

  Scenario: FlexLayout set_flex_wrap
    Given FlexLayout with set_flex_wrap("wrap"), many children
    Then children wrap to next line when full

  Scenario: FlexLayout per-child flex
    Given FlexLayout, set_flex_grow(2, child1), set_flex_grow(1, child2)
    Then child1 takes 2x space of child2

  # --- FormLayout ---
  Scenario: FormLayout renders fields in columns
    Given FormLayout with 4 TextFields
    Then fields arranged in responsive columns

  Scenario: FormLayout set_responsive_steps
    Given set_responsive_steps(("0", 1), ("600px", 2))
    Then at narrow width: 1 column, at wide: 2 columns

  # --- SplitLayout ---
  Scenario: SplitLayout renders primary/secondary
    Given SplitLayout with add_to_primary(Span("Left")), add_to_secondary(Span("Right"))
    Then "Left" and "Right" side by side with splitter

  Scenario: SplitLayout vertical orientation
    Given set_orientation_vertical(True)
    Then top/bottom layout

  Scenario: SplitLayout splitter position
    Given set_splitter_position("30%")
    Then primary takes ~30% of space

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Card & Scroller"
    Then URL contains "/test/card-scroller"
```

---

## View 16: `/test/card-scroller`

```gherkin
Feature: Card, Scroller, MasterDetailLayout

  # --- Card ---
  Scenario: Card renders with title
    Given Card with set_title("My Card")
    Then title "My Card" visible in title slot

  Scenario: Card subtitle
    Given Card with set_subtitle("Subtitle text")
    Then subtitle visible

  Scenario: Card content
    Given Card with add(Span("Body text"))
    Then "Body text" in default content area

  Scenario: Card footer
    Given Card with add_to_footer(Button("Action"))
    Then "Action" button in footer slot

  Scenario: Card media slot
    Given Card with set_media(Image("photo.jpg"))
    Then image in media slot

  Scenario: Card header prefix/suffix
    Given Card with set_header_prefix(Icon("lumo:star")), set_header_suffix(Button("X"))
    Then icon before title, button after title

  # --- Scroller ---
  Scenario: Scroller renders with content
    Given Scroller(Div("Scrollable content"), scroll_direction=ScrollDirection.VERTICAL)
    Then scroller renders with vertical scrollbar when content overflows

  Scenario: Scroller set_scroll_direction HORIZONTAL
    Given Scroller with set_scroll_direction(ScrollDirection.HORIZONTAL)
    Then horizontal scrollbar, no vertical

  Scenario: Scroller set_content replaces
    Given Scroller with Span("Old"), then set_content(Span("New"))
    Then "New" visible, "Old" gone

  # --- MasterDetailLayout ---
  Scenario: MasterDetailLayout renders
    Given MasterDetailLayout with set_master(Span("Master")), set_detail(Span("Detail"))
    Then master and detail panels visible

  Scenario: MasterDetailLayout drawer width
    Given MasterDetailLayout with set_drawer_width("400px")
    Then detail panel width is ~400px

  Scenario: MasterDetailLayout toggle visibility
    Given set_drawer_toggle_visible(True)
    Then toggle button visible for detail panel

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Upload"
    Then URL contains "/test/upload"
```

---

## View 17: `/test/upload`

```gherkin
Feature: Upload

  Scenario: Upload renders
    Given Upload#upload1 with set_receiver(callback)
    Then upload area visible with button

  Scenario: Upload file succeeds
    Given add_succeeded_listener → Span#upload-result
    When upload a small .txt file
    Then Span#upload-result shows filename

  Scenario: Upload max_files
    Given set_max_files(2)
    Then cannot upload more than 2 files

  Scenario: Upload max_file_size
    Given set_max_file_size(1024) (1KB)
    When try to upload a 2KB file
    Then file is rejected

  Scenario: Upload accepted_file_types
    Given set_accepted_file_types(".txt", ".csv")
    Then file input accept attribute is ".txt,.csv"

  Scenario: Upload auto_upload disabled
    Given set_auto_upload(False)
    When select file
    Then file is listed but NOT uploaded yet

  Scenario: Upload drop_allowed
    Given set_drop_allowed(True)
    Then drop area is visible (no "drop" disabled state)

  Scenario: Upload set_i18n
    Given set_i18n({"uploading": {"status": {"processing": "Procesando..."}}} )
    Then localized strings appear

  Scenario: Upload file_rejected_listener
    Given add_file_rejected_listener → Span#upload-rej, set_max_file_size(100)
    When upload large file
    Then Span#upload-rej shows rejection reason

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Display Components"
    Then URL contains "/test/display"
```

---

## View 18: `/test/display`

```gherkin
Feature: ProgressBar, Avatar, AvatarGroup, Markdown, MessageInput, MessageList

  # --- ProgressBar ---
  Scenario: ProgressBar renders
    Given ProgressBar#pb1 with set_value(0.6)
    Then progress bar at 60%

  Scenario: ProgressBar update value
    Given Button calling pb.set_value(0.9)
    When click button
    Then progress bar at 90%

  Scenario: ProgressBar indeterminate
    Given ProgressBar with set_indeterminate(True)
    Then shows indeterminate animation

  Scenario: ProgressBar min/max
    Given set_min(0), set_max(200), set_value(100)
    Then renders at 50% (100/200)

  # --- Avatar ---
  Scenario: Avatar renders with name
    Given Avatar("Sophia Williams") with id="av1"
    Then avatar shows initials "SW"

  Scenario: Avatar abbreviation
    Given Avatar with set_abbreviation("JD")
    Then shows "JD"

  Scenario: Avatar image
    Given Avatar with set_image("https://example.com/photo.jpg")
    Then avatar shows image

  Scenario: Avatar color_index
    Given Avatar with set_color_index(3)
    Then avatar uses color variant 3

  # --- AvatarGroup ---
  Scenario: AvatarGroup renders items
    Given AvatarGroup with 5 items
    Then 5 avatars visible

  Scenario: AvatarGroup max_items_visible
    Given AvatarGroup with 5 items, set_max_items_visible(3)
    Then 3 avatars + overflow indicator (+2)

  # --- Markdown ---
  Scenario: Markdown renders content
    Given Markdown("# Hello\n**bold** text") with id="md1"
    Then rendered HTML shows h1 "Hello" and bold text

  Scenario: Markdown update content
    Given Button calling md.set_content("## Updated")
    When click
    Then rendered HTML shows h2 "Updated"

  # --- MessageInput ---
  Scenario: MessageInput renders
    Given MessageInput#mi1 with add_submit_listener → Span#mi-result
    Then input field and submit button visible

  Scenario: MessageInput submit
    When type "Hello world" and press Enter (or click submit)
    Then Span#mi-result text is "Hello world"

  # --- MessageList ---
  Scenario: MessageList renders items
    Given MessageList with set_items([{"text":"Hi","userName":"Alice"}])
    Then message "Hi" from "Alice" visible

  Scenario: MessageList multiple items
    Given set_items with 3 messages
    Then 3 messages rendered in order

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: HTML Elements"
    Then URL contains "/test/html-elements"
```

---

## View 19: `/test/html-elements`

```gherkin
Feature: HTML Elements

  Scenario: H1 renders
    Given H1("Title") with id="h1"
    Then <h1> with text "Title"

  Scenario: H2 renders
    Given H2("Subtitle") with id="h2"
    Then <h2> with text "Subtitle"

  Scenario: H3-H6 render
    Given H3("H3"), H4("H4"), H5("H5"), H6("H6")
    Then each renders correct heading level

  Scenario: Paragraph renders
    Given Paragraph("Lorem ipsum") with id="p1"
    Then <p> with text "Lorem ipsum"

  Scenario: Span renders
    Given Span("inline") with id="sp1"
    Then <span> with text "inline"

  Scenario: Div renders with children
    Given Div with add(Span("child1"), Span("child2"))
    Then <div> contains 2 <span> children

  Scenario: Div set_text
    Given Div with set_text("text content")
    Then div shows "text content"

  Scenario: Anchor renders
    Given Anchor(href="https://example.com", text="Link")
    Then <a href="https://example.com"> with text "Link"

  Scenario: Anchor set_target
    Given Anchor with set_target("_blank")
    Then target attribute is "_blank"

  Scenario: IFrame renders
    Given IFrame(src="about:blank") with id="iframe1"
    Then <iframe src="about:blank">

  Scenario: Hr renders
    Given Hr()
    Then <hr> element exists

  Scenario: Pre renders
    Given Pre("code block") with id="pre1"
    Then <pre> with text "code block"

  Scenario: Image renders
    Given Image(src="logo.png", alt="Logo") with id="img1"
    Then <img src="logo.png" alt="Logo">

  Scenario: NativeLabel renders
    Given NativeLabel("Field label") with id="lbl1"
    Then <label> with text "Field label"

  Scenario: HTML containers (Header, Footer, Section, Nav, Main)
    Given Header(), Footer(), Section(), Nav(), Main()
    Then each renders its semantic HTML tag

  # --- Nav ---
  Scenario: Nav to next view
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
  Scenario: set_visible(False) hides component
    Given Button#vis-btn, Button#toggle calling vis_btn.set_visible(False)
    When click "#toggle"
    Then "#vis-btn" is not displayed

  Scenario: set_visible(True) shows component
    Given hidden component, toggle calling set_visible(True)
    When click toggle
    Then component visible

  # --- Enabled ---
  Scenario: set_enabled(False) disables
    Given Button#en-btn, Button#toggle-en calling en_btn.set_enabled(False)
    When click "#toggle-en"
    Then "#en-btn" has disabled attribute

  Scenario: set_enabled(True) re-enables
    Given disabled component
    When enable
    Then disabled attribute removed

  # --- CSS Classes ---
  Scenario: add_class_name
    Given Span#cls-span, Button calling span.add_class_name("highlight")
    When click button
    Then "#cls-span" has class "highlight"

  Scenario: remove_class_name
    Given Span with class "old", Button calling remove_class_name("old")
    When click button
    Then class "old" removed

  Scenario: set_class_name toggle
    Given Span, Button calling set_class_name("active", True) then set_class_name("active", False)
    When click twice
    Then class toggled

  # --- Inline Styles ---
  Scenario: get_style().set
    Given Span#sty-span, Button calling span.get_style().set("color", "red")
    When click button
    Then "#sty-span" has inline style color: red

  Scenario: get_style().remove
    Given Span with color:red, Button calling get_style().remove("color")
    When click button
    Then color style removed

  # --- Size ---
  Scenario: set_width / set_height
    Given Div#size-div, Button calling div.set_width("300px"), div.set_height("100px")
    When click button
    Then div is 300x100px

  Scenario: set_size_full
    Given Div#full-div, Button calling div.set_size_full()
    When click button
    Then div width=100%, height=100%

  Scenario: set_min_width / set_max_width
    Given Div, set_min_width("100px"), set_max_width("500px")
    Then min-width and max-width applied

  # --- Themes ---
  Scenario: add_theme_name
    Given Button#theme-btn, Button calling theme_btn.add_theme_name("primary")
    When click
    Then "#theme-btn" has theme="primary"

  Scenario: remove_theme_name
    Given Button with theme "primary error", remove "error"
    Then theme is "primary" only

  # --- ID ---
  Scenario: set_id
    Given Span, Button calling span.set_id("my-span")
    When click button
    Then element has id="my-span"

  # --- Tooltip ---
  Scenario: set_tooltip_text
    Given Button#tip-btn with set_tooltip_text("Click me!")
    When hover over "#tip-btn"
    Then tooltip "Click me!" visible

  # --- Helper text ---
  Scenario: set_helper_text on field
    Given TextField#help-tf with set_helper_text("Enter name")
    Then helper text "Enter name" visible below field

  # --- ARIA ---
  Scenario: set_aria_label
    Given Button#aria-btn with set_aria_label("Close dialog")
    Then aria-label="Close dialog"

  Scenario: set_aria_labelled_by
    Given Span#label-el with "Name", TextField#aria-tf with set_aria_labelled_by("label-el")
    Then aria-labelledby="label-el"

  # --- Focus/Blur ---
  Scenario: focus() programmatic
    Given TextField#focus-tf, Button calling focus_tf.focus()
    When click button
    Then "#focus-tf" is focused

  Scenario: add_focus_listener / add_blur_listener
    Given TextField#fb-tf with add_focus_listener → Span#fb-ev, add_blur_listener appending
    When click "#fb-tf" then click elsewhere
    Then Span#fb-ev tracks "focus,blur"

  # --- Nav ---
  Scenario: Nav to next view
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
  Scenario: TextField set_read_only(True)
    Given Button calling tf.set_read_only(True)
    When click button
    Then "#mix-tf" has readonly attribute
    And cannot type into field

  Scenario: Select set_read_only(True)
    Given Button calling sel.set_read_only(True)
    When click button
    Then "#mix-sel" cannot open dropdown

  Scenario: DatePicker set_read_only
    When set_read_only(True)
    Then cannot open calendar

  Scenario: set_read_only(False) restores
    Given readonly field, Button calling set_read_only(False)
    When click button
    Then field is editable again

  # --- HasValidation ---
  Scenario: TextField set_invalid(True)
    Given Button calling tf.set_invalid(True)
    When click button
    Then "#mix-tf" shows invalid state (red border)

  Scenario: TextField set_error_message
    Given tf.set_error_message("Required field"), tf.set_invalid(True)
    Then error message "Required field" visible below field

  Scenario: Select set_invalid + error_message
    Given sel.set_invalid(True), sel.set_error_message("Choose one")
    Then Select shows "Choose one" error

  Scenario: ComboBox set_invalid + error_message
    Given cb.set_invalid(True), cb.set_error_message("Invalid selection")
    Then ComboBox shows error

  Scenario: set_invalid(False) clears error
    Given invalid field, Button calling set_invalid(False)
    When click button
    Then error state cleared

  # --- HasRequired ---
  Scenario: TextField set_required_indicator_visible(True)
    Given Button calling tf.set_required_indicator_visible(True)
    When click
    Then "#mix-tf" shows required indicator (*)

  Scenario: Select required indicator
    Given sel.set_required_indicator_visible(True)
    Then required indicator visible

  Scenario: ComboBox required indicator
    Given cb.set_required_indicator_visible(True)
    Then required indicator visible

  Scenario: DatePicker required indicator
    Given dp.set_required_indicator_visible(True)
    Then required indicator visible

  Scenario: Client-side required validation
    Given TextField with required=True
    When focus, leave empty, blur
    Then field shows invalid (client validates required)

  # --- Combined mixins ---
  Scenario: Read-only field with error shows error but not editable
    Given tf.set_read_only(True), tf.set_invalid(True), tf.set_error_message("Error")
    Then field shows error but cannot be edited

  Scenario: Required + validation
    Given tf.set_required_indicator_visible(True), type value, clear, blur
    Then client validates and shows required error

  # --- Nav ---
  Scenario: Nav to next view
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
  Scenario: read_bean populates fields
    Given binder.read_bean(Person("Alice", "alice@x.com", 30))
    Then name="Alice", email="alice@x.com", age="30"

  Scenario: read_bean(None) clears fields
    Given fields populated, binder.read_bean(None)
    Then all fields empty

  # --- write_bean ---
  Scenario: write_bean writes form to object
    Given fields filled: name="Bob", email="bob@x.com", age="25"
    When click "#save"
    Then person object has name="Bob", email="bob@x.com", age=25
    And Span#binder-result text is "Bob,bob@x.com,25"

  # --- Validation ---
  Scenario: Required validator blocks save
    Given name field with as_required("Name is required")
    When leave name empty, click "#save"
    Then name field shows error "Name is required"
    And Span#binder-result does NOT update

  Scenario: Pattern validator
    Given email field with with_validator(email_pattern, "Invalid email")
    When type "not-email" in email, click save
    Then email shows "Invalid email"

  Scenario: Value range validator on age
    Given age with with_validator(lambda v: 0 < v < 150, "Invalid age")
    When type "200", click save
    Then age shows error

  Scenario: Valid form saves successfully
    Given all fields valid
    When click "#save"
    Then Span#binder-result shows saved values

  # --- Converters ---
  Scenario: String to int converter
    Given age field with with_converter(string_to_int)
    When type "abc" in age, click save
    Then conversion error shown

  # --- Dirty tracking ---
  Scenario: is_dirty after change
    Given binder.read_bean(person)
    When type in name field
    Then Span#dirty shows "true"

  Scenario: is_dirty false after read_bean
    Given binder.read_bean(person)
    Then Span#dirty shows "false"

  # --- set_bean ---
  Scenario: set_bean enables automatic sync
    Given binder.set_bean(person)
    When type "New Name" in name field
    Then person.name is updated immediately (no save needed)
    And Span#auto-sync shows "New Name"

  # --- Bean-level validation ---
  Scenario: Cross-field validator
    Given binder.with_validator(lambda p: p.age >= 18 if p.name else True, "Must be adult")
    When name="Minor", age=10, click save
    Then bean-level error "Must be adult"

  # --- remove_binding ---
  Scenario: Remove binding
    Given binding for name, Button calling binder.remove_binding(name_binding)
    When click, then modify name, click save
    Then name field changes NOT written to bean

  # --- Multiple fields invalid ---
  Scenario: Multiple validation errors
    Given name required, email pattern, age range
    When all invalid, click save
    Then all 3 fields show errors simultaneously

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Navigation"
    Then URL contains "/test/navigation"
```

---

## View 23: `/test/navigation`

```gherkin
Feature: Navigation — Routes, AppLayout, SideNav

  # --- Basic routing ---
  Scenario: @Route registers view
    Given view registered at "/test/navigation"
    Then view renders when navigating to that URL

  Scenario: Route with parameter
    Given @Route("/test/nav-param/:id")
    When navigate to "/test/nav-param/42"
    Then Span#param shows "42"

  Scenario: Route with optional parameter
    Given @Route("/test/nav-opt/:q?")
    When navigate to "/test/nav-opt"
    Then Span#opt shows "" (empty)
    When navigate to "/test/nav-opt/search"
    Then Span#opt shows "search"

  Scenario: @PageTitle sets title
    Given view with @PageTitle("My Page")
    Then document.title is "My Page"

  Scenario: Route page_title param
    Given @Route("/test/nav-title", page_title="Test Title")
    Then document.title is "Test Title"

  # --- RouterLink ---
  Scenario: RouterLink navigates without reload
    Given RouterLink("/test/nav-target", "Go to target")
    When click link
    Then URL changes to "/test/nav-target"
    And page did NOT fully reload (client-side navigation)

  Scenario: RouterLink with components
    Given RouterLink with add(Icon("lumo:arrow-right"), Span("Go"))
    Then link contains icon and text

  # --- AppLayout ---
  Scenario: AppLayout renders navbar + content
    Given layout with set_navbar(H1("App")), content=view
    Then navbar with "App" at top, view content below

  Scenario: AppLayout drawer
    Given layout with set_drawer(SideNav(...))
    Then drawer visible on left

  Scenario: AppLayout drawer toggle
    Given DrawerToggle in navbar
    When click toggle
    Then drawer opens/closes

  # --- SideNav ---
  Scenario: SideNav renders items
    Given SideNav with items: "Home"(/), "Users"(/users), "Settings"(/settings)
    Then 3 nav items visible

  Scenario: SideNav item click navigates
    When click "Users" item
    Then URL changes to "/users"

  Scenario: SideNav nested items
    Given "Settings" with children "General", "Security"
    When expand "Settings"
    Then "General", "Security" visible

  # --- Nav ---
  Scenario: Nav to next view
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

  Scenario: Push updates UI from background thread
    Given Button#start starts background task: sleep 1s → update Span#push-result
    When click "#start"
    Then within 3s, Span#push-result text is "done"

  Scenario: Multiple push updates
    Given background task sends 3 updates: "1", "2", "3" with 500ms delay each
    When click "#start"
    Then Span#push-count reaches "3" within 3s

  Scenario: Push ProgressBar update
    Given background task updates ProgressBar value from 0 to 1 in steps
    When click "#start"
    Then progress bar reaches 100% within 3s

  Scenario: UI.access runs callback
    Given Button triggering UI.access(lambda: span.set_text("accessed"))
    When click
    Then Span#push-access text is "accessed"

  Scenario: Push with component add
    Given background task adds Span("pushed") to layout
    When click "#start"
    Then "pushed" appears in layout

  Scenario: Push preserves existing UI state
    Given TextField with value "keep", background task adds new component
    When click "#start"
    Then TextField still has "keep" AND new component appears

  Scenario: Multiple rapid pushes
    Given task sends 10 updates rapidly (no delay)
    When click "#start"
    Then all 10 updates received (Span#push-count is "10")

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Theme"
    Then URL contains "/test/theme"
```

---

## View 25: `/test/theme`

```gherkin
Feature: Theme Switching & Styles

  # --- Theme switching ---
  Scenario: Default Lumo light theme
    Then <html> has theme link for Lumo
    And background is light

  Scenario: Switch to dark variant
    Given Button calling UI.set_theme_variant("dark")
    When click
    Then <html> has theme="dark" attribute
    And background is dark

  Scenario: Switch back to light
    Given dark active, Button calling UI.set_theme_variant("light")
    When click
    Then light theme restored

  Scenario: Switch to Aura theme
    Given Button calling UI.set_theme("aura", "light")
    When click
    Then theme link changes to Aura

  Scenario: Switch to Aura dark
    Given Button calling UI.set_theme("aura", "dark")
    When click
    Then Aura dark active, color-scheme: dark applied

  # --- @ColorScheme ---
  Scenario: Initial color scheme from decorator
    Given @ColorScheme("dark") on AppShell
    Then app starts in dark mode

  # --- @StyleSheet ---
  Scenario: Global stylesheet loaded
    Given @StyleSheet("styles/global.css") on @AppShell
    Then CSS from global.css is applied

  Scenario: View-specific stylesheet
    Given @StyleSheet("styles/test-theme.css") on test view
    Then CSS rules from test-theme.css applied

  Scenario: Styles apply to components
    Given CSS rule ".custom-btn { background: green; }" in stylesheet
    And Button with add_class_name("custom-btn")
    Then button has green background

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: ClientCallable"
    Then URL contains "/test/client-callable"
```

---

## View 26: `/test/client-callable`

```gherkin
Feature: @ClientCallable

  Scenario: Server method called from client JS
    Given component with @ClientCallable def greet(name): self.result.set_text(f"Hello {name}")
    And Button whose click executes JS: this.$server.greet("World")
    When click button
    Then Span#cc-result text is "Hello World"

  Scenario: @ClientCallable with return value
    Given @ClientCallable def compute(a, b): return a + b
    And JS calling this.$server.compute(3, 4).then(r => display(r))
    When trigger
    Then result shows "7"

  Scenario: @ClientCallable with no args
    Given @ClientCallable def ping(): self.result.set_text("pong")
    When trigger from JS
    Then result is "pong"

  Scenario: @ClientCallable multiple methods
    Given @ClientCallable def method1, def method2
    When call method1 then method2
    Then both execute correctly

  Scenario: @ClientCallable with string arg
    Given @ClientCallable def echo(msg): return msg
    When call with "test string"
    Then returns "test string"

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: CustomField"
    Then URL contains "/test/custom-field"
```

---

## View 27: `/test/custom-field`

```gherkin
Feature: CustomField

  Scenario: CustomField renders child fields
    Given CustomField#cf1 containing TextField("First"), TextField("Last")
    Then both text fields visible inside custom field

  Scenario: CustomField label
    Given CustomField with set_label("Full Name")
    Then label "Full Name" visible

  Scenario: CustomField value from children
    When type "John" in first, "Doe" in last
    Then custom field value combines both

  Scenario: CustomField value_change_listener
    Given add_value_change_listener → Span#cf-val
    When modify child fields
    Then event fires

  Scenario: CustomField set_read_only
    Given set_read_only(True)
    Then child fields are read-only

  Scenario: CustomField set_invalid + error_message
    Given set_invalid(True), set_error_message("Invalid name")
    Then error displayed

  Scenario: CustomField required
    Given set_required_indicator_visible(True)
    Then required indicator visible

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: VirtualList"
    Then URL contains "/test/virtual-list"
```

---

## View 28: `/test/virtual-list`

```gherkin
Feature: VirtualList

  Scenario: VirtualList renders items
    Given VirtualList#vl1 with set_items(["Item 1", ..., "Item 100"])
    And LitRenderer("<div>${item}</div>")
    Then items render in scrollable list

  Scenario: VirtualList scroll loads more
    Given 1000 items
    When scroll down
    Then more items become visible

  Scenario: VirtualList LitRenderer with properties
    Given items = [Person(name, age)], LitRenderer with with_property("name", lambda p: p.name)
    Then each row shows person name

  Scenario: VirtualList ComponentRenderer
    Given ComponentRenderer(lambda item: HorizontalLayout(Icon("lumo:user"), Span(item.name)))
    Then each row has icon + name

  Scenario: VirtualList set_items replaces
    Given Button calling vl.set_items(new_list)
    When click
    Then new items displayed

  Scenario: VirtualList with DataProvider
    Given CallbackDataProvider for lazy loading
    When scroll
    Then items fetched on demand

  Scenario: VirtualList item_label_generator
    Given set_item_label_generator(lambda x: x.upper())
    Then items displayed in uppercase

  # --- Nav ---
  Scenario: Nav to next view
    When click link "Next: Login"
    Then URL contains "/test/login"
```

---

## View 29: `/test/login`

```gherkin
Feature: LoginForm & LoginOverlay

  # --- LoginForm ---
  Scenario: LoginForm renders
    Given LoginForm#lf1
    Then username field, password field, and submit button visible

  Scenario: LoginForm submit
    Given add_login_listener → Span#lf-result
    When type "admin" in username, "pass123" in password, submit
    Then Span#lf-result text is "admin:pass123"

  Scenario: LoginForm error state
    Given login listener calls lf.set_error(True)
    When submit with wrong credentials
    Then error message visible in form

  Scenario: LoginForm forgot_password
    Given add_forgot_password_listener → Span#lf-forgot
    When click "Forgot password?" link
    Then Span#lf-forgot text is "forgot"

  Scenario: LoginForm set_i18n
    Given set_i18n({"form": {"title": "Iniciar sesion"}})
    Then form title is "Iniciar sesion"

  # --- LoginOverlay ---
  Scenario: LoginOverlay renders when opened
    Given LoginOverlay#lo1, set_opened(True)
    Then overlay visible with login form

  Scenario: LoginOverlay set_title
    Given set_title("My App")
    Then overlay shows "My App"

  Scenario: LoginOverlay set_description
    Given set_description("Enter credentials")
    Then description text visible

  Scenario: LoginOverlay submit
    Given add_login_listener → Span#lo-result
    When type credentials and submit
    Then Span#lo-result shows credentials

  Scenario: LoginOverlay close
    Given opened overlay
    When close
    Then overlay hidden

  # --- Final ---
  Scenario: All tests complete
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
