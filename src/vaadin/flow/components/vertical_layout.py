"""VerticalLayout component."""

from vaadin.flow.components.horizontal_layout import Alignment
from vaadin.flow.core.component import Component


class VerticalLayout(Component):
    """A layout that arranges children vertically."""

    _tag = "vaadin-vertical-layout"

    def __init__(self, *children: Component):
        super().__init__()
        self._children: list[Component] = list(children)
        self._spacing = True
        self._padding = True
        self._margin = False
        self._component_alignments: dict[Component, Alignment] = {}
        self._expanded_components: set[Component] = set()
        self._default_alignment: Alignment | None = None

    def _attach(self, tree):
        # Set default width before _attach applies pending styles
        if "width" not in self._pending_styles:
            self._pending_styles["width"] = "100%"
        super()._attach(tree)
        self._update_theme()
        if self._default_alignment:
            self.element.get_style().set("align-items", self._default_alignment.value)
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

    def set_padding(self, padding: bool):
        """Enable or disable padding."""
        self._padding = padding
        self._update_theme()

    def set_margin(self, margin: bool):
        """Enable or disable margin."""
        self._margin = margin
        self._update_theme()

    def expand(self, *components: Component):
        """Set flex-grow to 1 on the given components so they fill available space."""
        for component in components:
            self._expanded_components.add(component)
            if component._element:
                component.element.get_style().set("flex-grow", "1")

    def set_default_horizontal_component_alignment(self, alignment: Alignment):
        """Set default horizontal alignment for all children."""
        self._default_alignment = alignment
        if self._element:
            self.element.get_style().set("align-items", alignment.value)

    def set_horizontal_component_alignment(self, alignment: Alignment, *components: Component):
        """Set horizontal alignment for specific components."""
        for component in components:
            self._component_alignments[component] = alignment
            if component._element:
                component.element.get_style().set("align-self", alignment.value)

    def _apply_alignments(self):
        """Apply stored alignments and expand to attached components."""
        for component, alignment in self._component_alignments.items():
            if component._element:
                component.element.get_style().set("align-self", alignment.value)
        for component in self._expanded_components:
            if component._element:
                component.element.get_style().set("flex-grow", "1")

    def _update_theme(self):
        """Update the theme attribute."""
        if not self._element:
            return
        themes = []
        if self._margin:
            themes.append("margin")
        if self._padding:
            themes.append("padding")
        if self._spacing:
            themes.append("spacing")
        self.element.set_attribute("theme", " ".join(themes))
