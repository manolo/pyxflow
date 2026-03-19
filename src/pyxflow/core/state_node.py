"""StateNode - represents a node in the state tree."""

from enum import IntEnum
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pyxflow.core.state_tree import StateTree


class Feature(IntEnum):
    """Feature IDs for UIDL protocol."""
    ELEMENT_DATA = 0
    ELEMENT_PROPERTY_MAP = 1
    ELEMENT_CHILDREN_LIST = 2
    ELEMENT_ATTRIBUTE_MAP = 3
    ELEMENT_LISTENER_MAP = 4
    PUSH_CONFIGURATION_MAP = 5
    PUSH_CONFIGURATION_PARAMETERS_MAP = 6
    TEXT_NODE = 7
    INLINE_STYLE_PROPERTY_MAP = 12
    CLIENT_DELEGATE_HANDLERS = 19
    VIRTUAL_CHILDREN_LIST = 24


class StateNode:
    """A node in the state tree."""

    def __init__(self, node_id: int, tree: "StateTree"):
        self._id = node_id
        self._tree = tree
        self._features: dict[int, dict[str, Any]] = {}
        self._children: list["StateNode"] = []
        self._parent: "StateNode | None" = None
        self._attached = False

    @property
    def id(self) -> int:
        return self._id

    def attach(self):
        """Mark node as attached and record change."""
        if not self._attached:
            self._attached = True
            self._tree.add_change({"node": self._id, "type": "attach"})

    def put(self, feature: int, key: str, value: Any):
        """Set a feature value and record change."""
        if feature not in self._features:
            self._features[feature] = {}
        self._features[feature][key] = value
        self._tree.add_change({
            "node": self._id,
            "type": "put",
            "key": key,
            "feat": feature,
            "value": value
        })

    def get(self, feature: int, key: str, default: Any = None) -> Any:
        """Get a feature value."""
        return self._features.get(feature, {}).get(key, default)

    def remove(self, feature: int, key: str):
        """Remove a feature value and record change."""
        if feature in self._features and key in self._features[feature]:
            del self._features[feature][key]
            self._tree.add_change({
                "node": self._id,
                "type": "remove",
                "key": key,
                "feat": feature
            })

    def add_child(self, child: "StateNode", index: int | None = None):
        """Add a child node."""
        if index is None:
            index = len(self._children)
        self._children.insert(index, child)
        child._parent = self
        self._tree.add_change({
            "node": self._id,
            "type": "splice",
            "feat": Feature.ELEMENT_CHILDREN_LIST,
            "index": index,
            "addNodes": [child._id]
        })

    @property
    def is_attached(self) -> bool:
        """Whether this node is attached to the tree."""
        return self._attached

    def _detach_recursive(self):
        """Mark this node and all descendants as detached."""
        self._attached = False
        for child in self._children:
            child._detach_recursive()

    def remove_child(self, child: "StateNode"):
        """Remove a child node."""
        if child in self._children:
            index = self._children.index(child)
            self._children.remove(child)
            child._parent = None
            child._detach_recursive()
            self._tree.add_change({
                "node": self._id,
                "type": "splice",
                "feat": Feature.ELEMENT_CHILDREN_LIST,
                "index": index,
                "remove": 1
            })

    def clear_children(self, feature: int = Feature.ELEMENT_CHILDREN_LIST):
        """Clear children list and record change."""
        self._tree.add_change({
            "node": self._id,
            "type": "clear",
            "feat": feature
        })

    def add_children(self, children: list["StateNode"], index: int = 0):
        """Add multiple children in a single splice operation."""
        for i, child in enumerate(children):
            self._children.insert(index + i, child)
            child._parent = self
        self._tree.add_change({
            "node": self._id,
            "type": "splice",
            "feat": Feature.ELEMENT_CHILDREN_LIST,
            "index": index,
            "addNodes": [child._id for child in children]
        })
