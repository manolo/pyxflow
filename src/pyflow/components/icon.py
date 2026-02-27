"""Icon component."""

from vaadin.flow.core.component import Component


class Icon(Component):
    """A Vaadin icon component.

    Usage:
        Icon("vaadin:home")   # explicit collection:name
        Icon("home")          # auto-prefixes vaadin:
    """

    _v_fqcn = "com.vaadin.flow.component.icon.Icon"
    _tag = "vaadin-icon"

    def __init__(self, icon: str = ""):
        super().__init__()
        self._icon = self._normalize(icon)
        self._color: str | None = None

    @staticmethod
    def _normalize(icon: str) -> str:
        if icon and ":" not in icon:
            return f"vaadin:{icon}"
        return icon

    def _attach(self, tree):
        super()._attach(tree)
        if self._icon:
            self.element.set_attribute("icon", self._icon)

    def set_icon(self, icon: str):
        """Set the icon (e.g., 'vaadin:home' or 'home')."""
        self._icon = self._normalize(icon)
        if self._element:
            self.element.set_attribute("icon", self._icon)

    def get_icon(self) -> str:
        """Get the icon attribute value."""
        return self._icon

    def set_color(self, color: str):
        """Set the icon color via CSS fill."""
        self._color = color
        self.get_style().set("fill", color)

    def get_color(self) -> str | None:
        """Get the icon color."""
        return self._color

    def set_size(self, size: str):
        """Set the icon size (width and height)."""
        self.set_width(size)
        self.set_height(size)
