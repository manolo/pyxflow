"""StateTree - manages the server-side component tree."""


class StateTree:
    """Manages the server-side state tree for a UI."""

    def __init__(self):
        self._nodes: dict[int, "StateNode"] = {}
        self._next_node_id = 1
        self._changes: list[dict] = []
        self._elements: dict[int, "Element"] = {}  # node_id -> Element
        self._components: dict[int, "Component"] = {}  # node_id -> Component

    def register_element(self, element: "Element"):
        """Register an element for event dispatch."""
        self._elements[element.node_id] = element

    def get_element(self, node_id: int) -> "Element | None":
        """Get element by node ID."""
        return self._elements.get(node_id)

    def register_component(self, component: "Component"):
        """Register a component for property sync."""
        if component.element:
            self._components[component.element.node_id] = component

    def get_component(self, node_id: int) -> "Component | None":
        """Get component by node ID."""
        return self._components.get(node_id)

    def create_node(self) -> "StateNode":
        """Create a new state node."""
        from vaadin.flow.core.state_node import StateNode
        node_id = self._next_node_id
        self._next_node_id += 1
        node = StateNode(node_id, self)
        self._nodes[node_id] = node
        return node

    def get_node(self, node_id: int) -> "StateNode | None":
        """Get a node by ID."""
        return self._nodes.get(node_id)

    def collect_changes(self) -> list[dict]:
        """Collect and clear pending changes."""
        changes = self._changes.copy()
        self._changes.clear()
        return changes

    def add_change(self, change: dict):
        """Add a change to the pending changes."""
        self._changes.append(change)

    def reset(self):
        """Reset the tree to initial state (for page reload)."""
        self._nodes.clear()
        self._next_node_id = 1
        self._changes.clear()
        self._elements.clear()
        self._components.clear()
