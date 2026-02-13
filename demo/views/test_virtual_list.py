"""Test View 28: VirtualList — /test/virtual-list"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, LitRenderer, RouterLink, Span, VerticalLayout, VirtualList,
)


@Route("test/virtual-list", page_title="Test: VirtualList")
class TestVirtualListView(VerticalLayout):
    def __init__(self):
        # --- VirtualList with items ---
        vl1 = VirtualList()
        vl1.set_id("vl1")
        items = [f"Item {i}" for i in range(100)]
        vl1.set_items(items)
        vl1.set_renderer(
            LitRenderer("<div>${item.label}</div>")
            .with_property("label", lambda x: x)
        )
        vl1.set_height("200px")

        # --- VirtualList set_items replaces ---
        new_items = [f"New {i}" for i in range(5)]
        btn_replace = Button("Replace items")
        btn_replace.set_id("btn-vl-replace")
        btn_replace.add_click_listener(lambda e: vl1.set_items(new_items))

        # --- Nav link ---
        nav_link = RouterLink("Next: Login", "test/login")
        nav_link.set_id("nav-next")

        self.add(vl1, btn_replace, nav_link)
