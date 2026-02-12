from vaadin.flow import Route, Menu
from vaadin.flow.components import *

@Route("dialog-demo", page_title="Dialog Demo")
class DialogDemoView(VerticalLayout):
    def __init__(self):
        # Header to identify the view + working component
        self.add(Span("=== DialogDemoView ==="))
        self.add(TextField("Test field (should work)"))

        # Create dialog
        self.dialog = Dialog()
        self.dialog.set_header_title("Confirm Action")
        self.dialog.add(Span("Are you sure you want to proceed?"))

        # Main view
        open_button = Button("Open Dialog")
        open_button.add_click_listener(self._open_dialog)

        self.status = Span("Status: Ready")

        self.add(open_button, self.status)
        self.add(self.dialog)

    def _open_dialog(self, event):
        self.dialog.open()
        new_status = Span("Status: Dialog opened")
        self.add(new_status)
