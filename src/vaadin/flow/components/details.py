"""Details component — expandable panel."""

from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class Details(Component):
    """An expandable panel for showing and hiding content.

    The summary is always visible and toggles the content visibility on click.
    """

    _v_fqcn = "com.vaadin.flow.component.details.Details"
    _tag = "vaadin-details"

    def __init__(self, summary: "str | Component | None" = None, *content: Component):
        super().__init__()
        self._summary = summary  # str or Component
        self._content: list[Component] = list(content)
        self._opened = False
        self._toggle_listeners: list[Callable] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        self.element.set_property("opened", self._opened)

        # Summary: string becomes text in summary slot, Component gets slot="summary"
        if self._summary is not None:
            if isinstance(self._summary, str):
                self._attach_summary_text(tree)
            elif isinstance(self._summary, Component):
                self._attach_summary_component(tree)

        # Content children
        for child in self._content:
            child._ui = self._ui
            child._parent = self
            child._attach(tree)
            self.element.add_child(child.element)

        # opened-changed event
        self.element.add_event_listener("opened-changed", self._handle_opened_changed)

    def _attach_summary_text(self, tree: "StateTree"):
        """Attach a text summary via <vaadin-details-summary slot='summary'>."""
        summary_node = tree.create_node()
        summary_node.attach()
        summary_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-details-summary")
        summary_node.put(Feature.ELEMENT_ATTRIBUTE_MAP, "slot", "summary")
        text_node = tree.create_node()
        text_node.attach()
        text_node.put(Feature.TEXT_NODE, "text", self._summary)
        summary_node.add_child(text_node)
        self.element.node.add_child(summary_node)

    def _attach_summary_component(self, tree: "StateTree"):
        """Attach a Component as the summary."""
        assert isinstance(self._summary, Component)
        comp = self._summary
        comp._ui = self._ui
        comp._parent = self
        comp._attach(tree)
        comp.element.set_attribute("slot", "summary")
        self.element.add_child(comp.element)

    def set_summary_text(self, text: str):
        """Set the summary text."""
        self._summary = text

    def get_summary_text(self) -> str | None:
        if isinstance(self._summary, str):
            return self._summary
        return None

    def set_summary(self, summary: "str | Component | None"):
        """Set the summary (string or Component)."""
        self._summary = summary

    def set_opened(self, opened: bool):
        """Set whether the details panel is opened."""
        self._opened = opened
        if self._element:
            self.element.set_property("opened", opened)

    def is_opened(self) -> bool:
        return self._opened

    def add_content(self, *components: Component):
        """Add content components."""
        for comp in components:
            self._content.append(comp)
            if self._element:
                comp._ui = self._ui
                comp._parent = self
                comp._attach(self._element._tree)
                self.element.add_child(comp.element)

    def add_opened_change_listener(self, listener: Callable):
        """Add a listener for opened state changes."""
        self._toggle_listeners.append(listener)

    def _handle_opened_changed(self, event_data: dict):
        pass

    def _sync_property(self, name: str, value):
        if name == "opened":
            old = self._opened
            self._opened = bool(value)
            if old != self._opened:
                for listener in self._toggle_listeners:
                    listener({"opened": self._opened})
