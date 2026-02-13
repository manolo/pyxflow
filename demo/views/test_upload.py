"""Test View 17: Upload — /test/upload"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Span, Upload, VerticalLayout,
)
from vaadin.flow.menu import Menu
from demo.views.test_main_layout import TestMainLayout


@Route("test/upload", page_title="Test: Upload", layout=TestMainLayout)
@Menu(title="Upload", order=22)
class TestUploadView(VerticalLayout):
    def __init__(self):
        # --- Upload with receiver ---
        upload_result = Span("")
        upload_result.set_id("upload-result")
        upload1 = Upload()
        upload1.set_id("upload1")
        upload1.set_max_files(2)
        upload1.set_max_file_size(1024 * 1024)  # 1MB
        upload1.set_accepted_file_types(".txt", ".csv")

        def _on_upload(filename, mime_type, data):
            upload_result.set_text(filename)

        upload1.set_receiver(_on_upload)
        upload1.add_succeeded_listener(
            lambda e: upload_result.set_text(e.get("fileName", ""))
        )

        # --- Upload auto_upload disabled ---
        upload_manual = Upload()
        upload_manual.set_id("upload-manual")
        upload_manual.set_auto_upload(False)

        # --- Upload file_rejected_listener ---
        upload_rej_val = Span("")
        upload_rej_val.set_id("upload-rej")
        upload_rej = Upload()
        upload_rej.set_id("upload-rej-field")
        upload_rej.set_max_file_size(100)  # 100 bytes
        upload_rej.add_file_rejected_listener(
            lambda e: upload_rej_val.set_text("rejected")
        )

        self.add(
            upload1, upload_result,
            upload_manual,
            upload_rej, upload_rej_val,
        )
