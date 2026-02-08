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
    VerticalLayout,
)


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

        # --- Grid ---
        self.add_section("Grid")

        people = self._load_people()
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

        # --- Navigation ---
        self.add_section("Navigation")

        self.add(RouterLink("Go to Hello World", "/"))
        self.add(RouterLink("Go to About", "/about"))
        self.add(RouterLink("Go to Greet", "/greet/World"))

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
