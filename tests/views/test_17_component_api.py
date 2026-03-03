"""Test View 20: Base Component API — /test/component-api"""

from pyxflow import Route
from pyxflow.components import (
    Button, Div, Span, TextField, VerticalLayout,
)
from pyxflow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/component-api", page_title="Test: Component API", layout=TestMainLayout)
@Menu(title="17 Component API", order=17)
class TestComponentApiView(VerticalLayout):
    def __init__(self):
        # --- Visibility ---
        vis_btn = Button("Visible")
        vis_btn.set_id("vis-btn")
        btn_hide = Button("Hide")
        btn_hide.set_id("btn-hide")
        btn_hide.add_click_listener(lambda e: vis_btn.set_visible(False))
        btn_show = Button("Show")
        btn_show.set_id("btn-show")
        btn_show.add_click_listener(lambda e: vis_btn.set_visible(True))

        # --- Enabled ---
        en_btn = Button("Enabled")
        en_btn.set_id("en-btn")
        btn_disable = Button("Disable")
        btn_disable.set_id("btn-disable")
        btn_disable.add_click_listener(lambda e: en_btn.set_enabled(False))
        btn_enable = Button("Enable")
        btn_enable.set_id("btn-enable")
        btn_enable.add_click_listener(lambda e: en_btn.set_enabled(True))

        # --- CSS Classes ---
        cls_span = Span("Classy")
        cls_span.set_id("cls-span")
        btn_add_cls = Button("Add class")
        btn_add_cls.set_id("btn-add-cls")
        btn_add_cls.add_click_listener(lambda e: cls_span.add_class_name("highlight"))
        btn_rm_cls = Button("Remove class")
        btn_rm_cls.set_id("btn-rm-cls")
        cls_span.add_class_name("old")
        btn_rm_cls.add_click_listener(lambda e: cls_span.remove_class_name("old"))

        # --- Inline Styles ---
        sty_span = Span("Styled")
        sty_span.set_id("sty-span")
        btn_set_style = Button("Set color red")
        btn_set_style.set_id("btn-set-style")
        btn_set_style.add_click_listener(
            lambda e: sty_span.get_style().set("color", "red")
        )
        btn_rm_style = Button("Remove color")
        btn_rm_style.set_id("btn-rm-style")
        btn_rm_style.add_click_listener(
            lambda e: sty_span.get_style().remove("color")
        )

        # --- Size ---
        size_div = Div("Sizable")
        size_div.set_id("size-div")
        btn_size = Button("Set 300x100")
        btn_size.set_id("btn-size")

        def _set_size(e):
            size_div.set_width("300px")
            size_div.set_height("100px")

        btn_size.add_click_listener(_set_size)

        full_div = Div("Full")
        full_div.set_id("full-div")
        btn_full = Button("Set full")
        btn_full.set_id("btn-full")
        btn_full.add_click_listener(lambda e: full_div.set_size_full())

        # --- Themes ---
        theme_btn = Button("Themeable")
        theme_btn.set_id("theme-btn")
        btn_add_theme = Button("Add primary")
        btn_add_theme.set_id("btn-add-theme")
        btn_add_theme.add_click_listener(lambda e: theme_btn.add_theme_name("primary"))
        btn_rm_theme = Button("Remove primary")
        btn_rm_theme.set_id("btn-rm-theme")
        btn_rm_theme.add_click_listener(lambda e: theme_btn.remove_theme_name("primary"))

        # --- ID dynamic ---
        id_span = Span("Dynamic ID")
        btn_set_id = Button("Set ID")
        btn_set_id.set_id("btn-set-id")
        btn_set_id.add_click_listener(lambda e: id_span.set_id("my-span"))

        # --- Tooltip ---
        tip_btn = Button("Hover me")
        tip_btn.set_id("tip-btn")
        tip_btn.set_tooltip_text("Click me!")

        # --- ARIA ---
        aria_btn = Button("Close")
        aria_btn.set_id("aria-btn")
        aria_btn.set_aria_label("Close dialog")

        # --- Focus/Blur ---
        focus_tf = TextField("Focus me")
        focus_tf.set_id("focus-tf")
        btn_focus = Button("Focus field")
        btn_focus.set_id("btn-focus")
        btn_focus.add_click_listener(lambda e: focus_tf.focus())

        fb_ev = Span("")
        fb_ev.set_id("fb-ev")
        fb_tf = TextField("Focus/Blur")
        fb_tf.set_id("fb-tf")
        fb_tf.add_focus_listener(lambda e: fb_ev.set_text("focus"))
        fb_tf.add_blur_listener(lambda e: fb_ev.set_text("blur"))

        self.add(
            vis_btn, btn_hide, btn_show,
            en_btn, btn_disable, btn_enable,
            cls_span, btn_add_cls, btn_rm_cls,
            sty_span, btn_set_style, btn_rm_style,
            size_div, btn_size,
            full_div, btn_full,
            theme_btn, btn_add_theme, btn_rm_theme,
            id_span, btn_set_id,
            tip_btn,
            aria_btn,
            focus_tf, btn_focus,
            fb_tf, fb_ev,
        )
