"""Tests for data binding: Result, ValidationResult, Validators, Converters, Binder."""

import pytest

from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.components.text_field import TextField
from vaadin.flow.components.checkbox import Checkbox
from vaadin.flow.data import (
    Binder,
    Converter,
    Result,
    ValidationError,
    ValidationResult,
    email,
    max_length,
    min_length,
    pattern,
    positive,
    required,
    string_to_float,
    string_to_int,
    value_range,
)


# --- Helpers ---

class Person:
    def __init__(self, name="", age=0, email_addr="", active=True):
        self.name = name
        self.age = age
        self.email_addr = email_addr
        self.active = active


def make_field(label="") -> TextField:
    """Create a TextField attached to a tree so element is available."""
    tree = StateTree()
    field = TextField(label)
    field._attach(tree)
    return field


def make_checkbox(label="") -> Checkbox:
    """Create a Checkbox attached to a tree."""
    tree = StateTree()
    cb = Checkbox(label)
    cb._attach(tree)
    return cb


# --- Result tests ---

class TestResult:
    def test_ok(self):
        r = Result.ok(42)
        assert r.is_ok
        assert not r.is_error
        assert r.value == 42

    def test_error(self):
        r = Result.error("bad")
        assert r.is_error
        assert not r.is_ok
        assert r.message == "bad"

    def test_value_on_error_raises(self):
        r = Result.error("bad")
        with pytest.raises(ValueError):
            _ = r.value

    def test_message_on_ok_raises(self):
        r = Result.ok(1)
        with pytest.raises(ValueError):
            _ = r.message


# --- ValidationResult tests ---

class TestValidationResult:
    def test_ok(self):
        r = ValidationResult.ok()
        assert r.is_ok
        assert not r.is_error

    def test_error(self):
        r = ValidationResult.error("invalid")
        assert r.is_error
        assert r.message == "invalid"

    def test_message_on_ok_raises(self):
        r = ValidationResult.ok()
        with pytest.raises(ValueError):
            _ = r.message


# --- Validator tests ---

class TestValidators:
    def test_required_pass(self):
        v = required()
        assert v("hello").is_ok

    def test_required_fail_empty(self):
        v = required()
        assert v("").is_error

    def test_required_fail_none(self):
        v = required()
        assert v(None).is_error

    def test_required_fail_whitespace(self):
        v = required()
        assert v("   ").is_error

    def test_required_custom_message(self):
        v = required("fill this")
        assert v("").message == "fill this"

    def test_min_length_pass(self):
        v = min_length(3)
        assert v("abc").is_ok

    def test_min_length_fail(self):
        v = min_length(3)
        assert v("ab").is_error

    def test_max_length_pass(self):
        v = max_length(5)
        assert v("hello").is_ok

    def test_max_length_fail(self):
        v = max_length(5)
        assert v("toolong").is_error

    def test_pattern_pass(self):
        v = pattern(r"\d{3}")
        assert v("123").is_ok

    def test_pattern_fail(self):
        v = pattern(r"\d{3}")
        assert v("12a").is_error

    def test_value_range_pass(self):
        v = value_range(1, 10)
        assert v(5).is_ok

    def test_value_range_below(self):
        v = value_range(1, 10)
        assert v(0).is_error

    def test_value_range_above(self):
        v = value_range(1, 10)
        assert v(11).is_error

    def test_value_range_none_ok(self):
        v = value_range(1, 10)
        assert v(None).is_ok

    def test_positive_pass(self):
        v = positive()
        assert v(1).is_ok

    def test_positive_fail(self):
        v = positive()
        assert v(0).is_error

    def test_positive_negative(self):
        v = positive()
        assert v(-1).is_error

    def test_email_pass(self):
        v = email()
        assert v("user@example.com").is_ok

    def test_email_fail(self):
        v = email()
        assert v("not-email").is_error

    def test_email_empty_ok(self):
        v = email()
        assert v("").is_ok


# --- Converter tests ---

class TestConverters:
    def test_string_to_int_valid(self):
        c = string_to_int()
        r = c.to_model("42")
        assert r.is_ok
        assert r.value == 42

    def test_string_to_int_invalid(self):
        c = string_to_int()
        r = c.to_model("abc")
        assert r.is_error

    def test_string_to_int_empty(self):
        c = string_to_int()
        r = c.to_model("")
        assert r.is_ok
        assert r.value == 0

    def test_string_to_int_to_presentation(self):
        c = string_to_int()
        assert c.to_presentation(42) == "42"

    def test_string_to_float_valid(self):
        c = string_to_float()
        r = c.to_model("3.14")
        assert r.is_ok
        assert abs(r.value - 3.14) < 0.001

    def test_string_to_float_invalid(self):
        c = string_to_float()
        r = c.to_model("abc")
        assert r.is_error

    def test_string_to_float_empty(self):
        c = string_to_float()
        r = c.to_model("")
        assert r.is_ok
        assert r.value == 0.0

    def test_custom_converter(self):
        c = Converter(
            to_model=lambda v: Result.ok(v.upper()),
            to_presentation=lambda v: v.lower(),
        )
        assert c.to_model("hello").value == "HELLO"
        assert c.to_presentation("HELLO") == "hello"


# --- Binding tests ---

class TestBinding:
    def test_read_bean(self):
        field = make_field()
        person = Person(name="Alice")
        binder = Binder()
        binder.for_field(field).bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))
        binder.read_bean(person)
        assert field.get_value() == "Alice"

    def test_write_bean(self):
        field = make_field()
        person = Person(name="Alice")
        binder = Binder()
        binder.for_field(field).bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))
        field.set_value("Bob")
        binder.write_bean(person)
        assert person.name == "Bob"

    def test_required_fails(self):
        field = make_field()
        person = Person()
        binder = Binder()
        binder.for_field(field).as_required("Name required").bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v)
        )
        field.set_value("")
        with pytest.raises(ValidationError) as exc_info:
            binder.write_bean(person)
        assert "Name required" in str(exc_info.value)

    def test_with_validator_predicate(self):
        field = make_field()
        person = Person()
        binder = Binder()
        binder.for_field(field).with_validator(
            lambda v: len(v) >= 2, "Min 2 chars"
        ).bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))
        field.set_value("A")
        assert not binder.is_valid()

    def test_with_converter(self):
        field = make_field()
        person = Person(age=25)
        binder = Binder()
        binder.for_field(field).with_converter(string_to_int()).bind(
            lambda p: p.age, lambda p, v: setattr(p, 'age', v)
        )
        # Read should convert int to string
        binder.read_bean(person)
        assert field.get_value() == "25"
        # Write should convert string to int
        field.set_value("30")
        binder.write_bean(person)
        assert person.age == 30

    def test_post_conversion_validator(self):
        field = make_field()
        person = Person()
        binder = Binder()
        binder.for_field(field) \
            .with_converter(string_to_int()) \
            .with_validator(lambda v: v >= 0, "Must be non-negative") \
            .bind(lambda p: p.age, lambda p, v: setattr(p, 'age', v))
        field.set_value("-5")
        assert not binder.is_valid()

    def test_read_only_binding(self):
        field = make_field()
        person = Person(name="Alice")
        binder = Binder()
        binder.for_field(field).bind(lambda p: p.name)  # no setter
        binder.read_bean(person)
        assert field.get_value() == "Alice"
        # Write should succeed (no setter, so it just skips)
        field.set_value("Bob")
        binder.write_bean(person)
        assert person.name == "Alice"  # unchanged

    def test_checkbox_binding(self):
        cb = make_checkbox()
        person = Person(active=False)
        binder = Binder()
        binder.for_field(cb).bind(
            lambda p: p.active, lambda p, v: setattr(p, 'active', v)
        )
        binder.read_bean(person)
        assert cb.get_value() is False
        cb.set_value(True)
        binder.write_bean(person)
        assert person.active is True


# --- Binder tests ---

class TestBinder:
    def test_multiple_bindings(self):
        name_field = make_field()
        email_field = make_field()
        person = Person(name="Alice", email_addr="alice@test.com")
        binder = Binder()
        binder.for_field(name_field).bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v)
        )
        binder.for_field(email_field).bind(
            lambda p: p.email_addr, lambda p, v: setattr(p, 'email_addr', v)
        )
        binder.read_bean(person)
        assert name_field.get_value() == "Alice"
        assert email_field.get_value() == "alice@test.com"

    def test_is_valid(self):
        field = make_field()
        binder = Binder()
        binder.for_field(field).as_required().bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v)
        )
        field.set_value("ok")
        assert binder.is_valid()
        field.set_value("")
        assert not binder.is_valid()

    def test_write_bean_if_valid_success(self):
        field = make_field()
        person = Person()
        binder = Binder()
        binder.for_field(field).bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v)
        )
        field.set_value("Alice")
        assert binder.write_bean_if_valid(person) is True
        assert person.name == "Alice"

    def test_write_bean_if_valid_failure(self):
        field = make_field()
        person = Person()
        binder = Binder()
        binder.for_field(field).as_required().bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v)
        )
        field.set_value("")
        assert binder.write_bean_if_valid(person) is False
        assert person.name == ""  # unchanged

    def test_set_bean_populates_fields(self):
        field = make_field()
        binder = Binder()
        binder.for_field(field).bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v)
        )
        person = Person(name="Alice")
        binder.set_bean(person)
        assert field.get_value() == "Alice"

    def test_set_bean_auto_writes(self):
        field = make_field()
        binder = Binder()
        binder.for_field(field).bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v)
        )
        person = Person(name="Alice")
        binder.set_bean(person)
        # Simulate value change via _handle_change (as client would)
        field._handle_change({"value": "Bob"})
        assert person.name == "Bob"

    def test_bean_level_validator(self):
        name_field = make_field()
        email_field = make_field()
        person = Person()
        binder = Binder()
        binder.for_field(name_field).bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v)
        )
        binder.for_field(email_field).bind(
            lambda p: p.email_addr, lambda p, v: setattr(p, 'email_addr', v)
        )
        # Cross-field: if name is "admin", email must end with @admin.com
        binder.with_validator(
            lambda bean, b: bean.name != "admin" or bean.email_addr.endswith("@admin.com"),
            "Admin must use admin email"
        )
        name_field.set_value("admin")
        email_field.set_value("user@test.com")
        # Bean-level validators run with the bean's current state,
        # but write_bean writes fields first, then validates bean-level.
        # We need to write_bean which first validates bindings, then bean.
        with pytest.raises(ValidationError, match="Admin must use admin email"):
            binder.write_bean(person)

    def test_field_invalid_on_validation_failure(self):
        field = make_field()
        binder = Binder()
        binder.for_field(field).as_required("Required!").bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v)
        )
        field.set_value("")
        binder.validate()
        # Field should have invalid=True and errorMessage set
        assert field.element.get_property("invalid") is True
        assert field.element.get_property("errorMessage") == "Required!"

    def test_field_cleared_on_validation_success(self):
        field = make_field()
        binder = Binder()
        binder.for_field(field).as_required("Required!").bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v)
        )
        # First fail
        field.set_value("")
        binder.validate()
        assert field.element.get_property("invalid") is True
        # Then succeed
        field.set_value("ok")
        binder.validate()
        assert field.element.get_property("invalid") is False
        assert field.element.get_property("errorMessage") == ""

    def test_status_listener(self):
        field = make_field()
        binder = Binder()
        binder.for_field(field).bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v)
        )
        notifications = []
        binder.add_status_change_listener(lambda: notifications.append(True))
        # Simulate field change
        field._handle_change({"value": "test"})
        assert len(notifications) == 1

    def test_write_bean_raises_validation_error(self):
        field = make_field()
        person = Person()
        binder = Binder()
        binder.for_field(field).as_required("Name needed").bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v)
        )
        field.set_value("")
        with pytest.raises(ValidationError) as exc_info:
            binder.write_bean(person)
        assert len(exc_info.value.results) == 1
        assert exc_info.value.results[0].message == "Name needed"

    def test_converter_error_sets_field_invalid(self):
        field = make_field()
        person = Person()
        binder = Binder()
        binder.for_field(field).with_converter(
            string_to_int("Not a number")
        ).bind(lambda p: p.age, lambda p, v: setattr(p, 'age', v))
        field.set_value("abc")
        binder.validate()
        assert field.element.get_property("invalid") is True
        assert field.element.get_property("errorMessage") == "Not a number"
