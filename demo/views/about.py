"""About view example - demonstrates multiple routes."""

from vaadin.flow import Menu, Route
from vaadin.flow.components import RouterLink, Span, VerticalLayout
from demo.views.main_layout import MainLayout


@Route("about", page_title="About", layout=MainLayout)
@Menu(title="About", order=1, icon="vaadin:info-circle")
class AboutView(VerticalLayout):
    """Simple about page to test routing."""

    def __init__(self):
        super().__init__()

        # Header to identify the view
        self.add(Span("=== AboutView ==="))
        self.add(Span("About PyFlow"))
        self.add(Span("Python implementation of Vaadin Flow"))
        self.add(Span("Version 0.1.0"))
        self.add(RouterLink("Back to Components", "/components"))
