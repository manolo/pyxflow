# PyFlow Presentation — Slide Specs

## Overview

~15 slides. Target audience: Python developers, Java/Vaadin developers, tech leads evaluating frameworks.
Duration: 15-20 minutes.

### Narrative arc

1. **Inspiration** (slides 1-3): BSSN philosophy + why Python + why now
2. **What is PyFlow** (slides 4-6): Architecture, thin client, hello world
3. **Features** (slides 7-11): Components, Grid, CRUD, Push, ClientCallable
4. **How it was built** (slides 12-13): Spec-driven development with AI agents
5. **Closing** (slides 14-15): DX, getting started

### Source material

| Reference | Key takeaway |
|-----------|-------------|
| Dan North — _"Best Simple System for Now"_ (Jfokus) | Look for the **essence** of the problem. Simple is a function of Now. Don't over-engineer. |
| Arun Gupta — _"Spec-Driven Development using Coding Agents"_ | Write specs first, let AI generate code. Separate thinking from doing. "Run slow to run fast." |
| TIOBE Index (Feb 2026) | Python #1 at 21.81%, >10 points ahead of #2. Peaked at 26.98% in July 2025. |

---

## Design Language

Match the docs landing site (`../docs/index.html`).

| Token | Value |
|-------|-------|
| Background | `#1a1a2e` (dark navy) |
| Background gradient | `linear-gradient(135deg, #1a1a2e, #16213e, #0f3460)` |
| Accent primary | `#1676f3` (Vaadin blue) |
| Accent secondary | `#00d2ff` (cyan) |
| Text primary | `#e6edf3` |
| Text secondary | `#8899aa` |
| Code block bg | `#0d1117` |
| Font | System sans-serif (same as docs) |
| Mono font | `'SF Mono', 'Fira Code', Consolas, monospace` |

### reveal.js theme

Use `black` as base theme, override with custom CSS:

```css
.reveal {
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  color: #e6edf3;
}
.reveal h1, .reveal h2 { color: #fff; }
.reveal h3 { color: #00d2ff; }
.reveal code { color: #a5d6ff; }
.reveal a { color: #00d2ff; }
.reveal .highlight { color: #1676f3; }

/* Gradient text for key titles */
.gradient-text {
  background: linear-gradient(135deg, #fff, #1676f3);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

---

## Slides

### 1. Title

**Layout**: Centered, big impact

- Logo (`logo.svg`) centered, large
- Title: **"PyFlow"** (gradient text, very large)
- Subtitle: _"Build Web Apps in Pure Python"_
- Tagline: `No JavaScript. No HTML. Just Python.`

**Speaker notes**: Introduce yourself, mention this is a new way to build web apps with Python. Tease the story: this started with a question — what is the _essence_ of a web framework?

---

### 2. The Essence — BSSN

**Layout**: Left-aligned, quote-driven

- Heading: **"Look for the essence of the problem"**
- Quote block: _"A complex system that works is invariably found to have evolved from a simple system that worked."_ — John Gall
- Bullets (fragments):
  - "I saw Dan North's talk at Jfokus: _Best Simple System for Now_"
  - "His idea: don't ask _what is there_ — ask **what should be there**"
  - "So I looked at Vaadin Flow's 25 years of Java code..."
  - "...and asked: **what is the essence?**"

**Speaker notes**: Credit Dan North. BSSN = find the essence, strip everything else. Vaadin Flow has 25 years of accumulated complexity. But the core idea is brilliantly simple: server renders UI, browser is a thin client. That's the essence I wanted to port.

---

### 3. Why Python? Why Now?

**Layout**: Two columns — stats left, reasoning right

- Left column: TIOBE Index data
  - **Python #1** — 21.81% (Feb 2026)
  - >10 points ahead of C (#2, 11.05%)
  - >13 points ahead of Java (#4, 8.12%)
  - Chart showing Python's dominance (image or simplified bar chart)
  - _"The most popular language in the world has no full-stack web framework"_
- Right column (fragments):
  - "I hadn't written Python in 10 years"
  - "But 22% of all developers use it"
  - "They deserve enterprise-grade web components"
  - "One language, one team, one deployment"

**Speaker notes**: Python is the #1 language by a huge margin. Django/Flask/FastAPI are great for APIs, but they all need JavaScript for the frontend. There's no server-side UI framework like Vaadin for Python. That's the gap. TIOBE source: tiobe.com/tiobe-index/

**Image tip**: Screenshot the TIOBE ranking table and the historical chart from tiobe.com/tiobe-index/. Crop to show top 5-6 languages.

---

### 4. The Architecture — Thin Client

**Layout**: Full-slide image + text overlay

- `architecture.png` centered (or the animated diagram from docs)
- Key labels:
  - Left box: **"Python Server"** — Your code, business logic, data, sessions
  - Right box: **"Browser"** — Vaadin web components (thin client)
  - Connection: **"WebSocket — UI diffs only"**
- Bottom text: _"The browser is a thin client. All logic runs on the server."_

**Speaker notes**: This is the essence of Vaadin, unchanged for 25 years. Server maintains a state tree of UI nodes. Changes are sent as diffs (UIDL protocol). The browser just renders — no business logic, no data access, no API endpoints exposed. The same protocol that powers Java Vaadin Flow now runs in Python.

---

### 5. Why Thin Client Matters

**Layout**: 3 cards in a row

- Heading: **"Secure by Architecture"**
- Card 1: **Zero Attack Surface** — "No REST APIs to exploit. No GraphQL endpoints. The WebSocket protocol is opaque and binary."
- Card 2: **One Team, One Language** — "Full-stack Python. No JS specialists, no API contracts, no serialization layer."
- Card 3: **Server-side State** — "All validation, all business logic, all data access — stays on the server. Nothing sensitive in the browser."

**Speaker notes**: Three pillars from the Vaadin philosophy. Security: there is literally nothing to attack on the client. Team: one language means one team, faster iteration. State: no state sync bugs, no stale caches, no optimistic updates gone wrong.

---

### 6. Hello World

**Layout**: Two columns — code left, screenshot right

- Left: Python code block
  ```python
  @Route("hello")
  class HelloView(VerticalLayout):
      def __init__(self):
          name = TextField("Your name")
          Button("Say hello", lambda e:
              Notification.show(f"Hello {name.value}"))
          self.add(name, button)
  ```
- Right: `screenshot-hello.png`
- Caption below: _"7 lines. A complete interactive web view."_

**Speaker notes**: Walk through the code. No HTML, no JS, no template files. The class IS the view. `@Route` maps a URL. Components are Python objects. Events are lambdas. This is what "the essence" looks like.

---

### 7. Component Showcase

**Layout**: Full-slide screenshot

- `screenshot-components.png` (the Components demo view showing LoginForm, ListBox, ProgressBar, etc.)
- Heading overlay: **"49 Enterprise Components"**
- Subtitle: _"Form fields, grids, dialogs, menus, trees, charts — all from Python"_

**Speaker notes**: These are the exact same Vaadin web components used by thousands of Java enterprises. Production-ready, accessible, WCAG compliant, themeable. We didn't rebuild them — we reuse the existing frontend. Only the server side is Python.

---

### 8. Data Grid — Lazy Loading

**Layout**: Two columns — code left, screenshot right

- Left: Python code showing lazy data provider
  ```python
  grid = Grid()
  grid.add_column("name", header="Name").set_sortable(True)
  grid.add_column("email", header="Email").set_sortable(True)
  grid.set_data_provider(self.fetch_page)

  def fetch_page(self, offset, limit, sort_orders):
      return db.query(offset, limit), db.count()
  ```
- Right: `screenshot-grid.png`
- Caption: _"Lazy loading, server-side sorting, single callback."_

**Speaker notes**: Grid is the most complex component. Thousands of rows loaded on demand. Sorting, column reordering, selection — all handled by one callback. No pagination widgets, no state management libraries, no infinite scroll JavaScript.

---

### 9. Master-Detail — Binder & Validation

**Layout**: Two columns — screenshot left, code right

- Left: `screenshot-master-detail.png`
- Right: Python code showing Binder
  ```python
  binder = Binder(Person)
  binder.bind_instance_fields(self)

  def on_save(self, event):
      binder.write_bean(self.person)
      service.save(self.person)
  ```
- Caption: _"Grid + Form + Binder + Validation — the enterprise CRUD pattern."_

**Speaker notes**: The most common enterprise pattern. Binder does two-way data binding with validation. `bind_instance_fields` auto-wires form fields by name. Same API as Java Vaadin, same patterns.

---

### 10. Real-time Push — WebSocket

**Layout**: Two columns — code left, screenshot right

- Left: Python code showing WebSocket push
  ```python
  @AppShell
  @Push
  class App: pass

  async def _tick(self):
      while self._running:
          await asyncio.sleep(1)
          self._elapsed += 1
          ui.access(self._update_display)
  ```
- Right: `screenshot-stopwatch.png`
- Caption: _"Server pushes UI updates via WebSocket. No polling."_

**Speaker notes**: `@Push` enables WebSocket. `ui.access()` safely modifies UI from background tasks. Standard asyncio — no special framework, no Socket.IO, no custom protocols.

---

### 11. @ClientCallable — Browser calls Server

**Layout**: Two columns — screenshot left, code right

- Left: `screenshot-file-explorer.png`
- Right: Python code
  ```python
  @ClientCallable
  def open(self, key):
      item = self.tree_grid.get_item(key)
      subprocess.Popen(["open", item["path"]])
  ```
- Caption: _"Browser calls server methods directly. No REST API needed."_

**Speaker notes**: TreeGrid with double-click handler. The browser fires `$server.open(key)` — calls the Python method directly over WebSocket. Return values come back as resolved Promises. No REST endpoint to define, no serialization to worry about.

---

### 12. How It Was Built — Spec-Driven Development

**Layout**: Left-aligned, narrative

- Heading: **"Porting 25 Years of Java in 6 Weeks"**
- Quote: _"Write specs first, let AI generate code. Separate thinking from doing."_ — Arun Gupta, "Spec-Driven Development"
- Approach (fragments):
  - "Studied Java Flow source: StateTree, UIDL protocol, Feature IDs"
  - "Wrote language-agnostic specs: `PROTOCOL.md`, `PITFALLS.md`, `COMPONENTS.md`"
  - "AI agents generated Python code from specs"
  - "Specs became the test oracle — each pitfall became a test case"
  - "Result: **~16,000 LOC**, **2,300+ unit tests**, **400+ UI tests**"
- Bottom: _"The specs are reusable — the same specs could port Flow to Rust, Go, or any language."_

**Speaker notes**: Credit Arun Gupta's SDD talk. I followed his approach: define WHAT (specs), let AI handle HOW (implementation). Wrote specs by reverse-engineering Java Flow. 28 critical pitfalls documented — each one would have cost days of debugging. The specs are language-agnostic: `specs/PROTOCOL.md` describes the UIDL wire format, `specs/PITFALLS.md` lists every trap. An agent in any language can read them and build a working implementation.

---

### 13. The Spec-Driven Loop

**Layout**: Diagram + bullet points

- Heading: **"Spec → Implement → Test → Discover → Spec"**
- Visual: circular diagram showing the loop:
  1. **Read Java source** → understand behavior
  2. **Write spec** → document the "what" and "why"
  3. **AI generates Python** → from spec + Java reference
  4. **Tests validate** → unit tests + Playwright UI tests
  5. **Discover pitfall** → add to `PITFALLS.md`
  6. → back to step 1
- Key stat: _"28 pitfalls documented. Each one saves days of debugging."_

**Speaker notes**: This is the practical loop. Example pitfall: "Constants dedup — resending the same hash breaks FlowClient silently." Without the spec, you'd spend days debugging a blank page. With the spec, it's a one-line check. The specs are the real product — the Python code is just one instantiation.

---

### 14. Developer Experience

**Layout**: Left-aligned, feature list

- Heading: **"Developer Experience"**
- List (fragments):
  - **Pure Python** — Classes, decorators, lambdas. No DSL to learn.
  - **Type hints** — Full IDE autocomplete and error checking
  - **pip install** — `pip install vaadin-pyflow`, that's it
  - **asyncio native** — Background tasks, WebSocket push, standard Python
  - **49 components** — Forms, grids, dialogs, trees, charts, menus...
  - **Two themes** — Lumo & Aura, light & dark, one decorator to switch

**Speaker notes**: Emphasize familiarity. If you know Python, you know PyFlow. No new template language, no JSX, no build toolchain. The "best simple system for now" — just Python.

---

### 15. Getting Started / Closing

**Layout**: Centered, call to action

- Heading: **"Get Started in 30 Seconds"**
- Terminal block:
  ```
  pip install vaadin-pyflow
  vaadin init myapp
  cd myapp && vaadin --dev
  ```
- Then: **"Thank You"** (gradient text, large)
- Closing quote: _"Look for the essence of the problem — not what is there, but what should be there."_ — Dan North
- Links: GitHub repo, documentation, PyPI
- Logo at bottom

**Speaker notes**: Quick demo if time allows — open terminal, run the commands live, show the app. Otherwise, point to the repo and docs. End with Dan North's quote — it's the thread that ties the whole talk together.

---

## Fragment / Animation Guidelines

- Use **fragments** (`class="fragment"`) for bullet lists — reveal one point at a time
- Code blocks appear complete (no fragments within code)
- Screenshots fade in (`class="fragment fade-in"`)
- No excessive animations — keep it professional
- Slide transitions: `slide` (horizontal) is fine, avoid fancy 3D effects

## Speaker Notes

Every slide should have `<aside class="notes">` with:
- Key talking points
- Transition phrase to next slide
- Time estimate (aim for ~1 min per slide)

## Images Needed

| Image | Source | Notes |
|-------|--------|-------|
| `logo.svg` | `../docs/logo.svg` | PyFlow logo |
| `architecture.png` | `../docs/screenshots/architecture.png` | Server ↔ Browser diagram |
| `screenshot-hello.png` | `../docs/screenshots/` | Hello World view |
| `screenshot-grid.png` | `../docs/screenshots/` | Grid with lazy loading |
| `screenshot-master-detail.png` | `../docs/screenshots/` | SplitLayout + form |
| `screenshot-components.png` | `../docs/screenshots/` | Component gallery |
| `screenshot-stopwatch.png` | `../docs/screenshots/` | Stopwatch with push |
| `screenshot-file-explorer.png` | `../docs/screenshots/` | TreeGrid file browser |
| `tiobe-ranking.png` | **NEW** — screenshot from tiobe.com/tiobe-index/ | Top 5-6 languages table |
| `tiobe-chart.png` | **NEW** — screenshot from tiobe.com/tiobe-index/ | Historical trend graph |
| `theme-variants.png` | **NEW** — 2x2 grid of same view in Lumo/Aura light/dark | Optional, for slide 14 |

**Image tips:**
- All images must look good on dark `#1a1a2e` background
- Screenshots from the demo app are already Lumo Dark — they work perfectly
- For TIOBE screenshots: use browser dark mode or add a dark border/shadow
- Prefer 16:9 aspect ratio (1920x1080) to fill the slide cleanly

## Live Demo Option

If presenting with a live demo, slides 6, 8, 9, 10, 11 can switch to the running app instead of screenshots:
- Start `python -m demo` on `:8088` before the talk
- Alt-tab to browser, show the real app
- Alt-tab back to slides

Keep the screenshots in the slides as fallback (network issues, projector problems, etc.).

## Summary of References

### Dan North — "Best Simple System for Now" (Jfokus)

Key ideas used in this presentation:
- **"Look for the essence"** — not what is there, but what should be there
- **"Simple is a function of Now"** — context changes everything
- **Gall's Law** — complex systems that work evolve from simple ones that worked
- **CUPID** — Composable, Unix philosophy, Predictable, Idiomatic, Domain-based
- **"If you don't end up regretting your early technology decisions, you probably over-engineered"** — Randy Shoup
- **Just Start™** — and expect to be rubbish. "Code like no one is watching."

### Arun Gupta — "Spec-Driven Development using Coding Agents"

Key ideas used in this presentation:
- **Separate thinking from doing** — Specs define "what," agents define "how"
- **"Run slow to run fast"** — invest in specs upfront to accelerate delivery
- **Specs as reusable artifacts** — same spec → Java, Go, Python, any language
- **The SDD loop** — Define WHAT → Agents implement HOW → Human-in-the-loop oversees
- **Spec → Implementation plan → Phased delivery** with validation gates
- **"AI amplifies what you already have — make sure you're amplifying the right things"**

### TIOBE Index (February 2026)

- Python #1: 21.81% (peaked at 26.98% in July 2025)
- C #2: 11.05%, C++ #3: 8.55%, Java #4: 8.12%
- Python leads by >10 points — dominant across data science, AI, scripting, education
- "The most popular programming language in the world has no full-stack UI framework"
