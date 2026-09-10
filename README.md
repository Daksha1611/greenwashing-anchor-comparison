# Greenwashing Detection: Do Different Ways of Measuring It Agree?

Business Economics project — a review of five papers on detecting **greenwashing**
(companies claiming to be greener than they are) in corporate sustainability
disclosures, and whether the different published ways of measuring it actually
identify the same companies.

## → Main deliverable: [`REPORT.md`](REPORT.md)

The single consolidated report: what greenwashing is and why it's hard to
measure, each paper explained in plain language, the specific gap between them,
the project idea that fills it, and the datasets a future implementation would
need. **Start there.**

The files below are the supporting material behind the report. Every note is
written in plain language, and technical terms are explained the first time they
show up. See [`GLOSSARY.md`](GLOSSARY.md) for a quick reference.

## The core idea in one paragraph

To catch greenwashing you need to compare what a company **says** against what it
**does**. The "says" half is easy — score the sustainability report. The "does"
half is the hard part, and published research has picked three different answers:
government **fines**, measured **carbon emissions**, or **press coverage**. Some
papers check against nothing at all. Everybody picks one and stops, and **nobody
has checked whether they agree.** If ranking companies by fines gives a different
worst-offenders list than ranking them by press coverage, then at least one of
these published methods isn't measuring greenwashing — it may just be measuring
how visible a company is.

## The five papers

| # | Short name | What it does | Reality anchor | Notes |
|---|------------|--------------|----------------|-------|
| 1 | **GSI / ESG Disclosure** (Davidescu et al., 2026) | Builds a Greenwashing Severity Index for 204 Central & Eastern European firms from sustainability reports and news. We found its published formula contains no news component at all. | **None** (media claimed) | [notes/01](notes/01-davidescu-2026-gsi.md) |
| 2 | **Identifying Greenwashing with NLP** (Gorovaia & Makrominas, 2025) | Splits US firms by whether they've been fined for environmental violations, then reads their reports. Polluters write longer, more positive, less readable reports — and change their writing right after getting caught. | **Violations** | [notes/02](notes/02-gorovaia-makrominas-2025-violations.md) |
| 3 | **Environmental Scores as a Greenwashing Tool** (Peng et al., 2024) | Checks the environmental scores of 199 Fortune Global 500 firms against their actual carbon emissions. Higher scores go with *more* pollution, not less. | **Emissions** | [notes/03](notes/03-peng-2024-emissions.md) |
| 4 | **Deep Learning Greenwashing Index** (Wang, Gao & Sun, 2025) | Uses an AI language model to read Chinese company reports sentence by sentence, separating vague aspiration from concrete verifiable action. | **None** (by design) | [notes/04](notes/04-wang-2025-deep-learning-index.md) |
| 5 | **Mapping the Research Landscape** (Forliano et al., 2025) | Systematic review of 97 articles. Maps the field's theories and themes — useful for context, though it maps theories rather than measurement methods. | n/a (review) | [notes/05](notes/05-forliano-2025-landscape.md) |

## Synthesis

- [`synthesis/comparison.md`](synthesis/comparison.md) — the papers side by side: sample, reality anchor, method, headline result.
- [`synthesis/gsi-formula.md`](synthesis/gsi-formula.md) — full step-by-step reconstruction of Paper 1's index, separating what we verified from what isn't recoverable.
- [`synthesis/datasets-and-access.md`](synthesis/datasets-and-access.md) — the six data sources, with access notes, limits and available fields.
- [`synthesis/open-questions.md`](synthesis/open-questions.md) — the gap written as testable hypotheses, plus the full experimental design.

## Common thread

All five papers point toward the same conclusion:

> Companies that talk greener frequently perform worse. This has been shown twice
> over, independently, against pollution fines and against measured carbon
> emissions. But the tools built to detect greenwashing are increasingly scored
> against the company's own words rather than against reality, and more disclosure
> has not produced more honesty. If a detection method rewards polished writing
> and heavy press coverage rather than actual conduct, it repeats the problem it
> was built to expose.

## What we found while reviewing

Paper 1 is generally treated as the standard media-based greenwashing index, and
that is how we treated it when we started. Working through the methodology, we
found that its published formula contains no media component at all: all three
inputs come from the company's own report. The index measures how densely a report
is packed with ESG vocabulary, not any gap between what a company claims and how
the press describes it.

We checked our reading by recalculating the authors' own published figures, which
match exactly, so this is not a misunderstanding on our part. The working is in
[`synthesis/gsi-formula.md`](synthesis/gsi-formula.md).

This sharpens the research question rather than weakening it, but it changes what
we can claim. We build our own media-based measure and set it out in full, rather
than presenting it as a replication of theirs.

## The PDFs

All five papers are in [`papers/`](papers/); see
[`papers/SOURCES.md`](papers/SOURCES.md) for full citations, DOIs and links.

Three of the citations needed correcting against the PDFs. The clearest case is
Paper 2, which has exactly two authors rather than "et al.", and belongs to 2025
rather than 2024. Paper 1 is published by MDPI, and `SOURCES.md` records its
indexing status, which is worth knowing given how much this project relies on it.

## How to use these notes

Read [`REPORT.md`](REPORT.md) first — it's self-contained and explains the whole
idea from scratch. Then, if you want depth on a particular paper, go to its note.
[`synthesis/comparison.md`](synthesis/comparison.md) is the fastest way to see
how the five relate to each other.

## Status

**Literature review complete.** Notes, synthesis and report written.

**Experiments — not started.** This repository is the review and design phase.
No data has been retrieved and no index has been computed.
