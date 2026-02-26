# PyFlow Landing Website — Design Specs

**Content source of truth**: See `INDEX.md` — section-by-section content for regenerating `index.html`.

## Purpose

Single-page marketing landing site for Vaadin PyFlow. Dark theme, zero external dependencies, single HTML file.

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

1. Start the demo: `cd vaadin-pyflow && source .venv/bin/activate && python -m demo` → :8088
2. Use Playwright MCP to navigate and take screenshots
3. Save to `docs/screenshots/`

## Verification

```bash
cd docs && python -m http.server 8000
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
