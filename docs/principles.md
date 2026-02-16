# Principles for Directing AI Agents

These principles are drawn from [Ethan Mollick's](https://www.oneusefulthing.org/) research on working with AI, adapted for software engineering workflows.

---

## 1. Be Specific, Not Vague

AI agents perform dramatically better with concrete instructions than with open-ended requests.

| Vague | Specific |
|-------|----------|
| "Clean up this code" | "Refactor this function to separate data fetching from rendering. Keep the public API unchanged." |
| "Write tests" | "Write unit tests for the `calculate_total` function covering: empty input, single item, discount applied, and tax calculation." |
| "Review this PR" | "Check this PR for: SQL injection risks, missing error handling on API calls, and functions exceeding 30 lines." |

**Why it works:** Specificity reduces the space of possible outputs, making the AI more likely to produce what you actually need.

## 2. Assign a Role

Giving the AI a role activates relevant knowledge and sets the appropriate tone.

```markdown
You are a senior backend engineer reviewing code for production readiness.
Focus on error handling, performance, and security.
```

Effective roles are **specific to the task** — "senior backend engineer" is better than "helpful assistant" because it implies a particular set of priorities and standards.

## 3. Set Constraints

Constraints prevent common failure modes: over-engineering, scope creep, and stylistic drift.

Examples of useful constraints:
- "Do not add new dependencies"
- "Keep functions under 20 lines"
- "Use existing patterns in the codebase — do not introduce new architectural concepts"
- "If a change would touch more than 3 files, stop and explain your approach first"

**Constraints are the most underused tool in AI prompting.** They are cheap to add and dramatically reduce the chance of unwanted output.

## 4. Provide Context, Not Just Instructions

AI agents work best when they understand the *why* behind a request.

```markdown
## Context
This is a high-traffic API endpoint (10k req/s). The current implementation
makes a database call on every request. We need to add caching, but cache
invalidation must be correct — stale data here causes billing errors.

## Task
Add Redis caching to the `get_pricing` endpoint with a 5-minute TTL.
Invalidate on any write to the `pricing` table.
```

Context helps the agent make better tradeoff decisions when the instructions don't cover every edge case.

## 5. Iterate, Don't Restart

When AI output isn't right, refine rather than starting over. Each iteration gives the agent more signal about what you want.

**First attempt:** "Refactor this class."
**Refinement:** "Good direction, but keep the constructor signature unchanged — other modules depend on it."
**Refinement:** "The `process` method is still too long. Split the validation logic into a private method."

This works because the agent retains context across the conversation. Three targeted refinements typically produce better results than one perfectly crafted prompt.

## 6. Structure Your Instructions as Files

When you find yourself giving the same instructions repeatedly, move them into a file. This is the core idea behind [Pattern 01: Markdown-Driven Agents](../patterns/01-markdown-driven-agents/).

Benefits:
- **Consistency** — every session starts with the same baseline
- **Iteration** — you can refine instructions over time
- **Shareability** — team members get the same agent behavior
- **Version control** — instructions evolve with your codebase

---

## Putting It Together

These principles compound. A well-structured instructions file (Principle 6) that assigns a role (Principle 2), provides project context (Principle 4), sets constraints (Principle 3), and includes specific examples (Principle 1) will consistently produce better results than any single prompt, no matter how clever.
