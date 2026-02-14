"""Test View 22: Binder — /test/binder"""

from datetime import date, time

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, ComboBox, DatePicker, Select, Span, TextField, TimePicker,
    VerticalLayout,
)
from vaadin.flow.data.binder import Binder
from vaadin.flow.data.converter import string_to_int
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


class Person:
    def __init__(self, name="", email="", age=0, birthday=None,
                 start_time=None, country="", city=""):
        self.name = name
        self.email = email
        self.age = age
        self.birthday = birthday
        self.start_time = start_time
        self.country = country
        self.city = city


@Route("test/binder", page_title="Test: Binder", layout=TestMainLayout)
@Menu(title="Binder", order=21)
class TestBinderView(VerticalLayout):
    def __init__(self):
        self._person = Person("Alice", "alice@x.com", 30,
                              date(2000, 1, 15), time(9, 0), "US", "NYC")

        # --- Text Fields ---
        name_tf = TextField("Name")
        name_tf.set_id("name")
        email_tf = TextField("Email")
        email_tf.set_id("email")
        age_tf = TextField("Age")
        age_tf.set_id("age")

        # --- Date/Time/Select/Combo Fields ---
        dp = DatePicker("Birthday")
        dp.set_id("bind-dp")
        tp = TimePicker("Start time")
        tp.set_id("bind-tp")
        sel = Select("Country")
        sel.set_id("bind-sel")
        sel.set_items(["US", "UK", "DE", "FR"])
        cb = ComboBox("City")
        cb.set_id("bind-cb")
        cb.set_items(["NYC", "London", "Berlin", "Paris"])

        # --- Binder ---
        binder = Binder()
        name_binding = binder.for_field(name_tf).as_required(
            "Name is required"
        ).bind(
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
        binder.for_field(dp).bind(
            lambda p: p.birthday, lambda p, v: setattr(p, "birthday", v)
        )
        binder.for_field(tp).bind(
            lambda p: p.start_time, lambda p, v: setattr(p, "start_time", v)
        )
        binder.for_field(sel).bind(
            lambda p: p.country, lambda p, v: setattr(p, "country", v)
        )
        binder.for_field(cb).bind(
            lambda p: p.city, lambda p, v: setattr(p, "city", v)
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
                parts = [
                    person.name, person.email, str(person.age),
                    str(person.birthday) if person.birthday else "",
                    str(person.start_time) if person.start_time else "",
                    person.country, person.city,
                ]
                result.set_text(",".join(parts))
            except Exception:
                result.set_text("validation-error")

        btn_save.add_click_listener(_on_save)

        # --- Clear button (read_bean(None)) ---
        btn_clear = Button("Clear")
        btn_clear.set_id("clear")
        btn_clear.add_click_listener(lambda e: binder.read_bean(None))

        # --- Re-read button (read_bean with different person) ---
        btn_reread = Button("Re-read")
        btn_reread.set_id("reread")
        other_person = Person("Zara", "zara@x.com", 40,
                              date(1995, 6, 20), time(14, 30), "UK", "London")
        btn_reread.add_click_listener(lambda e: binder.read_bean(other_person))

        # --- Remove binding button ---
        btn_remove = Button("Remove name binding")
        btn_remove.set_id("remove-binding")
        btn_remove.add_click_listener(
            lambda e: binder.remove_binding(name_binding)
        )

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
            dp, tp, sel, cb,
            btn_save, btn_clear, btn_reread, btn_remove,
            result, dirty,
            auto_tf, auto_sync,
        )
