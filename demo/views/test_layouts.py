"""Test View 15: Layouts — /test/layouts"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, FlexLayout, FlexDirection, FlexWrap, FormLayout, HorizontalLayout,
    ResponsiveStep, RouterLink, Span, SplitLayout, TextField, VerticalLayout,
)
from vaadin.flow.components.horizontal_layout import Alignment, JustifyContentMode


@Route("test/layouts", page_title="Test: Layouts")
class TestLayoutsView(VerticalLayout):
    def __init__(self):
        # --- VerticalLayout spacing ---
        vl1 = VerticalLayout(Span("A"), Span("B"), Span("C"))
        vl1.set_id("vl1")

        vl_nospace = VerticalLayout(Span("X"), Span("Y"))
        vl_nospace.set_id("vl-nospace")
        vl_nospace.set_spacing(False)

        vl_pad = VerticalLayout(Span("P"))
        vl_pad.set_id("vl-pad")
        vl_pad.set_padding(True)

        # --- VerticalLayout expand ---
        child_expand = Span("Expanded")
        child_expand.set_id("child-expand")
        vl_expand = VerticalLayout(Span("Top"), child_expand)
        vl_expand.set_id("vl-expand")
        vl_expand.set_height("200px")
        vl_expand.expand(child_expand)

        # --- VerticalLayout justify/align ---
        vl_center = VerticalLayout(Span("Centered"))
        vl_center.set_id("vl-center")
        vl_center.set_justify_content_mode(JustifyContentMode.CENTER)
        vl_center.set_default_horizontal_component_alignment(Alignment.CENTER)
        vl_center.set_height("100px")

        # --- VerticalLayout add/remove dynamically ---
        vl_dyn = VerticalLayout()
        vl_dyn.set_id("vl-dyn")
        btn_add = Button("Add span")
        btn_add.set_id("btn-add-span")
        btn_add.add_click_listener(lambda e: vl_dyn.add(Span("New")))

        # --- VerticalLayout replace ---
        old_span = Span("Old")
        old_span.set_id("old-span")
        vl_replace = VerticalLayout(old_span)
        vl_replace.set_id("vl-replace")
        btn_replace = Button("Replace")
        btn_replace.set_id("btn-replace")
        btn_replace.add_click_listener(
            lambda e: vl_replace.replace(old_span, Span("Replaced"))
        )

        # --- VerticalLayout add_component_as_first ---
        vl_first = VerticalLayout(Span("Second"), Span("Third"))
        vl_first.set_id("vl-first")
        btn_add_first = Button("Add first")
        btn_add_first.set_id("btn-add-first")
        btn_add_first.add_click_listener(
            lambda e: vl_first.add_component_as_first(Span("First"))
        )

        # --- HorizontalLayout ---
        hl1 = HorizontalLayout(Span("L"), Span("M"), Span("R"))
        hl1.set_id("hl1")

        hl_expand = HorizontalLayout()
        hl_expand.set_id("hl-expand")
        hl_child = Span("Wide")
        hl_child.set_id("hl-child")
        hl_expand.add(hl_child, Span("Narrow"))
        hl_expand.expand(hl_child)
        hl_expand.set_width("100%")

        # --- FlexLayout ---
        fl = FlexLayout(Span("F1"), Span("F2"), Span("F3"))
        fl.set_id("fl1")
        fl.set_flex_direction(FlexDirection.COLUMN)

        fl_wrap = FlexLayout()
        fl_wrap.set_id("fl-wrap")
        fl_wrap.set_flex_wrap(FlexWrap.WRAP)
        for i in range(6):
            s = Span(f"W{i}")
            s.set_width("200px")
            fl_wrap.add(s)

        # --- FormLayout ---
        form = FormLayout(
            TextField("First name"),
            TextField("Last name"),
            TextField("Email"),
            TextField("Phone"),
        )
        form.set_id("form1")
        form.set_responsive_steps(
            ResponsiveStep("0", 1),
            ResponsiveStep("600px", 2),
        )

        # --- SplitLayout ---
        split = SplitLayout(Span("Primary"), Span("Secondary"))
        split.set_id("split1")
        split.set_width("100%")
        split.set_height("100px")

        # --- Nav link ---
        nav_link = RouterLink("Next: Card & Scroller", "test/card-scroller")
        nav_link.set_id("nav-next")

        self.add(
            vl1, vl_nospace, vl_pad, vl_expand, vl_center,
            vl_dyn, btn_add,
            vl_replace, btn_replace,
            vl_first, btn_add_first,
            hl1, hl_expand,
            fl, fl_wrap,
            form,
            split,
            nav_link,
        )
