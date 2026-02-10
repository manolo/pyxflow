import datetime

from vaadin.flow import Menu, Route
from demo.services import people_service
from demo.views.main_layout import MainLayout
from vaadin.flow.components import (
    Accordion,
    Avatar,
    AvatarGroup,
    AvatarGroupItem,
    Button,
    Card,
    Checkbox,
    CheckboxGroup,
    ComboBox,
    ComponentRenderer,
    ConfirmDialog,
    ContextMenu,
    DatePicker,
    DateTimePicker,
    Details,
    Dialog,
    Div,
    DrawerToggle,
    Footer,
    EmailField,
    FlexDirection,
    FlexLayout,
    FormLayout,
    Grid,
    H2,
    H3,
    Header,
    HorizontalLayout,
    Icon,
    IntegerField,
    LitRenderer,
    Markdown,
    MasterDetailLayout,
    MenuBar,
    Notification,
    NotificationVariant,
    NumberField,
    PasswordField,
    Popover,
    PopoverPosition,
    ProgressBar,
    RadioButtonGroup,
    RouterLink,
    Scroller,
    ScrollDirection,
    Select,
    SideNav,
    SideNavItem,
    Span,
    Tab,
    Tabs,
    TabSheet,
    TextArea,
    TextField,
    TimePicker,
    Upload,
    VerticalLayout,
    MessageInput,
    MessageList,
    MessageListItem,
    ListBox,
    MultiSelectListBox,
    CustomField,
    LoginForm,
    MultiSelectComboBox,
    VirtualList,
)
from vaadin.flow.components.horizontal_layout import Alignment
from vaadin.flow.core.keys import Key
from vaadin.flow.data import (
    Binder,
    CallbackDataProvider,
    ListDataProvider,
    Query,
    ValidationError,
    email,
    max_length,
    min_length,
    required,
    string_to_int,
    value_range,
)


class CrudPerson:
    _next_id = 1

    def __init__(self, name="", email="", age=0, role="", city="", department=""):
        self.id = CrudPerson._next_id
        CrudPerson._next_id += 1
        self.name = name
        self.email = email
        self.age = age
        self.role = role
        self.city = city
        self.department = department

    @staticmethod
    def from_dict(d: dict) -> "CrudPerson":
        return CrudPerson(d["name"], d["email"], int(d["age"]), d["role"], d["city"], d["department"])


@Route("components", page_title="Components Demo", layout=MainLayout)
@Menu(title="Components", order=2, icon="vaadin:grid-small")
class ComponentsDemoView(VerticalLayout):
    def __init__(self):
        self.add_class_name("components-view")
        self.click_count = 0

        # --- LoginForm ---
        section = self.add_section("LoginForm", "tall")

        login_form = LoginForm()
        self.login_label = Span("Login status: (none)")
        login_form.add_login_listener(
            lambda e: self.login_label.set_text(f"Login: {e['username']}")
        )
        login_form.add_forgot_password_listener(
            lambda e: self.login_label.set_text("Forgot password clicked")
        )
        section.add(login_form)
        section.add(self.login_label)

        # --- Theme Selector (ListBox) ---
        section = self.add_section("ListBox")
        list_box = ListBox()
        list_box.set_items("Lumo Light", "Lumo Dark", "Aura Light", "Aura Dark")
        list_box.set_value("Lumo Light")
        def _on_theme_selected(e):
            value = e['value']
            if not value:
                return
            parts = value.lower().split()
            self._ui.set_theme(parts[0], parts[1])
        list_box.add_value_change_listener(_on_theme_selected)
        section.add(Span("Select Theme"))
        section.add(list_box)

        # --- Progress ---
        section = self.add_section("ProgressBar")

        progress_bar = ProgressBar()
        progress_bar.set_value(0.6)
        section.add(Span("(60%)"))
        section.add(progress_bar)

        progress_indeterminate = ProgressBar()
        progress_indeterminate.set_indeterminate(True)
        section.add(Span("(indeterminate)"))
        section.add(progress_indeterminate)

        # --- Navigation ---
        section = self.add_section("Navigation")

        navigation = VerticalLayout()

        navigation.add(RouterLink("Go to Hello World", "/hello"))
        navigation.add(RouterLink("Go to About", "/"))
        navigation.add(RouterLink("Go to Greet", "/greet/World"))

        section.add(navigation)

        # --- Avatar ---
        section = self.add_section("Avatar")

        avatar1 = Avatar("Sophia Williams")
        avatar2 = Avatar()
        avatar2.set_name("Hugo Santos")
        avatar2.set_abbreviation("HS")
        avatar2.set_color_index(3)
        section.add(HorizontalLayout(avatar1, avatar2))

        # --- AvatarGroup ---
        section = self.add_section("AvatarGroup")

        avatar_group = AvatarGroup()
        avatar_group.add(
            AvatarGroupItem("Sophia Williams"),
            AvatarGroupItem("Hugo Santos"),
            AvatarGroupItem("Diana Novak"),
            AvatarGroupItem("Rashid Traore"),
        )
        avatar_group.set_max_items_visible(3)
        section.add(avatar_group)

        # --- Tabs ---
        section = self.add_section("Tabs")

        tab1 = Tab("Tab 1")
        tab2 = Tab("Tab 2")
        tab3 = Tab("Tab 3")
        tabs = Tabs(tab1, tab2, tab3)
        self.tabs_label = Span("Selected tab: Tab 1")
        tabs.add_selected_change_listener(self.on_tab_selected)
        self.tabs = tabs
        self.tab_list = [tab1, tab2, tab3]
        section.add(tabs)
        section.add(self.tabs_label)

        # --- TabSheet ---
        section = self.add_section("TabSheet")

        tab_sheet = TabSheet()
        tab_sheet.add("Dashboard", Span("Dashboard content"))
        tab_sheet.add("Settings", Span("Settings content"))
        section.add(tab_sheet)

        # --- MenuBar ---
        section = self.add_section("MenuBar")

        menu_bar = MenuBar()
        self.menu_label = Span("Menu action: (none)")
        file_item = menu_bar.add_item("File")
        file_item.get_sub_menu().add_item("New", lambda e: self.menu_label.set_text("Menu action: New"))
        file_item.get_sub_menu().add_item("Open", lambda e: self.menu_label.set_text("Menu action: Open"))
        edit_item = menu_bar.add_item("Edit")
        edit_item.get_sub_menu().add_item("Undo", lambda e: self.menu_label.set_text("Menu action: Undo"))
        menu_bar.add_item("Help", lambda e: self.menu_label.set_text("Menu action: Help"))
        section.add(menu_bar)
        section.add(self.menu_label)

        # --- Popover ---
        section = self.add_section("Popover")

        popover_target = Button("Click for Popover")
        popover = Popover()
        popover.set_target(popover_target)
        popover.add(Span("Popover content"))
        popover.add(Span("Click outside to close"))
        popover.set_position(PopoverPosition.BOTTOM)
        popover.set_open_on_click(True)
        section.add(popover_target)
        section.add(popover)

        # --- Details ---
        section = self.add_section("Details")

        details1 = Details("Contact information",
            Span("Sophia Williams — (501) 555-9128"))
        details1.set_opened(True)
        section.add(details1)

        details2 = Details("Billing address", Span("4027 Amber Lake Canyon, Springfield"))
        section.add(details2)

        # --- Accordion ---
        section = self.add_section("Accordion", "col-span-2")

        accordion = Accordion()
        accordion.add("Personal information",
            Span("Name: Sophia Williams\nEmail: sophia.williams@company.com"))
        accordion.add("Billing address",
            Span("4027 Amber Lake Canyon"))
        accordion.add("Payment method",
            Span("Visa ending in 1234"))
        accordion.open(0)
        section.add(accordion)

        # --- ContextMenu ---
        section = self.add_section("ContextMenu")

        self.context_label = Span("Context action: (none)")
        context_target = Span("Right-click here for context menu")
        context_target._set_style("padding", "var(--vaadin-padding-s, var(--lumo-space-s, 0.5rem))")
        context_target._set_style("background", "var(--vaadin-background-container, var(--lumo-primary-color-10pct, rgba(0, 100, 200, 0.1)))")
        context_target._set_style("border-radius", "var(--vaadin-radius-m, var(--lumo-border-radius-m, 8px))")

        context_menu = ContextMenu(context_target)
        context_menu.add_item("View", lambda e: self.context_label.set_text("Context action: View"))
        context_menu.add_item("Edit", lambda e: self.context_label.set_text("Context action: Edit"))
        context_menu.add_separator()
        context_menu.add_item("Delete", lambda e: self.context_label.set_text("Context action: Delete"))
        section.add(context_menu)
        section.add(self.context_label)

        # --- Markdown ---
        section = self.add_section("Markdown", "col-span-2")

        markdown = Markdown("""
## Rich Text Formatting

You can create **bold text**, *italicized text*, and `inline code` with Markdown.

### Lists
1. First item
2. Second item
3. Third item

- Apples
- Bananas
- Oranges

> Markdown is rendered by the `vaadin-markdown` component (new in Vaadin 25).

[Visit Vaadin website](https://vaadin.com)
""")
        section.add(markdown)

        # --- Buttons & Actions ---
        section = self.add_section("Buttons & Actions", "col-span-3")

        button = Button("Click Me!")
        button.add_theme_name("primary")
        button.add_click_listener(self.on_button_click)

        dialog_btn = Button("Open Dialog")
        dialog_btn.add_click_listener(self.open_dialog)

        notification_btn = Button("Show Notification")
        notification_btn.add_theme_name("tertiary")
        notification_btn.add_click_listener(self.show_notification)

        success_btn = Button("Success Notification")
        success_btn.add_theme_name("success", "primary")
        success_btn.add_click_listener(self.show_success)

        error_btn = Button("Error Notification")
        error_btn.add_theme_name("error", "primary")
        error_btn.add_click_listener(self.show_error)

        test_error_btn = Button("Throw Server Error")
        test_error_btn.add_theme_name("error", "tertiary")
        test_error_btn.add_click_listener(self.trigger_error)

        button_row = HorizontalLayout()
        button_row.add(button, dialog_btn, notification_btn, success_btn, error_btn, test_error_btn)
        section.add(button_row)

        self.click_label = Span("Click count: 0")
        section.add(self.click_label)

        # Dialog (hidden initially — overlay, not a visible card)
        self.dialog = Dialog()
        self.dialog.set_header_title("Sample Dialog")
        self.dialog.add(Span("This is a dialog with some content."))
        self.dialog.add(Span("You can close it by clicking outside."))
        self.add(self.dialog)

        # --- Component Features ---
        section = self.add_section("Component Features", "col-span-2")

        features_form = FormLayout()

        helper_field = TextField("With Helper Text")
        helper_field.set_helper_text("This is a helper text")
        helper_field.set_id("helper-text-field")
        features_form.add(helper_field)

        tooltip_field = TextField("With Tooltip")
        tooltip_field.set_tooltip_text("Hover to see this tooltip")
        features_form.add(tooltip_field)

        section.add(features_form)

        shortcut_label = Span("Shortcut: (none)")
        self.shortcut_label = shortcut_label
        shortcut_btn = Button("Press Enter (shortcut)")
        shortcut_btn.add_click_shortcut(Key.ENTER)
        shortcut_btn.add_click_listener(lambda e: self.shortcut_label.set_text("Shortcut: Button"))
        section.add(HorizontalLayout(shortcut_btn, shortcut_label))

        # --- Text Input Fields ---
        section = self.add_section("Text Input Fields", "col-span-2")

        text_form = FormLayout()

        text_field = TextField("TextField")
        text_field.set_value("Hello PyFlow!")
        text_form.add(text_field)

        password_field = PasswordField("PasswordField")
        password_field.set_placeholder("Enter password")
        text_form.add(password_field)

        email_field = EmailField("EmailField")
        email_field.set_placeholder("name@example.com")
        email_field.set_clear_button_visible(True)
        text_form.add(email_field)

        phone_field = TextField("Phone")
        phone_field.set_pattern("^[+]?[\\(]?[0-9]{3}[\\)]?[\\-]?[0-9]{3}[\\-]?[0-9]{4,6}$")
        phone_field.set_allowed_char_pattern("[0-9()+-]");
        text_form.add(phone_field)

        text_area = TextArea("TextArea")
        text_area.set_placeholder("Enter multiline text...")
        text_area.set_min_rows(1)
        text_area.set_max_rows(4)
        text_form.add(text_area)

        section.add(text_form)

        # --- Numeric Fields ---
        section = self.add_section("Numeric Fields")

        numeric_form = FormLayout()

        number_field = NumberField("NumberField")
        number_field.set_value(3.14)
        number_field.set_min(0)
        number_field.set_max(100)
        numeric_form.add(number_field)

        integer_field = IntegerField("IntegerField")
        integer_field.set_value(42)
        integer_field.set_step(5)
        numeric_form.add(integer_field)

        section.add(numeric_form)

        # --- Date, Time & Upload ---
        section = self.add_section("Date, Time & Upload", "col-span-2")

        date_time_form = FormLayout()

        date_picker = DatePicker("DatePicker")
        date_picker.set_value(datetime.date.today())
        date_time_form.add(date_picker)

        time_picker = TimePicker("TimePicker")
        time_picker.set_step(1800)
        time_picker.set_value(datetime.time(12, 0))
        date_time_form.add(time_picker)

        date_time_picker = DateTimePicker("Meeting date and time")
        date_time_picker.set_value(datetime.datetime(2025, 6, 15, 14, 30))
        date_time_picker.set_step(1800)
        date_time_form.add(date_time_picker)

        upload = Upload()
        upload_label = Span("Upload status: (none)")
        upload.set_receiver(self.on_upload_received)
        upload.add_succeeded_listener(self.on_upload_succeeded)
        date_time_form.add(upload)

        section.add(date_time_form)
        date_time_form.add(upload_label)

        # --- Selection Components ---
        section = self.add_section("Selection Components", "col-span-2")

        selection_form = FormLayout()

        checkbox = Checkbox("Single Checkbox")
        selection_form.add(checkbox)

        combo_box = ComboBox("ComboBox")
        combo_box.set_items("Firefox", "Chrome", "Safari", "Edge", "Opera")
        combo_box.set_placeholder("Select a browser")
        selection_form.add(combo_box)

        select = Select("Select")
        select.set_items("Option A", "Option B", "Option C")
        select.set_placeholder("Choose an option")
        selection_form.add(select)

        multi_combo = MultiSelectComboBox("MultiSelectComboBox")
        multi_combo.set_items("Java", "Python", "JavaScript", "TypeScript", "Rust", "Go")
        multi_combo.set_placeholder("Select skills")
        selection_form.add(multi_combo)

        radio_group = RadioButtonGroup("RadioButtonGroup")
        radio_group.set_items("Choice 1", "Choice 2", "Choice 3")
        selection_form.add(radio_group)

        checkbox_group = CheckboxGroup("CheckboxGroup")
        checkbox_group.set_items("Item X", "Item Y", "Item Z")
        selection_form.add(checkbox_group)
        section.add(selection_form)

        section = self.add_section("MultiSelectListBox")
        multi_list_box = MultiSelectListBox()
        multi_list_box.set_items("Option A", "Option B", "Option C", "Option D")
        multi_list_box_label = Span("MultiSelectListBox selected: (none)")
        multi_list_box.add_value_change_listener(
            lambda e: multi_list_box_label.set_text(
                f"MultiSelectListBox selected: {', '.join(sorted(e['value']))}" if e['value'] else "MultiSelectListBox selected: (none)"
            )
        )
        section.add(multi_list_box)
        section.add(multi_list_box_label)

        # --- Custom Fields ---
        section = self.add_section("Custom Fields")

        custom_form = FormLayout()

        custom_field = CustomField("Phone")
        prefix = Select()
        prefix.set_items("+1", "+44", "+358")
        prefix.set_width("100px")
        number = TextField("Phone number")
        custom_field.add(prefix, number)
        custom_form.add(custom_field)

        section.add(custom_form)

        # --- FlexLayout ---
        section = self.add_section("FlexLayout", "col-span-2")

        header_div = Header("Header")
        header_div.set_width("100%")
        header_div.set_height("60px")
        header_div._set_style("background-color", "var(--vaadin-focus-ring-color, var(--lumo-primary-color, #006af5))")
        header_div._set_style("color", "#fff")
        header_div._set_style("display", "flex")
        header_div._set_style("align-items", "center")
        header_div._set_style("justify-content", "center")

        footer_div = Footer("Footer")
        footer_div.set_width("100%")
        footer_div.set_height("50px")
        footer_div._set_style("background-color", "var(--vaadin-background-container-strong, var(--lumo-contrast-20pct, rgba(0, 0, 0, 0.2)))")
        footer_div._set_style("color", "var(--vaadin-text-color, var(--lumo-body-text-color, inherit))")
        footer_div._set_style("display", "flex")
        footer_div._set_style("align-items", "center")
        footer_div._set_style("justify-content", "center")

        nav_div = Div("Navigation")
        nav_div.set_width("25%")
        nav_div._set_style("background-color", "var(--vaadin-background-container, var(--lumo-primary-color-10pct, rgba(0, 100, 200, 0.1)))")
        nav_div._set_style("display", "flex")
        nav_div._set_style("align-items", "center")
        nav_div._set_style("justify-content", "center")

        content_div = Div("Content")
        content_div.set_width("75%")
        content_div._set_style("background-color", "var(--vaadin-background-container, var(--lumo-contrast-5pct, rgba(0, 0, 0, 0.05)))")
        content_div._set_style("color", "var(--vaadin-text-color, var(--lumo-body-text-color, inherit))")
        content_div._set_style("display", "flex")
        content_div._set_style("align-items", "center")
        content_div._set_style("justify-content", "center")

        middle = FlexLayout(nav_div, content_div)
        middle.set_width("100%")

        page_layout = FlexLayout(header_div, middle, footer_div)
        page_layout.set_flex_direction(FlexDirection.COLUMN)
        page_layout.set_width("100%")
        page_layout.set_height("300px")
        page_layout.expand(middle)

        section.add(page_layout)

        # --- Shared data for all grids ---
        people = [p.to_dict() for p in people_service.find_all()]

        # --- CRUD Master-Detail ---
        section = self.add_section("CRUD Master-Detail (Binder)", "col-span-3")

        self.crud_people = [CrudPerson.from_dict(p) for p in people]
        crud_roles = sorted({p["role"] for p in people})
        crud_departments = sorted({p["department"] for p in people})
        self.crud_selected: CrudPerson | None = None
        self.crud_is_new = False

        self.crud_layout = MasterDetailLayout()
        self.crud_layout.set_width_full()
        self.crud_layout.set_detail_size("400px")

        # Master: Grid
        self.crud_master = VerticalLayout()

        self.crud_grid = Grid()
        self.crud_grid.set_columns("name", "email", "age", "role", "city", "department")
        self.crud_grid.add_selection_listener(self._crud_on_select)
        self._crud_refresh_grid()

        crud_new_btn = Button("+ New Person")
        crud_new_btn.add_theme_name("primary")
        crud_new_btn.add_click_listener(self._crud_on_new)

        self.crud_master.add(self.crud_grid, crud_new_btn)

        # Detail: Form (not attached until selection or new)
        self.crud_detail = VerticalLayout()

        crud_form = FormLayout()

        self.crud_name = TextField("Name")
        self.crud_email = EmailField("Email")
        self.crud_age = TextField("Age")
        self.crud_role = Select("Role")
        self.crud_role.set_items(*crud_roles)
        self.crud_city = TextField("City")
        self.crud_dept = Select("Department")
        self.crud_dept.set_items(*crud_departments)

        crud_form.add(self.crud_name, self.crud_email, self.crud_age,
                      self.crud_role, self.crud_city, self.crud_dept)
        self.crud_detail.add(crud_form)

        crud_btn_bar = HorizontalLayout()
        crud_save = Button("Save")
        crud_save.add_theme_name("primary")
        crud_save.add_click_listener(self._crud_on_save)
        crud_delete = Button("Delete")
        crud_delete.add_theme_name("error")
        crud_delete.add_click_listener(self._crud_on_delete)
        crud_cancel = Button("Cancel")
        crud_cancel.add_click_listener(self._crud_on_cancel)
        crud_btn_bar.add(crud_save, crud_delete, crud_cancel)
        self.crud_detail.add(crud_btn_bar)

        self.crud_layout.set_master(self.crud_master)
        # Detail starts as None — master gets full width
        section.add(self.crud_layout)

        # Binder setup
        self.binder = Binder(CrudPerson)

        self.binder.for_field(self.crud_name) \
            .as_required("Name is required") \
            .with_validator(min_length(2, "Name must be at least 2 characters")) \
            .with_validator(max_length(50, "Name must be at most 50 characters")) \
            .bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))

        self.binder.for_field(self.crud_email) \
            .as_required("Email is required") \
            .with_validator(email("Please enter a valid email address")) \
            .bind(lambda p: p.email, lambda p, v: setattr(p, 'email', v))

        self.binder.for_field(self.crud_age) \
            .as_required("Age is required") \
            .with_converter(string_to_int("Age must be a number")) \
            .with_validator(value_range(1, 120, "Age must be between 1 and 120")) \
            .bind(lambda p: p.age, lambda p, v: setattr(p, 'age', v))

        self.binder.for_field(self.crud_role) \
            .as_required("Role is required") \
            .bind(lambda p: p.role, lambda p, v: setattr(p, 'role', v))

        self.binder.for_field(self.crud_city) \
            .bind(lambda p: p.city, lambda p, v: setattr(p, 'city', v))

        self.binder.for_field(self.crud_dept) \
            .as_required("Department is required") \
            .bind(lambda p: p.department, lambda p, v: setattr(p, 'department', v))

        # ConfirmDialog for delete (overlay — not a visible card)
        self.crud_confirm = ConfirmDialog()
        self.crud_confirm.set_header("Confirm Delete")
        self.crud_confirm.set_text("Are you sure you want to delete this person?")
        self.crud_confirm.set_confirm_text("Delete")
        self.crud_confirm.set_confirm_button_theme("error primary")
        self.crud_confirm.set_cancelable(True)
        self.crud_confirm.add_confirm_listener(self._crud_do_delete)
        self.add(self.crud_confirm)

        # ConfirmDialog for cancel with unsaved changes (overlay)
        self.crud_cancel_confirm = ConfirmDialog()
        self.crud_cancel_confirm.set_header("Unsaved changes")
        self.crud_cancel_confirm.set_text("You have unsaved changes. Discard them?")
        self.crud_cancel_confirm.set_confirm_text("Discard")
        self.crud_cancel_confirm.set_confirm_button_theme("error primary")
        self.crud_cancel_confirm.set_cancelable(True)
        self.crud_cancel_confirm.add_confirm_listener(lambda e: self._crud_clear_form())
        self.add(self.crud_cancel_confirm)

        # --- Grid ---
        section = self.add_section("Grid", "col-span-2")

        grid = Grid()
        grid.add_column("name", header="Name").set_auto_width(True).set_sortable(True)
        grid.add_column("email", header="Email").set_auto_width(True).set_sortable(True)
        grid.add_column("role", header="Role").set_sortable(True)
        grid.add_column("city", header="City").set_auto_width(True).set_sortable(True).set_resizable(True)
        grid.add_column("department", header="Department").set_sortable(True).set_resizable(True)
        grid.set_column_reordering_allowed(True)
        grid.set_items(people)
        self.grid_selection_label = Span("Selected: (none)")
        grid.add_selection_listener(self.on_grid_select)
        section.add(grid)
        section.add(self.grid_selection_label)

        # --- Grid with LitRenderer ---
        section = self.add_section("Grid with LitRenderer", "col-span-2")

        lit_grid = Grid()
        lit_grid.add_column(
            LitRenderer.of('<strong>${item.name}</strong>')
            .with_property("name", lambda item: item["name"]),
            header="Name",
        ).set_auto_width(True)
        lit_grid.add_column(
            LitRenderer.of('<span theme="badge">${item.role}</span>')
            .with_property("role", lambda item: item["role"]),
            header="Role",
        )
        lit_grid.add_column("city", header="City").set_auto_width(True)
        self.lit_renderer_label = Span("LitRenderer action: (none)")
        lit_grid.add_column(
            LitRenderer.of(
                '<vaadin-button theme="small" @click="${handleEdit}">Edit</vaadin-button>'
            )
            .with_function("handleEdit", self.on_lit_edit),
            header="Actions",
        )
        lit_grid.set_items(people)
        section.add(lit_grid)
        section.add(self.lit_renderer_label)

        # --- Grid with ComponentRenderer ---
        section = self.add_section("Grid with ComponentRenderer", "col-span-2")

        comp_grid = Grid()
        comp_grid.add_column("name", header="Name").set_auto_width(True)
        comp_grid.add_column("email", header="Email").set_auto_width(True)
        self.comp_renderer_label = Span("ComponentRenderer action: (none)")
        comp_grid.add_column(
            ComponentRenderer(self.create_action_buttons),
            header="Actions",
        )
        comp_grid.set_items(people)
        section.add(comp_grid)
        section.add(self.comp_renderer_label)

        # --- Grid with ListDataProvider ---
        section = self.add_section("Grid with ListDataProvider", "col-span-2")

        dp_items = list(people)
        self.dp = ListDataProvider(dp_items)
        self.dp_add_counter = 0

        dp_grid = Grid()
        dp_grid.add_column("name", header="Name").set_auto_width(True).set_sortable(True)
        dp_grid.add_column("city", header="City").set_auto_width(True).set_sortable(True)
        dp_grid.add_column("department", header="Department").set_sortable(True)
        dp_grid.set_data_provider(self.dp)

        self.dp_filter = TextField(f"Filter by name (Items: {len(dp_items)})")
        self.dp_filter.add_value_change_listener(self._dp_on_filter)

        dp_add_btn = Button("Add Person")
        dp_add_btn.add_click_listener(self._dp_on_add)

        dp_remove_btn = Button("Remove Last")
        dp_remove_btn.add_theme_name("error")
        dp_remove_btn.add_click_listener(self._dp_on_remove)

        dp_controls = HorizontalLayout()
        dp_controls.set_default_vertical_component_alignment(Alignment.BASELINE)
        dp_controls.add(self.dp_filter, dp_add_btn, dp_remove_btn)
        section.add(dp_controls)
        section.add(dp_grid)

        # --- Grid with Lazy DataProvider ---
        section = self.add_section("Grid with Lazy DataProvider", "col-span-2", "tall")

        # Simulate a large dataset (1000 items) served lazily
        self._lazy_data = [
            {"name": f"Person {i}", "city": f"City {i % 20}", "department": f"Dept {i % 5}"}
            for i in range(1000)
        ]
        self._lazy_fetches = 0
        self._lazy_loaded = 0

        def lazy_fetch(query):
            self._lazy_fetches += 1
            items = self._lazy_data[query.offset:query.offset + query.limit]
            self._lazy_loaded += len(items)
            self._lazy_stats_label.set_text(
                f"{len(self._lazy_data)} items totales (fetches: {self._lazy_fetches}, loaded: {self._lazy_loaded})"
            )
            return items

        def lazy_count(query):
            return len(self._lazy_data)

        lazy_dp = CallbackDataProvider(lazy_fetch, lazy_count)

        lazy_grid = Grid()
        lazy_grid.add_column("name", header="Name").set_auto_width(True).set_sortable(True)
        lazy_grid.add_column("city", header="City").set_auto_width(True).set_sortable(True)
        lazy_grid.add_column("department", header="Department").set_sortable(True)
        lazy_grid.set_data_provider(lazy_dp)

        self._lazy_stats_label = Span(f"{len(self._lazy_data)} items totales (fetches: 0, loaded: 0)")
        section.add(self._lazy_stats_label)
        section.add(lazy_grid)

        # --- Icon, DrawerToggle, SideNav (for bundle inclusion) ---
        section = self.add_section("Icon / SideNav")

        home_icon = Icon("vaadin:home")
        section.add(home_icon)

        drawer_toggle = DrawerToggle()
        section.add(drawer_toggle)

        side_nav = SideNav()
        side_nav.set_label("Navigation")
        side_nav.add_item(SideNavItem("Home", "/", Icon("vaadin:home")))
        side_nav.add_item(SideNavItem("About", "/", Icon("vaadin:info-circle")))
        parent_item = SideNavItem("Settings")
        parent_item.add_item(SideNavItem("General", "/settings/general"))
        parent_item.add_item(SideNavItem("Security", "/settings/security"))
        side_nav.add_item(parent_item)
        section.add(side_nav)

        # --- Scroller ---
        section = self.add_section("Scroller")

        scroll_content = VerticalLayout()
        for i in range(1, 21):
            scroll_content.add(Span(f"Scrollable item {i}"))
        scroller = Scroller(scroll_content, scroll_direction=ScrollDirection.VERTICAL)
        scroller.set_height("200px")
        scroller.set_width("300px")
        scroller._set_style("flex", "none")
        scroller._set_style("border", "1px solid var(--vaadin-border-color, var(--lumo-contrast-20pct, rgba(0, 0, 0, 0.2)))")
        section.add(scroller)

        # --- Card ---
        section = self.add_section("Card")

        card = Card()
        card.set_title("Card Title")
        card.set_subtitle("Card subtitle")
        card.add(Span("This is the card content area."))
        card.add_to_footer(Button("Action"))
        section.add(card)

        # --- MasterDetailLayout ---
        section = self.add_section("MasterDetailLayout", "col-span-2")

        md_layout = MasterDetailLayout()
        md_master = VerticalLayout()
        for i in range(1, 4):
            md_btn = Button(f"Item {i}")
            def on_md_click(e, idx=i, layout=md_layout):
                detail = VerticalLayout()
                detail.add(H3(f"Item {idx}"))
                detail.add(Span(f"Details for item {idx}."))
                close_btn = Button("Close")
                close_btn.add_click_listener(lambda ev, l=layout: l.set_detail(None))
                detail.add(close_btn)
                layout.set_detail(detail)
            md_btn.add_click_listener(on_md_click)
            md_master.add(md_btn)
        md_layout.set_master(md_master)
        md_layout.set_height("250px")
        md_layout._set_style("border", "1px solid var(--vaadin-border-color, var(--lumo-contrast-20pct, rgba(0, 0, 0, 0.2)))")
        section.add(md_layout)

        # --- MessageInput + MessageList ---
        section = self.add_section("MessageInput + MessageList", "col-span-2")

        self.message_list = MessageList()
        self.messages = [
            MessageListItem("Hello! How can I help?", user_name="Assistant"),
        ]
        self.message_list.set_items(*self.messages)
        section.add(self.message_list)

        message_input = MessageInput()
        message_input.add_submit_listener(self._on_message_submit)
        section.add(message_input)

        # --- VirtualList ---
        section = self.add_section("VirtualList", "col-span-2")

        virtual_list = VirtualList()
        virtual_items = [{"name": f"Person {i}", "city": f"City {i % 20}", "role": f"Role {i % 5}"} for i in range(200)]
        self.vl_label = Span("VirtualList: click an item")
        virtual_list.set_renderer(
            LitRenderer.of(
                '<div style="display:flex;align-items:center;padding:var(--vaadin-padding-xs,0.25rem) var(--vaadin-padding-s,0.5rem);border-bottom:1px solid var(--vaadin-border-color-secondary,rgba(0,0,0,0.1));cursor:pointer" @click="${handleClick}">'
                '<vaadin-avatar name="${item.name}" style="margin-right:var(--vaadin-gap-s,0.5rem)"></vaadin-avatar>'
                '<div><strong>${item.name}</strong><br/><small style="color:var(--vaadin-text-color-secondary,rgba(0,0,0,0.6))">${item.city} — ${item.role}</small></div>'
                '</div>'
            )
            .with_property("name", lambda x: x["name"])
            .with_property("city", lambda x: x["city"])
            .with_property("role", lambda x: x["role"])
            .with_function("handleClick", lambda item: self.vl_label.set_text(f"VirtualList: clicked {item['name']}"))
        )
        virtual_list.set_items(virtual_items)
        virtual_list.set_height("300px")
        virtual_list._set_style("flex", "none")
        virtual_list._set_style("overflow", "auto")
        virtual_list._set_style("border", "1px solid var(--vaadin-border-color, var(--lumo-contrast-20pct, rgba(0, 0, 0, 0.2)))")
        virtual_list._set_style("border-radius", "var(--vaadin-radius-m, var(--lumo-border-radius-m, 8px))")
        section.add(virtual_list)
        section.add(self.vl_label)

    def _on_message_submit(self, event):
        self.messages.append(MessageListItem(event["value"], user_name="You"))
        self.message_list.set_items(*self.messages)

    def add_section(self, title: str, *class_names: str) -> Div:
        """Create a dashboard card. Returns the card Div to add content to."""
        card = Div()
        card.add_class_name("component")
        for cn in class_names:
            card.add_class_name(cn)
        card.add(H3(title))
        self.add(card)
        return card

    def on_grid_select(self, event):
        item = event.get("item")
        if item:
            self.grid_selection_label.set_text(f"Selected: {item['name']}")
        else:
            self.grid_selection_label.set_text("Selected: (none)")

    def on_button_click(self, event):
        self.click_count += 1
        self.click_label.set_text(f"Click count: {self.click_count}")

    def open_dialog(self, event):
        self.dialog.open()

    def show_notification(self, event):
        Notification.show("This is a notification!", 3000, Notification.Position.BOTTOM_CENTER)

    def show_success(self, event):
        n = Notification.show("Operation successful!", 3000, Notification.Position.TOP_CENTER)
        n.add_theme_variants(NotificationVariant.LUMO_SUCCESS)

    def show_error(self, event):
        n = Notification.show("Something went wrong!", 5000, Notification.Position.MIDDLE)
        n.add_theme_variants(NotificationVariant.LUMO_ERROR)

    def trigger_error(self, event):
        raise RuntimeError("Test error from click listener")

    def on_lit_edit(self, item):
        self.lit_renderer_label.set_text(f"LitRenderer action: Edit {item['name']}")

    def create_action_buttons(self, item):
        view_btn = Button(f"View {item['name']}")
        view_btn.add_click_listener(lambda e, i=item: self.on_comp_view(i))
        return view_btn

    def on_comp_view(self, item):
        self.comp_renderer_label.set_text(f"ComponentRenderer action: View {item['name']}")

    def on_tab_selected(self, event_data):
        idx = event_data.get("selectedIndex", 0)
        if 0 <= idx < len(self.tab_list):
            self.tabs_label.set_text(f"Selected tab: {self.tab_list[idx].get_label()}")

    def on_upload_received(self, filename, mime_type, data):
        self.upload_label.set_text(f"Uploaded: {filename} ({len(data)} bytes)")

    def on_upload_succeeded(self, event_data):
        pass

    # --- DataProvider methods ---

    def _dp_update_label(self):
        self.dp_filter.set_label(f"Filter by name (Items: {self.dp.size(Query())})")

    def _dp_on_filter(self, event):
        text = self.dp_filter.get_value().lower()
        if text:
            self.dp.set_filter(lambda item, t=text: t in item["name"].lower())
        else:
            self.dp.set_filter(None)
        self._dp_update_label()

    def _dp_on_add(self, event):
        self.dp_add_counter += 1
        self.dp.add_item({
            "name": f"New Person {self.dp_add_counter}",
            "email": "",
            "age": 0,
            "role": "",
            "city": "Unknown",
            "department": "Unassigned",
        })
        self._dp_update_label()

    def _dp_on_remove(self, event):
        if self.dp.items:
            self.dp.remove_item(self.dp.items[-1])
            self._dp_update_label()

    # --- CRUD Master-Detail methods ---

    def _crud_refresh_grid(self):
        items = [
            {"id": p.id, "name": p.name, "email": p.email,
             "age": p.age, "role": p.role, "city": p.city, "department": p.department}
            for p in self.crud_people
        ]
        self.crud_grid.set_items(items)

    def _crud_on_select(self, event):
        item = event.get("item")
        if item:
            person = next((p for p in self.crud_people if p.id == item["id"]), None)
            if person:
                self.crud_selected = person
                self.crud_is_new = False
                self.binder.read_bean(person)
                self.crud_layout.set_detail(self.crud_detail)
        else:
            self._crud_clear_form()

    def _crud_on_new(self, event):
        self.crud_selected = CrudPerson()
        self.crud_is_new = True
        self.binder.read_bean(self.crud_selected)
        self.crud_layout.set_detail(self.crud_detail)

    def _crud_on_save(self, event):
        if self.crud_selected is None:
            Notification.show("Select a person or click New first", 3000, Notification.Position.MIDDLE)
            return
        if not self.binder.is_dirty():
            Notification.show("No changes to save", 3000, Notification.Position.MIDDLE)
            return
        try:
            self.binder.write_bean(self.crud_selected)
        except ValidationError:
            n = Notification.show("Please fix the errors in the form", 3000, Notification.Position.MIDDLE)
            n.add_theme_variants(NotificationVariant.LUMO_ERROR)
            return
        if self.crud_is_new:
            self.crud_people.append(self.crud_selected)
            self.crud_is_new = False
        self._crud_refresh_grid()
        self.binder.read_bean(self.crud_selected)
        n = Notification.show(f"Saved: {self.crud_selected.name}", 3000, Notification.Position.MIDDLE)
        n.add_theme_variants(NotificationVariant.LUMO_SUCCESS)

    def _crud_on_delete(self, event):
        if self.crud_selected is None or self.crud_is_new:
            Notification.show("Select a person to delete", 3000, Notification.Position.MIDDLE)
            return
        self.crud_confirm.set_text(f"Are you sure you want to delete {self.crud_selected.name}?")
        self.crud_confirm.open()

    def _crud_do_delete(self, event):
        if self.crud_selected is None:
            return
        name = self.crud_selected.name
        self.crud_people = [p for p in self.crud_people if p.id != self.crud_selected.id]
        self._crud_refresh_grid()
        self._crud_clear_form()
        n = Notification.show(f"Deleted: {name}", 3000, Notification.Position.MIDDLE)
        n.add_theme_variants(NotificationVariant.LUMO_SUCCESS)

    def _crud_on_cancel(self, event):
        if self.binder.is_dirty():
            self.crud_cancel_confirm.open()
        else:
            self._crud_clear_form()

    def _crud_clear_form(self):
        self.crud_selected = None
        self.crud_is_new = False
        self.crud_name.set_value("")
        self.crud_email.set_value("")
        self.crud_age.set_value("")
        self.crud_role.set_value("")
        self.crud_city.set_value("")
        self.crud_dept.set_value("")
        self.crud_layout.set_detail(None)
