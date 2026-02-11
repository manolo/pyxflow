"""WebSocket Push Tests."""

import asyncio
import json
import re

import aiohttp
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase

from vaadin.flow.server.http_server import _sessions
from vaadin.flow.router import AppShell, Push, clear_app_shell


class PushTestBase(AioHTTPTestCase):
    """Base class with helpers for push tests."""

    async def get_application(self):
        from vaadin.flow.server.http_server import create_app
        return create_app()

    def setUp(self):
        _sessions.clear()
        # Register @AppShell @Push so push is enabled
        @AppShell
        @Push
        class _TestAppShell:
            pass
        super().setUp()

    def tearDown(self):
        super().tearDown()
        _sessions.clear()
        clear_app_shell()

    async def _init_session(self):
        """Init a session and return (push_id, csrf_token)."""
        resp = await self.client.request("GET", "/?v-r=init&location=&query=")
        assert resp.status == 200
        data = await resp.json()
        uidl = data["appConfig"]["uidl"]
        push_id = uidl["Vaadin-Push-ID"]
        csrf = uidl["Vaadin-Security-Key"]
        return push_id, csrf


class TestPushAuth(PushTestBase):
    """Test push authentication and rejection."""

    async def test_push_without_session_returns_403(self):
        """WebSocket push without session cookie returns 403."""
        resp = await self.client.request("GET", "/VAADIN/push")
        assert resp.status == 403

    async def test_push_wrong_push_id_returns_403(self):
        """WebSocket push with wrong v-pushId returns 403."""
        await self._init_session()
        resp = await self.client.request("GET", "/VAADIN/push?v-pushId=wrong")
        assert resp.status == 403


class TestPushHandshake(PushTestBase):
    """Test Atmosphere handshake and heartbeat."""

    async def test_push_handshake_format(self):
        """First WS message is Atmosphere handshake: <len>|<UUID>|30000|X."""
        push_id, _ = await self._init_session()
        ws = await self.client.ws_connect(f"/VAADIN/push?v-pushId={push_id}")

        msg = await ws.receive(timeout=2)
        assert msg.type == aiohttp.WSMsgType.TEXT

        # Format: <length>|<UUID>|30000|X
        text = msg.data
        match = re.match(r"^(\d+)\|(.+)$", text)
        assert match, f"Expected <length>|<data>, got: {text}"
        length = int(match.group(1))
        data = match.group(2)
        assert len(data) == length
        parts = data.split("|")
        assert len(parts) == 3  # UUID|30000|X
        assert parts[1] == "30000"
        assert parts[2] == "X"
        # UUID format check
        assert re.match(r"^[0-9a-f-]{36}$", parts[0])

        await ws.close()

    async def test_push_heartbeat_accepted(self):
        """Sending 'X' heartbeat does not cause errors."""
        push_id, _ = await self._init_session()
        ws = await self.client.ws_connect(f"/VAADIN/push?v-pushId={push_id}")
        await ws.receive(timeout=2)  # consume handshake

        # Send heartbeat
        await ws.send_str("X")

        # Should not get an error or close — send another to confirm still alive
        await ws.send_str("X")

        await ws.close()

    async def test_push_reconnect_new_handshake(self):
        """Reconnecting gives a new UUID in the handshake."""
        push_id, _ = await self._init_session()

        # First connection
        ws1 = await self.client.ws_connect(f"/VAADIN/push?v-pushId={push_id}")
        msg1 = await ws1.receive(timeout=2)
        uuid1 = msg1.data.split("|")[1]
        await ws1.close()

        # Give server time to clean up
        await asyncio.sleep(0.05)

        # Second connection
        ws2 = await self.client.ws_connect(f"/VAADIN/push?v-pushId={push_id}")
        msg2 = await ws2.receive(timeout=2)
        uuid2 = msg2.data.split("|")[1]
        await ws2.close()

        assert uuid1 != uuid2


class TestPushMessages(PushTestBase):
    """Test push message delivery."""

    async def test_push_receives_changes(self):
        """Changes pushed via tree arrive on WS with meta.async."""
        push_id, _ = await self._init_session()
        ws = await self.client.ws_connect(f"/VAADIN/push?v-pushId={push_id}")
        await ws.receive(timeout=2)  # consume handshake

        # Inject a change and signal push
        session = list(_sessions.values())[0]
        tree = session["tree"]
        tree.add_change({"node": 10, "type": "put", "key": "text", "feat": 7, "value": "hello"})
        tree.notify_push()

        msg = await ws.receive(timeout=2)
        assert msg.type == aiohttp.WSMsgType.TEXT

        # Parse Atmosphere format
        text = msg.data
        pipe = text.index("|")
        payload = text[pipe + 1:]
        assert payload.startswith("for(;;);[")
        json_str = payload[len("for(;;);["):-1]
        data = json.loads(json_str)

        # Must have meta.async = True
        assert data.get("meta", {}).get("async") is True
        # Must have the change we added
        assert any(c.get("key") == "text" and c.get("value") == "hello"
                    for c in data.get("changes", []))

        await ws.close()

    async def test_push_message_atmosphere_format(self):
        """Push message matches <len>|for(;;);[{...}] format."""
        push_id, _ = await self._init_session()
        ws = await self.client.ws_connect(f"/VAADIN/push?v-pushId={push_id}")
        await ws.receive(timeout=2)  # consume handshake

        session = list(_sessions.values())[0]
        tree = session["tree"]
        tree.add_change({"node": 5, "type": "put", "key": "label", "feat": 1, "value": "test"})
        tree.notify_push()

        msg = await ws.receive(timeout=2)
        text = msg.data

        # Verify <length>|<message> format
        match = re.match(r"^(\d+)\|(.+)$", text, re.DOTALL)
        assert match, f"Expected <length>|<message>, got: {text[:100]}"
        declared_len = int(match.group(1))
        message = match.group(2)
        assert len(message) == declared_len
        assert message.startswith("for(;;);[")
        assert message.endswith("]")

        await ws.close()

    async def test_push_no_message_without_changes(self):
        """Signalling push without changes does not send a message."""
        push_id, _ = await self._init_session()
        ws = await self.client.ws_connect(f"/VAADIN/push?v-pushId={push_id}")
        await ws.receive(timeout=2)  # consume handshake

        session = list(_sessions.values())[0]
        tree = session["tree"]
        # Signal push without adding changes
        tree.notify_push()

        # Should not receive a message (use short timeout)
        try:
            msg = await asyncio.wait_for(ws.receive(), timeout=0.2)
            # If we get a message, it should be a close, not data
            assert msg.type != aiohttp.WSMsgType.TEXT, "Got unexpected push message with no changes"
        except asyncio.TimeoutError:
            pass  # Expected — no message

        await ws.close()


class TestPushReconnect(PushTestBase):
    """Test push reconnect delivers buffered messages."""

    async def test_push_reconnect_delivers_pending(self):
        """Buffered message from failed send is delivered on reconnect."""
        push_id, _ = await self._init_session()
        session = list(_sessions.values())[0]
        tree = session["tree"]

        # Connect first WS
        ws1 = await self.client.ws_connect(f"/VAADIN/push?v-pushId={push_id}")
        await ws1.receive(timeout=2)  # consume handshake

        # Give sender task time to start
        await asyncio.sleep(0.05)

        # Close the WS abruptly from client side
        await ws1.close()

        # Give server time to detect close and clean up sender
        await asyncio.sleep(0.1)

        # Now add a change and set it as pending_push (simulating failed send)
        tree.add_change({"node": 99, "type": "put", "key": "text", "feat": 7, "value": "reconnected"})
        handler = session["handler"]
        response_data = handler._build_response()
        response_data["meta"] = {"async": True}
        message = f"for(;;);[{json.dumps(response_data)}]"
        prefixed = f"{len(message)}|{message}"
        session["pending_push"] = prefixed

        # Reconnect
        ws2 = await self.client.ws_connect(f"/VAADIN/push?v-pushId={push_id}")
        await ws2.receive(timeout=2)  # consume handshake

        # The buffered message should arrive
        msg = await ws2.receive(timeout=2)
        assert msg.type == aiohttp.WSMsgType.TEXT
        text = msg.data
        pipe = text.index("|")
        payload = text[pipe + 1:]
        json_str = payload[len("for(;;);["):-1]
        data = json.loads(json_str)
        assert any(c.get("value") == "reconnected" for c in data.get("changes", []))

        await ws2.close()


class TestPushInitConfig(PushTestBase):
    """Test push-related init configuration."""

    async def test_push_init_config(self):
        """Init response has pushScript at top level, pushMode and Vaadin-Push-ID in uidl."""
        resp = await self.client.request("GET", "/?v-r=init&location=&query=")
        data = await resp.json()

        # pushScript at top level (alongside appConfig)
        assert "pushScript" in data, "pushScript must be at top level of init response"
        assert data["pushScript"] == "VAADIN/static/push/vaadinPush.js"

        # Vaadin-Push-ID in uidl
        uidl = data["appConfig"]["uidl"]
        assert "Vaadin-Push-ID" in uidl
        push_id = uidl["Vaadin-Push-ID"]
        assert len(push_id) == 32  # hex(16) = 32 chars

        # pushMode in initial changes (node 1, feat 5)
        changes = uidl.get("changes", [])
        push_mode_changes = [c for c in changes
                             if c.get("node") == 1
                             and c.get("key") == "pushMode"
                             and c.get("value") == "AUTOMATIC"]
        assert len(push_mode_changes) == 1, "pushMode=AUTOMATIC must be in init changes"
