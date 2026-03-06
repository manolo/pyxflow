"""Drag and Drop API -- DragSource and DropTarget mixins.

Implements the same API as Java Vaadin Flow's DragSource<T> and DropTarget<T>.
Uses the dndConnector.js already present in the bundle
(window.Vaadin.Flow.dndConnector).
"""

from __future__ import annotations

import types
from typing import TYPE_CHECKING

from pyxflow.components.constants import EffectAllowed, DropEffect

if TYPE_CHECKING:
    from pyxflow.core.component import Component

_DND_UPDATE_DRAG = "window.Vaadin.Flow.dndConnector.updateDragSource($0)"
_DND_UPDATE_DROP = "window.Vaadin.Flow.dndConnector.updateDropTarget($0)"


# ---------------------------------------------------------------------------
#  Events
# ---------------------------------------------------------------------------

class DragStartEvent:
    """Fired when a drag operation starts on a DragSource component."""

    def __init__(self, source: Component):
        self.source = source

    def get_component(self) -> Component:
        return self.source

    def set_drag_data(self, data) -> None:
        """Set drag data on the source component (server-side only)."""
        self.source._drag_data = data


class DragEndEvent:
    """Fired when a drag operation ends on a DragSource component."""

    def __init__(self, source: Component, drop_effect: DropEffect | None = None):
        self.source = source
        self._drop_effect = drop_effect

    def get_component(self) -> Component:
        return self.source

    def get_drop_effect(self) -> DropEffect | None:
        return self._drop_effect

    def is_successful(self) -> bool:
        return self._drop_effect is not None and self._drop_effect != DropEffect.NONE

    def clear_drag_data(self) -> None:
        """Clear drag data on the source component."""
        self.source._drag_data = None


class DropEvent:
    """Fired when a drop occurs on a DropTarget component."""

    def __init__(self, source: Component, drag_source: Component | None = None,
                 drag_data=None):
        self.source = source
        self._drag_source = drag_source
        self._drag_data = drag_data

    def get_component(self) -> Component:
        return self.source

    def get_drag_source_component(self) -> Component | None:
        return self._drag_source

    def get_drag_data(self):
        return self._drag_data


# ---------------------------------------------------------------------------
#  DragSource mixin
# ---------------------------------------------------------------------------

# Methods to bind dynamically in configure()
_DRAG_SOURCE_METHODS = (
    'set_draggable', 'is_draggable', 'set_drag_data',
    'get_drag_data', 'set_effect_allowed', 'get_effect_allowed',
    'add_drag_start_listener', 'add_drag_end_listener',
    '_update_drag_source', '_on_dragstart', '_on_dragend',
    'set_drag_image',
)


class DragSource:
    """Mixin that makes a component draggable using HTML5 Drag and Drop.

    Can be used as a mixin (class MyComponent(Div, DragSource)) or via
    the static ``DragSource.configure(component)`` factory method.
    """

    _draggable: bool = False
    _drag_data = None
    _effect_allowed: EffectAllowed = EffectAllowed.UNINITIALIZED

    @staticmethod
    def configure(component: Component, draggable: bool = True) -> Component:
        """Configure a component as a drag source.

        Args:
            component: The component to make draggable.
            draggable: Whether the component should be draggable.

        Returns:
            The component (for chaining).
        """
        if not isinstance(component, DragSource):
            for name in _DRAG_SOURCE_METHODS:
                method = getattr(DragSource, name)
                setattr(component, name, types.MethodType(method, component))
            component._draggable = False
            component._drag_data = None
            component._effect_allowed = EffectAllowed.UNINITIALIZED
        component.set_draggable(draggable)
        return component

    def set_draggable(self, draggable: bool) -> None:
        """Set whether this component is draggable."""
        self._draggable = draggable
        if self._element is not None:
            self.element.set_property("draggable", str(draggable).lower())
            self._update_drag_source()
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["draggable"] = str(draggable).lower()
            if not hasattr(self, "_pending_dnd_drag"):
                self._pending_dnd_drag = True
        # Always register internal dragstart/dragend listeners for active
        # drag source tracking (even if user doesn't add their own listeners)
        if draggable and not getattr(self, "_dnd_tracking_registered", False):
            self._dnd_tracking_registered = True
            self.add_drag_start_listener(lambda e: None)  # ensures event registration
            self.add_drag_end_listener(lambda e: None)     # ensures event registration

    def is_draggable(self) -> bool:
        """Check if this component is draggable."""
        return self._draggable

    def set_drag_data(self, data) -> None:
        """Set server-side drag data (not sent to client)."""
        self._drag_data = data

    def get_drag_data(self):
        """Get server-side drag data."""
        return self._drag_data

    def set_effect_allowed(self, effect: EffectAllowed) -> None:
        """Set the allowed drag effects."""
        self._effect_allowed = effect
        if self._element is not None:
            self.element.set_property("__effectAllowed", effect.value)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["__effectAllowed"] = effect.value

    def get_effect_allowed(self) -> EffectAllowed:
        """Get the allowed drag effects."""
        return self._effect_allowed

    def add_drag_start_listener(self, listener) -> None:
        """Add a listener for drag start events."""
        if not hasattr(self, "_drag_start_listeners"):
            self._drag_start_listeners = []
        self._drag_start_listeners.append(listener)
        if self._element is not None and not getattr(self, "_dragstart_event_registered", False):
            self._dragstart_event_registered = True
            from pyxflow.server.uidl_handler import _DRAGSTART_HASH
            self._element.add_event_listener(
                "dragstart", self._on_dragstart, hash_key=_DRAGSTART_HASH)

    def _on_dragstart(self, event_data: dict) -> None:
        """Internal dragstart event handler."""
        # Track active drag source on the UI
        ui = self.get_ui()
        if ui:
            ui._active_drag_source = self

        event = DragStartEvent(self)
        for listener in getattr(self, "_drag_start_listeners", []):
            listener(event)

    def add_drag_end_listener(self, listener) -> None:
        """Add a listener for drag end events."""
        if not hasattr(self, "_drag_end_listeners"):
            self._drag_end_listeners = []
        self._drag_end_listeners.append(listener)
        if self._element is not None and not getattr(self, "_dragend_event_registered", False):
            self._dragend_event_registered = True
            from pyxflow.server.uidl_handler import _DRAGEND_HASH
            self._element.add_event_listener(
                "dragend", self._on_dragend, hash_key=_DRAGEND_HASH)

    def _on_dragend(self, event_data: dict) -> None:
        """Internal dragend event handler."""
        # Clear active drag source on the UI
        ui = self.get_ui()
        if ui:
            ui._active_drag_source = None

        drop_effect_str = event_data.get("event.dataTransfer.dropEffect")
        drop_effect = None
        if drop_effect_str:
            try:
                drop_effect = DropEffect(drop_effect_str)
            except ValueError:
                pass
        event = DragEndEvent(self, drop_effect)
        for listener in getattr(self, "_drag_end_listeners", []):
            listener(event)

    def _update_drag_source(self) -> None:
        """Call the JS connector to update drag source state."""
        self.execute_js(_DND_UPDATE_DRAG)

    def set_drag_image(self, image_component: "Component",
                       offset_x: int = 0, offset_y: int = 0) -> None:
        """Set a custom drag image shown during drag.

        The dndConnector in the bundle reads __dragImage, __dragImageOffsetX,
        and __dragImageOffsetY from the drag source element and calls
        ``e.dataTransfer.setDragImage()`` during dragstart.

        Args:
            image_component: A component whose element is used as the drag
                ghost image. It must be in the DOM (e.g. added to a layout,
                even if positioned off-screen).
            offset_x: Horizontal offset of the cursor within the drag image.
            offset_y: Vertical offset of the cursor within the drag image.
        """
        # Both this component and image_component must be attached for the
        # element references to exist. Buffer if not yet attached.
        if self._element is not None and image_component._element is not None:
            self._element.execute_js(
                "window.Vaadin.Flow.dndConnector.setDragImage($1, $2, $3, $0)",
                image_component._element, offset_x, offset_y,
            )
        else:
            # Buffer for execution after attach
            self._pending_drag_image = (image_component, offset_x, offset_y)


# ---------------------------------------------------------------------------
#  DropTarget mixin
# ---------------------------------------------------------------------------

# Methods to bind dynamically in configure()
_DROP_TARGET_METHODS = (
    'set_active', 'is_active', 'set_drop_effect',
    'get_drop_effect', 'add_drop_listener',
    '_update_drop_target', '_on_drop',
)


class DropTarget:
    """Mixin that makes a component a drop target for HTML5 Drag and Drop.

    Can be used as a mixin (class MyComponent(Div, DropTarget)) or via
    the static ``DropTarget.configure(component)`` factory method.
    """

    _drop_active: bool = False
    _drop_effect: DropEffect | None = None

    @staticmethod
    def configure(component: Component, active: bool = True) -> Component:
        """Configure a component as a drop target.

        Args:
            component: The component to make a drop target.
            active: Whether the drop target should be active.

        Returns:
            The component (for chaining).
        """
        if not isinstance(component, DropTarget):
            for name in _DROP_TARGET_METHODS:
                method = getattr(DropTarget, name)
                setattr(component, name, types.MethodType(method, component))
            component._drop_active = False
            component._drop_effect = None
        component.set_active(active)
        return component

    def set_active(self, active: bool) -> None:
        """Set whether this drop target is active."""
        self._drop_active = active
        if self._element is not None:
            self.element.set_property("__active", active)
            self._update_drop_target()
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["__active"] = active
            if not hasattr(self, "_pending_dnd_drop"):
                self._pending_dnd_drop = True

    def is_active(self) -> bool:
        """Check if this drop target is active."""
        return self._drop_active

    def set_drop_effect(self, effect: DropEffect) -> None:
        """Set the drop effect."""
        self._drop_effect = effect
        if self._element is not None:
            self.element.set_property("__dropEffect", effect.value)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["__dropEffect"] = effect.value

    def get_drop_effect(self) -> DropEffect | None:
        """Get the drop effect."""
        return self._drop_effect

    def add_drop_listener(self, listener) -> None:
        """Add a listener for drop events."""
        if not hasattr(self, "_drop_listeners"):
            self._drop_listeners = []
        self._drop_listeners.append(listener)
        if self._element is not None and not getattr(self, "_drop_event_registered", False):
            self._drop_event_registered = True
            from pyxflow.server.uidl_handler import _DROP_HASH
            self._element.add_event_listener(
                "drop", self._on_drop, hash_key=_DROP_HASH)

    def _on_drop(self, event_data: dict) -> None:
        """Internal drop event handler."""
        ui = self.get_ui()
        drag_source = getattr(ui, "_active_drag_source", None) if ui else None
        drag_data = getattr(drag_source, "_drag_data", None) if drag_source else None

        event = DropEvent(self, drag_source=drag_source, drag_data=drag_data)
        for listener in getattr(self, "_drop_listeners", []):
            listener(event)

        # Clear active drag source after drop
        if ui and hasattr(ui, "_active_drag_source"):
            ui._active_drag_source = None

    def _update_drop_target(self) -> None:
        """Call the JS connector to update drop target state."""
        self.execute_js(_DND_UPDATE_DROP)
