# PyFlow — Python Implementation of Vaadin Flow

## First Steps

1. Read `STATUS.md` — current implementation status and what's pending
2. Read parent `../CLAUDE.md` — project overview, architecture, specs index
3. For protocol details: `../specs/PROTOCOL.md`, `../specs/RPC.md`, `../specs/PITFALLS.md`
4. For component roadmap: `../specs/COMPONENTS.md`

---

## Git Commits

- **One logical change per commit.** Never mix unrelated changes (e.g. new feature + refactor + bug fix) in a single commit.
- Tests must pass at each commit.
- Commit message: concise, describes the "why" not the "what".

---

## Quick Commands

```bash
# Run the app
source .venv/bin/activate && python -m demo
# http://localhost:8088

# Run tests
pytest tests/ -v

# Run specific test file
pytest tests/test_rpc_events.py -v

# Run Java reference (bundle-generator with AllComponentsView)
cd ../bundle-generator && ./mvnw package jetty:run-war
# http://localhost:8080
```

---

## Project Structure

```
vaadin-pyflow/
├── src/vaadin/flow/
│   ├── core/           # StateTree, StateNode, Element, Component
│   ├── components/     # Button, TextField, Grid, Dialog, etc. (35 components)
│   ├── data/           # Binder, DataProvider, validators, converters
│   ├── server/         # HTTP server (aiohttp), UIDL handler
│   └── app.py          # FlowApp entry point
├── demo/               # Demo app + __main__.py entry point
│   ├── views/          # View files (hello_world, about, components, grid, etc.)
│   └── services/       # PeopleService (data access layer)
├── tests/              # 962 unit tests
└── STATUS.md           # Implementation progress
../bundle-generator/    # Java project → frontend bundle (shared, at root level)
```

---

## Key Source Files

| File | Purpose |
|------|---------|
| `server/uidl_handler.py` | UIDL protocol: init, navigation, events, mSync, publishedEventHandler |
| `server/http_server.py` | aiohttp server, sessions, static files, upload |
| `core/state_tree.py` | Node management, change tracking, execute queue |
| `core/state_node.py` | Features, attach/put/splice, change collection |
| `core/element.py` | Element wrapper: properties, attributes, styles, events |
| `core/component.py` | Base Component class with element attachment |
| `components/grid.py` | Grid: connectors, renderers, sorting, lazy loading (~600 lines) |
| `components/dialog.py` | Dialog: FlowComponentHost, publishedEventHandler close |

---

## Adding New Components

1. Check Java implementation in `../flow-components/`
2. Check complexity/connector info in `../specs/COMPONENTS.md`
3. Get API: `mcp__Vaadin__get_component_java_api`
4. Create `components/new_component.py`
5. Export in `components/__init__.py`
6. Add tests in `tests/`
7. **Keep demos in sync** — Update BOTH:
   - Python: `demo/views/components.py` (`ComponentsDemoView`)
   - Java: `../bundle-generator/src/main/java/com/vaadin/pyflow/AllComponentsView.java`
   These MUST mirror each other. The Java view drives bundle generation — if a web component isn't used there, it won't be in the bundle.
8. Regenerate bundle: `cd ../bundle-generator && ./generate-bundle.sh`

---

## Event Hashes (Java Flow Compatible)

PyFlow uses hardcoded hashes from Java Flow for exact protocol compatibility.
Full hash table in `../specs/PROTOCOL.md`. Most common:

| Event | Hash |
|-------|------|
| click | `F8oCtNArLiI=` |
| change | `Fg73o1qebBo=` |
| keydown | `OSoHnU3SjNg=` |
| opened-changed (Dialog) | `t7mULTj4JVU=` |
| ui-navigate | `msDV4SvCysE=` |

---

## Testing with Playwright

Use MCP Playwright tools to verify UI:
```
browser_navigate → http://localhost:8088 (Python) or :8080 (Java)
browser_snapshot → get element refs
browser_click → interact
browser_take_screenshot → visual check
```

---

## Bundle Location

PyFlow serves the production bundle from:
```
../bundle-generator/target/ → extracted to bundle/
```
Generate with: `cd ../bundle-generator && ./generate-bundle.sh`
