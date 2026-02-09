"""Run: python -m demo"""

import asyncio
from vaadin.flow.router import discover_views
from vaadin.flow.server.http_server import run_server

if __name__ == "__main__":
    discover_views("demo.views")
    asyncio.run(run_server(host="localhost", port=8088))
