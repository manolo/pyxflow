from demo.services.sample_person_service import SamplePerson, sample_person_service
from demo.views.main_layout import MainLayout
from pyflow import Menu, Route
from pyflow.components import *
from pyflow.components.split_layout import SplitLayout
from pyflow.data import Binder, ValidationError


@Route("master-detail", page_title="Master-Detail", layout=MainLayout)
@Menu(title="Master-Detail", order=4, icon="vaadin:split-h")
class MasterDetailView(Div):
    def __init__(self):
        self.add_class_name("master-detail-view")
        self.set_size_full()

        hint = Div()
        hint.add_class_name("demo-hint")
        hint.add(Icon("vaadin:info-circle"), Span(
            "Master-Detail pattern \u2014 select a row in the Grid to edit it "
            "in the side form, powered by Binder with validation."))
        self.add(hint)

        self.sample_person: SamplePerson | None = None

        # Create UI
        split_layout = SplitLayout()
        split_layout.set_size_full()

        self._create_grid_layout(split_layout)
        self._create_editor_layout(split_layout)

        self.add(split_layout)

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

        # Configure Binder with validations
        self.binder = Binder(SamplePerson)
        self.binder.for_field(self.first_name).as_required("First name is required").bind(
            lambda p: p.first_name, lambda p, v: setattr(p, "first_name", v))
        self.binder.for_field(self.last_name).as_required("Last name is required").bind(
            lambda p: p.last_name, lambda p, v: setattr(p, "last_name", v))
        self.binder.for_field(self.email).as_required("Email is required").with_validator(
            lambda v: not v or "@" in v, "Must be a valid email address").bind(
            lambda p: p.email, lambda p, v: setattr(p, "email", v))
        self.binder.for_field(self.phone).bind(
            lambda p: p.phone, lambda p, v: setattr(p, "phone", v))
        self.binder.for_field(self.date_of_birth).bind(
            lambda p: p.date_of_birth, lambda p, v: setattr(p, "date_of_birth", v))
        self.binder.for_field(self.occupation).bind(
            lambda p: p.occupation, lambda p, v: setattr(p, "occupation", v))
        self.binder.for_field(self.role).bind(
            lambda p: p.role, lambda p, v: setattr(p, "role", v))
        self.binder.for_field(self.important).bind(
            lambda p: p.important, lambda p, v: setattr(p, "important", v))

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
                self.sample_person = SamplePerson()
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
        self.email = EmailField("Email")
        self.phone = TextField("Phone")
        self.date_of_birth = DatePicker("Date Of Birth")
        self.occupation = ComboBox("Occupation")
        self.role = ComboBox("Role")
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
        self.binder.read_bean(value)
