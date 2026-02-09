from demo.services.sample_person_service import SamplePerson, sample_person_service
from demo.views.main_layout import MainLayout
from vaadin.flow import Menu, Route
from vaadin.flow.components import (
    Button,
    Checkbox,
    DatePicker,
    Div,
    FormLayout,
    Grid,
    HorizontalLayout,
    LitRenderer,
    Notification,
    NotificationVariant,
    TextField,
)
from vaadin.flow.components.split_layout import SplitLayout
from vaadin.flow.data import Binder, ValidationError


@Route("master-detail", page_title="Master-Detail", layout=MainLayout)
@Menu(title="Master-Detail", order=4, icon="vaadin:split-h")
class MasterDetailView(Div):
    def __init__(self):
        self.add_class_name("master-detail-view")
        self.set_size_full()

        self.sample_person: SamplePerson | None = None

        # Create UI
        split_layout = SplitLayout()
        split_layout.set_size_full()

        self._create_grid_layout(split_layout)
        self._create_editor_layout(split_layout)

        self.add(split_layout)

        # Configure Grid
        self.grid.add_column("firstName", header="First Name").set_auto_width(True)
        self.grid.add_column("lastName", header="Last Name").set_auto_width(True)
        self.grid.add_column("email", header="Email").set_auto_width(True)
        self.grid.add_column("phone", header="Phone").set_auto_width(True)
        self.grid.add_column("dateOfBirth", header="Date Of Birth").set_auto_width(True)
        self.grid.add_column("occupation", header="Occupation").set_auto_width(True)
        self.grid.add_column("role", header="Role").set_auto_width(True)

        important_renderer = LitRenderer.of(
            '<vaadin-icon icon="vaadin:${item.icon}" '
            'style="width: var(--lumo-icon-size-s); height: var(--lumo-icon-size-s); '
            'color: ${item.color};"></vaadin-icon>'
        ).with_property(
            "icon", lambda item: "check" if item.get("important") else "minus"
        ).with_property(
            "color",
            lambda item: "var(--lumo-primary-text-color)"
            if item.get("important")
            else "var(--lumo-disabled-text-color)",
        )
        self.grid.add_column(important_renderer, header="Important").set_auto_width(True)

        self.grid.add_theme_name("no-border")

        # Load data
        self._all_people = [p.to_dict() for p in sample_person_service.find_all()]
        self.grid.set_items(self._all_people)

        # When a row is selected or deselected, populate form
        self.grid.add_selection_listener(self._on_select)

        # Configure Binder
        self.binder = Binder(SamplePerson)
        self.binder.bind_instance_fields(self)

        # Button listeners
        self.cancel.add_click_listener(self._on_cancel)
        self.save.add_click_listener(self._on_save)

    def _on_select(self, event):
        item = event.get("item")
        if item:
            person = sample_person_service.get(item["id"])
            if person:
                self._populate_form(person)
            else:
                Notification.show(
                    f"The requested samplePerson was not found, ID = {item['id']}",
                    3000,
                    Notification.Position.BOTTOM_START,
                )
                self._refresh_grid()
        else:
            self._clear_form()

    def _on_cancel(self, event):
        self._clear_form()
        self._refresh_grid()

    def _on_save(self, event):
        try:
            if self.sample_person is None:
                self.sample_person = SamplePerson(
                    id=0,
                    first_name="",
                    last_name="",
                    email="",
                    phone="",
                    date_of_birth="",
                    occupation="",
                    role="",
                    important=False,
                )
            self.binder.write_bean(self.sample_person)
            sample_person_service.save(self.sample_person)
            self._clear_form()
            self._refresh_grid()
            Notification.show("Data updated")
        except ValidationError:
            Notification.show("Failed to update the data. Check again that all values are valid")

    def _create_editor_layout(self, split_layout: SplitLayout):
        editor_layout_div = Div()
        editor_layout_div.add_class_name("editor-layout")

        editor_div = Div()
        editor_div.add_class_name("editor")
        editor_layout_div.add(editor_div)

        form_layout = FormLayout()
        self.first_name = TextField("First Name")
        self.last_name = TextField("Last Name")
        self.email = TextField("Email")
        self.phone = TextField("Phone")
        self.date_of_birth = TextField("Date Of Birth")
        self.occupation = TextField("Occupation")
        self.role = TextField("Role")
        self.important = Checkbox("Important")
        form_layout.add(
            self.first_name,
            self.last_name,
            self.email,
            self.phone,
            self.date_of_birth,
            self.occupation,
            self.role,
            self.important,
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
        button_layout.add(self.save, self.cancel)
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
        if value:
            self.binder.read_bean(value)
        else:
            self.first_name.set_value("")
            self.last_name.set_value("")
            self.email.set_value("")
            self.phone.set_value("")
            self.date_of_birth.set_value("")
            self.occupation.set_value("")
            self.role.set_value("")
            self.important.set_value(False)
