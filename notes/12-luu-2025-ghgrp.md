# Note 12 — Luu, Le, Luu & Nguyen (2025), the GHGRP as a natural experiment on greenwashing

**Citation.** Luu, N. H., Le, C., Luu, H. N., & Nguyen, D. T. K. (2025). Does mandatory greenhouse
gas emissions reporting program deter corporate greenwashing? *Journal of Environmental
Management, 373*, 123740. https://doi.org/10.1016/j.jenvman.2024.123740
(Elsevier; open access, CC BY 4.0)

**File.** `papers/luu-2025-ghgrp-greenwashing.pdf` (University of Lincoln Figshare deposit,
10 pages, CC BY 4.0).

**Citation check.** Verified against Crossref: four authors in order, volume 373, article 123740,
January 2025. **Full text read.**

---

## Research question

Did the US Environmental Protection Agency's **mandatory Greenhouse Gas Reporting Program
(GHGRP)** reduce corporate greenwashing?

## Method

- **Quasi-natural experiment with difference-in-differences.** The GHGRP began on
  30 October 2009; from **2010**, facilities emitting more than **25,000 metric tons** of
  greenhouse gas a year must report their emissions. Firms that own such facilities are the
  **treated** group; all other listed US firms are the **control** group. The authors compare the
  two groups before and after the rule.
- **Sample.** **2,731 publicly listed US firms, 2007–2022**, financial firms excluded: **134
  treated** and **2,597 control** firms. Treatment status comes from matching firm tickers to the
  EPA's FLIGHT data on GHGRP facilities.
- **Greenwashing measure (a ratings gap).** For each firm-year, the paper takes the
  **Refinitiv ESG disclosure score minus the Refinitiv ESG performance score**, after
  standardising each (subtract the mean, divide by the standard deviation). A higher value means
  disclosure outruns performance. The authors adopt this from Yu et al. (2020) and one other
  paper, and call it a peer-relative measure.
- Controls include firm size, leverage, profitability and sales; the specifications add firm,
  industry and year fixed effects.
- **Checks.** Tests of parallel pre-trends, placebo and falsification tests (for example, random
  assignment of treatment years), and a decomposition into disclosure and performance.

## Headline results

- Greenwashing **fell** after the GHGRP. In the fullest specification the effect is
  about **30.74%** of the sample's mean greenwashing score (a coefficient of 0.537 against a mean
  of 1.747).
- The mean greenwashing score in the sample is **1.747** (disclosure runs ahead of performance on
  average).
- The decomposition indicates the program pushed firms to **improve actual ESG performance while
  curbing inflated ESG claims**.
- **Larger and more profitable firms** show a bigger fall, and so do firms with more
  **environmental innovation** (all from the abstract).

## Reality anchor

**Ratings gap**: Refinitiv disclosure score minus Refinitiv performance score, with the GHGRP
as the policy shock. Note that **both halves of the gap come from the same vendor**. No
independent measure of conduct (emissions, fines) enters the greenwashing score itself; GHGRP is
used only to define who was affected by the rule.

## How it relates to our project

- **Same data source, same country, same period.** GHGRP is our planned emissions anchor
  (`synthesis/datasets-and-access.md`). This paper shows it can be used as a source of treatment
  status, and it uses the same 25,000-tonne threshold we have to live with.
- **A ready external validity test (hypothesis H7).** A valid greenwashing index should respond to
  the 2010 GHGRP mandate in the direction found here: lower afterwards. Indices that do not move
  are suspect. See `synthesis/open-questions.md`.
- **It contradicts Peng et al. (Paper 3) on whether mandatory disclosure helps.** Peng finds
  the score–emissions gap persists, and is larger, under mandatory disclosure. Luu et al. find
  greenwashing falls after the GHGRP. The two use different anchors and settings, which is
  exactly the point of our project: the conclusion depends on the measure. See
  `synthesis/extended-literature.md`.
- **Large firms respond most.** That fits the idea that size and visibility shape both behaviour
  and measurement.

## Limitations

- The measure relies on **one vendor's** disclosure and performance scores. The authors say
  themselves that it depends on third-party ESG assessments and subjective judgement.
- **Our own inference, not the authors':** because the GHGRP makes emissions public, a vendor's
  performance score could improve partly because better data became available, not because
  conduct changed. The ratings-gap design cannot rule that out.
- Only **134** firms are treated, against 2,597 controls, and treatment is defined by owning a
  large facility, which is itself related to firm size.
- The description of the measure does not say the scores are standardised within industry-year
  (the approach we would like for our own indices); see note 14.
- Non-US firms and firms below the threshold are outside the design.
