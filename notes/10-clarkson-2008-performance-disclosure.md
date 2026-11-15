# Note 10 — Clarkson, Li, Richardson & Vasvari (2008), environmental performance and disclosure

**Citation.** Clarkson, P. M., Li, Y., Richardson, G. D., & Vasvari, F. P. (2008). Revisiting the
relation between environmental performance and environmental disclosure: An empirical analysis.
*Accounting, Organizations and Society, 33*(4–5), 303–327.
https://doi.org/10.1016/j.aos.2007.05.003 (Elsevier; paywalled)

**File.** Not in `papers/`; see [`papers/TO_OBTAIN.md`](../papers/TO_OBTAIN.md).

**Citation check.** Verified against Crossref: four authors in order, volume 33, issue 4–5, pages
303–327. **Neither Crossref nor OpenAlex had an abstract for this paper, so this note rests on
the description in our research brief and the publisher metadata only; we have not read the paper
or its abstract.** Everything below that describes the paper is therefore marked † (from the
brief, unchecked).

---

## Research question

† Do firms with better environmental performance disclose more about the environment, or do poor
performers disclose more to repair their image? Two competing theories predict opposite signs:
**voluntary disclosure theory** (good performers signal their quality) and **legitimacy theory**
(poor performers use disclosure to defend themselves).

## Method

† A sample of **191 firms** drawn from the **five most polluting US industries**. Discretionary
environmental disclosure is measured with a **content index based on the GRI framework**, and
environmental performance is measured as pollution performance.

## Headline results

† A **positive association between environmental performance and disclosure**: better performers
disclose more, which fits voluntary disclosure theory, although some legitimisation patterns still
appear. We do not state any coefficients, because none are given in the brief.

## Reality anchor

**Emissions / pollution performance** † (measured, firm-level). We have not been able to check
which exact pollution measure the paper uses.

## How it relates to our project

This is a classic counterweight to Paper 2. Gorovaia & Makrominas find that **violators write
more and more positively**. Clarkson et al. find that **better performers disclose more**. They do
not necessarily contradict each other, because they measure different things: Paper 2 measures the
*volume and tone* of environmental language, while Clarkson et al. use a content index that counts
*specific, hard, verifiable items*.

So the sign of the talk–action relationship depends on **what kind of talk is measured**. That is
why our design should score verifiable action statements separately from vague commitments (using a
ClimateBERT-style classifier), rather than counting how much a firm says. See the "do bad
performers say more or less?" contradiction in `synthesis/extended-literature.md`.

## Limitations

† Our reading, pending the paper: a five-industry sample of heavy polluters cannot speak for
service-sector firms, and the study is from the early GRI era, before mandatory climate reporting
rules.
