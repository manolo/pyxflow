# Arun Gupta — "Spec-Driven Development Using Coding Agents"

**Jfokus 2026** | JetBrains (VP, Developer Experience) | 32 slides

---

## Summary

Arun Gupta argues that "vibe coding" (prompt-and-pray) is a dead end for serious projects. The alternative: **Spec-Driven Development (SDD)** — writing clear specifications before AI generates code. Separate thinking from doing. The human defines the WHAT, agents solve the HOW.

---

## Key Quotes

> "Vibe coding generates code based upon your vibe. You need an intention-first, code-second approach."

> "Run slow to run fast." — Invest in specs to accelerate delivery.

> "Separate thinking from doing: define intent before implementation."

> "Human judgment defines 'what,' AI efficiency delivers 'how.'"

> "The blueprint is the source of truth."

> "AI amplifies what you already have — make sure you're amplifying the right things." (citing DORA 2025)

> "SDD is writing down what your AI should know (AGENTS.md), what it should do (skills), and what you're building (implementation plan), so you can stop explaining and start building."

---

## The Problem: Vibe Coding

- No structure, no planning
- Hallucinated files, codebase misunderstandings
- Ignores corporate standards
- Hard to extend, review, or change
- "Nearly impossible to safely change once the original mental model is gone"
- Analogy: "Just build me something cool for grilling" — BBQ arrives but there's no space in the stone

---

## The Solution: Spec-Driven Development

Write specs in natural language that define:
- **Intent**: desired behavior
- **Interfaces**: contracts between components
- **Requirements**: functional and non-functional
- **Acceptance criteria**: Gherkin format (Given-When-Then)

Review and refine specs independently from the implementation. Agents generate and validate code against the specs.

---

## The SDD Workflow

```
Specs (Define WHAT) → Agents (Define HOW) → Human-in-the-loop (Oversees)
```

### The 3 Separations of SDD
1. Separate thinking from doing → Specs define "what", agents define "how"
2. Separate strategy from tactics → Review specs (strategic), not lines of code (tactical)
3. Separate patterns from projects → Build portable skills, not single-use prompts

### The 3 Practices That Matter
1. Invest upfront, accelerate delivery → "Run slow to run fast"
2. Build in phases with gates → Validate early, prevent drift
3. Let AI interview you → Better specs through collaboration

---

## DORA 2025 Report

"AI's primary role in software development is that of an amplifier. It magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones."

AI amplifies what you already have. If you have good practices, AI makes you better. If you have bad ones, it makes them worse.

---

## New SDLC with SDD

**Research** → **Standardize** → **Define** → **Loop**

1. Research: codebases, papers, interviews, dependencies
2. Standardize: rules (linting, ADRs), skills (prompts, templates), MCPs, structure
3. Define: scope, requirements, contracts (APIs, schemas), UI/UX, testing strategy
4. Loop: generation from specs, continuous validation, iterative refinement

---

## Practical Tools

- **AGENTS.md** — "README for agents". Persistent context. One file, multiple agents (Claude, GPT, Gemini).
- **Agent Skills** — Portable, reusable engineering patterns across projects.
- **Figma MCP** — Design-to-agents bridge. Selection link → automatic ui-spec.md.

---

## 7 Properties of Reusable Specs

1. **Clear scope** — "in scope" vs "out of scope" prevents feature creep
2. **Documented ADRs** — Explicit decisions with justification
3. **Language-agnostic** — Behavior (what), not implementation (how)
4. **Structured requirements** — Functional and non-functional separated
5. **Contract-first** — JSON schemas defined upfront
6. **Acceptance criteria** — Testable conditions with WHEN/THEN
7. **Tech stack recommendations** — Guidance without prescription

---

## Lessons Learned

- **Agent drift is real** — Agents deviate, over-implement, ignore scope
- **Test-first validation gates** — Tests must exist and pass before marking something complete
- **Capture patterns as Agent Skills** — Reusable across projects
- **Every spec subsection needs test cases** — Defined explicitly, not assumed

---

## Application to PyFlow

The PyFlow project follows exactly this pattern: specs written first (PROTOCOL.md, PITFALLS.md, COMPONENTS.md), agents generate Python from the specs, 28 pitfalls documented prevent days of debugging, and the specs are reusable for porting Flow to any language.
