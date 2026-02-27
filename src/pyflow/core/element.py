"""Element - represents a DOM element on the client."""

from typing import TYPE_CHECKING, Any, Callable

from pyflow.core.state_node import Feature, StateNode

if TYPE_CHECKING:
    from pyflow.core.state_tree import StateTree


class Style:
    """Inline style manager for an element."""

    def __init__(self, node: StateNode):
        self._node = node

    def set(self, name: str, value: str):
        """Set a style property."""
        self._node.put(Feature.INLINE_STYLE_PROPERTY_MAP, name, value)

    def get(self, name: str) -> str | None:
        """Get a style property."""
        return self._node.get(Feature.INLINE_STYLE_PROPERTY_MAP, name)

    def remove(self, name: str):
        """Remove a style property."""
        self._node.remove(Feature.INLINE_STYLE_PROPERTY_MAP, name)


class Element:
    """Represents a DOM element."""

    def __init__(self, tag: str, tree: "StateTree"):
        self._tree = tree
        self._node = tree.create_node()
        self._node.attach()
        self._node.put(Feature.ELEMENT_DATA, "tag", tag)
        self._style = Style(self._node)
        self._listeners: dict[str, list[Callable]] = {}
        # Register element for event dispatch
        tree.register_element(self)

    @property
    def node(self) -> StateNode:
        return self._node

    @property
    def node_id(self) -> int:
        return self._node.id

    def get_style(self) -> Style:
        """Get the style manager."""
        return self._style

    def set_property(self, name: str, value: Any):
        """Set a property."""
        self._node.put(Feature.ELEMENT_PROPERTY_MAP, name, value)

    def get_property(self, name: str, default: Any = None) -> Any:
        """Get a property."""
        return self._node.get(Feature.ELEMENT_PROPERTY_MAP, name, default)

    def set_attribute(self, name: str, value: str):
        """Set an attribute."""
        self._node.put(Feature.ELEMENT_ATTRIBUTE_MAP, name, value)

    def get_attribute(self, name: str) -> str | None:
        """Get an attribute."""
        return self._node.get(Feature.ELEMENT_ATTRIBUTE_MAP, name)

    def remove_attribute(self, name: str):
        """Remove an attribute."""
        self._node.remove(Feature.ELEMENT_ATTRIBUTE_MAP, name)

    def add_event_listener(self, event_type: str, listener: Callable, hash_key: str | None = None):
        """Add an event listener.

        Args:
            event_type: The DOM event type (e.g., "click", "opened-changed").
            listener: Callback function.
            hash_key: Optional explicit hash for the UIDL constant. If provided,
                      it is used directly instead of True (which is resolved later
                      by the UIDL handler based on event type).
        """
        if event_type not in self._listeners:
            self._listeners[event_type] = []
            # Register with UIDL
            self._node.put(Feature.ELEMENT_LISTENER_MAP, event_type, hash_key if hash_key else True)
        self._listeners[event_type].append(listener)

    def fire_event(self, event_type: str, event_data: dict):
        """Fire an event to listeners."""
        for listener in self._listeners.get(event_type, []):
            listener(event_data)

    def add_child(self, child: "Element", index: int | None = None):
        """Add a child element."""
        self._node.add_child(child._node, index)

    def add_children(self, children: list["Element"], index: int = 0):
        """Add multiple child elements in a single splice operation."""
        self._node.add_children([child._node for child in children], index)

    def remove_child(self, child: "Element"):
        """Remove a child element."""
        self._node.remove_child(child._node)

    def remove_property(self, name: str):
        """Remove a property."""
        self._node.remove(Feature.ELEMENT_PROPERTY_MAP, name)

    def execute_js(self, script: str, *args):
        """Execute JavaScript on this element.

        The element is available as $0 in the script.
        Additional arguments can be referenced as $1, $2, etc.

        Args:
            script: JavaScript code to execute.
            *args: Arguments passed to the script (Element refs or values).
        """
        command: list = [{"@v-node": self._node.id}]
        for arg in args:
            if hasattr(arg, "_node"):
                # Element reference
                command.append({"@v-node": arg._node.id})
            else:
                command.append(arg)
        command.append(script)
        self._tree.queue_execute(command)
