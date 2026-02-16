# Implementation Plan — reveal.js Presentation

Generic, reusable plan. Re-run after any change to `SPECS.md`.

---

## Prerequisites

- `presentation/SPECS.md` exists with slide definitions and design tokens
- `presentation/images/` has required images (or symlinks)
- Internet access for reveal.js CDN (or local copy)

---

## Step 1: Parse SPECS.md

Read `SPECS.md` and extract:

1. **Design Language** section — CSS tokens (background, accent, text colors, fonts, code block bg)
2. **reveal.js theme** section — base theme name and custom CSS overrides
3. **Slides** section — each `### N. Title` block:
   - Layout hint (centered, two-column, cards, full-slide image, etc.)
   - Content: headings, bullets, quotes, code blocks, image references, captions
   - Which items are fragments (`class="fragment"`)
   - Speaker notes (`<aside class="notes">`)
4. **Fragment / Animation Guidelines** — fragment classes, transition style
5. **Images Needed** table — filenames, sources, tips

---

## Step 2: Prepare images

For each image listed in the **Images Needed** table:

1. If source says `../docs/...` → symlink or copy into `presentation/images/`
2. If source says **NEW** → either:
   - Capture screenshot with Playwright MCP (`browser_navigate` + `browser_take_screenshot`)
   - Or mark as placeholder (`<!-- TODO: capture image -->`)
3. Verify images look good on the dark background specified in Design Language
4. Use 16:9 aspect ratio where possible

---

## Step 3: Scaffold `index.html`

Create `presentation/index.html` with this structure:

```
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[from slide 1 title]</title>
  <link rel="stylesheet" href="[reveal.js CDN]/dist/reveal.css">
  <link rel="stylesheet" href="[reveal.js CDN]/dist/theme/[base theme from SPECS].css">
  <link rel="stylesheet" href="[reveal.js CDN]/plugin/highlight/monokai.css">
  <style>
    /* Custom CSS from SPECS.md "reveal.js theme" section */
    /* Paste verbatim */
  </style>
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <!-- slides go here -->
    </div>
  </div>
  <script src="[reveal.js CDN]/dist/reveal.js"></script>
  <script src="[reveal.js CDN]/plugin/highlight/highlight.js"></script>
  <script src="[reveal.js CDN]/plugin/notes/notes.js"></script>
  <script>
    Reveal.initialize({
      hash: true,
      transition: 'slide',
      plugins: [RevealHighlight, RevealNotes]
    });
  </script>
</body>
</html>
```

Use CDN: `https://cdn.jsdelivr.net/npm/reveal.js@5/`

---

## Step 4: Generate slides

For each slide in SPECS.md (numbered `### N. Title`), create a `<section>`:

### Layout mapping

| SPECS layout | HTML pattern |
|--------------|-------------|
| **Centered, big impact** | `<section>` with centered content, large headings |
| **Left-aligned, quote-driven** | `<section style="text-align:left">` with `<blockquote>` |
| **Two columns** | `<div style="display:flex; gap:2em">` with two `<div style="flex:1">` children |
| **3 cards in a row** | `<div style="display:flex; gap:1.5em">` with 3 card `<div>`s |
| **Full-slide image** | `<img>` with overlay text using absolute positioning or background-image |
| **Diagram + bullets** | Two columns or image + list |

### Content mapping

| SPECS element | HTML |
|---------------|------|
| Heading with `**bold**` | `<h2>` or `<h3>` |
| `gradient-text` | `<span class="gradient-text">` |
| Bullet list (fragments) | `<ul>` with `<li class="fragment">` |
| Quote block | `<blockquote>` |
| Python code block | `<pre><code data-trim data-noescape class="language-python">` |
| Terminal block | `<pre><code data-trim class="language-bash">` |
| Image reference | `<img src="images/filename.png" alt="...">` |
| Caption / subtitle italic | `<p><em>text</em></p>` |
| Speaker notes | `<aside class="notes">text</aside>` |

### Per-slide checklist

For each slide:
- [ ] Correct `<section>` with layout
- [ ] All text content from SPECS
- [ ] Fragments applied to bullet items
- [ ] Code blocks with correct language class
- [ ] Images referenced with correct path
- [ ] Speaker notes included
- [ ] No content invented — strictly from SPECS

---

## Step 5: Style polish

1. **Custom CSS** — Copy the CSS block from SPECS.md "reveal.js theme" section into `<style>`
2. **Card styling** — If slides use cards, add:
   ```css
   .card {
     background: rgba(255,255,255,0.05);
     border-radius: 12px;
     padding: 1.5em;
     border: 1px solid rgba(255,255,255,0.1);
   }
   .card h3 { margin-top: 0; }
   ```
3. **Image sizing** — Screenshots should be max 500-600px wide in two-column layouts, full width in single-column
4. **Code block sizing** — `font-size: 0.55em` for code blocks to fit on slide
5. **Quote styling** — Styled blockquotes with left border
6. **Logo styling** — Centered logo on title slide, small logo on closing slide

---

## Step 6: Verify

Open in browser and check:

1. `python -m http.server 8001` from `presentation/`
2. Navigate to `http://localhost:8001`
3. **Overview mode** — Press `Esc` to see all slides as grid
4. **Navigation** — Arrow keys, spacebar work
5. **Fragments** — Bullet points reveal one at a time
6. **Code highlighting** — Python syntax colored
7. **Images** — All load, no broken references
8. **Speaker notes** — Press `S` to open notes window
9. **Responsive** — Resize window, slides scale properly
10. **PDF export** — Append `?print-pdf`, Cmd+P, check layout

### Automated verification with Playwright MCP

```
browser_navigate → http://localhost:8001
browser_snapshot → verify slide structure
browser_press_key → "ArrowRight" (repeat for each slide)
browser_take_screenshot → capture each slide for review
```

---

## Re-run Protocol

When SPECS.md changes:

1. Re-read SPECS.md (Step 1)
2. Update/add/remove images (Step 2)
3. Regenerate `index.html` from scratch or diff against existing (Steps 3-4)
4. Re-apply style polish (Step 5)
5. Re-verify (Step 6)

The plan reads SPECS.md dynamically — no slide content is hardcoded here.
