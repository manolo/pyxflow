"""Tests for Request / Response context API."""

import pytest
from unittest.mock import MagicMock, PropertyMock

from pyxflow.server.http_server import (
    Request, Response, _current_request, _current_response,
)


# ── Request ─────────────────────────────────────────────────────────────

class TestRequest:
    """Tests for the Request wrapper."""

    def _make_request(self, *, cookies=None, headers=None, secure=False, peername=None):
        """Build a mock aiohttp request."""
        r = MagicMock()
        r.cookies = cookies or {}
        r.headers = headers or {}
        r.secure = secure
        transport = MagicMock()
        transport.get_extra_info.return_value = peername
        r.transport = transport
        return r

    def test_get_current_returns_none_by_default(self):
        assert Request.get_current() is None

    def test_get_current_returns_set_value(self):
        req = Request(self._make_request())
        token = _current_request.set(req)
        try:
            assert Request.get_current() is req
        finally:
            _current_request.reset(token)

    def test_get_cookies(self):
        req = Request(self._make_request(cookies={"a": "1", "b": "2"}))
        assert req.get_cookies() == {"a": "1", "b": "2"}

    def test_get_cookie_existing(self):
        req = Request(self._make_request(cookies={"theme": "dark"}))
        assert req.get_cookie("theme") == "dark"

    def test_get_cookie_missing(self):
        req = Request(self._make_request())
        assert req.get_cookie("missing") is None

    def test_get_header(self):
        req = Request(self._make_request(headers={"User-Agent": "TestBot"}))
        assert req.get_header("User-Agent") == "TestBot"

    def test_get_header_missing(self):
        req = Request(self._make_request())
        assert req.get_header("X-Missing") is None

    def test_get_headers(self):
        req = Request(self._make_request(headers={"A": "1", "B": "2"}))
        assert req.get_headers() == {"A": "1", "B": "2"}

    def test_get_remote_address(self):
        req = Request(self._make_request(peername=("192.168.1.1", 12345)))
        assert req.get_remote_address() == "192.168.1.1"

    def test_get_remote_address_no_transport(self):
        r = MagicMock()
        r.transport = None
        req = Request(r)
        assert req.get_remote_address() is None

    def test_get_remote_address_no_peername(self):
        req = Request(self._make_request(peername=None))
        assert req.get_remote_address() is None

    def test_is_secure_true(self):
        req = Request(self._make_request(secure=True))
        assert req.is_secure() is True

    def test_is_secure_false(self):
        req = Request(self._make_request(secure=False))
        assert req.is_secure() is False


# ── Response ────────────────────────────────────────────────────────────

class TestResponse:
    """Tests for the Response wrapper."""

    def test_get_current_returns_none_by_default(self):
        assert Response.get_current() is None

    def test_get_current_returns_set_value(self):
        resp = Response()
        token = _current_response.set(resp)
        try:
            assert Response.get_current() is resp
        finally:
            _current_response.reset(token)

    def test_set_header(self):
        resp = Response()
        resp.set_header("X-Custom", "hello")
        mock_response = MagicMock()
        mock_response.headers = {}
        resp._apply_to(mock_response)
        assert mock_response.headers["X-Custom"] == "hello"

    def test_set_header_overwrites(self):
        resp = Response()
        resp.set_header("X-A", "1")
        resp.set_header("X-A", "2")
        mock_response = MagicMock()
        mock_response.headers = {}
        resp._apply_to(mock_response)
        assert mock_response.headers["X-A"] == "2"

    def test_add_cookie_minimal(self):
        resp = Response()
        resp.add_cookie("theme", "dark")
        mock_response = MagicMock()
        resp._apply_to(mock_response)
        mock_response.set_cookie.assert_called_once_with(
            "theme", "dark",
            path="/", secure=False, httponly=False, samesite="Lax",
        )

    def test_add_cookie_full(self):
        resp = Response()
        resp.add_cookie(
            "session", "abc123",
            max_age=3600, path="/app", domain="example.com",
            secure=True, httponly=True, samesite="Strict",
        )
        mock_response = MagicMock()
        resp._apply_to(mock_response)
        mock_response.set_cookie.assert_called_once_with(
            "session", "abc123",
            path="/app", secure=True, httponly=True, samesite="Strict",
            max_age=3600, domain="example.com",
        )

    def test_add_multiple_cookies(self):
        resp = Response()
        resp.add_cookie("a", "1")
        resp.add_cookie("b", "2")
        mock_response = MagicMock()
        resp._apply_to(mock_response)
        assert mock_response.set_cookie.call_count == 2

    def test_apply_to_empty(self):
        """Applying an empty response should not raise."""
        resp = Response()
        mock_response = MagicMock()
        mock_response.headers = {}
        resp._apply_to(mock_response)
        mock_response.set_cookie.assert_not_called()


# ── Import from pyxflow ─────────────────────────────────────────────────

class TestExports:
    """Verify Request/Response are importable from the top-level package."""

    def test_import_request(self):
        from pyxflow import Request as R
        assert R is Request

    def test_import_response(self):
        from pyxflow import Response as R
        assert R is Response
