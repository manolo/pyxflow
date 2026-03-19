"""VirtualList component."""

from typing import Callable, Generic, TypeVar, Optional, TYPE_CHECKING

from pyxflow.core.component import Component
from pyxflow.core.state_node import Feature
from pyxflow.components.renderer import Renderer, LitRenderer, ComponentRenderer
from pyxflow.components.constants import VirtualListVariant

if TYPE_CHECKING:
    from pyxflow.core.state_tree import StateTree

T = TypeVar('T')


class VirtualList(Component, Generic[T]):
    """A scrollable list that renders items on demand.

    VirtualList only renders the visible items, making it efficient for
    large datasets. Items are pushed via the virtualListConnector.

    Usage::

        vl = VirtualList()
        vl.set_items(["Item 1", "Item 2", ...])
        vl.set_renderer(LitRenderer.of("<div>${item.name}</div>").with_property("name", lambda x: x))
    """

    _v_fqcn = "com.vaadin.flow.component.virtuallist.VirtualList"
    _tag = "vaadin-virtual-list"

    def __init__(self):
        super().__init__()
        self._items: list[T] = []
        self._renderer: Optional[Renderer] = None
        self._key_to_item: dict[str, T] = {}

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        # Register client-callable method via Feature 19
        self._register_server_method("set_viewport_range")
        tree.add_change({
            "node": self.element.node_id,
            "type": "splice",
            "feat": Feature.CLIENT_DELEGATE_HANDLERS,
            "index": 0,
            "add": ["setViewportRange"],
        })

        # Init connector
        el_ref = {"@v-node": self.element.node_id}
        tree.queue_execute([
            el_ref,
            "return window.Vaadin.Flow.virtualListConnector.initLazy($0)"
        ])

        # Register in tree._components for publishedEventHandler dispatch
        tree._components[self.element.node_id] = self

        # Setup renderer
        if self._renderer:
            self._setup_renderer(tree)

        # Push initial data
        if self._items:
            self._push_all_data()

    def _setup_renderer(self, tree: "StateTree"):
        """Set up the renderer on the virtual list element."""
        renderer = self._renderer
        if renderer is None:
            return

        el_ref = {"@v-node": self.element.node_id}

        if isinstance(renderer, LitRenderer):
            template = renderer._template
            renderer_name = "renderer"
            client_callables = list(renderer._functions.keys())

            if client_callables:
                channel_id = tree.register_return_channel(
                    self.element.node_id,
                    lambda args, r=renderer: self._handle_renderer_callback(args, r),
                )
                return_channel = {"@v-return": [self.element.node_id, channel_id]}
            else:
                return_channel = None

            tree.queue_execute([
                el_ref, renderer_name, template,
                return_channel, client_callables,
                renderer._namespace, tree._app_id,
                "return window.Vaadin.setLitRenderer($0, $1, $2, $3, $4, $5, $6)",
            ])

        elif isinstance(renderer, ComponentRenderer):
            template = "${Vaadin.FlowComponentHost.getNode(appId, item.nodeid)}"
            renderer_name = "renderer"
            client_callables = []

            # Create container div as virtual child
            container_node = tree.create_node()
            container_node.attach()
            container_node.put(Feature.ELEMENT_DATA, "tag", "div")
            container_node.put(Feature.ELEMENT_DATA, "payload", {"type": "inMemory"})
            tree.add_change({
                "node": self.element.node_id,
                "type": "splice",
                "feat": Feature.VIRTUAL_CHILDREN_LIST,
                "index": 0,
                "addNodes": [container_node.id],
            })
            renderer._container_node = container_node

            client_key = tree._app_id.split("-")[0]

            tree.queue_execute([
                el_ref, renderer_name, template,
                None, client_callables,
                renderer._namespace, client_key,
                "return window.Vaadin.setLitRenderer($0, $1, $2, $3, $4, $5, $6)",
            ])

            container_ref = {"@v-node": container_node.id}
            tree.queue_execute([
                container_ref,
                "return (async function() { Vaadin.FlowComponentHost.patchVirtualContainer(this) }).apply($0)",
            ])

    def _handle_renderer_callback(self, args: list, renderer: LitRenderer):
        """Handle a return channel callback from a LitRenderer function."""
        if len(args) >= 2:
            handler_name = args[0]
            item_key = str(args[1])
            item = self._key_to_item.get(item_key)
            if item and handler_name in renderer._functions:
                renderer._functions[handler_name](item)

    def _push_all_data(self):
        """Push all items to the client."""
        if not self._element:
            return
        self._push_data(0, len(self._items))

    def _push_data(self, offset: int, limit: int):
        """Push items to the client at the given range."""
        if not self._element:
            return
        tree = self._element._tree
        el_ref = {"@v-node": self.element.node_id}

        end = min(offset + limit, len(self._items))
        items_slice = self._items[offset:end]

        connector_items = []
        for i, item in enumerate(items_slice):
            key = str(offset + i)
            self._key_to_item[key] = item
            ci: dict = {"key": key}

            if self._renderer:
                self._add_renderer_data(tree, ci, item, key)

            connector_items.append(ci)

        # updateSize
        tree.queue_execute([
            el_ref, len(self._items),
            "return $0.$connector.updateSize($1)",
        ])

        # set items at offset
        tree.queue_execute([
            el_ref, offset, connector_items,
            "return $0.$connector.set($1, $2)",
        ])

    def _add_renderer_data(self, tree: "StateTree", connector_item: dict, item: T, key: str):
        """Add renderer-specific data to a connector item."""
        renderer = self._renderer
        if renderer is None:
            return
        ns = renderer._namespace

        if isinstance(renderer, LitRenderer):
            for prop_name, provider in renderer._properties.items():
                connector_item[ns + prop_name] = provider(item)

        elif isinstance(renderer, ComponentRenderer):
            if key not in renderer._components:
                component = renderer._factory(item)
                component._attach(tree)
                assert renderer._container_node is not None
                renderer._container_node.add_child(component.element.node)
                renderer._components[key] = component
            component = renderer._components[key]
            connector_item[ns + "nodeid"] = component.element.node_id

    def set_items(self, items: list[T]):
        """Set the items for the virtual list."""
        self._items = list(items)
        self._key_to_item.clear()
        if self._element:
            self._push_all_data()

    def get_items(self) -> list[T]:
        return self._items.copy()

    def set_renderer(self, renderer: Renderer):
        """Set the renderer for the virtual list.

        Args:
            renderer: A LitRenderer or ComponentRenderer.
        """
        self._renderer = renderer
        if self._element:
            self._setup_renderer(self._element._tree)
            if self._items:
                self._push_all_data()

    # --- Client-callable methods (publishedEventHandler RPC) ---

    def set_viewport_range(self, start: int, length: int):
        """Called by client when the visible range changes."""
        self._push_data(start, length)

    def add_theme_variants(self, *variants: VirtualListVariant):
        """Add theme variants to the virtual list."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: VirtualListVariant):
        """Remove theme variants from the virtual list."""
        self.remove_theme_name(*variants)
