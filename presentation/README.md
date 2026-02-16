# PyFlow Presentation

## What This Is

HTML slide deck for presenting Vaadin PyFlow. Single `index.html` file powered by **reveal.js**.

Read `SPECS.md` for the full slide-by-slide specification, design tokens, and image guidelines.

## Tool: reveal.js

- Most mature HTML presentation framework (80k+ GitHub stars)
- Zero build tools needed — just include JS/CSS from CDN or local
- Built-in code syntax highlighting (highlight.js plugin)
- Keyboard navigation, speaker notes (`<aside class="notes">`), PDF export
- Supports fragments (step-by-step reveals within a slide)
- Dark theme out of the box — easy to match docs site colors

### Why reveal.js over alternatives

| Tool | Pros | Cons |
|------|------|------|
| **reveal.js** | Mature, huge ecosystem, no build step, great code blocks | JS dependency |
| Slidev | Vue-based, hot reload | Requires Node + build step |
| Marp | Pure markdown | Limited layout control |
| Plain HTML/CSS | Zero deps | Reinventing the wheel |

## File Structure

```
presentation/
├── index.html          # THE deck — all slides, CSS overrides, reveal.js config
├── images/             # Slide images (screenshots, diagrams, logos)
│   └── (symlink or copy from ../docs/screenshots/)
├── SPECS.md            # Full slide specs (this is the source of truth)
└── README.md           # This file
```

## Images

Screenshots come from the PyFlow demo app (Lumo Dark theme) and the docs site.

### Sources

| Image | Source |
|-------|--------|
| `architecture.png` | `../docs/screenshots/architecture.png` |
| `screenshot-*.png` | `../docs/screenshots/screenshot-*.png` |
| `logo.svg` | `../docs/logo.svg` |
| Code snippets | Inline `<pre><code>` with reveal.js highlight plugin |

### Tips for new images

- **Live demo screenshots**: Start `python -m demo`, use Playwright MCP to navigate and `browser_take_screenshot`
- **Architecture diagrams**: Reuse existing `architecture.png` or create new ones matching dark theme (`#1a1a2e` background)
- **Code screenshots**: Prefer live `<code>` blocks over images — reveal.js highlights Python natively
- **Aspect ratio**: Slides are 16:9 (1920x1080). Images should fit without cropping.
- **Dark backgrounds**: All images must look good on dark backgrounds. No white-background PNGs.

## How to Present

```bash
cd presentation
python -m http.server 8001
# Open http://localhost:8001
```

### Keyboard shortcuts (reveal.js)

| Key | Action |
|-----|--------|
| `Space` / `Right` | Next slide |
| `Left` | Previous slide |
| `Esc` / `O` | Overview (slide grid) |
| `S` | Speaker notes window |
| `F` | Fullscreen |
| `B` | Black screen (pause) |

### PDF export

Append `?print-pdf` to the URL, then Ctrl+P / Cmd+P and save as PDF.

## How to Verify

1. Open in browser, press `Esc` to see overview of all ~15 slides
2. Navigate through all slides with arrow keys
3. Check that code blocks have syntax highlighting
4. Check that screenshots load and are sharp at 1080p
5. Press `S` to verify speaker notes appear
6. Resize to smaller window — slides should scale, not break
