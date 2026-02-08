"""Tests for Binder dirty tracking (is_dirty / _take_snapshot)."""

import pytest

from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.components.text_field import TextField
from vaadin.flow.data import Binder, string_to_int


# --- Helpers ---

class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


def make_field(label="") -> TextField:
    """Create a TextField attached to a tree so element is available."""
    tree = StateTree()
    field = TextField(label)
    field._attach(tree)
    return field


# --- Tests ---

class TestBinderDirty:
    """Test Binder.is_dirty() and snapshot mechanism."""

    def test_not_dirty_after_read_bean(self):
        """is_dirty() returns False immediately after read_bean."""
        name_field = make_field("Name")
        binder = Binder(Person)
        binder.for_field(name_field).bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))

        person = Person(name="Alice")
        binder.read_bean(person)

        assert binder.is_dirty() is False

    def test_dirty_after_field_change(self):
        """is_dirty() returns True after changing a field value."""
        name_field = make_field("Name")
        binder = Binder(Person)
        binder.for_field(name_field).bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))

        person = Person(name="Alice")
        binder.read_bean(person)

        name_field.set_value("Bob")
        assert binder.is_dirty() is True

    def test_not_dirty_after_restoring_value(self):
        """is_dirty() returns False if field is changed back to original."""
        name_field = make_field("Name")
        binder = Binder(Person)
        binder.for_field(name_field).bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))

        person = Person(name="Alice")
        binder.read_bean(person)

        name_field.set_value("Bob")
        assert binder.is_dirty() is True

        name_field.set_value("Alice")
        assert binder.is_dirty() is False

    def test_not_dirty_no_snapshot(self):
        """is_dirty() returns False when no bean has been read."""
        name_field = make_field("Name")
        binder = Binder(Person)
        binder.for_field(name_field).bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))

        assert binder.is_dirty() is False

    def test_not_dirty_after_set_bean_none(self):
        """is_dirty() returns False after set_bean(None) clears snapshot."""
        name_field = make_field("Name")
        binder = Binder(Person)
        binder.for_field(name_field).bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))

        person = Person(name="Alice")
        binder.set_bean(person)
        name_field.set_value("Bob")
        assert binder.is_dirty() is True

        binder.set_bean(None)
        assert binder.is_dirty() is False

    def test_not_dirty_after_re_read_bean(self):
        """is_dirty() returns False after re-reading the same bean."""
        name_field = make_field("Name")
        binder = Binder(Person)
        binder.for_field(name_field).bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))

        person = Person(name="Alice")
        binder.read_bean(person)
        name_field.set_value("Bob")
        assert binder.is_dirty() is True

        binder.read_bean(person)
        assert binder.is_dirty() is False

    def test_dirty_with_multiple_fields(self):
        """is_dirty() detects change in any of multiple fields."""
        name_field = make_field("Name")
        age_field = make_field("Age")
        binder = Binder(Person)
        binder.for_field(name_field).bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))
        binder.for_field(age_field).with_converter(
            string_to_int("Must be a number")
        ).bind(lambda p: p.age, lambda p, v: setattr(p, 'age', v))

        person = Person(name="Alice", age=30)
        binder.read_bean(person)
        assert binder.is_dirty() is False

        # Change only age field
        age_field.set_value("31")
        assert binder.is_dirty() is True

    def test_dirty_with_converter_snapshot_stores_presentation(self):
        """Snapshot stores presentation values, so converter doesn't affect comparison."""
        age_field = make_field("Age")
        binder = Binder(Person)
        binder.for_field(age_field).with_converter(
            string_to_int("Must be a number")
        ).bind(lambda p: p.age, lambda p, v: setattr(p, 'age', v))

        person = Person(age=25)
        binder.read_bean(person)
        # Presentation value should be "25" (string)
        assert age_field.get_value() == "25"
        assert binder.is_dirty() is False

        age_field.set_value("26")
        assert binder.is_dirty() is True

        age_field.set_value("25")
        assert binder.is_dirty() is False

    def test_set_bean_takes_snapshot(self):
        """set_bean() calls read_bean() which takes snapshot."""
        name_field = make_field("Name")
        binder = Binder(Person)
        binder.for_field(name_field).bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))

        person = Person(name="Alice")
        binder.set_bean(person)
        assert binder.is_dirty() is False

        name_field.set_value("Bob")
        assert binder.is_dirty() is True

    def test_not_dirty_same_value_different_bean(self):
        """is_dirty() returns False when reading a new bean with same values."""
        name_field = make_field("Name")
        binder = Binder(Person)
        binder.for_field(name_field).bind(lambda p: p.name, lambda p, v: setattr(p, 'name', v))

        person1 = Person(name="Alice")
        binder.read_bean(person1)

        person2 = Person(name="Alice")
        binder.read_bean(person2)

        assert binder.is_dirty() is False
