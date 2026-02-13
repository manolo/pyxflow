"""HorizontalLayout component."""

from vaadin.flow.core.component import Component
from vaadin.flow.components.constants import (
    Alignment, JustifyContentMode, HorizontalLayoutVariant,
)


class HorizontalLayout(Component):
    """A layout that arranges children horizontally."""

    _v_fqcn = "com.vaadin.flow.component.orderedlayout.HorizontalLayout"
    _tag = "vaadin-horizontal-layout"

    def __init__(self, *children: Component):
        super().__init__()
        self._children: list[Component] = list(children)
        self._spacing = True
        self._margin = False
        self._component_alignments: dict[Component, Alignment] = {}
        self._expanded_components: set[Component] = set()
        self._default_alignment: Alignment | None = None

    def _attach(self, tree):
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
                if not component._element:
                    component._attach(self._element._tree)
                self.element.add_child(component.element)

    def remove(self, *components: Component):
        """Remove components from the layout."""
        for component in components:
            if component in self._children:
                self._children.remove(component)
                component._parent = None
                if self._element:
                    self.element.remove_child(component.element)

    def remove_all(self):
        """Remove all child components."""
        for child in list(self._children):
            self.remove(child)

    def set_spacing(self, spacing: bool):
        """Enable or disable spacing."""
        self._spacing = spacing
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

    def add_and_expand(self, *components: Component):
        """Add components and set them to expand (flex-grow: 1)."""
        self.add(*components)
        self.expand(*components)

    def set_default_vertical_component_alignment(self, alignment: Alignment):
        """Set default vertical alignment for all children."""
        self._default_alignment = alignment
        if self._element:
            self.element.get_style().set("align-items", alignment.value)

    def set_vertical_component_alignment(self, alignment: Alignment, *components: Component):
        """Set vertical alignment for specific components."""
        for component in components:
            self._component_alignments[component] = alignment
            # Apply immediately if already attached
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

    def set_padding(self, padding: bool):
        """Enable or disable padding."""
        self._padding = padding
        self._update_theme()

    def set_justify_content_mode(self, mode: JustifyContentMode):
        """Set justify-content-mode on the layout."""
        self._justify_content_mode = mode
        if self._element:
            self.element.get_style().set("justify-content", mode.value)

    def get_justify_content_mode(self) -> JustifyContentMode | None:
        return getattr(self, "_justify_content_mode", None)

    def set_align_items(self, alignment: Alignment):
        """Set the default alignment perpendicular to the layout direction."""
        self._default_alignment = alignment
        if self._element:
            self.element.get_style().set("align-items", alignment.value)

    def get_align_items(self) -> Alignment | None:
        return self._default_alignment

    def get_flex_grow(self, component: Component) -> float:
        """Get the flex-grow value of a component."""
        return float(component.get_style().get("flex-grow") or 0)

    def set_flex_grow(self, flex_grow: float, *components: Component):
        """Set flex-grow for specific components."""
        for component in components:
            if component._element:
                component.element.get_style().set("flex-grow", str(flex_grow))

    def set_flex_shrink(self, flex_shrink: float, *components: Component):
        """Set flex-shrink for specific components."""
        for component in components:
            if component._element:
                component.element.get_style().set("flex-shrink", str(flex_shrink))

    def replace(self, old_component: Component, new_component: Component):
        """Replace an existing component with a new one."""
        idx = self._children.index(old_component)
        self.remove(old_component)
        self.add_component_at_index(idx, new_component)

    def add_component_at_index(self, index: int, component: Component):
        """Add a component at a specific index."""
        self._children.insert(index, component)
        component._parent = self
        component._ui = self._ui
        if self._element:
            if not component._element:
                component._attach(self._element._tree)
            self.element.add_child(component.element, index)

    def add_component_as_first(self, component: Component):
        """Add a component as the first child."""
        self.add_component_at_index(0, component)

    def set_wrap(self, wrap: bool):
        """Enable or disable wrapping."""
        self._style.set("flex-wrap", "wrap" if wrap else "nowrap")

    def is_wrap(self) -> bool:
        return self._style.get("flex-wrap") == "wrap"

    def set_box_sizing(self, box_sizing: str):
        """Set box-sizing ('border-box' or 'content-box')."""
        self._style.set("box-sizing", box_sizing)

    def _update_theme(self):
        """Update the theme attribute."""
        if not self._element:
            return
        themes = []
        if self._margin:
            themes.append("margin")
        if getattr(self, "_padding", False):
            themes.append("padding")
        if self._spacing:
            themes.append("spacing")
        self.element.set_attribute("theme", " ".join(themes))

    def add_theme_variants(self, *variants: HorizontalLayoutVariant):
        """Add theme variants to the horizontal layout."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: HorizontalLayoutVariant):
        """Remove theme variants from the horizontal layout."""
        self.remove_theme_name(*variants)
