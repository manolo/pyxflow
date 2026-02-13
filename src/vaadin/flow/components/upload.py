"""Upload component."""

import json
from typing import Callable, TYPE_CHECKING

from vaadin.flow.core.component import Component
from vaadin.flow.core.state_node import Feature
from vaadin.flow.components.constants import UploadVariant as UploadVariant
from vaadin.flow.server.uidl_handler import (
    _FILE_REJECT_HASH, _UPLOAD_SUCCESS_HASH,
    _UPLOAD_ERROR_HASH, _FILE_REMOVE_HASH,
)

if TYPE_CHECKING:
    from vaadin.flow.core.state_tree import StateTree


class Upload(Component):
    """A file upload component.

    Upload allows the user to send files to the server via drag-and-drop
    or by clicking the upload button. Files are sent via multipart HTTP POST
    to a dynamic resource URL.
    """

    _v_fqcn = "com.vaadin.flow.component.upload.Upload"
    _tag = "vaadin-upload"

    def __init__(self):
        super().__init__()
        self._max_files = 0  # 0 = unlimited
        self._max_file_size = 0  # 0 = unlimited (bytes)
        self._auto_upload = True
        self._drop_allowed = True
        self._accepted_file_types: list[str] = []
        self._receiver: Callable | None = None  # callback(filename, mime_type, data)
        self._succeeded_listeners: list[Callable] = []
        self._failed_listeners: list[Callable] = []
        self._file_rejected_listeners: list[Callable] = []
        self._file_removed_listeners: list[Callable] = []
        self._resource_id: str | None = None
        self._upload_button: Component | None = None
        self._drop_label: Component | None = None
        self._drop_label_icon: Component | None = None

    def set_receiver(self, callback: Callable):
        """Set the receiver callback.

        Args:
            callback: Function(filename: str, mime_type: str, data: bytes)
        """
        self._receiver = callback

    def set_max_files(self, max_files: int):
        """Set maximum number of files (0 = unlimited)."""
        self._max_files = max_files
        if self._element:
            if max_files > 0:
                self.element.set_property("maxFiles", max_files)
            else:
                self.element.remove_property("maxFiles")

    def get_max_files(self) -> int:
        return self._max_files

    def set_max_file_size(self, max_size: int):
        """Set maximum file size in bytes (0 = unlimited)."""
        self._max_file_size = max_size
        if self._element:
            if max_size > 0:
                self.element.set_property("maxFileSize", max_size)
            else:
                self.element.remove_property("maxFileSize")

    def get_max_file_size(self) -> int:
        return self._max_file_size

    def set_auto_upload(self, auto: bool):
        """Set whether files are uploaded immediately."""
        self._auto_upload = auto
        if self._element:
            self.element.set_property("noAuto", not auto)

    def is_auto_upload(self) -> bool:
        return self._auto_upload

    def set_drop_allowed(self, allowed: bool):
        """Set whether drag-and-drop is allowed."""
        self._drop_allowed = allowed
        if self._element:
            self.element.set_property("nodrop", not allowed)

    def is_drop_allowed(self) -> bool:
        return self._drop_allowed

    def set_accepted_file_types(self, *types: str):
        """Set accepted file types (MIME types or extensions like '.pdf')."""
        self._accepted_file_types = list(types)
        if self._element:
            self.element.set_property("accept", ",".join(types) if types else "")

    def get_accepted_file_types(self) -> list[str]:
        return list(self._accepted_file_types)

    def add_succeeded_listener(self, listener: Callable):
        """Add a listener for successful uploads."""
        self._succeeded_listeners.append(listener)

    def add_failed_listener(self, listener: Callable):
        """Add a listener for failed uploads."""
        self._failed_listeners.append(listener)

    def add_file_rejected_listener(self, listener: Callable):
        """Add a listener for rejected files (client-side validation)."""
        self._file_rejected_listeners.append(listener)

    def add_file_removed_listener(self, listener: Callable):
        """Add a listener for when a file is removed from the upload list."""
        self._file_removed_listeners.append(listener)

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)

        # Set properties
        if self._max_files > 0:
            self.element.set_property("maxFiles", self._max_files)
        if self._max_file_size > 0:
            self.element.set_property("maxFileSize", self._max_file_size)
        if not self._auto_upload:
            self.element.set_property("noAuto", True)
        if not self._drop_allowed:
            self.element.set_property("nodrop", True)
        if self._accepted_file_types:
            self.element.set_property("accept", ",".join(self._accepted_file_types))

        # Slotted components
        if self._upload_button:
            self._upload_button._ui = self._ui
            self._upload_button._parent = self
            self._upload_button._attach(tree)
            self._upload_button.element.set_attribute("slot", "add-button")
            self.element.add_child(self._upload_button.element)
        if self._drop_label:
            self._drop_label._ui = self._ui
            self._drop_label._parent = self
            self._drop_label._attach(tree)
            self._drop_label.element.set_attribute("slot", "drop-label")
            self.element.add_child(self._drop_label.element)
        if self._drop_label_icon:
            self._drop_label_icon._ui = self._ui
            self._drop_label_icon._parent = self
            self._drop_label_icon._attach(tree)
            self._drop_label_icon.element.set_attribute("slot", "drop-label-icon")
            self.element.add_child(self._drop_label_icon.element)

        # Register upload handler in HTTP server and set target attribute
        from vaadin.flow.server.http_server import register_upload_handler, _sessions
        # Find session_id for this tree
        session_id = self._find_session_id()
        self._resource_id = register_upload_handler(session_id, self._handle_upload)

        # Set target as JSON object with uri (matches Java's ElementAttributeMap serialization)
        target_uri = f"VAADIN/dynamic/resource/0/{self._resource_id}/upload"
        self.element.node.put(
            Feature.ELEMENT_ATTRIBUTE_MAP, "target",
            {"uri": target_uri}
        )

        # Register event listeners (always registered, matching Java behavior)
        self.element.add_event_listener(
            "file-reject", self._on_file_reject, hash_key=_FILE_REJECT_HASH
        )
        self.element.add_event_listener(
            "upload-success", self._on_upload_success, hash_key=_UPLOAD_SUCCESS_HASH
        )
        self.element.add_event_listener(
            "upload-error", self._on_upload_error, hash_key=_UPLOAD_ERROR_HASH
        )
        self.element.add_event_listener(
            "file-remove", self._on_file_remove, hash_key=_FILE_REMOVE_HASH
        )

    def _find_session_id(self) -> str:
        """Find the session ID that owns this tree."""
        from vaadin.flow.server.http_server import _sessions
        for sid, session in _sessions.items():
            if session.get("tree") is self.element._tree:
                return sid
        return "unknown"

    def _handle_upload(self, filename: str, mime_type: str, data: bytes):
        """Handle uploaded file data from HTTP server."""
        if self._receiver:
            self._receiver(filename, mime_type, data)

    def _on_file_reject(self, event_data: dict):
        """Handle file-reject event from client."""
        for listener in self._file_rejected_listeners:
            listener(event_data)

    def _on_upload_success(self, event_data: dict):
        """Handle upload-success event from client."""
        for listener in self._succeeded_listeners:
            listener(event_data)

    def _on_upload_error(self, event_data: dict):
        """Handle upload-error event from client."""
        for listener in self._failed_listeners:
            listener(event_data)

    def _on_file_remove(self, event_data: dict):
        """Handle file-remove event from client."""
        for listener in self._file_removed_listeners:
            listener(event_data)

    def set_upload_button(self, button: Component | None):
        """Set a custom upload button component."""
        self._upload_button = button
        if self._element and button:
            button._ui = self._ui
            button._parent = self
            button._attach(self._element._tree)
            button.element.set_attribute("slot", "add-button")
            self.element.add_child(button.element)

    def get_upload_button(self) -> Component | None:
        return self._upload_button

    def set_drop_label(self, label: Component | None):
        """Set a custom drop label component."""
        self._drop_label = label
        if self._element and label:
            label._ui = self._ui
            label._parent = self
            label._attach(self._element._tree)
            label.element.set_attribute("slot", "drop-label")
            self.element.add_child(label.element)

    def get_drop_label(self) -> Component | None:
        return self._drop_label

    def set_drop_label_icon(self, icon: Component | None):
        """Set a custom drop label icon component."""
        self._drop_label_icon = icon
        if self._element and icon:
            icon._ui = self._ui
            icon._parent = self
            icon._attach(self._element._tree)
            icon.element.set_attribute("slot", "drop-label-icon")
            self.element.add_child(icon.element)

    def get_drop_label_icon(self) -> Component | None:
        return self._drop_label_icon

    def clear_file_list(self):
        """Clear the file list on the client side."""
        if self._element:
            self.element._tree.queue_execute([
                {"@v-node": self.element.node.id},
                "return $0.files = []",
            ])

    def set_i18n(self, i18n: dict):
        """Set the i18n localization object.

        The dict keys should match the web component's i18n structure.
        """
        self._i18n = i18n
        self.execute_js(f"return (function(){{$0.i18n = Object.assign({{}}, $0.i18n, {json.dumps(i18n)})}}).call(null)")

    def get_i18n(self) -> dict | None:
        return getattr(self, "_i18n", None)

    def add_theme_variants(self, *variants: UploadVariant):
        """Add theme variants to the upload."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: UploadVariant):
        """Remove theme variants from the upload."""
        self.remove_theme_name(*variants)
