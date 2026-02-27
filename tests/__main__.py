"""Run: python -m tests [--debug]"""

import sys

# Test server always runs in dev mode (needed for UI test detection)
if "--dev" not in sys.argv:
    sys.argv.append("--dev")

from pyflow import FlowApp

FlowApp(port=8088).run()
