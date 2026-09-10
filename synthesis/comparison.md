# The five papers side by side

The column that matters most for this project is **reality anchor** — what external fact, if any,
each paper checks corporate green talk against.

## Master table

| # | Paper | Sample | Period | Reality anchor | NLP method | Headline result |
|---|---|---|---|---|---|---|
| 1 | Davidescu et al. (2026), *Sustainability* | 204 large CEE firms (Coface Top 500 CEE) | 2023 | **None in the index.** Media corpus is collected and correlated separately, but does **not** enter the GSI formula | Dictionary counts, sentiment scoring, TF–IDF, LDA (described but unused) | Mean GSI 0.5765; highest Germany 0.6086, lowest Lithuania 0.5157; finance/e-commerce/aviation worst; large firms *lower* GSI (0.49) |
| 2 | Gorovaia & Makrominas (2025), *Eur. Financial Mgmt* | 441 US public firms, 1,120 CSR reports, 993 matched pairs | 2008–2022 | **Environmental violations** — MSCI ESG KLD negative env. indicators + Refinitiv "Environmental Fines" (ENERDP103) | Lemmatised text measures: environmental content density, readability, positiveness, length | Violators write longer (20,304 vs 15,091 words), more positive (0.823 vs 0.816), more environmental (0.185 vs 0.175), less readable reports; DiD shows firms change reporting *after* violating (β=0.175***) |
| 3 | Peng et al. (2024), *Bus. Strategy & Env.* | 1,403 obs., 199 Fortune Global 500 MNCs, 27 countries | 2001–2020 | **Measured carbon emissions** — Scope 1+2 and carbon intensity (Refinitiv Asset4) | **None** — panel regression on numeric data only | Environmental score *positively* predicts emissions (CE t+1: 0.775***, CI t+1: 1.304***); mandating disclosure did not close the gap; Paris Agreement did not prevent it |
| 4 | Wang, Gao & Sun (2025), *EPJ Data Science* | 9,534 obs., Chinese A-share firms | 2008–2023 | **None** — index is entirely text-internal | **MacBERT** (BERT-family) sentence-level classification, two fine-tuned classifiers | GWL = √(GWLS × GWLE); vs human labels: GWLS 97.79% acc / 98.82% F1, GWLE 95.13% acc / 95.59% F1 |
| 5 | Forliano et al. (2025), *Rev. Managerial Science* | 97 peer-reviewed articles (Scopus + WoS) | Review | n/a — literature review | Bibliometric + network analysis, full-text theory coding | Four thematic clusters; macro-level theories dominate (legitimacy, institutional, stakeholder); proposes multi-level framework |

## Reality anchors, ranked by how hard the evidence is

| Anchor | Papers | Strength | Weakness |
|---|---|---|---|
| **Measured emissions** | 3 | Physical quantity, directly comparable, hard to argue with | Reported to a rating provider, so self-reported at source; coverage skews large-cap |
| **Regulatory violations** | 2 | Legally adjudicated fact; binary and unambiguous | Only **positive** assurance — an unpenalised firm is not proven clean, merely unpenalised; enforcement intensity varies by regulator and region |
| **Media coverage** | (1, nominally) | Independent of the firm; broad coverage | Confounded with firm visibility, size and sector newsworthiness — **the hypothesis this project tests** |
| **None (text-internal)** | 4, and 1 in practice | Scales cheaply; no external data needed | Validates against human annotators, never against reality; cannot distinguish an honest verbose firm from a dishonest one |

## The pattern that motivates this project

Papers **2 and 3 agree**, using entirely independent anchors and entirely different methods:
firms that talk greener do worse in reality. Violators write more environmental content
(paper 2); higher environmental scores predict higher emissions (paper 3). Call this the
**talk–action gap**, and note that both results rest on external verification.

Papers **1 and 4** produce sophisticated greenwashing indices with **no external verification in
the index itself**. Paper 4 is candid about this. Paper 1 claims an external anchor its published
formula does not contain (see `gsi-formula.md` §3.1).

And papers 1 and 3 **disagree about large firms**:

- Paper 1: large firms have *lower* GSI (0.49) and better report/media alignment (r = 0.89) —
  read as large firms being more honest.
- Paper 3: the sample is *entirely* very large firms, and finds systematic greenwashing throughout.

Both can be true at once **only if** the media/text-anchored measure is picking up something other
than greenwashing in large firms — visibility, media fluency, professionalised reporting.
That is the salience hypothesis, and no paper in this set tests it.

## What no paper here does

- **Compares two or more anchors on the same firms.** Every paper commits to one anchor (or none)
  and stops. This is the gap.
- **Reports rank agreement between competing greenwashing measures.** No Spearman correlation, no
  overlap statistic, no κ between indices anywhere in the set.
- **Controls greenwashing scores for media coverage volume.** Paper 1 comes closest by discussing
  visibility, but never enters coverage volume as a regressor.

## Coverage note

Forliano et al.'s review closed in **February 2025** and cannot include papers 1 or 4. The two most
methodologically relevant papers in this set post-date the field's most recent map.
