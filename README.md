# Greenwashing Detection: Do Different Ways of Measuring It Agree?

Business Economics project: a review of 24 papers on detecting **greenwashing** (companies
claiming to be greener than they are) in corporate sustainability disclosures, and whether the
different published ways of measuring it actually identify the same companies.

## → Main deliverables

- [`BE_Report.docx`](BE_Report.docx) / [`BE_Report.pdf`](BE_Report.pdf): the course report,
  laid out in the department's paper format (title block, Abstract and Index Terms, Roman-numeral
  sections, APA references). 14 pages. Figures are in [`figures/`](figures/).

## Team

Aastha Amit Goliwar (2024IMG-001), Aayush Shankar (2024IMG-002), Ayush Pratap Singh (2024IMG-010),
Daksha Mehta (2024IMG-015), Panchadarla Veditha Keerti Rani (2024IMG-030),
Siddharth Bisarya (2024IMG-502). Course instructor: Dr. Arun Kumar.

## Other material

- [`BE_Project.tex`](BE_Project.tex) / [`BE_Project.pdf`](BE_Project.pdf): the longer LaTeX version
  of the same review (30 pages), with a full write-up of each paper and the verification record.
- [`REPORT.md`](REPORT.md): the earlier plain-language report on the first five papers. It is
  self-contained and still the best place to start if you want the idea explained from scratch.

The files below are the supporting material behind the reports. Every note is written in plain
language, and technical terms are explained the first time they show up. See
[`GLOSSARY.md`](GLOSSARY.md) for a quick reference.

## The core idea in one paragraph

To catch greenwashing you need to compare what a company **says** against what it **does**. The
"says" half is easy: score the sustainability report. The "does" half is the hard part, and
published research has picked several different answers: government **fines**, measured
**carbon emissions**, a commercial **ratings gap** (a disclosure score minus a performance
score), **press coverage or controversies**, or nothing at all. Papers usually pick one and stop.
If ranking companies by fines gives a different worst-offenders list than ranking them by press
coverage, then at least one of these published methods isn't measuring greenwashing: it may just
be measuring how visible a company is.

## The refined gap

An earlier version of this repository said nobody had checked whether the measures agree. After
reading 19 more papers, that is too broad: some come close. Bingler et al. (2024) relate one
talk measure to both emissions and negative news, as separate correlates; Raghunandan & Rajgopal
(2022) compare ESG scores against violations and emissions; Gibson Brandon et al. (2021) compare
ESG raters with each other. So the claim is now:

> **As far as we found, no study builds several greenwashing indices on the same firms, each
> anchored to a different reality check, and tests whether they rank the same firms as worst.**

The hedge matters: fifteen of the nineteen new papers were read by abstract only (see
[`papers/SOURCES.md`](papers/SOURCES.md)).

## The first five papers

| # | Short name | What it does | Reality anchor | Notes |
|---|------------|--------------|----------------|-------|
| 1 | **GSI / ESG Disclosure** (Davidescu et al., 2026) | Builds a Greenwashing Severity Index for 204 Central & Eastern European firms from sustainability reports and news. We found its published formula contains no news component at all. | **None** (media claimed) | [notes/01](notes/01-davidescu-2026-gsi.md) |
| 2 | **Identifying Greenwashing with NLP** (Gorovaia & Makrominas, 2025) | Splits US firms by whether they've been fined for environmental violations, then reads their reports. Polluters write longer, more positive, less readable reports, and change their writing right after getting caught. | **Violations** | [notes/02](notes/02-gorovaia-makrominas-2025-violations.md) |
| 3 | **Environmental Scores as a Greenwashing Tool** (Peng et al., 2024) | Checks the environmental scores of 199 Fortune Global 500 firms against their actual carbon emissions. Higher scores go with *more* pollution, not less. | **Emissions** | [notes/03](notes/03-peng-2024-emissions.md) |
| 4 | **Deep Learning Greenwashing Index** (Wang, Gao & Sun, 2025) | Uses an AI language model to read Chinese company reports sentence by sentence, separating vague aspiration from concrete verifiable action. | **None** (by design) | [notes/04](notes/04-wang-2025-deep-learning-index.md) |
| 5 | **Mapping the Research Landscape** (Forliano et al., 2025) | Systematic review of 97 articles. Maps the field's theories and themes; useful for context, though it maps theories rather than measurement methods. | n/a (review) | [notes/05](notes/05-forliano-2025-landscape.md) |

## The 19 additional papers

Grouped by what they tell us. **Anchor** uses the types in
[`synthesis/comparison.md`](synthesis/comparison.md). † = a detail taken from our research brief
and not confirmed from the abstract. "Basis" shows whether we read the full text.

### A. Measuring the "talk" side (text and NLP)

| # | Paper | Publisher | Anchor | Basis | Note |
|---|---|---|---|---|---|
| 6 | Lagasio (2024), ESG-washing Severity Index | Elsevier | None (as far as the abstract shows) | Abstract | [06](notes/06-lagasio-2024-esgsi.md) |
| 7 | Bingler et al. (2024), cheap talk, initiatives, emissions, reputation | Elsevier | Talk, related to emissions and news separately | Abstract | [07](notes/07-bingler-2024-cheap-talk.md) |
| 8 | Bingler et al. (2022), ClimateBert on TCFD disclosures | Elsevier | None | **Full text** | [08](notes/08-bingler-2022-climatebert-tcfd.md) |
| 9 | Hrasky (2012), carbon footprints: symbolism or action? | Emerald | Sector carbon intensity | Abstract | [09](notes/09-hrasky-2012-symbolism-action.md) |

### B. Disclosure against measured performance

| # | Paper | Publisher | Anchor | Basis | Note |
|---|---|---|---|---|---|
| 10 | Clarkson et al. (2008), performance and disclosure | Elsevier | Emissions / pollution | Brief only † | [10](notes/10-clarkson-2008-performance-disclosure.md) |
| 11 | Tadros & Magnan (2019), mapping performance into disclosure | Emerald | Environmental performance | Abstract | [11](notes/11-tadros-magnan-2019-mapping.md) |
| 12 | Luu et al. (2025), GHGRP and greenwashing | Elsevier | Ratings gap, GHGRP as shock | **Full text** | [12](notes/12-luu-2025-ghgrp.md) |
| 13 | Cho et al. (2015), CSR disclosure: the more things change | Emerald | None (legitimacy factors) | Abstract | [13](notes/13-cho-2015-more-things-change.md) |

### C. The ratings-gap anchor

| # | Paper | Publisher | Anchor | Basis | Note |
|---|---|---|---|---|---|
| 14 | Yu, Luu & Chen (2020), greenwashing in ESG disclosures | Elsevier | Ratings gap | Brief only † | [14](notes/14-yu-2020-esg-greenwashing.md) |
| 15 | Liu et al. (2024), crash risk | Taylor & Francis | Ratings gap † | Abstract | [15](notes/15-liu-2024-crash-risk.md) |
| 16 | Dorfleitner & Utz (2024), conceptual framework | Springer | Multiple, combined | **Full text** | [16](notes/16-dorfleitner-utz-2024-framework.md) |

### D. Violations

| # | Paper | Publisher | Anchor | Basis | Note |
|---|---|---|---|---|---|
| 17 | Raghunandan & Rajgopal (2022), ESG funds | Springer | Violations + emissions | **Full text** | [17](notes/17-raghunandan-rajgopal-2022-esg-funds.md) |

### E. Media, controversy and events

| # | Paper | Publisher | Anchor | Basis | Note |
|---|---|---|---|---|---|
| 18 | Boiral (2013), sustainability reports as simulacra | Emerald | News events (manual) | Abstract | [18](notes/18-boiral-2013-simulacra.md) |
| 19 | Ghitti et al. (2024), the agency of greenwashing | Springer | Controversy † (**unverified**) | Abstract | [19](notes/19-ghitti-2024-agency.md) |
| 20 | Bacher et al. (2025), greenwashing risk in asset pricing | Taylor & Francis | Controversy † | Abstract | [20](notes/20-bacher-2025-asset-pricing.md) |
| 21 | Utz (2019), corporate scandals and ESG reliability | Springer | Scandal events | Brief only † | [21](notes/21-utz-2019-scandals.md) |
| 22 | Cho (2009), Total SA's legitimation | Taylor & Francis | Events (case-level) | Abstract | [22](notes/22-cho-2009-total.md) |

### F. Reliability of the measures themselves

| # | Paper | Publisher | Anchor | Basis | Note |
|---|---|---|---|---|---|
| 23 | Drempetic et al. (2020), firm size and the ESG score | Springer | n/a (rating bias) | Brief only † | [23](notes/23-drempetic-2020-size-bias.md) |
| 24 | Gibson Brandon et al. (2021), ESG rating disagreement | Taylor & Francis | n/a (compares raters) | Abstract | [24](notes/24-gibson-brandon-2021-disagreement.md) |

## Synthesis

- [`synthesis/comparison.md`](synthesis/comparison.md): all 24 papers side by side: sample, publisher, reality anchor, method, headline result; plus the anchor types ranked by strength.
- [`synthesis/extended-literature.md`](synthesis/extended-literature.md): the 19 new papers in six themes, **three contradictions** explained by anchor choice, and the refined gap.
- [`synthesis/combining-and-improvements.md`](synthesis/combining-and-improvements.md): twelve ways to combine the papers into a better design, each labelled as from a paper or our own proposal.
- [`synthesis/gsi-formula.md`](synthesis/gsi-formula.md): full step-by-step reconstruction of Paper 1's index, separating what we verified from what isn't recoverable.
- [`synthesis/datasets-and-access.md`](synthesis/datasets-and-access.md): the data sources, with access notes, limits and available fields.
- [`synthesis/open-questions.md`](synthesis/open-questions.md): the gap written as testable hypotheses (H1–H7), plus the full experimental design.

## Common thread

> Companies that talk greener frequently perform worse. This has been shown independently
> against pollution fines (Papers 2, 17) and against measured carbon emissions (Papers 3, 17).
> But many of the tools built to detect greenwashing are scored against the company's own words,
> or against a commercial rating that itself rises with firm size and with how much a firm
> discloses, rather than against conduct. If a detection method rewards polished writing and
> heavy press coverage rather than actual conduct, it repeats the problem it was built to expose.

## What we found while reviewing

Paper 1 is generally treated as the standard media-based greenwashing index, and that is how we
treated it when we started. Working through the methodology, we found that its published
formula contains no media component at all: all three inputs come from the company's own report.
The index measures how densely a report is packed with ESG vocabulary, not any gap between what a
company claims and how the press describes it.

We checked our reading by recalculating the authors' own published figures, which match exactly,
so this is not a misunderstanding on our part. The working is in
[`synthesis/gsi-formula.md`](synthesis/gsi-formula.md).

This sharpens the research question rather than weakening it, but it changes what we can claim.
We build our own media-based measure and set it out in full, rather than presenting it as a
replication of theirs.

A related open check: Lagasio (2024, Paper 6) builds a text-only "severity index" in a similar
spirit. Paper 1 does not cite it. Whether the two share the same structure, and so whether our
finding applies to a family of indices, can only be settled from the full text of Paper 6.

## The PDFs

All five original papers and four of the 19 new ones (papers 8, 12, 16 and 17, which are
legally open access) are in [`papers/`](papers/); see [`papers/SOURCES.md`](papers/SOURCES.md) for
full citations, DOIs, licences and the verification record. The other 15 are listed in
[`papers/TO_OBTAIN.md`](papers/TO_OBTAIN.md) with direct links, so they can be fetched through an
institute library.

All 24 citations were checked against Crossref. One DOI needed correcting (Paper 8's year
component), one date is flagged (Paper 9), and three of the original citations were corrected
earlier; the details are in `papers/SOURCES.md`. [`references.bib`](references.bib) is the BibTeX
file generated from the verified records.

## How to use these notes

For the whole project in one document, read [`BE_Project.pdf`](BE_Project.pdf). For the
plain-language version of the first five papers, read [`REPORT.md`](REPORT.md). For depth on a
paper, go to its note. [`synthesis/comparison.md`](synthesis/comparison.md) is the fastest way to
see how all 24 relate to each other.

## Status

**Literature review and design: complete.** Notes, synthesis, citations and the LaTeX report are
written. Fifteen of the 19 new notes rest on abstracts and publisher metadata only; each says so.

**Experiments: not started.** This repository is a review and design project. No data has been
retrieved, no index has been computed, no model has been trained and no analysis code exists.
The hypotheses (H1–H7) and the twelve proposed improvements are designs, not results.
