"""AppLayout component."""

from typing import TYPE_CHECKING

from vaadin.flow.components.constants import AppLayoutSection
from vaadin.flow.core.component import Component

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class AppLayout(Component):
    """Application layout with navbar, drawer, and content areas.

    Usage:
        layout = AppLayout()
        layout.add_to_navbar(DrawerToggle(), H1("My App"))
        layout.add_to_drawer(side_nav)
        layout.set_content(view)

    Also serves as a RouterLayout — the router calls show_router_layout_content()
    to swap the content area on navigation.
    """

    _v_fqcn = "com.vaadin.flow.component.applayout.AppLayout"
    _tag = "vaadin-app-layout"
    _is_router_layout = True

    Section = AppLayoutSection

    def __init__(self):
        super().__init__()
        self._navbar_components: list[Component] = []
        self._drawer_components: list[Component] = []
        self._content: Component | None = None
        self._primary_section: AppLayoutSection = AppLayoutSection.NAVBAR
        self._drawer_opened = True

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        self.element.set_property("drawerOpened", self._drawer_opened)
        if self._primary_section != AppLayoutSection.NAVBAR:
            self.element.set_property("primarySection", self._primary_section.value)
        for comp in self._navbar_components:
            self._attach_slotted(comp, "navbar", tree)
        for comp in self._drawer_components:
            self._attach_slotted(comp, "drawer", tree)
        if self._content:
            self._attach_content(self._content, tree)

    def _attach_slotted(self, component: Component, slot: str, tree: "StateTree"):
        component._ui = self._ui
        component._parent = self
        component._attach(tree)
        component.element.set_attribute("slot", slot)
        self.element.add_child(component.element)

    def _attach_content(self, component: Component, tree: "StateTree"):
        component._ui = self._ui
        component._parent = self
        if not component._element:
            component._attach(tree)
        # Content children must NOT have a slot attribute
        self.element.add_child(component.element)

    def add_to_navbar(self, *components: Component):
        """Add components to the navbar area."""
        for comp in components:
            self._navbar_components.append(comp)
            if self._element:
                self._attach_slotted(comp, "navbar", self._element._tree)

    def add_to_drawer(self, *components: Component):
        """Add components to the drawer area."""
        for comp in components:
            self._drawer_components.append(comp)
            if self._element:
                self._attach_slotted(comp, "drawer", self._element._tree)

    def set_content(self, component: Component):
        """Set the content area (replaces previous content)."""
        if self._content and self._element:
            self.element.remove_child(self._content.element)
        self._content = component
        if self._element:
            self._attach_content(component, self._element._tree)

    def get_content(self) -> Component | None:
        return self._content

    def set_drawer_opened(self, opened: bool):
        """Open or close the drawer."""
        self._drawer_opened = opened
        if self._element:
            self.element.set_property("drawerOpened", opened)

    def is_drawer_opened(self) -> bool:
        """Check if the drawer is open."""
        return self._drawer_opened

    def set_primary_section(self, section: "AppLayoutSection | str"):
        """Set which section is primary (Section.NAVBAR or Section.DRAWER)."""
        if isinstance(section, str):
            section = AppLayoutSection(section)
        self._primary_section = section
        if self._element:
            self.element.set_property("primarySection", section.value)

    def get_primary_section(self) -> AppLayoutSection:
        """Get which section is primary."""
        return self._primary_section

    # --- RouterLayout interface ---

    def show_router_layout_content(self, content: Component):
        """Called by the router to set the routed view as content."""
        self.set_content(content)

    def remove_router_layout_content(self, old: Component):
        """Called by the router to remove the previous routed view."""
        if old and self._element and self._content is old:
            self.element.remove_child(old.element)
            self._content = None
