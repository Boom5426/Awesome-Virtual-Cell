# AIVC Curation Rules

Use this file to make inclusion, placement, and entry-writing decisions for `Awesome-Virtual-Cell`.

## Core Repository Intent

`Awesome-Virtual-Cell` is for resources that help readers understand, model, benchmark, or build AI-powered virtual cells and closely related cellular foundation models.

The repository is broad, but it is not a generic biomedical AI list.

## Executable Scope

Treat these as core or near-core topic areas:

- virtual cell perspectives and roadmaps
- perturbation modeling
- single-cell and multimodal foundation models
- spatial and morphology modeling when clearly tied to cellular systems
- biological AI agents when they materially connect to virtual cell workflows
- datasets, benchmarks, and challenges that support the above
- community resources closely connected to the field

Usually acceptable as adjacent but not core:

- broad biological AI infrastructure that directly supports cell modeling workflows
- foundation-model work that is not explicitly virtual-cell branded but is clearly useful for cellular representation learning
- reports or discussions that materially help readers navigate the space

Usually out of scope:

- generic biomedical AI with weak cell-modeling relevance
- sources with low credibility or unclear provenance
- broken links or placeholder entries
- items whose only relevance is very indirect

## Inclusion Rules in Practice

Prefer:

- peer-reviewed papers
- high-signal preprints
- official project pages
- official code or dataset links
- Chinese summaries only as secondary links, never as the primary source

Be cautious with:

- vague perspectives without a strong virtual-cell tie
- marketing-style project pages with no paper or usable artifact
- unrelated biology agent demos
- duplicate items that do not add new value

## Core vs Related

Mark an item as core when it strongly advances one of the repository’s main lines:

- AIVC roadmaps and perspectives
- perturbation response prediction
- single-cell foundation models
- spatial or morphology modeling for cell-state understanding
- benchmark and evaluation work directly tied to these tasks

Mark an item as related when:

- it is useful but not central
- it mainly supports adjacent workflows
- it belongs in the reader’s peripheral awareness rather than the main path

If you are unsure, prefer `Related Resources` over forcing a weak or non-paper-shaped item into the main paper flow.

### `[Related]` Inside `Research Papers`

This repository already uses a lightweight `[Related]` tag inside `Research Papers` for paper-shaped items that are:

- still worth seeing inline while browsing papers
- adjacent to the main path rather than central
- better understood next to nearby methods or models than in a generic resource bucket

Prefer `[Related]` inside `Research Papers` when the item is still a credible paper that helps readers scan the field.

Prefer `Related Resources` instead when:

- the item is not primarily a paper entry
- it is too peripheral for the main paper flow
- it is better treated as infrastructure, commentary, or a general pointer

## Section Placement Rules

### Overview Papers

Use for:

- high-level perspectives
- roadmaps
- major field overviews
- pieces that help a new reader understand why the area matters

Do not use for:

- ordinary method papers
- datasets or benchmarks

### Research Papers

Use for:

- method papers
- model papers
- evaluation papers tightly linked to modeling
- strong preprints or peer-reviewed core research items

Keep the main emphasis on:

- virtual cell
- perturbation
- foundation models
- spatial and morphology modeling
- agent-related work with clear cellular relevance

### Datasets and Benchmarks

Use for:

- curated datasets
- perturbation atlases
- challenge datasets
- benchmark suites
- evaluation frameworks and competitions

If the main contribution is evaluation or data infrastructure rather than a model, this section is usually a better fit than `Research Papers`.

### Reports and Blogs

Use for:

- institutional reports
- community summaries
- high-signal commentary
- blog posts that help readers orient themselves in the space

Avoid using this section for low-credibility commentary or thin rewrites of primary sources.

### Videos

Use for:

- talks
- lectures
- conference videos
- explainers that have real educational value for the topic

### Historical and Foundational Works

Use for:

- earlier background papers
- foundational methods that still matter for understanding the field
- older resources that provide important context but are not current AIVC work

### Related Resources

Use for:

- adjacent resources that a serious reader may still want
- broad biological AI resources with clear but not central relevance
- useful tools or resources that are not strong enough for the main sections

## Item-Type Heuristics

### Papers

Include when:

- the paper clearly advances a main topic
- the venue or preprint quality is credible
- the connection to virtual cell or cellular modeling is defensible

Hold when:

- the relevance is plausible but weak
- the source is too new or too unclear
- the link or artifact quality needs verification

Exclude when:

- the paper is mostly generic biomedical AI
- the cellular connection is superficial

Update existing instead of adding when:

- the same paper is already present under another label, acronym, or title variant
- the current entry exists but the venue, year, title, or primary link is stale
- the new suggestion mostly adds missing code, dataset, or project links to an existing item

### Datasets

Include when:

- the dataset can realistically support perturbation, cell-state, multimodal, spatial, or related modeling
- the source is official and reusable

Hold when:

- the dataset exists but access or provenance is unclear

Exclude when:

- it is too generic or not meaningfully tied to cell modeling workflows

### Benchmarks and Challenges

Include when:

- the benchmark evaluates relevant modeling tasks
- the challenge materially shapes how readers think about evaluation in the field

Exclude when:

- the benchmark is too generic or not cell-focused enough

### Reports, Blogs, and Media

Include when:

- they help readers understand the field, institutions, trends, or community direction
- they add value beyond simply restating a paper abstract

Exclude when:

- they are low-confidence commentary
- they are clearly promotional without informational value

## Entry Writing Rules

Align suggested entries with the current README style:

- start with a short bracketed label when it helps scanning
- add lightweight tags only in `Research Papers` when useful
- `[Related]` is allowed inside `Research Papers` for adjacent but still useful papers
- keep venue and year concise
- prefer `paper`, `code`, `dataset`, `project`, `homepage`, `video`, or `中文解读` style labels
- avoid overlong annotation inside the entry itself

## Duplicate and Maintenance Checks

Before recommending a new entry, check for existing coverage by:

- exact title
- common acronym or short label
- DOI
- project or code repository name

If the work already exists, prefer one of these maintenance outcomes:

- `update-existing` -> correct title, venue, year, or links
- `duplicate/no-op` -> no README change needed
- `move` -> keep the item but relocate it to a better section
- `demote` -> keep it but mark `[Related]` or move it to `Related Resources`

Suggested entry pattern for research items:

```text
- **[Label]** `[Tag]` Title (**Venue Year**) [[paper](...)] [[code](...)]
```

Suggested entry pattern for datasets:

```text
- **[Label]** Title (**Venue Year**) [[paper](...)] [[dataset](...)] [[code](...)]
```

Suggested entry pattern for reports or blogs:

```text
- **[Label]** Title (**Source Year**) [[media](...)] [[中文解读](...)]
```

## Decision Bias

- If the item is clearly useful but not central, route it to `Related Resources`.
- If the item is clearly useful, paper-shaped, and already fits the paper flow, a `[Related]` tag inside `Research Papers` is acceptable.
- If the item is central but the evidence is incomplete, return `hold` and state what needs verification.
- If the user asks for a README-ready entry, give one concise draft instead of multiple variants.
- If an item would force the repository’s scope to drift, exclude it even if it is broadly interesting.
