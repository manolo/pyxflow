"""Popover component."""

from enum import Enum
from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class PopoverPosition(str, Enum):
    BOTTOM = "bottom"
    BOTTOM_START = "bottom-start"
    BOTTOM_END = "bottom-end"
    TOP = "top"
    TOP_START = "top-start"
    TOP_END = "top-end"
    START = "start"
    START_TOP = "start-top"
    START_BOTTOM = "start-bottom"
    END = "end"
    END_TOP = "end-top"
    END_BOTTOM = "end-bottom"


class Popover(Component):
    """A popover overlay component anchored to a target element.

    Children are added as regular DOM children. The web component
    projects them into its overlay automatically.

    Target is set via executeJs to pass a direct element reference.

    Usage::

        popover = Popover()
        popover.set_target(button)
        popover.add(Span("Popover content"))
        popover.set_position(PopoverPosition.BOTTOM)
    """

    _v_fqcn = "com.vaadin.flow.component.popover.Popover"
    _tag = "vaadin-popover"

    def __init__(self):
        super().__init__()
        self._children: list[Component] = []
        self._target: Component | None = None
        self._position: PopoverPosition = PopoverPosition.BOTTOM
        self._opened = False
        self._modal = False
        self._open_on_click = True
        self._open_on_hover = False
        self._open_on_focus = False
        self._close_on_esc = True
        self._close_on_outside_click = True
        self._open_listeners: list[Callable] = []
        self._close_listeners: list[Callable] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        # Set initial properties
        self.element.set_property("position", self._position.value)
        if self._modal:
            self.element.set_property("modal", True)

        # Trigger: build JSON array from open_on_* flags
        self._apply_trigger()

        # Close behavior (inverted properties on the web component)
        if not self._close_on_esc:
            self.element.set_property("noCloseOnEsc", True)
        if not self._close_on_outside_click:
            self.element.set_property("noCloseOnOutsideClick", True)

        # Set target via executeJs (direct element reference)
        if self._target:
            self._apply_target(tree)

        # Attach children as regular children (web component slots them into overlay)
        for child in self._children:
            child._ui = self._ui
            child._parent = self
            child._attach(tree)
            self.element.add_child(child.element)

        # Register opened-changed listener for bidirectional sync
        self.element.add_event_listener("opened-changed", self._handle_opened_changed)

    def _apply_trigger(self):
        """Set the trigger property as a JSON array."""
        if not self._element:
            return
        triggers = []
        if self._open_on_click:
            triggers.append("click")
        if self._open_on_hover:
            triggers.append("hover")
        if self._open_on_focus:
            triggers.append("focus")
        self.element.set_property("trigger", triggers)

    def _apply_target(self, tree: "StateTree" = None):
        """Set the target via executeJs for a direct element reference."""
        if not self._target or not self._element:
            return
        if not self._target._element:
            return
        t = tree or self._element._tree
        t.queue_execute([
            {"@v-node": self.element.node_id},
            {"@v-node": self._target.element.node_id},
            "return (function() { $0.target = $1 }).apply(null)",
        ])

    def set_target(self, component: Component):
        """Set the target component the popover is anchored to."""
        self._target = component
        if self._element:
            self._apply_target()

    def get_target(self) -> Component | None:
        return self._target

    def add(self, *components: Component):
        """Add components to the popover content."""
        for component in components:
            self._children.append(component)
            if self._element:
                component._ui = self._ui
                component._parent = self
                component._attach(self._element._tree)
                self.element.add_child(component.element)

    def remove_all(self):
        """Remove all components from the popover."""
        if self._element:
            for child in self._children:
                if child._element:
                    self.element.remove_child(child.element)
        for child in self._children:
            child._parent = None
        self._children.clear()

    def open(self):
        """Open the popover."""
        self._opened = True
        if self._element:
            self.element.set_property("opened", True)
        for listener in self._open_listeners:
            listener({})

    def close(self):
        """Close the popover."""
        self._opened = False
        if self._element:
            self.element.set_property("opened", False)

    def is_opened(self) -> bool:
        return self._opened

    def set_opened(self, opened: bool):
        if opened:
            self.open()
        else:
            self.close()

    def set_position(self, position: PopoverPosition):
        """Set the popover position relative to the target."""
        self._position = position
        if self._element:
            self.element.set_property("position", position.value)

    def get_position(self) -> PopoverPosition:
        return self._position

    def set_modal(self, modal: bool):
        """Set whether the popover is modal."""
        self._modal = modal
        if self._element:
            self.element.set_property("modal", modal)

    def is_modal(self) -> bool:
        return self._modal

    def set_open_on_click(self, enabled: bool):
        """Set whether the popover opens on click."""
        self._open_on_click = enabled
        if self._element:
            self._apply_trigger()

    def is_open_on_click(self) -> bool:
        return self._open_on_click

    def set_open_on_hover(self, enabled: bool):
        """Set whether the popover opens on hover."""
        self._open_on_hover = enabled
        if self._element:
            self._apply_trigger()

    def is_open_on_hover(self) -> bool:
        return self._open_on_hover

    def set_open_on_focus(self, enabled: bool):
        """Set whether the popover opens on focus."""
        self._open_on_focus = enabled
        if self._element:
            self._apply_trigger()

    def is_open_on_focus(self) -> bool:
        return self._open_on_focus

    def set_close_on_esc(self, enabled: bool):
        """Set whether the popover closes on Escape key."""
        self._close_on_esc = enabled
        if self._element:
            self.element.set_property("noCloseOnEsc", not enabled)

    def is_close_on_esc(self) -> bool:
        return self._close_on_esc

    def set_close_on_outside_click(self, enabled: bool):
        """Set whether the popover closes on outside click."""
        self._close_on_outside_click = enabled
        if self._element:
            self.element.set_property("noCloseOnOutsideClick", not enabled)

    def is_close_on_outside_click(self) -> bool:
        return self._close_on_outside_click

    def add_open_listener(self, listener: Callable):
        """Add a listener for when the popover opens."""
        self._open_listeners.append(listener)

    def add_close_listener(self, listener: Callable):
        """Add a listener for when the popover closes."""
        self._close_listeners.append(listener)

    def remove(self, *components: Component):
        """Remove specific components from the popover."""
        for component in components:
            if component in self._children:
                self._children.remove(component)
                component._parent = None
                if self._element and component._element:
                    self.element.remove_child(component.element)

    def set_autofocus(self, autofocus: bool):
        """Set whether to auto-focus the first focusable element."""
        if self._element:
            self.element.set_property("autofocus", autofocus)

    def set_backdrop_visible(self, visible: bool):
        """Set whether the backdrop is visible when modal."""
        if self._element:
            self.element.set_property("withBackdrop", visible)

    def set_hover_delay(self, delay: int):
        """Set hover delay in milliseconds."""
        if self._element:
            self.element.set_property("hoverDelay", delay)

    def set_focus_delay(self, delay: int):
        """Set focus delay in milliseconds."""
        if self._element:
            self.element.set_property("focusDelay", delay)

    def set_hide_delay(self, delay: int):
        """Set hide delay in milliseconds."""
        if self._element:
            self.element.set_property("hideDelay", delay)

    def _handle_opened_changed(self, event_data: dict):
        """Handle opened-changed event from client.

        This is intentionally a no-op. State sync is handled by
        _sync_property("opened", value) via mSync, which receives
        the actual boolean value from the client.
        """
        pass

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "opened":
            old = self._opened
            self._opened = bool(value)
            if old != self._opened:
                if self._opened:
                    for listener in self._open_listeners:
                        listener({})
                else:
                    for listener in self._close_listeners:
                        listener({})
