# Pattern 03: Automation Workflows

**Integrate AI agents into CI/CD pipelines for automated code review, documentation, and quality checks.**

---

## The Problem

AI coding agents are typically used interactively — a developer asks a question, gets a response. But many valuable AI tasks are repetitive and predictable: reviewing PRs for common issues, checking documentation freshness, validating commit messages. Running these manually wastes developer time.

## How It Works

Use GitHub Actions (or any CI/CD system) to trigger AI-powered checks automatically on events like pull requests, pushes, or scheduled intervals.

The general pattern:

1. **Trigger** — a CI event fires (PR opened, code pushed, cron schedule)
2. **Context** — the workflow gathers relevant code, diffs, or metadata
3. **Prompt** — a structured prompt sends the context to an AI model
4. **Action** — the AI's response becomes a PR comment, check result, or issue

```
PR opened → Gather diff → Send to AI with review prompt → Post review comment
```

## When to Use This

- **PR review augmentation** — catch issues before human review starts
- **Documentation checks** — flag outdated docs when related code changes
- **Commit message validation** — enforce conventions beyond what linters catch
- **Security scanning** — supplement traditional SAST with AI-powered analysis
- **Release note generation** — summarize changes between tags

## When to Skip This

- Tasks requiring deep architectural understanding (AI review is a supplement, not a replacement)
- Repositories with very high PR volume where API costs would be significant
- Security-critical decisions that require human sign-off regardless

## Limitations

- **Cost** — API calls on every PR add up; use filters to skip trivial changes
- **Latency** — AI review adds seconds to minutes; run it in parallel with other checks
- **False positives** — AI suggestions need human judgment; present them as comments, not blocking checks
- **Context limits** — large diffs may need to be split or summarized before sending to the model

## Examples

- [`ai-code-review.yml`](examples/ai-code-review.yml) — GitHub Actions workflow that reviews PRs using the Anthropic API

## See Also

- [Prompt templates](../01-markdown-driven-agents/examples/prompt-templates.md#1-code-review) — the review prompt template used in the workflow
- [Core Principles](../../docs/principles.md) — specificity in prompts is especially important for automation (no human in the loop to clarify)
