"""Component - base class for UI components."""

from typing import TYPE_CHECKING

from vaadin.flow.core.element import Element

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class Component:
    """Base class for all UI components."""

    _tag: str = "div"

    def __init__(self):
        self._element: Element | None = None
        self._parent: "Component | None" = None
        self._ui: "UI | None" = None
        self._visible: bool = True
        self._enabled: bool = True
        self._class_names: set[str] = set()

    @property
    def element(self) -> Element:
        """Get the component's element."""
        if self._element is None:
            raise RuntimeError("Component not attached to a UI")
        return self._element

    def _create_element(self, tree: "StateTree") -> Element:
        """Create the element for this component."""
        return Element(self._tag, tree)

    def _attach(self, tree: "StateTree"):
        """Attach the component to a state tree."""
        self._element = self._create_element(tree)
        # Register component for property sync
        tree.register_component(self)

    def get_element(self) -> Element:
        """Get the element (public API)."""
        return self.element

    def _sync_property(self, name: str, value):
        """Called when a property is synced from client.

        Subclasses can override to handle specific properties.
        """
        pass

    # Visibility methods

    def is_visible(self) -> bool:
        """Check if the component is visible."""
        return self._visible

    def set_visible(self, visible: bool):
        """Set the visibility of the component.

        When a component is set to invisible, it is not rendered on the page.
        """
        self._visible = visible
        if self._element:
            self.element.get_style().set("display", "" if visible else "none")

    # Enabled methods

    def is_enabled(self) -> bool:
        """Check if the component is enabled."""
        return self._enabled

    def set_enabled(self, enabled: bool):
        """Set the enabled state of the component.

        When a component is disabled, it cannot receive user input.
        """
        self._enabled = enabled
        if self._element:
            # Most Vaadin components use the 'disabled' attribute
            if enabled:
                self.element.remove_attribute("disabled")
            else:
                self.element.set_attribute("disabled", "")

    # Class name methods

    def add_class_name(self, *class_names: str):
        """Add one or more CSS class names to the component."""
        for class_name in class_names:
            self._class_names.add(class_name)
        self._update_class_attribute()

    def remove_class_name(self, *class_names: str):
        """Remove one or more CSS class names from the component."""
        for class_name in class_names:
            self._class_names.discard(class_name)
        self._update_class_attribute()

    def has_class_name(self, class_name: str) -> bool:
        """Check if the component has a specific CSS class name."""
        return class_name in self._class_names

    def get_class_names(self) -> set[str]:
        """Get all CSS class names of the component."""
        return self._class_names.copy()

    def set_class_name(self, class_name: str, add: bool = True):
        """Add or remove a CSS class name.

        Args:
            class_name: The class name to add or remove
            add: If True, adds the class; if False, removes it
        """
        if add:
            self.add_class_name(class_name)
        else:
            self.remove_class_name(class_name)

    def _update_class_attribute(self):
        """Update the class attribute on the element."""
        if self._element:
            if self._class_names:
                self.element.set_attribute("class", " ".join(sorted(self._class_names)))
            else:
                self.element.remove_attribute("class")


class UI:
    """The root UI component."""

    def __init__(self, tree: "StateTree"):
        self._tree = tree
        self._root: Component | None = None

    @property
    def tree(self) -> "StateTree":
        return self._tree

    def set_content(self, component: Component):
        """Set the root content."""
        self._root = component
        component._ui = self
        component._attach(self._tree)
