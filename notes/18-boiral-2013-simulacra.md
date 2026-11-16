# Note 18 — Boiral (2013), sustainability reports as simulacra: a counter-account

**Citation.** Boiral, O. (2013). Sustainability reports as simulacra? A counter-account of A and
A+ GRI reports. *Accounting, Auditing & Accountability Journal, 26*(7), 1036–1071.
https://doi.org/10.1108/AAAJ-04-2012-00998 (Emerald; paywalled)

**File.** Not in `papers/`; see [`papers/TO_OBTAIN.md`](../papers/TO_OBTAIN.md). Our brief said an
accepted manuscript exists on CORE; OpenAlex lists no open copy and we could not find it.

**Citation check.** Verified against Crossref (the five-digit DOI suffix `-00998` is correct):
single author, volume 26, issue 7, pages 1036–1071. **This note is based on the abstract and
publisher metadata only; we have not read the full text.** The abstract is detailed, which is why
the numbers below are reliable.

---

## Research question

Can sustainability reporting be seen as a **simulacrum**: a polished image that hides real
sustainable-development problems and projects an idealised picture of the firm? The test case is
reports that have earned the Global Reporting Initiative (GRI)'s top application levels, **A or A+**.

## Method

**Content analysis and counter-accounting.** Counter-accounting means setting a company's own
account against independent information about the same company.

- **23 sustainability reports** from **energy and mining** firms with GRI level A or A+.
- About **2,700 pages** of report text, organised around **92 GRI indicators**.
- Compared with **116 significant news events** that clearly bore on those firms' responsibility
  for sustainability problems.
- The **1,258 pictures** in the reports were also categorised into recurring themes.

## Headline results

- **90 per cent of the significant negative events were not reported**, contrary to the GRI
  principles of balance, completeness and transparency.
- The pictures in the reports show various "simulacra" that are disconnected from the actual
  impact of the firms' business.
- The authors conclude that counter-accounting is a relevant way to assess the quality of
  sustainability reports, and that the reliability of GRI's A / A+ application levels is
  questionable.

## Reality anchor

**Media events, collected and matched by hand.** This is a media anchor, but a different kind from
average news tone: it is a list of specific negative events that happened.

## How it relates to our project

- **A hand-built version of the media anchor that measures omission, not tone.** Our planned
  GDELT measure averages the tone of coverage. Boiral asks something sharper: of the bad things
  the press reported about this firm, how many does its own report mention?
- **It suggests a better media measure.** We propose automating the idea as an **omission rate**:
  the share of a firm's negative, environment-themed news events that its report never mentions
  (Improvement 4 in `synthesis/combining-and-improvements.md`). That makes use of media for *what
  happened* and the report for *what was said*, rather than comparing their tone.
- **It links Paper 4's idea to an outside reference.** Wang et al.'s "selective disclosure"
  (staying quiet about what went badly) is measured against a list of required topics. Boiral's
  version measures it against events that actually occurred.

## Limitations

- **Two industries only** (energy and mining), and a small sample of 23 firms, so no claim of
  generality.
- **Manual and expensive**: it depends on the author's judgement about which news events are
  "significant", and does not scale without automation.
- News coverage reflects what journalists chose to cover; an unreported event is not necessarily a
  hidden one. That is the visibility problem our project is about.
- Based on the abstract only.
