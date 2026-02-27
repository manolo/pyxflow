from pyflow import Menu, Route
from pyflow.components import *
from pyflow.components.horizontal_layout import Alignment
from demo.views.main_layout import MainLayout


@Route("hello", page_title="Hello World", layout=MainLayout)
@Menu(title="Hello", order=1, icon="vaadin:hand")
class HelloWorldView(VerticalLayout):
    def __init__(self):
        hint = Div()
        hint.add_class_name("demo-hint")
        hint.add(Icon("vaadin:info-circle"), Span(
            "Simplest Vaadin view \u2014 type a name, click the button, "
            "and the server sends a notification back to the browser."))
        self.add(hint)

        self.name = TextField("Your name")
        self.say_hello = Button("Say hello", lambda e:
            Notification.show(f"Hello {self.name.value}", 5000, Notification.Position.MIDDLE))

        self.container = HorizontalLayout(self.name, self.say_hello)
        self.container.set_margin(True)
        self.container.set_vertical_component_alignment(
            Alignment.END, self.name, self.say_hello
        )
        self.add(self.container)
