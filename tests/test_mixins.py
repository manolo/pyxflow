"""Tests for HasValidation and HasRequired mixins."""

import pytest

from vaadin.flow.components import (
    TextField, EmailField, PasswordField, TextArea,
    NumberField, IntegerField, DatePicker, TimePicker, DateTimePicker,
    ComboBox, MultiSelectComboBox, Select, RadioButtonGroup, CheckboxGroup,
    Checkbox, CustomField,
    HasValidation, HasRequired,
)
from vaadin.flow.core.state_tree import StateTree


def create_tree():
    return StateTree()


# --- HasValidation mixin ---

class TestHasValidation:
    """Tests for HasValidation mixin API."""

    VALIDATION_COMPONENTS = [
        TextField, EmailField, PasswordField, TextArea,
        NumberField, IntegerField, DatePicker, TimePicker, DateTimePicker,
        ComboBox, MultiSelectComboBox, Select, RadioButtonGroup, CheckboxGroup,
        CustomField,
    ]

    @pytest.mark.parametrize("cls", VALIDATION_COMPONENTS, ids=lambda c: c.__name__)
    def test_is_instance(self, cls):
        comp = cls()
        assert isinstance(comp, HasValidation)

    def test_checkbox_not_has_validation(self):
        cb = Checkbox()
        assert not isinstance(cb, HasValidation)

    @pytest.mark.parametrize("cls", VALIDATION_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_invalid_before_attach(self, cls):
        comp = cls()
        assert comp.is_invalid() is False
        comp.set_invalid(True)
        assert comp.is_invalid() is True

    @pytest.mark.parametrize("cls", VALIDATION_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_invalid_after_attach(self, cls):
        tree = create_tree()
        comp = cls()
        comp._attach(tree)
        comp.set_invalid(True)
        assert comp.is_invalid() is True
        assert comp.element.node.get(1, "invalid") is True

    @pytest.mark.parametrize("cls", VALIDATION_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_invalid_buffered(self, cls):
        """set_invalid before attach → flushed via _pending_properties."""
        tree = create_tree()
        comp = cls()
        comp.set_invalid(True)
        comp._attach(tree)
        assert comp.element.node.get(1, "invalid") is True

    @pytest.mark.parametrize("cls", VALIDATION_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_error_message_before_attach(self, cls):
        comp = cls()
        assert comp.get_error_message() == ""
        comp.set_error_message("Required")
        assert comp.get_error_message() == "Required"

    @pytest.mark.parametrize("cls", VALIDATION_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_error_message_after_attach(self, cls):
        tree = create_tree()
        comp = cls()
        comp._attach(tree)
        comp.set_error_message("Required")
        assert comp.get_error_message() == "Required"
        assert comp.element.node.get(1, "errorMessage") == "Required"

    @pytest.mark.parametrize("cls", VALIDATION_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_error_message_buffered(self, cls):
        """set_error_message before attach → flushed via _pending_properties."""
        tree = create_tree()
        comp = cls()
        comp.set_error_message("Required")
        comp._attach(tree)
        assert comp.element.node.get(1, "errorMessage") == "Required"


# --- HasRequired mixin ---

class TestHasRequired:
    """Tests for HasRequired mixin API."""

    REQUIRED_COMPONENTS = [
        TextField, EmailField, PasswordField, TextArea,
        NumberField, IntegerField, DatePicker, TimePicker, DateTimePicker,
        ComboBox, MultiSelectComboBox, Select, RadioButtonGroup, CheckboxGroup,
        CustomField, Checkbox,
    ]

    @pytest.mark.parametrize("cls", REQUIRED_COMPONENTS, ids=lambda c: c.__name__)
    def test_is_instance(self, cls):
        comp = cls()
        assert isinstance(comp, HasRequired)

    @pytest.mark.parametrize("cls", REQUIRED_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_required_indicator_before_attach(self, cls):
        comp = cls()
        assert comp.is_required_indicator_visible() is False
        comp.set_required_indicator_visible(True)
        assert comp.is_required_indicator_visible() is True

    @pytest.mark.parametrize("cls", REQUIRED_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_required_indicator_after_attach(self, cls):
        tree = create_tree()
        comp = cls()
        comp._attach(tree)
        comp.set_required_indicator_visible(True)
        assert comp.is_required_indicator_visible() is True
        assert comp.element.node.get(1, "required") is True

    @pytest.mark.parametrize("cls", REQUIRED_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_required_indicator_buffered(self, cls):
        """set_required_indicator_visible before attach → flushed via _pending_properties."""
        tree = create_tree()
        comp = cls()
        comp.set_required_indicator_visible(True)
        comp._attach(tree)
        assert comp.element.node.get(1, "required") is True


# --- Convenience set_required() aliases ---

class TestSetRequiredAlias:
    """Components that had set_required() keep it as convenience alias."""

    ALIAS_COMPONENTS = [DatePicker, TimePicker, DateTimePicker, ComboBox, MultiSelectComboBox]

    @pytest.mark.parametrize("cls", ALIAS_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_required_delegates(self, cls):
        comp = cls()
        comp.set_required(True)
        assert comp.is_required_indicator_visible() is True

    @pytest.mark.parametrize("cls", ALIAS_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_required_after_attach(self, cls):
        tree = create_tree()
        comp = cls()
        comp._attach(tree)
        comp.set_required(True)
        assert comp.element.node.get(1, "required") is True


# --- Backward compatibility ---

class TestBackwardCompat:
    """Existing API for TextField.set_error_message and CustomField.set_invalid still works."""

    def test_text_field_error_message(self):
        tree = create_tree()
        tf = TextField()
        tf.set_error_message("Bad value")
        tf._attach(tree)
        assert tf.get_error_message() == "Bad value"
        assert tf.element.node.get(1, "errorMessage") == "Bad value"

    def test_email_field_error_message(self):
        tree = create_tree()
        ef = EmailField()
        ef.set_error_message("Invalid email")
        ef._attach(tree)
        assert ef.get_error_message() == "Invalid email"
        assert ef.element.node.get(1, "errorMessage") == "Invalid email"

    def test_custom_field_set_invalid(self):
        tree = create_tree()
        cf = CustomField()
        cf.set_invalid(True)
        cf.set_error_message("Required")
        cf._attach(tree)
        assert cf.is_invalid() is True
        assert cf.get_error_message() == "Required"
        assert cf.element.node.get(1, "invalid") is True
        assert cf.element.node.get(1, "errorMessage") == "Required"

    def test_custom_field_toggle_invalid(self):
        tree = create_tree()
        cf = CustomField()
        cf._attach(tree)
        cf.set_invalid(True)
        assert cf.element.node.get(1, "invalid") is True
        cf.set_invalid(False)
        assert cf.element.node.get(1, "invalid") is False
