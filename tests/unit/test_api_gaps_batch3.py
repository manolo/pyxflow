"""Tests for API gaps Batch 3: layout polish, Select empty selection,
ValueChangeMode, and set_i18n.
"""

from vaadin.flow.components import (
    DatePicker, DateTimePicker, EmailField, HorizontalLayout, NumberField,
    PasswordField, Select, Span, TextArea, TextField, TimePicker,
    Upload, ValueChangeMode, VerticalLayout,
)
from vaadin.flow.components.login import LoginForm, LoginOverlay
from vaadin.flow.components.message_input import MessageInput
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


def tree():
    return StateTree()


# =============================================================================
# Layout polish: get_flex_grow, add_and_expand
# =============================================================================


class TestLayoutGetFlexGrow:
    def test_vertical_get_flex_grow_default(self):
        t = tree()
        vl = VerticalLayout()
        btn = Span("A")
        vl._attach(t)
        vl.add(btn)
        assert vl.get_flex_grow(btn) == 0

    def test_vertical_get_flex_grow_after_set(self):
        t = tree()
        vl = VerticalLayout()
        btn = Span("A")
        vl._attach(t)
        vl.add(btn)
        vl.set_flex_grow(2.5, btn)
        assert vl.get_flex_grow(btn) == 2.5

    def test_horizontal_get_flex_grow_default(self):
        t = tree()
        hl = HorizontalLayout()
        btn = Span("A")
        hl._attach(t)
        hl.add(btn)
        assert hl.get_flex_grow(btn) == 0

    def test_horizontal_get_flex_grow_after_set(self):
        t = tree()
        hl = HorizontalLayout()
        btn = Span("A")
        hl._attach(t)
        hl.add(btn)
        hl.set_flex_grow(3.0, btn)
        assert hl.get_flex_grow(btn) == 3.0


class TestLayoutAddAndExpand:
    def test_vertical_add_and_expand(self):
        t = tree()
        vl = VerticalLayout()
        vl._attach(t)
        a = Span("A")
        b = Span("B")
        vl.add_and_expand(a, b)
        assert a in vl._children
        assert b in vl._children
        assert a in vl._expanded_components
        assert b in vl._expanded_components
        assert a.element.get_style().get("flex-grow") == "1"
        assert b.element.get_style().get("flex-grow") == "1"

    def test_horizontal_add_and_expand(self):
        t = tree()
        hl = HorizontalLayout()
        hl._attach(t)
        a = Span("A")
        b = Span("B")
        hl.add_and_expand(a, b)
        assert a in hl._children
        assert b in hl._children
        assert a in hl._expanded_components
        assert b in hl._expanded_components


class TestHorizontalLayoutWrap:
    def test_set_wrap(self):
        hl = HorizontalLayout()
        hl.set_wrap(True)
        assert hl.is_wrap() is True

    def test_set_wrap_false(self):
        hl = HorizontalLayout()
        hl.set_wrap(True)
        hl.set_wrap(False)
        assert hl.is_wrap() is False


# =============================================================================
# Select: empty selection
# =============================================================================


class TestSelectEmptySelection:
    def test_set_empty_selection_allowed(self):
        t = tree()
        sel = Select()
        sel.set_items("A", "B", "C")
        sel.set_empty_selection_allowed(True)
        sel._attach(t)
        # The list-box should have 4 children (1 empty + 3 items)
        children = sel._list_box._children
        assert len(children) == 4

    def test_empty_item_has_empty_value(self):
        t = tree()
        sel = Select()
        sel.set_items("A", "B")
        sel.set_empty_selection_allowed(True)
        sel._attach(t)
        # First child is the empty item
        empty_item = sel._list_box._children[0]
        props = empty_item._features.get(Feature.ELEMENT_PROPERTY_MAP, {})
        assert props.get("value") == ""

    def test_empty_selection_caption(self):
        t = tree()
        sel = Select()
        sel.set_items("A", "B")
        sel.set_empty_selection_allowed(True)
        sel.set_empty_selection_caption("-- Choose --")
        sel._attach(t)
        # The empty item's text node should have the caption
        empty_item = sel._empty_item_node
        text_node = empty_item._children[0]
        text = text_node._features.get(Feature.TEXT_NODE, {}).get("text")
        assert text == "-- Choose --"

    def test_set_empty_selection_caption_after_attach(self):
        t = tree()
        sel = Select()
        sel.set_items("X", "Y")
        sel.set_empty_selection_allowed(True)
        sel._attach(t)
        sel.set_empty_selection_caption("None")
        text_node = sel._empty_text_node
        text = text_node._features.get(Feature.TEXT_NODE, {}).get("text")
        assert text == "None"

    def test_not_allowed_no_empty_item(self):
        t = tree()
        sel = Select()
        sel.set_items("A", "B")
        sel._attach(t)
        children = sel._list_box._children
        assert len(children) == 2

    def test_disable_empty_selection_after_attach(self):
        t = tree()
        sel = Select()
        sel.set_items("A")
        sel.set_empty_selection_allowed(True)
        sel._attach(t)
        assert len(sel._list_box._children) == 2  # 1 empty + 1 item
        sel.set_empty_selection_allowed(False)
        assert len(sel._list_box._children) == 1  # empty removed
        assert sel._empty_item_node is None

    def test_is_empty_selection_allowed(self):
        sel = Select()
        assert sel.is_empty_selection_allowed() is False
        sel.set_empty_selection_allowed(True)
        assert sel.is_empty_selection_allowed() is True


# =============================================================================
# ValueChangeMode
# =============================================================================


class TestValueChangeMode:
    def test_default_mode_is_on_change(self):
        tf = TextField()
        assert tf.get_value_change_mode() == ValueChangeMode.ON_CHANGE

    def test_set_mode_eager(self):
        tf = TextField()
        tf.set_value_change_mode(ValueChangeMode.EAGER)
        assert tf.get_value_change_mode() == ValueChangeMode.EAGER

    def test_event_name_on_change(self):
        tf = TextField()
        assert tf._get_event_name() == "change"

    def test_event_name_eager(self):
        tf = TextField()
        tf.set_value_change_mode(ValueChangeMode.EAGER)
        assert tf._get_event_name() == "input"

    def test_event_name_lazy(self):
        tf = TextField()
        tf.set_value_change_mode(ValueChangeMode.LAZY)
        assert tf._get_event_name() == "input"

    def test_event_name_timeout(self):
        tf = TextField()
        tf.set_value_change_mode(ValueChangeMode.TIMEOUT)
        assert tf._get_event_name() == "input"

    def test_event_name_on_blur(self):
        tf = TextField()
        tf.set_value_change_mode(ValueChangeMode.ON_BLUR)
        assert tf._get_event_name() == "blur"

    def test_timeout_getter_setter(self):
        tf = TextField()
        assert tf.get_value_change_timeout() == 400
        tf.set_value_change_timeout(1000)
        assert tf.get_value_change_timeout() == 1000

    def test_attach_with_eager_mode(self):
        t = tree()
        tf = TextField()
        tf.set_value_change_mode(ValueChangeMode.EAGER)
        tf._attach(t)
        # Should have registered "input" listener, not "change"
        assert "input" in tf.element._listeners
        assert "change" not in tf.element._listeners

    def test_attach_with_on_blur_mode(self):
        t = tree()
        tf = TextField()
        tf.set_value_change_mode(ValueChangeMode.ON_BLUR)
        tf._attach(t)
        assert "blur" in tf.element._listeners
        assert "change" not in tf.element._listeners

    def test_text_area_value_change_mode(self):
        ta = TextArea()
        ta.set_value_change_mode(ValueChangeMode.EAGER)
        assert ta.get_value_change_mode() == ValueChangeMode.EAGER
        assert ta._get_event_name() == "input"

    def test_email_field_value_change_mode(self):
        ef = EmailField()
        ef.set_value_change_mode(ValueChangeMode.EAGER)
        assert ef.get_value_change_mode() == ValueChangeMode.EAGER
        assert ef._get_event_name() == "input"

    def test_password_field_value_change_mode(self):
        pf = PasswordField()
        pf.set_value_change_mode(ValueChangeMode.EAGER)
        assert pf.get_value_change_mode() == ValueChangeMode.EAGER
        assert pf._get_event_name() == "input"

    def test_number_field_value_change_mode(self):
        nf = NumberField()
        nf.set_value_change_mode(ValueChangeMode.EAGER)
        assert nf.get_value_change_mode() == ValueChangeMode.EAGER
        assert nf._get_event_name() == "input"

    def test_all_fields_default_on_change(self):
        """All text field types default to ON_CHANGE."""
        for cls in [TextField, TextArea, EmailField, PasswordField, NumberField]:
            field = cls()
            assert field.get_value_change_mode() == ValueChangeMode.ON_CHANGE, \
                f"{cls.__name__} default mode should be ON_CHANGE"


# =============================================================================
# set_i18n
# =============================================================================


class TestSetI18n:
    def test_upload_i18n(self):
        u = Upload()
        u.set_i18n({"addFiles": {"one": "Upload File"}})
        assert u.get_i18n() == {"addFiles": {"one": "Upload File"}}

    def test_upload_i18n_buffers_js(self):
        u = Upload()
        u.set_i18n({"dropFiles": {"one": "Drop file here"}})
        # Before attach, execute_js is buffered
        assert len(u._pending_execute_js) == 1

    def test_date_picker_i18n(self):
        dp = DatePicker()
        i18n = {"monthNames": ["Enero", "Febrero"]}
        dp.set_i18n(i18n)
        assert dp.get_i18n() == i18n

    def test_time_picker_i18n(self):
        tp = TimePicker()
        tp.set_i18n({"selector": "Time selector"})
        assert tp.get_i18n() == {"selector": "Time selector"}

    def test_date_time_picker_i18n(self):
        dtp = DateTimePicker()
        dtp.set_i18n({"dateLabel": "Fecha"})
        assert dtp.get_i18n() == {"dateLabel": "Fecha"}

    def test_login_form_i18n(self):
        lf = LoginForm()
        lf.set_i18n({"form": {"title": "Iniciar sesión"}})
        assert lf.get_i18n() == {"form": {"title": "Iniciar sesión"}}

    def test_login_overlay_i18n(self):
        lo = LoginOverlay()
        lo.set_i18n({"form": {"title": "Log in"}})
        assert lo.get_i18n() == {"form": {"title": "Log in"}}

    def test_message_input_i18n(self):
        mi = MessageInput()
        mi.set_i18n({"send": "Enviar", "message": "Mensaje"})
        assert mi.get_i18n() == {"send": "Enviar", "message": "Mensaje"}

    def test_get_i18n_default_none(self):
        dp = DatePicker()
        assert dp.get_i18n() is None

    def test_i18n_with_attach(self):
        t = tree()
        dp = DatePicker()
        dp.set_i18n({"monthNames": ["January"]})
        dp._attach(t)
        # After attach, buffered JS should have been flushed
        assert dp.get_i18n() == {"monthNames": ["January"]}


# =============================================================================
# ValueChangeMode enum values
# =============================================================================


class TestValueChangeModeEnum:
    def test_enum_values(self):
        assert ValueChangeMode.EAGER.value == "eager"
        assert ValueChangeMode.LAZY.value == "lazy"
        assert ValueChangeMode.TIMEOUT.value == "timeout"
        assert ValueChangeMode.ON_BLUR.value == "on_blur"
        assert ValueChangeMode.ON_CHANGE.value == "on_change"
