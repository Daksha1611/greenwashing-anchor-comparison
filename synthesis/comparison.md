# The papers side by side

The column that matters most for this project is **reality anchor**: what external fact, if any,
each paper checks corporate green talk against. This file has three parts: the five original
papers in detail, a single table covering all 24, and the ranking of anchor types.

**How to read the † mark.** For papers whose full text we could not read, a † marks a detail that
comes from our research brief and is **not** confirmed by the abstract or the paper. See
`papers/SOURCES.md` for which notes rest on the full text (P8, P12, P16, P17) and which on the
abstract only.

## Part 1. The five original papers

| # | Paper | Sample | Period | Reality anchor | NLP method | Headline result |
|---|---|---|---|---|---|---|
| 1 | Davidescu et al. (2026), *Sustainability* | 204 large CEE firms (Coface Top 500 CEE) | 2023 | **None in the index.** Media corpus is collected and correlated separately, but does **not** enter the GSI formula | Dictionary counts, sentiment scoring, TF–IDF, LDA (described but unused) | Mean GSI 0.5765; highest Germany 0.6086, lowest Lithuania 0.5157; finance/e-commerce/aviation worst; large firms *lower* GSI (0.49) |
| 2 | Gorovaia & Makrominas (2025), *Eur. Financial Mgmt* | 441 US public firms, 1,120 CSR reports, 993 matched pairs | 2008–2022 | **Environmental violations**: MSCI ESG KLD negative env. indicators + Refinitiv "Environmental Fines" (ENERDP103) | Lemmatised text measures: environmental content density, readability, positiveness, length | Violators write longer (20,304 vs 15,091 words), more positive (0.823 vs 0.816), more environmental (0.185 vs 0.175), less readable reports; DiD shows firms change reporting *after* violating (β=0.175***) |
| 3 | Peng et al. (2024), *Bus. Strategy & Env.* | 1,403 obs., 199 Fortune Global 500 MNCs, 27 countries | 2001–2020 | **Measured carbon emissions**: Scope 1+2 and carbon intensity (Refinitiv Asset4) | **None**: panel regression on numeric data only | Environmental score *positively* predicts emissions (CE t+1: 0.775***, CI t+1: 1.304***); mandating disclosure did not close the gap; Paris Agreement did not prevent it |
| 4 | Wang, Gao & Sun (2025), *EPJ Data Science* | 9,534 obs., Chinese A-share firms | 2008–2023 | **None**: index is entirely text-internal | **MacBERT** (BERT-family) sentence-level classification, two fine-tuned classifiers | GWL = √(GWLS × GWLE); vs human labels: GWLS 97.79% acc / 98.82% F1, GWLE 95.13% acc / 95.59% F1 |
| 5 | Forliano et al. (2025), *Rev. Managerial Science* | 97 peer-reviewed articles (Scopus + WoS) | Review | n/a (literature review) | Bibliometric + network analysis, full-text theory coding | Four thematic clusters; macro-level theories dominate (legitimacy, institutional, stakeholder); proposes multi-level framework |

## Part 2. All 24 papers

Anchor types: **E** = emissions / pollution; **V** = violations; **R** = ratings-gap (a
disclosure score minus a performance score); **C** = controversy / news events; **M** = average
media tone (our planned GDELT measure; not yet used by any paper here except nominally Paper 1);
**N** = none (text-internal); **n/a** = not a greenwashing measure.

| # | Paper | Publisher | Sample | Anchor | Method | Headline |
|---|---|---|---|---|---|---|
| 1 | Davidescu et al. (2026) | MDPI | 204 CEE firms, 2023 | N (M claimed, not in formula) | Dictionary + TF–IDF | Mean GSI 0.5765; formula has no media term |
| 2 | Gorovaia & Makrominas (2025) | Wiley | 441 US firms, 2008–2022 | V | Text measures, PSM, DiD | Violators write more and more positively; reporting shifts after a violation |
| 3 | Peng et al. (2024) | Wiley | 199 Fortune Global 500 firms, 2001–2020 | E | Panel regression | Higher environmental score goes with *more* emissions |
| 4 | Wang, Gao & Sun (2025) | Springer | 9,534 Chinese A-share firm-years, 2008–2023 | N | MacBERT classifiers | Symbolic vs substantive split; 97.79% agreement with human labels (component 1) |
| 5 | Forliano et al. (2025) | Springer | 97 articles | n/a | Systematic review | Four themes; macro theories dominate |
| 6 | Lagasio (2024) | Elsevier | 749 listed firms | N (as far as the abstract shows) | Sentiment + term frequency | ESGSI varies by industry and region |
| 7 | Bingler et al. (2024) | Elsevier | MSCI World firms (†14,584 reports, 2010–2020) | N for the index, then related to E and C separately | ClimateBert CTI | Only targeted engagement goes with less cheap talk; cheap talk goes with negative news and higher emissions growth |
| 8 | Bingler et al. (2022) | Elsevier | 818 TCFD-supporting firms, FY2014–2019 | N | ClimateBERT | TCFD support is mostly cheap talk; firms cherry-pick non-material content |
| 9 | Hrasky (2012) | Emerald | ASX Top 50, 2005 vs 2008 | E (sector carbon intensity, coarse) | Manual content analysis | Carbon-intensive sectors lean on action; less intensive sectors on symbolism |
| 10 | Clarkson et al. (2008) | Elsevier | †191 firms, five most polluting US industries | E | †GRI-based content index | †Better performers disclose more |
| 11 | Tadros & Magnan (2019) | Emerald | 78 firms, 14 years | E (performance measure not stated in abstract) | Panel regression, three disclosure channels | High performers disclose more; little sign low performers legitimise through disclosure |
| 12 | Luu et al. (2025) | Elsevier | 2,731 US firms, 2007–2022 (134 treated) | R, with GHGRP as shock | Difference-in-differences | Greenwashing fell after GHGRP; about 31% of the mean score in the fullest model |
| 13 | Cho et al. (2015) | Emerald | Fortune 500, late 1970s vs 2010 | None directly (legitimacy/exposure factors) | Disclosure indices, valuation model | Breadth up; legitimacy–disclosure link unchanged; not valued by investors |
| 14 | Yu, Luu & Chen (2020) | Elsevier | †1,925 large-cap firms, multi-country | R | †Peer-relative disclosure-minus-performance scores | †Scrutiny deters greenwashing |
| 15 | Liu et al. (2024) | Taylor & Francis | Listed firms (†Chinese, 2014–2021) | R (†) | Regression | Greenwashing raises stock price crash risk |
| 16 | Dorfleitner & Utz (2024) | Springer | Conceptual; two-firm illustration | Multiple, combined | Framework | Five pillars; misconduct factor stands in for real performance |
| 17 | Raghunandan & Rajgopal (2022) | Springer | 147 ESG funds, 74 managers; 2,428 non-ESG funds; 2010–2018 | V + E vs ESG scores | Fund-holdings regressions | ESG funds hold firms with more violations and fines, higher emissions per revenue, higher ESG scores |
| 18 | Boiral (2013) | Emerald | 23 GRI A/A+ reports; 116 news events | C (manual) | Counter-accounting | 90% of significant negative events not reported |
| 19 | Ghitti et al. (2024) | Springer | Listed firms (†US) | C (†, **unverified**) | Novel measure + governance regressions | More independent boards go with more greenwashing; greenwashing reduces firm value |
| 20 | Bacher et al. (2025) | Taylor & Francis | Global data; Europe 2011–2015 pre-Paris | C (†) | Double-selection LASSO, two-pass regression | Greenwashing priced in Europe before Paris; not after |
| 21 | Utz (2019) | Springer | † International sample (Asset4) | C (scandal events, used to test ratings) | †Event study | †Aggregated ESG assessments do not predict scandals |
| 22 | Cho (2009) | Taylor & Francis | One firm (Total SA), two disasters | C (case-level events) | Case study | Disclosure used to legitimise, not to account |
| 23 | Drempetic et al. (2020) | Springer | †Asset4 ratings | n/a (rating bias) | † Rating regressions | †Size and data availability raise the ESG score |
| 24 | Gibson Brandon et al. (2021) | Taylor & Francis | S&P 500, 7 raters, 2010–2017 | n/a (compares raters) | Return regressions | Returns rise with rater disagreement, mainly environmental; †average correlation ≈ 0.45 |

## Part 3. Reality anchors, ranked by how hard the evidence is

Two anchor types are new compared with the first version of this file: the **ratings-gap** and
**controversy** anchors. The old "media coverage" row is split in two, because an average of news
tone and a count of specific negative events are different things.

| Anchor | Papers | Strength | Weakness |
|---|---|---|---|
| **Measured emissions** | 3, 9 (coarse), 10, 11, 17 (partly) | Physical quantity, directly comparable, hard to argue with | Often reported to a rating provider, so self-reported at source; coverage skews large-cap |
| **Regulatory violations** | 2, 17 | Legally adjudicated fact; binary and unambiguous | Only **positive** assurance: an unpenalised firm is not proven clean, merely unpenalised; enforcement intensity varies by regulator and region |
| **Ratings-gap** (disclosure score minus performance score) | 12, 14, 15, (16 in part) | Cheap, works on large samples (2,731 firms in paper 12), and is the template that papers 12 and 15 copy from paper 14 | Both halves are **third-party scores**, so it inherits their biases: scores rise with firm size and data availability (Drempetic et al.), raters disagree (Gibson Brandon et al.), and scores track disclosure quantity rather than conduct (Raghunandan & Rajgopal) |
| **Controversy / news events** | 18, 19 (†), 20 (†), 21, 22, and 7 (negative news as a correlate) | Independent of the firm; captures what actually happened, not just what was said | Depends on what the press chose to cover, so confounded with firm **visibility**, size and newsworthiness. Papers 19 and 20 are marked † because the construction was not confirmed |
| **Average media tone** | (1, nominally) | Independent of the firm; broad coverage | Same visibility confound, stronger: tone averaged over many articles mixes conduct with attention. **The hypothesis this project tests** |
| **None (text-internal)** | 4, 6, 8, 1 in practice | Scales cheaply; no external data needed | Validates against human annotators, never against reality; cannot distinguish an honest verbose firm from a dishonest one |

## The pattern that motivates this project

Papers **2 and 3 agree**, using entirely independent anchors and entirely different methods:
firms that talk greener do worse in reality. Violators write more environmental content
(paper 2); higher environmental scores predict higher emissions (paper 3). Paper 17 adds a third
piece of evidence at fund level: ESG funds hold firms with more violations and higher emissions
intensity. Call this the **talk–action gap**; all three results rest on external verification.

Papers **1 and 4** produce sophisticated greenwashing indices with **no external verification in
the index itself**. Paper 4 is candid about this. Paper 1 claims an external anchor its published
formula does not contain (see `gsi-formula.md` §3.1). Paper 6 appears to be a close relative of
Paper 1 (see note 06), but we have only read its abstract.

Papers 1 and 3 **disagree about large firms**:

- Paper 1: large firms have *lower* GSI (0.49) and better report/media alignment (r = 0.89),
  read as large firms being more honest.
- Paper 3: the sample is *entirely* very large firms, and finds systematic greenwashing throughout.

Both can be true at once **only if** the media/text-anchored measure is picking up something other
than greenwashing in large firms: visibility, media fluency, professionalised reporting. That is
the salience hypothesis. The new papers add substantial prior support for it (rating size bias,
rater disagreement concentrated among large firms, and scores that track news coverage), but none
tests it on greenwashing indices. See `extended-literature.md`.

## What no paper here does

- **Compares two or more anchors on the same firms and ranks the same firms as worst under
  each.** Every paper commits to one anchor (or none) and stops. Papers 7 (talk against emissions
  and news), 17 (scores against violations and emissions) and 24 (raters against each other) come
  closest; the gap is stated precisely in `extended-literature.md`.
- **Reports rank agreement between competing greenwashing measures.** No Spearman correlation, no
  overlap statistic, no κ between greenwashing indices anywhere in the set. Paper 24 reports
  agreement between ESG *raters*, which is the model for what we propose.
- **Controls greenwashing scores for media coverage volume.** Paper 1 comes closest by discussing
  visibility, but never enters coverage volume as a regressor.

## Coverage note

Forliano et al.'s review closed in **February 2025** and cannot include papers 1 or 4, nor
most of the newest papers in Part 2. It does cite Dorfleitner & Utz (paper 16, as "2023"). The most
methodologically relevant papers for this project post-date the field's most recent map.
