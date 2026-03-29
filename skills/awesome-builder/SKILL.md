---
name: awesome-builder
description: Use when the user wants to design, restructure, diagnose, or improve an awesome-style repository, especially when a curated README feels hard to browse, poorly scoped, or difficult for new users.
---

# Awesome Builder

Help users turn an awesome-style repository from a flat resource dump into a navigable, maintainable project.

This skill is maintainer-facing. It focuses on structure, usability, scope, and curation quality rather than item-level inclusion decisions for a specific repository.

## When to Use

Use this skill when the user asks about:
- how to build an awesome project
- how to restructure an awesome README
- why an awesome list feels hard to use
- how to improve onboarding, section layout, or contribution flow
- how to make a curated repository easier for new users

Do not use this skill as the main workflow when the user:
- wants to decide whether one specific item belongs in `Awesome-Virtual-Cell`
- needs a paper, dataset, or benchmark classified into an AIVC section
- wants live literature updates

## Workflow

1. Read the current `README.md` before giving structural advice.
2. Read `CONTRIBUTING.md` when contribution flow, formatting rules, or submission expectations are part of the problem.
3. Read `references/awesome-guidelines.md`.
4. Infer the repository’s current problem shape:
   - weak onboarding
   - unclear scope
   - poor section order
   - inconsistent entry formatting
   - too many flat items
   - weak contribution guidance
5. Diagnose before prescribing. Identify the top 2 to 5 problems first.
6. Recommend the smallest structural changes that materially improve usability.
7. Prefer repository-level guidance such as:
   - top-of-page entry layer
   - section reordering
   - inclusion and exclusion rules
   - entry template normalization
   - contribution flow improvements
8. Tie each recommendation to a concrete consequence in the current repo, not just a generic awesome-list principle.
9. Default to Chinese unless the user is writing in English.

## Output Contract

Prefer a compact maintainer-facing structure:

```text
主要问题：
- ...

建议调整：
- ...

推荐结构：
- ...

维护规则建议：
- ...
```

When the user asks for a more concrete rewrite plan, also include:

```text
最小改版路径：
1. ...
2. ...
3. ...
```

## Quality Rules

- Optimize for scanability, not maximal categorization.
- Prefer light taxonomy over rigid over-classification.
- Recommend a `Start Here` layer when the repository is large or newcomer-heavy.
- Keep section names stable and intuitive.
- Favor small, high-leverage changes before proposing a full rewrite.
- Anchor structural advice to the current `README.md` and `CONTRIBUTING.md`, not an imagined generic repo.

## Reference Map

Load only the files needed for the current design diagnosis:

- `README.md` -> current section order, entry layer, and navigation structure
- `CONTRIBUTING.md` -> contribution flow and submission expectations
- `references/awesome-guidelines.md` -> awesome-project structure patterns, anti-patterns, entry templates, and maintenance heuristics
