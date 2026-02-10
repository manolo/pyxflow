import asyncio

from vaadin.flow import Menu, Route
from vaadin.flow.components import (
    Button, Div, HorizontalLayout, Icon, Span, VerticalLayout,
)
from demo.views.main_layout import MainLayout


@Route("push-demo", page_title="Stopwatch", layout=MainLayout)
@Menu(title="Stopwatch", order=10, icon="vaadin:timer")
class PushDemoView(VerticalLayout):
    def __init__(self):
        self._elapsed = 0  # seconds
        self._running = False
        self._task = None

        # --- Time display ---
        self._hours = Span("00")
        self._hours.add_class_name("sw-digit")
        self._min = Span("00")
        self._min.add_class_name("sw-digit")
        self._sec = Span("00")
        self._sec.add_class_name("sw-digit")

        sep1 = Span(":")
        sep1.add_class_name("sw-sep")
        sep2 = Span(":")
        sep2.add_class_name("sw-sep")

        time_row = HorizontalLayout(self._hours, sep1, self._min, sep2, self._sec)
        time_row.set_spacing(False)
        time_row.add_class_name("sw-time")

        circle = Div()
        circle.add_class_name("sw-circle")
        circle.add(time_row)

        # --- Buttons ---
        self._play_btn = Button(icon=Icon("vaadin:play"))
        self._play_btn.add_theme_name("icon", "primary")
        self._play_btn.add_class_name("sw-btn")
        self._play_btn.add_click_listener(self._on_play)

        self._pause_btn = Button(icon=Icon("vaadin:pause"))
        self._pause_btn.add_theme_name("icon")
        self._pause_btn.add_class_name("sw-btn")
        self._pause_btn.set_enabled(False)
        self._pause_btn.add_click_listener(self._on_pause)

        self._reset_btn = Button(icon=Icon("vaadin:refresh"))
        self._reset_btn.add_theme_name("icon", "error")
        self._reset_btn.add_class_name("sw-btn")
        self._reset_btn.set_enabled(False)
        self._reset_btn.add_click_listener(self._on_reset)

        btn_row = HorizontalLayout(self._play_btn, self._pause_btn, self._reset_btn)
        btn_row.add_class_name("sw-buttons")
        btn_row.set_spacing(False)

        # --- Layout ---
        self.add_class_name("sw-view")
        self.set_padding(False)
        self.add(circle, btn_row)

    def _update_display(self):
        h = self._elapsed // 3600
        m = (self._elapsed % 3600) // 60
        s = self._elapsed % 60
        self._hours.set_text(f"{h:02d}")
        self._min.set_text(f"{m:02d}")
        self._sec.set_text(f"{s:02d}")

    def _on_play(self, event):
        if not self._running:
            self._running = True
            self._play_btn.set_enabled(False)
            self._pause_btn.set_enabled(True)
            self._reset_btn.set_enabled(True)
            self._task = asyncio.create_task(self._tick())

    def _stop_task(self):
        self._running = False
        if self._task:
            self._task.cancel()
            self._task = None

    def _on_pause(self, event):
        if self._running:
            self._stop_task()
            self._play_btn.set_enabled(True)
            self._pause_btn.set_enabled(False)

    def _on_reset(self, event):
        self._stop_task()
        self._elapsed = 0
        self._update_display()
        self._play_btn.set_enabled(True)
        self._pause_btn.set_enabled(False)
        self._reset_btn.set_enabled(False)

    async def _tick(self):
        ui = self.get_ui()
        if ui is None:
            return
        while self._running:
            await asyncio.sleep(1)
            if self._running:
                self._elapsed += 1
                ui.access(self._update_display)
