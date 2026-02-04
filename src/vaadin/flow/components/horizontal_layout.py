"""HorizontalLayout component."""

from enum import Enum

from vaadin.flow.core.component import Component


class Alignment(Enum):
    """Alignment options."""
    START = "flex-start"
    END = "flex-end"
    CENTER = "center"
    STRETCH = "stretch"
    BASELINE = "baseline"


class HorizontalLayout(Component):
    """A layout that arranges children horizontally."""

    _tag = "vaadin-horizontal-layout"

    def __init__(self, *children: Component):
        super().__init__()
        self._children: list[Component] = list(children)
        self._spacing = True
        self._margin = False
        self._component_alignments: dict[Component, Alignment] = {}

    def _attach(self, tree):
        super()._attach(tree)
        self._update_theme()
        # Attach all children first
        for child in self._children:
            child._ui = self._ui
            child._parent = self
            child._attach(tree)
        # Then add all children in a single splice operation
        if self._children:
            self.element.add_children([child.element for child in self._children])
        # Apply stored alignments after children are attached
        self._apply_alignments()

    def add(self, *components: Component):
        """Add components to the layout."""
        for component in components:
            self._children.append(component)
            component._parent = self
            component._ui = self._ui
            if self._element:
                component._attach(self._ui.tree)
                self.element.add_child(component.element)

    def remove(self, *components: Component):
        """Remove components from the layout."""
        for component in components:
            if component in self._children:
                self._children.remove(component)
                component._parent = None
                if self._element:
                    self.element.remove_child(component.element)

    def set_spacing(self, spacing: bool):
        """Enable or disable spacing."""
        self._spacing = spacing
        self._update_theme()

    def set_margin(self, margin: bool):
        """Enable or disable margin."""
        self._margin = margin
        self._update_theme()

    def set_vertical_component_alignment(self, alignment: Alignment, *components: Component):
        """Set vertical alignment for specific components."""
        for component in components:
            self._component_alignments[component] = alignment
            # Apply immediately if already attached
            if component._element:
                component.element.get_style().set("align-self", alignment.value)

    def _apply_alignments(self):
        """Apply stored alignments to attached components."""
        for component, alignment in self._component_alignments.items():
            if component._element:
                component.element.get_style().set("align-self", alignment.value)

    def _update_theme(self):
        """Update the theme attribute."""
        if not self._element:
            return
        themes = []
        if self._margin:
            themes.append("margin")
        if self._spacing:
            themes.append("spacing")
        self.element.set_attribute("theme", " ".join(themes))
