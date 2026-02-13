"""Playwright UI test configuration.

Requires a running PyFlow server: cd vaadin-pyflow && source .venv/bin/activate && python -m demo
"""

import pytest

CONSECUTIVE_FAILURES = 0
MAX_CONSECUTIVE = 4

DEFAULT_BASE_URL = "http://localhost:8088"


@pytest.fixture(scope="session")
def base_url(request):
    """Default to localhost:8088 if --base-url is not provided."""
    return request.config.getoption("--base-url", default=None) or DEFAULT_BASE_URL


@pytest.fixture(scope="session")
def browser_context_args():
    return {"viewport": {"width": 1280, "height": 720}}


def pytest_runtest_makereport(item, call):
    global CONSECUTIVE_FAILURES
    if call.when == "call":
        if call.excinfo is not None:
            CONSECUTIVE_FAILURES += 1
        else:
            CONSECUTIVE_FAILURES = 0


def pytest_runtest_setup(item):
    if CONSECUTIVE_FAILURES > MAX_CONSECUTIVE:
        pytest.skip(f"ABORT: {CONSECUTIVE_FAILURES} consecutive failures")
