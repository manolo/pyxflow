"""Tests for input field components."""

import pytest

from vaadin.flow.components import (
    PasswordField,
    EmailField,
    ProgressBar,
    Select,
    RadioButtonGroup,
    CheckboxGroup,
)
from vaadin.flow.core.state_tree import StateTree


class TestPasswordField:
    """Test PasswordField component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_password_field(self):
        """PasswordField can be created."""
        field = PasswordField()
        assert field._tag == "vaadin-password-field"
        assert field.get_value() == ""

    def test_create_with_label(self):
        """PasswordField can be created with label."""
        field = PasswordField("Password")
        assert field.get_label() == "Password"

    def test_set_value(self, tree):
        """set_value works correctly."""
        field = PasswordField()
        field._attach(tree)
        field.set_value("secret123")
        assert field.get_value() == "secret123"

    def test_set_placeholder(self, tree):
        """set_placeholder works correctly."""
        field = PasswordField()
        field._attach(tree)
        field.set_placeholder("Enter password")
        assert field.get_placeholder() == "Enter password"

    def test_reveal_button_visible(self, tree):
        """Reveal button visibility can be toggled."""
        field = PasswordField()
        field._attach(tree)
        assert field.is_reveal_button_visible() is True
        field.set_reveal_button_visible(False)
        assert field.is_reveal_button_visible() is False

    def test_value_change_listener(self, tree):
        """Value change listener is called."""
        field = PasswordField()
        field._attach(tree)

        events = []
        field.add_value_change_listener(lambda e: events.append(e))

        field._handle_change({"value": "newpass"})

        assert len(events) == 1
        assert field.get_value() == "newpass"

    def test_sync_property(self, tree):
        """_sync_property updates internal state."""
        field = PasswordField()
        field._attach(tree)
        field._sync_property("value", "synced")
        assert field.get_value() == "synced"


class TestEmailField:
    """Test EmailField component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_email_field(self):
        """EmailField can be created."""
        field = EmailField()
        assert field._tag == "vaadin-email-field"
        assert field.get_value() == ""

    def test_create_with_label(self):
        """EmailField can be created with label."""
        field = EmailField("Email")
        assert field.get_label() == "Email"

    def test_set_value(self, tree):
        """set_value works correctly."""
        field = EmailField()
        field._attach(tree)
        field.set_value("test@example.com")
        assert field.get_value() == "test@example.com"

    def test_set_placeholder(self, tree):
        """set_placeholder works correctly."""
        field = EmailField()
        field._attach(tree)
        field.set_placeholder("name@example.com")
        assert field.get_placeholder() == "name@example.com"

    def test_set_error_message(self, tree):
        """set_error_message works correctly."""
        field = EmailField()
        field._attach(tree)
        field.set_error_message("Invalid email")
        assert field.get_error_message() == "Invalid email"

    def test_clear_button_visible(self, tree):
        """Clear button visibility can be toggled."""
        field = EmailField()
        field._attach(tree)
        assert field.is_clear_button_visible() is False
        field.set_clear_button_visible(True)
        assert field.is_clear_button_visible() is True

    def test_value_change_listener(self, tree):
        """Value change listener is called."""
        field = EmailField()
        field._attach(tree)

        events = []
        field.add_value_change_listener(lambda e: events.append(e))

        field._handle_change({"value": "new@test.com"})

        assert len(events) == 1
        assert field.get_value() == "new@test.com"


class TestProgressBar:
    """Test ProgressBar component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_progress_bar(self):
        """ProgressBar can be created."""
        bar = ProgressBar()
        assert bar._tag == "vaadin-progress-bar"
        assert bar.get_value() == 0.0

    def test_set_value(self, tree):
        """set_value works correctly."""
        bar = ProgressBar()
        bar._attach(tree)
        bar.set_value(0.5)
        assert bar.get_value() == 0.5

    def test_set_min_max(self, tree):
        """set_min and set_max work correctly."""
        bar = ProgressBar()
        bar._attach(tree)
        bar.set_min(10)
        bar.set_max(100)
        assert bar.get_min() == 10
        assert bar.get_max() == 100

    def test_indeterminate(self, tree):
        """Indeterminate mode can be toggled."""
        bar = ProgressBar()
        bar._attach(tree)
        assert bar.is_indeterminate() is False
        bar.set_indeterminate(True)
        assert bar.is_indeterminate() is True

    def test_default_range(self):
        """Default range is 0 to 1."""
        bar = ProgressBar()
        assert bar.get_min() == 0.0
        assert bar.get_max() == 1.0


class TestSelect:
    """Test Select component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_select(self):
        """Select can be created."""
        select = Select()
        assert select._tag == "vaadin-select"

    def test_create_with_label(self):
        """Select can be created with label."""
        select = Select("Choose")
        assert select.get_label() == "Choose"

    def test_set_items(self):
        """set_items works correctly."""
        select = Select()
        select.set_items("A", "B", "C")
        assert select.get_items() == ["A", "B", "C"]

    def test_set_value(self, tree):
        """set_value works correctly."""
        select = Select()
        select.set_items("A", "B", "C")
        select._attach(tree)
        select.set_value("B")
        assert select.get_value() == "B"

    def test_set_placeholder(self, tree):
        """set_placeholder works correctly."""
        select = Select()
        select._attach(tree)
        select.set_placeholder("Select an option")
        assert select.get_placeholder() == "Select an option"

    def test_value_change_listener(self, tree):
        """Value change listener is called."""
        select = Select()
        select.set_items("X", "Y", "Z")
        select._attach(tree)

        events = []
        select.add_value_change_listener(lambda e: events.append(e))

        select._handle_value_changed({"value": "Y"})

        assert len(events) == 1
        assert select.get_value() == "Y"

    def test_item_label_generator(self, tree):
        """Item label generator is used."""
        select = Select()
        select.set_item_label_generator(lambda x: f"Option: {x}")
        select.set_items(1, 2, 3)
        select._attach(tree)

        # Label should be generated
        assert select._get_item_label(1) == "Option: 1"


class TestRadioButtonGroup:
    """Test RadioButtonGroup component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_radio_group(self):
        """RadioButtonGroup can be created."""
        group = RadioButtonGroup()
        assert group._tag == "vaadin-radio-group"

    def test_create_with_label(self):
        """RadioButtonGroup can be created with label."""
        group = RadioButtonGroup("Choose one")
        assert group.get_label() == "Choose one"

    def test_set_items(self):
        """set_items works correctly."""
        group = RadioButtonGroup()
        group.set_items("A", "B", "C")
        assert group.get_items() == ["A", "B", "C"]

    def test_set_value(self, tree):
        """set_value works correctly."""
        group = RadioButtonGroup()
        group.set_items("A", "B", "C")
        group._attach(tree)
        group.set_value("B")
        assert group.get_value() == "B"

    def test_value_change_listener(self, tree):
        """Value change listener is called."""
        group = RadioButtonGroup()
        group.set_items("X", "Y", "Z")
        group._attach(tree)

        events = []
        group.add_value_change_listener(lambda e: events.append(e))

        group._handle_value_changed({"value": "Z"})

        assert len(events) == 1
        assert group.get_value() == "Z"


class TestCheckboxGroup:
    """Test CheckboxGroup component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_checkbox_group(self):
        """CheckboxGroup can be created."""
        group = CheckboxGroup()
        assert group._tag == "vaadin-checkbox-group"

    def test_create_with_label(self):
        """CheckboxGroup can be created with label."""
        group = CheckboxGroup("Select multiple")
        assert group.get_label() == "Select multiple"

    def test_set_items(self):
        """set_items works correctly."""
        group = CheckboxGroup()
        group.set_items("A", "B", "C")
        assert group.get_items() == ["A", "B", "C"]

    def test_set_value(self, tree):
        """set_value works correctly with set."""
        group = CheckboxGroup()
        group.set_items("A", "B", "C")
        group._attach(tree)
        group.set_value({"A", "C"})
        assert group.get_value() == {"A", "C"}

    def test_value_change_listener(self, tree):
        """Value change listener is called."""
        group = CheckboxGroup()
        group.set_items("X", "Y", "Z")
        group._attach(tree)

        events = []
        group.add_value_change_listener(lambda e: events.append(e))

        group._handle_value_changed({"value": ["X", "Z"]})

        assert len(events) == 1
        assert group.get_value() == {"X", "Z"}

    def test_empty_value(self):
        """Empty value is an empty set."""
        group = CheckboxGroup()
        assert group.get_value() == set()
