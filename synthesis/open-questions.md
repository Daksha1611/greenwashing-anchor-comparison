# The gap, as a testable question — and the design that tests it

## 1. The gap in one paragraph

Greenwashing indices in this literature are anchored to different external realities, or to none.
Gorovaia & Makrominas (2025) anchor to **regulatory violation records**; Peng et al. (2024) anchor
to **measured carbon emissions**; Wang et al. (2025) anchor to **nothing external**; Davidescu et
al. (2026) describe their index as anchored to **media coverage** but publish a formula containing
no media term (see `gsi-formula.md` §3.1). All four are peer-reviewed. **No study compares two or
more anchors on the same set of firms.** So we do not know whether these measures identify the
same firms — and if they do not, a substantial part of this literature may be measuring something
other than what it claims.

## 2. The primary research question

> **Do greenwashing measures built on media sentiment identify the same firms as measures built on
> regulatory violation records — or is media-anchored greenwashing detection largely measuring
> firm visibility?**

### Hypotheses

- **H1 (convergence).** GSI-media and GSI-violation rank firms similarly.
  *Test:* Spearman ρ between the two, over the full sample.
  *H1 fails if* ρ is small (say |ρ| < 0.3) or its confidence interval spans zero.

- **H2 (top-decile agreement).** The two indices flag the same worst offenders.
  *Test:* Jaccard index and Cohen's κ on the top-decile sets.
  *Rationale:* rank correlation over a whole sample can look respectable while the tails — the
  firms anyone would actually act on — disagree completely. This is the practically decisive test.

- **H3 (salience).** GSI-media is substantially explained by firm visibility rather than
  environmental conduct.
  *Test:* regress GSI-media on firm size and media coverage volume, with sector fixed effects.
  *H3 is supported if* size and coverage volume carry large, significant coefficients and the
  model explains a large share of variance — and especially if adding a real-conduct measure
  (violations or emissions) adds little incremental R².

- **H4 (anchor concordance, secondary).** The two *reality-anchored* measures agree with each
  other better than either agrees with the media measure — i.e. ρ(violation, emissions) >
  ρ(media, violation) and > ρ(media, emissions).
  *Rationale:* papers 2 and 3 already agree using independent anchors. If both hard anchors agree
  with each other but not with media, that isolates media as the outlier rather than suggesting
  all measures are simply noisy.

**Note that H1–H3 are informative whichever way they come out.** Convergence would validate a
cheap, globally available measure. Divergence would identify a measurement problem in a
literature that feeds ESG ratings.

## 3. Why it matters

ESG ratings move real money — index inclusion, fund mandates, cost of capital. Peng et al. (2024)
already show that a major commercial environmental score is *positively* associated with carbon
emissions. If academic greenwashing indices share a measurement flaw with commercial ratings —
rewarding visibility and disclosure fluency rather than conduct — then the tools built to detect
greenwashing may be reproducing the problem they were designed to expose. And because
media-based measures are cheap and globally available, they are the ones most likely to scale into
practice.

## 4. Experimental design

### 4.1 Sample

- **Target: 150–300 US-listed firms.** Large enough for stable rank statistics and for a
  regression with sector fixed effects; small enough that entity matching can be manually audited.
- **Frame construction — order matters.** Start from **GHGRP reporters matched to SEC CIKs**, then
  seek sustainability reports. Never start from report availability: that is precisely the
  selection bias Gorovaia & Makrominas engineered their sampling to avoid, and it would
  preferentially select the high-visibility firms whose behaviour H3 is about.
- **Period:** a recent multi-year window (e.g. 2019–2023), so violation and emissions records
  accumulate enough signal and post-hoc reporting changes (paper 2's DiD finding) are observable.
- **Stated limitation up front:** the GHGRP 25,000 t CO2e threshold biases the frame toward
  industrial firms. Report it; do not pretend to general coverage.

### 4.2 The three indices

All three are computed per firm-year, then standardised to a common scale before comparison.

**GSI-media (GDELT tone).**
Retrieve ESG/environment-filtered coverage per firm from GDELT; compute mean `V2Tone` and article
volume. The index rises as coverage tone becomes more negative — i.e. it is a media-anchored
greenwashing proxy in the sense Davidescu et al. *describe* (not the one they implement).
*Retain article volume as a separate variable — it is the key regressor in H3, not a nuisance.*

**GSI-violation (EPA ECHO).**
Aggregate facility-level violations to parent company: quarters in non-compliance, formal
enforcement actions, penalty amounts. Normalise by facility count and consider a state-year
enforcement baseline, since raw counts partly measure regulator activity.
*Inherits the asymmetry paper 2 flags: no violation ≠ clean. State it.*

**GSI-emissions (GHGRP).**
Aggregate facility CO2e to parent company. Compute both **absolute** emissions and **intensity**
(scaled by revenue), since Peng et al. found the two behave differently.
*Scope 1, US facilities only — not comparable to Refinitiv Scope 1+2. State it.*

**Disclosure-side measure (the "talk" half).**
ClimateBERT over sustainability report text, using the commitment-vs-action distinction. This is
the analogue of Wang et al.'s symbolic-vs-substantive split, and it is what makes each index a
*greenwashing* measure (talk minus action) rather than a pure reality measure.
**Not FinBERT** — FinBERT is trained on financial sentiment and is the wrong domain.

### 4.3 Statistical tests

| Test | Method | Purpose |
|---|---|---|
| Rank agreement | **Spearman ρ**, all index pairs, with bootstrap 95% CIs | H1, H4 |
| Top-decile overlap | **Jaccard index** on top-10% sets | H2 — raw overlap |
| Top-decile agreement | **Cohen's κ** on binary top-decile flags | H2 — overlap corrected for chance |
| Salience | OLS: `GSI_media ~ log(size) + log(coverage_volume) + sector FE` | H3 |
| Incremental validity | Add `GSI_violation` / `GSI_emissions` to the H3 model; compare adjusted R² | H3 |

**Why both Jaccard and κ:** Jaccard reports the plain overlap of two top-decile sets; κ corrects
for the overlap you would expect by chance. Reporting only Jaccard would overstate agreement.

**Multiple comparisons:** several pairwise tests are run, so apply a correction
(Benjamini–Hochberg) and report both raw and adjusted p-values.

**Pre-specify before looking:** thresholds (|ρ| < 0.3 as divergence), the decile cut, and the
regression specification are fixed *before* the indices are computed, so the analysis is not
tuned to the result.

### 4.4 Robustness

- Repeat with top **quintile** and top **5%** — conclusions should not hinge on the decile cut.
- Repeat with emissions **intensity** substituted for absolute emissions.
- Vary the GDELT tone window (annual vs trailing 12-month).
- Report the **entity match rate** and re-run on the high-confidence-match subset only. An
  unmeasured match rate makes every correlation uninterpretable.

## 5. Threats to validity

1. **Entity matching error.** The dominant risk. Bad company→facility joins inject noise that
   biases correlations toward zero — which would look like support for divergence. **A null result
   is only interpretable if the match rate is high and audited.** This is why matching is a
   first-class module.
2. **Sector confounding.** Heavy industry both emits more and attracts more negative coverage.
   Sector fixed effects throughout.
3. **Enforcement heterogeneity.** ECHO reflects regulator activity as well as firm conduct.
4. **GHGRP threshold.** Restricts and skews the sample frame.
5. **Reverse causality in media tone.** Coverage may follow a violation rather than independently
   detect greenwashing — a reason to test lagged specifications.
6. **Non-violation ≠ compliance.** Applies to GSI-violation throughout.

## 6. Secondary questions worth recording

- Does the Davidescu et al. formula, implemented **as published**, correlate with any reality
  anchor at all? Since it reduces to ESG term density, this is a sharp and cheap test of whether
  disclosure intensity carries any signal about conduct.
- Does the geometric-mean composite (Wang et al.) behave differently from an arithmetic mean on
  the same components?
- Does the post-violation reporting shift found by Gorovaia & Makrominas (β_DD = 0.175***)
  replicate on EPA ECHO violations rather than commercial database fines?
