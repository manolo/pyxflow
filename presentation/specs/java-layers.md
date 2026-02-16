# Spec: Vaadin Flow Java — Architecture Pipeline

Documents the complete architecture of Vaadin Flow in Java as a **data flow** (pipeline), not as a flat list of layers. Shows where each request travels and all the supporting systems around it.

---

## The main pipeline (runtime)

A button click traverses this entire chain, round trip:

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│   ╔═══════════════════════════════════════════════════════════════╗      │
│   ║                     BROWSER                                   ║      │
│   ╠═══════════════════════════════════════════════════════════════╣      │
│   ║                                                               ║      │
│   ║   Web Components                                              ║      │
│   ║   <vaadin-button>, <vaadin-grid>, <vaadin-text-field>...      ║      │
│   ║   Shadow DOM · Lit-based · Accessible · Themeable             ║      │
│   ║   49 components · @vaadin/* npm packages                      ║      │
│   ║                         ↕ DOM events / property changes       ║      │
│   ║                                                               ║      │
│   ║   FlowClient.js                                               ║      │
│   ║   UIDL interpreter · DOM tree sync · RPC sender               ║      │
│   ║   Constant pool · syncId/clientId tracking                    ║      │
│   ║   GWT-compiled (minified, ~200KB)                             ║      │
│   ║                                                               ║      │
│   ╚══════════════════════════╤════════════════════════════════════╝      │
│                              │                                           │
│                    HTTP POST /?v-r=uidl                                   │
│                    Content-Type: application/json                         │
│                    Body: {csrfToken, syncId, clientId, rpc: [...]}        │
│                              │                                           │
│   ╔══════════════════════════╧════════════════════════════════════╗      │
│   ║                     SERVER                                    ║      │
│   ╠═══════════════════════════════════════════════════════════════╣      │
│   ║                                                               ║      │
│   ║  ┌─────────────────────────────────────────────────────────┐  ║      │
│   ║  │  Servlet Container  (Tomcat / Jetty / Undertow)         │  ║      │
│   ║  │  Receives HTTP, manages threads, TLS                    │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  VaadinServlet                                          │  ║      │
│   ║  │  → Static files? → StaticFileServer                     │  ║      │
│   ║  │  → Otherwise → VaadinService.handleRequest()            │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  VaadinService                                          │  ║      │
│   ║  │  → Find/create VaadinSession                            │  ║      │
│   ║  │  → Acquire session lock                                 │  ║      │
│   ║  │  → Dispatch to Request Handler chain                    │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  Request Handlers  (chain, first match wins)            │  ║      │
│   ║  │                                                         │  ║      │
│   ║  │  /?v-r=init       → BootstrapHandler (index.html)       │  ║      │
│   ║  │  /?v-r=uidl       → UidlRequestHandler  ← THIS ONE     │  ║      │
│   ║  │  /?v-r=heartbeat  → HeartbeatHandler                   │  ║      │
│   ║  │  /?v-r=push       → PushRequestHandler (WS handshake)  │  ║      │
│   ║  │  /?v-r=upload     → StreamReceiverHandler               │  ║      │
│   ║  │  /?v-r=dl         → StreamRequestHandler (download)     │  ║      │
│   ║  │  /sw.js           → PwaHandler (service worker)         │  ║      │
│   ║  │  /favicon.ico     → FaviconHandler                      │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │ (UidlRequestHandler)            ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  ServerRpcHandler                                       │  ║      │
│   ║  │  Parses JSON → validates CSRF → checks syncId           │  ║      │
│   ║  │  Dispatches each RPC to typed handler:                  │  ║      │
│   ║  │                                                         │  ║      │
│   ║  │  "mSync"      → MapSyncRpcHandler (property sync)      │  ║      │
│   ║  │  "event"      → EventRpcHandler (click, change...)     │  ║      │
│   ║  │  "navigation"  → NavigationRpcHandler (route change)   │  ║      │
│   ║  │  "publishedEventHandler" → ClientCallableHandler       │  ║      │
│   ║  │  "attachExistingElement" → AttachExistingElementHandler │  ║      │
│   ║  │  "returnChannel" → ReturnChannelHandler                │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  StateTree / StateNode / Features                       │  ║      │
│   ║  │                                                         │  ║      │
│   ║  │  The heart of the system. A tree of numbered nodes.     │  ║      │
│   ║  │  Each node has Features (numbered maps):                │  ║      │
│   ║  │   F0  ElementData (tag, payload)                        │  ║      │
│   ║  │   F1  ElementPropertyMap (value, label, disabled...)    │  ║      │
│   ║  │   F2  ElementChildrenList (splice add/remove)           │  ║      │
│   ║  │   F3  ElementAttributeMap (theme, id, class)            │  ║      │
│   ║  │   F4  ElementListenerMap (click, change, keydown...)    │  ║      │
│   ║  │   F7  TextNodeMap (text content)                        │  ║      │
│   ║  │   F12 ElementStylePropertyMap (CSS inline)              │  ║      │
│   ║  │   F19 ClientDelegateHandlers (@ClientCallable)          │  ║      │
│   ║  │   F24 VirtualChildrenList (overlays, dialogs)           │  ║      │
│   ║  │   + F5,F6,F8-F11,F13-F18,F20-F23,F25 (15 more)        │  ║      │
│   ║  │                                                         │  ║      │
│   ║  │  39 NodeFeature classes · 11 Change types               │  ║      │
│   ║  │  ConstantPool (hash dedup) · CurrentInstance (TLS)      │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  Element API                                            │  ║      │
│   ║  │  DOM abstraction over StateNode                         │  ║      │
│   ║  │  .setProperty() .setAttribute() .appendChild()          │  ║      │
│   ║  │  .getStyle() .getClassList() .addEventListener()        │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  Component Model                                        │  ║      │
│   ║  │  Base class Component + 30+ mixins:                     │  ║      │
│   ║  │  HasValue, HasComponents, HasEnabled, HasSize, HasStyle │  ║      │
│   ║  │  ClickNotifier, FocusNotifier, BlurNotifier             │  ║      │
│   ║  │  AbstractField, Composite, KeyNotifier                  │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  Vaadin Components  (49 modules, 977 classes)           │  ║      │
│   ║  │  Button, Grid, TextField, Dialog, AppLayout,            │  ║      │
│   ║  │  ComboBox, DatePicker, Upload, MenuBar, TreeGrid...     │  ║      │
│   ║  │  + HTML Components (48 cls): Div, Span, H1-H6, Anchor  │  ║      │
│   ║  └──────────────────────────┬──────────────────────────────┘  ║      │
│   ║                             │                                 ║      │
│   ║  ┌──────────────────────────┴──────────────────────────────┐  ║      │
│   ║  │  YOUR CODE                                              │  ║      │
│   ║  │  @Route("hello") class HelloView extends VerticalLayout │  ║      │
│   ║  │  button.addClickListener(e -> { ... })                  │  ║      │
│   ║  │  binder.setBean(person)                                 │  ║      │
│   ║  │  grid.setDataProvider(callback)                         │  ║      │
│   ║  └─────────────────────────────────────────────────────────┘  ║      │
│   ║                                                               ║      │
│   ╚═══════════════════════════════════════════════════════════════╝      │
│                                                                          │
│   The click listener event modifies components →                        │
│   StateTree collects changes → UidlWriter serializes →                  │
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
  → FlowClient.js captures event
  → POST /?v-r=uidl  {rpc: [{type:"event", node:5, event:"click"}]}
  → Servlet Container (thread pool)
  → VaadinServlet.service()
  → VaadinService.handleRequest() → find session → lock
  → UidlRequestHandler.synchronizedHandleRequest()
  → ServerRpcHandler.handleRpc() → validate CSRF, check syncId
  → EventRpcHandler → StateNode(5) → Feature 4 (listeners)
  → Component.fireEvent(ClickEvent) → YOUR LISTENER
  → Your code modifies UI (label.setText, add(), navigate...)
  → StateTree.collectChanges() → [MapPutChange, ListAddChange...]
  → UidlWriter.createUidl() → {syncId: N, changes: [...]}
  → JSON response → HTTP 200
  → FlowClient applies changes to the DOM
  → Web Components re-render
```

### Pipeline 2: Bootstrap (initial load — once per tab)

```
GET /hello
  → Servlet Container
  → VaadinServlet → not static → VaadinService
  → BootstrapHandler / IndexHtmlRequestHandler
  → Router.resolveNavigationTarget("/hello") → HelloView.class
  → UI.init() → Router.navigate() → new HelloView() → constructor runs
  → StateTree collects all initial changes
  → Generates index.html:
      <base href="/">
      <link> theme CSS (Lumo/Aura)
      <script> FlowClient.js (bundle)
      <script> window.Vaadin = {appConfig: {...}, initialUIDL: {syncId:0, changes:[...]}}
  → HTML response → HTTP 200
  → Browser parses HTML → loads bundle → FlowClient initializes
  → Applies initialUIDL → creates DOM tree → Web Components render
```

### Pipeline 3: Push (server → client — WebSocket)

```
Background thread:
  → UI.access(() -> { label.setText("Updated!"); })
  → VaadinSession.access() → acquire lock → run callback → release lock
  → AtmospherePushConnection.push()
  → UidlWriter.createUidl(async=true)
  → JSON with meta: {async: true}
  → Atmosphere framework → WebSocket.send()
  → FlowClient receives push → applies changes → DOM update

Previous handshake (once):
  → GET /?v-r=push  Transport=websocket
  → PushRequestHandler → Atmosphere → WebSocket upgrade
  → Response: <length>|<UUID>|<heartbeat_ms>|<padding>
```

### Pipeline 4: SPA Navigation (client-side routing)

```
Click on <a router-link> or history.pushState
  → FlowClient intercepts (no full page reload)
  → POST /?v-r=uidl  {rpc: [{type:"navigation", location:"/about"}]}
  → ServerRpcHandler → NavigationRpcHandler
  → Router.navigate(UI, Location("/about"))
  → BeforeLeaveEvent → old view
  → BeforeEnterEvent → new view
  → Detach old view nodes from StateTree
  → new AboutView() → attach to StateTree
  → AfterNavigationEvent
  → UidlWriter collects changes (detach old + attach new)
  → JSON response with both sets of changes
  → FlowClient applies: remove old DOM nodes + create new ones
```

---

## Supporting systems (outside the main pipeline)

### Build time (before running)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Bundle Creator / Build Tools                                       │
│  ─────────────────────────────                                      │
│  flow-plugins/ (Maven plugin + Gradle plugin)                       │
│                                                                     │
│  1. Annotation Scanner                                              │
│     Scans classpath looking for @Route, @NpmPackage, @JsModule,     │
│     @CssImport, @Theme, @Uses → generates dependency list           │
│     93 classes in server/frontend/ + scanner/                       │
│                                                                     │
│  2. Node/npm Installer                                              │
│     FrontendTools, NodeInstaller — downloads Node.js if not present │
│     Runs npm install of @vaadin/* packages                          │
│                                                                     │
│  3. Import Generator                                                │
│     GenerateMainImports → generates generated/vaadin.ts with        │
│     imports of all detected web components                          │
│                                                                     │
│  4. Vite Build (production)                                         │
│     TaskPrepareProdBundle → TaskRunDevBundleBuild                   │
│     Runs: vite build → generates optimized JS/CSS bundle            │
│     Output: META-INF/VAADIN/build/ (stats.json + chunks)           │
│                                                                     │
│  5. Theme Compiler                                                  │
│     CssBundler → extracts CSS from Lumo/Aura themes                │
│     Generates: themes/<name>/styles.css                             │
│                                                                     │
│  PyFlow: vaadin --bundle (1 command, uses Maven internally)         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Dev time (development only)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Dev Server (vaadin-dev-server/)                                    │
│  ────────────────────────────────                                   │
│  ViteHandler — launches Vite process (node vite --port 5173)        │
│  ViteWebsocketProxy — proxies HMR WebSocket (Hot Module Replace)    │
│  DevBundleBuildingHandler — rebuilds on-the-fly                     │
│  DevToolsInterface — IDE ↔ server communication                     │
│  BrowserLiveReload — automatic reload                               │
│                                                                     │
│  Flow:                                                              │
│  GET /VAADIN/@vite/client → proxy → Vite :5173                     │
│  GET /VAADIN/generated/* → proxy → Vite :5173                      │
│  WebSocket HMR → proxy → Vite :5173                                │
│                                                                     │
│  PyFlow: no DevServer (bundle pre-built, Vite not needed)           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Session Management

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  VaadinSession (per user)                                           │
│  ──────────────────────────                                         │
│  → Contains N UI instances (1 per tab/window)                       │
│  → Lock (ReentrantLock) — serializes concurrent access              │
│  → ErrorHandler — exception handling                                │
│  → SessionRouteRegistry — per-session routes                        │
│  → WrappedHttpSession — wrapper over container's HttpSession        │
│                                                                     │
│  UI (per browser tab)                                               │
│  ──────────────────────────                                         │
│  → StateTree — the node tree                                        │
│  → Router — route resolution                                        │
│  → Page — JS access, History, viewport                              │
│  → UIInternals — syncId, clientId, pending JS, dependencies         │
│  → PushConnection — WebSocket reference (if push enabled)           │
│                                                                     │
│  PyFlow: session.py (~100 lines), UI in uidl_handler.py             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Router / Navigation

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Router (93 classes)                                                │
│  ──────────────────                                                 │
│  RouteRegistry — URL → view class map                               │
│  RouteResolver — resolves Location → NavigationTarget               │
│  NavigationStateRenderer — instantiates view, attaches to UI        │
│  RouterLayout — interface for layouts (views inside layouts)         │
│                                                                     │
│  Lifecycle events (in order):                                       │
│  1. BeforeLeaveEvent → old view (can cancel)                        │
│  2. BeforeEnterEvent → new view (can redirect)                      │
│  3. Instantiate view → constructor runs                             │
│  4. AfterNavigationEvent → both views                               │
│                                                                     │
│  HasUrlParameter<T> — typed parameters: /user/:id                   │
│  @RouteAlias — alternative routes                                   │
│  @ParentLayout — defines layout hierarchy                           │
│                                                                     │
│  PyFlow: router.py (~200 lines, no lifecycle events)                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Data Binding

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  flow-data/ (155 classes)                                           │
│  ───────────────────────                                            │
│                                                                     │
│  Binder<T>                                                          │
│  → forField(field).withConverter(...).withValidator(...).bind(prop)  │
│  → setBean(bean) / writeBean(bean) / readBean(bean)                 │
│  → Binding, BindingBuilder, StatusHandler                           │
│                                                                     │
│  DataProvider<T, F>                                                  │
│  → fromCallbacks(fetch, count) — lazy loading                       │
│  → DataCommunicator — manages visible window (offset/limit)         │
│  → DataKeyMapper — maps items to IDs for the client                 │
│  → HierarchicalDataProvider — for TreeGrid                          │
│                                                                     │
│  Validators: Email, Range, StringLength, Regexp, Bean (JSR-303)     │
│  Converters: StringToInteger, StringToDouble, LocalDateToDate...    │
│  SelectionModel: Single, Multi, None                                │
│                                                                     │
│  PyFlow: data/binder.py + data_provider.py + validators.py (~700L)  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Theme System

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Themes                                                             │
│  ──────                                                             │
│  2 themes: Lumo (default) and Aura (modern)                         │
│  Each one: light + dark variant                                     │
│                                                                     │
│  Loading:                                                           │
│  1. @Theme annotation on @AppShell                                  │
│  2. BootstrapHandler injects <link> in index.html                   │
│  3. CSS variables: --lumo-* / --aura-* / --vaadin-*                 │
│  4. Components import their own styles via Shadow DOM                │
│                                                                     │
│  Lumo dark: <html theme="dark">                                     │
│  Aura dark: <html style="color-scheme: dark">                       │
│                                                                     │
│  PyFlow: @ColorScheme decorator, UI.set_theme() (~50 lines)         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Spring Boot Integration

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  vaadin-spring/ (64 classes) — OPTIONAL                             │
│  ────────────────────────────────────                               │
│  VaadinServletConfiguration — auto-register servlet                 │
│  SpringInstantiator — creates views via ApplicationContext (@Autowired)│
│  @VaadinSessionScope, @UIScope — DI scopes                         │
│  SpringSecurityAutoConfiguration — integrates with Spring Security  │
│  @PermitAll, @RolesAllowed, @AnonymousAllowed — on views            │
│  DevModeBrowserLauncher — opens browser on startup                  │
│                                                                     │
│  PyFlow: does not have this layer (Python does not use Spring)      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Other systems

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Push / Atmosphere (8+ classes + external framework)                │
│  Bidirectional WebSocket, long-polling fallback                     │
│  PyFlow: push_handler.py (~200L, native aiohttp WebSocket)         │
│                                                                     │
│  Security (15 classes in server/auth/)                              │
│  CSRF tokens, @AnonymousAllowed, route access control               │
│  PyFlow: CSRF in uidl_handler.py                                    │
│                                                                     │
│  i18n (7 classes)                                                   │
│  I18NProvider — component translation                               │
│  PyFlow: not implemented                                            │
│                                                                     │
│  PWA (PwaHandler, PwaRegistry, PwaConfiguration)                    │
│  Service worker, manifest.json, offline support                     │
│  PyFlow: not implemented                                            │
│                                                                     │
│  DnD — Drag and Drop (8 classes in flow-dnd/)                      │
│  DragSource, DropTarget, DragEndEvent, DropEvent                    │
│  PyFlow: not implemented                                            │
│                                                                     │
│  Streaming (25 classes in server/streams/)                          │
│  Upload (StreamReceiverHandler) + Download (StreamResourceHandler)  │
│  PyFlow: upload in http_server.py                                   │
│                                                                     │
│  Error Handling                                                     │
│  DefaultErrorHandler → VaadinSession.getErrorHandler()              │
│  HasErrorParameter<T> — typed error views                           │
│  PyFlow: 3 layers (RPC → Encoder → Critical, see MEMORY.md)        │
│                                                                     │
│  Heartbeat (HeartbeatHandler)                                       │
│  GET /?v-r=heartbeat every 5 min — keeps session alive              │
│  PyFlow: not implemented (sessions do not expire)                   │
│                                                                     │
│  Lit Templates (flow-lit-template/, 8 classes)                      │
│  Server-side bindings for Lit templates                             │
│  PyFlow: not implemented                                            │
│                                                                     │
│  Hotswap (9 classes in server/hotswap/)                             │
│  Hot-reloads classes during development (JRebel, DCEVM)             │
│  PyFlow: not needed (Python reloads natively)                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Final counts

```
MAIN PIPELINE (runtime):
  Servlet Container        — external (Tomcat/Jetty)
  VaadinServlet/Service    — 331 classes (server/)
  Request Handlers         — 50 classes (server/communication/)
  ServerRpcHandler + RPCs  — 15 classes (communication/rpc/)
  StateTree + Features     — 103 classes (internal/)
  Element/DOM API          — 37 classes
  Component Model          — 141 classes
  Vaadin Components        — 977 classes (flow-components/)
  HTML Components          — 48 classes

SUPPORTING SYSTEMS:
  Data Binding             — 155 classes (flow-data/)
  Router                   — 93 classes
  Spring Integration       — 64 classes (vaadin-spring/)
  Frontend/Build Tools     — 93 classes (server/frontend/)
  Dev Server               — ~15 classes (vaadin-dev-server/)
  Push/Atmosphere          — 8+ classes + framework
  Auth/Security            — 15 classes
  i18n, PWA, DnD, etc.    — ~30 classes
  Hotswap, Templates       — ~17 classes

CLIENT (reused):
  FlowClient.js            — GWT-compiled (~200KB)
  Web Components           — 49 @vaadin/* npm packages
  Lumo/Aura themes         — CSS variables

─────────────────────────────────────────────
TOTAL JAVA:    3,081 classes · 451,000 LOC · 25 years
TOTAL PYFLOW:  ~70 files · 17,000 LOC · 6 weeks
RATIO:         26:1 in LOC
─────────────────────────────────────────────
```

---

## Simplified view for the slide

For a presentation slide, the pipeline can be condensed into blocks:

```
┌──────────────────────┐
│    WEB COMPONENTS    │  ← 49 @vaadin/* packages
├──────────────────────┤
│    FLOWCLIENT.JS     │  ← UIDL interpreter, RPC sender
├──────────────────────┤
│  HTTP / WebSocket    │
├──────────────────────┤
│  SERVLET CONTAINER   │  ← Tomcat / Jetty
├──────────────────────┤
│  VAADIN SERVICE      │  ← Session, Auth, Config, Static files
├──────────────────────┤
│  REQUEST HANDLERS    │  ← UIDL, Bootstrap, Push, Upload, Heartbeat
├──────────────────────┤
│  RPC DISPATCHER      │  ← mSync, Event, Navigation, ClientCallable
├──────────────────────┤
│  STATE TREE          │  ← Nodes, Features, Changes, ConstantPool
├──────────────────────┤
│  ELEMENT API         │  ← Properties, Attributes, Styles, Events
├──────────────────────┤
│  COMPONENT MODEL     │  ← Component, Mixins, Lifecycle
├──────────────────────┤
│  VAADIN COMPONENTS   │  ← Button, Grid, TextField... (49 modules)
├──────────────────────┤
│  DATA BINDING        │  ← Binder, DataProvider, Validators
├──────────────────────┤
│  ROUTER              │  ← @Route, Navigation lifecycle
├──────────────────────┤
│  YOUR CODE           │  ← @Route views, services
└──────────────────────┘
         +
   ┌───────────────┐  ┌───────────────┐  ┌───────────────┐
   │ SPRING BOOT   │  │  DEV SERVER   │  │ BUNDLE TOOLS  │
   │ DI, Security  │  │  Vite, HMR    │  │ Scanner, npm  │
   └───────────────┘  └───────────────┘  └───────────────┘
         +
   ┌───────────────┐  ┌───────────────┐  ┌───────────────┐
   │  PUSH         │  │  THEMES       │  │  i18n / PWA   │
   │  Atmosphere   │  │  Lumo / Aura  │  │  DnD / etc    │
   └───────────────┘  └───────────────┘  └───────────────┘
```
