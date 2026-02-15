"""Playwright UI test configuration.

Auto-starts the PyFlow test server unless a valid one is already running.
"""

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

# Root of the vaadin-pyflow project
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# The views module that the test server must be running
_EXPECTED_VIEWS = "tests.views"


def _check_server():
    """Check if a server is running on the default port.

    Returns:
        True — a PyFlow test server is responding (correct views module)
        str — a PyFlow server with wrong views module (e.g. "demo.views")
        False — something is listening but not a PyFlow dev server
        None — nothing is listening (connection refused)
    """
    try:
        resp = urllib.request.urlopen(f"{DEFAULT_BASE_URL}/", timeout=2)
        html = resp.read().decode("utf-8", errors="replace")
        # In dev mode, PyFlow injects <meta name="pyflow-views" content="...">
        m = re.search(r'<meta\s+name="pyflow-views"\s+content="([^"]+)"', html)
        if m:
            return True if m.group(1) == _EXPECTED_VIEWS else m.group(1)
        # No meta tag — either not PyFlow, or PyFlow in production mode
        return False
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

    status = _check_server()

    # Wrong PyFlow app (e.g. demo instead of tests)
    if isinstance(status, str):
        pytest.fail(
            f"Port {DEFAULT_PORT} is running '{status}' but UI tests need '{_EXPECTED_VIEWS}'.\n"
            f"Stop it and run:  cd vaadin-pyflow && python -m tests"
        )

    # Port occupied by something that's not a PyFlow dev server
    if status is False:
        pytest.fail(
            f"Port {DEFAULT_PORT} is in use but not a PyFlow dev server.\n"
            f"Kill it:  lsof -ti :{DEFAULT_PORT} | xargs kill -9\n"
            f"Or use a different port:  pytest tests/ui/ --base-url http://localhost:XXXX"
        )

    # Valid PyFlow test server already running
    if status is True:
        yield DEFAULT_BASE_URL
        return

    # Nothing running — auto-start the test server
    proc = subprocess.Popen(
        [sys.executable, "-c",
         "import vaadin.flow.app as _a; "
         f"_a._serve('tests.views', 'localhost', {DEFAULT_PORT}, False, dev=True)"],
        cwd=str(_PROJECT_ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    deadline = time.monotonic() + 15
    ready = False
    while time.monotonic() < deadline:
        if _check_server() is True:
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
