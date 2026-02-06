"""Tests for FormLayout, FormItem, and FormRow components."""

import json

import pytest

from vaadin.flow.components import FormLayout, FormItem, FormRow, ResponsiveStep
from vaadin.flow.components import TextField, Button, Span
from vaadin.flow.core.state_tree import StateTree


class TestResponsiveStep:
    """Test ResponsiveStep configuration."""

    def test_to_json_basic(self):
        """ResponsiveStep serializes with minWidth and columns."""
        step = ResponsiveStep("600px", 2)
        assert step.to_json() == {"minWidth": "600px", "columns": 2}

    def test_to_json_with_labels_position(self):
        """ResponsiveStep includes labelsPosition when set."""
        step = ResponsiveStep("800px", 3, ResponsiveStep.LabelsPosition.ASIDE)
        result = step.to_json()
        assert result == {"minWidth": "800px", "columns": 3, "labelsPosition": "aside"}

    def test_to_json_no_min_width(self):
        """ResponsiveStep omits minWidth when None."""
        step = ResponsiveStep(None, 1)
        assert step.to_json() == {"columns": 1}

    def test_labels_position_values(self):
        """LabelsPosition enum has correct values."""
        assert ResponsiveStep.LabelsPosition.ASIDE.value == "aside"
        assert ResponsiveStep.LabelsPosition.TOP.value == "top"

    def test_properties(self):
        """ResponsiveStep exposes properties."""
        step = ResponsiveStep("500px", 2, ResponsiveStep.LabelsPosition.TOP)
        assert step.min_width == "500px"
        assert step.columns == 2
        assert step.labels_position == ResponsiveStep.LabelsPosition.TOP


class TestFormItem:
    """Test FormItem component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        """FormItem has correct tag."""
        item = FormItem()
        assert item._tag == "vaadin-form-item"

    def test_create_empty(self):
        """FormItem can be created empty."""
        item = FormItem()
        assert item._children == []

    def test_create_with_components(self, tree):
        """FormItem can be created with components."""
        tf = TextField()
        item = FormItem(tf)
        item._attach(tree)
        assert tf in item._children

    def test_add(self, tree):
        """add() appends components."""
        item = FormItem()
        item._attach(tree)
        tf = TextField()
        item.add(tf)
        assert tf in item._children

    def test_remove(self, tree):
        """remove() removes components."""
        tf = TextField()
        item = FormItem(tf)
        item._attach(tree)
        item.remove(tf)
        assert tf not in item._children

    def test_remove_all(self, tree):
        """remove_all() clears all children."""
        tf1 = TextField()
        tf2 = TextField()
        item = FormItem(tf1, tf2)
        item._attach(tree)
        item.remove_all()
        assert item._children == []

    def test_add_to_label(self, tree):
        """_add_to_label sets slot='label' attribute."""
        item = FormItem()
        item._attach(tree)
        label = Span("Name")
        item._add_to_label(label)
        assert label in item._children
        assert label.element.get_attribute("slot") == "label"


class TestFormRow:
    """Test FormRow component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        """FormRow has correct tag."""
        row = FormRow()
        assert row._tag == "vaadin-form-row"

    def test_create_with_components(self, tree):
        """FormRow can be created with components."""
        tf = TextField()
        btn = Button("OK")
        row = FormRow(tf, btn)
        row._attach(tree)
        assert tf in row._children
        assert btn in row._children

    def test_add(self, tree):
        """add() appends components."""
        row = FormRow()
        row._attach(tree)
        tf = TextField()
        row.add(tf)
        assert tf in row._children

    def test_colspan(self, tree):
        """set_colspan/get_colspan work correctly."""
        tf = TextField()
        row = FormRow(tf)
        row._attach(tree)
        row.set_colspan(tf, 2)
        assert row.get_colspan(tf) == 2

    def test_add_with_colspan(self, tree):
        """add_with_colspan adds and sets colspan."""
        row = FormRow()
        row._attach(tree)
        tf = TextField()
        row.add_with_colspan(tf, 3)
        assert tf in row._children
        assert row.get_colspan(tf) == 3

    def test_default_colspan(self, tree):
        """Default colspan is 1."""
        tf = TextField()
        row = FormRow(tf)
        row._attach(tree)
        assert row.get_colspan(tf) == 1

    def test_add_form_item(self, tree):
        """add_form_item creates a FormItem with label."""
        row = FormRow()
        row._attach(tree)
        tf = TextField()
        item = row.add_form_item(tf, "Name")
        assert isinstance(item, FormItem)
        assert item in row._children


class TestFormLayout:
    """Test FormLayout component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        """FormLayout has correct tag."""
        layout = FormLayout()
        assert layout._tag == "vaadin-form-layout"

    def test_create_empty(self):
        """FormLayout can be created empty."""
        layout = FormLayout()
        assert layout._children == []

    def test_create_with_components(self, tree):
        """FormLayout can be created with components."""
        tf = TextField()
        btn = Button("OK")
        layout = FormLayout(tf, btn)
        layout._attach(tree)
        assert tf in layout._children
        assert btn in layout._children

    def test_add(self, tree):
        """add() appends components."""
        layout = FormLayout()
        layout._attach(tree)
        tf = TextField()
        layout.add(tf)
        assert tf in layout._children

    def test_remove(self, tree):
        """remove() removes components."""
        tf = TextField()
        layout = FormLayout(tf)
        layout._attach(tree)
        layout.remove(tf)
        assert tf not in layout._children

    # --- Colspan ---

    def test_colspan(self, tree):
        """set_colspan/get_colspan work correctly."""
        tf = TextField()
        layout = FormLayout(tf)
        layout._attach(tree)
        layout.set_colspan(tf, 2)
        assert layout.get_colspan(tf) == 2

    def test_add_with_colspan(self, tree):
        """add_with_colspan adds and sets colspan."""
        layout = FormLayout()
        layout._attach(tree)
        tf = TextField()
        layout.add_with_colspan(tf, 3)
        assert tf in layout._children
        assert layout.get_colspan(tf) == 3

    def test_default_colspan(self, tree):
        """Default colspan is 1."""
        tf = TextField()
        layout = FormLayout(tf)
        layout._attach(tree)
        assert layout.get_colspan(tf) == 1

    # --- Responsive steps ---

    def test_responsive_steps(self, tree):
        """set_responsive_steps sets the property."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_responsive_steps(
            ResponsiveStep(None, 1),
            ResponsiveStep("600px", 2),
            ResponsiveStep("800px", 3, ResponsiveStep.LabelsPosition.ASIDE),
        )
        steps = layout.get_responsive_steps()
        assert len(steps) == 3
        assert steps[0].columns == 1
        assert steps[1].min_width == "600px"
        assert steps[2].labels_position == ResponsiveStep.LabelsPosition.ASIDE

    def test_responsive_steps_property_value(self, tree):
        """Responsive steps are serialized as JSON property."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_responsive_steps(
            ResponsiveStep("500px", 2),
        )
        prop = layout.element.get_property("responsiveSteps")
        parsed = json.loads(prop)
        assert parsed == [{"minWidth": "500px", "columns": 2}]

    # --- FormItem convenience ---

    def test_add_form_item_with_string_label(self, tree):
        """add_form_item with string label creates Span."""
        layout = FormLayout()
        layout._attach(tree)
        tf = TextField()
        item = layout.add_form_item(tf, "Name")
        assert isinstance(item, FormItem)
        assert item in layout._children

    def test_add_form_item_with_component_label(self, tree):
        """add_form_item with Component label uses it directly."""
        layout = FormLayout()
        layout._attach(tree)
        tf = TextField()
        label = Span("Custom")
        item = layout.add_form_item(tf, label)
        assert isinstance(item, FormItem)
        assert label.element.get_attribute("slot") == "label"

    # --- FormRow convenience ---

    def test_add_form_row(self, tree):
        """add_form_row creates and adds a FormRow."""
        layout = FormLayout()
        layout._attach(tree)
        tf1 = TextField()
        tf2 = TextField()
        row = layout.add_form_row(tf1, tf2)
        assert isinstance(row, FormRow)
        assert row in layout._children

    # --- CSS custom properties ---

    def test_label_width(self, tree):
        """set/get_label_width works."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_label_width("200px")
        assert layout.get_label_width() == "200px"

    def test_label_spacing(self, tree):
        """set/get_label_spacing works."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_label_spacing("1em")
        assert layout.get_label_spacing() == "1em"

    def test_column_spacing(self, tree):
        """set/get_column_spacing works."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_column_spacing("2em")
        assert layout.get_column_spacing() == "2em"

    def test_row_spacing(self, tree):
        """set/get_row_spacing works."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_row_spacing("10px")
        assert layout.get_row_spacing() == "10px"

    # --- Auto-responsive properties ---

    def test_auto_responsive(self, tree):
        """set/is_auto_responsive works."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_auto_responsive(True)
        assert layout.is_auto_responsive() is True

    def test_auto_rows(self, tree):
        """set/is_auto_rows works."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_auto_rows(True)
        assert layout.is_auto_rows() is True

    def test_column_width(self, tree):
        """set/get_column_width works."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_column_width("300px")
        assert layout.get_column_width() == "300px"

    def test_max_columns(self, tree):
        """set/get_max_columns works."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_max_columns(4)
        assert layout.get_max_columns() == 4

    def test_min_columns(self, tree):
        """set/get_min_columns works."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_min_columns(1)
        assert layout.get_min_columns() == 1

    def test_expand_columns(self, tree):
        """set/is_expand_columns works."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_expand_columns(True)
        assert layout.is_expand_columns() is True

    def test_expand_fields(self, tree):
        """set/is_expand_fields works."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_expand_fields(True)
        assert layout.is_expand_fields() is True

    def test_labels_aside(self, tree):
        """set/is_labels_aside works."""
        layout = FormLayout()
        layout._attach(tree)
        layout.set_labels_aside(True)
        assert layout.is_labels_aside() is True

    # --- Attach with initial responsive steps ---

    def test_responsive_steps_set_before_attach(self, tree):
        """Responsive steps set before attach are applied on attach."""
        layout = FormLayout()
        layout.set_responsive_steps(
            ResponsiveStep("0", 1),
            ResponsiveStep("600px", 2),
        )
        layout._attach(tree)
        prop = layout.element.get_property("responsiveSteps")
        parsed = json.loads(prop)
        assert len(parsed) == 2
