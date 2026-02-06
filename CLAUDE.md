# PyFlow - Claude Code Instructions

## First Steps

**ALWAYS read these files first:**
1. `STATUS.md` - Current implementation status and what's missing
2. Parent `../CLAUDE.md` - Development workflow, UIDL protocol details
3. Parent `../SPECS.md` - Protocol specifications

## Project Overview

PyFlow is a Python implementation of Vaadin Flow. It reuses Vaadin's frontend (web components + FlowClient.js) and implements the server-side in Python.

## Quick Commands

```bash
# Run the app
source .venv/bin/activate
python run.py
# Open http://localhost:8080

# Run tests
pytest tests/ -v

# Run specific test file
pytest tests/test_rpc_events.py -v
```

## Project Structure

```
vaadin-pyflow/
├── src/vaadin/flow/
│   ├── core/           # StateTree, StateNode, Element, Component
│   ├── components/     # Button, TextField, Span, layouts, Dialog, etc.
│   ├── server/         # HTTP server, UIDL handler
│   └── examples/       # HelloWorldView, AboutView, DialogDemoView
├── tests/              # 220 tests
├── run.py              # Entry point
└── STATUS.md           # Implementation checklist
```

## Key Files

| File | Purpose |
|------|---------|
| `server/uidl_handler.py` | UIDL protocol, RPC handling |
| `server/http_server.py` | aiohttp server, sessions |
| `core/state_tree.py` | Node management, changes |
| `core/component.py` | Base Component class |
| `core/element.py` | Element wrapper for nodes |

## Adding New Components

1. Check Java implementation in `../flow-components/`
2. Get API with `mcp__Vaadin__get_component_java_api`
3. Create `components/new_component.py`
4. Export in `components/__init__.py`
5. Add tests in `tests/`
6. **IMPORTANT: Keep demos in sync** — Update BOTH:
   - Python: `src/vaadin/flow/examples/components_demo.py` (`ComponentsDemoView`)
   - Java: `bundle-generator/src/main/java/com/vaadin/pyflow/AllComponentsView.java`
   These two files MUST mirror each other (same structure, same components). The Java view drives the bundle generation — if a web component isn't used there, it won't be in the bundle.
7. Regenerate the bundle: `cd bundle-generator && ./generate-bundle.sh`

## UIDL Protocol Summary

**Client → Server:**
```json
{"csrfToken": "...", "rpc": [{"type": "event", "node": 3, "event": "click"}], "syncId": 0, "clientId": 0}
```

**Server → Client:**
```json
{"syncId": 1, "clientId": 1, "changes": [...], "constants": {...}}
```

## Event Hashes (Java Flow Compatible)

PyFlow uses hardcoded hashes from Java Flow for exact protocol compatibility:

| Event | Hash | Usage |
|-------|------|-------|
| click | `F8oCtNArLiI=` | Button clicks |
| change | `Fg73o1qebBo=` | TextField value sync |
| keydown | `OSoHnU3SjNg=` | Enter key handling |
| ui-navigate | `msDV4SvCysE=` | Navigation events |
| ui-leave-navigation | `i2nDWhpwLZE=` | Leave navigation |
| ui-refresh | `18ACma10cDE=` | Page refresh |

See `../SPECS.md` for hash generation details.

## Feature IDs (for UIDL changes)

| ID | Feature | Usage |
|----|---------|-------|
| 0 | ElementData | tag |
| 1 | ElementPropertyMap | value, label |
| 2 | ElementChildrenList | splice children |
| 3 | ElementAttributeMap | theme |
| 4 | ElementListenerMap | click, change |
| 7 | TextNode | text content |
| 12 | InlineStylePropertyMap | align-self |

## Testing with Playwright

Use MCP Playwright tools to verify UI:
```
mcp__playwright__browser_navigate → http://localhost:8080
mcp__playwright__browser_snapshot → get element refs
mcp__playwright__browser_click → click elements
mcp__playwright__browser_take_screenshot → visual verification
```

## Bundle Location

PyFlow uses the production bundle from my-hello:
```
../my-hello/target/classes/META-INF/VAADIN/webapp/VAADIN/build/
```
