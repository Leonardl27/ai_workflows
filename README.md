# AI Workflows

**Practical patterns for directing AI agents with structured markdown files.**

Inspired by [Ethan Mollick's](https://www.oneusefulthing.org/) research on working with AI — this repository collects proven patterns for getting reliable, high-quality output from AI coding agents. The repo itself is a living example: its own [CLAUDE.md](CLAUDE.md) directs AI contributors using the same patterns it teaches.

---

## Why This Matters

AI coding agents (Claude Code, Copilot, Cursor) are powerful but unpredictable without structure. The difference between mediocre and excellent AI output usually isn't the model — it's the instructions.

This repo demonstrates how to:
- **Direct AI agents** using markdown configuration files
- **Refactor code** with AI as a reliable collaborator
- **Automate workflows** by integrating AI into CI/CD pipelines

---

## Patterns

| # | Pattern | What You'll Learn |
|---|---------|-------------------|
| 01 | [Markdown-Driven Agents](patterns/01-markdown-driven-agents/) | Use `.md` files as agent configuration — the core technique |
| 02 | [Refactoring with AI](patterns/02-refactoring-with-ai/) | Structure AI-assisted refactoring for consistent results |
| 03 | [Automation Workflows](patterns/03-automation-workflows/) | Integrate AI agents into GitHub Actions and CI/CD |

Each pattern includes a README explaining the concept and an `examples/` folder with working artifacts.

---

## Quick Start

**Browse the patterns** — each is self-contained with its own README and examples.

**Use the templates** to bootstrap AI workflows in your own projects:
- [`templates/CLAUDE.md.template`](templates/CLAUDE.md.template) — Starter instructions file for any project
- [`templates/agent-prompt.md.template`](templates/agent-prompt.md.template) — Reusable prompt structure

**Read the principles** — [`docs/principles.md`](docs/principles.md) covers the foundational ideas behind all the patterns.

---

## Further Reading

- [Ethan Mollick's Substack](https://www.oneusefulthing.org/) — Research on AI collaboration
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code) — CLAUDE.md reference
- [GitHub Copilot Custom Instructions](https://docs.github.com/en/copilot/customizing-copilot) — Similar patterns for Copilot
