# Greenwashing detection: comparing reality anchors

A research project on greenwashing detection in corporate ESG disclosures.

## Research question

> **Do greenwashing measures built on media sentiment identify the same firms as measures built on
> regulatory violation records — or is media-anchored greenwashing detection largely measuring
> firm visibility?**

Greenwashing indices in the published literature are anchored to different external realities —
regulatory violations, measured emissions, media coverage — or to nothing external at all. No
study compares two anchors on the same set of firms. If media-anchored and violation-anchored
measures diverge, then media-based greenwashing indices may be measuring firm **visibility**
rather than greenwashing, which would matter for a substantial part of this literature and for the
ESG ratings it feeds.

Full argument: **[REPORT.md](REPORT.md)**. Unfamiliar term? **[GLOSSARY.md](GLOSSARY.md)**.

## Headline finding from the review

Davidescu et al. (2026) is treated in the literature — and was treated in this project's original
framing — as the canonical *media-anchored* greenwashing index. Reading the methodology closely,
**its published formula contains no media term**: every input is a TF–IDF score computed from the
firm's own report. The aggregation rule is recoverable, and reproduces the paper's published
figures to four decimal places, but the index measures ESG keyword density in disclosure, not any
report-versus-media discrepancy.

This sharpens the research question rather than undermining it — but it changes what can be
claimed, and it means this project builds its own explicitly specified media-anchored index rather
than claiming to replicate theirs. Details: **[synthesis/gsi-formula.md](synthesis/gsi-formula.md)**.

## Notes on the source papers

| # | Note | Paper | Reality anchor |
|---|---|---|---|
| 1 | [01](notes/01-davidescu-2026-gsi.md) | Davidescu et al. (2026), *Sustainability* — Greenwashing Severity Index, 204 CEE firms | **None in formula** (media claimed) |
| 2 | [02](notes/02-gorovaia-makrominas-2025-violations.md) | Gorovaia & Makrominas (2025), *Eur. Financial Mgmt* — violator vs non-violator CSR reports | Regulatory violations |
| 3 | [03](notes/03-peng-2024-emissions.md) | Peng et al. (2024), *Bus. Strategy & Env.* — environmental scores vs carbon emissions | Measured emissions |
| 4 | [04](notes/04-wang-2025-deep-learning-index.md) | Wang, Gao & Sun (2025), *EPJ Data Science* — MacBERT greenwashing index | None (text-internal) |
| 5 | [05](notes/05-forliano-2025-landscape.md) | Forliano et al. (2025), *Rev. Managerial Science* — systematic review of 97 articles | n/a (review) |

## Synthesis

- **[comparison.md](synthesis/comparison.md)** — the five papers side by side: sample, anchor, method, result.
- **[gsi-formula.md](synthesis/gsi-formula.md)** — full step-by-step reconstruction of the GSI, with what is verified and what is not.
- **[datasets-and-access.md](synthesis/datasets-and-access.md)** — the six data sources: access, rate limits, fields, gotchas.
- **[open-questions.md](synthesis/open-questions.md)** — the gap as testable hypotheses, plus the full experimental design.
- **[Papers/SOURCES.md](Papers/SOURCES.md)** — full APA citations, DOIs, publishers, indexing status.

## Data sources

| Source | Purpose | Access | URL |
|---|---|---|---|
| **GDELT Project** | Global news with computed tone scores → GSI-media | Free, no key | https://www.gdeltproject.org/ |
| **EPA ECHO** | Facility violations, inspections, penalties → GSI-violation | Free REST API, no key | https://echo.epa.gov/ |
| **EPA GHGRP / FLIGHT** | Facility greenhouse gas emissions → GSI-emissions | Free, bulk download + API | https://ghgdata.epa.gov/ |
| **SEC EDGAR** | 10-K filings; authoritative firm identity (CIK) — the join spine | Free; `User-Agent` required, 10 req/s | https://www.sec.gov/edgar/search/ |
| **Responsibility Reports** | Corporate sustainability report PDFs | Free archive, scraping required | https://www.responsibilityreports.com/ |
| **CDP** | Standardised climate disclosures | Partly licensed — treat as optional | https://www.cdp.net/en/data |

GDELT is used instead of NewsAPI because NewsAPI's free tier returns only about one month of
history, which cannot support a multi-year panel.

## Planned method

Three indices over the **same** 150–300 US-listed firms:

- **GSI-media** — GDELT tone (with article volume retained separately as the visibility regressor)
- **GSI-violation** — EPA ECHO violations aggregated to parent company
- **GSI-emissions** — EPA GHGRP facility emissions aggregated to parent company

Disclosure text is scored with **ClimateBERT** (commitment vs action). **Not FinBERT** — wrong domain.

Compared by **Spearman rank correlation**, **top-decile overlap** (Jaccard + Cohen's κ), and a
**regression of GSI-media on firm size and media coverage volume** with sector fixed effects to
test the salience hypothesis directly.

## Repository layout

```
├── README.md            you are here
├── REPORT.md            consolidated argument: findings, gap, why it matters, design
├── GLOSSARY.md          plain-language definitions
├── Papers/              source PDFs (unmodified) + SOURCES.md
├── notes/               one annotated note per paper, 01–05
├── synthesis/           cross-paper analysis and experimental design
├── src/                 pipeline scaffold — stubs and TODOs only, nothing implemented
└── data/                raw / interim / processed (gitignored)
```

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Uses **pypdf** (PyPDF2 is deprecated), spacy, transformers, pandas, scipy, statsmodels.

## Status

**Literature review — 5 of 6 papers.**

- [x] Davidescu et al. (2026) — GSI reconstructed and verified; formula problems documented
- [x] Gorovaia & Makrominas (2025) — citation corrected (two authors, 2025)
- [x] Peng et al. (2024)
- [x] Wang, Gao & Sun (2025) — authors extracted
- [x] Forliano et al. (2025) — authors extracted; issue number still unconfirmed
- [ ] **Pending:** *Detecting greenwashing behaviour in decarbonization performance*,
      *Accounting & Finance*, 65(4), 3739–3762 (2025). Not obtained; no note written; no findings assumed.

**Experiments — not started.** `src/` contains stubs, docstrings and TODOs only. No data has been
retrieved from any source; no index has been computed.

**Open tasks**
- Obtain the sixth paper
- Transcribe Davidescu et al. Appendices A.1–A.4 (the four dictionaries) into `data/raw/dictionaries/`
- Confirm the issue number for Forliano et al. (2025)
- Re-verify all API rate limits against live documentation before building the pipeline
