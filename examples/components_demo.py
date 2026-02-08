"""Demo view showcasing all implemented components."""

import csv
import datetime
from pathlib import Path

from vaadin.flow import Route
from vaadin.flow.components import (
    Button,
    Checkbox,
    CheckboxGroup,
    ComboBox,
    ComponentRenderer,
    ConfirmDialog,
    DatePicker,
    Dialog,
    EmailField,
    FormLayout,
    Grid,
    H2,
    H3,
    HorizontalLayout,
    IntegerField,
    LitRenderer,
    MenuBar,
    Notification,
    NotificationVariant,
    NumberField,
    PasswordField,
    ProgressBar,
    RadioButtonGroup,
    RouterLink,
    Select,
    Span,
    Tab,
    Tabs,
    TabSheet,
    TextArea,
    TextField,
    TimePicker,
    Upload,
    VerticalLayout,
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
    """Data model for the CRUD demo section."""

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



@Route("components", page_title="Components Demo")
class ComponentsDemoView(VerticalLayout):
    """View containing ALL components supported by PyFlow.
    Must match the Java AllComponentsView in structure and content."""

    def __init__(self):
        super().__init__()

        self.click_count = 0

        # Header
        self.add(H2("PyFlow Components Demo"))

        # --- Text Input Fields ---
        self.add_section("Text Input Fields")

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

        text_area = TextArea("TextArea")
        text_area.set_placeholder("Enter multiline text...")
        text_form.add(text_area)

        self.add(text_form)

        # --- Numeric Fields ---
        self.add_section("Numeric Fields")

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

        self.add(numeric_form)

        # --- Date & Time ---
        self.add_section("Date & Time")

        date_time_form = FormLayout()

        date_picker = DatePicker("DatePicker")
        date_picker.set_value(datetime.date.today())
        date_time_form.add(date_picker)

        time_picker = TimePicker("TimePicker")
        time_picker.set_step(1800)
        time_picker.set_value(datetime.time(12, 0))
        date_time_form.add(time_picker)

        self.add(date_time_form)

        # --- Selection Components ---
        self.add_section("Selection Components")

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

        radio_group = RadioButtonGroup("RadioButtonGroup")
        radio_group.set_items("Choice 1", "Choice 2", "Choice 3")
        selection_form.add(radio_group)

        checkbox_group = CheckboxGroup("CheckboxGroup")
        checkbox_group.set_items("Item X", "Item Y", "Item Z")
        selection_form.add(checkbox_group)

        self.add(selection_form)

        # --- Progress ---
        self.add_section("Progress")

        progress_bar = ProgressBar()
        progress_bar.set_value(0.6)
        self.add(Span("ProgressBar (60%):"))
        self.add(progress_bar)

        progress_indeterminate = ProgressBar()
        progress_indeterminate.set_indeterminate(True)
        self.add(Span("ProgressBar (indeterminate):"))
        self.add(progress_indeterminate)

        # --- Tabs ---
        self.add_section("Tabs")

        tab1 = Tab("Tab 1")
        tab2 = Tab("Tab 2")
        tab3 = Tab("Tab 3")
        tabs = Tabs(tab1, tab2, tab3)
        self.tabs_label = Span("Selected tab: Tab 1")
        tabs.add_selected_change_listener(self.on_tab_selected)
        self.tabs = tabs
        self.tab_list = [tab1, tab2, tab3]
        self.add(tabs)
        self.add(self.tabs_label)

        # --- TabSheet ---
        self.add_section("TabSheet")

        tab_sheet = TabSheet()
        tab_sheet.add("Dashboard", Span("Dashboard content"))
        tab_sheet.add("Settings", Span("Settings content"))
        self.add(tab_sheet)

        # --- MenuBar ---
        self.add_section("MenuBar")

        menu_bar = MenuBar()
        file_item = menu_bar.add_item("File")
        file_item.get_sub_menu().add_item("New", lambda e: self.on_menu_click("New"))
        file_item.get_sub_menu().add_item("Open", lambda e: self.on_menu_click("Open"))
        edit_item = menu_bar.add_item("Edit")
        edit_item.get_sub_menu().add_item("Undo", lambda e: self.on_menu_click("Undo"))
        menu_bar.add_item("Help", lambda e: self.on_menu_click("Help"))
        self.menu_label = Span("Menu action: (none)")
        self.add(menu_bar)
        self.add(self.menu_label)

        # --- Upload ---
        self.add_section("Upload")

        upload = Upload()
        self.upload_label = Span("Upload status: (none)")
        upload.set_receiver(self.on_upload_received)
        upload.add_succeeded_listener(self.on_upload_succeeded)
        self.add(upload)
        self.add(self.upload_label)

        # --- Navigation ---
        self.add_section("Navigation")

        self.add(RouterLink("Go to Hello World", "/"))
        self.add(RouterLink("Go to About", "/about"))
        self.add(RouterLink("Go to Greet", "/greet/World"))

        # --- Component Features ---
        self.add_section("Component Features")

        features_form = FormLayout()

        helper_field = TextField("With Helper Text")
        helper_field.set_helper_text("This is a helper text")
        helper_field.set_id("helper-text-field")
        helper_field.add_click_shortcut(Key.ENTER)
        helper_field.add_click_listener(lambda e: self.on_shortcut("With Helper Text"))
        features_form.add(helper_field)

        tooltip_field = TextField("With Tooltip")
        tooltip_field.set_tooltip_text("Hover to see this tooltip")
        tooltip_field.add_click_shortcut(Key.ENTER)
        tooltip_field.add_click_listener(lambda e: self.on_shortcut("With Tooltip"))
        features_form.add(tooltip_field)

        self.add(features_form)

        shortcut_label = Span("Shortcut: (none)")
        self.shortcut_label = shortcut_label
        shortcut_btn = Button("Press Enter (shortcut)")
        shortcut_btn.add_click_listener(lambda e: self.on_shortcut("Button"))
        shortcut_btn.add_click_shortcut(Key.ENTER)
        self.add(HorizontalLayout(shortcut_btn, shortcut_label))

        # --- Buttons & Actions ---
        self.add_section("Buttons & Actions")

        button = Button("Click Me!")
        button.add_click_listener(self.on_button_click)

        dialog_btn = Button("Open Dialog")
        dialog_btn.add_click_listener(self.open_dialog)

        notification_btn = Button("Show Notification")
        notification_btn.add_click_listener(self.show_notification)

        success_btn = Button("Success Notification")
        success_btn.add_click_listener(self.show_success)

        error_btn = Button("Error Notification")
        error_btn.add_click_listener(self.show_error)

        button_row = HorizontalLayout()
        button_row.add(button, dialog_btn, notification_btn, success_btn, error_btn)
        self.add(button_row)
        self.click_label = Span("Click count: 0")
        self.add(self.click_label)

        # Dialog (hidden initially)
        self.dialog = Dialog()
        self.dialog.set_header_title("Sample Dialog")
        self.dialog.add(Span("This is a dialog with some content."))
        self.dialog.add(Span("You can close it by clicking outside."))
        self.add(self.dialog)

        # --- Shared data for all grids ---
        people = self._load_people()

        # --- CRUD Master-Detail ---
        self.add_section("CRUD Master-Detail (Binder)")

        self.crud_people = [CrudPerson.from_dict(p) for p in people]
        crud_roles = sorted({p["role"] for p in people})
        crud_departments = sorted({p["department"] for p in people})
        self.crud_selected: CrudPerson | None = None
        self.crud_is_new = False

        crud_layout = HorizontalLayout()
        crud_layout.set_width_full()

        # Master: Grid
        self.crud_master = VerticalLayout()

        self.crud_grid = Grid()
        self.crud_grid.add_column("name", header="Name").set_auto_width(True)
        self.crud_grid.add_column("email", header="Email").set_auto_width(True)
        self.crud_grid.add_column("age", header="Age")
        self.crud_grid.add_column("role", header="Role")
        self.crud_grid.add_column("city", header="City").set_auto_width(True)
        self.crud_grid.add_column("department", header="Department")
        self.crud_grid.add_selection_listener(self._crud_on_select)
        self._crud_refresh_grid()

        crud_new_btn = Button("+ New Person")
        crud_new_btn.add_theme_name("primary")
        crud_new_btn.add_click_listener(self._crud_on_new)

        self.crud_master.add(self.crud_grid, crud_new_btn)

        # Detail: Form (hidden until selection or new)
        self.crud_detail = VerticalLayout()
        self.crud_detail.set_width("40%")
        self.crud_detail.set_visible(False)

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

        # ConfirmDialog for delete
        self.crud_confirm = ConfirmDialog()
        self.crud_confirm.set_header("Confirm Delete")
        self.crud_confirm.set_text("Are you sure you want to delete this person?")
        self.crud_confirm.set_confirm_text("Delete")
        self.crud_confirm.set_confirm_button_theme("error primary")
        self.crud_confirm.set_cancelable(True)
        self.crud_confirm.add_confirm_listener(self._crud_do_delete)
        self.add(self.crud_confirm)

        # ConfirmDialog for cancel with unsaved changes
        self.crud_cancel_confirm = ConfirmDialog()
        self.crud_cancel_confirm.set_header("Unsaved changes")
        self.crud_cancel_confirm.set_text("You have unsaved changes. Discard them?")
        self.crud_cancel_confirm.set_confirm_text("Discard")
        self.crud_cancel_confirm.set_confirm_button_theme("error primary")
        self.crud_cancel_confirm.set_cancelable(True)
        self.crud_cancel_confirm.add_confirm_listener(lambda e: self._crud_clear_form())
        self.add(self.crud_cancel_confirm)

        crud_layout.expand(self.crud_master)
        crud_layout.add(self.crud_master, self.crud_detail)
        self.add(crud_layout)

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

        # --- Grid ---
        self.add_section("Grid")

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
        self.add(grid)
        self.add(self.grid_selection_label)

        # --- Grid with LitRenderer ---
        self.add_section("Grid with LitRenderer")

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
        self.add(lit_grid)
        self.add(self.lit_renderer_label)

        # --- Grid with ComponentRenderer ---
        self.add_section("Grid with ComponentRenderer")

        comp_grid = Grid()
        comp_grid.add_column("name", header="Name").set_auto_width(True)
        comp_grid.add_column("email", header="Email").set_auto_width(True)
        self.comp_renderer_label = Span("ComponentRenderer action: (none)")
        comp_grid.add_column(
            ComponentRenderer(self.create_action_buttons),
            header="Actions",
        )
        comp_grid.set_items(people)
        self.add(comp_grid)
        self.add(self.comp_renderer_label)

        # --- Grid with ListDataProvider ---
        self.add_section("Grid with ListDataProvider")

        dp_items = [
            {"name": p["name"], "city": p["city"], "department": p["department"]}
            for p in people
        ]
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
        self.add(dp_controls)
        self.add(dp_grid)

        # --- Grid with Lazy DataProvider ---
        self.add_section("Grid with Lazy DataProvider")

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
        self.add(self._lazy_stats_label)
        self.add(lazy_grid)

    @staticmethod
    def _load_people() -> list[dict]:
        """Load people data from CSV."""
        csv_path = Path(__file__).parent / "people.csv"
        with open(csv_path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def add_section(self, title: str):
        """Add a section header."""
        self.add(H3(title))

    def on_grid_select(self, event):
        """Handle grid selection."""
        item = event.get("item")
        if item:
            self.grid_selection_label.set_text(f"Selected: {item['name']}")
        else:
            self.grid_selection_label.set_text("Selected: (none)")

    def on_button_click(self, event):
        """Handle button click."""
        self.click_count += 1
        self.click_label.set_text(f"Click count: {self.click_count}")

    def open_dialog(self, event):
        """Open the dialog."""
        self.dialog.open()

    def show_notification(self, event):
        """Show a basic notification."""
        Notification.show("This is a notification!", 3000, Notification.Position.BOTTOM_CENTER)

    def show_success(self, event):
        """Show a success notification."""
        n = Notification.show("Operation successful!", 3000, Notification.Position.TOP_CENTER)
        n.add_theme_variants(NotificationVariant.LUMO_SUCCESS)

    def show_error(self, event):
        """Show an error notification."""
        n = Notification.show("Something went wrong!", 5000, Notification.Position.MIDDLE)
        n.add_theme_variants(NotificationVariant.LUMO_ERROR)

    def on_lit_edit(self, item):
        """Handle LitRenderer edit button click."""
        self.lit_renderer_label.set_text(f"LitRenderer action: Edit {item['name']}")

    def create_action_buttons(self, item):
        """Create action buttons for ComponentRenderer."""
        btn = Button(f"View {item['name']}")
        btn.add_click_listener(lambda e, i=item: self.on_comp_view(i))
        return btn

    def on_comp_view(self, item):
        """Handle ComponentRenderer view button click."""
        self.comp_renderer_label.set_text(f"ComponentRenderer action: View {item['name']}")

    def on_tab_selected(self, event_data):
        """Handle tab selection."""
        idx = event_data.get("selectedIndex", 0)
        if 0 <= idx < len(self.tab_list):
            self.tabs_label.set_text(f"Selected tab: {self.tab_list[idx].get_label()}")

    def on_menu_click(self, name):
        """Handle menu item click."""
        self.menu_label.set_text(f"Menu action: {name}")

    def on_upload_received(self, filename, mime_type, data):
        """Handle file upload."""
        self.upload_label.set_text(f"Uploaded: {filename} ({len(data)} bytes)")

    def on_upload_succeeded(self, event_data):
        """Handle upload success event."""
        pass

    def on_shortcut(self, source):
        """Handle shortcut from any component."""
        self.shortcut_label.set_text(f"Shortcut: {source}")

    # --- DataProvider methods ---

    def _dp_update_label(self):
        """Update the filter field label with current item count."""
        self.dp_filter.set_label(f"Filter by name (Items: {self.dp.size(Query())})")

    def _dp_on_filter(self, event):
        """Filter DataProvider by name."""
        text = self.dp_filter.get_value().lower()
        if text:
            self.dp.set_filter(lambda item, t=text: t in item["name"].lower())
        else:
            self.dp.set_filter(None)
        self._dp_update_label()

    def _dp_on_add(self, event):
        """Add a person to the DataProvider."""
        self.dp_add_counter += 1
        self.dp.add_item({
            "name": f"New Person {self.dp_add_counter}",
            "city": "Unknown",
            "department": "Unassigned",
        })
        self._dp_update_label()

    def _dp_on_remove(self, event):
        """Remove the last person from the DataProvider."""
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
                self.crud_detail.set_visible(True)
        else:
            self._crud_clear_form()

    def _crud_on_new(self, event):
        self.crud_selected = CrudPerson()
        self.crud_is_new = True
        self.binder.read_bean(self.crud_selected)
        self.crud_detail.set_visible(True)

    def _crud_on_save(self, event):
        if self.crud_selected is None:
            Notification.show("Select a person or click New first", 3000)
            return
        if not self.binder.is_dirty():
            Notification.show("No changes to save", 3000)
            return
        try:
            self.binder.write_bean(self.crud_selected)
        except ValidationError:
            n = Notification.show("Please fix the errors in the form", 3000)
            n.add_theme_variants(NotificationVariant.LUMO_ERROR)
            return
        if self.crud_is_new:
            self.crud_people.append(self.crud_selected)
            self.crud_is_new = False
        self._crud_refresh_grid()
        self.binder.read_bean(self.crud_selected)
        n = Notification.show(f"Saved: {self.crud_selected.name}", 3000)
        n.add_theme_variants(NotificationVariant.LUMO_SUCCESS)

    def _crud_on_delete(self, event):
        if self.crud_selected is None or self.crud_is_new:
            Notification.show("Select a person to delete", 3000)
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
        n = Notification.show(f"Deleted: {name}", 3000)
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
        self.crud_detail.set_visible(False)
