# Note 16 — Dorfleitner & Utz (2024), a conceptual framework for firm-level greenwashing

**Citation.** Dorfleitner, G., & Utz, S. (2024). Green, green, it's green they say: a conceptual
framework for measuring greenwashing on firm level. *Review of Managerial Science, 18*(12),
3463–3486. https://doi.org/10.1007/s11846-023-00718-w (Springer; open access, CC BY 4.0)

**File.** `papers/dorfleitner-utz-2024-framework.pdf` (University of Augsburg OPUS copy, 25 pages,
CC BY 4.0).

**Citation check.** Verified against Crossref: two authors, volume 18, issue 12, pages 3463–3486
(online 2 December 2023; issue December 2024). Paper 5 (Forliano et al.) cites it as "2023", the
online-first year. **Full text read.**

---

## Research question

Can we measure greenwashing at the level of the **firm**, across many firms at once, rather than
one case or one advertisement at a time? And what would a defensible measure be built from?

## Method

This is a **conceptual paper**: it proposes a framework and works through it with a small
illustration. It does not test the framework on a large sample.

- **Idea.** Following Delmas and Burbano's definition, greenwashing means poor environmental
  performance combined with positive communication about it. The indicator is
  **apparent green performance minus real green performance**, taken in each of several
  **dimensions of greenness** (for example, emissions) and floored at zero.
- **Five pillars of information.** Four describe the *apparent* side:
  1. **soft ESG data** (for example, policies, memberships, initiatives),
  2. **textual self-representation** (what the firm writes about itself),
  3. **green marketing expenses**,
  4. **green virtue** (signals such as a sustainability board or links to green organisations),
  and one the *real* side:
  5. **hard ESG data** (measured outcomes).
- **The misconduct shortcut.** Real green performance is often hard to measure. The authors
  therefore suggest approximating it from evident corporate **misconduct** (a number between 0 and
  1 built from sources such as scandals or an ESG provider's controversy score). If real
  performance is taken to be apparent performance times (1 − misconduct), the greenwashing
  indicator reduces to apparent performance times misconduct, and no direct measure of real
  performance is needed.
- **Aggregation and weights.** Dimensions are combined into a single firm indicator. The weights
  and standardisations can be **calibrated** on a limited set of firm-years where in-depth case
  examination shows whether greenwashing occurred, or learned by machine learning, with the
  explicit model kept as a benchmark.
- **Illustration.** Using Refinitiv 2022 data for two firms, the paper computes indicator values
  of **0.136 for Delivery Hero** and **0.909 for Zalando**. It is an example of how the framework
  is applied, not a test.

## Headline results

There are no population-level empirical results. The contributions are the **five-pillar
framework**, the **misconduct approximation**, and a classification of greenwashing on **four
levels**: product/service, firm, financial intermediary and standard-setting environment.
The authors also stress that the indicator is best read as **greenwashing risk**, not as proof of
disclosed greenwashing, when it relies on the misconduct approximation.

## Reality anchor

**Multiple, combined.** The real side uses hard ESG data, or misconduct and controversy
information when hard data are unavailable. The apparent side combines four kinds of soft and
textual evidence.

## How it relates to our project

- **The only paper that explicitly proposes combining several information sources into one
  indicator.** It is the conceptual backbone for `synthesis/combining-and-improvements.md`.
- **What it does not do is the empirical step we add.** It combines pillars *before* asking
  whether the pillars agree. Our contribution is to test agreement first. If the pillars disagree,
  averaging them hides the disagreement (Improvement 11).
- **Calibration is a predictive-validity idea in embryo.** Calibrating on firm-years with known
  outcomes is close to our tie-breaker (H6): trust the index that matches observed conduct.
- **A caution for our own design:** the misconduct shortcut relies on controversy scores, which
  come from media. A media-derived "real performance" is exactly the kind of anchor our
  salience hypothesis worries about. Paper 5 cites this framework, so it is already part of the
  field's map.

## Limitations

- It is untested at scale: two illustrative firms, no validation sample.
- Weights are left to be calibrated; the paper does not provide them.
- The measure depends on a normative choice of what counts as "green" (the dimensions), which the
  authors acknowledge is subjective.
- The misconduct approximation can flag a firm that has behaved badly elsewhere as a greenwasher
  in a dimension where no misconduct was evident; the authors themselves read the result as risk,
  not fact, for that reason.
