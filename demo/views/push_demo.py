import asyncio

from vaadin.flow import Menu, Route
from vaadin.flow.components import Button, Span, VerticalLayout
from demo.views.main_layout import MainLayout


@Route("push-demo", page_title="Push Demo", layout=MainLayout)
@Menu(title="Push Demo", order=10, icon="vaadin:timer")
class PushDemoView(VerticalLayout):
    def __init__(self):
        self._label = Span("Counter: 0")
        self._counter = 0

        btn = Button("Start Counter")
        btn.add_click_listener(self._start)
        self.add(self._label, btn)

    def _start(self, event):
        if self._counter == 0:
            asyncio.create_task(self._count())

    async def _count(self):
        ui = self.get_ui()
        if not ui is None:
            while self._counter < 10:
                await asyncio.sleep(1)
                self._counter += 1
                ui.access(lambda c=self._counter: self._label.set_text(f"Counter: {c}"))
            self._counter = 0
            ui.access(lambda c=self._counter: self._label.set_text(f"Counter: {c}"))
