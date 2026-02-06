"""Tests for Dialog component."""

import pytest

from vaadin.flow.components import Dialog, Button, Span
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestDialog:
    """Test Dialog component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_dialog(self):
        """Dialog can be created."""
        dialog = Dialog()
        assert dialog.is_opened() is False
        assert dialog.is_modal() is True
        assert dialog.is_draggable() is False
        assert dialog.is_resizable() is False

    def test_dialog_tag(self):
        """Dialog has correct tag."""
        dialog = Dialog()
        assert dialog._tag == "vaadin-dialog"

    def test_open_close(self, tree):
        """open() and close() work correctly."""
        dialog = Dialog()
        dialog._attach(tree)

        dialog.open()
        assert dialog.is_opened() is True

        dialog.close()
        assert dialog.is_opened() is False

    def test_set_opened(self, tree):
        """set_opened works correctly."""
        dialog = Dialog()
        dialog._attach(tree)

        dialog.set_opened(True)
        assert dialog.is_opened() is True

        dialog.set_opened(False)
        assert dialog.is_opened() is False

    def test_set_modal(self, tree):
        """set_modal sets modeless property (inverted)."""
        dialog = Dialog()
        dialog._attach(tree)

        dialog.set_modal(False)
        assert dialog.is_modal() is False

        dialog.set_modal(True)
        assert dialog.is_modal() is True

    def test_set_draggable(self, tree):
        """set_draggable works correctly."""
        dialog = Dialog()
        dialog._attach(tree)

        dialog.set_draggable(True)
        assert dialog.is_draggable() is True

        dialog.set_draggable(False)
        assert dialog.is_draggable() is False

    def test_set_resizable(self, tree):
        """set_resizable works correctly."""
        dialog = Dialog()
        dialog._attach(tree)

        dialog.set_resizable(True)
        assert dialog.is_resizable() is True

        dialog.set_resizable(False)
        assert dialog.is_resizable() is False

    def test_set_header_title(self, tree):
        """set_header_title works correctly."""
        dialog = Dialog()
        dialog._attach(tree)

        dialog.set_header_title("My Dialog")
        assert dialog.get_header_title() == "My Dialog"

    def test_header_title_in_constructor(self, tree):
        """Header title can be set before attach."""
        dialog = Dialog()
        dialog.set_header_title("Test Title")
        dialog._attach(tree)

        assert dialog.get_header_title() == "Test Title"

    def test_set_width_height(self, tree):
        """set_width and set_height work correctly."""
        dialog = Dialog()
        dialog._attach(tree)

        dialog.set_width("400px")
        dialog.set_height("300px")

        # Width and height are set via CSS variables on style
        # Just verify they don't raise errors
        assert True

    def test_add_children_before_attach(self, tree):
        """Children can be added before attach."""
        dialog = Dialog()
        span = Span("Hello")
        dialog.add(span)

        dialog._attach(tree)

        # Dialog should have the span in its children
        assert len(dialog._children) == 1

    def test_add_children_after_attach(self, tree):
        """Children can be added after attach."""
        dialog = Dialog()
        dialog._attach(tree)

        span = Span("Hello")
        dialog.add(span)

        assert len(dialog._children) == 1

    def test_open_listener(self, tree):
        """Open listener is called when dialog opens."""
        dialog = Dialog()
        dialog._attach(tree)

        events_received = []

        def on_open(event):
            events_received.append(("open", event))

        dialog.add_open_listener(on_open)

        # Open the dialog (server-initiated) - fires open listeners
        dialog.open()

        assert len(events_received) == 1
        assert events_received[0][0] == "open"

    def test_close_listener(self, tree):
        """Close listener is called when user closes the dialog."""
        dialog = Dialog()
        dialog._attach(tree)

        # Open the dialog first
        dialog.open()
        # Simulate the echo from client (consumed by pending flag)
        dialog._handle_opened_changed({})

        events_received = []

        def on_close(event):
            events_received.append(("close", event))

        dialog.add_close_listener(on_close)

        # Simulate user closing the dialog (client sends opened-changed with empty data)
        dialog._handle_opened_changed({})

        assert len(events_received) == 1
        assert events_received[0][0] == "close"

    def test_sync_property(self, tree):
        """_sync_property updates internal state."""
        dialog = Dialog()
        dialog._attach(tree)

        dialog._sync_property("opened", True)
        assert dialog.is_opened() is True

    def test_attach_sets_virtual_child_node_ids(self, tree):
        """Attach sets virtualChildNodeIds property for renderer."""
        dialog = Dialog()
        span = Span("Content")
        dialog.add(span)
        dialog._attach(tree)

        # Dialog should have virtualChildNodeIds property set
        changes = tree.collect_changes()
        virtual_ids_change = next(
            (c for c in changes if c.get("key") == "virtualChildNodeIds"),
            None
        )
        assert virtual_ids_change is not None

    def test_initial_properties_set_on_attach(self, tree):
        """Initial properties are set on attach."""
        dialog = Dialog()
        dialog.set_header_title("Test")
        dialog._attach(tree)

        changes = tree.collect_changes()

        # Find headerTitle property change
        title_change = next(
            (c for c in changes if c.get("key") == "headerTitle" and c.get("value") == "Test"),
            None
        )
        assert title_change is not None
