"""Tests for multiple UIs per session (multi-tab support)."""

import json

from aiohttp.test_utils import AioHTTPTestCase

from vaadin.flow.server.http_server import _sessions


class TestMultiUI(AioHTTPTestCase):
    """Test that multiple browser tabs get independent UIs."""

    async def get_application(self):
        from vaadin.flow.server.http_server import create_app
        return create_app()

    def setUp(self):
        _sessions.clear()
        super().setUp()

    def tearDown(self):
        super().tearDown()
        _sessions.clear()

    async def _do_init(self, cookies=None):
        """Send init request, optionally with existing session cookie.

        Returns (response_data, session_cookie).
        """
        headers = {}
        if cookies:
            headers["Cookie"] = cookies
        resp = await self.client.request(
            "GET", "/?v-r=init&location=&query=", headers=headers
        )
        assert resp.status == 200
        data = await resp.json()
        # Extract Set-Cookie header
        cookie = resp.cookies.get("JSESSIONID")
        cookie_value = cookie.value if cookie else None
        return data, cookie_value

    async def test_first_init_creates_ui_0(self):
        """First init on a new session creates UI with v-uiId=0."""
        data, _ = await self._do_init()
        assert data["appConfig"]["v-uiId"] == 0

    async def test_second_init_creates_ui_1(self):
        """Second init on same session creates UI with v-uiId=1."""
        data1, cookie = await self._do_init()
        assert data1["appConfig"]["v-uiId"] == 0

        # Second init with same session cookie
        data2, _ = await self._do_init(cookies=f"JSESSIONID={cookie}")
        assert data2["appConfig"]["v-uiId"] == 1

    async def test_session_has_two_uis(self):
        """After two inits, session has two UI entries."""
        data1, cookie = await self._do_init()
        data2, _ = await self._do_init(cookies=f"JSESSIONID={cookie}")

        session = list(_sessions.values())[0]
        assert len(session["uis"]) == 2
        assert 0 in session["uis"]
        assert 1 in session["uis"]

    async def test_each_ui_has_independent_tree(self):
        """Each UI has its own StateTree instance."""
        _, cookie = await self._do_init()
        await self._do_init(cookies=f"JSESSIONID={cookie}")

        session = list(_sessions.values())[0]
        tree0 = session["uis"][0]["tree"]
        tree1 = session["uis"][1]["tree"]
        assert tree0 is not tree1

    async def test_each_ui_has_independent_handler(self):
        """Each UI has its own UidlHandler instance."""
        _, cookie = await self._do_init()
        await self._do_init(cookies=f"JSESSIONID={cookie}")

        session = list(_sessions.values())[0]
        handler0 = session["uis"][0]["handler"]
        handler1 = session["uis"][1]["handler"]
        assert handler0 is not handler1

    async def test_shared_csrf_token(self):
        """All UIs in a session share the same CSRF token."""
        data1, cookie = await self._do_init()
        data2, _ = await self._do_init(cookies=f"JSESSIONID={cookie}")

        csrf1 = data1["appConfig"]["uidl"]["Vaadin-Security-Key"]
        csrf2 = data2["appConfig"]["uidl"]["Vaadin-Security-Key"]
        assert csrf1 == csrf2

    async def test_uidl_routes_to_correct_ui(self):
        """UIDL with v-uiId=N routes to the correct handler."""
        data1, cookie = await self._do_init()
        data2, _ = await self._do_init(cookies=f"JSESSIONID={cookie}")

        csrf = data1["appConfig"]["uidl"]["Vaadin-Security-Key"]
        session = list(_sessions.values())[0]

        # Send UIDL to UI 0
        handler0 = session["uis"][0]["handler"]
        sync_id_0 = handler0._sync_id

        resp = await self.client.request(
            "POST", "/?v-r=uidl&v-uiId=0",
            json={"csrfToken": csrf, "syncId": sync_id_0, "clientId": 0, "rpc": []},
            headers={"Cookie": f"JSESSIONID={cookie}"},
        )
        assert resp.status == 200

        # Handler 0's syncId should have incremented
        assert handler0._sync_id == sync_id_0 + 1

        # Handler 1's syncId should be unchanged
        handler1 = session["uis"][1]["handler"]
        assert handler1._sync_id == 0  # Still at init value (handle_init sets it to 0, then _build_response increments it during init navigation... but no UIDL was sent to it)

    async def test_invalid_ui_id_returns_session_expired(self):
        """UIDL with non-existent v-uiId returns session-expired."""
        data, cookie = await self._do_init()
        csrf = data["appConfig"]["uidl"]["Vaadin-Security-Key"]

        resp = await self.client.request(
            "POST", "/?v-r=uidl&v-uiId=99",
            json={"csrfToken": csrf, "syncId": 0, "clientId": 0, "rpc": []},
            headers={"Cookie": f"JSESSIONID={cookie}"},
        )
        assert resp.status == 200
        text = await resp.text()
        assert "sessionExpired" in text

    async def test_page_reload_creates_new_ui(self):
        """Page reload (new init on same session) creates a new UI, not reusing old one."""
        data1, cookie = await self._do_init()
        ui_id_1 = data1["appConfig"]["v-uiId"]

        # Simulate page reload — new init on same session
        data2, _ = await self._do_init(cookies=f"JSESSIONID={cookie}")
        ui_id_2 = data2["appConfig"]["v-uiId"]

        assert ui_id_1 != ui_id_2
        assert ui_id_1 == 0
        assert ui_id_2 == 1
