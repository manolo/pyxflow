"""Test View 18: ProgressBar, Avatar, Markdown, MessageInput, MessageList — /test/display"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Avatar, AvatarGroup, AvatarGroupItem, Button, Markdown, MessageInput,
    MessageList, MessageListItem, ProgressBar, Span, VerticalLayout,
)
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/display", page_title="Test: Display Components", layout=TestMainLayout)
@Menu(title="Display", order=14)
class TestDisplayView(VerticalLayout):
    def __init__(self):
        # --- ProgressBar ---
        pb1 = ProgressBar()
        pb1.set_id("pb1")
        pb1.set_value(0.6)

        btn_pb = Button("Set 90%")
        btn_pb.set_id("btn-pb")
        btn_pb.add_click_listener(lambda e: pb1.set_value(0.9))

        # --- ProgressBar indeterminate ---
        pb_ind = ProgressBar()
        pb_ind.set_id("pb-ind")
        pb_ind.set_indeterminate(True)

        # --- ProgressBar min/max ---
        pb_range = ProgressBar()
        pb_range.set_id("pb-range")
        pb_range.set_min(0)
        pb_range.set_max(200)
        pb_range.set_value(100)

        # --- Avatar ---
        av1 = Avatar("Sophia Williams")
        av1.set_id("av1")

        av_abbr = Avatar()
        av_abbr.set_id("av-abbr")
        av_abbr.set_abbreviation("JD")

        av_color = Avatar("Color")
        av_color.set_id("av-color")
        av_color.set_color_index(3)

        # --- AvatarGroup ---
        ag = AvatarGroup()
        ag.set_id("ag1")
        ag.set_items([
            AvatarGroupItem(name="Alice"),
            AvatarGroupItem(name="Bob"),
            AvatarGroupItem(name="Charlie"),
            AvatarGroupItem(name="Diana"),
            AvatarGroupItem(name="Eve"),
        ])

        ag_max = AvatarGroup()
        ag_max.set_id("ag-max")
        ag_max.set_items([
            AvatarGroupItem(name="A"),
            AvatarGroupItem(name="B"),
            AvatarGroupItem(name="C"),
            AvatarGroupItem(name="D"),
            AvatarGroupItem(name="E"),
        ])
        ag_max.set_max_items_visible(3)

        # --- Markdown ---
        md = Markdown("# Hello\n**bold** text")
        md.set_id("md1")

        btn_md = Button("Update markdown")
        btn_md.set_id("btn-md")
        btn_md.add_click_listener(lambda e: md.set_content("## Updated"))

        # --- MessageInput ---
        mi_result = Span("")
        mi_result.set_id("mi-result")
        mi = MessageInput()
        mi.set_id("mi1")
        mi.add_submit_listener(
            lambda e: mi_result.set_text(str(e.get("value", "")))
        )

        # --- MessageList ---
        ml = MessageList()
        ml.set_id("ml1")
        ml.set_items(
            MessageListItem(text="Hi", user_name="Alice"),
            MessageListItem(text="Hello", user_name="Bob"),
            MessageListItem(text="Hey there", user_name="Charlie"),
        )

        self.add(
            pb1, btn_pb,
            pb_ind,
            pb_range,
            av1, av_abbr, av_color,
            ag, ag_max,
            md, btn_md,
            mi, mi_result,
            ml,
        )
