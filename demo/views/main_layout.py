"""Main application layout using AppLayout with navigation drawer."""

from vaadin.flow.components import (
    AppLayout,
    DrawerToggle,
    H1,
    SideNav,
    SideNavItem,
    Icon,
)
from vaadin.flow.menu import get_menu_entries


class MainLayout(AppLayout):
    """Persistent application layout with navbar and drawer navigation."""

    def __init__(self):
        super().__init__()

        # Navbar
        self.add_to_navbar(DrawerToggle(), H1("PyFlow"))

        # Drawer with SideNav — populated from @Menu-annotated routes
        nav = SideNav()
        for entry in get_menu_entries():
            icon = Icon(entry.icon) if entry.icon else None
            nav.add_item(SideNavItem(entry.title, entry.path, icon))
        self.add_to_drawer(nav)
