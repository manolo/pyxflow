"""Pytest configuration and fixtures for PyFlow tests."""

import pytest

# Import views to register routes via @Route decorator
# This needs to happen before any tests run
from examples import HelloWorldView, AboutView  # noqa: F401
from vaadin.flow.router import clear_routes


@pytest.fixture(autouse=True)
def reset_routes():
    """Reset route registry before each test to ensure isolation."""
    # Clear routes before test
    clear_routes()
    # Re-import to re-register routes
    # The imports at module level already registered them, so we need to re-register
    from vaadin.flow.router import _routes
    from examples.hello_world import HelloWorldView
    from examples.about import AboutView
    _routes[""] = (HelloWorldView, "Hello World")
    _routes["about"] = (AboutView, "About")
    yield
    # Clean up after test (optional)
