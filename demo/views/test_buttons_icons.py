"""Test View 1: Buttons & Icons — /test/buttons-icons"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Button, DrawerToggle, HorizontalLayout, Icon, Span,
    TextField, VerticalLayout,
)
from vaadin.flow.core.keys import Key
from vaadin.flow.menu import Menu
from demo.views.test_main_layout import TestMainLayout


@Route("test/buttons-icons", page_title="Test: Buttons & Icons", layout=TestMainLayout)
@Menu(title="Buttons & Icons", order=1)
class TestButtonsIconsView(VerticalLayout):
    def __init__(self):
        # --- Button renders with text ---
        btn1 = Button("Click me")
        btn1.set_id("btn1")

        # --- Button click fires listener ---
        result = Span("")
        result.set_id("result")
        btn_click = Button("Fire click")
        btn_click.set_id("btn-click")
        btn_click.add_click_listener(lambda e: result.set_text("clicked"))

        # --- Button set_text updates label ---
        btn_text = Button("Old")
        btn_text.set_id("btn-text")
        btn_text.add_click_listener(lambda e: btn_text.set_text("New"))

        # --- Button disabled ---
        btn_dis = Button("Disabled")
        btn_dis.set_id("btn-dis")
        btn_dis.set_enabled(False)

        # --- Button disable_on_click ---
        result2 = Span("")
        result2.set_id("result2")
        btn_doc = Button("DisableOnClick")
        btn_doc.set_id("btn-doc")
        btn_doc.set_disable_on_click(True)
        btn_doc.add_click_listener(lambda e: result2.set_text("clicked"))

        # --- Button click() programmatic ---
        result3 = Span("")
        result3.set_id("result3")
        btn_prog = Button("Programmatic")
        btn_prog.set_id("btn-prog")
        btn_prog.add_click_listener(lambda e: result3.set_text("prog"))
        trigger = Button("Trigger")
        trigger.set_id("trigger")
        trigger.add_click_listener(lambda e: btn_prog.click())

        # --- Icon renders ---
        icon1 = Icon("lumo:plus")
        icon1.set_id("icon1")

        # --- Icon color ---
        icon_color = Icon("lumo:edit")
        icon_color.set_id("icon-color")
        icon_color.set_color("red")

        # --- Icon size ---
        icon_size = Icon("lumo:user")
        icon_size.set_id("icon-size")
        icon_size.set_size("32px")

        # --- Button with icon prefix ---
        btn_icon = Button("Save", icon=Icon("lumo:plus"))
        btn_icon.set_id("btn-icon")

        # --- Button icon after text ---
        btn_icon_after = Button("Next", icon=Icon("lumo:arrow-right"))
        btn_icon_after.set_id("btn-icon-after")
        btn_icon_after.set_icon_after_text(True)

        # --- Button icon-only ---
        btn_icononly = Button(icon=Icon("lumo:plus"))
        btn_icononly.set_id("btn-icononly")

        # --- Button click shortcut with TextField ---
        # Tests both V01.14 (Enter triggers click) and V01.18 (value synced before click)
        self._short_field = TextField()
        self._short_field.set_id("short-field")
        self._short_counter = 0
        result4 = Span("")
        result4.set_id("result4")
        self._result4 = result4
        btn_short = Button("Shortcut", self._on_shortcut)
        btn_short.set_id("btn-short")
        btn_short.add_click_shortcut(Key.ENTER)
        short_row = HorizontalLayout()
        short_row.add(self._short_field, btn_short, result4)

        # --- DrawerToggle ---
        result5 = Span("")
        result5.set_id("result5")
        toggle1 = DrawerToggle()
        toggle1.set_id("toggle1")
        toggle1.add_click_listener(lambda e: result5.set_text("toggled"))

        self.add(
            btn1,
            btn_click, result,
            btn_text,
            btn_dis,
            btn_doc, result2,
            btn_prog, trigger, result3,
            icon1, icon_color, icon_size,
            btn_icon, btn_icon_after, btn_icononly,
            short_row,
            toggle1, result5,
        )

    def _on_shortcut(self, event):
        self._short_counter += 1
        val = self._short_field.get_value()
        self._result4.set_text(f"shortcut:{val}:{self._short_counter}")
