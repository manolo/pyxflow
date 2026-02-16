from vaadin.flow import AppShell, ColorScheme, Push, StyleSheet
from vaadin.flow.components import *
from vaadin.flow.menu import get_menu_entries, get_page_header


@AppShell
@Push
@ColorScheme("dark")
@StyleSheet("lumo/lumo.css", "styles/styles.css")
class MainLayout(AppLayout):
    def __init__(self):
        # Navbar
        self._page_header = H2("PyFlow")
        self.add_to_navbar(DrawerToggle(), self._page_header)

        # Drawer with SideNav — populated from @Menu-annotated routes
        nav = SideNav()
        logo = Image("/images/logo2.png", "PyFlow")
        logo.get_style().set("height", "60px")
        name = HorizontalLayout()
        name.add(H2("PyFlow"))
        name.set_align_items(FlexAlignment.CENTER)
        name.get_style().set("padding", "10px")
        for entry in get_menu_entries():
            icon = Icon(entry.icon) if entry.icon else None
            nav.add_item(SideNavItem(entry.title, entry.path, icon))
        self.add_to_drawer(name, nav)

        self.set_primary_section(AppLayoutSection.DRAWER)

    def show_router_layout_content(self, content):
        super().show_router_layout_content(content)
        title = get_page_header(content) or "PyFlow"
        self._page_header.set_text(title)
