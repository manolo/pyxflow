"""Test View 22: Binder — /test/binder"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, IntegerField, Span, TextField, VerticalLayout,
)
from vaadin.flow.data.binder import Binder
from vaadin.flow.data.converter import string_to_int
from vaadin.flow.menu import Menu
from demo.views.test_main_layout import TestMainLayout


class Person:
    def __init__(self, name="", email="", age=0):
        self.name = name
        self.email = email
        self.age = age


@Route("test/binder", page_title="Test: Binder", layout=TestMainLayout)
@Menu(title="Binder", order=21)
class TestBinderView(VerticalLayout):
    def __init__(self):
        self._person = Person("Alice", "alice@x.com", 30)

        # --- Fields ---
        name_tf = TextField("Name")
        name_tf.set_id("name")
        email_tf = TextField("Email")
        email_tf.set_id("email")
        age_tf = TextField("Age")
        age_tf.set_id("age")

        # --- Binder ---
        binder = Binder()
        binder.for_field(name_tf).as_required("Name is required").bind(
            lambda p: p.name, lambda p, v: setattr(p, "name", v)
        )
        binder.for_field(email_tf).with_validator(
            lambda v: "@" in v if v else False, "Invalid email"
        ).bind(
            lambda p: p.email, lambda p, v: setattr(p, "email", v)
        )
        binder.for_field(age_tf).with_converter(
            string_to_int("Not a number")
        ).with_validator(
            lambda v: 0 < v < 150, "Invalid age"
        ).bind(
            lambda p: p.age, lambda p, v: setattr(p, "age", v)
        )

        binder.read_bean(self._person)

        # --- Result ---
        result = Span("")
        result.set_id("binder-result")

        btn_save = Button("Save")
        btn_save.set_id("save")

        def _on_save(e):
            person = Person()
            try:
                binder.write_bean(person)
                result.set_text(f"{person.name},{person.email},{person.age}")
            except Exception:
                result.set_text("validation-error")

        btn_save.add_click_listener(_on_save)

        # --- Dirty tracking ---
        dirty = Span("false")
        dirty.set_id("dirty")
        name_tf.add_value_change_listener(
            lambda e: dirty.set_text(str(binder.is_dirty()).lower())
        )

        # --- set_bean (auto sync) ---
        auto_person = Person("Auto", "auto@x.com", 25)
        auto_tf = TextField("Auto name")
        auto_tf.set_id("auto-name")
        auto_sync = Span("")
        auto_sync.set_id("auto-sync")

        auto_binder = Binder()
        auto_binder.for_field(auto_tf).bind(
            lambda p: p.name, lambda p, v: setattr(p, "name", v)
        )
        auto_binder.set_bean(auto_person)
        auto_tf.add_value_change_listener(
            lambda e: auto_sync.set_text(auto_person.name)
        )

        self.add(
            name_tf, email_tf, age_tf,
            btn_save, result,
            dirty,
            auto_tf, auto_sync,
        )
