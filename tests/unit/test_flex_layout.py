"""Tests for FlexLayout component."""

import pytest

from pyxflow.components.flex_layout import (
    Alignment,
    ContentAlignment,
    FlexDirection,
    FlexLayout,
    FlexWrap,
    JustifyContentMode,
)
from pyxflow.components.span import Span
from pyxflow.core.state_node import Feature
from pyxflow.core.state_tree import StateTree


class TestFlexLayout:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def _attach(self, tree, component):
        component._attach(tree)
        return component

    # --- Basic ---

    def test_tag_is_div(self):
        layout = FlexLayout()
        assert layout._tag == "div"

    def test_display_flex_on_attach(self, tree):
        layout = self._attach(tree, FlexLayout())
        assert layout.element.get_style().get("display") == "flex"

    def test_add_children_in_constructor(self, tree):
        a = Span("A")
        b = Span("B")
        layout = self._attach(tree, FlexLayout(a, b))
        assert len(layout._children) == 2

    def test_add_after_attach(self, tree):
        layout = FlexLayout()
        layout._ui = type("UI", (), {"tree": tree})()
        layout._attach(tree)
        s = Span("X")
        layout.add(s)
        assert s in layout._children

    def test_remove(self, tree):
        s = Span("X")
        layout = FlexLayout(s)
        layout._ui = type("UI", (), {"tree": tree})()
        layout._attach(tree)
        layout.remove(s)
        assert s not in layout._children

    # --- Flex direction ---

    def test_set_flex_direction(self, tree):
        layout = self._attach(tree, FlexLayout())
        layout.set_flex_direction(FlexDirection.COLUMN)
        assert layout.get_flex_direction() == FlexDirection.COLUMN

    def test_set_flex_direction_row_reverse(self, tree):
        layout = self._attach(tree, FlexLayout())
        layout.set_flex_direction(FlexDirection.ROW_REVERSE)
        assert layout.get_flex_direction() == FlexDirection.ROW_REVERSE

    def test_default_flex_direction(self, tree):
        layout = self._attach(tree, FlexLayout())
        assert layout.get_flex_direction() == FlexDirection.ROW

    def test_set_flex_direction_none_resets(self, tree):
        layout = self._attach(tree, FlexLayout())
        layout.set_flex_direction(FlexDirection.COLUMN)
        layout.set_flex_direction(None)
        assert layout.get_flex_direction() == FlexDirection.ROW

    # --- Flex wrap ---

    def test_set_flex_wrap(self, tree):
        layout = self._attach(tree, FlexLayout())
        layout.set_flex_wrap(FlexWrap.WRAP)
        assert layout.get_flex_wrap() == FlexWrap.WRAP

    def test_default_flex_wrap(self, tree):
        layout = self._attach(tree, FlexLayout())
        assert layout.get_flex_wrap() == FlexWrap.NOWRAP

    def test_flex_wrap_reverse(self, tree):
        layout = self._attach(tree, FlexLayout())
        layout.set_flex_wrap(FlexWrap.WRAP_REVERSE)
        assert layout.get_flex_wrap() == FlexWrap.WRAP_REVERSE

    # --- Justify content ---

    def test_set_justify_content(self, tree):
        layout = self._attach(tree, FlexLayout())
        layout.set_justify_content_mode(JustifyContentMode.CENTER)
        assert layout.get_justify_content_mode() == JustifyContentMode.CENTER

    def test_justify_content_between(self, tree):
        layout = self._attach(tree, FlexLayout())
        layout.set_justify_content_mode(JustifyContentMode.BETWEEN)
        assert layout.get_justify_content_mode() == JustifyContentMode.BETWEEN

    def test_justify_content_evenly(self, tree):
        layout = self._attach(tree, FlexLayout())
        layout.set_justify_content_mode(JustifyContentMode.EVENLY)
        assert layout.get_justify_content_mode() == JustifyContentMode.EVENLY

    def test_default_justify_content(self, tree):
        layout = self._attach(tree, FlexLayout())
        assert layout.get_justify_content_mode() == JustifyContentMode.START

    # --- Align items ---

    def test_set_align_items(self, tree):
        layout = self._attach(tree, FlexLayout())
        layout.set_align_items(Alignment.CENTER)
        assert layout.get_align_items() == Alignment.CENTER

    def test_default_align_items(self, tree):
        layout = self._attach(tree, FlexLayout())
        assert layout.get_align_items() == Alignment.STRETCH

    def test_set_align_items_none_resets(self, tree):
        layout = self._attach(tree, FlexLayout())
        layout.set_align_items(Alignment.CENTER)
        layout.set_align_items(None)
        assert layout.get_align_items() == Alignment.STRETCH

    # --- Align self ---

    def test_set_align_self(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        layout.set_align_self(Alignment.END, s)
        assert layout.get_align_self(s) == Alignment.END

    def test_default_align_self(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        assert layout.get_align_self(s) == Alignment.AUTO

    def test_set_align_self_none_resets(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        layout.set_align_self(Alignment.CENTER, s)
        layout.set_align_self(None, s)
        assert layout.get_align_self(s) == Alignment.AUTO

    # --- Align content ---

    def test_set_align_content(self, tree):
        layout = self._attach(tree, FlexLayout())
        layout.set_align_content(ContentAlignment.SPACE_BETWEEN)
        assert layout.get_align_content() == ContentAlignment.SPACE_BETWEEN

    def test_default_align_content(self, tree):
        layout = self._attach(tree, FlexLayout())
        assert layout.get_align_content() == ContentAlignment.STRETCH

    # --- Flex grow ---

    def test_set_flex_grow(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        layout.set_flex_grow(2, s)
        assert layout.get_flex_grow(s) == 2.0

    def test_default_flex_grow(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        assert layout.get_flex_grow(s) == 0.0

    def test_expand(self, tree):
        a = Span("A")
        b = Span("B")
        layout = self._attach(tree, FlexLayout(a, b))
        layout.expand(a, b)
        assert layout.get_flex_grow(a) == 1.0
        assert layout.get_flex_grow(b) == 1.0

    # --- Flex shrink ---

    def test_set_flex_shrink(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        layout.set_flex_shrink(0, s)
        assert layout.get_flex_shrink(s) == 0.0

    def test_default_flex_shrink(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        assert layout.get_flex_shrink(s) == 1.0

    # --- Flex basis ---

    def test_set_flex_basis(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        layout.set_flex_basis("200px", s)
        assert layout.get_flex_basis(s) == "200px"

    def test_default_flex_basis(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        assert layout.get_flex_basis(s) is None

    def test_set_flex_basis_none_removes(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        layout.set_flex_basis("100px", s)
        layout.set_flex_basis(None, s)
        assert layout.get_flex_basis(s) is None

    # --- Order ---

    def test_set_order(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        layout.set_order(3, s)
        assert layout.get_order(s) == 3

    def test_default_order(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        assert layout.get_order(s) == 0

    def test_set_order_zero_removes(self, tree):
        s = Span("X")
        layout = self._attach(tree, FlexLayout(s))
        layout.set_order(5, s)
        layout.set_order(0, s)
        assert layout.get_order(s) == 0

    # --- Multiple components ---

    def test_flex_grow_multiple(self, tree):
        a = Span("A")
        b = Span("B")
        layout = self._attach(tree, FlexLayout(a, b))
        layout.set_flex_grow(1, a, b)
        assert layout.get_flex_grow(a) == 1.0
        assert layout.get_flex_grow(b) == 1.0

    def test_align_self_multiple(self, tree):
        a = Span("A")
        b = Span("B")
        layout = self._attach(tree, FlexLayout(a, b))
        layout.set_align_self(Alignment.CENTER, a, b)
        assert layout.get_align_self(a) == Alignment.CENTER
        assert layout.get_align_self(b) == Alignment.CENTER
