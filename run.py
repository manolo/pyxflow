#!/usr/bin/env python
"""Run the Vaadin PyFlow server with HelloWorld example."""

import asyncio
from vaadin.flow.server.http_server import run_server
from examples.hello_world import HelloWorldView

if __name__ == "__main__":
    print("=" * 50)
    print("  PyFlow - Python Vaadin Flow")
    print("=" * 50)
    print()
    print("  Open: http://localhost:8080")
    print("  Stop: Ctrl+C")
    print()
    asyncio.run(run_server(HelloWorldView, host="localhost", port=8080))
