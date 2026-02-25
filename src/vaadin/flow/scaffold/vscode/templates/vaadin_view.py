from vaadin.flow import Route
from vaadin.flow.components import (
    Div,
    H3,
    VerticalLayout,
)


@Route("{{route}}")
class {{classname}}(Div):
    def __init__(self):
        self.set_size_full()

        layout = VerticalLayout()
        layout.set_size_full()
        layout.add(H3("{{route}}"))

        self.add(layout)
