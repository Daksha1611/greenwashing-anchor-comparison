# Note 20 — Bacher et al. (2025), greenwashing risk in asset pricing

**Citation.** Bacher, K., Døskeland, M., Graça, R., Lavrutich, M., Pierce, M., & Pimentel, R.
(2025). Greenwashing risk in asset pricing: the shift after the Paris agreement. *Quantitative
Finance, 25*(11), 1851–1872. https://doi.org/10.1080/14697688.2025.2563091
(Taylor & Francis; open access, CC BY)

**File.** Not in `papers/`. Open access, but the automated download was blocked; see
[`papers/TO_OBTAIN.md`](../papers/TO_OBTAIN.md).

**Citation check.** Verified against Crossref: six authors in order, volume 25, issue 11,
pages 1851–1872; issue and pages confirmed (they were among the items our brief was least sure
of). Crossref prints the second author as "DØskeland"; we use Døskeland. **This note is based on
the abstract and publisher metadata only; we have not read the full text.** † marks details from
our research brief.

---

## Research question

Is greenwashing a **systematic risk** that investors are paid to bear, an **asset pricing factor**
like size or value? And did that change after the **2015 Paris Agreement**?

## Method

A **double-selection LASSO** approach (a statistical method for choosing which factors matter
from a large pool) and a **two-pass regression** estimate the contribution of greenwashing as a
new asset pricing factor: its stochastic discount factor loading and its associated risk premium,
using an extensive **global** dataset.

† The greenwashing measure is the one from Ghitti et al. (note 19), built from an ESG score and
an ESG controversy score. The abstract does not describe the measure.

## Headline results

From the abstract:

- **In Europe before the Paris Agreement (2011–2015)**, the loading and the risk premium for the
  greenwashing factor are statistically different from zero.
- That result is robust to alternative ways of building factor portfolios, and greenwashing
  firms **consistently underperform** their genuinely sustainable peers.
- The authors read this as investors treating greenwashing as a **systematic information risk**
  in an environment **lacking uniform ESG disclosure standards**.
- **After the Paris Agreement, greenwashing has no significant pricing power**, which effectively
  reclassifies it as a **firm-specific risk**.

## Reality anchor

† **Controversy** (ESG score versus controversy score), if the brief is right. Not confirmed from
the abstract.

## How it relates to our project

- **Controversy-anchored measures are in use in a top quantitative finance journal.** If the brief
  is right, a measure of this type is mainstream, which supports adding it as a fifth index
  (`synthesis/combining-and-improvements.md`, Improvement 1).
- **It echoes Peng et al.'s Paris Agreement finding from a different angle.** Peng (Paper 3) finds
  the Paris Agreement did not stop high environmental scores going with high emissions; this paper
  finds greenwashing stopped being a *priced* risk after Paris. Both treat Paris as a turning
  point, and both are sensitive to how greenwashing is measured.
- A greenwashing factor that is priced or not priced says something about the **market's view**,
  not directly about conduct, so it is a different kind of validity from an event or violation test.

## Limitations

- Based on the abstract only; we do not know the exact measure, the sample counts or the
  magnitudes.
- A finding about **pricing** is not a finding about **how accurate** the measure is: markets can
  price a risk that exists only because everyone is measuring the same score.
- The pricing result is specific to **Europe** and a short **2011–2015** pre-Paris window.
