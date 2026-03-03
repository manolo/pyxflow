"""Pytest configuration and fixtures for PyXFlow tests."""

import pytest

# Import views to register routes via @Route decorator
# This needs to happen before any tests run
from demo.views.hello_view import HelloWorldView  # noqa: F401
from demo.views.about_view import AboutView  # noqa: F401
from pyxflow.router import clear_routes


@pytest.fixture(autouse=True)
def reset_routes():
    """Reset route registry before each test to ensure isolation."""
    # Clear routes before test
    clear_routes()
    # Re-import to re-register routes
    # Route entry format: (view_class, page_title, param_names, compiled_regex, layout_class)
    from pyxflow.router import _routes
    from demo.views.hello_view import HelloWorldView
    from demo.views.about_view import AboutView
    from demo.views.main_layout import MainLayout
    _routes[""] = (HelloWorldView, "Hello World", [], None, MainLayout)
    _routes["about"] = (AboutView, "About", [], None, MainLayout)
    yield
    # Clean up after test (optional)
