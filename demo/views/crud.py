"""CRUD view with URL-driven selection, create, and delete.

Routes:
  /crud            -- Grid only, form cleared
  /crud/new        -- Empty form for new entry
  /crud/:id        -- Select person by id, populate form
  /crud/:id/delete -- Select person + show ConfirmDialog
"""

from demo.services.sample_person_service import SamplePerson, sample_person_service
from demo.views.main_layout import MainLayout
from vaadin.flow import BeforeEnterEvent, Menu, Route
from vaadin.flow.components import *
from vaadin.flow.components.split_layout import SplitLayout
from vaadin.flow.data import Binder, ValidationError


@Route("crud/:id?/:action?", page_title="CRUD", layout=MainLayout)
@Menu(title="CRUD", order=4, icon="vaadin:split-h")
class CrudView(Div):
    def __init__(self):
        self.add_class_name("master-detail-view")
        self.set_size_full()

        hint = Div()
        hint.add_class_name("demo-hint")
        hint.add(Icon("vaadin:info-circle"), Span(
            "CRUD pattern -- select a row to edit, use /crud/new to create, "
            "/crud/:id/delete to delete. All routes are deep-linkable."))
        self.add(hint)

        self.sample_person: SamplePerson | None = None

        # Create UI
        split_layout = SplitLayout()
        split_layout.set_size_full()

        self._create_grid_layout(split_layout)
        self._create_editor_layout(split_layout)

        self.add(split_layout)

        # ConfirmDialog for delete
        self._delete_dialog = ConfirmDialog(
            "Delete", "Are you sure you want to delete this person?", "Delete"
        )
        self._delete_dialog.set_cancelable(True)
        self._delete_dialog.set_confirm_button_theme("error primary")
        self._delete_dialog.add_confirm_listener(self._on_delete_confirm)
        self._delete_dialog.add_cancel_listener(self._on_delete_cancel)
        self.add(self._delete_dialog)

        # Configure Grid
        self.grid.set_columns("firstName", "lastName", "email", "phone", "dateOfBirth", "occupation", "role")
        self.grid.add_column(
            TextRenderer(lambda item: "\u2713" if item.get("important") else "\u2010"),
            header="Important",
        ).set_auto_width(True)

        self.grid.add_theme_name("no-border")

        # Load data
        self._all_people = [p.to_dict() for p in sample_person_service.find_all()]
        self.grid.set_items(self._all_people)

        # Populate ComboBoxes from data
        all_people = sample_person_service.find_all()
        occupations = sorted({p.occupation for p in all_people if p.occupation})
        self.occupation.set_items(*occupations)
        roles = sorted({p.role for p in all_people if p.role})
        self.role.set_items(*roles)

        # When a row is selected or deselected, populate form
        self.grid.add_selection_listener(self._on_select)

        # Configure Binder
        self.binder = Binder(SamplePerson)
        self.binder.bind_instance_fields(self)

        # Button listeners
        self.cancel.add_click_listener(self._on_cancel)
        self.save.add_click_listener(self._on_save)
        self.delete.add_click_listener(self._on_delete_click)

    def before_enter(self, event: BeforeEnterEvent):
        person_id = event.get("id", None)
        action = event.get("action", None)

        if person_id is None:
            # /crud -- clear form
            self._clear_form()
            return

        if person_id == "new":
            # /crud/new -- empty form for new entry
            self.grid.select(None)
            self.sample_person = SamplePerson()
            self.binder.read_bean(self.sample_person)
            self.delete.set_visible(False)
            return

        # /crud/:id or /crud/:id/delete
        try:
            int_id = int(person_id)
        except (ValueError, TypeError):
            Notification.show(f"Invalid person ID: {person_id}", 3000,
                              Notification.Position.BOTTOM_START)
            self._clear_form()
            return

        person = sample_person_service.get(int_id)
        if person is None:
            Notification.show(f"Person not found, ID = {int_id}", 3000,
                              Notification.Position.BOTTOM_START)
            self._clear_form()
            return

        self._populate_form(person)
        # Select the matching row in the grid
        row = next((d for d in self._all_people if d["id"] == int_id), None)
        if row:
            self.grid.select_item(row)

        if action == "delete":
            self._delete_dialog.set_text(
                f"Are you sure you want to delete "
                f"{person.first_name} {person.last_name}?"
            )
            self._delete_dialog.open()

    # -- Grid selection ------------------------------------------------

    def _on_select(self, event):
        item = event.get("item")
        if item:
            person = sample_person_service.get(item["id"])
            if person:
                self._populate_form(person)
                ui = self.get_ui()
                if ui:
                    ui.push_url(f"/crud/{person.id}")
            else:
                Notification.show(
                    f"The requested person was not found, ID = {item['id']}",
                    3000, Notification.Position.BOTTOM_START)
                self._refresh_grid()
        else:
            self._clear_form()
            ui = self.get_ui()
            if ui:
                ui.push_url("/crud")

    # -- Cancel / Save -------------------------------------------------

    def _on_cancel(self, event):
        self._clear_form()
        self._refresh_grid()
        ui = self.get_ui()
        if ui:
            ui.push_url("/crud")

    def _on_save(self, event):
        try:
            if self.sample_person is None:
                self.sample_person = SamplePerson()
            self.binder.write_bean(self.sample_person)
            sample_person_service.save(self.sample_person)
            self._clear_form()
            self._refresh_grid()
            Notification.show("Data updated")
            ui = self.get_ui()
            if ui:
                ui.push_url("/crud")
        except ValidationError:
            Notification.show("Failed to update the data. Check again that all values are valid")

    # -- Delete --------------------------------------------------------

    def _on_delete_click(self, event):
        if self.sample_person and self.sample_person.id:
            ui = self.get_ui()
            if ui:
                ui.push_url(f"/crud/{self.sample_person.id}/delete")
            self._delete_dialog.set_text(
                f"Are you sure you want to delete "
                f"{self.sample_person.first_name} {self.sample_person.last_name}?"
            )
            self._delete_dialog.open()

    def _on_delete_confirm(self, event):
        if self.sample_person and self.sample_person.id:
            sample_person_service.delete(self.sample_person.id)
            Notification.show("Person deleted")
        self._clear_form()
        self._refresh_grid()
        ui = self.get_ui()
        if ui:
            ui.navigate("crud")

    def _on_delete_cancel(self, event):
        ui = self.get_ui()
        if ui and self.sample_person and self.sample_person.id:
            ui.push_url(f"/crud/{self.sample_person.id}")
        elif ui:
            ui.push_url("/crud")

    # -- Layout helpers ------------------------------------------------

    def _create_editor_layout(self, split_layout: SplitLayout):
        editor_layout_div = Div()
        editor_layout_div.add_class_name("editor-layout")

        editor_div = Div()
        editor_div.add_class_name("editor")
        editor_layout_div.add(editor_div)

        form_layout = FormLayout()
        self.first_name = TextField("First Name")
        self.last_name = TextField("Last Name")
        self.email = EmailField("Email")
        self.phone = TextField("Phone")
        self.date_of_birth = DatePicker("Date Of Birth")
        self.occupation = ComboBox("Occupation")
        self.role = ComboBox("Role")
        self.important = Checkbox("Important")
        form_layout.add(
            self.first_name, self.last_name, self.email, self.phone,
            self.date_of_birth, self.occupation, self.role, self.important,
        )

        editor_div.add(form_layout)
        self._create_button_layout(editor_layout_div)

        split_layout.add_to_secondary(editor_layout_div)

    def _create_button_layout(self, editor_layout_div: Div):
        button_layout = HorizontalLayout()
        button_layout.add_class_name("button-layout")
        self.cancel = Button("Cancel")
        self.cancel.add_theme_name("tertiary")
        self.save = Button("Save")
        self.save.add_theme_name("primary")
        self.delete = Button("Delete")
        self.delete.add_theme_name("error tertiary")
        self.delete.set_visible(False)
        button_layout.add(self.save, self.delete, self.cancel)
        editor_layout_div.add(button_layout)

    def _create_grid_layout(self, split_layout: SplitLayout):
        wrapper = Div()
        wrapper.add_class_name("grid-wrapper")
        wrapper.set_size_full()
        self.grid = Grid()
        self.grid.set_size_full()
        wrapper.add(self.grid)
        split_layout.add_to_primary(wrapper)

    def _refresh_grid(self):
        self.grid.select(None)
        self._all_people = [p.to_dict() for p in sample_person_service.find_all()]
        self.grid.set_items(self._all_people)

    def _clear_form(self):
        self._populate_form(None)

    def _populate_form(self, value: SamplePerson | None):
        self.sample_person = value
        self.binder.read_bean(value)
        self.delete.set_visible(value is not None and value.id != 0)
