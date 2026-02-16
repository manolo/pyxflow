# Spec: PyFlow — Architecture Pipeline

Documents the PyFlow architecture as a **data flow** (pipeline), for direct comparison with `java-layers.md`. Same structure, same blocks — but showing how Python replaces each Java layer.

---

## The main pipeline (runtime)

A button click traverses this complete chain, round-trip:

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│   ╔═══════════════════════════════════════════════════════════════╗      │
│   ║                     BROWSER  (identical to Java)             ║      │
│   ╠═══════════════════════════════════════════════════════════════╣      │
│   ║                                                               ║      │
│   ║   Web Components  (reused — same as Java)                    ║      │
│   ║   <vaadin-button>, <vaadin-grid>, <vaadin-text-field>...      ║      │
│   ║   49 components · @vaadin/* npm packages                      ║      │
│   ║                         ↕ DOM events / property changes       ║      │
│   ║                                                               ║      │
│   ║   FlowClient.js  (reused — same build as Java)               ║      │
│   ║   UIDL interpreter · DOM tree sync · RPC sender               ║      │
│   ║   Constant pool · syncId/clientId tracking                    ║      │
│   ║                                                               ║      │
│   ╚══════════════════════════╤════════════════════════════════════╝      │
│                              │                                           │
│                    HTTP POST /?v-r=uidl  (same protocol)                 │
│                    Body: {csrfToken, syncId, clientId, rpc: [...]}        │
│                              │                                           │
│   ╔══════════════════════════╧════════════════════════════════════╗      │
│   ║                     SERVER  (Python — asyncio)               ║      │
│   ╠═══════════════════════════════════════════════════════════════╣      │
│   ║                                                               ║      │
│   ║  ┌─────────────────────────────────────────────────────────┐  ║      │
│   ║  │  aiohttp  (replaces Servlet Container)                  │  ║      │
│   ║  │  Receives HTTP, async event loop, native WebSocket      │  ║      │
│   ║  │  1 process, 1 thread, N concurrent connections          │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  http_server.py  (replaces VaadinServlet+VaadinService) │  ║      │
│   ║  │  → GET / → serve index.html (bundle)                    │  ║      │
│   ║  │  → GET /?v-r=init → handle_init()                       │  ║      │
│   ║  │  → POST /?v-r=uidl → handle_uidl()                     │  ║      │
│   ║  │  → GET /VAADIN/* → handle_static() (bundle assets)     │  ║      │
│   ║  │  → POST upload → handle_upload()                        │  ║      │
│   ║  │  → GET /?v-r=push → handle_push() (WebSocket)          │  ║      │
│   ║  │  → POST /?v-r=heartbeat → handle_heartbeat()           │  ║      │
│   ║  │  → GET /{path} → handle_route() (SPA catch-all)        │  ║      │
│   ║  │  → Session management (in-memory dict, JSESSIONID)      │  ║      │
│   ║  │  → CSRF validation                                      │  ║      │
│   ║  │  → _UidlEncoder (bulletproof JSON serialization)        │  ║      │
│   ║  │  → _critical_error_json (meta.appError, syncId=-1)      │  ║      │
│   ║  │  753 lines                                               │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  uidl_handler.py  (replaces UidlRequestHandler          │  ║      │
│   ║  │                    + ServerRpcHandler + all typed        │  ║      │
│   ║  │                    handlers + UidlWriter + ConstantPool)│  ║      │
│   ║  │                                                         │  ║      │
│   ║  │  handle_init() → appConfig + initial UIDL               │  ║      │
│   ║  │  handle_uidl() → validate syncId/clientId → _process_rpc│  ║      │
│   ║  │                                                         │  ║      │
│   ║  │  _process_rpc() — two-pass (mSync first, events after): │  ║      │
│   ║  │    "mSync"     → _handle_msync() (property sync)       │  ║      │
│   ║  │    "event"     → _handle_event() (click, change...)    │  ║      │
│   ║  │    "publishedEventHandler" → _handle_published_event()  │  ║      │
│   ║  │    "channel"   → tree.handle_return_channel()           │  ║      │
│   ║  │                                                         │  ║      │
│   ║  │  _handle_event() dispatches by event type:              │  ║      │
│   ║  │    "ui-navigate" → _handle_navigation()                 │  ║      │
│   ║  │    "click"       → _handle_click()                      │  ║      │
│   ║  │    "change"      → _handle_change()                     │  ║      │
│   ║  │    "keydown"     → _handle_keydown()                    │  ║      │
│   ║  │    others        → element.fire_event()                 │  ║      │
│   ║  │                                                         │  ║      │
│   ║  │  _build_response() → collect changes + execute + deps   │  ║      │
│   ║  │  compute_event_hash() — SHA-256, Java-compatible        │  ║      │
│   ║  │  20+ event hash configs (_CLICK, _CHANGE, _OPENED...)   │  ║      │
│   ║  │  1039 lines                                              │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  StateTree / StateNode / Feature  (core/)               │  ║      │
│   ║  │                                                         │  ║      │
│   ║  │  state_tree.py — 110 lines                               │  ║      │
│   ║  │    Tree of numbered nodes. Same semantics as Java.      │  ║      │
│   ║  │    create_node(), collect_changes(), queue_execute()     │  ║      │
│   ║  │    register_element(), register_component()             │  ║      │
│   ║  │    register_return_channel(), notify_push()             │  ║      │
│   ║  │                                                         │  ║      │
│   ║  │  state_node.py — 121 lines                               │  ║      │
│   ║  │    Feature enum (IDs identical to Java):                │  ║      │
│   ║  │     F0  ElementData (tag, payload)                      │  ║      │
│   ║  │     F1  ElementPropertyMap (value, label, disabled...)  │  ║      │
│   ║  │     F2  ElementChildrenList (splice add/remove)         │  ║      │
│   ║  │     F3  ElementAttributeMap (theme, id, class)          │  ║      │
│   ║  │     F4  ElementListenerMap (click, change, keydown...)  │  ║      │
│   ║  │     F5  PushConfigurationMap                            │  ║      │
│   ║  │     F6  PushConfigurationParametersMap                  │  ║      │
│   ║  │     F7  TextNodeMap                                     │  ║      │
│   ║  │     F12 InlineStylePropertyMap                          │  ║      │
│   ║  │     F19 ClientDelegateHandlers (@ClientCallable)        │  ║      │
│   ║  │     F24 VirtualChildrenList (overlays, dialogs)         │  ║      │
│   ║  │    attach(), put(), get(), remove(), splice             │  ║      │
│   ║  │                                                         │  ║      │
│   ║  │  Java: 39 NodeFeature classes, 11 Change types          │  ║      │
│   ║  │  Python: 1 enum (11 IDs) + 5 change types              │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  Element  (core/element.py — 130 lines)                 │  ║      │
│   ║  │  DOM abstraction over StateNode                         │  ║      │
│   ║  │  .set_property() .set_attribute() .add_child()          │  ║      │
│   ║  │  .get_style() .add_event_listener() .fire_event()       │  ║      │
│   ║  │  .execute_js() → $0 = element in the script             │  ║      │
│   ║  │  + Style class (inline CSS via F12)                     │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  Component  (core/component.py — 750 lines)             │  ║      │
│   ║  │  Base class + mixins:                                   │  ║      │
│   ║  │  HasValue, HasComponents, HasEnabled, HasSize, HasStyle │  ║      │
│   ║  │  HasReadOnly, HasValidation, HasRequired                │  ║      │
│   ║  │  ClickNotifier, FocusNotifier, BlurNotifier             │  ║      │
│   ║  │  HasAriaLabel, KeyNotifier                              │  ║      │
│   ║  │  __init_subclass__ auto-init (no super().__init__())    │  ║      │
│   ║  │  _BufferedStyle, _pending_* deferred patterns           │  ║      │
│   ║  │  @ClientCallable decorator                              │  ║      │
│   ║  │  UI class (singleton per session)                       │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  Vaadin Components  (components/ — 57 files)            │  ║      │
│   ║  │  49 components + constants + mixins + renderer           │  ║      │
│   ║  │  Button, Grid, TextField, Dialog, AppLayout,            │  ║      │
│   ║  │  ComboBox, DatePicker, Upload, MenuBar, TreeGrid...     │  ║      │
│   ║  │  + HTML Components: Div, Span, H1-H6, Anchor, etc.     │  ║      │
│   ║  │  12,447 lines (Grid = 1,433 alone)                      │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  YOUR CODE                                              │  ║      │
│   ║  │  @Route("hello")                                        │  ║      │
│   ║  │  class HelloView(VerticalLayout):                       │  ║      │
│   ║  │      def __init__(self):                                │  ║      │
│   ║  │          button = Button("Click me")                    │  ║      │
│   ║  │          button.add_click_listener(lambda e: ...)       │  ║      │
│   ║  │          self.add(button)                               │  ║      │
│   ║  └─────────────────────────────────────────────────────────┘  ║      │
│   ║                                                               ║      │
│   ╚═══════════════════════════════════════════════════════════════╝      │
│                                                                          │
│   The click listener event modifies components →                        │
│   StateTree collects changes → _build_response() serializes →           │
│   JSON response travels back through the same path →                    │
│   FlowClient applies changes to the DOM → Web Components re-render     │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## The 4 communication pipelines

### Pipeline 1: Button Click (runtime — 95% of traffic)

```
<vaadin-button> DOM click
  → FlowClient.js captures event  (identical to Java)
  → POST /?v-r=uidl  {rpc: [{type:"event", node:5, event:"click"}]}
  → aiohttp event loop (async, single-thread)
  → handle_uidl_post() → handle_uidl()
  → get session from _sessions[JSESSIONID] → get UI by v-uiId
  → Validate CSRF token
  → handler.handle_uidl(payload) → validate syncId/clientId
  → _process_rpc() — Pass 1: mSync, Pass 2: events
  → _handle_event() → _handle_click(node_id)
  → tree.get_element(node_id) → element.fire_event("click")
  → Component._fire_click_event() → YOUR LISTENER
  → Your code modifies UI (label.set_text(), add(), ...)
  → _build_response() → tree.collect_changes() + collect_execute()
  → Constants dedup (_sent_constants tracking)
  → JSON response with for(;;); wrapper → HTTP 200
  → FlowClient applies changes to the DOM
  → Web Components re-render
```

### Pipeline 2: Bootstrap (initial load — once per tab)

```
GET /hello
  → aiohttp route: handle_route() → "no extension" → index.html
  → get_index_html():
      Reads bundle/index.html
      + Injects <base href="/">
      + Injects overflow:hidden
      + Injects featureFlags (MasterDetailLayout)
      + Injects .v-system-error CSS
      + Applies @ColorScheme (theme attr + color-scheme style)
  → HTML response → HTTP 200
  → Browser loads bundle → FlowClient initializes

GET /?v-r=init
  → handle_init()
  → get_or_create_session() → new JSESSIONID if none exists
  → Allocate new UI (tree + handler) per tab
  → handler.handle_init(browser_details, route, ui_id)
  → _create_initial_nodes() (body + push params + container)
  → _handle_navigation() → Router.match_route()
  → View constructor runs → components are created
  → tree.collect_changes() → initial UIDL
  → @AppShell @StyleSheet → EAGER dependencies
  → @Push → pushScript: "VAADIN/static/push/vaadinPush.js"
  → Response: {appConfig: {uidl: {syncId:0, changes:[...]}}}
  → Set-Cookie: JSESSIONID
  → FlowClient applies initialUIDL → DOM tree → render
```

### Pipeline 3: Push (server → client — WebSocket)

```
Background task:
  → UI.access(callback)
  → callback modifies UI (label.set_text("Updated!"))
  → tree.notify_push() → _push_event.set()
  → _push_sender() coroutine wakes up
  → Guard: tree._changes not empty? (avoids syncId desync)
  → handler._build_response() with changes
  → Injects meta: {"async": true} (avoids endRequest error)
  → JSON with for(;;); wrapper
  → Atmosphere length-prefix: <len>|<message>
  → WebSocket.send_str()
  → FlowClient receives → applies changes → DOM update

Prior handshake (once):
  → GET /?v-r=push (WebSocket upgrade)
  → handle_push() → validate session, UI, pushId
  → aiohttp WebSocketResponse
  → Atmosphere handshake: <len>|<UUID>|30000|X
  → Loop: waits for messages (heartbeat "X" only)
```

### Pipeline 4: SPA Navigation (client-side routing)

```
Click on <a router-link> or history.pushState
  → FlowClient intercepts (no full page reload)
  → POST /?v-r=uidl  {rpc: [{type:"event", event:"ui-navigate",
                               data:{route:"/about"}}]}
  → _handle_event() → "ui-navigate" → _handle_navigation()
  → Router.match_route(route) → (view_class, title, params, layout)
  → before_leave() guard on current view (can cancel)
  → Layout mode:
      same layout → reuse, swap content only
      different layout → remove old, create new + view
      no layout → direct view in container
  → View constructor runs → _attach(tree) → components in StateTree
  → _collect_stylesheets() → EAGER deps for view CSS
  → after_navigation() callback
  → serverConnected execute (FlowClient navigation state machine)
  → _build_response() → changes (detach old + attach new)
  → FlowClient applies: remove old DOM + create new
```

---

## Support systems (outside the main pipeline)

### Build time (before running)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Bundle Generator  (bundle_generator.py — 393 lines)               │
│  ─────────────────────────────────────────                          │
│  vaadin --bundle                                                    │
│                                                                     │
│  1. Component Discovery                                             │
│     Scans all Component subclasses with _v_fqcn                    │
│     → generates AllComponentsView.java with @Uses(...)             │
│     (Replaces Java's Annotation Scanner — 93 classes → 1 function) │
│                                                                     │
│  2. Maven Build (delegated)                                         │
│     Generates pom.xml + AllComponentsView.java                     │
│     Runs: mvn package -Pproduction                                  │
│     Maven internally invokes: Node/npm install + Vite build        │
│     Output: target/*.war → extracts bundle/ from META-INF/VAADIN/  │
│                                                                     │
│  3. Bundle Extraction                                               │
│     Decompresses WAR → copies VAADIN/, index.html, lumo/, aura/    │
│     Result: src/vaadin/flow/bundle/ (ships in wheel)                │
│                                                                     │
│  Java: 93 classes (scanner) + Node/npm installer + Import Generator │
│        + Vite build + Theme compiler = an entire subsystem          │
│  Python: 1 file, delegates to Maven, extracts the result            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Dev time (development only)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Dev Mode  (app.py — FlowApp._run_dev())                           │
│  ─────────────────────────────────────                              │
│  No Vite, no HMR, no DevServer, no ViteWebsocketProxy              │
│                                                                     │
│  Mechanism:                                                         │
│  1. Parent process: creates socket, watchfiles monitors .py         │
│  2. Change detected → kills child → re-spawns child                 │
│  3. Child inherits socket (fd inheritance — no EADDRINUSE)          │
│  4. Clients reconnect automatically (Atmosphere reconnect)          │
│                                                                     │
│  ~100 lines vs Java's ~15 classes (ViteHandler, etc.)               │
│  Bundle already pre-built → no need for Vite or Node in dev        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Session Management

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Sessions  (http_server.py — ~50 lines)                            │
│  ─────────────────────────────────────                              │
│  _sessions: dict[str, dict]   ← in-memory                          │
│  JSESSIONID cookie (httponly)                                       │
│  SESSION_TIMEOUT = 1800s (30 min, same as Java)                    │
│  Periodic cleanup: _session_cleanup_ctx (every 60s)                │
│                                                                     │
│  Session = {                                                        │
│      csrf_token, last_activity, next_ui_id,                         │
│      uis: { ui_id: {tree, handler, push_ws, push_sender_task} }    │
│  }                                                                  │
│                                                                     │
│  UI = 1 StateTree + 1 UidlHandler per browser tab                  │
│  No ReentrantLock (single-thread async, no contention)             │
│                                                                     │
│  Java: VaadinSession + VaadinService + WrappedHttpSession +        │
│        SessionRouteRegistry + ErrorHandler + ~20 classes            │
│  Python: dict + 2 functions                                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Router / Navigation

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Router  (router.py — 397 lines)                                   │
│  ──────────────────────────────                                     │
│  @Route("path") → register in _routes dict                         │
│  @RouteAlias("alt-path") → alias routes                            │
│  @PageTitle("title") → static page title                           │
│  @StyleSheet("url") → CSS dependencies                             │
│  @AppShell → global config class                                   │
│  @Push → enable WebSocket push                                     │
│  @ColorScheme("dark") → initial theme                              │
│                                                                     │
│  match_route(path) → (view_class, title, params, layout)           │
│  Static routes first, then parameterized (:param, :param?)         │
│  discover_views(package) → import all modules → trigger @Route     │
│                                                                     │
│  Layout support:                                                    │
│  - RouterLayout interface (show/remove_router_layout_content)      │
│  - Same layout class → reuse instance, swap content                │
│  - before_leave() guard, after_navigation() callback               │
│  - HasDynamicTitle via get_page_title()                             │
│                                                                     │
│  Java: 93 classes (Router, RouteRegistry, RouteResolver,           │
│        NavigationStateRenderer, BeforeLeave/Enter/AfterEvent...)   │
│  Python: 1 file, 397 lines                                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Data Binding

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  data/  (5 files, 836 lines)                                       │
│  ───────────────────────────────                                    │
│                                                                     │
│  Binder  (binder.py — 380 lines)                                   │
│  → for_field(field).with_converter(...).with_validator(...).bind()  │
│  → set_bean(bean) / write_bean(bean) / read_bean(bean)             │
│  → Binding, BindingBuilder                                         │
│  → is_valid(), is_dirty(), clear()                                 │
│                                                                     │
│  DataProvider  (provider.py — 191 lines)                           │
│  → from_callback(fetch, count) — lazy loading                      │
│  → CallbackDataProvider                                             │
│  → Flat only (no HierarchicalDataProvider — TreeGrid uses flat DFS)│
│                                                                     │
│  Validators  (validator.py — 89 lines)                             │
│  → StringLengthValidator, RegexpValidator, RangeValidator           │
│  → EmailValidator, custom validator functions                       │
│                                                                     │
│  Converters  (converter.py — 51 lines)                             │
│  → StringToIntegerConverter, StringToFloatConverter                 │
│                                                                     │
│  Result  (result.py — 78 lines)                                    │
│  → Result.ok(value), Result.error(message)                         │
│                                                                     │
│  Java: 155 classes (flow-data/), DataCommunicator, DataKeyMapper,  │
│        HierarchicalDataProvider, Bean validation (JSR-303),        │
│        SelectionModel (Single, Multi, None)                         │
│  Python: 5 files, 836 lines                                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Theme System

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Themes  (spread across several files, ~50 lines total)            │
│  ──────                                                             │
│  2 themes: Lumo (default) and Aura (modern)                         │
│  Each one: light + dark variant                                     │
│                                                                     │
│  Loading:                                                           │
│  1. Bundle includes both themes (pre-built)                         │
│  2. get_index_html() applies @ColorScheme to <html>                │
│  3. UI.set_theme(theme, variant) → execute_js() at runtime        │
│     Removes ALL theme <link>s + adds new one                       │
│  4. @ColorScheme("dark") → <html theme="dark"                     │
│                              style="color-scheme: dark">           │
│                                                                     │
│  Java: ThemeRegistry + CssBundler + BootstrapHandler injection     │
│  Python: decorators + string replacement in index.html              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Error Handling

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  3 layers of error handling                                         │
│  ────────────────────────                                           │
│                                                                     │
│  Layer 1: _process_rpc() — per each RPC                            │
│  try/except → Notification with error message (LUMO_ERROR theme)   │
│  Does not break the flow — the user sees a red toast               │
│                                                                     │
│  Layer 2: _UidlEncoder — JSON serialization                        │
│  str() fallback for unknown types                                   │
│  json.dumps() can NEVER fail → no blank pages from TypeError       │
│                                                                     │
│  Layer 3: handle_uidl() outer try/except — safety net              │
│  _critical_error_json() → meta.appError with syncId: -1            │
│  FlowClient shows .v-system-error overlay (top-right, z-10000)    │
│  Click/ESC → refresh page                                          │
│                                                                     │
│  Java: DefaultErrorHandler, HasErrorParameter<T>, VaadinService    │
│  Python: 3 nested try/except with escalating severity              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Other systems

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Push / WebSocket  (http_server.py — ~130 lines)                   │
│  Native aiohttp WebSocket (no Atmosphere framework)                │
│  Emulated Atmosphere handshake format: <len>|<UUID>|30000|X        │
│  alwaysXhrToServer: RPCs via HTTP, pushes via WS                   │
│  _push_sender() coroutine per UI                                   │
│  Java: Atmosphere framework (8+ classes + external jar)             │
│  Python: inline in http_server.py, ~130 lines                      │
│                                                                     │
│  Security                                                           │
│  CSRF token per session (secrets.token_hex)                         │
│  Validated on every UIDL request                                    │
│  No @RolesAllowed, @AnonymousAllowed (not implemented)             │
│  Java: 15 classes in server/auth/                                  │
│  Python: 5 lines of validation                                     │
│                                                                     │
│  CSS / @StyleSheet                                                  │
│  @StyleSheet("url") on @AppShell → EAGER deps in init              │
│  @StyleSheet("url") on views → EAGER deps on navigation            │
│  Static files from <app>/static/ directory                          │
│  Java: CssImportHandler, AbstractAnnotationValidator, etc.          │
│  Python: decorator + list append                                    │
│                                                                     │
│  CLI  (app.py — 299 lines)                                         │
│  vaadin [module] [--dev] [--debug] [--port N] [--host H]           │
│  vaadin [module] --bundle [--keep] [--vaadin-version V]            │
│  Auto-detect app module (finds <pkg>/views/)                       │
│  Dev mode with watchfiles + fd inheritance                          │
│  Java: Spring Boot auto-configuration, 64 classes                  │
│  Python: 1 file, manual argparse                                   │
│                                                                     │
│  NOT implemented (not needed for current scope):                    │
│  - i18n (I18NProvider)                                              │
│  - PWA (service worker, manifest)                                   │
│  - DnD (drag and drop)                                              │
│  - Lit Templates (server bindings)                                  │
│  - Hotswap (Python reloads natively with --dev)                    │
│  - Spring Boot (Python doesn't use Spring)                          │
│  - Bean Validation (JSR-303)                                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Final counts

```
MAIN PIPELINE (runtime):
  aiohttp               — external (pip install aiohttp)
  http_server.py         — 753 lines (Servlet+Service+Handlers)
  uidl_handler.py        — 1,039 lines (UIDL+RPC+ConstantPool)
  state_tree.py          — 110 lines
  state_node.py          — 121 lines
  element.py             — 130 lines
  component.py           — 750 lines (Component + mixins + UI)
  components/ (57 files) — 12,447 lines (49 components)

SUPPORT SYSTEMS:
  Data Binding (5 files) — 836 lines
  Router (1 file)        — 397 lines
  CLI / App (1 file)     — 299 lines
  Bundle Generator       — 393 lines
  Menu                   — 121 lines

CLIENT (reused — identical to Java):
  FlowClient.js          — GWT-compiled (~200KB)
  Web Components         — 49 @vaadin/* npm packages
  Lumo/Aura themes       — CSS variables

─────────────────────────────────────────────
TOTAL PYTHON:  77 files · 17,457 LOC
TOTAL JAVA:    3,081 classes · 451,000 LOC
RATIO:         26:1 in LOC · 40:1 in files
─────────────────────────────────────────────
```

---

## Simplified view for the slide

```
┌──────────────────────┐
│    WEB COMPONENTS    │  ← reused (same bundle)
├──────────────────────┤
│    FLOWCLIENT.JS     │  ← reused (same bundle)
├──────────────────────┤
│  HTTP / WebSocket    │
├──────────────────────┤
│  aiohttp             │  ← replaces Servlet Container
├──────────────────────┤
│  http_server.py      │  ← replaces VaadinServlet + VaadinService
│  (753L)              │     + Request Handlers + Session + CSRF
├──────────────────────┤
│  uidl_handler.py     │  ← replaces UidlRequestHandler
│  (1,039L)            │     + ServerRpcHandler + UidlWriter
│                      │     + ConstantPool + all typed handlers
├──────────────────────┤
│  StateTree + Node    │  ← same semantics, 231 lines
│  (231L)              │     (vs 103 Java classes)
├──────────────────────┤
│  Element             │  ← same API, 130 lines
│  (130L)              │     (vs 37 Java classes)
├──────────────────────┤
│  Component + Mixins  │  ← same API, 750 lines
│  (750L)              │     (vs 141 Java classes)
├──────────────────────┤
│  49 Components       │  ← same API, 12,447 lines
│  (12,447L)           │     (vs 977 Java classes)
├──────────────────────┤
│  Data Binding        │  ← Binder + DataProvider, 836 lines
│  (836L)              │     (vs 155 Java classes)
├──────────────────────┤
│  Router              │  ← @Route + match + discover, 397 lines
│  (397L)              │     (vs 93 Java classes)
├──────────────────────┤
│  YOUR CODE           │  ← @Route views, same API
└──────────────────────┘
         +
   ┌───────────────┐  ┌───────────────┐
   │  CLI / App    │  │ BUNDLE GEN    │
   │  --dev, --dbg │  │ vaadin --bndl │
   │  299L         │  │ 393L          │
   └───────────────┘  └───────────────┘
         +
   ┌───────────────┐  ┌───────────────┐
   │  PUSH         │  │  THEMES       │
   │  aiohttp WS   │  │  Lumo / Aura  │
   │  ~130L inline │  │  ~50L         │
   └───────────────┘  └───────────────┘
```

---

## Direct comparison: Java vs Python by layer

| Layer | Java | Python | Ratio |
|-------|------|--------|-------|
| Servlet/HTTP Server | Tomcat/Jetty + VaadinServlet + VaadinService (~331 cls) | aiohttp + http_server.py (753L) | ~100:1 |
| Request Handlers + RPC | UidlRequestHandler + ServerRpcHandler + 6 typed handlers (~65 cls) | uidl_handler.py (1,039L) | ~15:1 |
| StateTree + Features | 103 classes, 39 NodeFeature types, 11 Change types | state_tree.py + state_node.py (231L) | ~100:1 |
| Element/DOM API | 37 classes | element.py (130L) | ~70:1 |
| Component Model | 141 classes (Component + 30+ mixins) | component.py (750L) | ~45:1 |
| Vaadin Components | 977 classes (49 modules in flow-components/) | components/ (12,447L, 57 files) | ~20:1 |
| Data Binding | 155 classes (flow-data/) | data/ (836L, 5 files) | ~45:1 |
| Router | 93 classes | router.py (397L) | ~55:1 |
| Build Tools | 93 classes + Node installer + Vite build | bundle_generator.py (393L) + Maven | ~55:1 |
| Spring Boot | 64 classes (vaadin-spring/) | — (not needed) | ∞ |
| Dev Server | ~15 classes (ViteHandler, HMR proxy) | ~100L in app.py (watchfiles) | ~35:1 |
| Push | 8+ classes + Atmosphere framework | ~130L inline in http_server.py | ~15:1 |
| **TOTAL** | **3,081 classes · 451,000 LOC** | **77 files · 17,457 LOC** | **26:1** |
