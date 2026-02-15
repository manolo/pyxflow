# PyFlow Landing Website — Specs

## Purpose

Single-page marketing/documentation landing site for Vaadin PyFlow — a Python framework for building web UIs with Vaadin components. The goal is to make developers fall in love with PyFlow at first sight.

## Architecture

```
web/
├── index.html              # Single self-contained page (HTML + CSS + JS)
├── logo.svg                # PyFlow logo (Python snake + flow motif, blue/cyan gradient)
├── screenshots/            # App screenshots from the demo (Lumo Dark theme)
│   ├── screenshot-hello.png
│   ├── screenshot-grid.png
│   ├── screenshot-master-detail.png
│   ├── screenshot-components.png
│   ├── screenshot-file-explorer.png
│   ├── screenshot-stopwatch.png
│   └── architecture.png
├── SPECS.md                # This file
└── CLAUDE.md               # Instructions for Claude Code
```

**Zero external dependencies.** No fonts, no libraries, no CDN, no build tools. Everything is embedded in `index.html`.

## Sections (in order)

### 1. Nav (fixed top)
- Logo + "PyFlow" brand
- Links: Features, Architecture, Examples, Components, Quick Start, GitHub
- Frosted glass effect: `backdrop-filter: blur(12px)`
- On mobile (<768px): nav links hidden, only brand visible

### 2. Hero (full viewport)
- Left: headline "Build Web Apps in **Pure Python**" + subtitle + CTA buttons (Get Started, View on GitHub)
- Right: code block with **typing animation** of a hello world view
- Typing animation: character-by-character reveal preserving HTML syntax spans, blinking cursor
- Background: 3-stop gradient `#1a1a2e → #16213e → #0f3460` with subtle radial glows

### 3. Why PyFlow (feature cards)
- 4 cards in a responsive grid: Pure Python, 49+ Components, Real-time Push, Hot Reload
- Each card: SVG icon (inline, no deps) + title + description
- Hover effect: lift + blue border glow

### 4. Architecture — "How It Works"
- AI-generated illustration (`screenshots/architecture.png`) showing server-browser concept
- Animated diagram: **Python Server** box ↔ WebSocket wire ↔ **Browser (Thin Client)** box
  - Server lists: Business logic, Data access & validation, UI state management, Session & security, Your Python code
  - Browser lists: Vaadin web components, DOM rendering, then negatives with 🛡️ icon (No business logic, No data access, No API endpoints)
  - Animated cyan wire with pulsing gradient between them, labeled "WebSocket" / "UI diffs only"
- Subtitle: "Your code runs on the server. The browser is just a *Thin-Client*. No server APIs to expose, no JS business code to ship."
- 3 benefit cards below:
  1. **Zero Attack Surface** — No REST APIs, no GraphQL, binary WebSocket opaque to pentesters
  2. **Server-side State** — All logic/validation/data on server, nothing sensitive in browser
  3. **Minimal Bandwidth** — Only UI diffs, no full-page reloads, no heavy JS bundles
- CSS animation: `wirePulse` keyframes on the connection line

### 5. Code Showcase (side-by-side)
- 3 examples, alternating layout (code-left/screenshot-right, then reversed):
  1. **Hello World** — `views/hello.py` → `screenshot-hello.png`
  2. **Data Grid** — `views/grid.py` → `screenshot-grid.png` (reversed layout)
  3. **Master-Detail CRUD** — `views/master_detail.py` → `screenshot-master-detail.png`
- Code blocks: macOS-style window chrome (red/yellow/green dots, filename)
- Syntax highlighting via CSS classes (no external lib)

### 6. Component Gallery
- Hero image: `screenshot-components.png` (LoginForm, ListBox, ProgressBar, Avatar, Tabs, MenuBar, etc.)
- 2-column grid below: File Explorer + Stopwatch screenshots

### 7. Quick Start
- Terminal-style block with install commands: `pip install vaadin-pyflow`, create app, run with `--dev`
- File tree showing minimal app structure (3 files)

### 8. Footer
- Links: GitHub, Issues, Vaadin
- "Apache 2.0 License" text

## Design Language

| Token | Value |
|-------|-------|
| Background base | `#1a1a2e` |
| Background deep | `#16213e` |
| Background darkest | `#0f3460` |
| Code block bg | `#0d1117` |
| Accent primary | `#1676f3` (Vaadin blue) |
| Accent secondary | `#00d2ff` (cyan) |
| Text primary | `#e6edf3` |
| Text secondary | `#8899aa` |
| Text muted | `#6e7681` |
| Border subtle | `rgba(255,255,255,0.06)` |
| Border hover | `rgba(22,118,243,0.3)` |
| Font stack | `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, ...` |
| Mono font | `'SF Mono', 'Fira Code', 'Cascadia Code', Consolas, monospace` |

### Syntax highlighting classes

| Class | Color | Usage |
|-------|-------|-------|
| `.kw` | `#ff7b72` | Keywords: `from`, `import`, `def`, `lambda` |
| `.fn` | `#d2a8ff` | Function names |
| `.str` | `#a5d6ff` | String literals |
| `.cls` | `#7ee787` | Class names |
| `.dec` | `#ffa657` | Decorators: `@route` |
| `.cmt` | `#6e7681` | Comments |
| `.op` | `#79c0ff` | Operators |

## Animations

- **Typing animation** (hero): JS-driven, 35-60ms per character, 120ms between lines, blinking cursor
- **Fade-in on scroll**: CSS `opacity + translateY` transitions triggered by `IntersectionObserver` (threshold: 0.1)
- **Hover lifts**: `translateY(-2px)` to `translateY(-4px)` on buttons, cards, gallery items

## Responsive Breakpoints

- **>768px**: 2-column grids, full nav, side-by-side showcase
- **<=768px**: Single column, centered text, nav links hidden, stacked showcase items

## Screenshots

Screenshots are captured from the PyFlow demo app running at `localhost:8089` with Lumo Dark theme. To refresh them:

1. Start the demo: `cd ../.. && python -m vaadin --dev` (from the pyflow demo project)
2. Use Playwright MCP to navigate and take screenshots
3. Save to `web/screenshots/`

## Verification

```bash
cd web && python -m http.server 8000
# Open http://localhost:8000
```

Checklist:
- [ ] All 6 screenshots + architecture.png load correctly (hello, grid, master-detail, components, file-explorer, stopwatch, architecture)
- [ ] Typing animation plays in hero section
- [ ] Code snippets have syntax highlighting
- [ ] Smooth scroll between sections via nav links
- [ ] Fade-in animations trigger on scroll
- [ ] Responsive layout on narrow viewport (<768px)
- [ ] Logo SVG renders correctly
- [ ] All external links point to correct URLs
