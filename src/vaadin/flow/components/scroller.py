"""Scroller component."""

from typing import TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.components.constants import ScrollDirection, ScrollerVariant as ScrollerVariant  # noqa: F401 — re-export

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class Scroller(Component):
    """A scrollable container component.

    Usage::

        scroller = Scroller(content, scroll_direction=ScrollDirection.VERTICAL)
        scroller.set_height("200px")
    """

    _v_fqcn = "com.vaadin.flow.component.orderedlayout.Scroller"
    _tag = "vaadin-scroller"

    def __init__(self, *children: Component,
                 scroll_direction: ScrollDirection = ScrollDirection.BOTH):
        self._children: list[Component] = list(children)
        self._scroll_direction = scroll_direction

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._scroll_direction != ScrollDirection.BOTH:
            self.element.set_property("scrollDirection", self._scroll_direction.value)
        for child in self._children:
            child._ui = self._ui
            child._parent = self
            child._attach(tree)
            self.element.add_child(child.element)

    def add(self, *components: Component):
        """Add components to the scroller."""
        for comp in components:
            self._children.append(comp)
            if self._element:
                comp._ui = self._ui
                comp._parent = self
                comp._attach(self._element._tree)
                self.element.add_child(comp.element)

    def remove_all(self):
        """Remove all child components."""
        if self._element:
            for child in self._children:
                if child._element:
                    self.element.remove_child(child.element)
        for child in self._children:
            child._parent = None
        self._children.clear()

    def set_content(self, component: Component):
        """Set a single component as content (replaces all children)."""
        if self._element:
            for child in self._children:
                if child._element:
                    self.element.remove_child(child.element)
        self._children = [component]
        if self._element:
            component._ui = self._ui
            component._parent = self
            component._attach(self._element._tree)
            self.element.add_child(component.element)

    def set_scroll_direction(self, direction: ScrollDirection):
        """Set the scroll direction."""
        self._scroll_direction = direction
        if self._element:
            self.element.set_property("scrollDirection", direction.value)

    def get_content(self) -> Component | None:
        """Get the first content component, or None."""
        return self._children[0] if self._children else None

    def get_scroll_direction(self) -> ScrollDirection:
        return self._scroll_direction

    def add_theme_variants(self, *variants: ScrollerVariant):
        """Add theme variants to the scroller."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: ScrollerVariant):
        """Remove theme variants from the scroller."""
        self.remove_theme_name(*variants)
