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
        self._pending_styles: dict[str, str] = {}
        self._pending_theme: str | None = None

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
        # Apply deferred styles
        if self._pending_styles:
            for name, value in self._pending_styles.items():
                self._element.get_style().set(name, value)
            self._pending_styles.clear()
        # Apply deferred theme
        if self._pending_theme is not None:
            self._element.set_attribute("theme", self._pending_theme)
            self._pending_theme = None

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

    # --- HasSize methods ---

    def _set_style(self, name: str, value: str | None):
        """Set a style property, buffering if not yet attached."""
        val = value or ""
        if self._element:
            self._element.get_style().set(name, val)
        else:
            self._pending_styles[name] = val

    def _get_style(self, name: str) -> str | None:
        """Get a style property."""
        if self._element:
            return self._element.get_style().get(name)
        return self._pending_styles.get(name)

    def set_width(self, width: str | None):
        """Set width (e.g., '100px', '50%', '10em'). None removes width."""
        self._set_style("width", width)

    def get_width(self) -> str | None:
        return self._get_style("width")

    def set_height(self, height: str | None):
        """Set height (e.g., '100px', '50%', '10em'). None removes height."""
        self._set_style("height", height)

    def get_height(self) -> str | None:
        return self._get_style("height")

    def set_min_width(self, min_width: str | None):
        self._set_style("min-width", min_width)

    def get_min_width(self) -> str | None:
        return self._get_style("min-width")

    def set_max_width(self, max_width: str | None):
        self._set_style("max-width", max_width)

    def get_max_width(self) -> str | None:
        return self._get_style("max-width")

    def set_min_height(self, min_height: str | None):
        self._set_style("min-height", min_height)

    def get_min_height(self) -> str | None:
        return self._get_style("min-height")

    def set_max_height(self, max_height: str | None):
        self._set_style("max-height", max_height)

    def get_max_height(self) -> str | None:
        return self._get_style("max-height")

    def set_size_full(self):
        """Set both width and height to 100%."""
        self.set_width("100%")
        self.set_height("100%")

    def set_width_full(self):
        """Set width to 100%."""
        self.set_width("100%")

    def set_height_full(self):
        """Set height to 100%."""
        self.set_height("100%")

    def set_size_undefined(self):
        """Remove both width and height."""
        self.set_width(None)
        self.set_height(None)

    # --- HasTheme methods ---

    def _get_theme_set(self) -> set[str]:
        """Get current theme names as a set."""
        if self._element:
            current = self._element.get_attribute("theme") or ""
        elif self._pending_theme:
            current = self._pending_theme
        else:
            current = ""
        return set(current.split()) if current else set()

    def _apply_theme_set(self, names: set[str]):
        """Apply a set of theme names."""
        value = " ".join(sorted(names)) if names else None
        if self._element:
            if value:
                self._element.set_attribute("theme", value)
            else:
                self._element.remove_attribute("theme")
        else:
            self._pending_theme = value

    def add_theme_name(self, *theme_names: str):
        """Add one or more theme names."""
        names = self._get_theme_set()
        names.update(theme_names)
        self._apply_theme_set(names)

    def remove_theme_name(self, *theme_names: str):
        """Remove one or more theme names."""
        names = self._get_theme_set()
        names -= set(theme_names)
        self._apply_theme_set(names)

    def has_theme_name(self, theme_name: str) -> bool:
        """Check if the component has a specific theme name."""
        return theme_name in self._get_theme_set()

    def get_theme_name(self) -> str | None:
        """Get theme names as space-separated string."""
        if self._element:
            return self._element.get_attribute("theme")
        return self._pending_theme

    def set_theme_name(self, theme_name: str | None):
        """Set theme names, overwriting any previous ones. None removes all."""
        if self._element:
            if theme_name:
                self._element.set_attribute("theme", theme_name)
            else:
                self._element.remove_attribute("theme")
        else:
            self._pending_theme = theme_name

    # --- HasStyle shortcut ---

    def get_style(self) -> "Style":
        """Get the inline style manager."""
        return self.element.get_style()


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
