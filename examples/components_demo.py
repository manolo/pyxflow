"""Demo view showcasing all implemented components."""

import csv
from pathlib import Path

from vaadin.flow import Route
from vaadin.flow.components import (
    Button,
    Checkbox,
    CheckboxGroup,
    Dialog,
    EmailField,
    Grid,
    HorizontalLayout,
    IntegerField,
    Notification,
    NotificationVariant,
    NumberField,
    PasswordField,
    ProgressBar,
    RadioButtonGroup,
    Select,
    Span,
    TextArea,
    TextField,
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
        self.add(Span("=== PyFlow Components Demo ==="))

        # --- Text Input Fields ---
        self.add_section("Text Input Fields")

        text_field = TextField("TextField")
        text_field.set_value("Hello PyFlow!")
        self.add(text_field)

        password_field = PasswordField("PasswordField")
        password_field.set_placeholder("Enter password")
        self.add(password_field)

        email_field = EmailField("EmailField")
        email_field.set_placeholder("name@example.com")
        email_field.set_clear_button_visible(True)
        self.add(email_field)

        text_area = TextArea("TextArea")
        text_area.set_placeholder("Enter multiline text...")
        self.add(text_area)

        # --- Numeric Fields ---
        self.add_section("Numeric Fields")

        number_field = NumberField("NumberField")
        number_field.set_value(3.14)
        number_field.set_min(0)
        number_field.set_max(100)
        self.add(number_field)

        integer_field = IntegerField("IntegerField")
        integer_field.set_value(42)
        integer_field.set_step(5)
        self.add(integer_field)

        # --- Selection Components ---
        self.add_section("Selection Components")

        checkbox = Checkbox("Single Checkbox")
        self.add(checkbox)

        select = Select("Select")
        select.set_items("Option A", "Option B", "Option C")
        select.set_placeholder("Choose an option")
        self.add(select)

        radio_group = RadioButtonGroup("RadioButtonGroup")
        radio_group.set_items("Choice 1", "Choice 2", "Choice 3")
        self.add(radio_group)

        checkbox_group = CheckboxGroup("CheckboxGroup")
        checkbox_group.set_items("Item X", "Item Y", "Item Z")
        self.add(checkbox_group)

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

        # --- Grid ---
        self.add_section("Grid")

        people = self._load_people()
        grid = Grid()
        grid.add_column("name", header="Name").set_auto_width(True)
        grid.add_column("email", header="Email").set_auto_width(True)
        grid.add_column("role", header="Role")
        grid.add_column("city", header="City").set_auto_width(True)
        grid.add_column("department", header="Department")
        grid.set_items(people)
        self.grid_selection_label = Span("Selected: (none)")
        grid.add_selection_listener(self.on_grid_select)
        self.add(grid)
        self.add(self.grid_selection_label)

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
        self.add(Span("Click count: 0"))

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
        self.add(Span(f"--- {title} ---"))

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
        self.add(Span(f"Click count: {self.click_count}"))

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
