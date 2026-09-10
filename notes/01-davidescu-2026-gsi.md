# Note 01 — Davidescu et al. (2026), Greenwashing Severity Index for CEE firms

**Citation.** Davidescu, A. A., Manta, E. M., Bîrlan, I., Miler, A. M., & Niță, A. S. C. (2026).
Detecting greenwashing in ESG disclosure: An NLP-based analysis of Central and Eastern European
firms. *Sustainability, 18*(3), 1486. https://doi.org/10.3390/su18031486 (MDPI, open access, CC BY)

**File.** `papers/sustainability-18-01486-v2.pdf`
**Citation check.** Matches the citation supplied. Received 20 Dec 2025, accepted 22 Jan 2026,
published 2 Feb 2026.

---

## Research question

Can you detect greenwashing by comparing what a company says about itself in its sustainability
report against what the outside world says about it in the news? The authors build a
**Greenwashing Severity Index (GSI)** and use it to ask how much greenwashing there is across
Central and Eastern Europe (CEE), and whether it varies by country, industry and firm size.

> *Greenwashing* here is defined broadly: not just misleading environmental claims, but any gap
> between "apparent" sustainability performance (what the report says) and "real" sustainability
> performance (what the firm actually does). The authors deliberately extend it across all three
> ESG pillars — environmental, social and governance — rather than treating it as an
> environment-only problem.

## Method

**Sample.** 204 large firms operating in CEE, for the year 2023. Sampling started from the
Coface Top 500 CEE (2023) ranking. News was collected with the Python `gnews` package plus
custom web scraping; sustainability/annual reports were pulled from company websites.

> Note on the sample funnel: the paper says filtering produced "a refined corpus covering
> approximately 320 companies", but the headline sample is 204. **The step from ~320 to 204 is
> never explained.** Flagged as underspecified.

**Four hand-built dictionaries** (word lists) do the work:

- **A1 Greenwashing dictionary** — 1,140 "positive" words scored **−1** (e.g. *sustainability*,
  *climate-friendly*, *ethical*, *low-impact*) and 990 "negative" words scored **+1**
  (e.g. *pollution*, *irresponsible*, *anti-environmental*, *eco-fraud*).
- **A2/A3/A4 Environmental, Social, Governance dictionaries** — 122 words each.

> **Internal inconsistency flagged.** Section 2.1 says A1 words are marked −1 or +1. Section 2.2
> says "each word in the Greenwashing Dictionary (A1) was assigned a sentiment score ranging from
> −3 to +3". These two statements cannot both be true. The actual scale used is not recoverable
> from the text.

**Techniques used** (each explained on first use in `GLOSSARY.md`): sentiment scoring normalised
by document length, Pearson correlation between report-tone and news-tone, **TF–IDF** term
weighting, **LDA** topic modelling, and **propensity score matching (PSM)**.

## Headline results (real numbers)

- **Mean GSI ≈ 0.5765** (median 0.5745, SD 0.1111, min 0.00063, max 0.8150). The authors read
  this as "moderate but widespread" greenwashing.
- **By country:** Germany highest (0.6086), then Romania (0.5970), Hungary (0.5943);
  Lithuania lowest (0.5157).
- **By industry:** finance, online commerce and aviation highest (0.64, 0.63, 0.61);
  construction lowest (0.49).
- **By firm size:** large firms show *lower* GSI (0.49) and stronger report/news alignment
  (r = 0.89) than SMEs. The authors attribute this to visibility and regulatory scrutiny.
- **Correlations:** GSI correlates 0.82 / 0.91 / 0.96 with the E / S / G "Washing" components.
- **PSM:** firms with high ESG "focus imbalance" have higher GSI —
  ATT = **0.048, 95% CI (−0.004, 0.100), p = 0.077** (nearest neighbour, 48 matched pairs); and
  ATT = **0.0403, 95% CI (−0.0017, 0.0823), p = 0.064** (Mahalanobis, 71 pairs).
- **Robustness:** re-weighting the three pillars gives Spearman rank correlations with the
  baseline GSI of 0.842 (E-dominant), 0.941 (S-dominant), 0.966 (G-dominant).

## Problems found in this paper (important — see `synthesis/gsi-formula.md`)

These are my findings from reading the paper, not the authors' own caveats.

1. **The published GSI formula contains no media term.** Section 2.6 defines
   `GSI = ωE·E_tfidf + ωS·S_tfidf + ωG·G_tfidf` with equal weights of 1/3. Every input is a
   TF–IDF score computed from the firm's *own report*. Nothing from the news corpus enters it.
   This contradicts the abstract, which says the GSI "captures discrepancies between firms' ESG
   self-representation and external public narratives". **As published, the GSI is a measure of
   ESG term density in the report, not a report-vs-media discrepancy measure.** This matters
   directly for our project — see below.
2. **"Significantly higher" overstates the PSM result.** Both ATT estimates have 95% confidence
   intervals that include zero and p-values above 0.05 (0.077 and 0.064). The abstract's claim
   that imbalanced firms "display significantly higher GSI values" is not supported at
   conventional significance levels.
3. **"All GSI values exceed 0.5" is contradicted by their own Table 5**, which reports a
   minimum GSI of 0.00063.
4. **Robustness range misstated.** The text says rank correlations range "between 0.94 and 0.97",
   but their Table 12 reports 0.842 for the environmental-dominant specification.
5. **E/S/G "Washing" scores are never formally defined.** They are the variables actually
   reported in every results table, but no equation introduces them. (I recovered their
   relationship to GSI arithmetically — see `synthesis/gsi-formula.md`.)

## Stated limitations (the authors' own)

- Textual data captures *communicative alignment*, not verified operational performance.
- Media narratives may themselves be biased or incomplete.
- English-language-only sources may underrepresent local ESG discourse.
- Cross-sectional (single year), so no insight into dynamics or response to regulation.

Their **third future-research direction is, almost exactly, our project**: triangulate NLP-based
greenwashing indicators against "objective environmental, social and governance outcomes, such as
emissions data, workplace safety records, governance enforcement actions, or supply-chain audits".

## Connection to the other papers

- **vs. Gorovaia & Makrominas (note 02):** the sharpest contrast in the set. Both use NLP on
  corporate sustainability text, but Gorovaia & Makrominas anchor to a *hard external record*
  (environmental fines), whereas this paper's index — as actually specified — anchors to nothing
  external at all. This is the divergence our project tests.
- **vs. Peng et al. (note 03):** Peng et al. anchor to measured carbon emissions and find that
  *higher* environmental scores go with *worse* emissions. Davidescu et al. find larger firms have
  *lower* GSI. Since large firms are also the high-visibility, high-scoring firms, these two
  results point in opposite directions — which is precisely the salience hypothesis we want to test.
- **vs. Wang et al. (note 04):** both build a composite text-based index; Wang et al. are explicit
  that theirs is text-internal, Davidescu et al. claim an external anchor they do not implement.
- **vs. Forliano et al. (note 05):** supplies the field-level context — measurement heterogeneity
  is a known, named weakness of this literature.
