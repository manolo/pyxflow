"""Card component."""

from typing import TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.components.constants import CardVariant as CardVariant

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class Card(Component):
    """A card component with multiple content slots.

    Slots: title, subtitle, header-prefix, header-suffix, media, footer, and default.

    Usage::

        card = Card()
        card.set_title("My Card")
        card.set_subtitle("Some details")
        card.add(Span("Card body content"))
        card.add_to_footer(Button("Action"))
    """

    _v_fqcn = "com.vaadin.flow.component.card.Card"
    _tag = "vaadin-card"

    def __init__(self, *children: Component):
        self._children: list[Component] = list(children)
        self._title: Component | str | None = None
        self._subtitle: Component | str | None = None
        self._media: Component | None = None
        self._header: Component | None = None
        self._header_prefix: Component | None = None
        self._header_suffix: Component | None = None
        self._footer_children: list[Component] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._title is not None:
            self._attach_title(tree)
        if self._subtitle is not None:
            self._attach_subtitle(tree)
        if self._media:
            self._attach_slotted(self._media, "media", tree)
        if self._header:
            self._attach_slotted(self._header, "header", tree)
        if self._header_prefix:
            self._attach_slotted(self._header_prefix, "header-prefix", tree)
        if self._header_suffix:
            self._attach_slotted(self._header_suffix, "header-suffix", tree)
        for child in self._children:
            self._attach_child(child, tree)
        for child in self._footer_children:
            self._attach_slotted(child, "footer", tree)

    def _attach_slotted(self, component: Component, slot: str, tree: "StateTree"):
        component._ui = self._ui
        component._parent = self
        component._attach(tree)
        component.element.set_attribute("slot", slot)
        self.element.add_child(component.element)

    def _attach_child(self, component: Component, tree: "StateTree"):
        component._ui = self._ui
        component._parent = self
        component._attach(tree)
        self.element.add_child(component.element)

    def _attach_title(self, tree: "StateTree"):
        if isinstance(self._title, str):
            from vaadin.flow.components.html import Div
            comp = Div(self._title)
            self._title_component = comp
        else:
            comp = self._title
            self._title_component = comp
        self._attach_slotted(comp, "title", tree)

    def _attach_subtitle(self, tree: "StateTree"):
        if isinstance(self._subtitle, str):
            from vaadin.flow.components.html import Div
            comp = Div(self._subtitle)
            self._subtitle_component = comp
        else:
            comp = self._subtitle
            self._subtitle_component = comp
        self._attach_slotted(comp, "subtitle", tree)

    def add(self, *components: Component):
        """Add components to the default (content) slot."""
        for comp in components:
            self._children.append(comp)
            if self._element:
                self._attach_child(comp, self._element._tree)

    def remove(self, *components: Component):
        """Remove specific components from the default content slot."""
        for comp in components:
            if comp in self._children:
                self._children.remove(comp)
                comp._parent = None
                if self._element and comp._element:
                    self.element.remove_child(comp.element)

    def remove_all(self):
        """Remove all components from the default content slot."""
        if self._element:
            for child in self._children:
                if child._element:
                    self.element.remove_child(child.element)
        for child in self._children:
            child._parent = None
        self._children.clear()

    def set_title(self, title: "Component | str"):
        """Set the title (slot='title'). Can be a string or a Component."""
        self._title = title
        if self._element:
            self._attach_title(self._element._tree)

    def get_title(self) -> "Component | str | None":
        return self._title

    def set_subtitle(self, subtitle: "Component | str"):
        """Set the subtitle (slot='subtitle'). Can be a string or a Component."""
        self._subtitle = subtitle
        if self._element:
            self._attach_subtitle(self._element._tree)

    def get_subtitle(self) -> "Component | str | None":
        return self._subtitle

    def set_media(self, component: Component):
        """Set the media component (slot='media')."""
        self._media = component
        if self._element:
            self._attach_slotted(component, "media", self._element._tree)

    def set_header(self, component: Component):
        """Set the header component (slot='header')."""
        self._header = component
        if self._element:
            self._attach_slotted(component, "header", self._element._tree)

    def set_header_prefix(self, component: Component):
        """Set the header prefix component (slot='header-prefix')."""
        self._header_prefix = component
        if self._element:
            self._attach_slotted(component, "header-prefix", self._element._tree)

    def set_header_suffix(self, component: Component):
        """Set the header suffix component (slot='header-suffix')."""
        self._header_suffix = component
        if self._element:
            self._attach_slotted(component, "header-suffix", self._element._tree)

    def get_media(self) -> Component | None:
        """Get the media component."""
        return self._media

    def get_header(self) -> Component | None:
        """Get the header component."""
        return self._header

    def get_header_prefix(self) -> Component | None:
        """Get the header prefix component."""
        return self._header_prefix

    def get_header_suffix(self) -> Component | None:
        """Get the header suffix component."""
        return self._header_suffix

    def add_to_footer(self, *components: Component):
        """Add components to the footer slot."""
        for comp in components:
            self._footer_children.append(comp)
            if self._element:
                self._attach_slotted(comp, "footer", self._element._tree)

    def add_theme_variants(self, *variants: CardVariant):
        """Add theme variants to the card."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: CardVariant):
        """Remove theme variants from the card."""
        self.remove_theme_name(*variants)
