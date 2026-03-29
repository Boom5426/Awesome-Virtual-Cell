---
name: aivc-curator
description: Use when the user wants to judge whether a paper, dataset, benchmark, blog, or related resource belongs in Awesome-Virtual-Cell, whether an existing README entry should be updated, where an item should be placed, or how it should be written in house style.
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
2. If the task is about a concrete item, check whether the same work already appears in `README.md` by title, alias, acronym, DOI, or project name.
3. Extract the item type:
   - overview paper
   - research paper
   - dataset
   - benchmark or challenge
   - report or blog
   - video or talk
   - historical or foundational work
   - related resource
4. Extract the maintenance action:
   - new entry
   - update existing entry
   - duplicate or no-op
   - demote, move, or remove
5. Verify the minimum metadata needed for a reliable call:
   - canonical title
   - venue and year
   - primary link
   - optional code, dataset, benchmark, or project link
6. Judge fit against the repository’s scope:
   - core AIVC
   - adjacent but useful
   - weakly related or out of scope
7. Return a structured decision with:
   - include / update-existing / hold / exclude
   - suggested section
   - core vs related
   - duplicate status
   - short rationale
   - exact fields to correct if the recommendation is `update-existing`
   - missing information to verify if the call is uncertain
   - suggested README entry text if inclusion is recommended
8. If the user asks about a borderline item, explain the boundary instead of forcing a confident decision.
9. Default to Chinese unless the user is writing in English.

## Output Contract

Prefer this compact structure:

```text
收录建议：
- 结论：收录 / 更新现有 / 暂缓 / 不收录
- 建议位置：
- 属性：主线 / Related
- 重复检查：

理由：
- ...

若更新现有：
- 需要修改：

还需要确认：
- ...

建议条目写法：
- ...
```

For English requests, use:

```text
Decision:
- Recommendation: include / update-existing / hold / exclude
- Suggested section:
- Placement: core / related
- Duplicate check:

Rationale:
- ...

If updating existing:
- Fields to fix:

Still needed:
- ...

Suggested README entry:
- ...
```

## Quality Rules

- Follow the repository’s current `Scope` and `Inclusion Rules`, not personal preference.
- Prefer primary-source links and higher-confidence resources.
- Prefer updating an existing entry over adding a near-duplicate.
- If something is useful but off the main path, prefer `Related Resources` over forced placement in the core sections.
- Be conservative with low-confidence sources, broken links, or overly generic biomedical AI resources.
- When recommending inclusion, keep the suggested entry concise and aligned with the README’s existing format.

## Reference Map

Load only the files needed for the current curation task:

- `references/aivc-curation-rules.md` -> executable scope, placement rules, in-scope boundaries, and entry-writing patterns for this repository
- `README.md` -> duplicate checks, existing wording, year buckets, and section placement
- `CONTRIBUTING.md` -> contributor-facing submission expectations when the user asks how to submit or format changes
