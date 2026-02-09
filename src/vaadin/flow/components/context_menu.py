"""ContextMenu component — right-click / long-press context menu.

Reuses the contextMenuConnector already implemented for MenuBar.
"""

from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class ContextMenuItem:
    """A menu item in a ContextMenu."""

    def __init__(self, text: str = "", click_listener: Callable | None = None):
        self._text = text
        self._click_listener = click_listener
        self._children: list["ContextMenuItem"] = []
        self._enabled = True
        self._checkable = False
        self._checked = False
        self._is_separator = False
        self._node = None

    def get_sub_menu(self) -> "ContextSubMenu":
        return ContextSubMenu(self)

    def set_text(self, text: str):
        self._text = text

    def get_text(self) -> str:
        return self._text

    def set_enabled(self, enabled: bool):
        self._enabled = enabled

    def is_enabled(self) -> bool:
        return self._enabled

    def set_checkable(self, checkable: bool):
        self._checkable = checkable

    def is_checkable(self) -> bool:
        return self._checkable

    def set_checked(self, checked: bool):
        self._checked = checked

    def is_checked(self) -> bool:
        return self._checked


class ContextSubMenu:
    """Submenu of a ContextMenuItem."""

    def __init__(self, parent: ContextMenuItem):
        self._parent = parent

    def add_item(self, text: str, click_listener: Callable | None = None) -> ContextMenuItem:
        item = ContextMenuItem(text, click_listener)
        self._parent._children.append(item)
        return item

    def add_separator(self):
        """Add a separator (hr) item."""
        sep = ContextMenuItem()
        sep._is_separator = True  # noqa: already declared in __init__
        self._parent._children.append(sep)

    def get_items(self) -> list[ContextMenuItem]:
        return self._parent._children.copy()


class ContextMenu(Component):
    """A context menu component.

    Attaches to a target component and shows a menu on right-click
    (or long-press on touch devices).

    Uses contextMenuConnector.generateItemsTree() — same connector as MenuBar.
    """

    _tag = "vaadin-context-menu"

    def __init__(self, target: Component | None = None):
        super().__init__()
        self._target = target
        self._items: list[ContextMenuItem] = []
        self._open_on_click = False

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        if self._open_on_click:
            self.element.set_property("openOnClick", True)

        # Init connector: contextMenuConnector.initLazy(element, appId)
        client_key = tree._app_id.split("-")[0]
        el_ref = {"@v-node": self.element.node.id}
        tree.queue_execute([
            el_ref, client_key,
            "return window.Vaadin.Flow.contextMenuConnector.initLazy($0, $1)"
        ])

        # Attach and add the target as a child of the context-menu element
        if self._target:
            if not self._target._element:
                self._target._ui = self._ui
                self._target._parent = self
                self._target._attach(tree)
            self.element.add_child(self._target.element)

        if self._items:
            self._build_items(tree)

    def _build_items(self, tree: "StateTree"):
        """Build item nodes and call generateItemsTree connector.

        Same architecture as MenuBar: container div as virtual child,
        root sub-container holds items, sub-containers for submenus.
        """
        # 1. Main virtual container
        container = tree.create_node()
        container.attach()
        container.put(Feature.ELEMENT_DATA, "tag", "div")
        container.put(Feature.ELEMENT_DATA, "payload", {"type": "inMemory"})
        self._container = container

        # 2. Root sub-container
        root_container = tree.create_node()
        root_container.attach()
        root_container.put(Feature.ELEMENT_DATA, "tag", "div")
        container.add_child(root_container)

        # 3. Create item nodes
        for item in self._items:
            self._create_item_node(tree, root_container, item)

        # 4. Virtual child splice
        tree.add_change({
            "node": self.element.node.id,
            "type": "splice",
            "feat": Feature.VIRTUAL_CHILDREN_LIST,
            "index": 0,
            "addNodes": [container.id]
        })

        # 5. Call $connector.generateItems(rootContainerNodeId)
        el_ref = {"@v-node": self.element.node.id}
        tree.queue_execute([
            el_ref, root_container.id,
            "return $0.$connector.generateItems($1)"
        ])

    def _create_item_node(self, tree, parent_node, item: ContextMenuItem):
        """Create a state node for a ContextMenuItem."""
        item_node = tree.create_node()
        item_node.attach()

        if getattr(item, '_is_separator', False):
            item_node.put(Feature.ELEMENT_DATA, "tag", "hr")
            parent_node.add_child(item_node)
            return

        item_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-context-menu-item")

        # Text child
        text_node = tree.create_node()
        text_node.attach()
        text_node.put(Feature.TEXT_NODE, "text", item._text)
        item_node.add_child(text_node)

        if not item._enabled:
            item_node.put(Feature.ELEMENT_ATTRIBUTE_MAP, "disabled", "")

        item._node = item_node

        # Click listener
        if item._click_listener:
            el = _ContextItemElement(item_node, tree)
            el._listeners["click"] = [item._click_listener]
            tree.register_element(el)
            item_node.put(Feature.ELEMENT_LISTENER_MAP, "click", True)

        parent_node.add_child(item_node)

        # Submenu children
        if item._children:
            sub_container = tree.create_node()
            sub_container.attach()
            sub_container.put(Feature.ELEMENT_DATA, "tag", "div")
            self._container.add_child(sub_container)

            for child in item._children:
                self._create_item_node(tree, sub_container, child)

            item_node.put(Feature.ELEMENT_PROPERTY_MAP, "_containerNodeId", sub_container.id)

    def add_item(self, text: str, click_listener: Callable | None = None) -> ContextMenuItem:
        """Add a root-level menu item."""
        item = ContextMenuItem(text, click_listener)
        self._items.append(item)
        return item

    def add_separator(self):
        """Add a separator between items."""
        sep = ContextMenuItem()
        sep._is_separator = True  # noqa: already declared in __init__
        self._items.append(sep)

    def get_items(self) -> list[ContextMenuItem]:
        return self._items.copy()

    def set_target(self, target: Component):
        """Set the target component for the context menu."""
        self._target = target

    def set_open_on_click(self, open_on_click: bool):
        """Set whether to open on left-click instead of right-click."""
        self._open_on_click = open_on_click
        if self._element:
            self.element.set_property("openOnClick", open_on_click)


class _ContextItemElement:
    """Lightweight element wrapper for ContextMenuItem event dispatch."""

    def __init__(self, node, tree):
        self._node = node
        self._tree = tree
        self._listeners: dict[str, list[Callable]] = {}
        self._style = None

    @property
    def node(self):
        return self._node

    @property
    def node_id(self):
        return self._node.id

    def fire_event(self, event_type: str, event_data: dict):
        for listener in self._listeners.get(event_type, []):
            listener(event_data)
