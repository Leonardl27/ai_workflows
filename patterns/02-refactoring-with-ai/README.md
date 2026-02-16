# Pattern 02: Refactoring with AI

**Structure AI-assisted refactoring so results are predictable, reviewable, and safe.**

---

## The Problem

Asking an AI to "refactor this code" produces unpredictable results. The agent might rename everything, change the public API, add unnecessary abstractions, or refactor different things than you intended. Without structure, AI refactoring is a gamble.

## How It Works

Break refactoring into a structured conversation:

### Step 1: Describe the target state

Tell the agent what the code should look like *after* refactoring, not just that it needs refactoring.

```
Refactor process_order() to separate these concerns:
1. Input validation → private method
2. Price calculation → pure function (no side effects)
3. Database writes → repository layer
Keep the function signature unchanged.
```

### Step 2: Ask for a plan before code

```
Show me your refactoring plan before writing code.
List which functions you'll create, move, or modify.
```

This catches misunderstandings before they become a 500-line diff.

### Step 3: Constrain the scope

```
Constraints:
- Only modify files in src/orders/
- Do not change any function signatures in __init__.py
- Do not add new dependencies
```

### Step 4: Review incrementally

For large refactors, ask the agent to work in stages rather than producing one massive change. Each stage should leave the code in a working state.

## When to Use This

- Functions over 50 lines that mix multiple concerns
- Code that's hard to test because of tight coupling
- Repeated patterns that could be consolidated
- Before adding new features to messy code (refactor first, then extend)

## When to Skip This

- Code that's already well-structured — don't refactor for refactoring's sake
- Hot paths where you need manual performance control
- Generated code (ORM migrations, protobuf stubs) — refactoring these causes drift from the generator

## Examples

The `examples/` folder contains a before/after pair showing a realistic refactoring:

- [`before.py`](examples/before.py) — A data processing function with mixed concerns, magic numbers, poor error handling, and no testability
- [`after.py`](examples/after.py) — The same logic refactored into clean, testable components with inline commentary explaining each decision

## See Also

- [Refactoring prompt template](../01-markdown-driven-agents/examples/prompt-templates.md#2-refactoring) — reusable prompt for structuring refactoring requests
- [Core Principles](../../docs/principles.md) — specificity and constraints are key to good refactoring prompts
