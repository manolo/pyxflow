"""Test View 16: Card, Scroller, MasterDetailLayout — /test/card-scroller"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, Card, MasterDetailLayout, RouterLink, Scroller, ScrollDirection,
    Span, VerticalLayout,
)


@Route("test/card-scroller", page_title="Test: Card & Scroller")
class TestCardScrollerView(VerticalLayout):
    def __init__(self):
        # --- Card with title ---
        card1 = Card()
        card1.set_id("card1")
        card1.set_title("My Card")
        card1.set_subtitle("Subtitle text")
        card1.add(Span("Body text"))
        footer_btn = Button("Action")
        footer_btn.set_id("card-action")
        card1.add_to_footer(footer_btn)

        # --- Card with header prefix/suffix ---
        card2 = Card()
        card2.set_id("card2")
        card2.set_title("Card 2")
        card2.add(Span("Card 2 body"))

        # --- Scroller vertical ---
        scroller = Scroller(scroll_direction=ScrollDirection.VERTICAL)
        scroller.set_id("scroller1")
        scroller.set_height("100px")
        scroller.set_width("200px")
        long_content = VerticalLayout()
        for i in range(20):
            long_content.add(Span(f"Line {i}"))
        scroller.set_content(long_content)

        # --- Scroller horizontal ---
        scroller_h = Scroller(scroll_direction=ScrollDirection.HORIZONTAL)
        scroller_h.set_id("scroller-h")
        scroller_h.set_height("50px")
        from vaadin.flow.components import HorizontalLayout
        wide = HorizontalLayout()
        for i in range(20):
            s = Span(f"Item {i}")
            s.set_width("100px")
            wide.add(s)
        scroller_h.set_content(wide)

        # --- MasterDetailLayout ---
        mdl = MasterDetailLayout()
        mdl.set_id("mdl1")
        mdl.set_master(Span("Master panel"))
        mdl.set_detail(Span("Detail panel"))
        mdl.set_width("100%")
        mdl.set_height("200px")

        # --- Nav link ---
        nav_link = RouterLink("Next: Upload", "test/upload")
        nav_link.set_id("nav-next")

        self.add(
            card1, card2,
            scroller, scroller_h,
            mdl,
            nav_link,
        )
