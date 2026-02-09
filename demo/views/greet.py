from vaadin.flow import Route, PageTitle
from demo.views.main_layout import MainLayout
from vaadin.flow.components import H2, RouterLink, Span, VerticalLayout


@Route("greet/:name", layout=MainLayout)
@PageTitle("Greeting")
class GreetView(VerticalLayout):
    def set_parameter(self, params):
        name = params.get("name", "stranger")
        self.add(H2(f"Hello, {name}!"))
        self.add(Span("This view uses a route parameter."))
        self.add(RouterLink("Back to Components", "/components"))
