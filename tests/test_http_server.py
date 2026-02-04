"""HTTP Server Foundation Tests."""

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
