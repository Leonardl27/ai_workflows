# Prompt Templates

Reusable prompt structures for common AI-assisted development tasks. Copy, fill in the bracketed placeholders, and use with any AI coding agent.

---

## 1. Code Review

```markdown
Review this code for:
- [ ] Security vulnerabilities (injection, auth bypass, data exposure)
- [ ] Error handling gaps (unhandled exceptions, missing validation)
- [ ] Performance issues (N+1 queries, unnecessary allocations, missing indexes)

Context: [What the code does and where it runs — e.g., "public-facing API
endpoint handling payment processing, ~500 req/s"]

Focus on issues that could cause production incidents. Skip style nits.
```

**When to use:** Before merging PRs, especially for security-sensitive or performance-critical code paths.

---

## 2. Refactoring

```markdown
Refactor [target — e.g., "the UserService class"] with these goals:
- [Goal 1 — e.g., "Separate database logic from business logic"]
- [Goal 2 — e.g., "Make the class testable without a database connection"]

Constraints:
- Keep the public API unchanged — [list callers if known]
- Do not introduce new dependencies
- [Any other constraints]

Show me the plan before writing code.
```

**When to use:** When code works but is hard to maintain, test, or extend. Asking for the plan first prevents large, unwanted rewrites.

---

## 3. Test Generation

```markdown
Write tests for [function/class name] covering:
- Happy path: [describe expected normal behavior]
- Edge cases: [list specific edges — e.g., "empty input, single item, maximum size"]
- Error cases: [list error conditions — e.g., "network timeout, invalid ID format"]

Use [test framework — e.g., "pytest"] and follow the patterns in [path to existing tests].
Match the existing test style — do not introduce new test utilities.
```

**When to use:** When adding test coverage to existing code. Pointing to existing test files ensures consistency.

---

## 4. Debug Investigation

```markdown
I'm seeing [symptom — e.g., "intermittent 500 errors on the /orders endpoint"].

What I know:
- [Fact 1 — e.g., "Started after deploying commit abc123"]
- [Fact 2 — e.g., "Only happens under high load"]
- [Fact 3 — e.g., "Logs show 'connection pool exhausted'"]

Relevant files: [list files or directories]

Walk me through likely root causes, ranked by probability.
Do not suggest fixes yet — just help me understand the problem.
```

**When to use:** When you need a systematic investigation rather than a quick fix. Separating diagnosis from treatment prevents premature solutions.

---

## Template Structure

All four templates follow the same underlying structure:

1. **Task** — what you want done (one clear sentence)
2. **Scope** — what to focus on (checklist or bullet points)
3. **Context** — what the agent needs to know (environment, constraints, history)
4. **Format** — how you want the output (plan first, ranked list, specific test framework)

This structure maps directly to the [principles](../../../docs/principles.md): specificity (task + scope), context (background info), and constraints (what *not* to do).
