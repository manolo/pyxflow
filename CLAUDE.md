# PyXFlow — Python Implementation of Vaadin Flow

## First Steps

1. Read `STATUS.md` — current implementation status and what's pending
2. Read parent `../migrate-flow-specs/CLAUDE.md` — project overview, architecture, specs index
3. For protocol details: `../migrate-flow-specs/specs/PROTOCOL.md`, `../migrate-flow-specs/specs/RPC.md`, `../migrate-flow-specs/specs/PITFALLS.md`
4. For component roadmap: `../migrate-flow-specs/specs/COMPONENTS.md`

---

## Git Commits

- **One logical change per commit.** Never mix unrelated changes (e.g. new feature + refactor + bug fix) in a single commit.
- Tests must pass at each commit.
- Commit message: concise, describes the "why" not the "what".

---

## Quick Commands

```bash
# Run the app (auto-detects demo/ module)
source .venv/bin/activate && python -m demo
# http://localhost:8088
# Or via CLI: pyxflow demo --port 8088
# Or auto-detect: pyxflow --port 8088  (finds demo/views/ automatically)

# Run unit tests (default — runs tests/unit/)
pytest -v

# Run ALL tests (unit + UI — auto-starts server if needed)
pytest --all -v

# Run specific test file
pytest tests/unit/test_rpc_events.py -v

# Run UI tests only (auto-starts server if none running on :8088)
pytest tests/ui/ -v            # headless
pytest tests/ui/ --headed -v   # visible browser

# Regenerate the frontend bundle (auto-discovers _v_fqcn components)
pyxflow --bundle

# Run Java reference (flow-components)
cd ../migrate-flow-specs/flow-components && ./mvnw package jetty:run-war
# http://localhost:8080
```

---

## Project Structure

```
pyxflow/
├── src/pyxflow/
│   ├── core/           # StateTree, StateNode, Element, Component
│   ├── components/     # Button, TextField, Grid, Dialog, etc. (50+ components)
│   ├── data/           # Binder, DataProvider, validators, converters
│   ├── server/         # HTTP server (aiohttp), UIDL handler
│   ├── main.py         # FlowApp + CLI entry point
│   └── resources/      # setup_app, generate_bundle, scaffold templates
├── demo/               # Demo app + __main__.py entry point
│   ├── views/          # Demo views (9 routes)
│   ├── static/         # Static assets (images, CSS) served at /images/*, /styles/*
│   └── services/       # PeopleService (data access layer)
├── tests/
│   ├── views/          # 29 test views with TestMainLayout (independent app, python -m tests)
│   ├── unit/           # 2457 unit tests (default pytest target)
│   └── ui/             # 446 Playwright UI tests (run explicitly via pytest tests/ui/)
└── STATUS.md           # Implementation progress
../migrate-flow-specs/flow-components/  # Java project → frontend bundle
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
| `core/component.py` | Base Component class with element attachment, _BufferedStyle, deferred execute_js |
| `components/grid.py` | Grid: connectors, renderers, sorting, lazy loading (~600 lines) |
| `components/dialog.py` | Dialog: FlowComponentHost, publishedEventHandler close |

---

## Adding New Components

1. Check Java implementation in `../migrate-flow-specs/flow-components/`
2. Check complexity/connector info in `../migrate-flow-specs/specs/COMPONENTS.md`
3. Get API: `mcp__Vaadin__get_component_java_api`
4. Create `components/new_component.py`
5. Export in `components/__init__.py`
6. Add tests in `tests/`
7. Add `_v_fqcn` class attribute with the Java FQCN (e.g. `_v_fqcn = "com.vaadin.flow.component.button.Button"`)
8. Regenerate bundle: `pyxflow --bundle` (auto-discovers all `_v_fqcn` components)

---

## Event Hashes

PyXFlow computes event hashes dynamically using `compute_event_hash(config)` in `server/uidl_handler.py`. The function uses `base64(sha256(BOM + json.encode('utf-16-be'))[:8])` -- the same algorithm as Java Flow.

All hash constants are computed at module load from their config dicts (e.g. `_CLICK_HASH = compute_event_hash(_CLICK_CONFIG)`). No hardcoded hash strings -- if a config changes, the hash updates automatically.

Hash constants are centralized in `server/uidl_handler.py`. Component files import from there.

---

## Tracking What's Missing

When the user asks "qué falta" / "what's missing" / "what's pending", perform a gap analysis covering:

1. **Unimplemented features** — Check `STATUS.md` § "What's Missing" → "Unimplemented Features" (PWA, Security, etc.)
2. **Missing API methods** — Check `STATUS.API.md` for `[ ]` markers. Count `[x]` vs `[ ]` for coverage %.
3. **Missing tests** — Compare unit test count (`pytest --co -q | tail -1`) and UI test count (`pytest tests/ui/ --co -q | tail -1`) against `STATUS.md`. Check `tests/ui/SPECS.md` for pending UI test scenarios.
4. **LOC** — Run `find src -name '*.py' | xargs wc -l | tail -1` (implementation) and `find tests -name '*.py' | xargs wc -l | tail -1` (tests). Demo code is not counted.

**After ANY implementation work**, update these files:
- `STATUS.md` — Update test counts, LOC, move items from "Missing" to "Implemented", update API coverage ratio
- `STATUS.API.md` — Flip `[ ]` → `[x]` for newly implemented methods, update header counts
- Keep the "What's Missing" section in STATUS.md current — it's the single source of truth for gap analysis

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

The Vaadin frontend bundle (FlowClient, web components, Lumo/Aura themes) is pre-built and shipped inside the wheel at `src/pyxflow/bundle/`. At runtime, the server discovers it automatically.

### Regenerating the bundle (PyXFlow developers)

From the `pyxflow/` checkout:

```bash
pyxflow --bundle                          # build → src/pyxflow/bundle/
pyxflow --bundle --keep                   # keep bundle-project/ for debugging
pyxflow --bundle --vaadin-version 25.1.0  # pin a different Vaadin version
```

The command auto-discovers all `Component` subclasses with `_v_fqcn`, generates a Maven project with `@Uses` for each, builds in production mode, and extracts the bundle from the WAR.

If `bundle-project/` already exists (from a previous `--keep`), it reuses the Maven project and skips `mvn clean` for faster rebuilds.

### Custom bundle for user projects

Users can generate their own bundle to include only the components they use, or to add custom web components:

```bash
# From the project root (where my_app/ lives)
pyxflow my_app --bundle                   # build → my_app/bundle/
pyxflow my_app --bundle --keep            # keep my_app/bundle-project/
```

The generated `my_app/bundle/` takes priority over the package-internal bundle at runtime. This allows projects to:
- Use a different Vaadin version than the one shipped with pyxflow
- Include additional web components (by adding `_v_fqcn` to custom components)
- Reduce bundle size by only including used components (future)

### Bundle discovery priority

`get_bundle_directory()` checks these locations in order:
1. `<app_directory>/bundle/` — user-project bundle (highest priority)
2. `<package>/bundle/` — package-internal (shipped in wheel)
3. `./bundle/` — development fallback
