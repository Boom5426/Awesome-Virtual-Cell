# Awesome Guidelines

Use this file when helping a maintainer design or improve an awesome-style repository.

## What a Good Awesome Repository Does

A strong awesome repository is not just a pile of links. It should:

- tell new users what the repository is about within a few seconds
- make scope boundaries obvious
- help users decide where to start
- group resources in ways that reduce scanning cost
- keep entries consistent enough to skim quickly
- stay maintainable as the list grows

## Entry Layer

Large curated repositories should usually have a short entry layer near the top:

- one-sentence description
- `Contents`
- `Scope`
- `Inclusion Rules`
- optional `Start Here` or `How to Use This List`

This layer matters most when:

- the repository has many sections
- newcomers are a target audience
- the topic is broad or ambiguous

## Section Design

Prefer sections based on user goals, not only on source type.

Good patterns:

- overview or start-here resources first
- core resources before peripheral ones
- datasets and benchmarks separated from papers when they serve different user workflows
- related resources pushed down rather than mixed into the main line

Common section types:

- Overview / Start Here
- Research Papers
- Datasets and Benchmarks
- Reports / Blogs / Media
- Videos / Talks
- Historical / Foundational Works
- Related Resources
- Contributing / License

## Inclusion and Exclusion Rules

Curated lists get stronger when they explicitly say what belongs.

Good inclusion rules usually answer:

- what is in scope
- what is adjacent but acceptable
- what is usually out of scope
- what kinds of links count as primary or high-confidence

Typical exclusions:

- weakly related resources
- broken or placeholder links
- low-confidence secondary sources
- repetitive items that add little beyond stronger existing entries

## Entry Template Patterns

Pick one entry template and keep it stable.

Good entry fields often include:

- short label or project name
- title
- venue and year
- paper / code / dataset / project links only when useful
- optional lightweight tag if it helps browsing

Good properties:

- concise
- skimmable
- consistent across a section

Bad properties:

- too many bracket types
- too many link variants per item
- inconsistent capitalization
- labels that do not help the reader decide whether to click

## Newcomer-Friendly Patterns

If a repository feels hard for new users, these fixes usually matter more than adding content:

- bring the main path closer to the top
- add a short “start here” subsection
- move background or historical material lower
- reduce default cognitive load
- prefer fewer, clearer sections over many subtle ones

When a list is broad, recommend a reading path such as:

- first read overview resources
- then browse core papers or tools
- then move to datasets and benchmarks

## Contribution Guidance

Large curated repositories should usually include:

- what kinds of contributions are welcome
- what minimum metadata to provide
- how maintainers judge inclusion
- formatting expectations for new entries

This keeps the repository from drifting into inconsistent styles.

## Common Failure Modes

### 1. Resource Dump

Symptoms:
- long flat lists
- little prioritization
- hard to know where to begin

Fix:
- add an entry layer
- reorder sections
- surface a small start-here path

### 2. Scope Blur

Symptoms:
- core and adjacent material mixed together
- readers cannot tell what the repository is really about

Fix:
- tighten `Scope`
- add `Related Resources`
- write clear inclusion rules

### 3. Over-Classification

Symptoms:
- too many categories
- items are hard to place consistently
- maintainers spend too much effort classifying edge cases

Fix:
- use lighter tags
- keep fewer main sections
- classify by user need first

### 4. Formatting Drift

Symptoms:
- entries look different from one another
- different link labels for the same resource type
- noisy markdown

Fix:
- define one entry template
- normalize link labels
- remove low-value formatting

### 5. Weak Newcomer Path

Symptoms:
- expert maintainers can use the list, but new users cannot
- important overview materials are buried

Fix:
- put overview content earlier
- add “start here”
- describe intended browsing paths

## Recommendation Bias

When proposing changes:

- prefer the smallest restructuring that noticeably improves usability
- keep user mental models stable
- do not rebuild everything if section order and entry rules would solve most problems
- push weakly related material downward before deleting it
