"""SideNav and SideNavItem components."""

from typing import TYPE_CHECKING

from pyflow.core.component import Component
from pyflow.core.element import Element
from pyflow.core.state_node import Feature
from pyflow.components.constants import SideNavVariant

if TYPE_CHECKING:
    from pyflow.core.state_tree import StateTree


class SideNavItem(Component):
    """A navigation item for SideNav.

    Usage:
        item = SideNavItem("Home", "/")
        item = SideNavItem("Home", "/", Icon("vaadin:home"))
    """

    _v_fqcn = "com.vaadin.flow.component.sidenav.SideNavItem"
    _tag = "vaadin-side-nav-item"

    def __init__(self, label: str = "", path: str | None = None, icon: Component | None = None):
        super().__init__()
        self._label = label
        self._path = path
        self._icon = icon
        self._items: list["SideNavItem"] = []
        self._text_node = None
        self._expanded = False

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._label:
            self._text_node = tree.create_node()
            self._text_node.attach()
            self._text_node.put(Feature.TEXT_NODE, "text", self._label)
            self.element.node.add_child(self._text_node)
        if self._path is not None:
            self.element.set_attribute("path", self._path)
        if self._icon:
            self._icon._attach(tree)
            self._icon.element.set_attribute("slot", "prefix")
            self.element.add_child(self._icon.element)
        if self._expanded:
            self.element.set_property("expanded", True)
        for item in self._items:
            self._attach_sub_item(item, tree)

    def _attach_sub_item(self, item: "SideNavItem", tree: "StateTree"):
        item._attach(tree)
        item.element.set_attribute("slot", "children")
        self.element.add_child(item.element)

    def add_item(self, *items: "SideNavItem"):
        """Add nested navigation items."""
        for item in items:
            self._items.append(item)
            if self._element:
                self._attach_sub_item(item, self._element._tree)

    def set_path(self, path: str):
        """Set the navigation path."""
        self._path = path
        if self._element:
            self.element.set_attribute("path", path)

    def get_path(self) -> str | None:
        return self._path

    def set_label(self, label: str):
        """Set the label text."""
        self._label = label
        if self._text_node:
            self._text_node.put(Feature.TEXT_NODE, "text", label)

    def get_label(self) -> str:
        return self._label

    def set_expanded(self, expanded: bool):
        """Expand or collapse nested items."""
        self._expanded = expanded
        if self._element:
            self.element.set_property("expanded", expanded)

    def is_expanded(self) -> bool:
        """Check if nested items are expanded."""
        return self._expanded

    def set_prefix_component(self, component: Component):
        """Set the prefix slot component (typically an Icon)."""
        self._icon = component
        if self._element:
            component._attach(self._element._tree)
            component.element.set_attribute("slot", "prefix")
            self.element.add_child(component.element)

    def set_suffix_component(self, component: Component):
        """Set the suffix slot component."""
        self._suffix = component
        if self._element:
            component._attach(self._element._tree)
            component.element.set_attribute("slot", "suffix")
            self.element.add_child(component.element)

    def get_items(self) -> list["SideNavItem"]:
        """Get nested navigation items."""
        return self._items.copy()

    def remove(self, *items: "SideNavItem"):
        """Remove specific nested items."""
        for item in items:
            if item in self._items:
                self._items.remove(item)
                if self._element and item._element:
                    self.element.remove_child(item.element)

    def remove_all(self):
        """Remove all nested items."""
        for item in list(self._items):
            self.remove(item)


class SideNav(Component):
    """Side navigation component.

    Usage:
        nav = SideNav()
        nav.set_label("Menu")
        nav.add_item(SideNavItem("Home", "/"))
    """

    _v_fqcn = "com.vaadin.flow.component.sidenav.SideNav"
    _tag = "vaadin-side-nav"

    def __init__(self):
        super().__init__()
        self._label: str | None = None
        self._label_element: Element | None = None
        self._items: list[SideNavItem] = []
        self._collapsible = False

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._label:
            self._create_label_element(tree)
        if self._collapsible:
            self.element.set_property("collapsible", True)
        for item in self._items:
            item._attach(tree)
            self.element.add_child(item.element)

    def _create_label_element(self, tree: "StateTree"):
        """Create a <span slot="label"> child for the nav label."""
        label_el = Element("span", tree)
        label_el.set_attribute("slot", "label")
        # Create text node for the label
        text_node = tree.create_node()
        text_node.attach()
        text_node.put(Feature.TEXT_NODE, "text", self._label)
        label_el.node.add_child(text_node)
        self.element.add_child(label_el)
        self._label_element = label_el

    def add_item(self, *items: SideNavItem):
        """Add navigation items."""
        for item in items:
            self._items.append(item)
            if self._element:
                item._attach(self._element._tree)
                self.element.add_child(item.element)

    def set_label(self, label: str):
        """Set the navigation label."""
        self._label = label
        if self._element and self._label_element is None:
            self._create_label_element(self._element._tree)

    def get_label(self) -> str | None:
        return self._label

    def set_collapsible(self, collapsible: bool):
        """Set whether the nav is collapsible."""
        self._collapsible = collapsible
        if self._element:
            self.element.set_property("collapsible", collapsible)

    def is_collapsible(self) -> bool:
        """Check if the nav is collapsible."""
        return self._collapsible

    def set_expanded(self, expanded: bool):
        """Set whether the nav is expanded (when collapsible)."""
        self._expanded = expanded
        if self._element:
            self.element.set_property("collapsed", not expanded)

    def is_expanded(self) -> bool:
        return getattr(self, "_expanded", True)

    def get_items(self) -> list[SideNavItem]:
        """Get all navigation items."""
        return self._items.copy()

    def remove(self, *items: SideNavItem):
        """Remove specific navigation items."""
        for item in items:
            if item in self._items:
                self._items.remove(item)
                if self._element and item._element:
                    self.element.remove_child(item.element)

    def remove_all(self):
        """Remove all navigation items."""
        for item in list(self._items):
            self.remove(item)

    def add_theme_variants(self, *variants: SideNavVariant):
        """Add theme variants to the side nav."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: SideNavVariant):
        """Remove theme variants from the side nav."""
        self.remove_theme_name(*variants)
