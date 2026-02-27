"""FormLayout, FormItem, and FormRow components."""

import json
from enum import Enum
from typing import Any, TYPE_CHECKING, Union

from vaadin.flow.core.component import Component

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class ResponsiveStep:
    """Defines a responsive breakpoint for FormLayout columns.

    Each step specifies the minimum viewport width at which a certain
    number of columns should be used.
    """

    class LabelsPosition(Enum):
        """Position of field labels within a FormItem."""
        ASIDE = "aside"
        TOP = "top"

    def __init__(self, min_width: str | None, columns: int,
                 labels_position: "ResponsiveStep.LabelsPosition | None" = None):
        self._min_width = min_width
        self._columns = columns
        self._labels_position = labels_position

    @property
    def min_width(self) -> str | None:
        return self._min_width

    @property
    def columns(self) -> int:
        return self._columns

    @property
    def labels_position(self) -> "ResponsiveStep.LabelsPosition | None":
        return self._labels_position

    def to_json(self) -> dict:
        """Serialize to a dict for the responsiveSteps property."""
        result: dict[str, Any] = {"columns": self._columns}
        if self._min_width is not None:
            result["minWidth"] = self._min_width
        if self._labels_position is not None:
            result["labelsPosition"] = self._labels_position.value
        return result


class FormItem(Component):
    """A wrapper component for form fields with label support.

    FormItem wraps a field and provides a label slot. It is used
    inside FormLayout to associate labels with fields.
    """

    _tag = "vaadin-form-item"

    def __init__(self, *components: Component):
        super().__init__()
        self._children: list[Component] = list(components)
        self._label_components: set[int] = set()  # Track by id() which are label-slot

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        for child in self._children:
            child._ui = self._ui
            child._parent = self
            child._attach(tree)
            if id(child) in self._label_components:
                child.element.set_attribute("slot", "label")
        if self._children:
            self.element.add_children([child.element for child in self._children])

    def add(self, *components: Component):
        """Add components to the form item."""
        for component in components:
            self._children.append(component)
            component._parent = self
            component._ui = self._ui
            if self._element:
                if not component._element:
                    component._attach(self._element._tree)
                self.element.add_child(component.element)

    def remove(self, *components: Component):
        """Remove components from the form item."""
        for component in components:
            if component in self._children:
                self._children.remove(component)
                self._label_components.discard(id(component))
                component._parent = None
                if self._element:
                    self.element.remove_child(component.element)

    def remove_all(self):
        """Remove all components from the form item."""
        for child in list(self._children):
            self.remove(child)

    def _add_to_label(self, *components: Component):
        """Add components to the label slot.

        Sets the 'slot' attribute to 'label' on each component's element
        so they render in the FormItem's label area.
        """
        for component in components:
            self._children.append(component)
            self._label_components.add(id(component))
            component._parent = self
            component._ui = self._ui
            if self._element:
                component._attach(self._element._tree)
                component.element.set_attribute("slot", "label")
                self.element.add_child(component.element)


class FormRow(Component):
    """A row container for auto-responsive FormLayout.

    Groups fields into a single row within a FormLayout
    when auto-responsive mode is enabled.
    """

    _tag = "vaadin-form-row"

    def __init__(self, *components: Component):
        super().__init__()
        self._children: list[Component] = list(components)

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        for child in self._children:
            child._ui = self._ui
            child._parent = self
            child._attach(tree)
        if self._children:
            self.element.add_children([child.element for child in self._children])

    def add(self, *components: Component):
        """Add components to the row."""
        for component in components:
            self._children.append(component)
            component._parent = self
            component._ui = self._ui
            if self._element:
                component._attach(self._element._tree)
                self.element.add_child(component.element)

    def add_with_colspan(self, component: Component, colspan: int):
        """Add a component with a specific column span."""
        self.add(component)
        self.set_colspan(component, colspan)

    def set_colspan(self, component: Component, colspan: int):
        """Set the column span for a component."""
        if component._element:
            component.element.set_attribute("colspan", str(colspan))

    def get_colspan(self, component: Component) -> int:
        """Get the column span for a component."""
        if component._element:
            val = component.element.get_attribute("colspan")
            if val is not None:
                return int(val)
        return 1

    def add_form_item(self, field: Component, label: Union[str, Component]) -> FormItem:
        """Add a field with a label, wrapped in a FormItem."""
        from vaadin.flow.components.span import Span

        item = FormItem(field)
        if isinstance(label, str):
            label_component = Span(label)
        else:
            label_component = label
        item._add_to_label(label_component)
        self.add(item)
        return item


class FormLayout(Component):
    """A responsive form layout component.

    FormLayout arranges fields in columns and supports responsive
    breakpoints to adjust the number of columns based on viewport width.
    """

    _v_fqcn = "com.vaadin.flow.component.formlayout.FormLayout"
    _tag = "vaadin-form-layout"

    def __init__(self, *components: Component):
        super().__init__()
        self._children: list[Component] = list(components)
        self._responsive_steps: list[ResponsiveStep] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        for child in self._children:
            child._ui = self._ui
            child._parent = self
            child._attach(tree)
        if self._children:
            self.element.add_children([child.element for child in self._children])
        if self._responsive_steps:
            self._apply_responsive_steps()

    # --- Children management ---

    def add(self, *components: Component):
        """Add components to the layout."""
        for component in components:
            self._children.append(component)
            component._parent = self
            component._ui = self._ui
            if self._element:
                component._attach(self._element._tree)
                self.element.add_child(component.element)

    def add_with_colspan(self, component: Component, colspan: int):
        """Add a component with a specific column span."""
        self.add(component)
        self.set_colspan(component, colspan)

    def remove(self, *components: Component):
        """Remove components from the layout."""
        for component in components:
            if component in self._children:
                self._children.remove(component)
                component._parent = None
                if self._element:
                    self.element.remove_child(component.element)

    # --- Colspan ---

    def set_colspan(self, component: Component, colspan: int):
        """Set the column span for a component."""
        if component._element:
            component.element.set_attribute("colspan", str(colspan))

    def get_colspan(self, component: Component) -> int:
        """Get the column span for a component."""
        if component._element:
            val = component.element.get_attribute("colspan")
            if val is not None:
                return int(val)
        return 1

    # --- Responsive steps ---

    def set_responsive_steps(self, *steps: ResponsiveStep):
        """Set the responsive steps for column layout."""
        self._responsive_steps = list(steps)
        if self._element:
            self._apply_responsive_steps()

    def _apply_responsive_steps(self):
        """Apply responsive steps as a JSON property."""
        steps_json = json.dumps([step.to_json() for step in self._responsive_steps])
        self.element.set_property("responsiveSteps", steps_json)

    def get_responsive_steps(self) -> list[ResponsiveStep]:
        """Get the current responsive steps."""
        return list(self._responsive_steps)

    # --- FormItem convenience ---

    def add_form_item(self, field: Component, label: Union[str, Component]) -> FormItem:
        """Add a field with a label, wrapped in a FormItem.

        Args:
            field: The field component.
            label: A string label or a Component for the label slot.

        Returns:
            The created FormItem.
        """
        from vaadin.flow.components.span import Span

        item = FormItem(field)
        if isinstance(label, str):
            label_component = Span(label)
        else:
            label_component = label
        item._add_to_label(label_component)
        self.add(item)
        return item

    # --- FormRow convenience ---

    def add_form_row(self, *components: Component) -> "FormRow":
        """Add components grouped in a FormRow.

        Returns:
            The created FormRow.
        """
        row = FormRow(*components)
        self.add(row)
        return row

    # --- CSS custom properties ---

    def set_label_width(self, width: str):
        """Set the label width (e.g., '200px', '8em')."""
        if self._element:
            self.element.get_style().set("--vaadin-form-layout-label-width", width)

    def get_label_width(self) -> str | None:
        """Get the label width."""
        if self._element:
            return self.element.get_style().get("--vaadin-form-layout-label-width")
        return None

    def set_label_spacing(self, spacing: str):
        """Set the spacing between label and field."""
        if self._element:
            self.element.get_style().set("--vaadin-form-layout-label-spacing", spacing)

    def get_label_spacing(self) -> str | None:
        """Get the label spacing."""
        if self._element:
            return self.element.get_style().get("--vaadin-form-layout-label-spacing")
        return None

    def set_column_spacing(self, spacing: str):
        """Set the spacing between columns."""
        if self._element:
            self.element.get_style().set("--vaadin-form-layout-column-spacing", spacing)

    def get_column_spacing(self) -> str | None:
        """Get the column spacing."""
        if self._element:
            return self.element.get_style().get("--vaadin-form-layout-column-spacing")
        return None

    def set_row_spacing(self, spacing: str):
        """Set the spacing between rows."""
        if self._element:
            self.element.get_style().set("--vaadin-form-layout-row-spacing", spacing)

    def get_row_spacing(self) -> str | None:
        """Get the row spacing."""
        if self._element:
            return self.element.get_style().get("--vaadin-form-layout-row-spacing")
        return None

    # --- Auto-responsive properties ---

    def _set_form_property(self, name: str, value):
        """Set a property, buffering in _pending_properties if not yet attached."""
        if self._element:
            self.element.set_property(name, value)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties[name] = value

    def _get_form_property(self, name: str, default=None):
        """Get a property from element or pending buffer."""
        if self._element:
            return self.element.get_property(name, default)
        return getattr(self, "_pending_properties", {}).get(name, default)

    def set_auto_responsive(self, auto_responsive: bool):
        """Enable or disable auto-responsive mode."""
        self._set_form_property("autoResponsive", auto_responsive)

    def is_auto_responsive(self) -> bool:
        return self._get_form_property("autoResponsive", False)

    def set_auto_rows(self, auto_rows: bool):
        """Enable or disable auto-rows mode."""
        self._set_form_property("autoRows", auto_rows)

    def is_auto_rows(self) -> bool:
        return self._get_form_property("autoRows", False)

    def set_column_width(self, width: str):
        """Set the column width for auto-responsive mode."""
        self._set_form_property("columnWidth", width)

    def get_column_width(self) -> str | None:
        return self._get_form_property("columnWidth")

    def set_max_columns(self, max_columns: int):
        """Set the maximum number of columns."""
        self._set_form_property("maxColumns", max_columns)

    def get_max_columns(self) -> int | None:
        return self._get_form_property("maxColumns")

    def set_min_columns(self, min_columns: int):
        """Set the minimum number of columns."""
        self._set_form_property("minColumns", min_columns)

    def get_min_columns(self) -> int | None:
        return self._get_form_property("minColumns")

    def set_expand_columns(self, expand: bool):
        """Set whether columns should expand to fill available space."""
        self._set_form_property("expandColumns", expand)

    def is_expand_columns(self) -> bool:
        return self._get_form_property("expandColumns", False)

    def set_expand_fields(self, expand: bool):
        """Set whether fields should expand within their column."""
        self._set_form_property("expandFields", expand)

    def is_expand_fields(self) -> bool:
        return self._get_form_property("expandFields", False)

    def set_labels_aside(self, aside: bool):
        """Set whether labels are positioned beside fields."""
        self._set_form_property("labelsAside", aside)

    def is_labels_aside(self) -> bool:
        return self._get_form_property("labelsAside", False)
