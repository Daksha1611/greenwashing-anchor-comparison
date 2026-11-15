# Note 17 — Raghunandan & Rajgopal (2022), do ESG funds make stakeholder-friendly investments?

**Citation.** Raghunandan, A., & Rajgopal, S. (2022). Do ESG funds make stakeholder-friendly
investments? *Review of Accounting Studies, 27*(3), 822–863.
https://doi.org/10.1007/s11142-022-09693-1 (Springer; open access, CC BY 4.0)

**File.** `papers/raghunandan-rajgopal-2022-esg-funds.pdf` (LSE Research Online, published
version, 43 pages, CC BY 4.0).

**Citation check.** Verified against Crossref: two authors, volume 27, issue 3, pages 822–863.
**Full text read** (we searched the text for the sample, the data sources and the main results;
we did not work through every table).

---

## Research question

Funds that call themselves "ESG" claim to put money into firms that treat their stakeholders well.
Do the firms they hold actually have better records on labour law, environmental law and carbon
emissions than the firms held by the same managers' non-ESG funds?

## Method

- **Funds.** **147** self-labelled US ESG mutual funds (identified by Morningstar) from **74 asset
  managers**, compared with **2,428** non-ESG funds run by the same institutions, **2010–2018**.
  The comparison is within the same asset manager and year, which removes manager-level
  differences.
- **Compliance record.** Violations come from **Violation Tracker**, a database compiled by the
  non-profit **Good Jobs First**. It covers violations of federal laws written by more than 50
  US agencies (most commonly workplace safety, but also labour, environmental and consumer
  protection). The paper measures whether a portfolio firm committed violations and how large the
  **penalties** were.
- **Emissions.** Carbon emissions per unit of revenue and whether the firm discloses carbon
  emissions voluntarily.
- **ESG scores.** Average ESG scores of the held firms, from commercial providers (MSCI's KLD
  and Thomson Reuters are named in the paper).

## Headline results

From the abstract and text:

- ESG funds hold firms with **worse track records for compliance with labour and environmental
  laws**, and those firms **pay more in fines**, relative to firms held by non-ESG funds at the
  same managers.
- ESG funds' holdings are **more likely to disclose carbon emissions voluntarily**, but they also
  have **higher carbon emissions per unit of revenue**.
- Despite this, ESG funds hold firms with **higher average ESG scores**.
- ESG scores are **correlated with the quantity of voluntary ESG-related disclosure**, but **not
  with firms' compliance records or actual levels of carbon emissions**. In the text the authors
  add that the scores are correlated with metrics of **news coverage** and with the existence and
  quantity of disclosure, but not with the actual content of that disclosure, and they cite
  Drempetic et al. (2017, an earlier version of note 23) as consistent with this.
- ESG funds appear to **underperform financially** and **charge higher fees** than other funds in
  the same manager and year.
- The paper also notes that these fines are typically small relative to the size of the large
  firms involved.

## Reality anchor

**Violations** (Violation Tracker) **plus emissions**, compared against **commercial ESG scores**.
The comparison is made at the level of **fund portfolios**, not of individual companies.

## How it relates to our project

1. **An independent confirmation of the talk–action gap.** Here the "talk" is an ESG score or a
   fund label, and the check is a violations database, so it is a third piece of evidence beside
   Papers 2 and 3, at portfolio level.
2. **A new violations source to cross-check EPA ECHO.** Violation Tracker aggregates penalties
   across more than 50 federal agencies, and the paper uses it at the level of the portfolio
   firm, so it is worth adding to `synthesis/datasets-and-access.md` as a cross-check on our own
   aggregation of ECHO facilities to parent companies. **We have not verified its access terms,
   its parent-company coverage or its licence**, and all three need checking before use.
3. **Ratings and violations disagree.** ESG scores track the *quantity of voluntary
   disclosure* and news coverage, not conduct. That is a partial version of our own question: do
   different measures of the same concept agree? Here the answer is no. It also bears on the
   salience hypothesis: a score that moves with news coverage is partly a visibility measure.

## Limitations

- Portfolio-level evidence says what funds hold, not which individual companies greenwash.
- The paper's own measure of "conduct" is federal violations and penalties, which includes a
  great deal of workplace safety. Environmental violations are one slice.
- Violation Tracker, like any enforcement record, reflects regulators' activity as well as
  corporate behaviour, and a firm with no violation is not shown to be clean.
- The sample is US-only and covers 2010–2018.
