#!/usr/bin/env python
"""Run the Vaadin PyFlow server with example views."""

import asyncio
from vaadin.flow.server.http_server import run_server

# Import views to register them via @Route decorator
from examples import HelloWorldView, AboutView, DialogDemoView, ComponentsDemoView  # noqa: F401

if __name__ == "__main__":
    print("=" * 50)
    print("  PyFlow - Python Vaadin Flow")
    print("=" * 50)
    print()
    print("  Routes:")
    print("    http://localhost:8080/            -> HelloWorldView")
    print("    http://localhost:8080/about       -> AboutView")
    print("    http://localhost:8080/dialog-demo -> DialogDemoView")
    print("    http://localhost:8080/components  -> ComponentsDemoView")
    print()
    print("  Stop: Ctrl+C")
    print()
    asyncio.run(run_server(host="localhost", port=8080))
