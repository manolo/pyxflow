"""About view — default landing page."""

from vaadin.flow import Menu, Route
from vaadin.flow.components import Span, VerticalLayout
from demo.views.main_layout import MainLayout


@Route("", page_title="About", layout=MainLayout)
@Menu(title="About", order=0, icon="vaadin:info-circle")
class AboutView(VerticalLayout):
    """About page — default view."""

    def __init__(self):
        super().__init__()

        self.add(Span("About PyFlow"))
        self.add(Span("Python implementation of Vaadin Flow"))
        self.add(Span("Version 0.1.0"))
