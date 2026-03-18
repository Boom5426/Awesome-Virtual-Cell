---
name: aivc-curator
description: Use when the user wants to judge whether a paper, dataset, benchmark, blog, or related resource belongs in Awesome-Virtual-Cell, where it should be placed, or how it should be written as a README entry.
---

# AIVC Curator

Help maintainers make consistent inclusion and placement decisions for `Awesome-Virtual-Cell`.

This skill is repository-specific. It should apply the current README scope and inclusion rules rather than generic biology curation instincts.

## When to Use

Use this skill when the user asks:
- whether a paper should be included
- whether a dataset, benchmark, report, or video is in scope
- where an item should live in the README
- whether something is core or only related
- how to write a new README entry in the current house style

Do not use this skill as the main workflow when the user:
- wants general advice on building an awesome project
- wants broad README structure redesign
- needs a live literature search without a curation decision

## Workflow

1. Read `references/aivc-curation-rules.md`.
2. Extract the item type:
   - overview paper
   - research paper
   - dataset
   - benchmark or challenge
   - report or blog
   - video or talk
   - historical or foundational work
   - related resource
3. Judge fit against the repository’s scope:
   - core AIVC
   - adjacent but useful
   - weakly related or out of scope
4. Return a structured decision with:
   - include / hold / exclude
   - suggested section
   - core vs related
   - short rationale
   - missing information to verify if the call is uncertain
   - suggested README entry text if inclusion is recommended
5. If the user asks about a borderline item, explain the boundary instead of forcing a confident decision.
6. Default to Chinese unless the user is writing in English.

## Output Contract

Prefer this compact structure:

```text
收录建议：
- 结论：收录 / 暂缓 / 不收录
- 建议位置：
- 属性：主线 / Related

理由：
- ...

还需要确认：
- ...

建议条目写法：
- ...
```

For English requests, use:

```text
Decision:
- Recommendation: include / hold / exclude
- Suggested section:
- Placement: core / related

Rationale:
- ...

Still needed:
- ...

Suggested README entry:
- ...
```

## Quality Rules

- Follow the repository’s current `Scope` and `Inclusion Rules`, not personal preference.
- Prefer primary-source links and higher-confidence resources.
- If something is useful but off the main path, prefer `Related Resources` over forced placement in the core sections.
- Be conservative with low-confidence sources, broken links, or overly generic biomedical AI resources.
- When recommending inclusion, keep the suggested entry concise and aligned with the README’s existing format.

## Reference Map

Load only this file unless the task expands beyond curation:

- `references/aivc-curation-rules.md` -> executable scope, placement rules, in-scope boundaries, and entry-writing patterns for this repository
