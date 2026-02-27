"""Renderers for Grid columns."""

import secrets
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from pyflow.core.component import Component


class Renderer:
    """Base class for column renderers."""

    def __init__(self):
        self._namespace = f"lr_{secrets.token_hex(8)}_"


class LitRenderer(Renderer):
    """A renderer that uses a Lit HTML template.

    Properties are injected into the template as ``item.<name>``.
    Functions are registered as client-callable handlers invoked from the template
    (e.g. ``@click="${() => handleClick(item)}"``).
    """

    def __init__(self, template: str):
        super().__init__()
        self._template = template
        self._properties: dict[str, Callable] = {}  # name -> value_provider(item)
        self._functions: dict[str, Callable] = {}    # name -> handler(item)

    @staticmethod
    def of(template: str) -> "LitRenderer":
        return LitRenderer(template)

    def with_property(self, name: str, provider: Callable) -> "LitRenderer":
        """Add a property that will be available as ``item.<name>`` in the template."""
        self._properties[name] = provider
        return self

    def with_function(self, name: str, handler: Callable) -> "LitRenderer":
        """Add a function callable from the template.

        The handler receives the item dict when the function is invoked.
        """
        self._functions[name] = handler
        return self


class TextRenderer(LitRenderer):
    """A renderer that displays text from a value provider function.

    The function receives the item and returns a string.
    """

    def __init__(self, value_provider: Callable):
        super().__init__("${item.text}")
        self._properties["text"] = value_provider

    @staticmethod
    def of(value_provider: Callable) -> "TextRenderer":
        return TextRenderer(value_provider)


class ComponentRenderer(Renderer):
    """A renderer that creates a server-side Component for each row.

    The factory function receives the item dict and returns a Component.
    Components are rendered using FlowComponentHost via a container div
    that is a virtual child of the column.
    """

    def __init__(self, factory: Callable):
        super().__init__()
        self._factory = factory  # factory(item) -> Component
        self._components: dict[str, "Component"] = {}  # item_key -> component
        self._container_node = None  # div node, virtual child of column
