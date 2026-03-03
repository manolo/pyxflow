"""Tests for Upload component."""

import pytest

from pyxflow.components.upload import Upload
from pyxflow.core.state_tree import StateTree
from pyxflow.core.state_node import Feature
from pyxflow.server.http_server import _upload_handlers, _sessions


class TestUpload:

    @pytest.fixture
    def tree(self):
        return StateTree()

    @pytest.fixture(autouse=True)
    def cleanup_handlers(self):
        """Clean up upload handlers after each test."""
        yield
        _upload_handlers.clear()

    def test_tag(self):
        upload = Upload()
        assert upload._tag == "vaadin-upload"

    def test_default_properties(self):
        upload = Upload()
        assert upload.get_max_files() == 0
        assert upload.get_max_file_size() == 0
        assert upload.is_auto_upload() is True
        assert upload.is_drop_allowed() is True
        assert upload.get_accepted_file_types() == []

    def test_set_max_files(self, tree):
        upload = Upload()
        upload.set_max_files(3)
        assert upload.get_max_files() == 3

        upload._attach(tree)
        changes = tree.collect_changes()
        prop_changes = [c for c in changes if c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert any(c["key"] == "maxFiles" and c["value"] == 3 for c in prop_changes)

    def test_set_max_file_size(self, tree):
        upload = Upload()
        upload.set_max_file_size(10 * 1024 * 1024)
        assert upload.get_max_file_size() == 10 * 1024 * 1024

        upload._attach(tree)
        changes = tree.collect_changes()
        prop_changes = [c for c in changes if c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert any(c["key"] == "maxFileSize" and c["value"] == 10 * 1024 * 1024 for c in prop_changes)

    def test_set_auto_upload_false(self, tree):
        upload = Upload()
        upload.set_auto_upload(False)
        assert upload.is_auto_upload() is False

        upload._attach(tree)
        changes = tree.collect_changes()
        prop_changes = [c for c in changes if c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert any(c["key"] == "noAuto" and c["value"] is True for c in prop_changes)

    def test_set_drop_allowed_false(self, tree):
        upload = Upload()
        upload.set_drop_allowed(False)
        assert upload.is_drop_allowed() is False

        upload._attach(tree)
        changes = tree.collect_changes()
        prop_changes = [c for c in changes if c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert any(c["key"] == "nodrop" and c["value"] is True for c in prop_changes)

    def test_set_accepted_file_types(self, tree):
        upload = Upload()
        upload.set_accepted_file_types("image/*", ".pdf")
        assert upload.get_accepted_file_types() == ["image/*", ".pdf"]

        upload._attach(tree)
        changes = tree.collect_changes()
        prop_changes = [c for c in changes if c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert any(c["key"] == "accept" and c["value"] == "image/*,.pdf" for c in prop_changes)

    def test_target_attribute_set_on_attach(self, tree):
        # Register a fake session so _find_session_id works
        _sessions["test-session"] = {"tree": tree}
        try:
            upload = Upload()
            upload._attach(tree)

            changes = tree.collect_changes()
            attr_changes = [c for c in changes if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP]
            target_change = [c for c in attr_changes if c.get("key") == "target"]
            assert len(target_change) == 1
            target_value = target_change[0]["value"]
            assert isinstance(target_value, dict)
            assert "uri" in target_value
            assert target_value["uri"].startswith("VAADIN/dynamic/resource/")
            assert target_value["uri"].endswith("/upload")
        finally:
            _sessions.pop("test-session", None)

    def test_event_listeners_registered(self, tree):
        upload = Upload()
        upload._attach(tree)

        changes = tree.collect_changes()
        listener_changes = [c for c in changes if c.get("feat") == Feature.ELEMENT_LISTENER_MAP]
        event_types = [c["key"] for c in listener_changes]
        assert "file-reject" in event_types
        assert "upload-success" in event_types
        assert "upload-error" in event_types

    def test_receiver_callback(self, tree):
        received = []
        upload = Upload()
        upload.set_receiver(lambda f, m, d: received.append((f, m, d)))
        upload._attach(tree)

        # Simulate upload handler call
        upload._handle_upload("test.txt", "text/plain", b"hello")
        assert len(received) == 1
        assert received[0] == ("test.txt", "text/plain", b"hello")

    def test_succeeded_listener(self):
        events = []
        upload = Upload()
        upload.add_succeeded_listener(lambda e: events.append(e))

        upload._on_upload_success({"detail": {"file": {"name": "test.txt"}}})
        assert len(events) == 1

    def test_failed_listener(self):
        events = []
        upload = Upload()
        upload.add_failed_listener(lambda e: events.append(e))

        upload._on_upload_error({"detail": {"file": {"name": "test.txt"}}})
        assert len(events) == 1

    def test_file_rejected_listener(self):
        events = []
        upload = Upload()
        upload.add_file_rejected_listener(lambda e: events.append(e))

        upload._on_file_reject({"detail": {"error": "File too large"}})
        assert len(events) == 1

    def test_upload_handler_registered(self, tree):
        _sessions["test-session"] = {"tree": tree}
        try:
            upload = Upload()
            upload._attach(tree)

            # An upload handler should be registered
            assert upload._resource_id is not None
            assert upload._resource_id in _upload_handlers
        finally:
            _sessions.pop("test-session", None)

    def test_set_max_files_after_attach(self, tree):
        upload = Upload()
        upload._attach(tree)
        tree.collect_changes()

        upload.set_max_files(5)
        changes = tree.collect_changes()
        prop_changes = [c for c in changes if c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert any(c["key"] == "maxFiles" and c["value"] == 5 for c in prop_changes)

    def test_set_max_file_size_after_attach(self, tree):
        upload = Upload()
        upload._attach(tree)
        tree.collect_changes()

        upload.set_max_file_size(1024)
        changes = tree.collect_changes()
        prop_changes = [c for c in changes if c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert any(c["key"] == "maxFileSize" and c["value"] == 1024 for c in prop_changes)

    def test_no_receiver_does_not_crash(self, tree):
        upload = Upload()
        upload._attach(tree)
        # Calling handle_upload without a receiver should not raise
        upload._handle_upload("test.txt", "text/plain", b"data")
