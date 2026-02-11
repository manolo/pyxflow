"""MasterDetailLayout component."""

from typing import TYPE_CHECKING

from vaadin.flow.core.component import Component

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class MasterDetailLayout(Component):
    """A layout with master and detail areas.

    The master area shows a list/overview, and the detail area shows
    details of a selected item. The detail can overlay on small screens.

    Usage::

        layout = MasterDetailLayout()
        layout.set_master(grid)
        layout.set_detail(form)
    """

    _tag = "vaadin-master-detail-layout"

    def __init__(self):
        self._master: Component | None = None
        self._detail: Component | None = None
        self._has_initialized = False

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._master:
            self._attach_child(self._master, tree)
        if self._detail:
            self._attach_child(self._detail, tree, slot="detail")
            self._call_set_detail(skip_transition=True)
        self._has_initialized = True

    def _attach_child(self, component: Component, tree: "StateTree", slot: str | None = None):
        component._ui = self._ui
        component._parent = self
        component._attach(tree)
        if slot:
            component.element.set_attribute("slot", slot)
        self.element.add_child(component.element)

    def set_master(self, component: Component):
        """Set the master (list/overview) component."""
        if self._master and self._element:
            self.element.remove_child(self._master.element)
        self._master = component
        if self._element:
            self._attach_child(component, self._element._tree)

    def get_master(self) -> Component | None:
        return self._master

    def set_detail(self, component: Component | None):
        """Set the detail component. Pass None to hide the detail area."""
        if self._detail and self._element:
            self.element.remove_child(self._detail.element)
        self._detail = component
        if self._element and component:
            if component._element:
                # Already attached — just re-add as child
                self.element.add_child(component.element)
            else:
                self._attach_child(component, self._element._tree, slot="detail")
        if self._element:
            self._call_set_detail(skip_transition=not self._has_initialized)

    def _call_set_detail(self, skip_transition: bool = False):
        """Call the web component's _setDetail() for animation."""
        tree = self._element._tree
        self_ref = {"@v-node": self.element.node_id}
        if self._detail and self._detail._element:
            detail_ref = {"@v-node": self._detail.element.node_id}
            tree.queue_execute([
                self_ref, detail_ref, skip_transition,
                "return $0._setDetail($1, $2)"
            ])
        else:
            tree.queue_execute([
                self_ref, skip_transition,
                "return $0._setDetail(null, $1)"
            ])

    def get_detail(self) -> Component | None:
        return self._detail

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
