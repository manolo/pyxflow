# Spec: Vaadin Platform — Subsystems outside Flow

Source: [`vaadin/platform` versions.json](https://github.com/vaadin/platform/blob/main/versions.json)

The Vaadin platform is not just Flow + Web Components. The `versions.json` records **all** artifacts that are coordinated in each release. This document catalogs the subsystems that are **outside** the `flow/` repo and the core web components.

---

## Structure of versions.json

```
versions.json
├── "core"       → open source web components + server integrations
├── "vaadin"     → commercial components and tools (pro)
├── "kits"       → value-added kits (mostly commercial)
├── "react"      → React wrappers for core and pro
└── "platform"   → coordinated version (e.g. "25.1.0-alpha8")
```

---

## 1. Server integrations (core)

Alternatives to Spring Boot for the server. Each one provides a `VaadinServlet` adapted to the framework.

| Subsystem | Version | What it does | License | Repo |
|-----------|---------|--------------|---------|------|
| **flow** | 25.1.0-alpha8 | Core Flow: StateTree, UIDL, Element, Component model, Router, Build tools, Dev server | Apache 2.0 | [vaadin/flow](https://github.com/vaadin/flow) |
| **flow-components** | {{version}} | Java wrappers for the 49 core web components (Button, Grid, etc.) | Apache 2.0 | [vaadin/flow-components](https://github.com/vaadin/flow-components) |
| **vaadin-spring** | (inside flow) | Spring Boot integration: auto-config servlet, DI scopes, Spring Security | Apache 2.0 | Inside flow repo |
| **flow-cdi** | 16.0.0 | Jakarta CDI integration: `@RouteScoped`, `@NormalRouteScoped`, auto-deploy `CdiVaadinServlet`. For Jakarta EE servers (WildFly, Payara, Liberty) | Apache 2.0 | [vaadin/cdi](https://github.com/vaadin/cdi) |
| **vaadin-quarkus** | 3.1.0-alpha1 | Quarkus extension: runs Vaadin Flow on Quarkus (Kubernetes-native Java). CDI-based DI, custom `QuarkusVaadinServletService` | Apache 2.0 | [vaadin/quarkus](https://github.com/vaadin/quarkus) |

### Hilla (alternative framework)

| Subsystem | Version | What it does | License | Repo |
|-----------|---------|--------------|---------|------|
| **hilla** | 25.1.0-alpha8 | Full-stack React/Lit + Spring Boot framework. `@BrowserCallable` generates TypeScript types automatically. Does not use UIDL — the UI is 100% client-side, the server exposes typed endpoints | Apache 2.0 | [vaadin/hilla](https://github.com/vaadin/hilla) |

> **Hilla vs Flow**: Flow maintains state on the server (thin client). Hilla maintains state on the client (thick client, REST endpoints).

### MPR (Multi-Platform Runtime)

| Subsystem | Version | What it does | License | Repo |
|-----------|---------|--------------|---------|------|
| **mpr-v7** | 8.0.1 | Runs Vaadin 7 apps/components inside Flow. Incremental view-by-view migration | Commercial | [vaadin/multiplatform-runtime](https://github.com/vaadin/multiplatform-runtime) |
| **mpr-v8** | 8.0.1 | Same but for Vaadin 8. `MprServlet` routes requests to the correct framework | Commercial | idem |

---

## 2. Commercial components (vaadin)

Pro web components. Require a Vaadin subscription. Same architecture as core (Lit, shadow DOM) but in separate repos.

| Component | npm package | What it does |
|-----------|-------------|--------------|
| **Board** | `@vaadin/board` | Responsive dashboard-style layout. Rows that reflow based on viewport (4 cols → 1 col) |
| **Charts** | `@vaadin/charts` | Interactive charts: line, bar, pie, area, scatter, gauge, OHLC, heatmap, waterfall... Vector graphics + animations |
| **CRUD** | `@vaadin/crud` | High-level component: Grid + form for creating/reading/editing/deleting entities |
| **Dashboard** | `@vaadin/dashboard` | Configurable layout: widgets with drag-and-drop, resize, auto-arrange. The end user can reorganize |
| **Grid Pro** | `@vaadin/grid-pro` | Grid with inline editing. Click on cell → editable (text/checkbox/select). Full keyboard navigation |
| **Map** | `@vaadin/map` | Interactive geographic map. OpenStreetMap, XYZ tiles, WMS, vectors, markers, polygons |
| **Rich Text Editor** | `@vaadin/rich-text-editor` | WYSIWYG editor: bold, italic, headings, lists, blockquotes, code, links, images. Values in HTML or Quill Delta |

Additionally:
| Tool | What it does |
|------|--------------|
| **Spreadsheet** | Excel component in the browser (.xlsx). Formulas, formatting, charts, multiple sheets. Based on Apache POI |
| **Designer** | Visual WYSIWYG IDE plugin (IntelliJ/Eclipse) for designing UIs. **Discontinued** — replaced by Copilot |
| **TestBench** | Vaadin app testing: (1) UI unit tests without a browser (server-side), (2) E2E tests with Selenium + high-level APIs for Vaadin components |

---

## 3. Kits (value-added)

Packages that solve specific production/enterprise problems. Mostly commercial.

| Kit | Version | What it does | License |
|-----|---------|--------------|---------|
| **Copilot** | 25.1.0-alpha4 | In-browser tool in dev mode. Inspect/edit UI visually, AI prompts to modify views, IDE + Java hotswap integration | Commercial (basic inspection free) |
| **Collaboration Engine** | 7.0.0 | Real-time collaborative features: `CollaborationBinder` (shared form editing), `CollaborationAvatarGroup` (presence), `CollaborationMessageList` (chat). Minimal code | Apache 2.0 (since v24.5) |
| **Kubernetes Kit** | 3.0.1 | Deploy on K8s with session replication (Hazelcast/Redis). Rolling updates without losing sessions, HA, horizontal scaling | Commercial |
| **SSO Kit** | 4.0.0 | Single Sign-On via OpenID Connect. Supports Keycloak, Okta, Azure AD. RP-Initiated Logout + Back-Channel Logout. Based on Spring Security | Commercial |
| **AppSec Kit** | 4.0.0 | Scans SBOM (dependencies) against NVD + GitHub Security Advisories. UI in Dev Tools to analyze and annotate vulnerabilities | Commercial |
| **Observability Kit** | 4.0.0 | Java agent based on OpenTelemetry. Collects traces, metrics and logs from frontend and backend. Integrates with Grafana, Datadog, etc. | Commercial |
| **Swing Kit** | 3.0.0 | Renders Vaadin views inside Java Swing desktop apps. Bidirectional Swing ↔ Vaadin communication. Incremental modernization of legacy Swing | Commercial |
| **Azure Kit** | 1.0.0 | Terraform templates for Azure deployment (AKS). Builds on Kubernetes Kit + Azure-specific automation | Commercial |

---

## 4. React wrappers (react)

| Package | npm | What it does |
|---------|-----|--------------|
| **react-components** | `@vaadin/react-components` | React wrappers for the 49 core components |
| **react-components-pro** | `@vaadin/react-components-pro` | React wrappers for Board, Charts, CRUD, Dashboard, Grid Pro, Map, Rich Text Editor |

> These are for use with Hilla (React frontend). Flow uses the Lit web components directly.

---

## 5. Internal utilities (core)

| Subsystem | What it does |
|-----------|--------------|
| **vaadin-lumo-theme** / **vaadin-aura-theme** | Java wrappers for injecting themes into Flow |
| **vaadin-router** | Client-side router (JS, `@vaadin/router`). Used by Hilla, not by Flow |
| **vaadin-usage-statistics** | Anonymous usage telemetry in dev mode |
| **vaadin-development-mode-detector** | Detects whether the app runs in dev mode |
| **vaadin-license-checker** | Validates commercial licenses in dev mode. Shows prompt in browser if license is missing |
| **vaadin-feature-pack** | Modernization Toolkit: classes that reproduce V7/V8/Swing/AWT features in Flow. Used by the Dragonfly transpiler |
| **vaadin-core** | npm meta-package that bundles all @vaadin/* core |

---

## Visual map: the entire ecosystem

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          VAADIN PLATFORM 25                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── FRONTEND (Browser) ──────────────────────────────────────────────┐   │
│  │                                                                      │   │
│  │  Web Components Core (49)     Web Components Pro (7)                 │   │
│  │  @vaadin/button, grid, ...    @vaadin/board, charts, crud, ...       │   │
│  │  Apache 2.0                   Commercial                             │   │
│  │                                                                      │   │
│  │  React Wrappers               FlowClient.js                         │   │
│  │  @vaadin/react-components     UIDL interpreter (GWT-compiled)        │   │
│  │  @vaadin/react-components-pro                                        │   │
│  │                                                                      │   │
│  │  Vaadin Router (client-side)  Lumo / Aura themes                    │   │
│  │  Usage Statistics             License Checker                        │   │
│  │  Dev Mode Detector                                                   │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─── FRAMEWORKS (Server) ─────────────────────────────────────────────┐   │
│  │                                                                      │   │
│  │  ┌─ Flow (server-side) ──┐  ┌─ Hilla (client-side) ──┐             │   │
│  │  │ StateTree + UIDL      │  │ @BrowserCallable        │             │   │
│  │  │ Server-side state     │  │ Auto TypeScript gen      │             │   │
│  │  │ Thin client           │  │ React/Lit frontend       │             │   │
│  │  │ flow-components (49)  │  │ Thick client             │             │   │
│  │  └───────────────────────┘  └──────────────────────────┘             │   │
│  │                                                                      │   │
│  │  Server integrations:                                                │   │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐       │   │
│  │  │ Spring Boot│ │ CDI        │ │ Quarkus    │ │ Servlet    │       │   │
│  │  │ (built-in) │ │ flow-cdi   │ │ vaadin-    │ │ (raw)      │       │   │
│  │  │ Apache 2.0 │ │ Apache 2.0 │ │ quarkus    │ │            │       │   │
│  │  └────────────┘ └────────────┘ │ Apache 2.0 │ └────────────┘       │   │
│  │                                └────────────┘                        │   │
│  │  Legacy migration:                                                   │   │
│  │  ┌────────────────┐ ┌─────────────────┐                             │   │
│  │  │ MPR v7/v8      │ │ Feature Pack    │                             │   │
│  │  │ Run V7/V8 in   │ │ V7/V8/Swing →   │                             │   │
│  │  │ Flow (bridge)  │ │ Flow (transpile)│                             │   │
│  │  │ Commercial     │ │ Commercial      │                             │   │
│  │  └────────────────┘ └─────────────────┘                             │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─── KITS (Production / Enterprise) ──────────────────────────────────┐   │
│  │                                                                      │   │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                │   │
│  │  │ Kubernetes   │ │ SSO Kit      │ │ Observability│                │   │
│  │  │ Kit          │ │ OIDC auth    │ │ Kit          │                │   │
│  │  │ Session HA   │ │ Keycloak,    │ │ OpenTelemetry│                │   │
│  │  │ Hazelcast/   │ │ Okta, Azure  │ │ Grafana,     │                │   │
│  │  │ Redis        │ │ AD           │ │ Datadog      │                │   │
│  │  └──────────────┘ └──────────────┘ └──────────────┘                │   │
│  │                                                                      │   │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                │   │
│  │  │ AppSec Kit   │ │ Azure Kit    │ │ Swing Kit    │                │   │
│  │  │ Vuln scanner │ │ Terraform    │ │ Vaadin in    │                │   │
│  │  │ SBOM + NVD   │ │ AKS deploy   │ │ Swing apps   │                │   │
│  │  └──────────────┘ └──────────────┘ └──────────────┘                │   │
│  │                                                                      │   │
│  │  ┌──────────────────────────────────────────────────┐               │   │
│  │  │ Collaboration Engine (open source since 24.5)    │               │   │
│  │  │ Real-time: shared forms, presence, messaging     │               │   │
│  │  └──────────────────────────────────────────────────┘               │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─── TOOLS ───────────────────────────────────────────────────────────┐   │
│  │                                                                      │   │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                │   │
│  │  │ Copilot      │ │ TestBench    │ │ Spreadsheet  │                │   │
│  │  │ In-browser   │ │ UI unit +    │ │ Excel in     │                │   │
│  │  │ AI dev tool  │ │ E2E Selenium │ │ browser      │                │   │
│  │  └──────────────┘ └──────────────┘ └──────────────┘                │   │
│  │                                                                      │   │
│  │  Designer (discontinued — replaced by Copilot)                      │   │
│  │                                                                      │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Total ecosystem count

| Category | Artifacts | License |
|----------|-----------|---------|
| Web Components core | 49 | Apache 2.0 |
| Web Components pro | 7 | Commercial |
| React wrappers | 2 packages | Matches underlying |
| Flow (core) | 1 repo (2,104 classes) | Apache 2.0 |
| Flow Components | 1 repo (977 classes) | Apache 2.0 |
| Hilla | 1 framework | Apache 2.0 |
| Server integrations | 3 (Spring, CDI, Quarkus) | Apache 2.0 |
| Legacy migration | 3 (MPR v7, MPR v8, Feature Pack) | Commercial |
| Kits | 8 | 7 commercial, 1 open source |
| Tools | 3 (Copilot, TestBench, Spreadsheet) | Commercial |
| Internal utilities | 7 | Mixed |
| **Total artifacts in platform** | **~85** | |

> PyFlow reuses the 49 core web components + FlowClient.js + Lumo/Aura themes.
> It does not need Spring, CDI, Quarkus, MPR, or any of the kits.
> The pro components could work if included in the bundle.
