# Greenwashing detection: what the literature establishes, and what it leaves open

**Status:** literature review complete for 5 of 6 planned papers. No experiments run.
**Date:** 2026-09-10

---

## Summary

Five papers were read in full. They establish, with independent methods and independent data, that
firms which talk greener frequently perform worse in reality. They also reveal a methodological
split that nobody in this set addresses: greenwashing indices are anchored to **different external
realities, or to none at all**, and no study checks whether these anchors identify the same firms.

Reading the papers also produced an unplanned finding. The index this project treats as the
canonical *media-anchored* measure — Davidescu et al.'s Greenwashing Severity Index — **contains
no media term in its published formula**. That sharpens the research question rather than
undermining it, but it changes what we can claim, and it is documented in detail in
`synthesis/gsi-formula.md`.

---

## 1. What the five papers establish

### 1.1 The talk–action gap is real, and shows up under two independent anchors

The two strongest empirical papers reach the same conclusion by completely different routes.

**Gorovaia & Makrominas (2025)** classify 441 US public firms as environmental violators or not,
using recorded environmental fines, and then read their CSR reports. Violators write reports that
are **longer** (20,304 vs 15,091 words), **more positive** (0.823 vs 0.816), carry **more
environmental content** (0.185 vs 0.175) — and are **less readable**. All differences significant
at 1% except readability. Their difference-in-differences analysis shows firms **change their
reporting after committing a violation** (β_DD = 0.175, p < 0.001 for environmental content).

**Peng et al. (2024)** never look at text at all. They regress measured carbon emissions on
Refinitiv environmental scores for 199 Fortune Global 500 firms over 2001–2020, and find the
score **positively** predicts emissions (0.775, t = 5.13 for emissions at t+1; 1.304, t = 7.09 for
carbon intensity). Higher environmental scores go with *more* carbon.

Two anchors — legal violations and physical emissions. Two methods — NLP text measures and panel
regression. Same conclusion. This is as close to a settled finding as this literature offers.

Peng et al. add two results that matter for policy: **mandatory disclosure did not close the gap**
(the `Post_Man × EN` interaction is insignificant, t = 1.17), and the **Paris Agreement did not
prevent** greenwashing in carbon reduction. More disclosure has not, by itself, produced more honesty.

### 1.2 Text-based detection has become technically sophisticated

**Wang, Gao & Sun (2025)** apply MacBERT, a BERT-family language model, to 9,534 firm-year
observations of Chinese A-share CSR reports, classifying sentences to build two components:
**selective disclosure** (staying quiet about failures) and **expressive manipulation** (symbolic
rather than substantive language), combined as a geometric mean, `GWL = √(GWLS × GWLE)`. Agreement
with human annotators is high — 97.79% accuracy for the first component, 95.13% for the second.

This is a real methodological advance over dictionary counting, because a keyword list cannot
distinguish a concrete commitment from a vague aspiration; both use the same words.

### 1.3 The field's own map confirms it is theory-rich and measurement-heterogeneous

**Forliano et al. (2025)** systematically review 97 articles from Scopus and Web of Science,
identifying four thematic clusters and a dominance of macro-level theories (legitimacy,
institutional, stakeholder). Useful for placing this work — but note it is a **map of theories,
not of measurement anchors**, and its coverage closed in February 2025, before both Davidescu et
al. (2026) and Wang et al. (2025). It documents genuine construct heterogeneity across the field;
it does not itself demonstrate the specific gap below.

### 1.4 An index that measures disclosure volume, presented as measuring discrepancy

**Davidescu et al. (2026)** build a Greenwashing Severity Index across 204 CEE firms, described
throughout as capturing "discrepancies between firms' ESG self-representation and external public
narratives".

Reading the methodology closely, the published formula is:

```
GSI = ⅓·E_tfidf + ⅓·S_tfidf + ⅓·G_tfidf
```

**Every input is a TF–IDF score computed from the firm's own report.** The media corpus is
collected, and used for separate group-level sentiment correlations, but **it does not enter the
index.** As specified, the GSI computes no discrepancy of any kind — it measures ESG keyword
density in corporate disclosure. The paper's own correlation table is consistent with this: overall
ESG focus correlates 0.63 with GSI, and the authors themselves observe that greater ESG emphasis
in reporting is associated with higher greenwashing scores.

I verified the aggregation arithmetically against the paper's own tables — it reproduces their
published figures to four decimal places across every reported grouping. So the formula is
correctly recovered; it simply is not the formula the abstract describes. Full documentation,
including four further internal inconsistencies (a sentiment scale stated two incompatible ways,
a claim that "all GSI values exceed 0.5" against a reported minimum of 0.00063, a misstated
robustness range, and PSM results described as "significant" at p = 0.077 and p = 0.064), is in
`synthesis/gsi-formula.md`.

---

## 2. The gap

Laid out plainly:

| Paper | Reality anchor |
|---|---|
| Gorovaia & Makrominas (2025) | Regulatory violations (environmental fines) |
| Peng et al. (2024) | Measured carbon emissions |
| Wang, Gao & Sun (2025) | **None** — text-internal, by explicit design |
| Davidescu et al. (2026) | **None in the formula** — media claimed, not implemented |

**No paper in this set compares two anchors on the same firms.** Each commits to one and stops.
There is no Spearman correlation, no overlap statistic, no κ between competing greenwashing
measures anywhere in the literature reviewed here.

That gap has a sharp empirical consequence, visible in a direct tension between two of the papers:

- **Davidescu et al. find large firms are the *cleanest*** — GSI 0.49 versus the 0.5765 sample
  mean, with report/media alignment of r = 0.89 — and read this as large firms being more honest
  under scrutiny.
- **Peng et al.'s sample is *entirely* very large firms** — Fortune Global 500 — and finds
  systematic greenwashing throughout it.

Both results can hold simultaneously **only if the text/media-anchored measure is capturing
something other than greenwashing in large firms**: visibility, media fluency, professionalised
disclosure. That is the **salience hypothesis**, and no study in this literature tests it.

Notably, Davidescu et al.'s own third future-research direction is to triangulate NLP-based
indicators against "objective environmental, social and governance outcomes, such as emissions
data, workplace safety records, governance enforcement actions". **The authors of the
media-framed index are themselves asking for this comparison.**

---

## 3. Why it matters

ESG ratings direct real capital — index inclusion, fund mandates, cost of capital. Peng et al.
have already shown that a widely used commercial environmental score is positively associated with
the emissions it is meant to reflect inversely. The academic instruments built to *detect*
greenwashing are increasingly proposed as correctives to exactly those ratings.

If those instruments share the ratings' flaw — rewarding visibility and disclosure fluency rather
than conduct — then the corrective reproduces the problem. And media-anchored measures are the
ones most likely to scale into practice, because news data is cheap, global and continuously
updated in a way that regulatory records are not.

Testing whether they agree is therefore not a narrow methodological exercise. It determines
whether a whole class of cheap, scalable greenwashing measures means what it claims.

---

## 4. How the design follows

The research question:

> Do greenwashing measures built on media sentiment identify the same firms as measures built on
> regulatory violation records — or is media-anchored greenwashing detection largely measuring
> firm visibility?

The design falls directly out of the gap. Build **three** indices over **the same** 150–300
US-listed firms, one per anchor:

- **GSI-media** — GDELT tone. GDELT rather than NewsAPI because NewsAPI's free tier yields about
  one month of history, which cannot support a panel.
- **GSI-violation** — EPA ECHO facility violations, inspections and penalties, aggregated to parent.
- **GSI-emissions** — EPA GHGRP facility emissions, aggregated to parent.

The disclosure side uses **ClimateBERT**'s commitment-versus-action distinction — the English
analogue of Wang et al.'s symbolic-versus-substantive split. **Not FinBERT**: it is trained on
financial sentiment and is the wrong domain.

Then compare: **Spearman ρ** for overall rank agreement, **Jaccard and Cohen's κ** on top-decile
overlap (rank correlation can look respectable while the tails — the firms anyone would act on —
disagree entirely), and a **regression of GSI-media on firm size and media coverage volume** with
sector fixed effects to test salience directly.

Three design choices inherited from the papers:

1. **Sample frame from GHGRP/EDGAR first, then seek reports** — never start from report
   availability. That is the selection bias Gorovaia & Makrominas built their whole sampling
   procedure to avoid, and it would preferentially select high-visibility firms, contaminating the
   very hypothesis under test.
2. **Both absolute emissions and intensity**, since Peng et al. found they behave differently.
3. **Measure and report the entity match rate.** Bad company→facility joins inject noise that
   biases correlations toward zero — which would masquerade as evidence of divergence. A null
   result is only interpretable if match quality is audited. This is why entity matching is a
   first-class module (`src/entity_matching.py`), not a preprocessing detail.

We do **not** claim to replicate Davidescu et al.'s GSI — the component scores are not
reproducible from the paper (see `gsi-formula.md` §4). We implement the aggregation rule as
verified, and build our own explicitly specified media-anchored index alongside it.

Full design, hypotheses, tests and threats to validity: `synthesis/open-questions.md`.

---

## 5. What is still missing

- **One paper not obtained:** *Detecting greenwashing behaviour in decarbonization performance*,
  *Accounting & Finance*, 65(4), 3739–3762 (2025). No note written, no findings assumed. Its title
  suggests a decarbonisation anchor that would sit directly alongside Peng et al., so it should be
  obtained before this review is called complete.
- **Dictionaries A.1–A.4** from Davidescu et al. are in the open-access PDF but not yet transcribed.
- **The issue number** for Forliano et al. is not printed on the PDF and remains unconfirmed.
