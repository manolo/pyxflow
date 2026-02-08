"""Greet view - demonstrates route parameters."""

from vaadin.flow import Route, PageTitle
from vaadin.flow.components import H2, RouterLink, Span, VerticalLayout


@Route("greet/:name")
@PageTitle("Greeting")
class GreetView(VerticalLayout):
    """View that greets a user by name from the route parameter."""

    def set_parameter(self, params):
        name = params.get("name", "stranger")
        self.add(H2(f"Hello, {name}!"))
        self.add(Span("This view uses a route parameter."))
        self.add(RouterLink("Back to Components", "/components"))
