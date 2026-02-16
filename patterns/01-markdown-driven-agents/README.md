# Pattern 01: Markdown-Driven Agents

**Use structured markdown files to configure AI agent behavior consistently across sessions.**

---

## The Problem

AI coding agents start every session as a blank slate. You end up repeating the same instructions: "use our coding style," "don't add dependencies," "follow the existing patterns." The agent's output quality depends on whether you remembered to include the right context.

## How It Works

Instead of giving instructions ad-hoc, you write them into a markdown file that the agent reads at the start of every session.

```
your-project/
├── CLAUDE.md          # Instructions for Claude Code
├── .cursorrules       # Instructions for Cursor
├── .github/copilot-instructions.md  # Instructions for Copilot
└── src/
```

The file typically includes:
- **Project overview** — what the codebase does, key technologies
- **Role definition** — what kind of expert the agent should act as
- **Style rules** — coding conventions, documentation standards
- **Constraints** — what the agent should *not* do
- **Workflow instructions** — how to approach specific task types

The agent reads this file automatically (or you reference it), and every interaction starts from a consistent baseline.

## When to Use This

- You work with AI agents regularly on the same codebase
- Multiple people use AI agents on the same project
- You find yourself repeating the same instructions across sessions
- You want to version-control your AI workflow alongside your code

## When to Skip This

- One-off tasks or throwaway scripts
- Exploratory conversations where you want maximum flexibility
- Projects too small to have established conventions

## Limitations

- Instructions files can become stale if not maintained alongside the code
- Overly long files may be partially ignored due to context window limits
- Different AI tools use different file names and formats (no universal standard yet)

## Examples

- [Annotated CLAUDE.md walkthrough](examples/claude-md-annotated.md) — line-by-line breakdown of a real instructions file
- [Prompt templates](examples/prompt-templates.md) — reusable templates for common tasks

## See Also

- [Core Principles](../../docs/principles.md) — the foundational ideas behind this pattern
- [CLAUDE.md Template](../../templates/CLAUDE.md.template) — copy-paste starter for your own project
