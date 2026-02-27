"""MasterDetailLayout component."""

from typing import Callable, TYPE_CHECKING

from pyflow.core.component import Component
from pyflow.core.state_node import Feature
from pyflow.components.constants import MasterDetailLayoutVariant

if TYPE_CHECKING:
    from pyflow.core.state_tree import StateTree


class MasterDetailLayout(Component):
    """A layout with master and detail areas.

    The master area shows a list/overview, and the detail area shows
    details of a selected item. The detail can overlay on small screens.

    The detail component is added as a **virtual child** (Feature 24) so
    that the web component's ``_setDetail(element, skipTransition)``
    method manages DOM placement and View Transition animation.

    Usage::

        layout = MasterDetailLayout()
        layout.set_master(grid)
        layout.set_detail(form)
    """

    _v_fqcn = "com.vaadin.flow.component.masterdetaillayout.MasterDetailLayout"
    _tag = "vaadin-master-detail-layout"

    def __init__(self):
        self._master: Component | None = None
        self._detail: Component | None = None
        self._has_initialized = False
        self._pending_detail_cmd: list | None = None
        self._virtual_children: set = set()  # track components added as virtual children

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        # Default overlay mode = drawer (Java constructor does setOverlayMode(DRAWER))
        self.element.set_property("stackOverlay", False)

        if self._master:
            self._attach_master(self._master, tree)
        if self._detail:
            self._add_virtual_child(self._detail, tree)
            self._virtual_children.add(id(self._detail))
        self._update_details()
        self._has_initialized = True

        # If detail was pre-set (e.g., in before_enter which runs before _attach),
        # re-queue _setDetail now that _has_initialized=True so animation is enabled.
        # The dedup in _update_details() cancels the previous skipTransition=true command.
        if self._detail:
            self._update_details()

        # Flush pending event listeners
        for listener in getattr(self, "_pending_backdrop_listeners", []):
            self.element.add_event_listener("backdrop-click", listener)
        for listener in getattr(self, "_pending_escape_listeners", []):
            self.element.add_event_listener("detail-escape-press", listener)

    def _attach_master(self, component: Component, tree: "StateTree"):
        """Attach master as regular child (Feature 2, default slot)."""
        component._ui = self._ui
        component._parent = self
        component._attach(tree)
        self.element.add_child(component.element)

    def _add_virtual_child(self, component: Component, tree: "StateTree"):
        """Add a component as a virtual child (Feature 24).

        Virtual children are tracked by the state tree but NOT placed in
        the DOM by the protocol.  The web component's ``_setDetail()``
        handles DOM placement and animation.
        """
        if not component._element:
            component._ui = self._ui
            component._parent = self
            component._attach(tree)
        # Mark as in-memory virtual child (required by FlowClient)
        component.element._node.put(
            Feature.ELEMENT_DATA, "payload", {"type": "inMemory"}
        )
        # Splice into Feature 24 of the layout
        tree.add_change({
            "node": self.element.node_id,
            "type": "splice",
            "feat": Feature.VIRTUAL_CHILDREN_LIST,
            "index": 0,
            "addNodes": [component.element.node_id],
        })

    def _remove_virtual_child_component(self, component: Component):
        """Remove a specific component from virtual children (Feature 24)."""
        if component._element:
            self._element._tree.add_change({
                "node": self.element.node_id,
                "type": "splice",
                "feat": Feature.VIRTUAL_CHILDREN_LIST,
                "index": 0,
                "remove": 1,
            })

    def _update_details(self):
        """Call the web component's _setDetail() for DOM placement and animation.

        Like Java's ``updateDetails()``, cancels any previous pending
        ``_setDetail`` command so that only the latest one is sent.
        This prevents duplicate commands (e.g. from recursive event
        handlers) from cancelling each other's View Transition animation.
        """
        tree = self._element._tree
        # Cancel previous pending command (Java: pendingDetailsUpdate.cancelExecution())
        if self._pending_detail_cmd is not None:
            try:
                tree._pending_execute.remove(self._pending_detail_cmd)
            except ValueError:
                pass  # Already collected
        self_ref = {"@v-node": self.element.node_id}
        skip_transition = not self._has_initialized
        if self._detail and self._detail._element:
            detail_ref = {"@v-node": self._detail.element.node_id}
            cmd = [
                self_ref, detail_ref, skip_transition,
                "return $0._setDetail($1, $2)"
            ]
        else:
            cmd = [
                self_ref, skip_transition,
                "return $0._setDetail(null, $1)"
            ]
        tree.queue_execute(cmd)
        self._pending_detail_cmd = cmd

    def set_master(self, component: Component):
        """Set the master (list/overview) component."""
        if self._master and self._element:
            self.element.remove_child(self._master.element)
        self._master = component
        if self._element:
            self._attach_master(component, self._element._tree)

    def get_master(self) -> Component | None:
        return self._master

    def set_detail(self, component: Component | None):
        """Set the detail component. Pass None to hide the detail area.

        The detail is added as a virtual child (Feature 24) so that
        ``_setDetail()`` can manage DOM placement with animation.
        Virtual children are kept alive (never removed from Feature 24)
        -- only ``_setDetail(null)`` hides them visually.
        """
        old = self._detail
        if component is old and self._has_initialized:
            return  # No change
        self._detail = component

        # Add new component as virtual child (only once per component)
        if self._element and component and id(component) not in self._virtual_children:
            self._add_virtual_child(component, self._element._tree)
            self._virtual_children.add(id(component))

        # Remove old component from virtual children only if replacing with a different non-None one
        if old and component and old is not component and self._element and old._element and id(old) in self._virtual_children:
            self._remove_virtual_child_component(old)
            self._virtual_children.discard(id(old))

        if self._element:
            self._update_details()

    def get_detail(self) -> Component | None:
        return self._detail

    def set_animation_enabled(self, enabled: bool):
        """Set whether layout animation is enabled."""
        if self._element:
            self.element.set_property("noAnimation", not enabled)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["noAnimation"] = not enabled

    def is_animation_enabled(self) -> bool:
        """Check if layout animation is enabled (default: True)."""
        if self._element:
            return not self.element.node.get(
                Feature.ELEMENT_PROPERTY_MAP, "noAnimation", False
            )
        pending = getattr(self, "_pending_properties", {})
        return not pending.get("noAnimation", False)

    def set_overlay_mode(self, mode: str):
        """Set the overlay mode ('drawer' or 'stack')."""
        stack = mode == "stack"
        if self._element:
            self.element.set_property("stackOverlay", stack)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["stackOverlay"] = stack

    def set_force_overlay(self, force: bool):
        """Set whether overlay mode is enforced."""
        if self._element:
            self.element.set_property("forceOverlay", force)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["forceOverlay"] = force

    def set_detail_size(self, size: str):
        """Set the detail area size (e.g., '400px', '250px')."""
        if self._element:
            self.element.set_property("detailSize", size)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["detailSize"] = size

    def set_master_min_size(self, size: str):
        """Set the minimum master area size (e.g., '450px')."""
        if self._element:
            self.element.set_property("masterMinSize", size)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["masterMinSize"] = size

    def get_detail_size(self) -> str | None:
        """Get the detail area size."""
        if self._element:
            return self.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "detailSize", None)
        return getattr(self, "_pending_properties", {}).get("detailSize")

    def get_master_min_size(self) -> str | None:
        """Get the minimum master area size."""
        if self._element:
            return self.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "masterMinSize", None)
        return getattr(self, "_pending_properties", {}).get("masterMinSize")

    def set_detail_min_size(self, size: str):
        """Set the minimum detail area size (e.g., '200px')."""
        if self._element:
            self.element.set_property("detailMinSize", size)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["detailMinSize"] = size

    def set_orientation(self, orientation: str):
        """Set orientation ('horizontal' or 'vertical')."""
        if self._element:
            self.element.set_property("orientation", orientation)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["orientation"] = orientation

    def get_orientation(self) -> str:
        """Get orientation (default: 'horizontal')."""
        if self._element:
            return self.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "orientation", "horizontal")
        return getattr(self, "_pending_properties", {}).get("orientation", "horizontal")

    def set_containment(self, containment: str):
        """Set containment mode ('layout' or 'viewport')."""
        if self._element:
            self.element.set_property("containment", containment)
        else:
            if not hasattr(self, "_pending_properties"):
                self._pending_properties = {}
            self._pending_properties["containment"] = containment

    def add_backdrop_click_listener(self, listener: Callable):
        """Add a listener for backdrop click events (when overlay detail is dismissed)."""
        if self._element:
            self.element.add_event_listener("backdrop-click", listener)
        else:
            if not hasattr(self, "_pending_backdrop_listeners"):
                self._pending_backdrop_listeners: list[Callable] = []
            self._pending_backdrop_listeners.append(listener)

    def add_detail_escape_press_listener(self, listener: Callable):
        """Add a listener for Escape key press in the detail area."""
        if self._element:
            self.element.add_event_listener("detail-escape-press", listener)
        else:
            if not hasattr(self, "_pending_escape_listeners"):
                self._pending_escape_listeners: list[Callable] = []
            self._pending_escape_listeners.append(listener)

    def add_theme_variants(self, *variants: MasterDetailLayoutVariant):
        """Add theme variants to the master detail layout."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: MasterDetailLayoutVariant):
        """Remove theme variants from the master detail layout."""
        self.remove_theme_name(*variants)
