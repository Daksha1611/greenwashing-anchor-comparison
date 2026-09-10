# Note 02 — Gorovaia & Makrominas (2025), violation-anchored greenwashing detection

**Citation (corrected).** Gorovaia, N., & Makrominas, M. (2025). Identifying greenwashing in
corporate-social responsibility reports using natural-language processing.
*European Financial Management, 31*(1), 427–462. https://doi.org/10.1111/eufm.12509
(Wiley; open access under CC BY-NC-ND)

**File.** `papers/Euro Fin Management - 2024 - Gorovaia - Identifying greenwashing in corporate‐social responsibility reports using.pdf`

**Citation discrepancies flagged.**
1. There are exactly **two authors** — Nina Gorovaia (Frederick University, Cyprus) and Michalis
   Makrominas (Frederick University, Cyprus). The supplied citation used "Gorovaia, N., et al.",
   which implies three or more. **"et al." is wrong here**; cite both names.
2. **Year should be 2025, not 2024.** The copyright line reads "© 2024 The Author(s)"
   (online-first), but the article of record is *Eur Financ Manag.* 2025;31:427–462 — volume 31,
   issue 1, 2025. The filename's "2024" reflects the online-first date.
3. Volume, issue and page range (31(1), 427–462) were not in the supplied citation; added.

---

## Research question

Do firms that have actually been penalised for environmental violations write their CSR reports
differently from firms with a clean record? And do firms *change* how they write right after they
commit a violation?

This reframes greenwashing detection around a hard, binary, external fact: **did this firm receive
a monetary penalty for an environmental violation, yes or no?** The authors call it a "simple, yet
error-free" yardstick, and use it to split firms into *violators* and *nonviolators*.

## Method

**Reality anchor.** Firms are classified as violators using **MSCI ESG KLD Stats** negative
environmental indicators (2008–2019), extended with **Refinitiv**'s "Environmental Fines"
(ENERDP103) for 2020–2022. Timeframe: **2008–2022**, US public firms.

> **Important nuance for our project.** The anchor is a *commercial ESG database field* recording
> environmental fines — **not** EPA enforcement records queried directly. Our planned use of EPA
> ECHO is therefore not a replication of their anchor but a more primary-source version of it.
> This is a difference worth stating explicitly rather than glossing.

**Sample construction (deliberately avoids selection bias).** Rather than starting from whichever
CSR reports happen to be easy to find — which skews toward large, green, narrow-industry firms —
they start from the full KLD/Refinitiv firm population, then:

1. Run **propensity score matching** year by year, with annual replacement, k-nearest-neighbour
   k = 1, caliper 0.5, matching on Age, Size, ROE, Leverage, M/B, D/E, Intangibility and industry.
   Result: **993 matched pairs** (1,986 matched firm-year observations).
2. Search four sources for the CSR reports of the matched firms (company webpages, Sustainability
   Reporting, Corporate Register, GRI databases). Result: **1,120 available CSR reports** across
   **441 unique firms** (237 nonviolators, 204 violators).
3. Violators produce more reports per firm: **3.12 vs 2.03** (ratio 1.53).

**Text measures.** Environmental score (density of environmental content), readability score,
positiveness score, report length in pages and words, plus interactions. Text is lemmatised and
lowercased.

## Headline results (real numbers)

**Univariate (N = 1,120), violators vs nonviolators:**

| Measure | Violator | Nonviolator | Difference | p |
|---|---|---|---|---|
| Environmental score | 0.185 | 0.175 | 0.010*** | <0.001 |
| Positiveness score | 0.823 | 0.816 | 0.007** | 0.012 |
| N-pages | 57 | 46 | 11*** | <0.001 |
| Total words | 20,304 | 15,091 | 5,213*** | <0.001 |
| Readability score | 47.400 | 45.950 | 1.450 (n.s.) | 0.114 |
| % women directors | 0.193 | 0.210 | −0.017*** | <0.001 |
| N. of directors | 10.230 | 10.438 | −0.207** | 0.012 |

> Minor table error flagged: the Positiveness Score difference is printed as **−0.007** although
> 0.823 − 0.816 = **+0.007**, and the surrounding text describes violators as *more* positive.
> The sign in the table appears to be a typo.

Violators are also more likely to be **domestic** (odds ratio 1.84***) and to have
**concentrated ownership** (odds ratio 2.64***).

**Multivariate logit** (predicting violator status, industry + year fixed effects, N = 1,120):
violator status is positively associated with environmental score, positiveness and report length,
and *negatively* with the environment × readability interaction — i.e. violators write **more**
environmental content, **more positively**, at **greater length**, but **less readably**.

**Staggered difference-in-differences** (N = 475, 79 firms, ~6.01 reports per firm) — does
reporting change *after* a violation?

| Dependent variable | β_DD | p |
|---|---|---|
| Environmental score | 0.175*** | <0.001 |
| Positiveness score | 0.804*** | <0.001 |
| N-words | 0.917*** | <0.001 |
| Environment × Positiveness | 3.328*** | <0.001 |
| Environment × Readability | 0.142*** | <0.001 |
| Readability score | 0.449 (n.s.) | 0.750 |

So firms measurably **modify their reporting right after committing a violation** — the strongest
causal-flavoured evidence in this set of five papers.

## Stated limitations

- The binary fine-based measure gives **positive assurance for violators but only negative
  assurance for nonviolators**: a firm with no recorded fine is not proven clean, only unpenalised.
  (The authors are explicit about this asymmetry — it is a real constraint we inherit if we use
  EPA ECHO the same way.)
- CSR reporting is voluntary, so report availability is uneven; observations with missing
  variables are dropped rather than substituted.
- Findings concern US public firms 2008–2022 and may not generalise.

## Connection to the other papers

- **vs. Davidescu et al. (note 01):** the head-to-head contrast our project is built on. Same
  broad task (detect greenwashing from sustainability text), opposite anchoring philosophy —
  hard violation records here, media/self-referential text there.
- **Direction of the effect is the crux.** Here, *more* environmental language predicts *worse*
  real behaviour. In Davidescu et al., higher ESG term density mechanically produces a *higher*
  GSI (also read as worse). The two happen to agree in sign — but for entirely different reasons,
  and only one of them is validated against reality.
- **vs. Peng et al. (note 03):** strongly consistent. Peng et al. find higher environmental
  *scores* go with higher *emissions*; Gorovaia & Makrominas find heavier environmental *language*
  goes with *violations*. Two different anchors, same "talk more, do less" conclusion.
- **vs. Wang et al. (note 04):** Wang et al. would classify this kind of unverifiable, aspirational,
  positive language as "symbolic" — a conceptual bridge between the two.
