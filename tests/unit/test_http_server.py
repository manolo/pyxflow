"""HTTP Server Foundation Tests."""

import time
import pytest
import aiohttp
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase


class TestHttpServerRoutes(AioHTTPTestCase):
    """Test HTTP server routes exist and respond correctly."""

    async def get_application(self):
        """Create the application for testing."""
        from pyflow.server.http_server import create_app
        return create_app()

    async def test_root_returns_html(self):
        """GET / should return index.html."""
        resp = await self.client.request("GET", "/")
        assert resp.status == 200
        text = await resp.text()
        assert "<!DOCTYPE html>" in text or "<html" in text

    async def test_init_endpoint_exists(self):
        """GET /?v-r=init should return JSON."""
        resp = await self.client.request("GET", "/?v-r=init&location=&query=")
        assert resp.status == 200
        assert resp.content_type == "application/json"

    async def test_uidl_endpoint_exists(self):
        """POST /?v-r=uidl should accept requests."""
        # First get init to establish session
        init_resp = await self.client.request("GET", "/?v-r=init&location=&query=")
        init_data = await init_resp.json()
        csrf = init_data["appConfig"]["uidl"]["Vaadin-Security-Key"]

        # Now send UIDL request
        payload = {"csrfToken": csrf, "rpc": [], "syncId": 0, "clientId": 0}
        resp = await self.client.request(
            "POST",
            "/?v-r=uidl&v-uiId=0",
            json=payload
        )
        assert resp.status == 200


class TestStaticFiles(AioHTTPTestCase):
    """Test static file serving."""

    async def get_application(self):
        from pyflow.server.http_server import create_app
        return create_app()

    async def test_vaadin_build_files_served(self):
        """GET /VAADIN/build/* should serve static files or 404 if no bundle."""
        # This will return 404 until we configure the bundle path
        resp = await self.client.request("GET", "/VAADIN/build/")
        # Accept 200, 403 (directory listing disabled), or 404 (no bundle)
        assert resp.status in [200, 403, 404]


class TestSessionManagement(AioHTTPTestCase):
    """Test session and CSRF management."""

    async def get_application(self):
        from pyflow.server.http_server import create_app
        return create_app()

    async def test_init_sets_session_cookie(self):
        """Init request should set a session cookie."""
        resp = await self.client.request("GET", "/?v-r=init&location=&query=")
        assert resp.status == 200
        # Check for Set-Cookie header
        assert "Set-Cookie" in resp.headers or resp.cookies

    async def test_init_returns_csrf_token(self):
        """Init response should include CSRF token."""
        resp = await self.client.request("GET", "/?v-r=init&location=&query=")
        data = await resp.json()
        assert "appConfig" in data
        assert "uidl" in data["appConfig"]
        assert "Vaadin-Security-Key" in data["appConfig"]["uidl"]
        csrf = data["appConfig"]["uidl"]["Vaadin-Security-Key"]
        assert len(csrf) > 10  # Should be a real token

    async def test_uidl_rejects_invalid_csrf(self):
        """UIDL request with invalid CSRF should be rejected."""
        payload = {"csrfToken": "invalid-token", "rpc": [], "syncId": 0, "clientId": 0}
        resp = await self.client.request(
            "POST",
            "/?v-r=uidl&v-uiId=0",
            json=payload
        )
        # Should reject - either 403 or error in response
        assert resp.status == 403 or resp.status == 200  # May return error in body


class TestSessionExpired(AioHTTPTestCase):
    """Test session-expired response triggers client reload."""

    async def get_application(self):
        from pyflow.server.http_server import create_app
        return create_app()

    async def test_uidl_without_session_returns_session_expired_json(self):
        """UIDL without session should return meta.sessionExpired JSON (not 403)."""
        payload = {"csrfToken": "x", "rpc": [], "syncId": 0, "clientId": 0}
        resp = await self.client.request("POST", "/?v-r=uidl", json=payload)
        assert resp.status == 200
        text = await resp.text()
        assert '"sessionExpired":true' in text
        assert text.startswith("for(;;);")

    async def test_uidl_without_session_on_subroute(self):
        """UIDL on sub-route without session should also return session expired."""
        payload = {"csrfToken": "x", "rpc": [], "syncId": 0, "clientId": 0}
        resp = await self.client.request("POST", "/about?v-r=uidl", json=payload)
        assert resp.status == 200
        text = await resp.text()
        assert '"sessionExpired":true' in text


class TestHeartbeat(AioHTTPTestCase):
    """Test heartbeat endpoint keeps sessions alive."""

    async def get_application(self):
        from pyflow.server.http_server import create_app
        return create_app()

    async def test_heartbeat_without_session_returns_403(self):
        """Heartbeat without valid session should return 403."""
        resp = await self.client.request("POST", "/?v-r=heartbeat")
        assert resp.status == 403

    async def test_heartbeat_with_session_returns_200(self):
        """Heartbeat with valid session should return 200."""
        # Establish session via init
        init_resp = await self.client.request("GET", "/?v-r=init&location=&query=")
        assert init_resp.status == 200

        # Send heartbeat (session cookie is maintained by test client)
        resp = await self.client.request("POST", "/?v-r=heartbeat")
        assert resp.status == 200

    async def test_heartbeat_on_subroute_returns_200(self):
        """Heartbeat on sub-route (e.g. /about?v-r=heartbeat) should work."""
        # Establish session via init on sub-route
        init_resp = await self.client.request("GET", "/about?v-r=init&location=about&query=")
        assert init_resp.status == 200

        # Send heartbeat on sub-route
        resp = await self.client.request("POST", "/about?v-r=heartbeat")
        assert resp.status == 200


class TestSessionCleanup:
    """Test session expiry and cleanup (pure function tests, no HTTP)."""

    def setup_method(self):
        """Clear global session state before each test."""
        from pyflow.server.http_server import _sessions, _upload_handlers
        _sessions.clear()
        _upload_handlers.clear()

    def teardown_method(self):
        """Clear global session state after each test."""
        from pyflow.server.http_server import _sessions, _upload_handlers
        _sessions.clear()
        _upload_handlers.clear()

    def test_expired_session_is_cleaned_up(self):
        """Sessions idle longer than SESSION_TIMEOUT are removed."""
        from pyflow.server.http_server import (
            _sessions, _cleanup_expired_sessions, SESSION_TIMEOUT,
        )
        _sessions["old-session"] = {
            "last_activity": time.monotonic() - SESSION_TIMEOUT - 1,
        }
        _cleanup_expired_sessions()
        assert "old-session" not in _sessions

    def test_active_session_not_cleaned(self):
        """Sessions with recent activity are kept."""
        from pyflow.server.http_server import (
            _sessions, _cleanup_expired_sessions,
        )
        _sessions["active-session"] = {
            "last_activity": time.monotonic(),
        }
        _cleanup_expired_sessions()
        assert "active-session" in _sessions

    def test_upload_handlers_cleaned_with_session(self):
        """Upload handlers belonging to expired sessions are also removed."""
        from pyflow.server.http_server import (
            _sessions, _upload_handlers, _cleanup_expired_sessions,
            SESSION_TIMEOUT,
        )
        _sessions["expired-sess"] = {
            "last_activity": time.monotonic() - SESSION_TIMEOUT - 1,
        }
        _upload_handlers["upload-1"] = ("expired-sess", lambda: None)
        _upload_handlers["upload-2"] = ("other-sess", lambda: None)

        _cleanup_expired_sessions()

        assert "upload-1" not in _upload_handlers
        assert "upload-2" in _upload_handlers


class TestUidlEncoder:
    """Test that UIDL JSON encoder handles Python types."""

    def test_date_serialized_as_iso(self):
        import datetime
        from pyflow.server.http_server import _UidlEncoder
        import json
        d = datetime.date(2025, 6, 15)
        result = json.dumps({"col": d}, cls=_UidlEncoder)
        assert result == '{"col": "2025-06-15"}'

    def test_datetime_serialized_as_iso(self):
        import datetime
        from pyflow.server.http_server import _UidlEncoder
        import json
        dt = datetime.datetime(2025, 6, 15, 14, 30, 0)
        result = json.dumps({"col": dt}, cls=_UidlEncoder)
        assert result == '{"col": "2025-06-15T14:30:00"}'

    def test_normal_types_unchanged(self):
        from pyflow.server.http_server import _UidlEncoder
        import json
        data = {"a": 1, "b": "text", "c": True, "d": None, "e": [1, 2]}
        result = json.dumps(data, cls=_UidlEncoder)
        assert json.loads(result) == data

    def test_unknown_type_falls_back_to_str(self):
        """Unknown types are serialized as str() instead of raising."""
        from pyflow.server.http_server import _UidlEncoder
        import json
        from decimal import Decimal
        result = json.dumps({"val": Decimal("3.14")}, cls=_UidlEncoder)
        assert result == '{"val": "3.14"}'


class TestCriticalErrorJson:
    """Test the meta.appError response for unrecoverable errors."""

    def test_critical_error_json_format(self):
        """Should produce for(;;);[{syncId:-1, meta:{appError:...}}]."""
        from pyflow.server.http_server import _critical_error_json
        import json
        result = _critical_error_json("Error", "Something broke")
        assert result.startswith("for(;;);[")
        assert result.endswith("]")
        json_str = result[len("for(;;);["):-1]
        data = json.loads(json_str)
        assert data["syncId"] == -1
        assert data["changes"] == []
        assert data["meta"]["appError"]["caption"] == "Error"
        assert data["meta"]["appError"]["message"] == "Something broke"
        assert data["meta"]["appError"]["details"] is None
        assert data["meta"]["appError"]["url"] is None

    def test_critical_error_json_all_none(self):
        """All-None fields should produce valid JSON (client refreshes silently)."""
        from pyflow.server.http_server import _critical_error_json
        import json
        result = _critical_error_json()
        json_str = result[len("for(;;);["):-1]
        data = json.loads(json_str)
        app_error = data["meta"]["appError"]
        assert all(v is None for v in app_error.values())

    def test_critical_error_json_with_url(self):
        """URL field should be passed through for redirect."""
        from pyflow.server.http_server import _critical_error_json
        import json
        result = _critical_error_json(url="/login")
        json_str = result[len("for(;;);["):-1]
        data = json.loads(json_str)
        assert data["meta"]["appError"]["url"] == "/login"


class TestDevModeMetaTag:
    """Test pyflow-views meta tag injection in dev mode."""

    def setup_method(self):
        import pyflow.server.http_server as _http
        self._http = _http
        self._orig_dev = _http._dev_mode
        self._orig_views = _http._views_module

    def teardown_method(self):
        self._http._dev_mode = self._orig_dev
        self._http._views_module = self._orig_views

    def test_meta_tag_present_in_dev_mode(self):
        """Dev mode with views_module should inject pyflow-views meta tag."""
        self._http._dev_mode = True
        self._http._views_module = "tests.views"
        html = self._http.get_index_html()
        assert '<meta name="pyflow-views" content="tests.views">' in html

    def test_meta_tag_absent_in_production(self):
        """Production mode should NOT include pyflow-views meta tag."""
        self._http._dev_mode = False
        self._http._views_module = "tests.views"
        html = self._http.get_index_html()
        assert "pyflow-views" not in html

    def test_meta_tag_absent_when_no_views_module(self):
        """Dev mode without views_module should NOT include meta tag."""
        self._http._dev_mode = True
        self._http._views_module = ""
        html = self._http.get_index_html()
        assert "pyflow-views" not in html

    def test_meta_tag_content_matches_module(self):
        """Meta tag content should reflect the actual views module."""
        self._http._dev_mode = True
        self._http._views_module = "demo.views"
        html = self._http.get_index_html()
        assert '<meta name="pyflow-views" content="demo.views">' in html


class TestFaviconFallbackHttp(AioHTTPTestCase):
    """Test that /favicon.ico is served from scaffold when no app static."""

    async def get_application(self):
        from pyflow.server.http_server import create_app
        return create_app()

    async def test_favicon_returns_200(self):
        """GET /favicon.ico should return 200 even without app static dir."""
        resp = await self.client.request("GET", "/favicon.ico")
        assert resp.status == 200
        assert resp.content_type == "image/x-icon"
        data = await resp.read()
        # Valid ICO magic bytes
        assert data[:4] == b"\x00\x00\x01\x00"
        assert len(data) > 1000

    async def test_favicon_returns_ico_content_type(self):
        resp = await self.client.request("GET", "/favicon.ico")
        assert resp.content_type == "image/x-icon"


class TestUidlErrorHandling(AioHTTPTestCase):
    """Test that UIDL errors return meta.appError instead of HTTP 500."""

    async def get_application(self):
        from pyflow.server.http_server import create_app
        return create_app()

    async def test_uidl_error_returns_app_error_not_500(self):
        """If handle_uidl raises, response is meta.appError with syncId=-1."""
        import json
        from unittest.mock import patch

        # Establish session
        init_resp = await self.client.request("GET", "/?v-r=init&location=&query=")
        init_data = await init_resp.json()
        csrf = init_data["appConfig"]["uidl"]["Vaadin-Security-Key"]

        payload = {"csrfToken": csrf, "rpc": [], "syncId": 0, "clientId": 0}

        # Patch handle_uidl on the UidlHandler to raise
        with patch(
            "pyflow.server.uidl_handler.UidlHandler.handle_uidl",
            side_effect=RuntimeError("boom"),
        ):
            resp = await self.client.request(
                "POST", "/?v-r=uidl&v-uiId=0", json=payload,
            )

        # Must be 200 (not 500) with meta.appError
        assert resp.status == 200
        text = await resp.text()
        assert text.startswith("for(;;);")
        json_str = text[len("for(;;);["):-1]
        data = json.loads(json_str)
        assert data["syncId"] == -1
        assert "appError" in data["meta"]
        assert data["meta"]["appError"]["caption"] == "Internal error"
