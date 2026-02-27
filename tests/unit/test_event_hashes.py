"""Tests for dynamic event hash computation."""

import pytest

from pyflow.server.uidl_handler import (
    compute_event_hash,
    _CLICK_HASH, _CLICK_CONFIG,
    _CHANGE_HASH, _CHANGE_CONFIG,
    _OPENED_CHANGED_HASH, _OPENED_CHANGED_CONFIG,
    _CHECKED_CHANGED_HASH, _CHECKED_CHANGED_CONFIG,
    _KEYDOWN_HASH, _KEYDOWN_CONFIG,
    _CLOSED_HASH, _CLOSED_CONFIG,
    _SELECTED_CHANGED_HASH, _SELECTED_CHANGED_CONFIG,
    _SELECTED_VALUES_CHANGED_HASH, _SELECTED_VALUES_CHANGED_CONFIG,
    _VALUE_CHANGED_HASH, _VALUE_CHANGED_CONFIG,
    _SELECTED_ITEMS_CHANGED_HASH, _SELECTED_ITEMS_CHANGED_CONFIG,
    _SPLITTER_DRAGEND_HASH, _SPLITTER_DRAGEND_CONFIG,
    _UI_NAVIGATE_HASH, _UI_NAVIGATE_CONFIG,
    _UI_LEAVE_NAVIGATION_HASH, _UI_LEAVE_NAVIGATION_CONFIG,
    _UI_REFRESH_HASH, _UI_REFRESH_CONFIG,
    _FILE_REJECT_HASH, _FILE_REJECT_CONFIG,
    _UPLOAD_SUCCESS_HASH, _UPLOAD_SUCCESS_CONFIG,
    _FILE_REMOVE_HASH, _FILE_REMOVE_CONFIG,
    _SUBMIT_HASH, _SUBMIT_CONFIG,
    _LOGIN_HASH, _LOGIN_CONFIG,
)


class TestComputeEventHash:
    """Tests for compute_event_hash function."""

    def test_empty_config_produces_known_hash(self):
        """Empty config {} produces the known closed-event hash."""
        assert compute_event_hash({}) == _CLOSED_HASH

    def test_same_config_produces_same_hash(self):
        """Identical configs always produce the same hash."""
        config = {"}value": False}
        assert compute_event_hash(config) == compute_event_hash(config)

    def test_different_configs_produce_different_hashes(self):
        """Different configs produce different hashes."""
        hashes = {
            compute_event_hash(_CLICK_CONFIG),
            compute_event_hash(_CHANGE_CONFIG),
            compute_event_hash(_OPENED_CHANGED_CONFIG),
            compute_event_hash(_CHECKED_CHANGED_CONFIG),
            compute_event_hash(_KEYDOWN_CONFIG),
            compute_event_hash(_CLOSED_CONFIG),
            compute_event_hash(_SELECTED_CHANGED_CONFIG),
            compute_event_hash(_SELECTED_VALUES_CHANGED_CONFIG),
            compute_event_hash(_UI_NAVIGATE_CONFIG),
            compute_event_hash(_UI_LEAVE_NAVIGATION_CONFIG),
            compute_event_hash(_UI_REFRESH_CONFIG),
            compute_event_hash(_FILE_REJECT_CONFIG),
            compute_event_hash(_FILE_REMOVE_CONFIG),
            compute_event_hash(_SUBMIT_CONFIG),
            compute_event_hash(_LOGIN_CONFIG),
            compute_event_hash(_SELECTED_ITEMS_CHANGED_CONFIG),
        }
        # All unique configs should produce unique hashes
        assert len(hashes) == 16

    def test_hash_format(self):
        """Hash is base64 encoded, 12 chars with trailing =."""
        h = compute_event_hash({})
        assert len(h) == 12
        assert h.endswith("=")

    def test_change_and_value_changed_same_config_same_hash(self):
        """change and value-changed have the same config, so same hash."""
        assert _CHANGE_HASH == _VALUE_CHANGED_HASH

    def test_closed_and_splitter_dragend_same_hash(self):
        """closed and splitter-dragend both have empty config, same hash."""
        assert _CLOSED_HASH == _SPLITTER_DRAGEND_HASH

    def test_upload_success_and_error_same_hash(self):
        """upload-success and upload-error have the same config."""
        assert _UPLOAD_SUCCESS_HASH == compute_event_hash(_UPLOAD_SUCCESS_CONFIG)

    @pytest.mark.parametrize("name,hash_val,config", [
        ("CLICK", _CLICK_HASH, _CLICK_CONFIG),
        ("CHANGE", _CHANGE_HASH, _CHANGE_CONFIG),
        ("OPENED_CHANGED", _OPENED_CHANGED_HASH, _OPENED_CHANGED_CONFIG),
        ("CHECKED_CHANGED", _CHECKED_CHANGED_HASH, _CHECKED_CHANGED_CONFIG),
        ("KEYDOWN", _KEYDOWN_HASH, _KEYDOWN_CONFIG),
        ("CLOSED", _CLOSED_HASH, _CLOSED_CONFIG),
        ("SELECTED_CHANGED", _SELECTED_CHANGED_HASH, _SELECTED_CHANGED_CONFIG),
        ("SELECTED_VALUES_CHANGED", _SELECTED_VALUES_CHANGED_HASH, _SELECTED_VALUES_CHANGED_CONFIG),
        ("VALUE_CHANGED", _VALUE_CHANGED_HASH, _VALUE_CHANGED_CONFIG),
        ("SELECTED_ITEMS_CHANGED", _SELECTED_ITEMS_CHANGED_HASH, _SELECTED_ITEMS_CHANGED_CONFIG),
        ("SPLITTER_DRAGEND", _SPLITTER_DRAGEND_HASH, _SPLITTER_DRAGEND_CONFIG),
        ("UI_NAVIGATE", _UI_NAVIGATE_HASH, _UI_NAVIGATE_CONFIG),
        ("UI_LEAVE_NAVIGATION", _UI_LEAVE_NAVIGATION_HASH, _UI_LEAVE_NAVIGATION_CONFIG),
        ("UI_REFRESH", _UI_REFRESH_HASH, _UI_REFRESH_CONFIG),
        ("FILE_REJECT", _FILE_REJECT_HASH, _FILE_REJECT_CONFIG),
        ("UPLOAD_SUCCESS", _UPLOAD_SUCCESS_HASH, _UPLOAD_SUCCESS_CONFIG),
        ("FILE_REMOVE", _FILE_REMOVE_HASH, _FILE_REMOVE_CONFIG),
        ("SUBMIT", _SUBMIT_HASH, _SUBMIT_CONFIG),
        ("LOGIN", _LOGIN_HASH, _LOGIN_CONFIG),
    ])
    def test_module_hash_matches_computed(self, name, hash_val, config):
        """Each module-level hash equals compute_event_hash(config)."""
        assert hash_val == compute_event_hash(config), f"{name} hash mismatch"

    def test_verified_java_hashes(self):
        """Verify hashes that were confirmed to match Java Flow output."""
        # These 10 hashes were verified against Java Flow captures
        assert _CLICK_HASH == "F8oCtNArLiI="
        assert _CHANGE_HASH == "Fg73o1qebBo="
        assert _KEYDOWN_HASH == "OSoHnU3SjNg="
        assert _CLOSED_HASH == "vIpODLLAUDo="
        assert _UI_NAVIGATE_HASH == "msDV4SvCysE="
        assert _UI_LEAVE_NAVIGATION_HASH == "i2nDWhpwLZE="
        assert _UI_REFRESH_HASH == "18ACma10cDE="
        assert _FILE_REJECT_HASH == "0dtnkjBiKGk="
        assert _UPLOAD_SUCCESS_HASH == "RwCOyvcoKgk="
        assert _FILE_REMOVE_HASH == "F6Wh0NdCR9A="
        assert _SUBMIT_HASH == "6cdZ3Qcd5ng="
        assert _LOGIN_HASH == "S9QZwwCzxQA="
        assert _SELECTED_VALUES_CHANGED_HASH == "NfDcIkUtPrY="
