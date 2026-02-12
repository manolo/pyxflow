"""MenuBar component."""

from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class SubMenu:
    """Represents a submenu of a MenuItem."""

    def __init__(self, parent: "MenuItem"):
        self._parent = parent

    def add_item(self, text: str, click_listener: Callable | None = None) -> "MenuItem":
        """Add an item to this submenu."""
        item = MenuItem(text, click_listener)
        self._parent._children.append(item)
        return item

    def get_items(self) -> list["MenuItem"]:
        """Get the items in this submenu."""
        return self._parent._children.copy()


class MenuItem:
    """Represents a menu item in a MenuBar.

    This is a data model, not a Component. It maps to a
    vaadin-menu-bar-item element in the UIDL tree.
    """

    def __init__(self, text: str = "", click_listener: Callable | None = None):
        self._text = text
        self._click_listener = click_listener
        self._children: list["MenuItem"] = []
        self._enabled = True
        self._checkable = False
        self._checked = False
        self._node = None  # StateNode, created during _attach

    def get_sub_menu(self) -> SubMenu:
        """Get the submenu for adding child items."""
        return SubMenu(self)

    def add_click_listener(self, listener: Callable):
        """Add a click listener."""
        self._click_listener = listener

    def set_enabled(self, enabled: bool):
        """Set the enabled state."""
        self._enabled = enabled

    def is_enabled(self) -> bool:
        """Check if enabled."""
        return self._enabled

    def set_text(self, text: str):
        """Set the item text."""
        self._text = text

    def get_text(self) -> str:
        """Get the item text."""
        return self._text

    def set_checkable(self, checkable: bool):
        """Set whether the item is checkable."""
        self._checkable = checkable

    def is_checkable(self) -> bool:
        """Check if the item is checkable."""
        return self._checkable

    def set_checked(self, checked: bool):
        """Set the checked state."""
        self._checked = checked

    def is_checked(self) -> bool:
        """Get the checked state."""
        return self._checked

    def is_parent_item(self) -> bool:
        """Check if this item has children (is a parent/submenu trigger)."""
        return len(self._children) > 0


class MenuBar(Component):
    """A menu bar component with dropdown menus.

    Uses menubarConnector.initLazy() and contextMenuConnector.generateItemsTree()
    to build the hierarchical menu structure.
    """

    _v_fqcn = "com.vaadin.flow.component.menubar.MenuBar"
    _tag = "vaadin-menu-bar"

    def __init__(self):
        super().__init__()
        self._items: list[MenuItem] = []
        self._open_on_hover = False

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        if self._open_on_hover:
            self.element.set_property("openOnHover", True)

        # Init connector: menubarConnector.initLazy(element, appId)
        client_key = tree._app_id.split("-")[0]
        el_ref = {"@v-node": self.element.node.id}
        tree.queue_execute([
            el_ref, client_key,
            "return window.Vaadin.Flow.menubarConnector.initLazy($0, $1)"
        ])

        # Build item nodes and generate items
        if self._items:
            self._build_items(tree)

    def _build_items(self, tree: "StateTree"):
        """Create container div with menu item nodes, then call generateItems.

        Structure matches Java's MenuItemsArrayGenerator:
        - Main container (virtual child of menubar, payload: inMemory)
          - Root sub-container (holds top-level items)
          - Sub-container per parent item (holds submenu items)
        """
        # 1. Create the main virtual container div
        container = tree.create_node()
        container.attach()
        container.put(Feature.ELEMENT_DATA, "tag", "div")
        # Mark as in-memory virtual child (required by FlowClient)
        container.put(Feature.ELEMENT_DATA, "payload", {"type": "inMemory"})

        # Keep reference for sub-container attachment
        self._container = container

        # 2. Create root sub-container for top-level items
        root_container = tree.create_node()
        root_container.attach()
        root_container.put(Feature.ELEMENT_DATA, "tag", "div")
        container.add_child(root_container)

        # 3. For each root MenuItem, create item nodes
        for item in self._items:
            self._create_item_node(tree, root_container, item)

        # 4. Add main container as virtual child of the menubar
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

    def _create_item_node(self, tree: "StateTree", parent_node, item: MenuItem):
        """Create a state node for a MenuItem and its children."""
        # Create vaadin-menu-bar-item element
        item_node = tree.create_node()
        item_node.attach()
        item_node.put(Feature.ELEMENT_DATA, "tag", "vaadin-menu-bar-item")

        # Set text as text node child
        text_node = tree.create_node()
        text_node.attach()
        text_node.put(Feature.TEXT_NODE, "text", item._text)
        item_node.add_child(text_node)

        # Disabled state
        if not item._enabled:
            item_node.put(Feature.ELEMENT_ATTRIBUTE_MAP, "disabled", "")

        # Store node reference for event handling
        item._node = item_node  # type: ignore[assignment]

        # Register click listener if provided
        if item._click_listener:
            el = _ItemElement(item_node, tree)
            el._listeners["click"] = [item._click_listener]
            tree.register_element(el)  # type: ignore[arg-type]
            # Register click event in Feature 4 so FlowClient sends click events
            item_node.put(Feature.ELEMENT_LISTENER_MAP, "click", True)

        # Add item to parent container
        parent_node.add_child(item_node)

        # Handle submenu children
        if item._children:
            # Create sub-container as child of MAIN container (not parent_node)
            sub_container = tree.create_node()
            sub_container.attach()
            sub_container.put(Feature.ELEMENT_DATA, "tag", "div")
            self._container.add_child(sub_container)

            for child_item in item._children:
                self._create_item_node(tree, sub_container, child_item)

            # Store container node ID so the connector can find submenu items
            item_node.put(Feature.ELEMENT_PROPERTY_MAP, "_containerNodeId", sub_container.id)

    def add_item(self, text: str, click_listener: Callable | None = None) -> MenuItem:
        """Add a root-level menu item."""
        item = MenuItem(text, click_listener)
        self._items.append(item)
        return item

    def get_items(self) -> list[MenuItem]:
        """Get the root-level items."""
        return self._items.copy()

    def set_open_on_hover(self, open_on_hover: bool):
        """Set whether submenus open on hover."""
        self._open_on_hover = open_on_hover
        if self._element:
            self.element.set_property("openOnHover", open_on_hover)

    def is_open_on_hover(self) -> bool:
        """Check if submenus open on hover."""
        return self._open_on_hover


class _ItemElement:
    """Lightweight element wrapper for MenuItem nodes.

    Used to register click listeners for event dispatch
    without creating a full Element (which would create a new node).
    """

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
        """Fire an event to listeners."""
        for listener in self._listeners.get(event_type, []):
            listener(event_data)
