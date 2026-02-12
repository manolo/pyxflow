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

# Regenerate the frontend bundle (auto-discovers _v_fqcn components)
vaadin --bundle

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
│   ├── components/     # Button, TextField, Grid, Dialog, etc. (49 components)
│   ├── data/           # Binder, DataProvider, validators, converters
│   ├── server/         # HTTP server (aiohttp), UIDL handler
│   └── app.py          # FlowApp entry point
├── demo/               # Demo app + __main__.py entry point
│   ├── views/          # View files (hello_world, about, components, grid, etc.)
│   └── services/       # PeopleService (data access layer)
├── tests/              # 1591 unit tests
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
| `core/component.py` | Base Component class with element attachment, deferred execute_js |
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
7. Add `_v_fqcn` class attribute with the Java FQCN (e.g. `_v_fqcn = "com.vaadin.flow.component.button.Button"`)
8. Regenerate bundle: `vaadin --bundle` (auto-discovers all `_v_fqcn` components)

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

## Bundle

The Vaadin frontend bundle (FlowClient, web components, Lumo/Aura themes) is pre-built and shipped inside the wheel at `src/vaadin/flow/bundle/`. At runtime, the server discovers it automatically.

### Regenerating the bundle (PyFlow developers)

From the `vaadin-pyflow/` checkout:

```bash
vaadin --bundle                          # build → src/vaadin/flow/bundle/
vaadin --bundle --keep                   # keep bundle-project/ for debugging
vaadin --bundle --vaadin-version 25.1.0  # pin a different Vaadin version
```

The command auto-discovers all `Component` subclasses with `_v_fqcn`, generates a Maven project with `@Uses` for each, builds in production mode, and extracts the bundle from the WAR.

If `bundle-project/` already exists (from a previous `--keep`), it reuses the Maven project and skips `mvn clean` for faster rebuilds.

### Custom bundle for user projects

Users can generate their own bundle to include only the components they use, or to add custom web components:

```bash
# From the project root (where my_app/ lives)
vaadin my_app --bundle                   # build → my_app/bundle/
vaadin my_app --bundle --keep            # keep my_app/bundle-project/
```

The generated `my_app/bundle/` takes priority over the package-internal bundle at runtime. This allows projects to:
- Use a different Vaadin version than the one shipped with pyflow
- Include additional web components (by adding `_v_fqcn` to custom components)
- Reduce bundle size by only including used components (future)

### Bundle discovery priority

`get_bundle_directory()` checks these locations in order:
1. `<app_directory>/bundle/` — user-project bundle (highest priority)
2. `<package>/bundle/` — package-internal (shipped in wheel)
3. `./bundle/` — development fallback
