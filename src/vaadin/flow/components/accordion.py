"""Accordion component — vertically stacked expandable panels."""

from typing import Callable, TYPE_CHECKING

from vaadin.flow.components.details import Details
from vaadin.flow.core.component import Component

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class AccordionPanel(Details):
    """A panel within an Accordion. Extends Details."""
    pass


class Accordion(Component):
    """A vertically stacked set of expandable panels.

    Only one panel can be expanded at a time.
    """

    _tag = "vaadin-accordion"

    def __init__(self):
        super().__init__()
        self._panels: list[AccordionPanel] = []
        self._opened_index: int | None = None
        self._change_listeners: list[Callable] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        for panel in self._panels:
            panel._ui = self._ui
            panel._parent = self
            panel._attach(tree)
            self.element.add_child(panel.element)

        if self._opened_index is not None:
            self.element.set_property("opened", self._opened_index)

        self.element.add_event_listener("opened-changed", self._handle_opened_changed)

    def add(self, summary, content: Component) -> AccordionPanel:
        """Add a panel with a summary and content.

        Args:
            summary: Panel summary (string or Component)
            content: Panel content component

        Returns:
            The created AccordionPanel.
        """
        panel = AccordionPanel(summary, content)
        self._panels.append(panel)
        if self._element:
            panel._ui = self._ui
            panel._parent = self
            panel._attach(self._element._tree)
            self.element.add_child(panel.element)
        return panel

    def open(self, index: int):
        """Open the panel at the given index."""
        self._opened_index = index
        if self._element:
            self.element.set_property("opened", index)

    def close(self):
        """Close all panels."""
        self._opened_index = None
        if self._element:
            self.element.set_property("opened", None)

    def get_opened_index(self) -> int | None:
        return self._opened_index

    def get_opened_panel(self) -> AccordionPanel | None:
        if self._opened_index is not None and 0 <= self._opened_index < len(self._panels):
            return self._panels[self._opened_index]
        return None

    def get_panels(self) -> list[AccordionPanel]:
        return self._panels.copy()

    def add_opened_change_listener(self, listener: Callable):
        self._change_listeners.append(listener)

    def _handle_opened_changed(self, event_data: dict):
        pass

    def _sync_property(self, name: str, value):
        if name == "opened":
            old = self._opened_index
            self._opened_index = int(value) if value is not None else None
            if old != self._opened_index:
                for listener in self._change_listeners:
                    listener({"openedIndex": self._opened_index})
