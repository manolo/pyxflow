"""About view example - demonstrates multiple routes."""

from vaadin.flow import Route
from vaadin.flow.components import Span, VerticalLayout


@Route("about", page_title="About")
class AboutView(VerticalLayout):
    """Simple about page to test routing."""

    def __init__(self):
        super().__init__()

        self.add(Span("About PyFlow"))
        self.add(Span("Python implementation of Vaadin Flow"))
        self.add(Span("Version 0.1.0"))
