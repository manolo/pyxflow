"""Test View 24: WebSocket Push — /test/push"""

import asyncio

from pyflow import Route
from pyflow.components import (
    Button, ProgressBar, Span, VerticalLayout,
)
from pyflow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/push", page_title="Test: Push", layout=TestMainLayout)
@Menu(title="24 Push", order=24)
class TestPushView(VerticalLayout):
    def __init__(self):
        # --- Single push update ---
        push_result = Span("")
        push_result.set_id("push-result")
        btn_start = Button("Start task")
        btn_start.set_id("start")

        def _start_task(e):
            async def _bg():
                ui = self.get_ui()
                if ui is None:
                    return
                await asyncio.sleep(0.05)
                ui.access(lambda: push_result.set_text("done"))

            asyncio.create_task(_bg())

        btn_start.add_click_listener(_start_task)

        # --- Multiple push updates ---
        push_count = Span("0")
        push_count.set_id("push-count")
        btn_multi = Button("Multi push")
        btn_multi.set_id("multi")

        def _start_multi(e):
            async def _bg():
                ui = self.get_ui()
                if ui is None:
                    return
                for i in range(1, 4):
                    await asyncio.sleep(0.05)
                    ui.access(lambda n=i: push_count.set_text(str(n)))

            asyncio.create_task(_bg())

        btn_multi.add_click_listener(_start_multi)

        # --- Push ProgressBar ---
        pb = ProgressBar()
        pb.set_id("push-pb")
        pb.set_value(0)
        btn_pb = Button("Progress task")
        btn_pb.set_id("progress")

        def _start_progress(e):
            async def _bg():
                ui = self.get_ui()
                if ui is None:
                    return
                for step in range(1, 6):
                    await asyncio.sleep(0.05)
                    ui.access(lambda v=step / 5: pb.set_value(v))

            asyncio.create_task(_bg())

        btn_pb.add_click_listener(_start_progress)

        # --- UI.access ---
        access_result = Span("")
        access_result.set_id("push-access")
        btn_access = Button("UI.access")
        btn_access.set_id("access")

        def _on_access(e):
            ui = self.get_ui()
            if ui:
                ui.access(lambda: access_result.set_text("accessed"))

        btn_access.add_click_listener(_on_access)

        self.add(
            btn_start, push_result,
            btn_multi, push_count,
            btn_pb, pb,
            btn_access, access_result,
        )
