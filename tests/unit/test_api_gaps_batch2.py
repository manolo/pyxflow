"""Tests for API gaps implemented in Batches 1-7.

Covers: HasAriaLabel, FocusNotifier/BlurNotifier, field properties (clearButton,
prefix/suffix, maxLength, autoselect, autoOpen, overlayWidth), layout APIs
(justify, align, flex, replace, addComponentAtIndex, boxSizing, wrap), Grid
advanced (frozen, key, column ops, allRowsVisible, componentColumn, scroll,
emptyState), Selection (emptySelection, select/deselect, itemEnabledProvider),
Dialog/Notification/Popover/ConfirmDialog/Button extras, navigation component
APIs, Upload slotted components, HTML elements, Binder, SplitLayout, Card,
MasterDetailLayout.
"""

from pyxflow.components import (
    Accordion, AccordionPanel, Anchor, Article, Aside, Button, Card,
    CheckboxGroup, ContextMenu, DatePicker, DateTimePicker, Details, Dialog,
    Div, EmailField, FlexLayout, Grid, H5, H6, HorizontalLayout, Hr, IFrame,
    ListBox, Main, MenuBar, MultiSelectComboBox, MultiSelectListBox, Nav,
    NativeLabel, Notification, NumberField, PasswordField, Popover, Pre,
    RadioButtonGroup, Scroller, Section, Select, SideNav, SideNavItem, Span,
    SplitLayout, Tab, TabSheet, Tabs, TextArea, TextField, TimePicker,
    VerticalLayout,
)
from pyxflow.components.confirm_dialog import ConfirmDialog
from pyxflow.components.horizontal_layout import Alignment, JustifyContentMode
from pyxflow.components.master_detail_layout import MasterDetailLayout
from pyxflow.components.upload import Upload
from pyxflow.components.combo_box import ComboBox
from pyxflow.core.component import Component
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature
from pyxflow.data.binder import Binder


def tree():
    return StateTree()


# =============================================================================
# Batch 1: HasAriaLabel, FocusNotifier/BlurNotifier
# =============================================================================


class TestHasAriaLabel:
    def test_set_aria_label_before_attach(self):
        btn = Button("OK")
        btn.set_aria_label("Confirm action")
        assert btn.get_aria_label() == "Confirm action"

    def test_set_aria_label_after_attach(self):
        t = tree()
        btn = Button("OK")
        btn._attach(t)
        btn.set_aria_label("Confirm")
        assert btn.get_aria_label() == "Confirm"
        assert btn.element.get_attribute("aria-label") == "Confirm"

    def test_set_aria_label_buffered(self):
        t = tree()
        btn = Button("OK")
        btn.set_aria_label("Confirm")
        btn._attach(t)
        assert btn.element.get_attribute("aria-label") == "Confirm"

    def test_set_aria_labelled_by(self):
        t = tree()
        btn = Button("OK")
        btn.set_aria_labelled_by("label-id")
        btn._attach(t)
        assert btn.get_aria_labelled_by() == "label-id"
        assert btn.element.get_attribute("aria-labelledby") == "label-id"


class TestFocusBlurNotifier:
    def test_add_focus_listener(self):
        t = tree()
        tf = TextField()
        events = []
        tf.add_focus_listener(lambda e: events.append("focus"))
        tf._attach(t)
        # Simulate focus event
        tf.element.fire_event("focus", {})
        assert events == ["focus"]

    def test_add_blur_listener(self):
        t = tree()
        tf = TextField()
        events = []
        tf.add_blur_listener(lambda e: events.append("blur"))
        tf._attach(t)
        tf.element.fire_event("blur", {})
        assert events == ["blur"]


# =============================================================================
# Batch 2: Field properties (clearButton, prefix/suffix, maxLength, etc.)
# =============================================================================


class TestFieldProperties:
    def test_text_field_clear_button(self):
        t = tree()
        tf = TextField()
        tf.set_clear_button_visible(True)
        tf._attach(t)
        assert tf.is_clear_button_visible() is True
        assert tf.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "clearButtonVisible") is True

    def test_text_field_max_length(self):
        tf = TextField()
        tf.set_max_length(100)
        assert tf.get_max_length() == 100

    def test_text_field_min_length(self):
        t = tree()
        tf = TextField()
        tf.set_min_length(5)
        tf._attach(t)
        assert tf.get_min_length() == 5

    def test_text_field_autoselect(self):
        t = tree()
        tf = TextField()
        tf.set_autoselect(True)
        tf._attach(t)
        assert tf.is_autoselect() is True

    def test_text_field_prefix_suffix(self):
        t = tree()
        tf = TextField()
        tf._attach(t)
        prefix = Span("$")
        suffix = Span(".00")
        tf.set_prefix_component(prefix)
        tf.set_suffix_component(suffix)
        assert prefix.element.get_attribute("slot") == "prefix"
        assert suffix.element.get_attribute("slot") == "suffix"

    def test_text_area_clear_button(self):
        t = tree()
        ta = TextArea()
        ta.set_clear_button_visible(True)
        ta._attach(t)
        assert ta.is_clear_button_visible() is True

    def test_password_field_clear_button(self):
        t = tree()
        pf = PasswordField()
        pf.set_clear_button_visible(True)
        pf._attach(t)
        assert pf.is_clear_button_visible() is True

    def test_password_field_max_length(self):
        t = tree()
        pf = PasswordField()
        pf._attach(t)
        pf.set_max_length(50)
        assert pf.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "maxlength") == 50

    def test_email_field_max_length(self):
        t = tree()
        ef = EmailField()
        ef._attach(t)
        ef.set_max_length(255)
        assert ef.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "maxlength") == 255

    def test_number_field_clear_button(self):
        t = tree()
        nf = NumberField()
        nf.set_clear_button_visible(True)
        nf._attach(t)
        assert nf.is_clear_button_visible() is True

    def test_date_picker_clear_button(self):
        t = tree()
        dp = DatePicker()
        dp.set_clear_button_visible(True)
        dp._attach(t)
        assert dp.is_clear_button_visible() is True

    def test_date_picker_auto_open(self):
        t = tree()
        dp = DatePicker()
        dp._attach(t)
        dp.set_auto_open(False)
        assert dp.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "autoOpenDisabled") is True

    def test_time_picker_clear_button(self):
        tp = TimePicker()
        tp.set_clear_button_visible(True)
        assert tp.is_clear_button_visible() is True

    def test_time_picker_auto_open(self):
        t = tree()
        tp = TimePicker()
        tp._attach(t)
        tp.set_auto_open(False)
        assert tp.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "autoOpenDisabled") is True

    def test_date_time_picker_auto_open(self):
        t = tree()
        dtp = DateTimePicker()
        dtp._attach(t)
        dtp.set_auto_open(False)

    def test_combo_box_clear_button(self):
        cb = ComboBox()
        cb.set_clear_button_visible(True)
        assert cb.is_clear_button_visible() is True

    def test_combo_box_auto_open(self):
        t = tree()
        cb = ComboBox()
        cb._attach(t)
        cb.set_auto_open(False)
        assert cb.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "autoOpenDisabled") is True

    def test_combo_box_overlay_width(self):
        t = tree()
        cb = ComboBox()
        cb._attach(t)
        cb.set_overlay_width("300px")

    def test_multi_select_combo_box_clear_button(self):
        mscb = MultiSelectComboBox()
        mscb.set_clear_button_visible(True)
        assert mscb.is_clear_button_visible() is True

    def test_multi_select_combo_box_auto_open(self):
        t = tree()
        mscb = MultiSelectComboBox()
        mscb._attach(t)
        mscb.set_auto_open(False)
        assert mscb.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "autoOpenDisabled") is True


# =============================================================================
# Batch 3: Layout APIs
# =============================================================================


class TestLayoutAPIs:
    def test_vertical_layout_justify_content(self):
        t = tree()
        vl = VerticalLayout()
        vl.set_justify_content_mode(JustifyContentMode.CENTER)
        vl._attach(t)
        assert vl.get_justify_content_mode() == JustifyContentMode.CENTER

    def test_vertical_layout_align_items(self):
        vl = VerticalLayout()
        vl.set_align_items(Alignment.STRETCH)
        assert vl.get_align_items() == Alignment.STRETCH

    def test_vertical_layout_flex_grow(self):
        t = tree()
        vl = VerticalLayout()
        s = Span("test")
        vl.add(s)
        vl._attach(t)
        vl.set_flex_grow(2.0, s)

    def test_vertical_layout_replace(self):
        t = tree()
        vl = VerticalLayout()
        old = Span("old")
        new = Span("new")
        vl.add(old)
        vl._attach(t)
        vl.replace(old, new)
        assert new in vl._children
        assert old not in vl._children

    def test_vertical_layout_add_component_at_index(self):
        t = tree()
        vl = VerticalLayout()
        s1 = Span("first")
        s2 = Span("third")
        vl.add(s1, s2)
        vl._attach(t)
        middle = Span("middle")
        vl.add_component_at_index(1, middle)
        assert vl._children[1] is middle

    def test_vertical_layout_wrap(self):
        vl = VerticalLayout()
        vl.set_wrap(True)
        assert vl.is_wrap() is True

    def test_vertical_layout_box_sizing(self):
        t = tree()
        vl = VerticalLayout()
        vl.set_box_sizing("border-box")
        vl._attach(t)

    def test_horizontal_layout_justify_content(self):
        hl = HorizontalLayout()
        hl.set_justify_content_mode(JustifyContentMode.BETWEEN)
        assert hl.get_justify_content_mode() == JustifyContentMode.BETWEEN

    def test_horizontal_layout_padding(self):
        t = tree()
        hl = HorizontalLayout()
        hl.set_padding(True)
        hl._attach(t)
        assert hl.has_theme_name("padding")

    def test_horizontal_layout_replace(self):
        t = tree()
        hl = HorizontalLayout()
        old = Span("old")
        new = Span("new")
        hl.add(old)
        hl._attach(t)
        hl.replace(old, new)
        assert new in hl._children
        assert old not in hl._children

    def test_horizontal_layout_add_component_at_index(self):
        hl = HorizontalLayout()
        s1 = Span("A")
        s2 = Span("C")
        hl.add(s1, s2)
        mid = Span("B")
        hl.add_component_at_index(1, mid)
        assert hl._children[1] is mid

    def test_flex_layout_replace(self):
        t = tree()
        fl = FlexLayout()
        old = Span("old")
        new = Span("new")
        fl.add(old)
        fl._attach(t)
        fl.replace(old, new)
        assert new in fl._children

    def test_flex_layout_add_component_at_index(self):
        fl = FlexLayout()
        s1 = Span("A")
        s2 = Span("C")
        fl.add(s1, s2)
        mid = Span("B")
        fl.add_component_at_index(1, mid)
        assert fl._children[1] is mid


# =============================================================================
# Batch 4: Grid advanced
# =============================================================================


class TestGridAdvanced:
    def test_column_frozen(self):
        t = tree()
        grid = Grid()
        col = grid.add_column("name")
        col.set_frozen(True)
        grid.set_items([{"name": "Alice"}])
        grid._attach(t)
        assert col._frozen is True

    def test_column_frozen_to_end(self):
        grid = Grid()
        col = grid.add_column("name")
        col.set_frozen_to_end(True)
        assert col._frozen_to_end is True

    def test_column_visible(self):
        grid = Grid()
        col = grid.add_column("name")
        col.set_visible(False)
        assert col.is_visible() is False

    def test_column_key(self):
        grid = Grid()
        col = grid.add_column("name").set_key("name-key")
        assert col.get_key() == "name-key"

    def test_get_column_by_key(self):
        grid = Grid()
        col = grid.add_column("name").set_key("my-key")
        found = grid.get_column_by_key("my-key")
        assert found is col

    def test_get_column_by_key_not_found(self):
        grid = Grid()
        grid.add_column("name")
        assert grid.get_column_by_key("missing") is None

    def test_remove_column(self):
        grid = Grid()
        col = grid.add_column("name")
        grid.remove_column(col)
        assert col not in grid._columns

    def test_remove_all_columns(self):
        grid = Grid()
        grid.add_column("a")
        grid.add_column("b")
        grid.remove_all_columns()
        assert len(grid._columns) == 0

    def test_all_rows_visible(self):
        t = tree()
        grid = Grid()
        grid.add_column("name")
        grid.set_items([{"name": "A"}])
        grid.set_all_rows_visible(True)
        grid._attach(t)
        assert grid.is_all_rows_visible() is True
        assert grid.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "allRowsVisible") is True

    def test_scroll_to_index(self):
        t = tree()
        grid = Grid()
        grid.add_column("name")
        grid.set_items([{"name": f"Item {i}"} for i in range(100)])
        grid._attach(t)
        grid.scroll_to_index(50)
        # Verify JS command queued
        assert any("scrollToIndex" in str(cmd) for cmd in t._pending_execute)

    def test_recalculate_column_widths(self):
        t = tree()
        grid = Grid()
        grid.add_column("name")
        grid.set_items([{"name": "A"}])
        grid._attach(t)
        grid.recalculate_column_widths()
        assert any("recalculateColumnWidths" in str(cmd) for cmd in t._pending_execute)

    def test_set_empty_state_text(self):
        t = tree()
        grid = Grid()
        grid.add_column("name")
        grid.set_items([])
        grid.set_empty_state_text("No items found")
        grid._attach(t)

    def test_append_header_row(self):
        t = tree()
        grid = Grid()
        grid.add_column("name")
        grid.set_items([])
        grid._attach(t)
        row = grid.append_header_row()
        assert row is not None


# =============================================================================
# Batch 5: Selection components
# =============================================================================


class TestSelectionComponents:
    def test_select_empty_selection_allowed(self):
        t = tree()
        sel = Select()
        sel.set_empty_selection_allowed(True)
        sel._attach(t)
        assert sel.is_empty_selection_allowed() is True

    def test_select_empty_selection_caption(self):
        sel = Select()
        sel.set_empty_selection_caption("-- Choose --")

    def test_select_overlay_width(self):
        t = tree()
        sel = Select()
        sel._attach(t)
        sel.set_overlay_width("200px")

    def test_select_prefix_component(self):
        t = tree()
        sel = Select()
        sel._attach(t)
        icon = Span("$")
        sel.set_prefix_component(icon)
        assert icon.element.get_attribute("slot") == "prefix"

    def test_checkbox_group_select(self):
        cg = CheckboxGroup()
        cg.set_items(["A", "B", "C"])
        cg.select("A", "B")
        assert cg.get_value() == {"A", "B"}

    def test_checkbox_group_deselect(self):
        cg = CheckboxGroup()
        cg.set_items(["A", "B", "C"])
        cg.set_value({"A", "B", "C"})
        cg.deselect("B")
        assert cg.get_value() == {"A", "C"}

    def test_checkbox_group_deselect_all(self):
        cg = CheckboxGroup()
        cg.set_items(["A", "B"])
        cg.set_value({"A", "B"})
        cg.deselect_all()
        assert cg.get_value() == set()

    def test_checkbox_group_item_enabled_provider(self):
        cg = CheckboxGroup()
        cg.set_items(["A", "B", "C"])
        cg.set_item_enabled_provider(lambda item: item != "B")
        assert cg._item_enabled_provider is not None

    def test_radio_button_group_item_enabled_provider(self):
        rbg = RadioButtonGroup()
        rbg.set_items(["A", "B", "C"])
        rbg.set_item_enabled_provider(lambda item: item != "C")
        assert rbg._item_enabled_provider is not None

    def test_multi_select_list_box_select(self):
        mslb = MultiSelectListBox()
        mslb.set_items(["X", "Y", "Z"])
        mslb.select("X", "Z")
        assert mslb.get_value() == {"X", "Z"}

    def test_multi_select_list_box_deselect(self):
        mslb = MultiSelectListBox()
        mslb.set_items(["X", "Y", "Z"])
        mslb.set_value({"X", "Y", "Z"})
        mslb.deselect("Y")
        assert mslb.get_value() == {"X", "Z"}

    def test_multi_select_list_box_deselect_all(self):
        mslb = MultiSelectListBox()
        mslb.set_items(["X", "Y"])
        mslb.set_value({"X", "Y"})
        mslb.deselect_all()
        assert mslb.get_value() == set()


# =============================================================================
# Batch 6: Dialog/Notification/Popover/ConfirmDialog/Button extras
# =============================================================================


class TestDialogExtras:
    def test_dialog_remove(self):
        t = tree()
        dialog = Dialog()
        s = Span("test")
        dialog.add(s)
        dialog._attach(t)
        dialog.remove(s)
        assert s not in dialog._children

    def test_dialog_set_top(self):
        t = tree()
        dialog = Dialog()
        dialog._attach(t)
        dialog.set_top("100px")

    def test_dialog_set_left(self):
        t = tree()
        dialog = Dialog()
        dialog._attach(t)
        dialog.set_left("50px")


class TestConfirmDialogExtras:
    def test_close_on_esc(self):
        t = tree()
        cd = ConfirmDialog()
        cd.set_close_on_esc(False)
        cd._attach(t)
        assert cd.is_close_on_esc() is False

    def test_opened_change_listener(self):
        t = tree()
        cd = ConfirmDialog()
        cd._attach(t)
        events = []
        cd.add_opened_change_listener(lambda e: events.append(e))
        cd.open()
        cd.close()
        assert len(events) == 2


class TestNotificationExtras:
    def test_notification_remove(self):
        t = tree()
        notif = Notification()
        s = Span("msg")
        notif.add(s)
        notif._attach(t)
        notif.remove(s)
        assert s not in notif._children


class TestPopoverExtras:
    def test_popover_remove(self):
        t = tree()
        pop = Popover()
        s = Span("content")
        pop.add(s)
        pop._attach(t)
        pop.remove(s)
        assert s not in pop._children

    def test_popover_set_autofocus(self):
        pop = Popover()
        pop.set_autofocus(True)

    def test_popover_set_backdrop_visible(self):
        pop = Popover()
        pop.set_backdrop_visible(True)

    def test_popover_hover_delay(self):
        pop = Popover()
        pop.set_hover_delay(200)

    def test_popover_focus_delay(self):
        pop = Popover()
        pop.set_focus_delay(150)

    def test_popover_hide_delay(self):
        pop = Popover()
        pop.set_hide_delay(300)


class TestButtonExtras:
    def test_set_autofocus(self):
        t = tree()
        btn = Button("Submit")
        btn._attach(t)
        btn.set_autofocus(True)
        assert btn.is_autofocus() is True
        assert btn.element.get_attribute("autofocus") == ""

    def test_set_autofocus_false(self):
        t = tree()
        btn = Button("Submit")
        btn._attach(t)
        btn.set_autofocus(True)
        btn.set_autofocus(False)
        assert btn.is_autofocus() is False

    def test_click(self):
        events = []
        btn = Button("OK")
        btn.add_click_listener(lambda e: events.append("clicked"))
        btn.click()
        assert events == ["clicked"]


# =============================================================================
# Batch 7: Tabs/TabSheet/SideNav/Details/Accordion/MenuBar/ContextMenu
# =============================================================================


class TestTabsExtras:
    def test_add_tab_at_index(self):
        t = tree()
        t1 = Tab("First")
        t3 = Tab("Third")
        tabs = Tabs(t1, t3)
        tabs._attach(t)
        t2 = Tab("Second")
        tabs.add_tab_at_index(1, t2)
        assert tabs._tabs[1] is t2

    def test_add_tab_as_first(self):
        t = tree()
        t2 = Tab("Second")
        tabs = Tabs(t2)
        tabs._attach(t)
        t1 = Tab("First")
        tabs.add_tab_as_first(t1)
        assert tabs._tabs[0] is t1


class TestTabExtras:
    def test_tab_set_flex_grow(self):
        t = tree()
        tab = Tab("Test")
        tab._attach(t)
        tab.set_flex_grow(2.0)


class TestTabSheetExtras:
    def test_get_tab_by_content(self):
        ts = TabSheet()
        content = Span("Content")
        tab = ts.add("My Tab", content)
        found = ts.get_tab(content)
        assert found is tab

    def test_get_component_by_tab(self):
        ts = TabSheet()
        content = Span("Content")
        tab = ts.add("My Tab", content)
        found = ts.get_component(tab)
        assert found is content


class TestSideNavExtras:
    def test_side_nav_expanded(self):
        nav = SideNav()
        nav.set_expanded(False)
        assert nav.is_expanded() is False

    def test_side_nav_get_items(self):
        nav = SideNav()
        item = SideNavItem("Home", "/")
        nav.add_item(item)
        assert len(nav.get_items()) == 1
        assert nav.get_items()[0] is item

    def test_side_nav_remove(self):
        nav = SideNav()
        item = SideNavItem("Home", "/")
        nav.add_item(item)
        nav.remove(item)
        assert len(nav.get_items()) == 0

    def test_side_nav_remove_all(self):
        nav = SideNav()
        nav.add_item(SideNavItem("A", "/a"))
        nav.add_item(SideNavItem("B", "/b"))
        nav.remove_all()
        assert len(nav.get_items()) == 0


class TestSideNavItemExtras:
    def test_suffix_component(self):
        t = tree()
        item = SideNavItem("Home", "/")
        item._attach(t)
        badge = Span("3")
        item.set_suffix_component(badge)
        assert badge.element.get_attribute("slot") == "suffix"

    def test_get_items(self):
        item = SideNavItem("Parent")
        child = SideNavItem("Child", "/child")
        item.add_item(child)
        assert len(item.get_items()) == 1

    def test_remove(self):
        item = SideNavItem("Parent")
        child = SideNavItem("Child", "/child")
        item.add_item(child)
        item.remove(child)
        assert len(item.get_items()) == 0

    def test_remove_all(self):
        item = SideNavItem("Parent")
        item.add_item(SideNavItem("A", "/a"))
        item.add_item(SideNavItem("B", "/b"))
        item.remove_all()
        assert len(item.get_items()) == 0


class TestDetailsExtras:
    def test_get_summary(self):
        d = Details("Summary")
        assert d.get_summary() == "Summary"

    def test_get_content(self):
        s = Span("Content")
        d = Details("Summary", s)
        assert len(d.get_content()) == 1
        assert d.get_content()[0] is s

    def test_remove(self):
        t = tree()
        s = Span("Content")
        d = Details("Summary", s)
        d._attach(t)
        d.remove(s)
        assert len(d.get_content()) == 0

    def test_remove_all(self):
        s1 = Span("A")
        s2 = Span("B")
        d = Details("Summary", s1, s2)
        d.remove_all()
        assert len(d.get_content()) == 0

    def test_add_component_at_index(self):
        d = Details("Summary")
        s1 = Span("A")
        s2 = Span("C")
        d.add_content(s1, s2)
        mid = Span("B")
        d.add_component_at_index(1, mid)
        assert d._content[1] is mid


class TestAccordionExtras:
    def test_add_panel_directly(self):
        acc = Accordion()
        panel = AccordionPanel("Summary", Span("Content"))
        result = acc.add(panel)
        assert result is panel
        assert panel in acc.get_panels()

    def test_remove_panel(self):
        t = tree()
        acc = Accordion()
        panel = acc.add("Panel", Span("Content"))
        acc._attach(t)
        acc.remove(panel)
        assert panel not in acc.get_panels()

    def test_open_by_panel(self):
        t = tree()
        acc = Accordion()
        p1 = acc.add("First", Span("A"))
        p2 = acc.add("Second", Span("B"))
        acc._attach(t)
        acc.open(p2)
        assert acc.get_opened_index() == 1


class TestMenuBarExtras:
    def test_close(self):
        t = tree()
        mb = MenuBar()
        mb.add_item("File")
        mb._attach(t)
        mb.close()  # Should queue JS command

    def test_remove(self):
        mb = MenuBar()
        item = mb.add_item("File")
        mb.remove(item)
        assert item not in mb.get_items()

    def test_remove_all(self):
        mb = MenuBar()
        mb.add_item("File")
        mb.add_item("Edit")
        mb.remove_all()
        assert len(mb.get_items()) == 0


class TestContextMenuExtras:
    def test_is_opened(self):
        cm = ContextMenu()
        assert cm.is_opened() is False

    def test_add_opened_change_listener(self):
        cm = ContextMenu()
        events = []
        cm.add_opened_change_listener(lambda e: events.append(e))
        assert len(cm._opened_change_listeners) == 1

    def test_remove(self):
        cm = ContextMenu()
        item = cm.add_item("Delete")
        cm.remove(item)
        assert item not in cm.get_items()

    def test_remove_all(self):
        cm = ContextMenu()
        cm.add_item("Copy")
        cm.add_item("Paste")
        cm.remove_all()
        assert len(cm.get_items()) == 0


# =============================================================================
# Batch 7: Upload slotted components
# =============================================================================


class TestUploadExtras:
    def test_set_upload_button(self):
        t = tree()
        upload = Upload()
        upload._attach(t)
        btn = Button("Upload File")
        upload.set_upload_button(btn)
        assert upload.get_upload_button() is btn
        assert btn.element.get_attribute("slot") == "add-button"

    def test_set_drop_label(self):
        t = tree()
        upload = Upload()
        upload._attach(t)
        label = Span("Drop files here")
        upload.set_drop_label(label)
        assert upload.get_drop_label() is label
        assert label.element.get_attribute("slot") == "drop-label"

    def test_set_drop_label_icon(self):
        t = tree()
        upload = Upload()
        upload._attach(t)
        icon = Span("icon")
        upload.set_drop_label_icon(icon)
        assert upload.get_drop_label_icon() is icon
        assert icon.element.get_attribute("slot") == "drop-label-icon"

    def test_clear_file_list(self):
        t = tree()
        upload = Upload()
        upload._attach(t)
        upload.clear_file_list()
        # Verify JS command queued
        assert any("files" in str(cmd) for cmd in t._pending_execute)

    def test_upload_button_in_attach(self):
        t = tree()
        upload = Upload()
        btn = Button("Custom Upload")
        upload.set_upload_button(btn)
        upload._attach(t)
        assert btn._element is not None
        assert btn.element.get_attribute("slot") == "add-button"


# =============================================================================
# Batch 7: HTML elements
# =============================================================================


class TestHtmlElements:
    def test_h5(self):
        t = tree()
        h = H5("Heading 5")
        h._attach(t)
        assert h._tag == "h5"
        assert h.get_text() == "Heading 5"

    def test_h6(self):
        h = H6("Heading 6")
        assert h._tag == "h6"
        assert h.get_text() == "Heading 6"

    def test_pre(self):
        p = Pre("code here")
        assert p._tag == "pre"
        assert p.get_text() == "code here"

    def test_native_label(self):
        lbl = NativeLabel("Name:")
        assert lbl._tag == "label"
        assert lbl.get_text() == "Name:"

    def test_hr(self):
        hr = Hr()
        assert hr._tag == "hr"

    def test_anchor(self):
        t = tree()
        a = Anchor("https://example.com", "Example")
        a._attach(t)
        assert a._tag == "a"
        assert a.get_href() == "https://example.com"
        assert a.get_text() == "Example"
        assert a.element.get_attribute("href") == "https://example.com"

    def test_anchor_set_target(self):
        t = tree()
        a = Anchor("https://example.com", "Example")
        a.set_target("_blank")
        a._attach(t)
        assert a.get_target() == "_blank"
        assert a.element.get_attribute("target") == "_blank"

    def test_anchor_set_href_after_attach(self):
        t = tree()
        a = Anchor()
        a._attach(t)
        a.set_href("https://vaadin.com")
        assert a.get_href() == "https://vaadin.com"
        assert a.element.get_attribute("href") == "https://vaadin.com"

    def test_iframe(self):
        t = tree()
        iframe = IFrame("https://example.com")
        iframe._attach(t)
        assert iframe._tag == "iframe"
        assert iframe.get_src() == "https://example.com"
        assert iframe.element.get_attribute("src") == "https://example.com"

    def test_iframe_set_src(self):
        t = tree()
        iframe = IFrame()
        iframe._attach(t)
        iframe.set_src("https://vaadin.com")
        assert iframe.get_src() == "https://vaadin.com"

    def test_section(self):
        t = tree()
        s = Section("content")
        s._attach(t)
        assert s._tag == "section"

    def test_nav(self):
        n = Nav()
        assert n._tag == "nav"

    def test_main(self):
        m = Main()
        assert m._tag == "main"

    def test_article(self):
        a = Article("content")
        assert a._tag == "article"
        assert a.get_text() == "content"

    def test_aside(self):
        a = Aside()
        assert a._tag == "aside"

    def test_section_add_children(self):
        t = tree()
        s = Section()
        s.add(Span("child"))
        s._attach(t)
        assert len(s._children) == 1


# =============================================================================
# Batch 7: Binder
# =============================================================================


class TestBinderExtras:
    def test_remove_binding_by_instance(self):
        binder = Binder()
        field = TextField()
        binding = binder.for_field(field).bind(
            lambda b: getattr(b, "name", ""),
            lambda b, v: setattr(b, "name", v),
        )
        assert len(binder._bindings) == 1
        binder.remove_binding(binding)
        assert len(binder._bindings) == 0

    def test_remove_binding_by_field(self):
        binder = Binder()
        field = TextField()
        binder.for_field(field).bind(
            lambda b: getattr(b, "name", ""),
            lambda b, v: setattr(b, "name", v),
        )
        binder.remove_binding(field)
        assert len(binder._bindings) == 0

    def test_remove_bean(self):
        binder = Binder()
        binder.set_bean({"name": "Alice"})
        assert binder.get_bean() is not None
        binder.remove_bean()
        assert binder.get_bean() is None


# =============================================================================
# Batch 7: SplitLayout remove
# =============================================================================


class TestSplitLayoutExtras:
    def test_remove_primary(self):
        t = tree()
        sl = SplitLayout()
        primary = Span("primary")
        sl.add_to_primary(primary)
        sl._attach(t)
        sl.remove(primary)
        assert sl.get_primary_component() is None

    def test_remove_secondary(self):
        t = tree()
        sl = SplitLayout()
        secondary = Span("secondary")
        sl.add_to_secondary(secondary)
        sl._attach(t)
        sl.remove(secondary)
        assert sl.get_secondary_component() is None


# =============================================================================
# Batch 7: Card remove
# =============================================================================


class TestCardExtras:
    def test_remove_specific(self):
        t = tree()
        card = Card()
        s1 = Span("A")
        s2 = Span("B")
        card.add(s1, s2)
        card._attach(t)
        card.remove(s1)
        assert s1 not in card._children
        assert s2 in card._children


# =============================================================================
# Batch 7: MasterDetailLayout extras
# =============================================================================


class TestMasterDetailLayoutExtras:
    def test_get_detail_size(self):
        t = tree()
        mdl = MasterDetailLayout()
        mdl.set_detail_size("400px")
        mdl._attach(t)
        assert mdl.get_detail_size() == "400px"

    def test_get_master_min_size(self):
        t = tree()
        mdl = MasterDetailLayout()
        mdl.set_master_min_size("300px")
        mdl._attach(t)
        assert mdl.get_master_min_size() == "300px"

    def test_set_detail_min_size(self):
        t = tree()
        mdl = MasterDetailLayout()
        mdl.set_detail_min_size("200px")
        mdl._attach(t)
        assert mdl.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "detailMinSize") == "200px"

    def test_set_orientation(self):
        t = tree()
        mdl = MasterDetailLayout()
        mdl.set_orientation("vertical")
        mdl._attach(t)
        assert mdl.get_orientation() == "vertical"

    def test_set_containment(self):
        t = tree()
        mdl = MasterDetailLayout()
        mdl.set_containment("viewport")
        mdl._attach(t)
        assert mdl.element.node.get(Feature.ELEMENT_PROPERTY_MAP, "containment") == "viewport"

    def test_add_backdrop_click_listener_before_attach(self):
        t = tree()
        mdl = MasterDetailLayout()
        events = []
        mdl.add_backdrop_click_listener(lambda e: events.append(e))
        mdl._attach(t)
        # Verify listener was registered
        assert "backdrop-click" in mdl.element._listeners

    def test_add_detail_escape_press_listener(self):
        t = tree()
        mdl = MasterDetailLayout()
        events = []
        mdl.add_detail_escape_press_listener(lambda e: events.append(e))
        mdl._attach(t)
        assert "detail-escape-press" in mdl.element._listeners
