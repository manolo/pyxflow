"""Tests for Binder dirty tracking (is_dirty / _take_snapshot)."""

import pytest

from pyxflow.core.state_tree import StateTree
from pyxflow.components.text_field import TextField
from pyxflow.components.email_field import EmailField
from pyxflow.components.select import Select
from pyxflow.data import Binder, string_to_int


# --- Helpers ---

class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


class CrudPerson:
    """Mimics the CRUD demo person with all field types."""
    def __init__(self, name="", email="", age=0, role="", city="", department=""):
        self.name = name
        self.email = email
        self.age = age
        self.role = role
        self.city = city
        self.department = department


def make_field(label="") -> TextField:
    """Create a TextField attached to a tree so element is available."""
    tree = StateTree()
    field = TextField(label)
    field._attach(tree)
    return field


def make_select(label="", items=None) -> Select:
    """Create a Select attached to a tree so element is available."""
    tree = StateTree()
    field = Select(label)
    if items:
        field.set_items(*items)
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


class TestBinderDirtyWithSelect:
    """Regression tests for dirty tracking with Select fields.

    Reproduces the CRUD master-detail scenario: read_bean → is_dirty
    must return False when no user edits occurred, even after mSync.
    """

    def test_not_dirty_after_read_bean_with_select(self):
        """Select field: is_dirty() returns False after read_bean."""
        roles = ["Admin", "Developer", "Designer", "User"]
        role_field = make_select("Role", roles)
        binder = Binder(CrudPerson)
        binder.for_field(role_field).bind(
            lambda p: p.role, lambda p, v: setattr(p, 'role', v))

        person = CrudPerson(role="Developer")
        binder.read_bean(person)

        assert role_field.get_value() == "Developer"
        assert binder.is_dirty() is False

    def test_not_dirty_after_select_sync_property_same_value(self):
        """mSync with same value must not cause false dirty.

        When the client sends mSync for the Select's value (e.g. after
        the form renders), _sync_property resolves the label back to
        the item.  If the item matches, is_dirty() must stay False.
        """
        roles = ["Admin", "Developer", "Designer", "User"]
        role_field = make_select("Role", roles)
        binder = Binder(CrudPerson)
        binder.for_field(role_field).bind(
            lambda p: p.role, lambda p, v: setattr(p, 'role', v))

        person = CrudPerson(role="Developer")
        binder.read_bean(person)

        # Simulate mSync from client with same value
        role_field._sync_property("value", "Developer")

        assert role_field.get_value() == "Developer"
        assert binder.is_dirty() is False

    def test_dirty_after_select_sync_property_different_value(self):
        """mSync with a different value must cause dirty."""
        roles = ["Admin", "Developer", "Designer", "User"]
        role_field = make_select("Role", roles)
        binder = Binder(CrudPerson)
        binder.for_field(role_field).bind(
            lambda p: p.role, lambda p, v: setattr(p, 'role', v))

        person = CrudPerson(role="Developer")
        binder.read_bean(person)

        # User changes role on client
        role_field._sync_property("value", "Admin")

        assert role_field.get_value() == "Admin"
        assert binder.is_dirty() is True

    def test_not_dirty_after_select_sync_empty_resolves_to_none(self):
        """mSync with empty string resolves to None.

        If the client sends value="" (e.g. selectConnector reset), and
        the original value was also None/empty, is_dirty must be False.
        """
        roles = ["Admin", "Developer", "Designer", "User"]
        role_field = make_select("Role", roles)
        binder = Binder(CrudPerson)
        binder.for_field(role_field).bind(
            lambda p: p.role, lambda p, v: setattr(p, 'role', v))

        # read_bean(None) clears fields
        binder.read_bean(None)
        # After clear, Select._value = "" (from Binding.clear)
        assert role_field.get_value() == ""
        snapshot_value = binder._snapshot[0]

        # mSync sends empty string — _sync_property sets _value = None
        role_field._sync_property("value", "")
        current = role_field.get_value()

        # Either both are "" or both are None — must not be dirty
        # This is the critical assertion: if _sync_property("value", "")
        # changes _value from "" to None, it would cause a false dirty.
        if current != snapshot_value:
            pytest.fail(
                f"mSync empty string changed value: "
                f"snapshot={snapshot_value!r} current={current!r} — "
                f"this would cause false dirty detection in CRUD cancel"
            )
        assert binder.is_dirty() is False

    def test_crud_full_cycle_select_and_textfield(self):
        """Full CRUD cycle: read_bean → is_dirty with mixed field types.

        Mimics: click person in grid → form shows → click Cancel.
        """
        tree = StateTree()
        roles = ["Admin", "Developer", "Designer", "User"]
        depts = ["Engineering", "HR", "Marketing", "Support"]

        name_field = TextField("Name")
        name_field._attach(tree)
        email_field = EmailField("Email")
        email_field._attach(tree)
        age_field = TextField("Age")
        age_field._attach(tree)
        role_field = Select("Role")
        role_field.set_items(*roles)
        role_field._attach(tree)
        city_field = TextField("City")
        city_field._attach(tree)
        dept_field = Select("Department")
        dept_field.set_items(*depts)
        dept_field._attach(tree)

        binder = Binder(CrudPerson)
        binder.for_field(name_field).bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v))
        binder.for_field(email_field).bind(
            lambda p: p.email, lambda p, v: setattr(p, 'email', v))
        binder.for_field(age_field).with_converter(
            string_to_int("Must be a number")
        ).bind(lambda p: p.age, lambda p, v: setattr(p, 'age', v))
        binder.for_field(role_field).bind(
            lambda p: p.role, lambda p, v: setattr(p, 'role', v))
        binder.for_field(city_field).bind(
            lambda p: p.city, lambda p, v: setattr(p, 'city', v))
        binder.for_field(dept_field).bind(
            lambda p: p.department, lambda p, v: setattr(p, 'department', v))

        # Step 1: click person → read_bean
        person = CrudPerson(
            name="Hugo Santos", email="hugo@company.com", age=33,
            role="Developer", city="Oslo", department="HR")
        binder.read_bean(person)

        # Step 2: no edits — immediately check dirty
        assert binder.is_dirty() is False

        # Step 3: simulate mSync for all fields (as if client echoed values back)
        name_field._sync_property("value", "Hugo Santos")
        email_field._sync_property("value", "hugo@company.com")
        age_field._sync_property("value", "33")
        role_field._sync_property("value", "Developer")
        city_field._sync_property("value", "Oslo")
        dept_field._sync_property("value", "HR")

        # Step 4: is_dirty must still be False — Cancel should NOT show dialog
        assert binder.is_dirty() is False

    def test_crud_cycle_read_clear_read(self):
        """Full cycle: read person → clear → read another person.

        Mimics: click person → cancel → click another person → cancel.
        """
        tree = StateTree()
        roles = ["Admin", "Developer", "User"]

        name_field = TextField("Name")
        name_field._attach(tree)
        role_field = Select("Role")
        role_field.set_items(*roles)
        role_field._attach(tree)

        binder = Binder(CrudPerson)
        binder.for_field(name_field).bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v))
        binder.for_field(role_field).bind(
            lambda p: p.role, lambda p, v: setattr(p, 'role', v))

        # Click person 1
        person1 = CrudPerson(name="Alice", role="Admin")
        binder.read_bean(person1)
        assert binder.is_dirty() is False

        # Cancel → clear form
        binder.read_bean(None)
        assert binder.is_dirty() is False

        # Click person 2
        person2 = CrudPerson(name="Bob", role="Developer")
        binder.read_bean(person2)
        assert binder.is_dirty() is False
        assert name_field.get_value() == "Bob"
        assert role_field.get_value() == "Developer"

    def test_select_not_dirty_after_read_bean_unattached_then_attach(self):
        """read_bean on unattached Select, then attach — must not be dirty.

        Mimics CRUD first click: read_bean runs before set_detail attaches
        the form fields.
        """
        tree = StateTree()
        roles = ["Admin", "Developer", "Designer"]

        # Create fields but DON'T attach yet (like CRUD __init__)
        name_field = TextField("Name")
        role_field = Select("Role")
        role_field.set_items(*roles)

        binder = Binder(CrudPerson)
        binder.for_field(name_field).bind(
            lambda p: p.name, lambda p, v: setattr(p, 'name', v))
        binder.for_field(role_field).bind(
            lambda p: p.role, lambda p, v: setattr(p, 'role', v))

        # read_bean BEFORE attach (fields have _element = None)
        person = CrudPerson(name="Hugo", role="Developer")
        binder.read_bean(person)

        # Values are stored internally even without element
        assert name_field.get_value() == "Hugo"
        assert role_field.get_value() == "Developer"
        assert binder.is_dirty() is False

        # Now attach (like set_detail triggers)
        name_field._attach(tree)
        role_field._attach(tree)

        # Still not dirty after attach
        assert binder.is_dirty() is False
