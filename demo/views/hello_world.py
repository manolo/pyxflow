"""Hello World example - matches my-hello Java application."""

from vaadin.flow import Menu, Route
from vaadin.flow.components import (
    Button,
    HorizontalLayout,
    Notification,
    TextField,
    VerticalLayout,
)
from vaadin.flow.components.horizontal_layout import Alignment
from demo.main_layout import MainLayout


@Route("", page_title="Hello World", layout=MainLayout)
@Menu(title="Home", order=0, icon="vaadin:home")
class HelloWorldView(VerticalLayout):
    """Hello World view matching the Java reference implementation."""

    def __init__(self):
        super().__init__()

        self.name = TextField("Your name")
        self.say_hello = Button("Say hello")
        self.say_hello.add_click_listener(self._on_click)

        self.container = HorizontalLayout(self.name, self.say_hello)
        self.container.set_margin(True)
        self.container.set_vertical_component_alignment(
            Alignment.END, self.name, self.say_hello
        )
        self.add(self.container)

    def _on_click(self, event):
        """Handle button click."""
        Notification.show(f"Hello {self.name.value}", 0, Notification.Position.BOTTOM_CENTER)
