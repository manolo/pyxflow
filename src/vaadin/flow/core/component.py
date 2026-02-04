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
