# TIOBE Programming Community Index — February 2026

Data captured from tiobe.com/tiobe-index/ on February 15, 2026.

---

## Top 10 Rankings (Feb 2026)

| Rank | Language | Rating | Change (YoY) |
|------|----------|--------|---------------|
| 1 | Python | 21.81% | — |
| 2 | C | 11.05% | — |
| 3 | C++ | 8.55% | — |
| 4 | Java | 8.12% | — |
| 5 | C# | ~6% | — |
| 6 | JavaScript | ~4% | — |
| 7 | Visual Basic | ~3% | — |
| 8 | R | ~2.5% | — |
| 9 | SQL | ~2% | — |
| 10 | Delphi/Object Pascal | ~2% | — |

### Key Takeaway
- **Python leads by >10 percentage points** over #2 (C)
- Python peaked at **26.98%** in July 2025
- Python has been #1 continuously since ~2021

---

## Historical Chart Data

Full time series data is stored in `lib/tiobe-data.js` (10 series, ~293 data points each, from 2001 to Feb 2026).

### Chart Series Colors (matching Highcharts original)

| Language | Color |
|----------|-------|
| Python | `#2caffe` |
| C | `#544fc5` |
| C++ | `#00e272` |
| Java | `#fe6a35` |
| C# | `#6b8abc` |
| JavaScript | `#d568fb` |
| Visual Basic | `#2ee0ca` |
| R | `#fa4b42` |
| SQL | `#feb56a` |
| Delphi/Object Pascal | `#91e8e1` |

---

## How Data Was Extracted

1. Navigated to tiobe.com/tiobe-index/ using Playwright
2. Dismissed cookie dialog via `document.getElementById('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()`
3. Extracted Highcharts data via browser console:
   ```javascript
   var chart = Highcharts.charts.find(c => c);
   var data = chart.series.map(s => ({
     name: s.name,
     color: s.color,
     data: s.data.map(p => [p.x, p.y])
   }));
   JSON.stringify(data);
   ```
4. Saved as `lib/tiobe-data.js` with `const TIOBE_SERIES = [...]`

### To Update
1. Visit tiobe.com/tiobe-index/
2. Open browser console
3. Run the extraction code above
4. Replace the array in `lib/tiobe-data.js`
5. Update the stats in SPECS.md (slide 3) and index.html

---

## Presentation Usage

### Slide 3 — "Why Python? Why Now?"
- Stats row: **21.81%** (Python, cyan glow) vs **11.05%** (C, muted gray)
- Interactive Highcharts chart below (320px height)
- Caption: "The most popular language in the world has no full-stack web framework"

### The Argument
Python is the #1 language by a massive margin. Django, Flask, and FastAPI serve APIs, but they all need JavaScript for the frontend. There is no server-side UI framework (like Vaadin) for Python. PyFlow fills that gap.

---

## Static Fallback Images

If Highcharts CDN is unavailable or for PDF export:
- `images/tiobe-ranking.png` — Screenshot of the top-10 ranking table
- `images/tiobe-chart.png` — Screenshot of the historical trend chart

Both captured from tiobe.com on the same date.
