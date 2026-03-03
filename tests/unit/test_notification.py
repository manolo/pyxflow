"""Tests for Notification component."""

import pytest

from pyxflow.components import Notification, NotificationVariant
from pyxflow.components.notification import _set_current_tree, _get_current_tree
from pyxflow.components.span import Span
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature


class TestNotification:
    """Test Notification component."""

    @pytest.fixture
    def tree(self):
        """Create a tree with body node (node 1) pre-created."""
        t = StateTree()
        # Create body node (node 1) as UidlHandler does
        body = t.create_node()
        assert body.id == 1
        return t

    def test_create_notification(self):
        """Notification can be created with defaults."""
        n = Notification()
        assert n.text == ""
        assert n.duration == 0
        assert n.position == Notification.Position.BOTTOM_START
        assert n.assertive is False
        assert n.is_opened() is False

    def test_create_with_text(self):
        """Notification can be created with text."""
        n = Notification("Hello")
        assert n.text == "Hello"

    def test_create_with_all_params(self):
        """Notification can be created with all parameters."""
        n = Notification("Msg", 3000, Notification.Position.TOP_CENTER, True)
        assert n.text == "Msg"
        assert n.duration == 3000
        assert n.position == Notification.Position.TOP_CENTER
        assert n.assertive is True

    def test_tag(self):
        """Notification has correct tag."""
        assert Notification._tag == "vaadin-notification"

    def test_set_text(self, tree):
        """Text property can be set."""
        n = Notification()
        n._attach(tree)
        n.text = "Updated"
        assert n.text == "Updated"

    def test_set_duration(self, tree):
        """Duration property can be set."""
        n = Notification()
        n._attach(tree)
        n.duration = 5000
        assert n.duration == 5000

    def test_set_position(self, tree):
        """Position property can be set."""
        n = Notification()
        n._attach(tree)
        n.position = Notification.Position.TOP_END
        assert n.position == Notification.Position.TOP_END

    def test_set_assertive(self, tree):
        """Assertive property can be set."""
        n = Notification()
        n._attach(tree)
        n.assertive = True
        assert n.assertive is True

    def test_open_close(self, tree):
        """open() and close() work correctly."""
        n = Notification("Test")
        n._attach(tree)

        n.open()
        assert n.is_opened() is True

        n.close()
        assert n.is_opened() is False

    def test_set_opened(self, tree):
        """set_opened works correctly."""
        n = Notification("Test")
        n._attach(tree)

        n.set_opened(True)
        assert n.is_opened() is True

        n.set_opened(False)
        assert n.is_opened() is False

    def test_uidl_changes_on_attach(self, tree):
        """Attach produces correct UIDL changes."""
        n = Notification("Hello", 5000)
        n._opened = True
        n._attach(tree)

        changes = tree.collect_changes()

        # Should have attach change
        attach_changes = [c for c in changes if c.get("type") == "attach"]
        assert len(attach_changes) >= 1

        # Should have tag
        tag_change = next(
            (c for c in changes if c.get("key") == "tag" and c.get("value") == "vaadin-notification"),
            None
        )
        assert tag_change is not None

        # Duration should be float
        duration_change = next(
            (c for c in changes if c.get("key") == "duration"),
            None
        )
        assert duration_change is not None
        assert duration_change["value"] == 5000.0
        assert isinstance(duration_change["value"], float)

        # Position
        position_change = next(
            (c for c in changes if c.get("key") == "position"),
            None
        )
        assert position_change is not None
        assert position_change["value"] == "bottom-start"

        # Text
        text_change = next(
            (c for c in changes if c.get("key") == "text" and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP),
            None
        )
        assert text_change is not None
        assert text_change["value"] == "Hello"

        # virtualChildNodeIds
        vcni_change = next(
            (c for c in changes if c.get("key") == "virtualChildNodeIds"),
            None
        )
        assert vcni_change is not None
        assert vcni_change["value"] == []

        # Clear feat 2
        clear_change = next(
            (c for c in changes if c.get("type") == "clear" and c.get("feat") == Feature.ELEMENT_CHILDREN_LIST),
            None
        )
        assert clear_change is not None

    def test_body_attachment_via_open(self, tree):
        """Notification.open() auto-attaches to body (node 1) via tree context."""
        from pyxflow.components.notification import _set_current_tree
        _set_current_tree(tree)
        try:
            n = Notification("Test")
            n.open()

            changes = tree.collect_changes()

            # Find splice to node 1
            body_splice = next(
                (c for c in changes if c.get("node") == 1 and c.get("type") == "splice" and c.get("feat") == Feature.ELEMENT_CHILDREN_LIST),
                None
            )
            assert body_splice is not None
            assert n.element.node_id in body_splice["addNodes"]
        finally:
            _set_current_tree(None)

    def test_event_hashes(self, tree):
        """Event listeners use correct notification-specific hashes."""
        n = Notification("Test")
        n._attach(tree)

        changes = tree.collect_changes()

        # closed event should use notification hash
        closed_change = next(
            (c for c in changes if c.get("key") == "closed" and c.get("feat") == Feature.ELEMENT_LISTENER_MAP),
            None
        )
        assert closed_change is not None
        assert closed_change["value"] == "vIpODLLAUDo="

        # opened-changed event should use notification hash (not dialog hash)
        opened_change = next(
            (c for c in changes if c.get("key") == "opened-changed" and c.get("feat") == Feature.ELEMENT_LISTENER_MAP),
            None
        )
        assert opened_change is not None
        assert opened_change["value"] == "uqvzCy8jAQc="

    def test_opened_changed_listener(self, tree):
        """Open/close listeners are called correctly."""
        n = Notification("Test")
        n._attach(tree)

        events_received = []

        def on_open(event):
            events_received.append(("open", event))

        def on_close(event):
            events_received.append(("close", event))

        n.add_open_listener(on_open)
        n.add_close_listener(on_close)

        # Open the notification (server-initiated) - fires open listener
        n.open()
        assert len(events_received) == 1
        assert events_received[0][0] == "open"

        # Simulate echo from client (consumed by pending flag)
        n._handle_opened_changed({})

        # Simulate user/auto-close: client sends opened-changed then closed
        n._handle_opened_changed({})
        n._handle_closed({})
        assert len(events_received) == 2
        assert events_received[1][0] == "close"

    def test_closed_listener(self, tree):
        """Closed event listener is called correctly."""
        n = Notification("Test")
        n._attach(tree)
        n._opened = True

        events_received = []

        def on_close(event):
            events_received.append(event)

        n.add_close_listener(on_close)

        n._handle_closed({"some": "data"})
        assert len(events_received) == 1
        assert n.is_opened() is False

    def test_sync_property(self, tree):
        """_sync_property updates internal state."""
        n = Notification("Test")
        n._attach(tree)

        n._sync_property("opened", True)
        assert n.is_opened() is True

        n._sync_property("opened", False)
        assert n.is_opened() is False

    def test_theme_variants_add(self, tree):
        """Theme variants can be added."""
        n = Notification("Test")
        n._attach(tree)

        n.add_theme_variants(NotificationVariant.LUMO_SUCCESS)

        changes = tree.collect_changes()
        theme_change = next(
            (c for c in changes if c.get("key") == "theme" and c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP),
            None
        )
        assert theme_change is not None
        assert "success" in theme_change["value"]

    def test_theme_variants_remove(self, tree):
        """Theme variants can be removed."""
        n = Notification("Test")
        n._attach(tree)

        n.add_theme_variants(NotificationVariant.LUMO_SUCCESS, NotificationVariant.LUMO_ERROR)
        tree.collect_changes()  # clear

        n.remove_theme_variants(NotificationVariant.LUMO_SUCCESS)
        changes = tree.collect_changes()

        theme_change = next(
            (c for c in changes if c.get("key") == "theme" and c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP),
            None
        )
        assert theme_change is not None
        assert "error" in theme_change["value"]
        assert "success" not in theme_change["value"]

    def test_theme_variants_remove_all(self, tree):
        """Removing all theme variants removes the attribute."""
        n = Notification("Test")
        n._attach(tree)

        n.add_theme_variants(NotificationVariant.LUMO_SUCCESS)
        tree.collect_changes()  # clear

        n.remove_theme_variants(NotificationVariant.LUMO_SUCCESS)
        changes = tree.collect_changes()

        # Should have a remove for the theme attribute
        remove_change = next(
            (c for c in changes if c.get("key") == "theme" and c.get("type") == "remove"),
            None
        )
        assert remove_change is not None

    def test_theme_variants_before_attach(self, tree):
        """Theme variants set before attach are applied."""
        n = Notification("Test")
        n.add_theme_variants(NotificationVariant.LUMO_ERROR)
        n._attach(tree)

        changes = tree.collect_changes()
        theme_change = next(
            (c for c in changes if c.get("key") == "theme" and c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP),
            None
        )
        assert theme_change is not None
        assert "error" in theme_change["value"]

    def test_static_show(self, tree):
        """Notification.show() creates and opens a notification."""
        _set_current_tree(tree)
        try:
            n = Notification.show("Hello World")
            assert n.is_opened() is True
            assert n.text == "Hello World"
            assert n.duration == 5000
            assert n.position == Notification.Position.BOTTOM_START
        finally:
            _set_current_tree(None)

    def test_static_show_with_params(self, tree):
        """Notification.show() accepts all parameters."""
        _set_current_tree(tree)
        try:
            n = Notification.show("Msg", 3000, Notification.Position.TOP_CENTER, True)
            assert n.is_opened() is True
            assert n.text == "Msg"
            assert n.duration == 3000
            assert n.position == Notification.Position.TOP_CENTER
            assert n.assertive is True
        finally:
            _set_current_tree(None)

    def test_static_show_attaches_to_body(self, tree):
        """Notification.show() attaches to body node."""
        _set_current_tree(tree)
        try:
            n = Notification.show("Test")
            changes = tree.collect_changes()

            # Should be spliced to node 1 (body)
            body_splice = next(
                (c for c in changes if c.get("node") == 1 and c.get("type") == "splice"),
                None
            )
            assert body_splice is not None
        finally:
            _set_current_tree(None)

    def test_add_components(self, tree):
        """Components can be added as notification content."""
        n = Notification()
        n._attach(tree)
        tree.collect_changes()  # clear

        span = Span("Custom content")
        n.add(span)

        assert len(n._children) == 1

    def test_position_enum_values(self):
        """All Position enum values are correct."""
        assert Notification.Position.TOP_STRETCH.value == "top-stretch"
        assert Notification.Position.TOP_START.value == "top-start"
        assert Notification.Position.TOP_CENTER.value == "top-center"
        assert Notification.Position.TOP_END.value == "top-end"
        assert Notification.Position.MIDDLE.value == "middle"
        assert Notification.Position.BOTTOM_START.value == "bottom-start"
        assert Notification.Position.BOTTOM_CENTER.value == "bottom-center"
        assert Notification.Position.BOTTOM_END.value == "bottom-end"
        assert Notification.Position.BOTTOM_STRETCH.value == "bottom-stretch"

    def test_variant_enum_values(self):
        """All NotificationVariant enum values are correct."""
        assert NotificationVariant.LUMO_PRIMARY.value == "primary"
        assert NotificationVariant.LUMO_CONTRAST.value == "contrast"
        assert NotificationVariant.LUMO_SUCCESS.value == "success"
        assert NotificationVariant.LUMO_ERROR.value == "error"
        assert NotificationVariant.LUMO_WARNING.value == "warning"

    def test_open_auto_attaches(self, tree):
        """open() auto-attaches when tree context is available."""
        _set_current_tree(tree)
        try:
            n = Notification("Auto")
            n.open()
            assert n.is_opened() is True
            assert n._element is not None
        finally:
            _set_current_tree(None)

    def test_current_tree_context(self):
        """Tree context management works correctly."""
        assert _get_current_tree() is None

        tree = StateTree()
        _set_current_tree(tree)
        assert _get_current_tree() is tree

        _set_current_tree(None)
        assert _get_current_tree() is None
