"""Tests for Notification component."""

import pytest

from vaadin.flow.components import (
    Notification,
    NotificationPosition,
    NotificationVariant,
    Span,
)
from vaadin.flow.core.state_tree import StateTree


class TestNotification:
    """Test Notification component."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_create_notification(self):
        """Notification can be created."""
        notification = Notification()
        assert notification.is_opened() is False
        assert notification.get_text() == ""
        assert notification.get_duration() == 5000

    def test_create_notification_with_text(self):
        """Notification can be created with text."""
        notification = Notification("Hello!")
        assert notification.get_text() == "Hello!"

    def test_create_notification_with_duration(self):
        """Notification can be created with custom duration."""
        notification = Notification("Test", duration=3000)
        assert notification.get_duration() == 3000

    def test_notification_tag(self):
        """Notification has correct tag."""
        notification = Notification()
        assert notification._tag == "vaadin-notification"

    def test_open_close(self, tree):
        """open() and close() work correctly."""
        notification = Notification("Test")
        notification._attach(tree)

        notification.open()
        assert notification.is_opened() is True

        notification.close()
        assert notification.is_opened() is False

    def test_set_opened(self, tree):
        """set_opened works correctly."""
        notification = Notification("Test")
        notification._attach(tree)

        notification.set_opened(True)
        assert notification.is_opened() is True

        notification.set_opened(False)
        assert notification.is_opened() is False

    def test_set_text(self):
        """set_text works correctly."""
        notification = Notification()
        notification.set_text("New text")
        assert notification.get_text() == "New text"

    def test_set_duration(self, tree):
        """set_duration works correctly."""
        notification = Notification("Test")
        notification._attach(tree)

        notification.set_duration(10000)
        assert notification.get_duration() == 10000

    def test_set_position(self, tree):
        """set_position works correctly."""
        notification = Notification("Test")
        notification._attach(tree)

        notification.set_position(NotificationPosition.TOP_CENTER)
        assert notification.get_position() == NotificationPosition.TOP_CENTER

    def test_default_position(self):
        """Default position is BOTTOM_START."""
        notification = Notification()
        assert notification.get_position() == NotificationPosition.BOTTOM_START

    def test_add_theme_variants(self, tree):
        """add_theme_variants works correctly."""
        notification = Notification("Test")
        notification._attach(tree)

        notification.add_theme_variants(NotificationVariant.LUMO_SUCCESS)
        assert "success" in notification._theme_variants

    def test_remove_theme_variants(self, tree):
        """remove_theme_variants works correctly."""
        notification = Notification("Test")
        notification._attach(tree)

        notification.add_theme_variants(NotificationVariant.LUMO_ERROR)
        notification.remove_theme_variants(NotificationVariant.LUMO_ERROR)
        assert "error" not in notification._theme_variants

    def test_add_children(self, tree):
        """Custom children can be added."""
        notification = Notification()
        notification._attach(tree)

        span = Span("Custom content")
        notification.add(span)

        assert len(notification._children) == 1

    def test_open_listener(self, tree):
        """Open listener is called when notification opens."""
        notification = Notification("Test")
        notification._attach(tree)

        events_received = []

        def on_open(event):
            events_received.append(("open", event))

        notification.add_open_listener(on_open)

        # Simulate opened-changed event
        notification._handle_opened_changed({"opened": True})

        assert len(events_received) == 1

    def test_close_listener(self, tree):
        """Close listener is called when notification closes."""
        notification = Notification("Test")
        notification._attach(tree)
        notification._opened = True  # Start opened

        events_received = []

        def on_close(event):
            events_received.append(("close", event))

        notification.add_close_listener(on_close)

        # Simulate opened-changed event
        notification._handle_opened_changed({"opened": False})

        assert len(events_received) == 1

    def test_sync_property(self, tree):
        """_sync_property updates internal state."""
        notification = Notification("Test")
        notification._attach(tree)

        notification._sync_property("opened", True)
        assert notification.is_opened() is True

    def test_attach_creates_card_node(self, tree):
        """Attach creates card node for content."""
        notification = Notification("Test")
        notification._attach(tree)

        assert hasattr(notification, "_card_node")
        assert notification._card_node is not None

    def test_show_static_method(self):
        """Notification.show creates and opens notification."""
        notification = Notification.show("Hello", 3000, NotificationPosition.TOP_END)

        assert notification.get_text() == "Hello"
        assert notification.get_duration() == 3000
        assert notification.get_position() == NotificationPosition.TOP_END
        assert notification.is_opened() is True  # _opened is True but not actually opened until attached


class TestNotificationPosition:
    """Test NotificationPosition enum."""

    def test_all_positions_have_values(self):
        """All positions have correct string values."""
        assert NotificationPosition.TOP_STRETCH.value == "top-stretch"
        assert NotificationPosition.TOP_START.value == "top-start"
        assert NotificationPosition.TOP_CENTER.value == "top-center"
        assert NotificationPosition.TOP_END.value == "top-end"
        assert NotificationPosition.MIDDLE.value == "middle"
        assert NotificationPosition.BOTTOM_START.value == "bottom-start"
        assert NotificationPosition.BOTTOM_CENTER.value == "bottom-center"
        assert NotificationPosition.BOTTOM_END.value == "bottom-end"
        assert NotificationPosition.BOTTOM_STRETCH.value == "bottom-stretch"


class TestNotificationVariant:
    """Test NotificationVariant enum."""

    def test_all_variants_have_values(self):
        """All variants have correct string values."""
        assert NotificationVariant.LUMO_PRIMARY.value == "primary"
        assert NotificationVariant.LUMO_CONTRAST.value == "contrast"
        assert NotificationVariant.LUMO_SUCCESS.value == "success"
        assert NotificationVariant.LUMO_ERROR.value == "error"
        assert NotificationVariant.LUMO_WARNING.value == "warning"
