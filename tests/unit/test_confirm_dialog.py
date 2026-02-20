"""Tests for ConfirmDialog component."""

import pytest

from vaadin.flow.components.confirm_dialog import ConfirmDialog
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestConfirmDialog:
    """Test ConfirmDialog component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_default(self):
        """ConfirmDialog can be created with defaults."""
        cd = ConfirmDialog()
        assert cd.get_header() == ""
        assert cd.get_text() == ""
        assert cd.get_confirm_text() == "Confirm"
        assert cd.is_opened() is False
        assert cd.is_cancelable() is False
        assert cd.is_rejectable() is False

    def test_create_with_args(self):
        """ConfirmDialog accepts constructor arguments."""
        cd = ConfirmDialog(header="Title", text="Message", confirm_text="OK")
        assert cd.get_header() == "Title"
        assert cd.get_text() == "Message"
        assert cd.get_confirm_text() == "OK"

    def test_tag(self):
        """ConfirmDialog has correct tag."""
        cd = ConfirmDialog()
        assert cd._tag == "vaadin-confirm-dialog"

    def test_open_close(self, tree):
        """open() and close() work correctly."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.open()
        assert cd.is_opened() is True

        cd.close()
        assert cd.is_opened() is False

    def test_set_header(self, tree):
        """set_header sets the header property."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.set_header("Delete?")
        assert cd.get_header() == "Delete?"

    def test_set_text(self, tree):
        """set_text sets the message property."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.set_text("Are you sure?")
        assert cd.get_text() == "Are you sure?"

    def test_set_confirm_text(self, tree):
        """set_confirm_text changes the confirm button text."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.set_confirm_text("Yes")
        assert cd.get_confirm_text() == "Yes"

    def test_set_confirm_button_theme(self, tree):
        """set_confirm_button_theme sets the confirmTheme property."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.set_confirm_button_theme("error primary")
        node = cd.element.node
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "confirmTheme") == "error primary"

    def test_set_cancelable(self, tree):
        """set_cancelable controls cancel button visibility."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.set_cancelable(True)
        assert cd.is_cancelable() is True
        node = cd.element.node
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "cancelButtonVisible") is True

        cd.set_cancelable(False)
        assert cd.is_cancelable() is False

    def test_set_cancel_text(self, tree):
        """set_cancel_text changes the cancel button text."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.set_cancel_text("Abort")
        assert cd.get_cancel_text() == "Abort"

    def test_set_cancel_button_theme(self, tree):
        """set_cancel_button_theme sets the cancelTheme property."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.set_cancel_button_theme("tertiary")
        node = cd.element.node
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "cancelTheme") == "tertiary"

    def test_set_rejectable(self, tree):
        """set_rejectable controls reject button visibility."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.set_rejectable(True)
        assert cd.is_rejectable() is True
        node = cd.element.node
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "rejectButtonVisible") is True

    def test_set_reject_text(self, tree):
        """set_reject_text changes the reject button text."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.set_reject_text("No")
        assert cd.get_reject_text() == "No"

    def test_set_reject_button_theme(self, tree):
        """set_reject_button_theme sets the rejectTheme property."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.set_reject_button_theme("error")
        node = cd.element.node
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "rejectTheme") == "error"

    def test_confirm_listener(self, tree):
        """Confirm event fires registered listeners."""
        cd = ConfirmDialog()
        cd._attach(tree)

        result = []
        cd.add_confirm_listener(lambda e: result.append("confirmed"))

        cd.element.fire_event("confirm", {})
        assert result == ["confirmed"]
        assert cd.is_opened() is False

    def test_cancel_listener(self, tree):
        """Cancel event fires registered listeners."""
        cd = ConfirmDialog()
        cd._attach(tree)

        result = []
        cd.add_cancel_listener(lambda e: result.append("cancelled"))

        cd.element.fire_event("cancel", {})
        assert result == ["cancelled"]
        assert cd.is_opened() is False

    def test_reject_listener(self, tree):
        """Reject event fires registered listeners."""
        cd = ConfirmDialog()
        cd._attach(tree)

        result = []
        cd.add_reject_listener(lambda e: result.append("rejected"))

        cd.element.fire_event("reject", {})
        assert result == ["rejected"]
        assert cd.is_opened() is False

    def test_multiple_listeners(self, tree):
        """Multiple listeners on same event all fire."""
        cd = ConfirmDialog()
        cd._attach(tree)

        results = []
        cd.add_confirm_listener(lambda e: results.append("a"))
        cd.add_confirm_listener(lambda e: results.append("b"))

        cd.element.fire_event("confirm", {})
        assert results == ["a", "b"]

    def test_attach_sets_initial_properties(self, tree):
        """Attaching sets all configured properties."""
        cd = ConfirmDialog(header="Delete", text="Sure?", confirm_text="Yes")
        cd.set_cancelable(True)
        cd.set_confirm_button_theme("error primary")
        cd._attach(tree)

        node = cd.element.node
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "header") == "Delete"
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "message") == "Sure?"
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "confirmText") == "Yes"
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "confirmTheme") == "error primary"
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "cancelButtonVisible") is True

    def test_attach_registers_event_listeners(self, tree):
        """Attaching registers confirm/cancel/reject event listeners."""
        cd = ConfirmDialog()
        cd._attach(tree)

        # Event listeners should be registered
        node = cd.element.node
        assert node.get(Feature.ELEMENT_LISTENER_MAP, "confirm") is not None
        assert node.get(Feature.ELEMENT_LISTENER_MAP, "cancel") is not None
        assert node.get(Feature.ELEMENT_LISTENER_MAP, "reject") is not None

    def test_open_sets_opened_property(self, tree):
        """open() sets the opened property on the element."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.open()
        node = cd.element.node
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "opened") is True

    def test_close_clears_opened_property(self, tree):
        """close() clears the opened property."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd.open()
        cd.close()
        node = cd.element.node
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "opened") is False

    def test_sync_property_opened(self, tree):
        """_sync_property handles opened property from client."""
        cd = ConfirmDialog()
        cd._attach(tree)

        cd._sync_property("opened", True)
        assert cd.is_opened() is True

        cd._sync_property("opened", False)
        assert cd.is_opened() is False

    def test_properties_before_attach(self):
        """Properties set before attach are applied on attach."""
        cd = ConfirmDialog()
        cd.set_header("Title")
        cd.set_text("Body")
        cd.set_confirm_text("OK")
        cd.set_cancelable(True)
        cd.set_rejectable(True)

        tree = StateTree()
        cd._attach(tree)

        node = cd.element.node
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "header") == "Title"
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "message") == "Body"
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "confirmText") == "OK"
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "cancelButtonVisible") is True
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "rejectButtonVisible") is True

    def test_open_before_attach_flushed(self):
        """open() called before attach must flush opened=True during _attach.

        Pitfall 31: before_enter() runs before _attach(), so open() called
        there sets _opened=True but _element is None. _attach() must flush it.
        """
        cd = ConfirmDialog(header="Delete", text="Sure?")
        cd.open()  # before attach -- _element is None
        assert cd.is_opened() is True

        tree = StateTree()
        cd._attach(tree)

        node = cd.element.node
        assert node.get(Feature.ELEMENT_PROPERTY_MAP, "opened") is True
