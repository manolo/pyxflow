"""Tabs and Tab components."""

from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class Tab(Component):
    """A tab component for use within Tabs.

    Represents a single tab with a text label or child components.
    """

    _v_fqcn = "com.vaadin.flow.component.tabs.Tab"
    _tag = "vaadin-tab"

    def __init__(self, label: str = ""):
        super().__init__()
        self._label = label
        self._text_node = None
        self._selected = False

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._label:
            self._text_node = tree.create_node()
            self._text_node.attach()
            self._text_node.put(Feature.TEXT_NODE, "text", self._label)
            self.element.node.add_child(self._text_node)

    def set_label(self, label: str):
        """Set the tab label text."""
        self._label = label
        if self._text_node:
            self._text_node.put(Feature.TEXT_NODE, "text", label)

    def get_label(self) -> str:
        """Get the tab label text."""
        return self._label

    def is_selected(self) -> bool:
        """Check if this tab is selected."""
        return self._selected


class Tabs(Component):
    """A tabs component for organizing content.

    Contains Tab children and tracks the selected tab via the
    selected property (0-indexed).
    """

    _v_fqcn = "com.vaadin.flow.component.tabs.Tabs"
    _tag = "vaadin-tabs"

    def __init__(self, *tabs: Tab):
        super().__init__()
        self._tabs: list[Tab] = list(tabs)
        self._selected_index = 0 if tabs else -1
        self._change_listeners: list[Callable] = []
        self._autoselect = True
        self._orientation = "horizontal"

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        # Attach all tab children
        for tab in self._tabs:
            tab._attach(tree)
            self.element.node.add_child(tab.element.node)

        # Set selected property
        self.element.set_property("selected", self._selected_index)
        if self._orientation != "horizontal":
            self.element.set_attribute("orientation", self._orientation)

        # Update selected state on tabs
        self._update_tab_selection()

        # Register selected-changed event listener
        # This event syncs the 'selected' property from client
        self.element.add_event_listener("selected-changed", self._handle_selected_changed)

        # Register updateSelectedTab as a client-callable method (Feature 19)
        tree.add_change({
            "node": self.element.node_id,
            "type": "splice",
            "feat": Feature.CLIENT_DELEGATE_HANDLERS,
            "index": 0,
            "add": ["updateSelectedTab"]
        })

    def add(self, *tabs: Tab):
        """Add tabs to the component."""
        was_empty = len(self._tabs) == 0
        for tab in tabs:
            self._tabs.append(tab)
            if self._element:
                tab._attach(self._element._tree)
                self.element.node.add_child(tab.element.node)
        if was_empty and self._autoselect and self._tabs:
            self.set_selected_index(0)

    def remove(self, *tabs: Tab):
        """Remove tabs from the component."""
        for tab in tabs:
            if tab in self._tabs:
                idx = self._tabs.index(tab)
                self._tabs.remove(tab)
                if self._element:
                    self.element.node.remove_child(tab.element.node)
                # Adjust selected index if needed
                if idx < self._selected_index:
                    self._selected_index -= 1
                    if self._element:
                        self.element.set_property("selected", self._selected_index)
                elif idx == self._selected_index:
                    if self._autoselect and self._tabs:
                        new_idx = min(idx, len(self._tabs) - 1)
                        self.set_selected_index(new_idx)
                    else:
                        self._selected_index = -1
                        if self._element:
                            self.element.set_property("selected", -1)

    def remove_all(self):
        """Remove all tabs."""
        for tab in list(self._tabs):
            self.remove(tab)

    def get_selected_tab(self) -> Tab | None:
        """Get the currently selected tab."""
        if 0 <= self._selected_index < len(self._tabs):
            return self._tabs[self._selected_index]
        return None

    def get_selected_index(self) -> int:
        """Get the selected tab index."""
        return self._selected_index

    def set_selected_index(self, index: int):
        """Set the selected tab by index."""
        old_index = self._selected_index
        self._selected_index = index
        if self._element:
            self.element.set_property("selected", index)
        self._update_tab_selection()
        if old_index != index:
            for listener in self._change_listeners:
                listener({"selectedIndex": index, "previousIndex": old_index})

    def set_selected_tab(self, tab: Tab):
        """Set the selected tab."""
        if tab in self._tabs:
            self.set_selected_index(self._tabs.index(tab))

    def get_tab_count(self) -> int:
        """Get the number of tabs."""
        return len(self._tabs)

    def set_orientation(self, orientation: str):
        """Set the tabs orientation ('horizontal' or 'vertical')."""
        self._orientation = orientation
        if self._element:
            self.element.set_attribute("orientation", orientation)

    def get_orientation(self) -> str:
        """Get the tabs orientation."""
        return self._orientation

    def set_autoselect(self, autoselect: bool):
        """Set whether the first tab should be auto-selected."""
        self._autoselect = autoselect

    def is_autoselect(self) -> bool:
        """Check if the first tab is auto-selected."""
        return self._autoselect

    def add_selected_change_listener(self, listener: Callable):
        """Add a listener for tab selection changes."""
        self._change_listeners.append(listener)

    def _update_tab_selection(self):
        """Update the selected state on Tab children."""
        for i, tab in enumerate(self._tabs):
            tab._selected = (i == self._selected_index)

    def _handle_selected_changed(self, event_data: dict):
        """Handle selected-changed event from client."""
        # The selected property is synced via mSync, so we read it from there
        pass

    def update_selected_tab(self, changed_from_client=True):
        """Called by client via publishedEventHandler when tab selection changes.

        This is invoked by the items-changed event listener on the web component
        which calls this.$server.updateSelectedTab(true).
        The selected property should already be synced via mSync before this call.
        """
        self._update_tab_selection()

    def _sync_property(self, name: str, value):
        """Handle property sync from client."""
        if name == "selected":
            old_index = self._selected_index
            self._selected_index = int(value) if value is not None else -1
            self._update_tab_selection()
            if old_index != self._selected_index:
                for listener in self._change_listeners:
                    listener({"selectedIndex": self._selected_index, "previousIndex": old_index})
