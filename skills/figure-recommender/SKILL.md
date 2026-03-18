---
name: figure-recommender
description: Use when the user wants help choosing a scientific chart type, matching a data-storytelling goal to a figure, or finding the right notebook template in Awesome-Scientific-Figures.
---

# Figure Recommender

Recommend chart types and reference notebooks for users working with the figures curated in this repo.

This skill is for recommendation only. It does not replace notebook editing, data cleaning, or full plotting tutorials.

## When to Use

Use this skill when the user:
- does not know which chart type fits their data
- wants 1 to 3 figure options for a paper, report, or exploratory analysis
- wants the best matching notebook under `Awesome-Scientific-Figures/`
- asks whether a specific chart type is appropriate

Do not use this skill as the primary workflow when the user:
- already chose a notebook and wants code edits
- wants debugging for a plotting script or notebook
- wants a full tutorial on Matplotlib, Seaborn, or Jupyter

## Workflow

1. Read `references/figure-recommender.md`.
2. Infer these signals from the request:
   - data type
   - storytelling goal
   - variable structure
   - whether there are groups, time, hierarchy, network relations, or rankings
   - use case: paper figure, supplement, slide deck, or exploration
   - whether the user prefers readability or stronger visual styling
3. If one or two signals are missing but the intent is still clear, make a reasonable assumption and say it briefly.
4. If the request is too underspecified to choose responsibly, ask a short follow-up question before recommending.
5. Recommend at most 3 chart types.
6. For each recommendation, include:
   - chart type
   - exact repo-relative reference file path
   - one short reason tied to the user's goal
7. When there is a common mismatch, include one `Not recommended` / `不推荐` item.
8. If the request is in English, answer in English. Otherwise default to Chinese.

## Output Contract

Keep the answer compact. Prefer this structure:

```text
推荐图种 1：
- 图种：
- 参考文件：
- 适合原因：

推荐图种 2：
- 图种：
- 参考文件：
- 适合原因：

可选图种 3：
- 图种：
- 参考文件：
- 适合原因：

不推荐：
- 图种：
- 原因：
```

For English requests, use:

```text
Recommended figure 1:
- Figure type:
- Reference file:
- Why it fits:

Recommended figure 2:
- Figure type:
- Reference file:
- Why it fits:

Optional figure 3:
- Figure type:
- Reference file:
- Why it fits:

Not recommended:
- Figure type:
- Why not:
```

## Quality Rules

- Prefer readable, mainstream figures for new users.
- Do not recommend style-heavy charts unless the user clearly values presentation style or the data structure truly needs them.
- Prefer one strong recommendation over three weak ones.
- Keep notebook paths exact, for example `Awesome-Scientific-Figures/热力图.ipynb`.
- If the best answer is "use a simple chart first", say that directly.

## Reference Map

Load only this file unless the task expands beyond recommendation:

- `references/figure-recommender.md` -> chart-selection rules, notebook mapping, anti-patterns, and bilingual cue words
