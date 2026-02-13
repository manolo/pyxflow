"""Playwright UI test configuration.

Auto-starts the PyFlow demo server unless a valid one is already running.
"""

import json
import subprocess
import sys
import time
from pathlib import Path

import pytest
import urllib.request
import urllib.error

CONSECUTIVE_FAILURES = 0
MAX_CONSECUTIVE = 4

DEFAULT_PORT = 8088
DEFAULT_BASE_URL = f"http://localhost:{DEFAULT_PORT}"
HEALTH_URL = f"{DEFAULT_BASE_URL}/?v-r=health"

# Test routes that must be registered for UI tests to work
REQUIRED_ROUTES = {"test/buttons-icons", "test/text-inputs"}

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
