# PyFlow Landing Website — Content Spec

**Source of truth** for `index.html`. Edit this file to change page content; regenerate HTML from it.

**Design tokens & animations**: See `SPECS.md`
**Modification instructions**: See `CLAUDE.md`
**Asset sources & regeneration guide**: See `README.md`

---

## Page Metadata

| Field | Value |
|-------|-------|
| Title | `PyFlow — Build Web Apps in Pure Python` |
| Language | `en` |
| Format | Single self-contained HTML file (embedded `<style>` + `<script>`, zero external dependencies) |

---

## Section 1: Nav (fixed top)

| Field | Value |
|-------|-------|
| ID | *(none — `<nav>` element)* |
| Position | Fixed top, z-index 100, frosted glass (`backdrop-filter: blur(12px)`) |
| Brand | Logo (`logo.png`, 60px) + "PyFlow" + "by Vaadin" subtitle |

**Nav links** (in order):

| Label | Target |
|-------|--------|
| Features | `#why` |
| Architecture | `#architecture` |
| Examples | `#showcase` |
| Components | `#gallery` |
| Quick Start | `#quickstart` |
| GitHub | `https://github.com/vaadin/vaadin-pyflow` (external) |

**Responsive**: Links hidden on mobile (<768px), only brand visible.

---

## Section 2: Hero

| Field | Value |
|-------|-------|
| ID | `hero` |
| Layout | Full viewport height, 2-column grid (text left, code right) |
| Background | 3-stop gradient: `#1a1a2e → #16213e → #0f3460` with radial glows |

**Left column — text:**

| Element | Content |
|---------|---------|
| Headline | `Build Web Apps` / `in Pure Python` (gradient accent on "Pure Python") |
| Subtitle | `No JavaScript. No HTML. Just Python.` / `Enterprise-grade Vaadin components, powered by Python.` |
| CTA primary | "Get Started" → `#quickstart` |
| CTA secondary | "View on GitHub" (with GitHub SVG icon) → `https://github.com/vaadin/vaadin-pyflow` |

**Right column — code block with typing animation:**

| Field | Value |
|-------|-------|
| Filename | `hello.py` |
| Window chrome | macOS dots (red/yellow/green) |
| Animation | Character-by-character reveal, 35-60ms/char, 120ms between lines, blinking cursor |

```python
from vaadin.flow import Route, Menu
from vaadin.flow.components import *

@Route("hello")
@Menu("Hello", icon="vaadin:hand")
class HelloView(HorizontalLayout):
    def __init__(self):
        name = TextField("Your name")
        button = Button("Say hello", lambda e:
            Notification.show(f"Hello {name.value}"))
        self.add(name, button)
```

---

## Section 3: Why PyFlow

| Field | Value |
|-------|-------|
| ID | `why` |
| Title | `Why PyFlow?` |
| Subtitle | `Everything you need to build production web apps, without leaving Python.` |
| Layout | 4 feature cards in responsive grid (`minmax(240px, 1fr)`) |

**Feature cards** (each has an inline SVG icon):

| # | Icon | Title | Description |
|---|------|-------|-------------|
| 1 | Star | Pure Python | Write your entire UI in Python. No JavaScript, no HTML templates, no CSS. Just clean, idiomatic Python code. |
| 2 | Grid (4 squares) | 49+ Vaadin Components | Enterprise-grade UI components: Grid, Forms, Charts, Login, MenuBar, TreeGrid, and many more. Battle-tested at scale. |
| 3 | Lightning bolt | Real-time Push | Built-in WebSocket support for live updates. Stream data to the browser in real time with server push. |
| 4 | Refresh arrow | Hot Reload | Instant feedback with `--dev` mode. Edit your Python code and see changes reflected immediately in the browser. |

---

## Section 4: Architecture — "How It Works"

| Field | Value |
|-------|-------|
| ID | `architecture` |
| Title | `How It Works` |
| Subtitle | `Your code runs on the server. The browser is just a Thin-Client.` / `No server APIs to expose, no JS business code to ship.` |

**Architecture illustration:**

| Image | Alt text |
|-------|----------|
| `screenshots/architecture.png` | Server-side architecture: Python server connected to thin-client browsers via WebSocket |

**Animated diagram** — two boxes connected by a pulsing wire:

**Python Server box** (green checkmarks):
1. Business logic
2. Data access & validation
3. UI state management
4. Session & security
5. Your Python code

**Wire** (animated gradient pulse):
- Label: `UIDL/WebSocket`
- Sub-label: `UI diffs only`

**Browser (Thin Client) box** (shield icons for negatives, green checks for positives):
- Vaadin web components (positive)
- DOM rendering (positive)
- No business logic (negative/shield)
- No data access (negative/shield)
- No API endpoints (negative/shield)

**3 benefit cards:**

| # | Icon | Title | Description |
|---|------|-------|-------------|
| 1 | Lock | Zero Attack Surface | No REST APIs, no GraphQL, no endpoints to exploit. The UIDL protocol is opaque to pentesters. XSS and injection are by design impossible. |
| 2 | Shield | Server-side State | All logic, validation, and data stay on the server. Nothing sensitive reaches the browser. Dificult to tamper from DevTools. |
| 3 | Lightning bolt | Minimal Bandwidth | Only UI diffs travel the wire. No full-page reloads, no heavy JS bundles to download. Instant interactions over WebSocket. |

---

## Section 5: Code Showcase

| Field | Value |
|-------|-------|
| ID | `showcase` |
| Title | `See It in Action` |
| Subtitle | `Real examples, real screenshots. From hello world to full CRUD apps.` |
| Layout | 3 examples, alternating (normal / reversed / normal) side-by-side grid |

### Example 1: Hello World

| Field | Value |
|-------|-------|
| Label | `Hello World` |
| Description | `A complete web app in Python. Text field, button, and a notification toast.` |
| Filename | `views/hello.py` |
| Screenshot | `screenshots/screenshot-hello.gif` |
| Layout | Normal (code left, screenshot right) |

```python
from vaadin.flow import Route, Menu
from vaadin.flow.components import *

@Route("hello")
@Menu("Hello", icon="vaadin:hand")
class HelloView(HorizontalLayout):
    def __init__(self):
        name = TextField("Your name")
        button = Button("Say hello", lambda e:
            Notification.show(f"Hello {name.value}"))
        self.add(name, button)
```

### Example 2: Data Grid with Lazy Loading

| Field | Value |
|-------|-------|
| Label | `Data Grid with Lazy Loading` |
| Description | `Sortable columns, lazy data provider, selection events. Fetches only visible rows.` |
| Filename | `views/grid.py` |
| Screenshot | `screenshots/screenshot-grid.gif` |
| Layout | Reversed (screenshot left, code right) |

```python
@Route("grid")
@Menu("Grid", icon="vaadin:table")
class GridView(VerticalLayout):
    def __init__(self):
        self.grid = Grid()
        self.grid.add_column("name", header="Name")
        self.grid.add_column("email", header="Email")
        self.grid.add_column("role").set_sortable(True)
        self.grid.add_column("city").set_sortable(True)

        # Lazy: only fetches visible rows
        self.grid.set_data_provider(self.fetch)
        self.add(self.grid)

    def fetch(self, offset, limit, sorts):
        return people[offset:offset+limit], len(people)
```

### Example 3: Master-Detail CRUD

| Field | Value |
|-------|-------|
| Label | `Master-Detail CRUD` |
| Description | `SplitLayout with Grid + Form. Binder handles validation and save/cancel.` |
| Filename | `views/master_detail.py` |
| Screenshot | `screenshots/screenshot-master-detail.gif` |
| Layout | Normal (code left, screenshot right) |

```python
from vaadin.flow.components import *
from vaadin.flow.data import Binder

@Route("master-detail")
@Menu("Master-Detail", icon="vaadin:split-h")
class MasterDetailView(Div):
    def __init__(self):
        split = SplitLayout()
        self.grid = Grid()
        self.grid.set_columns("firstName", "lastName",
            "email", "phone")
        self.grid.set_items(people)
        split.add_to_primary(self.grid)

        form = FormLayout()
        self.first = TextField("First Name")
        self.last = TextField("Last Name")
        form.add(self.first, self.last)

        self.binder = Binder(Person)
        self.binder.bind_instance_fields(self)
        split.add_to_secondary(form)
        self.add(split)
```

---

## Section 6: Component Gallery

| Field | Value |
|-------|-------|
| ID | `gallery` |
| Title | `Component Gallery` |
| Subtitle | `49+ enterprise-grade Vaadin components, all accessible from Python.` |

**Images:**

| Position | Image | Alt text |
|----------|-------|----------|
| Hero (full width) | `screenshots/screenshot-components.gif` | Component Gallery showing LoginForm, ListBox, ProgressBar, Avatar, Tabs, MenuBar and more |
| Grid card 1 | `screenshots/screenshot-file-explorer.gif` | TreeGrid File Explorer |
| Grid card 2 | `screenshots/screenshot-stopwatch.gif` | Stopwatch with Server Push |

---

## Section 7: Quick Start

| Field | Value |
|-------|-------|
| ID | `quickstart` |
| Title | `Quick Start` |
| Subtitle | `Up and running in under a minute.` |

**Terminal commands:**

```bash
# Install PyFlow
$ pip install git+https://github.com/manolo/vaadin-pyflow.git

# Create your app
$ mkdir myapp && cd myapp
$ mkdir views

# Optionally create some demo views
$ vaadin --setup

# Run with hot reload
$ vaadin --dev
```

**File tree:**

```
myapp/
  views/            <- your views
    hello.py
  static/           <- optional
    styles/styles.css  <- custom styles
```

---

## Section 8: Footer

| Field | Value |
|-------|-------|
| ID | *(none — `<footer>` element)* |
| Links | GitHub (`https://github.com/vaadin/vaadin-pyflow`), Issues (`https://github.com/vaadin/vaadin-pyflow/issues`) |
| Text | `PyFlow by Vaadin }> — Open source under the Apache 2.0 License.` |

---

## Other Documentation Files

| File | Purpose |
|------|---------|
| `SPECS.md` | Design system: colors, typography, syntax classes, animations, responsive rules |
| `CLAUDE.md` | Instructions for modifying the site with Claude Code |
| `README.md` | Asset sources, logo generation prompts, regeneration guide |
