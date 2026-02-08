"""DrawerToggle component."""

from vaadin.flow.components.button import Button


class DrawerToggle(Button):
    """A toggle button for the AppLayout drawer. The hamburger icon is built-in."""

    _tag = "vaadin-drawer-toggle"
