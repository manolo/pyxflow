# Marcus Hellberg — "Full-stack Web Apps, 100% Java"

**Jfokus 2026** | Vaadin (@marcushellberg) | 19 slides

---

## Summary

Marcus Hellberg presents Vaadin as the answer to web development fragmentation. The premise: full-stack teams using a single language ship quality software faster. Vaadin eliminates the need for JavaScript, REST APIs, and serialization contracts — everything is Java (or, as PyFlow demonstrates, any server-side language).

---

## Key Quotes

> "What if frontend development didn't need to be so difficult?"

> "Full-stack teams ship quality software faster."

> "Everything is a component."

> "98% reported an increase in productivity, 45% time saved on development, 39% cost savings." (Vaadin community survey)

---

## Talk Structure

### 1. The Problem: DIY Stack vs Full-Stack
- **DIY stack**: Components, Frontend, Communication, Backend — each piece is separate, different vendors, different languages
- **Full-stack**: Everything integrated under one umbrella — more productivity, less friction
- Horizontal axis: Control ←→ Productivity

### 2. The Principle: "Everything is a component"
- `new Button("Click me")` → rendered button
- `new DatePicker()` → complete calendar
- `new Grid<Employee>()` → data table with virtual scrolling
- No HTML, no CSS, no JS — just Java objects

### 3. Layouts compose the UI
- `VerticalLayout` stacks components vertically
- `HorizontalLayout` arranges them horizontally
- Freely nested → declarative composition
- `@Route("hello")` maps a class to a URL

### 4. Events for interaction
- `button.addClickListener(e -> ...)` — Java lambdas
- The server handles the event, updates the UI, sends diff to browser
- The browser is a thin client — no business logic

### 5. Speed run: Vaadin live
- Live demo building an app step by step
- TextField + Button + Grid in minutes
- Code + visual result side by side

### 6. Apache 2.0
- Vaadin is open source (Apache 2.0 license)
- Slide with "Apache 2.0" in large text — clear message that it's free

### 7. Closing with humor
- Jim Carrey meme (Bruce Almighty) — reaction to the simplicity
- QR to `github.com/marcushellberg/full-stack-java-2026`
- Team photo at the Jfokus booth wearing Viking helmets

---

## Survey Data

| Metric | Result |
|--------|--------|
| Productivity increase | 98% reported |
| Time saved | 45% |
| Cost savings | 39% |

---

## Concepts That Apply to PyFlow

- **"Everything is a component"** — Exactly the same API in Python: `Button("Click me")`, `Grid()`, `DatePicker()`
- **Full-stack without JavaScript** — PyFlow takes it further: you don't even need Java
- **Thin client architecture** — Same model as Vaadin Flow: server maintains state, browser renders diffs
- **The same 49 web components** — PyFlow reuses the Vaadin bundle, it doesn't reimplement the components
- **Apache 2.0** — Same open source philosophy
