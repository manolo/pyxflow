"""Tests for Grid Editor (inline row editing)."""

import pytest

from pyxflow.components.grid import (
    Grid, Column, EditorImpl, _EditorRenderer,
    EditorOpenEvent, EditorCloseEvent, EditorSaveEvent, EditorCancelEvent,
)
from pyxflow.components.text_field import TextField
from pyxflow.components.number_field import IntegerField
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature
from pyxflow.data.binder import Binder


class TestEditorEvents:
    """Test editor event classes."""

    def test_open_event(self):
        editor = EditorImpl(Grid())
        item = {"name": "Alice"}
        event = EditorOpenEvent(editor, item)
        assert event.editor is editor
        assert event.item is item

    def test_close_event(self):
        editor = EditorImpl(Grid())
        item = {"name": "Bob"}
        event = EditorCloseEvent(editor, item)
        assert event.editor is editor
        assert event.item is item

    def test_save_event(self):
        editor = EditorImpl(Grid())
        item = {"name": "Carol"}
        event = EditorSaveEvent(editor, item)
        assert event.editor is editor
        assert event.item is item

    def test_cancel_event(self):
        editor = EditorImpl(Grid())
        item = {"name": "Dan"}
        event = EditorCancelEvent(editor, item)
        assert event.editor is editor
        assert event.item is item


class TestEditorImpl:
    """Test EditorImpl state management."""

    def _make_grid_with_binder(self):
        """Create a Grid with columns, binder, and editor."""
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.add_column("age", header="Age")

        name_field = TextField()
        age_field = IntegerField()

        binder = Binder()
        binder.for_field(name_field).bind(
            lambda item: item.get("name", ""),
            lambda item, val: item.__setitem__("name", val),
        )
        binder.for_field(age_field).bind(
            lambda item: item.get("age", 0),
            lambda item, val: item.__setitem__("age", val),
        )

        editor = grid.get_editor()
        editor.set_binder(binder)
        return grid, editor, binder, name_field, age_field

    def test_lazy_creation(self):
        grid = Grid()
        editor = grid.get_editor()
        assert isinstance(editor, EditorImpl)
        assert grid.get_editor() is editor  # Same instance

    def test_initial_state(self):
        grid = Grid()
        editor = grid.get_editor()
        assert not editor.is_open()
        assert editor.get_item() is None
        assert editor.get_binder() is None
        assert not editor.is_buffered()

    def test_set_binder(self):
        grid = Grid()
        editor = grid.get_editor()
        binder = Binder()
        result = editor.set_binder(binder)
        assert result is editor
        assert editor.get_binder() is binder

    def test_set_buffered(self):
        grid = Grid()
        editor = grid.get_editor()
        result = editor.set_buffered(True)
        assert result is editor
        assert editor.is_buffered()

    def test_edit_item_requires_binder(self):
        grid = Grid()
        editor = grid.get_editor()
        with pytest.raises(ValueError, match="Binder must be set"):
            editor.edit_item({"name": "Alice"})

    def test_edit_item_requires_item(self):
        grid, editor, *_ = self._make_grid_with_binder()
        with pytest.raises(ValueError, match="Item must not be None"):
            editor.edit_item(None)

    def test_edit_item_opens(self):
        grid, editor, binder, name_field, age_field = self._make_grid_with_binder()
        item = {"name": "Alice", "age": 30}
        editor.edit_item(item)
        assert editor.is_open()
        assert editor.get_item() is item

    def test_edit_item_unbuffered_reads_bean(self):
        """In unbuffered mode, set_bean is called (auto-writes on change)."""
        grid, editor, binder, name_field, age_field = self._make_grid_with_binder()
        item = {"name": "Alice", "age": 30}
        editor.edit_item(item)
        assert name_field.get_value() == "Alice"
        assert age_field.get_value() == 30
        assert binder.get_bean() is item

    def test_edit_item_buffered_reads_bean(self):
        """In buffered mode, read_bean is called (no auto-write)."""
        grid, editor, binder, name_field, age_field = self._make_grid_with_binder()
        editor.set_buffered(True)
        item = {"name": "Bob", "age": 25}
        editor.edit_item(item)
        assert name_field.get_value() == "Bob"
        assert age_field.get_value() == 25
        assert binder.get_bean() is None  # read_bean doesn't set bean

    def test_buffered_save(self):
        grid, editor, binder, name_field, age_field = self._make_grid_with_binder()
        editor.set_buffered(True)
        item = {"name": "Carol", "age": 40}
        editor.edit_item(item)

        # Modify field values
        name_field.set_value("Carol Updated")
        age_field.set_value(41)

        # Save
        result = editor.save()
        assert result is True
        assert item["name"] == "Carol Updated"
        assert item["age"] == 41
        assert not editor.is_open()

    def test_buffered_cancel(self):
        grid, editor, binder, name_field, age_field = self._make_grid_with_binder()
        editor.set_buffered(True)
        item = {"name": "Dan", "age": 35}
        editor.edit_item(item)

        name_field.set_value("Dan Modified")
        editor.cancel()
        assert not editor.is_open()
        assert item["name"] == "Dan"  # Unchanged

    def test_buffered_ignores_double_edit(self):
        grid, editor, binder, name_field, age_field = self._make_grid_with_binder()
        editor.set_buffered(True)
        item_a = {"name": "A", "age": 1}
        editor.edit_item(item_a)
        editor.edit_item({"name": "B", "age": 2})  # Silently ignored
        assert editor.get_item() is item_a  # Still editing A

    def test_unbuffered_auto_close_on_new_edit(self):
        grid, editor, binder, name_field, age_field = self._make_grid_with_binder()
        item1 = {"name": "A", "age": 1}
        item2 = {"name": "B", "age": 2}
        close_events = []
        editor.add_close_listener(lambda e: close_events.append(e.item))

        editor.edit_item(item1)
        editor.edit_item(item2)
        assert editor.get_item() is item2
        assert len(close_events) == 1
        assert close_events[0] is item1

    def test_close_editor_unbuffered(self):
        grid, editor, binder, name_field, age_field = self._make_grid_with_binder()
        editor.edit_item({"name": "A", "age": 1})
        editor.close_editor()
        assert not editor.is_open()

    def test_close_editor_buffered_raises(self):
        grid, editor, binder, name_field, age_field = self._make_grid_with_binder()
        editor.set_buffered(True)
        editor.edit_item({"name": "A", "age": 1})
        with pytest.raises(ValueError, match="Use save"):
            editor.close_editor()

    def test_save_not_buffered_returns_false(self):
        grid, editor, binder, name_field, age_field = self._make_grid_with_binder()
        editor.edit_item({"name": "A", "age": 1})
        assert editor.save() is False

    def test_save_not_open_returns_false(self):
        grid, editor, binder, name_field, age_field = self._make_grid_with_binder()
        editor.set_buffered(True)
        assert editor.save() is False

    def test_generate_data_editing_item(self):
        grid = Grid()
        editor = grid.get_editor()
        editor._edited = {"name": "Alice"}

        connector_item = {"key": "0"}
        editor.generate_data(editor._edited, connector_item)
        assert connector_item["_editing"] is True

    def test_generate_data_non_editing_item(self):
        grid = Grid()
        editor = grid.get_editor()
        editor._edited = {"name": "Alice"}

        other_item = {"name": "Bob"}
        connector_item = {"key": "1"}
        editor.generate_data(other_item, connector_item)
        assert "_editing" not in connector_item

    def test_generate_data_editor_closed(self):
        grid = Grid()
        editor = grid.get_editor()
        connector_item = {"key": "0"}
        editor.generate_data({"name": "A"}, connector_item)
        assert "_editing" not in connector_item


class TestEditorListeners:
    """Test editor event listeners."""

    def _make_editor(self):
        grid = Grid()
        editor = grid.get_editor()
        binder = Binder()
        field = TextField()
        binder.for_field(field).bind(
            lambda item: item.get("name", ""),
            lambda item, val: item.__setitem__("name", val),
        )
        editor.set_binder(binder)
        return editor

    def test_open_listener(self):
        editor = self._make_editor()
        events = []
        editor.add_open_listener(lambda e: events.append(e))
        item = {"name": "A"}
        editor.edit_item(item)
        assert len(events) == 1
        assert isinstance(events[0], EditorOpenEvent)
        assert events[0].item is item

    def test_close_listener(self):
        editor = self._make_editor()
        events = []
        editor.add_close_listener(lambda e: events.append(e))
        item = {"name": "A"}
        editor.edit_item(item)
        editor.close_editor()
        assert len(events) == 1
        assert isinstance(events[0], EditorCloseEvent)
        assert events[0].item is item

    def test_save_listener(self):
        editor = self._make_editor()
        editor.set_buffered(True)
        events = []
        editor.add_save_listener(lambda e: events.append(e))
        item = {"name": "A"}
        editor.edit_item(item)
        editor.save()
        assert len(events) == 1
        assert isinstance(events[0], EditorSaveEvent)
        assert events[0].item is item

    def test_cancel_listener(self):
        editor = self._make_editor()
        editor.set_buffered(True)
        events = []
        editor.add_cancel_listener(lambda e: events.append(e))
        item = {"name": "A"}
        editor.edit_item(item)
        editor.cancel()
        assert len(events) == 1
        assert isinstance(events[0], EditorCancelEvent)
        assert events[0].item is item

    def test_save_fires_close_too(self):
        editor = self._make_editor()
        editor.set_buffered(True)
        close_events = []
        editor.add_close_listener(lambda e: close_events.append(e))
        item = {"name": "A"}
        editor.edit_item(item)
        editor.save()
        assert len(close_events) == 1

    def test_cancel_fires_close_too(self):
        editor = self._make_editor()
        editor.set_buffered(True)
        close_events = []
        editor.add_close_listener(lambda e: close_events.append(e))
        item = {"name": "A"}
        editor.edit_item(item)
        editor.cancel()
        assert len(close_events) == 1

    def test_listener_removal(self):
        editor = self._make_editor()
        events = []
        remove = editor.add_open_listener(lambda e: events.append(e))
        editor.edit_item({"name": "A"})
        assert len(events) == 1
        editor.close_editor()

        remove()
        editor.edit_item({"name": "B"})
        assert len(events) == 1  # No new event


class TestColumnEditor:
    """Test Column.set_editor_component."""

    def test_set_editor_component_static(self):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        field = TextField()
        col.set_editor_component(field)
        assert col.get_editor_component() is field
        assert col._editor_renderer is not None

    def test_set_editor_component_function(self):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        factory = lambda item: TextField()
        col.set_editor_component(factory)
        assert col.get_editor_component() is None  # No static component
        assert col._editor_renderer is not None

    def test_set_editor_component_none(self):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        col.set_editor_component(TextField())
        col.set_editor_component(None)
        assert col.get_editor_component() is None

    def test_set_editor_requires_grid(self):
        col = Column("col0", "name", "Name")
        with pytest.raises(AssertionError, match="Column must be added"):
            col.set_editor_component(TextField())

    def test_set_editor_creates_editor_lazily(self):
        grid = Grid()
        assert grid._editor is None
        col = grid.add_column("name", header="Name")
        col.set_editor_component(TextField())
        assert grid._editor is not None  # Created by get_editor()

    def test_chaining(self):
        grid = Grid()
        col = grid.add_column("name", header="Name")
        result = col.set_editor_component(TextField())
        assert result is col


class TestEditorRenderer:
    """Test _EditorRenderer."""

    def test_generate_data_when_open(self):
        grid = Grid()
        editor = grid.get_editor()
        renderer = _EditorRenderer(editor, "col0")

        # Simulate an open editor with a component
        item = {"name": "Alice"}
        editor._edited = item
        field = TextField()
        tree = StateTree()
        field._attach(tree)
        renderer._component = field

        connector_item = {"key": "0"}
        renderer.generate_data(item, connector_item)
        assert "_col0_editor" in connector_item
        assert connector_item["_col0_editor"] == field.element.node_id

    def test_generate_data_when_closed(self):
        grid = Grid()
        editor = grid.get_editor()
        renderer = _EditorRenderer(editor, "col0")

        connector_item = {"key": "0"}
        renderer.generate_data({"name": "Alice"}, connector_item)
        assert "_col0_editor" not in connector_item

    def test_generate_data_no_component(self):
        grid = Grid()
        editor = grid.get_editor()
        renderer = _EditorRenderer(editor, "col0")
        editor._edited = {"name": "Alice"}

        connector_item = {"key": "0"}
        renderer.generate_data({"name": "Alice"}, connector_item)
        assert "_col0_editor" not in connector_item

    def test_build_component(self):
        grid = Grid()
        editor = grid.get_editor()
        renderer = _EditorRenderer(editor, "col0")

        field = TextField()
        renderer._component_function = lambda item: field
        editor._edited = {"name": "Alice"}

        tree = StateTree()
        container = tree.create_node()
        container.attach()
        renderer._container_node = container

        renderer.refresh_data({"name": "Alice"})
        assert renderer._component is field

    def test_setup_creates_virtual_container(self):
        tree = StateTree()
        grid = Grid()
        editor = grid.get_editor()
        renderer = _EditorRenderer(editor, "col0")

        col_node = tree.create_node()
        col_node.attach()

        renderer.setup(tree, col_node)
        assert renderer._container_node is not None
        assert renderer._container_node.get(Feature.ELEMENT_DATA, "tag") == "div"
        assert renderer._container_node.get(Feature.ELEMENT_DATA, "payload") == {"type": "inMemory"}


class TestGridEditorIntegration:
    """Integration tests for Grid + Editor + push_data."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def _make_grid(self, tree):
        grid = Grid()
        grid.add_column("name", header="Name")
        grid.add_column("age", header="Age")
        grid.set_items([
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
        ])
        grid._attach(tree)
        return grid

    def test_push_data_with_editor_open(self, tree):
        grid = self._make_grid(tree)
        name_field = TextField()
        binder = Binder()
        binder.for_field(name_field).bind(
            lambda item: item.get("name", ""),
            lambda item, val: item.__setitem__("name", val),
        )
        editor = grid.get_editor()
        editor.set_binder(binder)

        # Start editing first item
        item = grid._items[0]
        editor.edit_item(item)

        # Collect execute commands and verify _editing was pushed
        executes = tree.collect_execute()
        # Find the connector.set() call with item data
        set_calls = [e for e in executes if isinstance(e[-1], str) and "connector.set" in e[-1]]
        assert len(set_calls) > 0
        # The items array should have _editing: True for item 0
        for call in set_calls:
            for arg in call:
                if isinstance(arg, list) and len(arg) > 0 and isinstance(arg[0], dict):
                    items_data = arg
                    if any("_editing" in it for it in items_data):
                        assert items_data[0].get("_editing") is True
                        assert "_editing" not in items_data[1]

    def test_push_data_with_editor_closed(self, tree):
        grid = self._make_grid(tree)
        # No editor open - no _editing flag
        tree.collect_execute()  # Clear attach executes
        grid._push_data()
        executes = tree.collect_execute()
        for call in executes:
            for arg in call:
                if isinstance(arg, list) and len(arg) > 0 and isinstance(arg[0], dict):
                    for it in arg:
                        assert "_editing" not in it

    def test_editor_with_column_editor_components(self, tree):
        grid = Grid()
        name_col = grid.add_column("name", header="Name")
        age_col = grid.add_column("age", header="Age")

        name_field = TextField()
        age_field = IntegerField()
        name_col.set_editor_component(name_field)
        age_col.set_editor_component(age_field)

        binder = Binder()
        binder.for_field(name_field).bind(
            lambda item: item.get("name", ""),
            lambda item, val: item.__setitem__("name", val),
        )
        binder.for_field(age_field).bind(
            lambda item: item.get("age", 0),
            lambda item, val: item.__setitem__("age", val),
        )
        editor = grid.get_editor()
        editor.set_binder(binder)

        grid.set_items([{"name": "Alice", "age": 30}])
        grid._attach(tree)

        # Verify editor renderer was set up (virtual container created)
        assert name_col._editor_renderer._container_node is not None
        assert age_col._editor_renderer._container_node is not None

    def test_buffered_save_writes_to_item(self, tree):
        grid = self._make_grid(tree)
        name_field = TextField()
        binder = Binder()
        binder.for_field(name_field).bind(
            lambda item: item.get("name", ""),
            lambda item, val: item.__setitem__("name", val),
        )
        editor = grid.get_editor()
        editor.set_binder(binder)
        editor.set_buffered(True)

        item = grid._items[0]
        editor.edit_item(item)
        name_field.set_value("Alice Updated")
        editor.save()
        assert item["name"] == "Alice Updated"
        assert not editor.is_open()

    def test_unbuffered_auto_writes(self, tree):
        grid = self._make_grid(tree)
        name_field = TextField()
        binder = Binder()
        binder.for_field(name_field).bind(
            lambda item: item.get("name", ""),
            lambda item, val: item.__setitem__("name", val),
        )
        editor = grid.get_editor()
        editor.set_binder(binder)

        item = grid._items[0]
        editor.edit_item(item)
        # In unbuffered mode, set_bean auto-writes
        name_field.set_value("Alice Auto")
        assert item["name"] == "Alice Auto"
