# Marcus Hellberg — "Full-stack Web Apps, 100% Java"

**Jfokus 2026** | Vaadin (@marcushellberg) | 19 slides

---

## Summary

Marcus presents Vaadin as the solution to frontend complexity. The premise: full-stack teams ship quality software faster. If you can do everything in a single language (Java), you eliminate friction between frontend and backend, API contracts, and the need for JS specialists.

---

## Key Quotes

> "What if frontend development didn't need to be so difficult?"

> "Full-stack teams ship quality software faster."

> "Everything is a component." — `new Button("Click me");` and that's it.

> "98% reported an increase in productivity. 45% time saved on development. 39% cost savings." (Vaadin community survey)

---

## Core Concepts

### The Problem: DIY Stack vs Full-Stack
- **DIY stack** (left side): Components + Frontend + Communication + Backend — each layer is independent, chosen separately, integrated manually
- **Full-stack** (right side): Everything integrated in a single framework — fewer decisions, less friction
- Horizontal axis: Control ←→ Productivity. Vaadin sits at the productivity extreme.

### "Everything is a component"
- `new Button("Click me");` → renders a real button in the browser
- `new DatePicker();` → complete interactive calendar
- `new Grid<Employee>();` → data table with sorting, lazy loading
- No HTML, no CSS, no JS. Just Java.

### Layouts compose views
- `VerticalLayout` — stacks components vertically
- `HorizontalLayout` — arranges them horizontally
- They nest: `VerticalLayout(HorizontalLayout(Button, Button), Button)`
- `@Route("hello")` maps a URL to a Java class

### Events for interaction
```java
var name = new TextField("Your name");
var button = new Button("Say hello");
button.addClickListener(e -> {
    add(new Paragraph("Hello, " + name.getValue()));
});
```

### Apache 2.0 License
- Fully open source framework

---

## Productivity Data (Vaadin Community Survey)

| Metric | Value |
|--------|-------|
| Productivity increase reported | 98% |
| Time saved in development | 45% |
| Cost savings | 39% |

---

## The Demo: "Vaadin Speed Run"

Marcus does a speed run building a complete app live:
1. Hello World with `@Route` + `VerticalLayout` + `H1`
2. TextField + Button with event listener
3. Immediate visual result in the browser

Meme reference: Jim Carrey scene (Bruce Almighty) — "It's good!" when something works on the first try.

---

## Application to PyFlow

This presentation is the Java version of exactly what PyFlow does in Python. The same components (`Button`, `TextField`, `Grid`, `DatePicker`), the same philosophy ("everything is a component"), the same layout model (`VerticalLayout`, `HorizontalLayout`), and the same promise ("full-stack in one language"). PyFlow simply swaps Java for Python, with the same API and the same web components.

Marcus's key phrase — "What if frontend development didn't need to be so difficult?" — is identical to PyFlow's promise, just for the Python ecosystem.
