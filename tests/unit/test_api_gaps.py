"""Tests for API gap implementations: HasReadOnly, remove_all, Grid item-click,
Dialog header/footer, Button disable-on-click."""

import pytest

from pyflow.components import (
    Button, Checkbox, CheckboxGroup, ComboBox, CustomField,
    DatePicker, DateTimePicker, Dialog, EmailField, FlexLayout,
    Grid, HorizontalLayout, IntegerField, ListBox, MultiSelectComboBox,
    MultiSelectListBox, Notification, NumberField, PasswordField, Popover,
    RadioButtonGroup, Card, Scroller, Select, Span, Tab, Tabs,
    TextArea, TextField, TimePicker, VerticalLayout,
    HasReadOnly,
)
from pyflow.core.state_tree import StateTree


def create_tree():
    return StateTree()


# =============================================================================
# 1. HasReadOnly mixin
# =============================================================================


class TestHasReadOnly:
    """Tests for HasReadOnly mixin API."""

    READ_ONLY_COMPONENTS = [
        TextField, EmailField, PasswordField, TextArea,
        NumberField, IntegerField, DatePicker, TimePicker, DateTimePicker,
        ComboBox, MultiSelectComboBox, Select, RadioButtonGroup, CheckboxGroup,
        Checkbox, CustomField, ListBox, MultiSelectListBox,
    ]

    @pytest.mark.parametrize("cls", READ_ONLY_COMPONENTS, ids=lambda c: c.__name__)
    def test_is_instance(self, cls):
        comp = cls()
        assert isinstance(comp, HasReadOnly)

    @pytest.mark.parametrize("cls", READ_ONLY_COMPONENTS, ids=lambda c: c.__name__)
    def test_default_not_read_only(self, cls):
        comp = cls()
        assert comp.is_read_only() is False

    @pytest.mark.parametrize("cls", READ_ONLY_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_read_only_before_attach(self, cls):
        comp = cls()
        comp.set_read_only(True)
        assert comp.is_read_only() is True

    @pytest.mark.parametrize("cls", READ_ONLY_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_read_only_after_attach(self, cls):
        tree = create_tree()
        comp = cls()
        comp._attach(tree)
        comp.set_read_only(True)
        assert comp.is_read_only() is True
        assert comp.element.node.get(1, "readonly") is True

    @pytest.mark.parametrize("cls", READ_ONLY_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_read_only_buffered(self, cls):
        """set_read_only before attach → flushed via _pending_properties."""
        tree = create_tree()
        comp = cls()
        comp.set_read_only(True)
        comp._attach(tree)
        assert comp.element.node.get(1, "readonly") is True

    @pytest.mark.parametrize("cls", READ_ONLY_COMPONENTS, ids=lambda c: c.__name__)
    def test_set_read_only_false(self, cls):
        tree = create_tree()
        comp = cls()
        comp._attach(tree)
        comp.set_read_only(True)
        comp.set_read_only(False)
        assert comp.is_read_only() is False
        assert comp.element.node.get(1, "readonly") is False


# =============================================================================
# 2. remove_all on container components
# =============================================================================


class TestRemoveAll:
    """Tests for remove_all on container components."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    # --- VerticalLayout ---

    def test_vertical_layout_remove_all(self, tree):
        vl = VerticalLayout()
        s1, s2 = Span("A"), Span("B")
        vl.add(s1, s2)
        vl._attach(tree)
        assert len(vl._children) == 2
        vl.remove_all()
        assert len(vl._children) == 0

    def test_vertical_layout_remove_all_before_attach(self):
        vl = VerticalLayout()
        s1 = Span("A")
        vl.add(s1)
        vl.remove_all()
        assert len(vl._children) == 0

    # --- HorizontalLayout ---

    def test_horizontal_layout_remove_all(self, tree):
        hl = HorizontalLayout()
        s1, s2 = Span("A"), Span("B")
        hl.add(s1, s2)
        hl._attach(tree)
        assert len(hl._children) == 2
        hl.remove_all()
        assert len(hl._children) == 0

    # --- FlexLayout ---

    def test_flex_layout_remove_all(self, tree):
        fl = FlexLayout()
        s1, s2 = Span("A"), Span("B")
        fl.add(s1, s2)
        fl._attach(tree)
        fl.remove_all()
        assert len(fl._children) == 0

    # --- Tabs ---

    def test_tabs_remove_all(self, tree):
        t1, t2 = Tab("A"), Tab("B")
        tabs = Tabs(t1, t2)
        tabs._attach(tree)
        assert tabs.get_tab_count() == 2
        tabs.remove_all()
        assert tabs.get_tab_count() == 0

    # --- Dialog ---

    def test_dialog_remove_all(self, tree):
        dialog = Dialog()
        dialog.add(Span("A"), Span("B"))
        dialog._attach(tree)
        assert len(dialog._children) == 2
        dialog.remove_all()
        assert len(dialog._children) == 0

    def test_dialog_remove_all_before_attach(self):
        dialog = Dialog()
        dialog.add(Span("A"))
        dialog.remove_all()
        assert len(dialog._children) == 0

    # --- Notification ---

    def test_notification_remove_all(self, tree):
        notif = Notification()
        notif.add(Span("A"), Span("B"))
        notif._attach(tree)
        assert len(notif._children) == 2
        notif.remove_all()
        assert len(notif._children) == 0

    # --- Popover ---

    def test_popover_remove_all(self, tree):
        popover = Popover()
        popover.add(Span("A"))
        popover._attach(tree)
        popover.remove_all()
        assert len(popover._children) == 0

    # --- Card ---

    def test_card_remove_all(self, tree):
        card = Card()
        card.add(Span("A"), Span("B"))
        card._attach(tree)
        card.remove_all()
        assert len(card._children) == 0

    # --- Scroller ---

    def test_scroller_remove_all(self, tree):
        scroller = Scroller()
        scroller.add(Span("A"))
        scroller._attach(tree)
        scroller.remove_all()
        assert len(scroller._children) == 0

    # --- CustomField ---

    def test_custom_field_remove_all(self, tree):
        cf = CustomField()
        cf.add(TextField(), TextField())
        cf._attach(tree)
        assert len(cf._children) == 2
        cf.remove_all()
        assert len(cf._children) == 0


# =============================================================================
# 3. Grid add_item_click_listener / add_item_double_click_listener
# =============================================================================


class TestGridItemClick:
    """Tests for Grid item click listeners."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_add_item_click_listener(self, tree):
        grid = Grid()
        grid.add_column("name")
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}])
        events = []
        grid.add_item_click_listener(lambda e: events.append(e))
        grid._attach(tree)

        # Simulate item-click event from client
        grid._handle_item_click({"event.detail.itemKey": "0"})
        assert len(events) == 1
        assert events[0]["item"]["name"] == "Alice"

    def test_add_item_double_click_listener(self, tree):
        grid = Grid()
        grid.add_column("name")
        grid.set_items([{"name": "Alice"}, {"name": "Bob"}])
        events = []
        grid.add_item_double_click_listener(lambda e: events.append(e))
        grid._attach(tree)

        grid._handle_item_double_click({"event.detail.itemKey": "1"})
        assert len(events) == 1
        assert events[0]["item"]["name"] == "Bob"

    def test_item_click_unknown_key(self, tree):
        grid = Grid()
        grid.add_column("name")
        grid.set_items([{"name": "Alice"}])
        events = []
        grid.add_item_click_listener(lambda e: events.append(e))
        grid._attach(tree)

        # Unknown key → no event fired
        grid._handle_item_click({"event.detail.itemKey": "999"})
        assert len(events) == 0

    def test_item_click_no_key(self, tree):
        grid = Grid()
        grid.add_column("name")
        grid.set_items([{"name": "Alice"}])
        events = []
        grid.add_item_click_listener(lambda e: events.append(e))
        grid._attach(tree)

        # Missing key → no event fired
        grid._handle_item_click({})
        assert len(events) == 0

    def test_item_click_registered_after_attach(self, tree):
        """Listener added after attach still registers event."""
        grid = Grid()
        grid.add_column("name")
        grid.set_items([{"name": "Alice"}])
        grid._attach(tree)

        events = []
        grid.add_item_click_listener(lambda e: events.append(e))

        # Event listener should be registered
        assert "item-click" in grid.element._listeners
        grid._handle_item_click({"event.detail.itemKey": "0"})
        assert len(events) == 1

    def test_multiple_item_click_listeners(self, tree):
        grid = Grid()
        grid.add_column("name")
        grid.set_items([{"name": "Alice"}])
        events1, events2 = [], []
        grid.add_item_click_listener(lambda e: events1.append(e))
        grid.add_item_click_listener(lambda e: events2.append(e))
        grid._attach(tree)

        grid._handle_item_click({"event.detail.itemKey": "0"})
        assert len(events1) == 1
        assert len(events2) == 1


# =============================================================================
# 4. Dialog get_header / get_footer
# =============================================================================


class TestDialogHeaderFooter:
    """Tests for Dialog header/footer sections."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_get_header_returns_section(self):
        dialog = Dialog()
        header = dialog.get_header()
        assert header is not None
        assert header._slot_name == "header"

    def test_get_footer_returns_section(self):
        dialog = Dialog()
        footer = dialog.get_footer()
        assert footer is not None
        assert footer._slot_name == "footer"

    def test_add_to_header_before_attach(self, tree):
        dialog = Dialog()
        btn = Button("Close")
        dialog.get_header().add(btn)
        dialog._attach(tree)
        assert len(dialog.get_header()._children) == 1
        # Header child should be attached
        assert btn._element is not None
        # Should have slot="header"
        assert btn.element.get_attribute("slot") == "header"

    def test_add_to_footer_before_attach(self, tree):
        dialog = Dialog()
        save = Button("Save")
        cancel = Button("Cancel")
        dialog.get_footer().add(save, cancel)
        dialog._attach(tree)
        assert len(dialog.get_footer()._children) == 2
        assert save.element.get_attribute("slot") == "footer"
        assert cancel.element.get_attribute("slot") == "footer"

    def test_add_to_header_after_attach(self, tree):
        dialog = Dialog()
        dialog._attach(tree)
        btn = Button("Close")
        dialog.get_header().add(btn)
        assert btn._element is not None
        assert btn.element.get_attribute("slot") == "header"

    def test_add_to_footer_after_attach(self, tree):
        dialog = Dialog()
        dialog._attach(tree)
        btn = Button("OK")
        dialog.get_footer().add(btn)
        assert btn._element is not None
        assert btn.element.get_attribute("slot") == "footer"

    def test_header_footer_in_virtual_child_ids(self, tree):
        dialog = Dialog()
        content = Span("Content")
        header_btn = Button("X")
        footer_btn = Button("OK")
        dialog.add(content)
        dialog.get_header().add(header_btn)
        dialog.get_footer().add(footer_btn)
        dialog._attach(tree)

        ids = dialog.element.get_property("virtualChildNodeIds")
        assert content.element.node_id in ids
        assert header_btn.element.node_id in ids
        assert footer_btn.element.node_id in ids

    def test_header_remove_all(self, tree):
        dialog = Dialog()
        dialog.get_header().add(Button("A"), Button("B"))
        dialog._attach(tree)
        assert len(dialog.get_header()._children) == 2
        dialog.get_header().remove_all()
        assert len(dialog.get_header()._children) == 0

    def test_footer_remove_all(self, tree):
        dialog = Dialog()
        dialog.get_footer().add(Button("OK"))
        dialog._attach(tree)
        dialog.get_footer().remove_all()
        assert len(dialog.get_footer()._children) == 0


# =============================================================================
# 5. Button set_disable_on_click
# =============================================================================


class TestButtonDisableOnClick:
    """Tests for Button disable-on-click."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_default_not_disabled(self):
        btn = Button("Click me")
        assert btn.is_disable_on_click() is False

    def test_set_disable_on_click_before_attach(self, tree):
        btn = Button("Submit")
        btn.set_disable_on_click(True)
        assert btn.is_disable_on_click() is True
        btn._attach(tree)
        assert btn.element.node.get(1, "disableOnClick") is True

    def test_set_disable_on_click_after_attach(self, tree):
        btn = Button("Submit")
        btn._attach(tree)
        btn.set_disable_on_click(True)
        assert btn.is_disable_on_click() is True
        assert btn.element.node.get(1, "disableOnClick") is True

    def test_set_disable_on_click_false(self, tree):
        btn = Button("Submit")
        btn.set_disable_on_click(True)
        btn._attach(tree)
        btn.set_disable_on_click(False)
        assert btn.is_disable_on_click() is False
        assert btn.element.node.get(1, "disableOnClick") is False
