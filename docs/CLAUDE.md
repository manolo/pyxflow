# PyXFlow Landing Website

## What This Is

Single-page marketing landing site for Vaadin PyXFlow. Pure HTML+CSS+JS, zero dependencies, no build tools.

**Content source of truth**: `INDEX.md` — section-by-section content for regenerating `index.html`.
**Design specs**: `SPECS.md` — colors, typography, animations, responsive rules.
**Asset sources**: `README.md` — screenshot origins, logo prompts, regeneration guide.

## File Structure

```
docs/
├── index.html          # THE site — all HTML, CSS, and JS in one file
├── logo.png            # Logo (Python snake + flow, blue/cyan gradient)
├── screenshots/        # App screenshots (Lumo Dark theme)
│   ├── screenshot-hello.png
│   ├── screenshot-grid.png
│   ├── screenshot-master-detail.png
│   ├── screenshot-components.png
│   ├── screenshot-file-explorer.png
│   ├── screenshot-stopwatch.png
│   └── architecture.png
├── SPECS.md            # Full design specs
└── CLAUDE.md           # This file
```

## Key Constraints

- **Single file**: Everything in `index.html` — embedded `<style>` and `<script>`, no external files
- **No dependencies**: No CDN fonts, no JS libraries, no CSS frameworks
- **Dark theme**: Must match Lumo Dark screenshots — background `#1a1a2e`, code blocks `#0d1117`
- **Syntax highlighting**: Manual `<span>` classes (`.kw`, `.fn`, `.str`, `.dec`, `.cmt`), not a library
- **Screenshots are static PNGs**: Referenced as `screenshots/screenshot-*.png`

## How to Update Content

### Changing code examples
The showcase section has 3 examples with hand-written syntax-highlighted HTML. Each `<pre>` block uses `<span class="kw">`, `<span class="str">`, etc. for coloring. When updating code examples:
1. Write the Python code
2. Wrap keywords in `<span class="kw">`, strings in `<span class="str">`, decorators in `<span class="dec">`, function names in `<span class="fn">`, comments in `<span class="cmt">`
3. The hero typing animation code is in the `<script>` section — the `codeLines` array contains HTML-encoded lines

### Updating screenshots
Screenshots come from the PyXFlow demo app. To refresh:
1. Start the demo app (ask user which port)
2. Use Playwright MCP: `browser_navigate` → `browser_take_screenshot`
3. Save PNGs to `docs/screenshots/`

### Adding a new showcase example
1. Add a new `<div class="showcase-item fade-in">` (or `showcase-item reverse fade-in` for alternating layout) inside the `#showcase` section
2. Include a `.showcase-code` block with window chrome (dots + filename) and a `<pre>` with syntax spans
3. Include a `.showcase-screenshot` with the corresponding screenshot `<img>`

### Adding a new feature card
Add inside `.features` grid in the `#why` section:
```html
<div class="feature-card fade-in">
  <div class="feature-icon"><svg>...</svg></div>
  <h3>Title</h3>
  <p>Description</p>
</div>
```

## How to Verify

```bash
cd docs && python -m http.server 8000
# Open http://localhost:8000
```

Or use Playwright MCP:
1. `browser_navigate` → `http://localhost:8000`
2. `browser_take_screenshot` for the hero
3. Navigate to `#why`, `#architecture`, `#showcase`, `#gallery`, `#quickstart` and screenshot each
4. Resize to 390x844 for mobile check

## GitHub URLs

- Repository: `https://github.com/manolo/pyxflow`
- Issues: `https://github.com/manolo/pyxflow/issues`
- Nav GitHub link: `https://github.com/manolo/pyxflow`

## PyXFlow API Patterns (for code snippets)

Code snippets must match the real PyXFlow API. Reference source at `~/Github/platform/python/pyxflow/`.

### Imports
```python
from pyxflow import Route, Menu, Push       # decorators
from pyxflow.components import *             # UI components
from pyxflow.data import Binder, ...         # data binding
```

### Decorators
- `@Route("path")` — uppercase R, only the route path
- `@Menu("Title", icon="vaadin:icon")` — separate decorator for menu entry
- `@Push` — decorator on AppShell class for WebSocket push
- `@AppShell` — marks the global app config class
- `@ColorScheme("dark")` — sets initial theme

### Views are classes
```python
@Route("hello")
@Menu("Hello", icon="vaadin:hand")
class HelloView(VerticalLayout):
    def __init__(self):
        ...
```

### Button smart params
`Button("text", callback)` — no `on_click=` needed, Button auto-detects callable args.

### Key components
- `VerticalLayout`, `HorizontalLayout`, `Div` — layout bases
- `Grid` — `add_column()`, `set_items()`, `set_data_provider(callback)`
- `SplitLayout` — `add_to_primary()`, `add_to_secondary()`
- `TreeGrid` — `add_hierarchy_column()`, `set_items(items, children_provider=fn)`
- `Binder(Model)` — `bind_instance_fields(self)`, `read_bean()`, `write_bean()`
- `Notification.show("text")`

## CSS Structure (in order inside `<style>`)

1. Reset & Base
2. Utility (`.container`, `.section`, `.fade-in`)
3. Nav (fixed, frosted glass)
4. Hero (full viewport, gradient, grid layout)
5. Hero Code Block (typing animation, window chrome)
6. Syntax colors (`.kw`, `.fn`, `.str`, `.cls`, `.dec`, `.cmt`, `.op`)
7. Why PyXFlow (feature cards grid)
8. Architecture (illustration, animated diagram with 🛡️ icons for browser negatives, benefit cards)
9. Code Showcase (alternating side-by-side)
10. Component Gallery (hero image + grid)
11. Quick Start (terminal + file tree)
12. Footer
13. Responsive (`@media max-width: 768px`)

## JS (in `<script>` at bottom)

Two features:
1. **Typing animation**: `codeLines` array → character-by-character reveal with `revealChars()` that preserves HTML tags → blinking cursor at end
2. **Scroll fade-in**: `IntersectionObserver` adds `.visible` class to `.fade-in` elements when they enter viewport
