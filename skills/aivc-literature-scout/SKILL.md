---
name: aivc-literature-scout
description: Use when the user wants a recent literature sweep for Awesome-Virtual-Cell, especially for latest papers, Nature-family journals, major labs, big groups, or a time-bounded update of what the README is missing.
---

# AIVC Literature Scout

Find recent, high-signal candidate items before final curation for `Awesome-Virtual-Cell`.

This skill is for scouting and shortlist building. After scouting, use `aivc-curator` to decide final placement and README-ready wording.

## When to Use

Use this skill when the user asks:
- what recent papers are missing from the repo
- what to add from the last 6 to 24 months
- what Nature-family papers to track
- what major labs or groups have recently published
- for a shortlist before editing `README.md`

Do not use this skill as the main workflow when the user:
- already has one specific item and only wants an inclusion decision
- wants repository structure advice rather than literature updates
- wants direct notebook or plotting recommendations

## Workflow

1. Read `references/literature-scout-rules.md`.
2. Read the relevant parts of `README.md` to understand the current coverage and avoid duplicate scouting.
3. Infer the search frame:
   - time window
   - topic emphasis
   - venue emphasis
   - lab or group emphasis
4. Search primary sources first and de-duplicate by title, DOI, acronym, and repo or project name.
5. Build a shortlist grouped into:
   - add now
   - maybe or hold
   - already listed
   - skip
6. For each `add now` or `maybe` item, include:
   - canonical title
   - venue and year
   - primary link
   - one-line relevance to AIVC
   - likely README section
7. If the user wants README edits, show the shortlist first and wait for approval before writing.
8. Default to Chinese unless the user is writing in English.

## Output Contract

Prefer this compact structure:

```text
检索范围：
- 时间：
- 重点：

建议优先补充：
- 标题：
- 来源：
- 建议位置：
- 理由：
- 主链接：

可选补充：
- ...

已在 README：
- ...

建议跳过：
- ...
```

For English requests, use:

```text
Search frame:
- Time window:
- Emphasis:

Add now:
- Title:
- Source:
- Suggested section:
- Why it matters:
- Primary link:

Maybe:
- ...

Already listed:
- ...

Skip:
- ...
```

## Quality Rules

- Prefer primary-source links and recent exact dates when the user asks for the latest work.
- Prefer a short, high-signal shortlist over a noisy dump.
- Treat Nature-family journals and major-lab releases as priority buckets, not automatic inclusion.
- Separate scouting from curation: finding a paper does not automatically mean it belongs in the README.

## Reference Map

Load only the files needed for the current scouting task:

- `references/literature-scout-rules.md` -> source priority, venue focus, major-lab checklist, and shortlist rules
- `README.md` -> current repo coverage and duplicate checks
- `skills/aivc-curator/references/aivc-curation-rules.md` -> final fit and placement criteria when the task moves from scouting to curation
