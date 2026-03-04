# WebSocket Push

Push enables the server to update the UI without client requests.
Uses WebSocket for real-time communication.

## Enable Push

Add `@Push` to your layout or view:

```python
from pyxflow import Push, AppShell, Route
from pyxflow.components import AppLayout

@AppShell
@Push
class MainLayout(AppLayout):
    pass
```

Or on individual views:

```python
@Route("live")
@Push
class LiveView(VerticalLayout):
    pass
```

## UI.access() Pattern

All UI modifications from background tasks MUST use `ui.access()`:

```python
import asyncio
from pyxflow import Route
from pyxflow.components import VerticalLayout, Span, Button

@Route("counter")
class CounterView(VerticalLayout):
    def __init__(self):
        self.count = 0
        self.label = Span("0")
        self.add(self.label, Button("Start", self.start))

    def start(self, event):
        asyncio.create_task(self._count_loop())

    async def _count_loop(self):
        ui = self.get_ui()
        while self.count < 100:
            await asyncio.sleep(1)
            self.count += 1
            ui.access(lambda: self.label.set_text(str(self.count)))
```

## Stopwatch Example

```python
import asyncio
from pyxflow import Route, Push
from pyxflow.components import *

@Route("stopwatch")
@Push
class StopwatchView(VerticalLayout):
    def __init__(self):
        self._elapsed = 0
        self._running = False
        self._task = None

        self._display = H1("00:00:00")
        self._start_btn = Button("Start", self._on_start)
        self._stop_btn = Button("Stop", self._on_stop)
        self._stop_btn.set_enabled(False)

        self.add(self._display, HorizontalLayout(self._start_btn, self._stop_btn))

    def _on_start(self, e):
        self._running = True
        self._start_btn.set_enabled(False)
        self._stop_btn.set_enabled(True)
        self._task = asyncio.create_task(self._tick())

    def _on_stop(self, e):
        self._running = False
        if self._task:
            self._task.cancel()
        self._start_btn.set_enabled(True)
        self._stop_btn.set_enabled(False)

    async def _tick(self):
        ui = self.get_ui()
        while self._running:
            await asyncio.sleep(1)
            if self._running:
                self._elapsed += 1
                h, m, s = self._elapsed // 3600, (self._elapsed % 3600) // 60, self._elapsed % 60
                ui.access(lambda: self._display.set_text(f"{h:02d}:{m:02d}:{s:02d}"))
```

## Key Rules

1. **Always use `ui.access()`** for UI changes from async tasks
2. **Get `ui` reference early** -- call `self.get_ui()` before `await`
3. **Check `self._running`** after `await` to handle cancellation gracefully
4. **Cancel tasks on detach** to prevent memory leaks
