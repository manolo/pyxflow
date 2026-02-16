# Rebuild Guide — PyFlow Presentation

How to regenerate `index.html` from scratch. All design decisions captured here so nothing needs to be re-researched.

---

## Quick Rebuild

```
1. Read SPECS.md (slide content, design tokens)
2. Read this file (design decisions, CSS patterns, lib usage)
3. Regenerate images if needed (§ Images below)
4. Generate index.html following the Structure + Design Decisions below
5. Serve: cd presentation && python -m http.server 8001
6. Verify in browser: http://localhost:8001
```

---

## File Structure

```
presentation/
├── index.html              # THE deck (generated from SPECS.md + this guide)
├── SPECS.md                # Source of truth for slide CONTENT
├── REBUILD.md              # THIS FILE — design decisions, CSS, lib usage
├── PLAN.md                 # Generic step-by-step plan (references SPECS.md)
├── README.md               # Quick reference for presenting
├── record_gifs.py          # Playwright script to record demo GIFs (see § Animated GIFs)
├── jfokus/                 # Source PDFs from Jfokus 2026 talks
│   ├── Full-stack web apps, 100% Java.pdf        # Marcus Hellberg (19 slides)
│   ├── Spec-driven-Development-using-Coding-Agents.pdf  # Arun Gupta (32 slides)
│   └── The-Best-Simple-System-for-Now.pdf         # Dan North (22 slides)
├── references/             # Inspirational talk summaries (Spanish, with key quotes)
│   ├── dan-north-bssn.md           # Dan North — "Best Simple System for Now"
│   ├── arun-gupta-sdd.md           # Arun Gupta — "Spec-Driven Development"
│   ├── marcus-hellberg-fullstack.md       # Marcus Hellberg — "Full-stack Web Apps, 100% Java"
│   ├── marcus-hellberg-fullstack-java.md  # (duplicate — same content, can delete)
│   └── tiobe-feb-2026.md           # TIOBE Index data (Feb 2026)
├── lib/                    # Reusable JS libraries (DO NOT regenerate)
│   ├── typewriter.js       # Character-by-character code typing animation
│   ├── tiobe-chart.js      # Highcharts interactive chart (dark theme)
│   └── tiobe-data.js       # TIOBE series data (10 languages, ~293 points each)
└── images/                 # All slide images
    ├── architecture.png    # Symlink → ../../docs/screenshots/architecture.png
    ├── logo.png            # Symlink → ../../docs/logo.png
    ├── screenshot-*.png    # Symlinks → ../../docs/screenshots/screenshot-*.png (static fallbacks)
    ├── screenshot-*.gif    # Animated GIFs of each demo view (used in slides)
    ├── demo-hello.gif      # Animated GIF from record_gifs.py (NOT used in slides)
    ├── bg-*.jpg            # Unsplash background photos for non-demo slides
    ├── tiobe-ranking.png   # Captured from tiobe.com (static fallback)
    └── tiobe-chart.png     # Captured from tiobe.com (static fallback)
```

---

## CDN Dependencies

```html
<!-- reveal.js 5 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/black.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/monokai.css">
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/highlight.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/notes/notes.js"></script>

<!-- Highcharts (for TIOBE chart) -->
<script src="https://code.highcharts.com/highcharts.js"></script>
```

---

## Script Loading Order

```html
<!-- 1. reveal.js core + plugins -->
<script src="reveal.js"></script>
<script src="highlight.js"></script>
<script src="notes.js"></script>
<script>
  Reveal.initialize({
    hash: true,
    transition: 'slide',
    plugins: [RevealHighlight, RevealNotes],
    slideNumber: true
  });
</script>

<!-- 2. Reusable libs (AFTER Reveal init — they listen for Reveal events) -->
<script src="lib/typewriter.js"></script>
<script src="https://code.highcharts.com/highcharts.js"></script>
<script src="lib/tiobe-data.js"></script>
<script src="lib/tiobe-chart.js"></script>
```

**IMPORTANT**: Libs must load AFTER `Reveal.initialize()` because they register `Reveal.on('slidechanged')` and `Reveal.on('ready')` event listeners.

---

## Design Decisions (from user feedback)

### Background images
- **Demo slides** (6-11): Animated GIF of the demo view as background + inline `<img>` for the visible screenshot
- **Non-demo slides** (1, 2, 5, 12-15): Dark Unsplash photos as `data-background-image` with low opacity (0.10-0.15)
- **Slides 3, 4**: No background image (chart and architecture diagram are the main content)
- All backgrounds use `data-background-size="cover"` (photos) or `"contain"` (GIFs with position)
- Background images add visual depth without distracting from content

### Code blocks — Typewriter animation
- Use `<pre class="typewriter-code" data-speed="25"><code>` — NOT regular `<pre><code>`
- The `typewriter.js` lib types code character by character, preserving syntax highlighting
- Speed varies: `data-speed="20"` for long code, `"25"` for medium, `"30"` for short, `"40"` for terminal
- Animation triggers on slide entry (Reveal `slidechanged` event)
- Blinking cyan cursor appears while typing, fades to idle after completion
- Font size: `0.65em` (in `.reveal pre code`)

### TIOBE chart — Interactive Highcharts
- Slide 3 has `<div id="tiobe-chart">` — NOT a static image
- `tiobe-chart.js` renders it via Highcharts with dark theme, hover effects, Python highlighted
- Chart auto-initializes when the slide becomes active
- Stats row above chart: Python 21.81% (glow) vs C 11.05% (muted) vs Java 8.12% (muted)
- Container has embossed border: subtle background, thin border, outer shadow + inner top highlight for relief effect:
  ```
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 12px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.06);
  padding: 0.5em;
  ```

### Slide 12 — "Porting 25 Years..."
- Reduced from 5 fragments to 3 bullet fragments + 1 stats-row fragment = 4 clicks total
- Stats row shows: ~16K LOC, 2,300+ unit tests, 400+ UI tests (with glow effect)
- Was originally too crowded with 6 clicks but only 3 visible items

### Slide 14 — Developer Experience
- 3x2 grid of cards with emoji icons, NOT a bullet list
- Each card is a fragment (reveals one at a time)
- Cards have hover effect (translateY + border color change)
- Icons (HTML entities, NOT literal emojis — for cross-platform rendering):
  - `&#x1F40D;` Pure Python
  - `&#x2328;&#xFE0F;` Type Hints
  - `&#x1F4E6;` pip install
  - `&#x26A1;` asyncio
  - `&#x1F9F1;` 49 Components
  - `&#x1F3A8;` Two Themes

### Slide 3 — "Why Python?"
- Centered layout with stats-row at top + interactive chart below
- NOT two-column layout (was too cramped for the chart)
- Caption: "The most popular language in the world has no full-stack web framework"

---

## CSS Patterns

### Gradient text
```css
.gradient-text {
  background: linear-gradient(135deg, #fff, #1676f3);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

### Glow effect (for key numbers)
```css
.glow { text-shadow: 0 0 20px rgba(0,210,255,0.4), 0 0 40px rgba(0,210,255,0.2); }
```

### Stats row
```css
.stats-row { display: flex; gap: 1.5em; justify-content: center; }
.stat-box .num { font-size: 1.8em; font-weight: bold; color: #00d2ff; }
.stat-box .label { font-size: 0.5em; color: #8899aa; }
```

### DX cards (3x2 grid)
```css
.dx-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1em; }
.dx-card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  padding: 1em 1.2em;
}
.dx-card:hover { transform: translateY(-2px); border-color: rgba(22,118,243,0.4); }
.dx-card .dx-icon { font-size: 1.4em; }
.dx-card strong { color: #00d2ff; font-size: 0.75em; }
.dx-card span { font-size: 0.55em; color: #8899aa; }
```

### Security cards (3-column flex)
```css
.three-cards { display: flex; gap: 1.2em; }
.three-cards > .card { flex: 1; }
.card {
  background: rgba(255,255,255,0.05);
  border-radius: 12px;
  padding: 1.2em;
  border: 1px solid rgba(255,255,255,0.1);
  backdrop-filter: blur(4px);
}
```

### Cycle diagram (Slide 13)
```css
.cycle-step {
  display: inline-block;
  background: rgba(22,118,243,0.15);
  border: 1px solid rgba(22,118,243,0.3);
  border-radius: 8px;
  padding: 0.4em 0.8em;
  font-size: 0.6em;
}
.cycle-arrow { color: #1676f3; font-size: 0.8em; }
```

### Two-column layout
```css
.two-columns { display: flex; gap: 2em; align-items: center; }
.two-columns > div { flex: 1; }
```

### List bullets (custom triangle)
```css
.reveal ul { list-style: none; padding-left: 0; }
.reveal ul li::before { content: "\25B8  "; color: #1676f3; }
```

---

## Slide-by-Slide Background Image Map

Two categories: **demo slides** use animated GIF screenshots, **non-demo slides** use thematic photos from Unsplash (dark backgrounds).

| Slide | Background Image | Opacity | Size | Source |
|-------|-----------------|---------|------|--------|
| 1. Title | bg-python.jpg | 0.12 | cover | Unsplash — code on dark monitor |
| 2. BSSN | bg-zen.jpg | 0.10 | cover | Unsplash — zen stones on dark bg |
| 3. Why Python | (none — has interactive chart) | — | — | — |
| 4. Architecture | (none — image is main content) | — | — | — |
| 5. Secure | bg-security.jpg | 0.10 | cover | Unsplash — matrix-style green code |
| 6. Hello World | screenshot-hello.gif | 0.08 | contain, right center | Demo GIF |
| 7. Components | screenshot-components.gif | 0.15 | cover | Demo GIF |
| 8. Grid | screenshot-grid.gif | 0.06 | contain, right center | Demo GIF |
| 9. Master-Detail | screenshot-master-detail.gif | 0.06 | contain, left center | Demo GIF |
| 10. Push | screenshot-stopwatch.gif | 0.06 | contain, right center | Demo GIF |
| 11. ClientCallable | screenshot-file-explorer.gif | 0.06 | contain, left center | Demo GIF |
| 12. SDD | bg-ai-coding.jpg | 0.15 | cover | Unsplash — dark blue blueprint grid |
| 13. Loop | bg-cycle.jpg | 0.12 | cover | Unsplash — abstract dark rings |
| 14. DX | bg-developer.jpg | 0.10 | cover | Unsplash — code on dark monitors |
| 15. Closing | bg-rocket.jpg | 0.12 | cover | Unsplash — rocket launch at night |

---

## Images — How to Regenerate

### Symlinks (static screenshots)

```bash
cd presentation/images
ln -sf ../../docs/screenshots/architecture.png architecture.png
ln -sf ../../docs/logo.png logo.png
ln -sf ../../docs/screenshots/screenshot-hello.png screenshot-hello.png
ln -sf ../../docs/screenshots/screenshot-components.png screenshot-components.png
ln -sf ../../docs/screenshots/screenshot-grid.png screenshot-grid.png
ln -sf ../../docs/screenshots/screenshot-master-detail.png screenshot-master-detail.png
ln -sf ../../docs/screenshots/screenshot-stopwatch.png screenshot-stopwatch.png
ln -sf ../../docs/screenshots/screenshot-file-explorer.png screenshot-file-explorer.png
```

### Animated GIFs (demo recordings)

The `screenshot-*.gif` files used in the slides were screen-recorded from the running demo app (`python -m demo` on port 8088/8089). There are two methods:

**Method 1: `record_gifs.py`** (Playwright, automated)

```bash
# Start the demo server
cd vaadin-pyflow && source .venv/bin/activate && python -m demo
# In another terminal:
python presentation/record_gifs.py            # all demos
python presentation/record_gifs.py hello      # just one
```

- Requires: `playwright`, `ffmpeg`
- Server must be running on `:8089`
- Outputs `demo-*.gif` to `images/` (hello, components, grid, master-detail, stopwatch)
- Does NOT record file-explorer (must be done manually)
- Outputs smaller GIFs (800-900px wide) named `demo-*.gif`

**Method 2: Manual screen recording** (higher quality, what's in the slides)

The `screenshot-*.gif` files currently used were recorded at a larger resolution (~2066px wide) via OS screen recording or external tools, then converted to GIF with ffmpeg:

```bash
# Convert a screen recording to optimized GIF
ffmpeg -i recording.mov -vf "fps=20,scale=1100:-1:flags=lanczos,palettegen=stats_mode=diff" palette.png
ffmpeg -i recording.mov -i palette.png -lavfi "fps=20,scale=1100:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=3" output.gif
```

### screenshot-hello.gif crop

The original recording was 2066x1144. It was cropped to remove 40% from the right and 30% from the bottom:

```bash
cd presentation/images
ffmpeg -i screenshot-hello.gif -vf "crop=1240:800:0:0" -y screenshot-hello-tmp.gif && mv screenshot-hello-tmp.gif screenshot-hello.gif
```

Result: 1240x800 (keeps the TextField + Button area, removes empty space).

### Background photos (Unsplash)

All backgrounds must have **dark tones** to work with the dark gradient theme. Download at 1920px width, JPEG quality 80.

```bash
cd presentation/images

# bg-python.jpg — code on dark monitor (Pankaj Patel)
curl -L -o bg-python.jpg "https://images.unsplash.com/photo-1518773553398-650c184e0bb3?w=1920&q=80"

# bg-zen.jpg — zen stones stacked on dark background
curl -L -o bg-zen.jpg "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1920&q=80"

# bg-security.jpg — matrix-style green code on black
curl -L -o bg-security.jpg "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1920&q=80"

# bg-ai-coding.jpg — dark blue blueprint/grid (Claudio Guglieri)
curl -L -o bg-ai-coding.jpg "https://images.unsplash.com/photo-1759210358926-4673cc44d35f?w=1920&q=80"

# bg-cycle.jpg — abstract dark rings/circles
curl -L -o bg-cycle.jpg "https://images.unsplash.com/photo-1558591710-4b4a1ae0f04d?w=1920&q=80"

# bg-developer.jpg — developer at monitors in dark room
curl -L -o bg-developer.jpg "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1920&q=80"

# bg-rocket.jpg — SpaceX Falcon 9 night launch (Bill Jelen)
curl -L -o bg-rocket.jpg "https://images.unsplash.com/photo-1530447920184-b88c8872?w=1920&q=80"
```

**License**: All Unsplash photos are free for commercial use (Unsplash License). No attribution required.

**Selection criteria**: Dark background, no bright whites/pastels, thematically related to the slide topic, looks good at 10-15% opacity on the dark navy gradient.

### TIOBE screenshots (static fallback)

Used only if Highcharts CDN is unavailable or for PDF export:

1. Navigate to tiobe.com/tiobe-index/
2. Dismiss the cookie dialog
3. Screenshot the top-10 ranking table → `tiobe-ranking.png`
4. Screenshot the historical trend chart → `tiobe-chart.png`

---

## Reusable Libraries Reference

### `lib/typewriter.js`
- **What**: Character-by-character code typing animation preserving syntax highlighting
- **Trigger**: `<pre class="typewriter-code" data-speed="25"><code class="language-python">`
- **Options**: `data-speed` (ms/char, default 25), `data-delay` (ms before start, default 300), `data-cursor` (true/false)
- **Behavior**: Captures highlighted HTML after highlight.js runs, clears content, types char-by-char on slide entry. Tags (span etc.) are added instantly. Newlines pause 3x, spaces 0.5x. Cursor blinks in cyan (#00d2ff).
- **Dependencies**: reveal.js (listens for `slidechanged`/`ready` events), highlight.js (for syntax coloring)

### `lib/tiobe-chart.js`
- **What**: Interactive Highcharts spline chart with TIOBE data, dark theme
- **Trigger**: `<div id="tiobe-chart" style="width:100%; height:320px;"></div>`
- **Behavior**: Auto-initializes when containing slide becomes active. Python line is thicker (3 vs 1.5). Hover dims other series. Tooltip shows date + percentage.
- **Dependencies**: Highcharts CDN, `lib/tiobe-data.js`
- **Export**: `window.initTiobeChart(containerId)` for manual use

### `lib/tiobe-data.js`
- **What**: Raw TIOBE Index data extracted from tiobe.com (Feb 2026)
- **Content**: `TIOBE_SERIES` global array with 10 series (Python, C, C++, Java, C#, JavaScript, Visual Basic, R, SQL, Delphi/Object Pascal), each with ~293 data points (timestamp, percentage) from 2001 to 2026.
- **Size**: ~60KB
- **To update**: Visit tiobe.com, extract `Highcharts.charts[0].series` data via browser console (see `references/tiobe-feb-2026.md` for extraction code)

---

## Reference Materials

Summaries of Jfokus 2026 talks that inspired the presentation narrative. Source PDFs in `jfokus/`.

### `references/dan-north-bssn.md`
- **Talk**: Dan North — "Best Simple System for Now" (Jfokus 2026 keynote, 22 slides)
- **Key quotes used in slides**: "Look for the essence of the problem", Gall's Law, Randy Shoup on over-engineering
- **Concepts**: BSSN, CUPID (alternative to SOLID), Esencia vs Accidente (Brooks), "Just Start"
- **Used in**: Slide 2 (opening quote, philosophy), Slide 15 (closing quote)

### `references/arun-gupta-sdd.md`
- **Talk**: Arun Gupta (JetBrains) — "Spec-Driven Development Using Coding Agents" (32 slides)
- **Key quotes used in slides**: "Run slow to run fast", "Separate thinking from doing", "AI amplifies what you already have" (DORA 2025)
- **Concepts**: SDD workflow, 3 separations, 7 properties of reusable specs, AGENTS.md
- **Used in**: Slide 12 (SDD quote), Slide 13 (the loop)

### `references/marcus-hellberg-fullstack.md`
- **Talk**: Marcus Hellberg (Vaadin) — "Full-stack Web Apps, 100% Java" (19 slides)
- **Key quotes**: "Full-stack teams ship quality software faster", "Everything is a component"
- **Data**: 98% productivity increase, 45% time saved, 39% cost savings (Vaadin community survey)
- **Used in**: Background context (same philosophy as PyFlow, different language)

### `references/tiobe-feb-2026.md`
- **Data**: TIOBE Programming Community Index, February 2026
- **Key stats**: Python #1 at 21.81%, >10 points ahead of C (#2), peaked at 26.98% in July 2025
- **Includes**: Extraction code for updating `lib/tiobe-data.js`
- **Used in**: Slide 3 (stats row + interactive chart)
