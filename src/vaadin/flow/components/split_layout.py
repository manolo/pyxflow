"""SplitLayout component."""

from enum import Enum
from typing import TYPE_CHECKING

from vaadin.flow.core.component import Component

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class Orientation(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


class SplitLayout(Component):
    """A layout with two resizable areas separated by a draggable splitter.

    Usage::

        split = SplitLayout()
        split.add_to_primary(grid_wrapper)
        split.add_to_secondary(editor_panel)
        split.set_splitter_position(70)
    """

    _tag = "vaadin-split-layout"

    def __init__(self, *args):
        """Create a SplitLayout.

        Args can be:
            () - empty
            (orientation) - with orientation
            (primary, secondary) - with two components
            (primary, secondary, orientation) - full
        """
        super().__init__()
        self._primary: Component | None = None
        self._secondary: Component | None = None
        self._orientation: Orientation = Orientation.HORIZONTAL
        self._splitter_position: float | None = None

        if len(args) == 1 and isinstance(args[0], Orientation):
            self._orientation = args[0]
        elif len(args) == 2:
            self._primary = args[0]
            self._secondary = args[1]
        elif len(args) == 3:
            self._primary = args[0]
            self._secondary = args[1]
            self._orientation = args[2]

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._orientation == Orientation.VERTICAL:
            self.element.set_property("orientation", "vertical")
        if self._primary:
            self._attach_slotted(self._primary, "primary", tree)
        if self._secondary:
            self._attach_slotted(self._secondary, "secondary", tree)
        if self._splitter_position is not None:
            self._apply_splitter_position()

    def _attach_slotted(self, component: Component, slot: str, tree: "StateTree"):
        component._ui = self._ui
        component._parent = self
        component._attach(tree)
        component.element.set_attribute("slot", slot)
        self.element.add_child(component.element)

    def add_to_primary(self, *components: Component):
        """Add component(s) to the primary (left/top) area."""
        if len(components) == 1:
            comp = components[0]
        else:
            from vaadin.flow.components.html import Div
            comp = Div()
            for c in components:
                comp.add(c)
        self._primary = comp
        if self._element:
            self._attach_slotted(comp, "primary", self._element._tree)
            if self._splitter_position is not None:
                self._apply_splitter_position()

    def add_to_secondary(self, *components: Component):
        """Add component(s) to the secondary (right/bottom) area."""
        if len(components) == 1:
            comp = components[0]
        else:
            from vaadin.flow.components.html import Div
            comp = Div()
            for c in components:
                comp.add(c)
        self._secondary = comp
        if self._element:
            self._attach_slotted(comp, "secondary", self._element._tree)
            if self._splitter_position is not None:
                self._apply_splitter_position()

    def get_primary_component(self) -> Component | None:
        return self._primary

    def get_secondary_component(self) -> Component | None:
        return self._secondary

    def set_orientation(self, orientation: Orientation):
        """Set the orientation (HORIZONTAL or VERTICAL)."""
        self._orientation = orientation
        if self._element:
            if orientation == Orientation.VERTICAL:
                self.element.set_property("orientation", "vertical")
            else:
                self.element.set_property("orientation", "horizontal")

    def get_orientation(self) -> Orientation:
        return self._orientation

    def set_splitter_position(self, position: float):
        """Set the splitter position as a percentage (0-100)."""
        self._splitter_position = max(0.0, min(100.0, position))
        if self._element:
            self._apply_splitter_position()

    def get_splitter_position(self) -> float | None:
        return self._splitter_position

    def _apply_splitter_position(self):
        """Apply flex styles to primary/secondary to set splitter position."""
        pos = self._splitter_position
        if pos is None:
            return
        if self._primary and self._primary._element:
            self._primary.element.get_style().set("flex", f"1 1 {pos}%")
        if self._secondary and self._secondary._element:
            self._secondary.element.get_style().set("flex", f"1 1 {100 - pos}%")

    def set_primary_style(self, style_name: str, value: str):
        """Set a CSS style on the primary component."""
        if self._primary and self._primary._element:
            self._primary.element.get_style().set(style_name, value)

    def set_secondary_style(self, style_name: str, value: str):
        """Set a CSS style on the secondary component."""
        if self._secondary and self._secondary._element:
            self._secondary.element.get_style().set(style_name, value)

    def add_splitter_drag_end_listener(self, listener):
        """Add a listener for when the user stops dragging the splitter."""
        if self._element:
            self.element.add_event_listener("splitter-dragend", listener)
        else:
            if not hasattr(self, "_pending_drag_listeners"):
                self._pending_drag_listeners = []
            self._pending_drag_listeners.append(listener)

    def remove_all(self):
        """Remove all children."""
        if self._primary and self._element:
            self.element.remove_child(self._primary.element)
        if self._secondary and self._element:
            self.element.remove_child(self._secondary.element)
        self._primary = None
        self._secondary = None
