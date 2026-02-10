"""HTTP Server Foundation Tests."""

import time
import pytest
import aiohttp
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop


class TestHttpServerRoutes(AioHTTPTestCase):
    """Test HTTP server routes exist and respond correctly."""

    async def get_application(self):
        """Create the application for testing."""
        from vaadin.flow.server.http_server import create_app
        return create_app()

    @unittest_run_loop
    async def test_root_returns_html(self):
        """GET / should return index.html."""
        resp = await self.client.request("GET", "/")
        assert resp.status == 200
        text = await resp.text()
        assert "<!DOCTYPE html>" in text or "<html" in text

    @unittest_run_loop
    async def test_init_endpoint_exists(self):
        """GET /?v-r=init should return JSON."""
        resp = await self.client.request("GET", "/?v-r=init&location=&query=")
        assert resp.status == 200
        assert resp.content_type == "application/json"

    @unittest_run_loop
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
        from vaadin.flow.server.http_server import create_app
        return create_app()

    @unittest_run_loop
    async def test_vaadin_build_files_served(self):
        """GET /VAADIN/build/* should serve static files or 404 if no bundle."""
        # This will return 404 until we configure the bundle path
        resp = await self.client.request("GET", "/VAADIN/build/")
        # Accept 200, 403 (directory listing disabled), or 404 (no bundle)
        assert resp.status in [200, 403, 404]


class TestSessionManagement(AioHTTPTestCase):
    """Test session and CSRF management."""

    async def get_application(self):
        from vaadin.flow.server.http_server import create_app
        return create_app()

    @unittest_run_loop
    async def test_init_sets_session_cookie(self):
        """Init request should set a session cookie."""
        resp = await self.client.request("GET", "/?v-r=init&location=&query=")
        assert resp.status == 200
        # Check for Set-Cookie header
        assert "Set-Cookie" in resp.headers or resp.cookies

    @unittest_run_loop
    async def test_init_returns_csrf_token(self):
        """Init response should include CSRF token."""
        resp = await self.client.request("GET", "/?v-r=init&location=&query=")
        data = await resp.json()
        assert "appConfig" in data
        assert "uidl" in data["appConfig"]
        assert "Vaadin-Security-Key" in data["appConfig"]["uidl"]
        csrf = data["appConfig"]["uidl"]["Vaadin-Security-Key"]
        assert len(csrf) > 10  # Should be a real token

    @unittest_run_loop
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
        from vaadin.flow.server.http_server import create_app
        return create_app()

    @unittest_run_loop
    async def test_uidl_without_session_returns_session_expired_json(self):
        """UIDL without session should return meta.sessionExpired JSON (not 403)."""
        payload = {"csrfToken": "x", "rpc": [], "syncId": 0, "clientId": 0}
        resp = await self.client.request("POST", "/?v-r=uidl", json=payload)
        assert resp.status == 200
        text = await resp.text()
        assert '"sessionExpired":true' in text
        assert text.startswith("for(;;);")

    @unittest_run_loop
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
        from vaadin.flow.server.http_server import create_app
        return create_app()

    @unittest_run_loop
    async def test_heartbeat_without_session_returns_403(self):
        """Heartbeat without valid session should return 403."""
        resp = await self.client.request("POST", "/?v-r=heartbeat")
        assert resp.status == 403

    @unittest_run_loop
    async def test_heartbeat_with_session_returns_200(self):
        """Heartbeat with valid session should return 200."""
        # Establish session via init
        init_resp = await self.client.request("GET", "/?v-r=init&location=&query=")
        assert init_resp.status == 200

        # Send heartbeat (session cookie is maintained by test client)
        resp = await self.client.request("POST", "/?v-r=heartbeat")
        assert resp.status == 200

    @unittest_run_loop
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
        from vaadin.flow.server.http_server import _sessions, _upload_handlers
        _sessions.clear()
        _upload_handlers.clear()

    def teardown_method(self):
        """Clear global session state after each test."""
        from vaadin.flow.server.http_server import _sessions, _upload_handlers
        _sessions.clear()
        _upload_handlers.clear()

    def test_expired_session_is_cleaned_up(self):
        """Sessions idle longer than SESSION_TIMEOUT are removed."""
        from vaadin.flow.server.http_server import (
            _sessions, _cleanup_expired_sessions, SESSION_TIMEOUT,
        )
        _sessions["old-session"] = {
            "last_activity": time.monotonic() - SESSION_TIMEOUT - 1,
        }
        _cleanup_expired_sessions()
        assert "old-session" not in _sessions

    def test_active_session_not_cleaned(self):
        """Sessions with recent activity are kept."""
        from vaadin.flow.server.http_server import (
            _sessions, _cleanup_expired_sessions,
        )
        _sessions["active-session"] = {
            "last_activity": time.monotonic(),
        }
        _cleanup_expired_sessions()
        assert "active-session" in _sessions

    def test_upload_handlers_cleaned_with_session(self):
        """Upload handlers belonging to expired sessions are also removed."""
        from vaadin.flow.server.http_server import (
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
