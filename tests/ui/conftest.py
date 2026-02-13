"""Playwright UI test configuration.

Auto-starts the PyFlow demo server unless --base-url is provided.
"""

import subprocess
import sys
import time
from pathlib import Path

import pytest
import urllib.request

CONSECUTIVE_FAILURES = 0
MAX_CONSECUTIVE = 4

DEFAULT_PORT = 18088
DEFAULT_BASE_URL = f"http://localhost:{DEFAULT_PORT}"

# Root of the vaadin-pyflow project
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


@pytest.fixture(scope="session")
def base_url(request):
    """Start demo server automatically, or use --base-url if provided."""
    explicit = request.config.getoption("--base-url", default=None)
    if explicit:
        yield explicit
        return

    # Start the demo server in a subprocess
    proc = subprocess.Popen(
        [sys.executable, "-c",
         f"from vaadin.flow import FlowApp; "
         f"FlowApp.__init__.__wrapped__ = None; "  # skip auto-detect
         f"import vaadin.flow.app as _a; "
         f"_a._serve('demo.views', 'localhost', {DEFAULT_PORT}, False)"],
        cwd=str(_PROJECT_ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    # Wait for server to be ready
    url = f"{DEFAULT_BASE_URL}/"
    deadline = time.monotonic() + 15
    ready = False
    while time.monotonic() < deadline:
        try:
            urllib.request.urlopen(url, timeout=1)
            ready = True
            break
        except Exception:
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
