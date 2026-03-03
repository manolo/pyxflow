"""Button component."""

from typing import Callable, TYPE_CHECKING

from pyxflow.core.component import Component
from pyxflow.core.state_node import Feature
from pyxflow.components.constants import ButtonVariant

if TYPE_CHECKING:
    from pyxflow.components.icon import Icon
    from pyxflow.core.state_tree import StateTree


class Button(Component):
    """A button component."""

    _v_fqcn = "com.vaadin.flow.component.button.Button"
    _tag = "vaadin-button"

    def __init__(self, text: "str | Icon | Callable | None" = "", on_click: "Callable | Icon | None" = None, icon: "Icon | None" = None):
        super().__init__()
        # Smart parameter detection: Button(Icon(...)), Button(lambda e: ...), etc.
        if text is not None and isinstance(text, Component):
            icon = icon or (on_click if isinstance(on_click, Component) else None)
            if not icon:
                icon = text  # type: ignore[assignment]
            on_click = on_click if callable(on_click) else None
            text = ""
        elif callable(text):
            on_click = text  # type: ignore[assignment]
            text = ""
        if on_click is not None and isinstance(on_click, Component):
            icon = on_click  # type: ignore[assignment]
            on_click = None
        self._text = text
        self._icon_component: "Icon | None" = icon
        self._click_listeners: list[Callable] = []
        self._text_node = None
        self._icon_after_text = False
        self._disable_on_click = False
        if on_click:
            self._click_listeners.append(on_click)

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        # Text node first (clear_children inside), then icon — otherwise clear erases the icon
        if self._text:
            self._create_text_node(tree, self._text)
        if self._icon_component:
            self._attach_icon(tree, self._icon_component)
            if not self._text:
                self.add_theme_name("icon")
        if self._disable_on_click:
            self.element.set_property("disableOnClick", True)
        # Register click listener
        self.element.add_event_listener("click", self._handle_click)

    def _create_text_node(self, tree: "StateTree", text: str):
        """Create text node child for button text."""
        self._text_node = tree.create_node()
        self._text_node.attach()
        self._text_node.put(Feature.TEXT_NODE, "text", text)
        # Emit clear before first splice (matches Java Flow behavior)
        self.element.node.clear_children()
        self.element.node.add_child(self._text_node)

    def _attach_icon(self, tree: "StateTree", icon: "Icon"):
        """Attach an icon component as prefix child."""
        icon._ui = self._ui
        icon._parent = self
        icon._attach(tree)
        slot = "suffix" if self._icon_after_text else "prefix"
        icon.element.set_attribute("slot", slot)
        self.element.add_child(icon.element)

    def set_icon(self, icon: "Icon"):
        """Set the button icon (prefix slot)."""
        self._icon_component = icon
        if self._element:
            self._attach_icon(self._element._tree, icon)

    def set_icon_after_text(self, after: bool):
        """Place the icon after the text (suffix slot) instead of before (prefix)."""
        self._icon_after_text = after
        if self._icon_component and self._icon_component._element:
            slot = "suffix" if after else "prefix"
            self._icon_component.element.set_attribute("slot", slot)

    def is_icon_after_text(self) -> bool:
        return self._icon_after_text

    def set_text(self, text: str):
        """Set the button text."""
        self._text = text
        if self._text_node:
            self._text_node.put(Feature.TEXT_NODE, "text", text)

    def get_text(self) -> str:
        """Get the button text."""
        return self._text

    def add_click_listener(self, listener: Callable):
        """Add a click listener."""
        self._click_listeners.append(listener)

    def set_disable_on_click(self, disable: bool):
        """Set whether the button disables itself when clicked.

        When enabled, the button is immediately disabled on the client
        before the click event is sent to the server, preventing
        double-click issues.
        """
        self._disable_on_click = disable
        if self._element:
            self.element.set_property("disableOnClick", disable)

    def is_disable_on_click(self) -> bool:
        """Check if the button disables itself when clicked."""
        return self._disable_on_click

    def set_autofocus(self, autofocus: bool):
        """Set whether the button should auto-focus on page load."""
        self._autofocus = autofocus
        if self._element:
            if autofocus:
                self.element.set_attribute("autofocus", "")
            else:
                self.element.remove_attribute("autofocus")

    def is_autofocus(self) -> bool:
        return getattr(self, "_autofocus", False)

    def click(self):
        """Trigger a click event programmatically (server-side)."""
        self._handle_click({})

    def add_theme_variants(self, *variants: ButtonVariant):
        """Add theme variants to the button."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: ButtonVariant):
        """Remove theme variants from the button."""
        self.remove_theme_name(*variants)

    def _handle_click(self, event_data: dict):
        """Handle click event."""
        if self._disable_on_click:
            self.set_enabled(False)
        for listener in self._click_listeners:
            listener(event_data)
