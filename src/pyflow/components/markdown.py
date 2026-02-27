"""Markdown component — renders markdown content as HTML."""

from vaadin.flow.core.component import Component


class Markdown(Component):
    """Renders Markdown content as HTML.

    New in Vaadin 25. The content is sanitized on the client side
    to prevent XSS.
    """

    _v_fqcn = "com.vaadin.flow.component.markdown.Markdown"
    _tag = "vaadin-markdown"

    def __init__(self, content: str = ""):
        super().__init__()
        self._content = content

    def _attach(self, tree):
        super()._attach(tree)
        if self._content:
            self.element.set_property("content", self._content)

    def set_content(self, content: str):
        """Set the markdown content."""
        self._content = content
        if self._element:
            self.element.set_property("content", content)

    def append_content(self, content: str):
        """Append content to the existing markdown content."""
        self._content += content
        if self._element:
            self.element.set_property("content", self._content)

    def get_content(self) -> str:
        return self._content
