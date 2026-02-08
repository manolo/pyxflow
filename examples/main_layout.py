"""Main application layout using AppLayout with navigation drawer."""

from vaadin.flow.components import (
    AppLayout,
    DrawerToggle,
    H1,
    SideNav,
    SideNavItem,
    Icon,
)


class MainLayout(AppLayout):
    """Persistent application layout with navbar and drawer navigation."""

    def __init__(self):
        super().__init__()

        # Navbar
        self.add_to_navbar(DrawerToggle(), H1("PyFlow"))

        # Drawer with SideNav
        nav = SideNav()
        nav.add_item(
            SideNavItem("Home", "/", Icon("vaadin:home")),
            SideNavItem("About", "/about", Icon("vaadin:info-circle")),
            SideNavItem("Components", "/components", Icon("vaadin:grid-small")),
            SideNavItem("Grid", "/grid", Icon("vaadin:table")),
        )
        self.add_to_drawer(nav)
