"""TabSheet component."""

import uuid
from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.components.tabs import Tab, Tabs

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class TabSheet(Component):
    """A tab sheet component that combines tabs with content panels.

    Wraps a Tabs component in the 'tabs' slot and associates each tab
    with a content component.
    """

    _v_fqcn = "com.vaadin.flow.component.tabs.TabSheet"
    _tag = "vaadin-tabsheet"

    def __init__(self):
        super().__init__()
        self._tabs_component = Tabs()
        self._tab_to_content: dict[Tab, Component] = {}
        self._tab_ids: dict[Tab, str] = {}
        self._change_listeners: list[Callable] = []

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        # Attach Tabs component and put it in the "tabs" slot
        self._tabs_component._attach(tree)
        self._tabs_component.element.set_attribute("slot", "tabs")
        self.element.node.add_child(self._tabs_component.element.node)

        # Attach all content panels and set tab/content ID links
        for tab, content in self._tab_to_content.items():
            tab_id = self._tab_ids[tab]
            # Set the tab's ID so the web component can associate tab ↔ content
            tab.element.set_attribute("id", tab_id)
            content._attach(tree)
            content.element.set_attribute("tab", tab_id)
            self.element.node.add_child(content.element.node)

        # Forward selection change events
        self._tabs_component.add_selected_change_listener(self._on_tab_selected)

    def add(self, label_or_tab, content: Component) -> Tab:
        """Add a tab with content.

        Args:
            label_or_tab: Either a string label or a Tab instance.
            content: The content component for this tab.

        Returns:
            The Tab instance.
        """
        if isinstance(label_or_tab, str):
            tab = Tab(label_or_tab)
        else:
            tab = label_or_tab

        # Generate a unique ID to link tab and content
        tab_id = f"tabsheet-tab-{uuid.uuid4().hex[:8]}"
        self._tab_ids[tab] = tab_id
        self._tab_to_content[tab] = content

        # Add tab to internal Tabs component
        self._tabs_component.add(tab)

        if self._element:
            # Attach content and set linking attribute
            content._attach(self._element._tree)
            content.element.set_attribute("tab", tab_id)
            self.element.node.add_child(content.element.node)

        # Set the tab's ID so the web component can associate them
        if tab._element:
            tab.element.set_attribute("id", tab_id)

        return tab

    def remove(self, tab: Tab):
        """Remove a tab and its content."""
        if tab in self._tab_to_content:
            content = self._tab_to_content.pop(tab)
            self._tab_ids.pop(tab, None)
            self._tabs_component.remove(tab)
            if self._element and content._element:
                self.element.node.remove_child(content.element.node)

    def get_selected_tab(self) -> Tab | None:
        """Get the currently selected tab."""
        return self._tabs_component.get_selected_tab()

    def set_selected_tab(self, tab: Tab):
        """Set the selected tab."""
        self._tabs_component.set_selected_tab(tab)

    def get_selected_index(self) -> int:
        """Get the selected tab index."""
        return self._tabs_component.get_selected_index()

    def set_selected_index(self, index: int):
        """Set the selected tab by index."""
        self._tabs_component.set_selected_index(index)

    def add_selected_change_listener(self, listener: Callable):
        """Add a listener for tab selection changes."""
        self._change_listeners.append(listener)

    def get_tab_count(self) -> int:
        """Get the number of tabs."""
        return self._tabs_component.get_tab_count()

    def get_tab_at(self, index: int) -> Tab:
        """Get the tab at the given index."""
        return self._tabs_component._tabs[index]

    def get_index_of(self, tab: Tab) -> int:
        """Get the index of the given tab, or -1 if not found."""
        try:
            return self._tabs_component._tabs.index(tab)
        except ValueError:
            return -1

    def _on_tab_selected(self, event_data: dict):
        """Forward selection events to listeners."""
        for listener in self._change_listeners:
            listener(event_data)
