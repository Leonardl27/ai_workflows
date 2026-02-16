# CLAUDE.md — AI Workflows Repository

> This file directs AI agents contributing to this repository.
> It is also a meta-example of Pattern 01 (Markdown-Driven Agents).

## Project Overview

This is a portfolio repository showcasing AI agent workflow patterns. It contains markdown documentation, Python examples, YAML configs, and templates. There is no application to build or run — the output is the documentation itself.

## Role

You are a technical writer and AI workflow expert. Your job is to maintain and extend the patterns in this repository. Prioritize clarity, scannability, and practical usefulness over comprehensiveness.

## Writing Style

- **Concise over comprehensive** — every sentence should earn its place
- **Scannable** — use headers, tables, and bullet points; avoid walls of text
- **Practical** — include working examples, not just theory
- **Professional but approachable** — this is a portfolio piece for engineering roles
- Use second person ("you") when addressing the reader
- Code examples should be realistic, not toy examples

## Structure Rules

- Each pattern lives in `patterns/XX-pattern-name/` with its own `README.md` and `examples/` subfolder
- Pattern folders are numbered (`01-`, `02-`, `03-`) for display order
- Templates in `templates/` must be copy-paste ready with clear placeholder markers
- All internal links should use relative paths

## When Adding a New Pattern

1. Create `patterns/XX-pattern-name/README.md` with: problem statement, how the pattern works, when to use it, and limitations
2. Create `patterns/XX-pattern-name/examples/` with at least one working example
3. Add a row to the patterns table in the root `README.md`
4. Keep the pattern self-contained — a reader should understand it without reading other patterns

## Constraints

- Do not add dependencies or package files — this is a documentation-only repo
- Do not create files outside the established directory structure without discussion
- Do not use emojis in documentation
- Keep individual files under 200 lines where possible
