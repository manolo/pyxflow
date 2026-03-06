"""Tests for Drag and Drop API (DragSource, DropTarget)."""

import pytest
from pyxflow.components import (
    Div, Span, DragSource, DropTarget,
    DragStartEvent, DragEndEvent, DropEvent,
    EffectAllowed, DropEffect,
)
from pyxflow.core.state_tree import StateTree
from pyxflow.core.component import UI


@pytest.fixture
def tree():
    return StateTree()


@pytest.fixture
def ui(tree):
    return UI(tree)


# ---------------------------------------------------------------------------
#  EffectAllowed / DropEffect enums
# ---------------------------------------------------------------------------

class TestEnums:
    def test_effect_allowed_values(self):
        assert EffectAllowed.MOVE.value == "move"
        assert EffectAllowed.COPY.value == "copy"
        assert EffectAllowed.LINK.value == "link"
        assert EffectAllowed.COPY_MOVE.value == "copyMove"
        assert EffectAllowed.COPY_LINK.value == "copyLink"
        assert EffectAllowed.MOVE_LINK.value == "moveLink"
        assert EffectAllowed.ALL.value == "all"
        assert EffectAllowed.NONE.value == "none"
        assert EffectAllowed.UNINITIALIZED.value == "uninitialized"

    def test_drop_effect_values(self):
        assert DropEffect.MOVE.value == "move"
        assert DropEffect.COPY.value == "copy"
        assert DropEffect.LINK.value == "link"
        assert DropEffect.NONE.value == "none"

    def test_effect_allowed_is_str_subclass(self):
        assert isinstance(EffectAllowed.MOVE, str)
        assert EffectAllowed.MOVE.value == "move"

    def test_drop_effect_is_str_subclass(self):
        assert isinstance(DropEffect.COPY, str)
        assert DropEffect.COPY.value == "copy"


# ---------------------------------------------------------------------------
#  DragSource mixin
# ---------------------------------------------------------------------------

class TestDragSourceMixin:
    def test_set_draggable_before_attach(self, tree):
        """DragSource.configure sets draggable and buffers for attach."""
        div = Div()
        DragSource.configure(div)
        assert div.is_draggable() is True

    def test_set_draggable_after_attach(self, tree):
        """Draggable property is set on element after attach."""
        div = Div()
        DragSource.configure(div)
        div._attach(tree)
        assert div.element.get_property("draggable") == "true"

    def test_configure_returns_component(self):
        """configure() returns the same component for chaining."""
        div = Div()
        result = DragSource.configure(div)
        assert result is div

    def test_configure_not_draggable(self, tree):
        div = Div()
        DragSource.configure(div, draggable=False)
        assert div.is_draggable() is False
        div._attach(tree)
        assert div.element.get_property("draggable") == "false"

    def test_drag_data_stored_server_side(self):
        """Drag data is stored on the component, not sent to client."""
        div = Div()
        DragSource.configure(div)
        div.set_drag_data("my-data")
        assert div.get_drag_data() == "my-data"

    def test_drag_data_default_none(self):
        div = Div()
        DragSource.configure(div)
        assert div.get_drag_data() is None

    def test_effect_allowed_before_attach(self, tree):
        div = Div()
        DragSource.configure(div)
        div.set_effect_allowed(EffectAllowed.COPY)
        assert div.get_effect_allowed() == EffectAllowed.COPY
        div._attach(tree)
        assert div.element.get_property("__effectAllowed") == "copy"

    def test_effect_allowed_after_attach(self, tree):
        div = Div()
        DragSource.configure(div)
        div._attach(tree)
        div.set_effect_allowed(EffectAllowed.MOVE)
        assert div.element.get_property("__effectAllowed") == "move"

    def test_default_effect_allowed(self):
        div = Div()
        DragSource.configure(div)
        assert div.get_effect_allowed() == EffectAllowed.UNINITIALIZED

    def test_drag_start_listener(self, tree, ui):
        """Drag start listeners are called with DragStartEvent."""
        div = Div()
        DragSource.configure(div)
        events = []
        div.add_drag_start_listener(lambda e: events.append(e))
        div._ui = ui
        div._attach(tree)
        # Simulate dragstart event
        div._on_dragstart({})
        assert len(events) == 1
        assert isinstance(events[0], DragStartEvent)
        assert events[0].get_component() is div

    def test_drag_end_listener(self, tree, ui):
        """Drag end listeners are called with DragEndEvent."""
        div = Div()
        DragSource.configure(div)
        events = []
        div.add_drag_end_listener(lambda e: events.append(e))
        div._ui = ui
        div._attach(tree)
        # Simulate dragend event with drop effect
        div._on_dragend({"event.dataTransfer.dropEffect": "move"})
        assert len(events) == 1
        assert isinstance(events[0], DragEndEvent)
        assert events[0].get_drop_effect() == DropEffect.MOVE
        assert events[0].is_successful() is True

    def test_drag_end_none_drop_effect(self, tree, ui):
        """DragEndEvent with 'none' drop effect is not successful."""
        div = Div()
        DragSource.configure(div)
        events = []
        div.add_drag_end_listener(lambda e: events.append(e))
        div._ui = ui
        div._attach(tree)
        div._on_dragend({"event.dataTransfer.dropEffect": "none"})
        assert events[0].get_drop_effect() == DropEffect.NONE
        assert events[0].is_successful() is False

    def test_drag_end_clear_data(self):
        """DragEndEvent.clear_drag_data() clears the drag data."""
        div = Div()
        DragSource.configure(div)
        div.set_drag_data("test")
        event = DragEndEvent(div)
        event.clear_drag_data()
        assert div.get_drag_data() is None


# ---------------------------------------------------------------------------
#  DropTarget mixin
# ---------------------------------------------------------------------------

class TestDropTargetMixin:
    def test_configure_sets_active(self, tree):
        div = Div()
        DropTarget.configure(div)
        assert div.is_active() is True

    def test_configure_active_false(self, tree):
        div = Div()
        DropTarget.configure(div, active=False)
        assert div.is_active() is False

    def test_configure_returns_component(self):
        result = DropTarget.configure(Div())
        assert isinstance(result, Div)

    def test_active_property_after_attach(self, tree):
        div = Div()
        DropTarget.configure(div)
        div._attach(tree)
        assert div.element.get_property("__active") is True

    def test_active_property_set_after_attach(self, tree):
        div = Div()
        DropTarget.configure(div)
        div._attach(tree)
        div.set_active(False)
        assert div.element.get_property("__active") is False
        assert div.is_active() is False

    def test_drop_effect_before_attach(self, tree):
        div = Div()
        DropTarget.configure(div)
        div.set_drop_effect(DropEffect.COPY)
        assert div.get_drop_effect() == DropEffect.COPY
        div._attach(tree)
        assert div.element.get_property("__dropEffect") == "copy"

    def test_drop_effect_after_attach(self, tree):
        div = Div()
        DropTarget.configure(div)
        div._attach(tree)
        div.set_drop_effect(DropEffect.LINK)
        assert div.element.get_property("__dropEffect") == "link"

    def test_default_drop_effect_none(self):
        div = Div()
        DropTarget.configure(div)
        assert div.get_drop_effect() is None

    def test_drop_listener(self, tree, ui):
        """Drop listeners receive DropEvent with drag source info."""
        # Set up drag source
        source = Div()
        DragSource.configure(source)
        source.set_drag_data("hello")
        source._ui = ui
        source._attach(tree)
        ui._active_drag_source = source

        # Set up drop target
        target = Div()
        DropTarget.configure(target)
        target._ui = ui
        events = []
        target.add_drop_listener(lambda e: events.append(e))
        target._attach(tree)

        # Simulate drop event
        target._on_drop({})
        assert len(events) == 1
        assert isinstance(events[0], DropEvent)
        assert events[0].get_drag_source_component() is source
        assert events[0].get_drag_data() == "hello"
        # Active drag source cleared after drop
        assert ui._active_drag_source is None

    def test_drop_listener_no_source(self, tree, ui):
        """Drop without active drag source (e.g. cross-browser)."""
        target = Div()
        DropTarget.configure(target)
        target._ui = ui
        events = []
        target.add_drop_listener(lambda e: events.append(e))
        target._attach(tree)

        target._on_drop({})
        assert events[0].get_drag_source_component() is None
        assert events[0].get_drag_data() is None


# ---------------------------------------------------------------------------
#  Active drag source tracking
# ---------------------------------------------------------------------------

class TestActiveDragSourceTracking:
    def test_dragstart_sets_active_source(self, tree, ui):
        div = Div()
        DragSource.configure(div)
        div._ui = ui
        div._attach(tree)

        # Simulate dragstart
        div._on_dragstart({})
        assert ui._active_drag_source is div

    def test_dragend_clears_active_source(self, tree, ui):
        div = Div()
        DragSource.configure(div)
        div._ui = ui
        div._attach(tree)

        ui._active_drag_source = div
        div._on_dragend({})
        assert ui._active_drag_source is None

    def test_ui_initializes_with_no_drag_source(self, ui):
        assert ui._active_drag_source is None


# ---------------------------------------------------------------------------
#  DragStartEvent
# ---------------------------------------------------------------------------

class TestDragStartEvent:
    def test_get_component(self):
        div = Div()
        event = DragStartEvent(div)
        assert event.get_component() is div

    def test_set_drag_data(self):
        div = Div()
        event = DragStartEvent(div)
        event.set_drag_data({"key": "value"})
        assert div._drag_data == {"key": "value"}


# ---------------------------------------------------------------------------
#  DragEndEvent
# ---------------------------------------------------------------------------

class TestDragEndEvent:
    def test_successful_move(self):
        event = DragEndEvent(Div(), DropEffect.MOVE)
        assert event.is_successful() is True
        assert event.get_drop_effect() == DropEffect.MOVE

    def test_not_successful_none(self):
        event = DragEndEvent(Div(), DropEffect.NONE)
        assert event.is_successful() is False

    def test_no_drop_effect(self):
        event = DragEndEvent(Div())
        assert event.get_drop_effect() is None
        assert event.is_successful() is False


# ---------------------------------------------------------------------------
#  DropEvent
# ---------------------------------------------------------------------------

class TestDropEvent:
    def test_with_source(self):
        source = Div()
        target = Div()
        event = DropEvent(target, drag_source=source, drag_data="data")
        assert event.get_component() is target
        assert event.get_drag_source_component() is source
        assert event.get_drag_data() == "data"

    def test_without_source(self):
        event = DropEvent(Div())
        assert event.get_drag_source_component() is None
        assert event.get_drag_data() is None


# ---------------------------------------------------------------------------
#  Event hash registration
# ---------------------------------------------------------------------------

class TestEventHashes:
    def test_dragstart_hash_exists(self):
        from pyxflow.server.uidl_handler import _DRAGSTART_HASH
        assert isinstance(_DRAGSTART_HASH, str)
        assert len(_DRAGSTART_HASH) > 0

    def test_dragend_hash_exists(self):
        from pyxflow.server.uidl_handler import _DRAGEND_HASH
        assert isinstance(_DRAGEND_HASH, str)
        assert len(_DRAGEND_HASH) > 0

    def test_drop_hash_exists(self):
        from pyxflow.server.uidl_handler import _DROP_HASH
        assert isinstance(_DROP_HASH, str)
        assert len(_DROP_HASH) > 0

    def test_dragend_hash_differs_from_dragstart(self):
        """Dragend has event data config, so hash should differ from empty."""
        from pyxflow.server.uidl_handler import _DRAGSTART_HASH, _DRAGEND_HASH
        assert _DRAGEND_HASH != _DRAGSTART_HASH


# ---------------------------------------------------------------------------
#  Mixin-as-class pattern
# ---------------------------------------------------------------------------

class DraggableDiv(Div, DragSource):
    """A Div that is a DragSource via class inheritance."""
    def __init__(self):
        super().__init__()
        self.set_draggable(True)


class DroppableDiv(Div, DropTarget):
    """A Div that is a DropTarget via class inheritance."""
    def __init__(self):
        super().__init__()
        self.set_active(True)


class TestMixinAsClass:
    def test_draggable_div(self, tree):
        d = DraggableDiv()
        assert d.is_draggable() is True
        d._attach(tree)
        assert d.element.get_property("draggable") == "true"

    def test_droppable_div(self, tree):
        d = DroppableDiv()
        assert d.is_active() is True
        d._attach(tree)
        assert d.element.get_property("__active") is True

    def test_isinstance_check(self):
        d = DraggableDiv()
        assert isinstance(d, DragSource)
        assert isinstance(d, Div)

    def test_configure_on_mixin_class(self, tree):
        """DragSource.configure on an already-DragSource component works."""
        d = DraggableDiv()
        result = DragSource.configure(d)
        assert result is d
        assert d.is_draggable() is True


# ---------------------------------------------------------------------------
#  set_drag_image
# ---------------------------------------------------------------------------

class TestSetDragImage:
    def test_set_drag_image_after_attach(self, tree):
        """set_drag_image on attached components calls execute_js immediately."""
        source = Div()
        DragSource.configure(source)
        source._attach(tree)

        img = Span()
        img._attach(tree)

        source.set_drag_image(img, 10, 20)
        # Should have queued an execute_js call
        assert not hasattr(source, "_pending_drag_image")

    def test_set_drag_image_before_attach(self, tree):
        """set_drag_image before attach buffers in _pending_drag_image."""
        source = Div()
        DragSource.configure(source)

        img = Span()
        source.set_drag_image(img, 5, 15)
        assert hasattr(source, "_pending_drag_image")
        assert source._pending_drag_image == (img, 5, 15)

    def test_set_drag_image_flushed_on_attach(self, tree):
        """_pending_drag_image is flushed during _attach when image is attached."""
        source = Div()
        DragSource.configure(source)

        img = Span()
        img._attach(tree)  # image already attached

        source.set_drag_image(img, 28, 28)
        assert hasattr(source, "_pending_drag_image")

        source._attach(tree)
        assert not hasattr(source, "_pending_drag_image")

    def test_set_drag_image_default_offsets(self, tree):
        """Default offsets are 0, 0."""
        source = Div()
        DragSource.configure(source)

        img = Span()
        source.set_drag_image(img)
        assert source._pending_drag_image == (img, 0, 0)

    def test_set_drag_image_flushed_when_image_attaches_after_source(self, tree):
        """Drag image is flushed when the image component attaches after the source."""
        source = Div()
        DragSource.configure(source)
        img = Span()

        source.set_drag_image(img, 20, 20)
        assert hasattr(source, "_pending_drag_image")

        # Source attaches first — image not yet attached, pending remains
        source._attach(tree)
        assert hasattr(source, "_pending_drag_image")
        assert hasattr(img, "_drag_image_refs")
        assert source in img._drag_image_refs

        # Image attaches later — pending is flushed
        img._attach(tree)
        assert not hasattr(source, "_pending_drag_image")
        assert not hasattr(img, "_drag_image_refs")

    def test_set_drag_image_multiple_sources_share_image(self, tree):
        """Multiple drag sources sharing one image component all flush on image attach."""
        src1 = Div()
        src2 = Div()
        DragSource.configure(src1)
        DragSource.configure(src2)
        img = Span()

        src1.set_drag_image(img, 10, 10)
        src2.set_drag_image(img, 20, 20)

        src1._attach(tree)
        src2._attach(tree)
        # Both pending, both registered as refs
        assert hasattr(src1, "_pending_drag_image")
        assert hasattr(src2, "_pending_drag_image")
        assert len(img._drag_image_refs) == 2

        img._attach(tree)
        assert not hasattr(src1, "_pending_drag_image")
        assert not hasattr(src2, "_pending_drag_image")
        assert not hasattr(img, "_drag_image_refs")

    def test_set_drag_image_both_attached_no_pending(self, tree):
        """When both source and image are already attached, no pending state is created."""
        source = Div()
        DragSource.configure(source)
        img = Span()

        source._attach(tree)
        img._attach(tree)

        source.set_drag_image(img, 5, 5)
        assert not hasattr(source, "_pending_drag_image")
        assert not hasattr(img, "_drag_image_refs")

    def test_set_drag_image_via_configure(self, tree):
        """set_drag_image works on components configured via static factory."""
        source = Div()
        DragSource.configure(source)
        img = Span()
        # Method should be bound via configure
        assert hasattr(source, "set_drag_image")
