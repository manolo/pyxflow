# Development

## Setup

```bash
git clone https://github.com/manolo/pyflow.git
cd pyflow
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
playwright install chromium
```

This installs everything needed for development: the project in editable mode, unit tests (pytest), UI tests (Playwright), and slide PDF export (Pillow, pyyaml).

## Run the demo

```bash
python -m demo                # http://localhost:8088
python -m demo --dev          # hot-reload on file changes
python -m demo --debug        # verbose protocol logging
```

## Tests

```bash
# Unit tests (default)
pytest

# All tests -- unit + UI (auto-starts server if needed)
pytest --all

# Specific test file
pytest tests/unit/test_rpc_events.py -v
```

UI integration tests (Playwright is installed with `.[dev]`):

```bash
# Run UI tests only (auto-starts the server if needed)
pytest tests/ui/

# With visible browser
pytest tests/ui/ --headed
```

UI tests are in `tests/ui/` and excluded from the default `pytest` run. Use `pytest --all` to run everything in one go. They use a shared browser session with SPA navigation across 29 test views in `tests/views/`, each backed by a `TestMainLayout` with a menu sidebar. The test server auto-starts via `python -m tests`.

<img src="docs/screenshots/screenshots-tests.gif" alt="UI Tests" width="650">

## Frontend bundle

PyFlow ships with a pre-built Vaadin frontend bundle at `src/pyflow/bundle/`. This is the **optimized** version (code-split into lazy-loaded chunks) so the browser only downloads what it needs.

In normal development you **do not need** to run `pyflow bundle` -- the committed bundle is ready to use.

You must regenerate and commit the bundle when:
- Upgrading the Vaadin version in `pyproject.toml` (`vaadin-version` / `flow-version`)
- Adding a new component with `_v_fqcn` (only needed with `--build`, the pre-built JAR already includes all components)

```bash
# Regenerate from Maven Central JARs (fast, seconds)
pyflow bundle --optimized

# Verify it works
python -m demo  # check http://localhost:8088

# Commit the updated bundle
git add src/pyflow/bundle/
git commit -m "Update frontend bundle to Vaadin X.Y.Z"
```

See `BUNDLE.md` for details on optimized vs unoptimized variants and `--build` mode.

## Project structure

```
src/pyflow/
├── core/           # StateTree, StateNode, Element, Component
├── components/     # 49 Vaadin components
├── data/           # Binder, DataProvider, validators, converters
└── server/         # HTTP server (aiohttp), UIDL protocol handler

demo/
├── views/          # Demo views (7 routes)
└── __main__.py     # python -m demo

tests/
├── views/          # 29 test views with TestMainLayout (independent app)
├── unit/           # Unit tests (default pytest target)
├── ui/             # Playwright integration tests (run explicitly)
└── __main__.py     # python -m tests (test server on :8088)
```

## Architecture

```
Browser                          Server (Python)
┌──────────────────┐             ┌──────────────────────┐
│ Vaadin Web       │   HTTP/WS   │ StateTree            │
│ Components       │<----------->│ Components (Python)  │
│ FlowClient.js    │   (UIDL)    │ UIDL Handler         │
└──────────────────┘             └──────────────────────┘
```

The browser runs the standard Vaadin frontend (web components + FlowClient.js). The Python server maintains a state tree and communicates changes via the UIDL protocol over HTTP, with optional WebSocket for push.
