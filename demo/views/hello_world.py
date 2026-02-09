from vaadin.flow import Menu, Route
from vaadin.flow.components import (
    Button,
    HorizontalLayout,
    Notification,
    TextField,
    VerticalLayout,
)
from vaadin.flow.components.horizontal_layout import Alignment
from demo.views.main_layout import MainLayout


@Route("hello", page_title="Hello World", layout=MainLayout)
@Menu(title="Hello", order=1, icon="vaadin:hand")
class HelloWorldView(VerticalLayout):
    def __init__(self):
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
        Notification.show(f"Hello {self.name.value}", 0, Notification.Position.BOTTOM_CENTER)
