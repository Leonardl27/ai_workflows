# Annotated CLAUDE.md Walkthrough

This is a line-by-line breakdown of an effective CLAUDE.md file for a Python web API project. Each section is annotated with *why* it works.

---

## The Full Example

```markdown
# CLAUDE.md — Inventory API

## Project Overview
FastAPI service managing product inventory. Connects to PostgreSQL
via SQLAlchemy. Deployed on AWS ECS with GitHub Actions CI/CD.

## Role
You are a senior Python backend engineer. Prioritize correctness,
clear error messages, and test coverage.

## Tech Stack
- Python 3.12, FastAPI, SQLAlchemy 2.0, Pydantic v2
- PostgreSQL 15, Redis for caching
- pytest, httpx for testing

## Code Style
- Use type hints on all function signatures
- Pydantic models for all request/response schemas
- Repository pattern for database access (see src/repositories/)
- Keep endpoint functions thin — business logic goes in src/services/

## Testing
- Every new endpoint needs integration tests in tests/api/
- Use factory_boy fixtures (see tests/conftest.py)
- Test happy path + at least one error case

## Constraints
- Do not add new pip dependencies without discussion
- Do not modify alembic migrations after they've been committed
- Keep functions under 25 lines
- No print statements — use the configured logger

## Common Tasks
### Adding a new endpoint
1. Create Pydantic models in src/schemas/
2. Add repository method in src/repositories/
3. Add service function in src/services/
4. Create endpoint in src/api/routes/
5. Write tests in tests/api/
```

---

## Section-by-Section Breakdown

### Project Overview

```markdown
## Project Overview
FastAPI service managing product inventory. Connects to PostgreSQL
via SQLAlchemy. Deployed on AWS ECS with GitHub Actions CI/CD.
```

**Why it works:** Two sentences that orient the agent. It now knows the framework, database, ORM, and deployment target — enough to make informed decisions about patterns and tradeoffs.

### Role

```markdown
## Role
You are a senior Python backend engineer. Prioritize correctness,
clear error messages, and test coverage.
```

**Why it works:** "Senior Python backend engineer" activates relevant expertise. The three priorities (correctness, error messages, tests) tell the agent what to optimize for when making tradeoffs. See [Principle 2: Assign a Role](../../../docs/principles.md#2-assign-a-role).

### Tech Stack

```markdown
## Tech Stack
- Python 3.12, FastAPI, SQLAlchemy 2.0, Pydantic v2
```

**Why it works:** Version numbers matter. SQLAlchemy 1.x and 2.0 have very different APIs. Pydantic v1 vs v2 changes model syntax. Without this, the agent may generate code for the wrong version.

### Code Style

```markdown
## Code Style
- Repository pattern for database access (see src/repositories/)
- Keep endpoint functions thin — business logic goes in src/services/
```

**Why it works:** Points to existing patterns in the codebase. "See src/repositories/" tells the agent where to look for examples rather than inventing its own approach.

### Constraints

```markdown
## Constraints
- Do not modify alembic migrations after they've been committed
- No print statements — use the configured logger
```

**Why it works:** These prevent specific, known failure modes. Without the migrations constraint, an agent might "fix" a migration instead of creating a new one. See [Principle 3: Set Constraints](../../../docs/principles.md#3-set-constraints).

### Common Tasks

```markdown
## Common Tasks
### Adding a new endpoint
1. Create Pydantic models in src/schemas/
2. Add repository method in src/repositories/
...
```

**Why it works:** Step-by-step workflows for repeated tasks. The agent follows this sequence instead of guessing the project's conventions. This is the highest-leverage section — it turns implicit team knowledge into explicit instructions.
