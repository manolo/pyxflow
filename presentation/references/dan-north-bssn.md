# Dan North — "Best Simple System for Now" (BSSN)

**Jfokus 2026** | Keynote | 22 slides

---

## Summary

Dan North presents a development philosophy based on finding the **essence** of each problem, rather than accumulating complexity. The talk revolves around the idea that "simple" is not a fixed property: it depends on the current context. What was complex yesterday may be simple today if the context has changed.

---

## Key Quotes

> "Look for the essence of the problem — not what is there, but what should be there."

> "A complex system that works is invariably found to have evolved from a simple system that worked." — John Gall (Gall's Law)

> "If you don't end up regretting your early technology decisions, you probably over-engineered." — Randy Shoup

---

## Core Concepts

### BSSN = Best Simple System for Now
- Don't try to design the perfect system from the start
- Design for what you know NOW
- Accept that you'll have to change it later
- "Now" is the key word — context changes everything

### Gall's Law
- Complex systems that work always evolved from simple systems that worked
- You can't design a complex system from scratch and expect it to work
- Start with something simple that works, then iterate

### CUPID (Dan North's alternative to SOLID)
- **C**omposable — small, focused units that combine well
- **U**nix philosophy — do one thing well, work with others
- **P**redictable — behaves as expected, no surprises
- **I**diomatic — follows the conventions of the language/framework
- **D**omain-based — models the problem domain, not the solution domain

### Essence vs Accident (Frederick Brooks)
- **Essential complexity**: inherent to the problem
- **Accidental complexity**: introduced by the solution
- The goal is to eliminate accidental complexity and keep only the essence

### "Just Start"
- Don't wait for the perfect design
- Start building and expect to be bad at first
- Iterate based on what you learn

---

## Application to PyFlow

The essence of Vaadin Flow is: **the server maintains a state tree, the browser is a thin client**. The 25 years of Java code are accidental complexity around that essence. PyFlow extracts that essence and reimplements it in Python.
