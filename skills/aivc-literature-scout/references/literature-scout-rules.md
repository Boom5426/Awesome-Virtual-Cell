# AIVC Literature Scout Rules

Use this file to gather recent candidate items for `Awesome-Virtual-Cell` before final curation.

## Search Priorities

Prioritize these source classes in order:

1. official journal pages
2. official preprint pages
3. official project or lab pages
4. official code or dataset repositories

Prefer primary links over summaries, social posts, or secondary commentary.

## Default Search Windows

If the user does not specify a time window:

- default to the last 12 to 18 months for update requests
- widen to 24 months only when the repo likely has a recent coverage gap
- narrow to 3 to 6 months when the user asks for the latest work

## Priority Venue Buckets

Treat these as high-priority scans:

- Nature
- Nature Biotechnology
- Nature Methods
- Nature Genetics
- Nature Cell Biology
- Nature Communications
- Nature Computational Science
- Nature Biomedical Engineering
- Cell
- Cell Genomics
- Cell Research

Strong preprints are still in scope when they are clearly field-shaping or come with credible code, data, or project pages.

## Major-Lab / Group / Researcher Heuristics

Check these groups or named researchers when the user asks for big labs, major groups, or specific people:

- Arc Institute
- Chan Zuckerberg Initiative
- Genentech
- Broad Institute
- Satija Lab
- Theis Lab
- Recursion
- Stanford SNAP
- Yosef Lab
- Gerstein Lab
- Emma Lundberg

Do not force these groups into every search. Use them as emphasis buckets when relevant.

When the user asks for protein, subcellular localization, cell imaging, image-based proteomics, spatial proteomics, or morphology-heavy work, treat Emma Lundberg as a priority scan target.

## Candidate Checklist

For each candidate item, try to capture:

- canonical title
- venue and year
- primary link
- optional code, dataset, or project link
- why it matters for AIVC
- whether it appears in `README.md` already
- likely section: overview, research, datasets and benchmarks, reports/blogs, videos, historical, related

## De-Duplication Rules

Before surfacing a candidate as new, check:

- exact title match
- acronym or label match
- DOI match
- repo or project name match
- title variants across preprint and published versions

If a work is already present, mark it `already listed` unless the better recommendation is to update metadata.

## Shortlist Rules

Use these buckets:

- `add now` -> strong candidate and likely in scope
- `maybe` -> relevant but needs a curation decision or more metadata
- `already listed` -> present in the repo already
- `skip` -> weak fit, low credibility, or duplicate without useful new information

## Handoff to Curation

After scouting, hand off to `aivc-curator` when the user wants:

- inclusion vs exclusion
- exact section placement
- core vs related judgment
- README-ready entry text
- update-existing vs duplicate decisions
