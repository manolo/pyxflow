"""Tests for LoginForm and LoginOverlay components."""

import pytest

from vaadin.flow.components.login import LoginForm, LoginOverlay
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestLoginForm:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        lf = LoginForm()
        assert lf._tag == "vaadin-login-form"

    def test_create(self):
        lf = LoginForm()
        assert lf._error is False
        assert lf._no_forgot_password is False
        assert lf._login_listeners == []
        assert lf._forgot_password_listeners == []
        assert lf._action == ""

    def test_attach(self, tree):
        lf = LoginForm()
        lf._attach(tree)
        assert lf._element is not None

    def test_attach_registers_events(self, tree):
        lf = LoginForm()
        lf._attach(tree)
        assert "login" in lf.element._listeners
        assert "forgot-password" in lf.element._listeners

    def test_attach_event_listeners_in_changes(self, tree):
        lf = LoginForm()
        lf._attach(tree)
        changes = tree.collect_changes()
        listener_changes = [
            c for c in changes if c.get("feat") == Feature.ELEMENT_LISTENER_MAP
        ]
        event_names = [c["key"] for c in listener_changes]
        assert "login" in event_names
        assert "forgot-password" in event_names

    def test_set_error(self):
        lf = LoginForm()
        lf.set_error(True)
        assert lf.is_error()

    def test_set_error_after_attach(self, tree):
        lf = LoginForm()
        lf._attach(tree)
        tree.collect_changes()

        lf.set_error(True)
        changes = tree.collect_changes()
        error_changes = [c for c in changes if c.get("key") == "error"]
        assert any(c["value"] is True for c in error_changes)

    def test_set_forgot_password_visible(self):
        lf = LoginForm()
        lf.set_forgot_password_button_visible(False)
        assert lf._no_forgot_password is True

    def test_set_forgot_password_visible_after_attach(self, tree):
        lf = LoginForm()
        lf._attach(tree)
        tree.collect_changes()

        lf.set_forgot_password_button_visible(False)
        changes = tree.collect_changes()
        nfp_changes = [c for c in changes if c.get("key") == "noForgotPassword"]
        assert any(c["value"] is True for c in nfp_changes)

    def test_login_event(self, tree):
        lf = LoginForm()
        lf._attach(tree)

        events = []
        lf.add_login_listener(lambda e: events.append(e))
        lf._on_login({"event.detail.username": "user", "event.detail.password": "pass"})
        assert len(events) == 1
        assert events[0]["username"] == "user"
        assert events[0]["password"] == "pass"

    def test_login_event_empty(self, tree):
        lf = LoginForm()
        lf._attach(tree)

        events = []
        lf.add_login_listener(lambda e: events.append(e))
        lf._on_login({})
        assert events[0]["username"] == ""
        assert events[0]["password"] == ""

    def test_forgot_password_event(self, tree):
        lf = LoginForm()
        lf._attach(tree)

        events = []
        lf.add_forgot_password_listener(lambda e: events.append(e))
        lf._on_forgot_password({})
        assert len(events) == 1

    def test_multiple_login_listeners(self):
        lf = LoginForm()
        results = []
        lf.add_login_listener(lambda e: results.append("a"))
        lf.add_login_listener(lambda e: results.append("b"))
        lf._on_login({"event.detail.username": "u", "event.detail.password": "p"})
        assert results == ["a", "b"]

    def test_set_action(self):
        lf = LoginForm()
        lf.set_action("/login")
        assert lf._action == "/login"

    def test_set_action_after_attach(self, tree):
        lf = LoginForm()
        lf._attach(tree)
        tree.collect_changes()

        lf.set_action("/login")
        changes = tree.collect_changes()
        action_changes = [c for c in changes if c.get("key") == "action"]
        assert any(c["value"] == "/login" for c in action_changes)

    def test_attach_with_error(self, tree):
        lf = LoginForm()
        lf.set_error(True)
        lf._attach(tree)

        changes = tree.collect_changes()
        error_changes = [c for c in changes if c.get("key") == "error"]
        assert any(c["value"] is True for c in error_changes)

    def test_attach_with_no_forgot_password(self, tree):
        lf = LoginForm()
        lf.set_forgot_password_button_visible(False)
        lf._attach(tree)

        changes = tree.collect_changes()
        nfp_changes = [c for c in changes if c.get("key") == "noForgotPassword"]
        assert any(c["value"] is True for c in nfp_changes)

    def test_attach_with_action(self, tree):
        lf = LoginForm()
        lf.set_action("/auth")
        lf._attach(tree)

        changes = tree.collect_changes()
        action_changes = [c for c in changes if c.get("key") == "action"]
        assert any(c["value"] == "/auth" for c in action_changes)

    def test_login_re_enables_form(self, tree):
        lf = LoginForm()
        lf._attach(tree)
        tree.collect_changes()

        lf._on_login({"event.detail.username": "u", "event.detail.password": "p"})
        changes = tree.collect_changes()
        disabled_changes = [c for c in changes if c.get("key") == "disabled"]
        assert any(c["value"] is False for c in disabled_changes)

    def test_sync_property_error(self):
        lf = LoginForm()
        lf._sync_property("error", True)
        assert lf._error is True

    def test_sync_property_disabled(self):
        lf = LoginForm()
        lf._sync_property("disabled", True)
        assert lf._enabled is False


class TestLoginOverlay:

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_tag(self):
        lo = LoginOverlay()
        assert lo._tag == "vaadin-login-overlay"

    def test_create(self):
        lo = LoginOverlay()
        assert lo._opened is False
        assert lo._title == ""
        assert lo._description == ""
        assert lo._error is False
        assert lo._no_forgot_password is False

    def test_open_close(self):
        lo = LoginOverlay()
        lo.open()
        assert lo.is_opened()
        lo.close()
        assert not lo.is_opened()

    def test_open_after_attach(self, tree):
        lo = LoginOverlay()
        lo._attach(tree)
        tree.collect_changes()

        lo.open()
        changes = tree.collect_changes()
        opened_changes = [c for c in changes if c.get("key") == "opened"]
        assert any(c["value"] is True for c in opened_changes)

    def test_close_after_attach(self, tree):
        lo = LoginOverlay()
        lo._attach(tree)
        lo.open()
        tree.collect_changes()

        lo.close()
        changes = tree.collect_changes()
        opened_changes = [c for c in changes if c.get("key") == "opened"]
        assert opened_changes[-1]["value"] is False

    def test_set_title(self):
        lo = LoginOverlay()
        lo.set_title("My App")
        assert lo.get_title() == "My App"

    def test_set_title_after_attach(self, tree):
        lo = LoginOverlay()
        lo._attach(tree)
        tree.collect_changes()

        lo.set_title("My App")
        changes = tree.collect_changes()
        title_changes = [c for c in changes if c.get("key") == "title"]
        assert any(c["value"] == "My App" for c in title_changes)

    def test_set_description(self):
        lo = LoginOverlay()
        lo.set_description("Sign in")
        assert lo.get_description() == "Sign in"

    def test_set_description_after_attach(self, tree):
        lo = LoginOverlay()
        lo._attach(tree)
        tree.collect_changes()

        lo.set_description("Sign in")
        changes = tree.collect_changes()
        desc_changes = [c for c in changes if c.get("key") == "description"]
        assert any(c["value"] == "Sign in" for c in desc_changes)

    def test_set_error(self):
        lo = LoginOverlay()
        lo.set_error(True)
        assert lo.is_error()

    def test_set_error_after_attach(self, tree):
        lo = LoginOverlay()
        lo._attach(tree)
        tree.collect_changes()

        lo.set_error(True)
        changes = tree.collect_changes()
        error_changes = [c for c in changes if c.get("key") == "error"]
        assert any(c["value"] is True for c in error_changes)

    def test_login_event(self, tree):
        lo = LoginOverlay()
        lo._attach(tree)

        events = []
        lo.add_login_listener(lambda e: events.append(e))
        lo._on_login({"event.detail.username": "admin", "event.detail.password": "secret"})
        assert len(events) == 1
        assert events[0]["username"] == "admin"
        assert events[0]["password"] == "secret"

    def test_forgot_password_event(self, tree):
        lo = LoginOverlay()
        lo._attach(tree)

        events = []
        lo.add_forgot_password_listener(lambda e: events.append(e))
        lo._on_forgot_password({})
        assert len(events) == 1

    def test_attach_with_title_description(self, tree):
        lo = LoginOverlay()
        lo.set_title("App")
        lo.set_description("Desc")
        lo._attach(tree)

        changes = tree.collect_changes()
        title_changes = [c for c in changes if c.get("key") == "title"]
        desc_changes = [c for c in changes if c.get("key") == "description"]
        assert any(c["value"] == "App" for c in title_changes)
        assert any(c["value"] == "Desc" for c in desc_changes)

    def test_attach_opened(self, tree):
        lo = LoginOverlay()
        lo.open()
        lo._attach(tree)

        changes = tree.collect_changes()
        opened_changes = [c for c in changes if c.get("key") == "opened"]
        assert any(c["value"] is True for c in opened_changes)

    def test_set_forgot_password_visible(self):
        lo = LoginOverlay()
        lo.set_forgot_password_button_visible(False)
        assert lo._no_forgot_password is True

    def test_set_forgot_password_visible_after_attach(self, tree):
        lo = LoginOverlay()
        lo._attach(tree)
        tree.collect_changes()

        lo.set_forgot_password_button_visible(False)
        changes = tree.collect_changes()
        nfp_changes = [c for c in changes if c.get("key") == "noForgotPassword"]
        assert any(c["value"] is True for c in nfp_changes)

    def test_sync_property_opened(self):
        lo = LoginOverlay()
        lo._sync_property("opened", True)
        assert lo._opened is True

    def test_sync_property_error(self):
        lo = LoginOverlay()
        lo._sync_property("error", True)
        assert lo._error is True

    def test_login_re_enables_overlay(self, tree):
        lo = LoginOverlay()
        lo._attach(tree)
        tree.collect_changes()

        lo._on_login({"event.detail.username": "u", "event.detail.password": "p"})
        changes = tree.collect_changes()
        disabled_changes = [c for c in changes if c.get("key") == "disabled"]
        assert any(c["value"] is False for c in disabled_changes)

    def test_registers_event_listeners(self, tree):
        lo = LoginOverlay()
        lo._attach(tree)
        assert "login" in lo.element._listeners
        assert "forgot-password" in lo.element._listeners
