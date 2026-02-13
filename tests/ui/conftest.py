"""Playwright UI test configuration.

Auto-starts the PyFlow demo server unless a valid one is already running.
"""

import json
import re
import subprocess
import sys
import time
from pathlib import Path

import pytest
import urllib.request
import urllib.error
from playwright.sync_api import expect

CONSECUTIVE_FAILURES = 0
MAX_CONSECUTIVE = 4

DEFAULT_PORT = 8088
DEFAULT_BASE_URL = f"http://localhost:{DEFAULT_PORT}"
HEALTH_URL = f"{DEFAULT_BASE_URL}/?v-r=health"

# Test routes that must be registered for UI tests to work
REQUIRED_ROUTES = {"test/buttons-icons", "test/text-inputs", "test/grid-basic", "test/login"}

# Root of the vaadin-pyflow project
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Sentinel: port is occupied but not a valid PyFlow health response
_PORT_OCCUPIED = object()


def _check_server():
    """Check if a server is running on the default port.

    Returns:
        dict — valid health JSON from a PyFlow server
        _PORT_OCCUPIED — something is listening but not a valid PyFlow health endpoint
        None — nothing is listening (connection refused)
    """
    try:
        resp = urllib.request.urlopen(HEALTH_URL, timeout=2)
        data = json.loads(resp.read())
        if isinstance(data, dict) and data.get("pyflow"):
            return data
        return _PORT_OCCUPIED
    except (json.JSONDecodeError, ValueError):
        # Got a response but not valid JSON → port occupied by something else
        return _PORT_OCCUPIED
    except (urllib.error.URLError, OSError):
        # Connection refused → nothing running
        return None


@pytest.fixture(scope="session")
def base_url(request):
    """Use existing server if valid, otherwise auto-start one."""
    explicit = request.config.getoption("--base-url", default=None)
    if explicit:
        yield explicit
        return

    health = _check_server()

    # Port occupied by something that's not a valid PyFlow server
    if health is _PORT_OCCUPIED:
        pytest.fail(
            f"Port {DEFAULT_PORT} is in use but not responding to PyFlow health check.\n"
            f"Kill it:  lsof -ti :{DEFAULT_PORT} | xargs kill -9\n"
            f"Or use a different port:  pytest tests/ui/ --base-url http://localhost:XXXX"
        )

    # Valid PyFlow server — check routes
    if health is not None:
        registered = set(health.get("routes", []))
        missing = REQUIRED_ROUTES - registered
        if missing:
            pytest.fail(
                f"PyFlow server on port {DEFAULT_PORT} is missing test routes: {missing}\n"
                f"Restart with:  cd vaadin-pyflow && source .venv/bin/activate && python -m demo"
            )
        yield DEFAULT_BASE_URL
        return

    # Nothing running — auto-start the demo server
    proc = subprocess.Popen(
        [sys.executable, "-c",
         "import vaadin.flow.app as _a; "
         f"_a._serve('demo.views', 'localhost', {DEFAULT_PORT}, False, dev=True)"],
        cwd=str(_PROJECT_ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    deadline = time.monotonic() + 15
    ready = False
    while time.monotonic() < deadline:
        health = _check_server()
        if isinstance(health, dict):
            ready = True
            break
        if proc.poll() is not None:
            out = proc.stdout.read().decode() if proc.stdout else ""
            pytest.fail(f"Server exited with code {proc.returncode}:\n{out}")
        time.sleep(0.3)

    if not ready:
        proc.kill()
        out = proc.stdout.read().decode() if proc.stdout else ""
        pytest.fail(f"Server did not start within 15s:\n{out}")

    yield DEFAULT_BASE_URL

    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(timeout=2)


@pytest.fixture(scope="session")
def browser_context_args():
    return {"viewport": {"width": 1280, "height": 720}}


def navigate_to(page, base_url, path, wait_selector, timeout=15000):
    """Navigate to a test view, preferring SideNav click over goto.

    If the SideNav has a link matching the path, click it (SPA navigation).
    Falls back to page.goto() if SPA navigation doesn't complete.
    """
    if path in page.url:
        page.wait_for_selector(wait_selector, timeout=timeout)
        return
    # Try SideNav link first (client-side navigation, faster)
    nav_link = page.locator(f"vaadin-side-nav-item[path='/{path}']")
    if nav_link.count() > 0 and nav_link.is_visible():
        nav_link.click()
        # Verify SPA navigation completed; fall back to goto if blocked (e.g. push WS)
        try:
            expect(page).to_have_url(re.compile(re.escape(path)), timeout=3000)
        except AssertionError:
            page.goto(f"{base_url}/{path}")
    else:
        page.goto(f"{base_url}/{path}")
    page.wait_for_selector(wait_selector, timeout=timeout)


@pytest.fixture(scope="session")
def shared_page(browser, base_url):
    """Single browser page reused across all test modules.

    Tests navigate via SideNav links (SPA) or goto as fallback.
    Each module's view_page fixture uses navigate_to() to reach its view.
    """
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    page = ctx.new_page()
    # Navigate to the first view to bootstrap the SPA
    page.goto(f"{base_url}/test/buttons-icons")
    page.wait_for_selector("vaadin-button", timeout=15000)
    yield page
    ctx.close()


def pytest_runtest_makereport(item, call):
    global CONSECUTIVE_FAILURES
    if call.when == "call":
        if call.excinfo is not None:
            CONSECUTIVE_FAILURES += 1
        else:
            CONSECUTIVE_FAILURES = 0


def pytest_configure(config):
    config.addinivalue_line("markers", "spec(*ids): links test to SPECS.md scenario IDs (e.g. V01.01)")


def pytest_runtest_setup(item):
    if CONSECUTIVE_FAILURES > MAX_CONSECUTIVE:
        pytest.skip(f"ABORT: {CONSECUTIVE_FAILURES} consecutive failures")
