# The Greenwashing Severity Index (GSI): full reconstruction

Source: Davidescu et al. (2026), *Sustainability, 18*(3), 1486, Sections 2.1–2.6 and Tables 5–12.
Open access (CC BY), so the text is fully available.

**Purpose of this document.** We intend to replicate this index exactly. A plausible-but-wrong
reconstruction would silently corrupt everything downstream, so this file separates three things:
what the paper **states**, what I **verified arithmetically**, and what remains **ambiguous**.

**Bottom line up front.** The aggregation step is fully recoverable and I have confirmed it
against the paper's own published numbers to four decimal places. **The component scores are
not fully recoverable** — several inputs are underspecified, and there is a substantive
contradiction between the formula the paper prints and the quantity the paper claims to measure.
**The GSI cannot currently be replicated from the paper alone.**

---

## 1. What the paper states

### Step 1 — Corpora

Two text corpora per firm, both preprocessed identically (lowercasing, punctuation normalisation,
tokenisation, lemmatisation, stopword and symbol removal):

- **Corporate corpus:** sustainability or annual reports, from company websites / IR pages.
- **Media corpus:** news articles retrieved via the Python `gnews` package plus custom scraping,
  filtered to (a) articles naming the company in headline or body, (b) sustainability/ESG/CSR
  relevance by keyword screening, with duplicates and syndicated copies removed by textual
  similarity.

Sample: 204 firms, CEE, year 2023, sourced from the Coface Top 500 CEE (2023).

### Step 2 — Dictionaries (Appendices A.1–A.4)

| Dictionary | Size | Scoring |
|---|---|---|
| A1 Greenwashing | 1,140 "positive" + 990 "negative" terms | positive = −1, negative = +1 |
| A2 Environmental (E) | 122 terms | membership only |
| A3 Social (S) | 122 terms | membership only |
| A4 Governance (G) | 122 terms | membership only |

Built by compiling candidate terms from existing ESG lexicons and prior studies, manual curation,
then validation on a pilot corpus.

### Step 3 — Comparative sentiment score (Equation 1)

```
Comparative Score = Total Score / Total number of Tokens
```

where Total Score is the sum of A1 polarity values over matched terms in the lemmatised document.
Computed separately for the report and the media text.

### Step 4 — Consistency check (Equation 2)

Pearson correlation *r* between report-derived and media-derived comparative scores, computed
**at country, industry and firm-size level** (not per firm).

### Step 5 — TF–IDF

Standard definitions, as printed:

```
TF-IDF(t, d, D) = TF(t, d) × IDF(t, D)
TF(t, d)        = f(t,d) / N_d
IDF(t, D)       = log( N_D / n_t )
```

### Step 6 — Focus scores

```
Focus Score = Total Number of Keyword Occurrences / Total Number of Tokens
Average Score = (E_focus + S_focus + G_focus) / 3
```

Normalised via **Min–Max scaling to the interval [0, 0.99]**.

### Step 7 — TF–IDF-aggregated ESG components

```
E_tfidf = Σ_{t ∈ E} TF-IDF(t, d, D)
S_tfidf = Σ_{t ∈ S} TF-IDF(t, d, D)
G_tfidf = Σ_{t ∈ G} TF-IDF(t, d, D)
```

### Step 8 — The GSI itself (Section 2.6)

```
GSI = ω_E · E_tfidf + ω_S · S_tfidf + ω_G · G_tfidf
where ω_E = ω_S = ω_G = 1/3
```

Higher = more greenwashing. Equal weights are justified as an "unbiased approach".

---

## 2. What I verified arithmetically

The paper's results tables report variables called **E Washing, S Washing, G Washing** which are
**never formally defined by any equation**. They are, however, the quantities actually tabulated
everywhere. I tested the hypothesis that GSI is simply their unweighted mean:

| Group | E Wash | S Wash | G Wash | Mean of the three | Published GSI |
|---|---|---|---|---|---|
| Whole sample | 0.4474 | 0.6566 | 0.6254 | **0.5765** | **0.5765** |
| Germany | 0.5061 | 0.6602 | 0.6595 | **0.6086** | **0.6086** |
| Poland | 0.4203 | 0.6185 | 0.5853 | **0.5414** | **0.5414** |
| Lithuania | 0.3880 | 0.5953 | 0.5636 | **0.5156** | **0.5157** |

Exact to four decimal places (Lithuania differs by 0.0001, consistent with rounding of the inputs).

**Therefore, confirmed:**

```
GSI = (E_Washing + S_Washing + G_Washing) / 3
```

and the variables the paper calls `E_tfidf`, `S_tfidf`, `G_tfidf` in Section 2.6 are the same
quantities it calls `E Washing`, `S Washing`, `G Washing` in the results tables — after Min–Max
normalisation to [0, 0.99].

This also rules out one alternative reading: the components are **not** the `E Focus / S Focus /
G Focus` variables, which are reported separately and correlate with the Washing scores only at
0.76, 0.65 and 0.64 respectively.

**So the aggregation step is fully recoverable. That is the good news, and it is the smaller half.**

---

## 3. What is ambiguous, underspecified or contradictory

Ordered by how much damage each would do to a replication.

### 3.1 The formula contains no media term at all — CRITICAL

Every input to the published GSI is derived from the firm's **own report**. The media corpus
enters the paper only in Sections 2.2–2.3, which produce the comparative sentiment scores and the
group-level Pearson correlations — and **neither of those quantities appears anywhere in the GSI
equation.**

This directly contradicts the paper's own description of the index:

> Abstract: "a Greenwashing Severity Index (GSI) that captures discrepancies between firms' ESG
> self-representation and external public narratives."
> Introduction: "measures the difference between corporate ESG disclosures and external media
> coverage."

**As specified, the GSI computes no difference of any kind.** It is a weighted sum of ESG keyword
TF–IDF mass in the corporate report. Mechanically, a firm scores higher simply by using more
ESG vocabulary — which the paper's own correlation table corroborates (ESG Focus correlates 0.63
with GSI, and the text concedes "an overall emphasis on ESG in sustainability reporting is
associated with an increase in false propaganda trends").

Three readings are possible, and **the paper does not let us choose between them**:

- **(a)** The media corpus is genuinely absent from the index, and the abstract overstates it.
  This is what the equations say.
- **(b)** The TF–IDF document collection *D* spans both report and media documents, so the IDF
  term carries media information implicitly. The paper never states the composition of *D*.
  Even under this reading the index is not a *discrepancy* measure.
- **(c)** An unstated differencing step (e.g. report-minus-media component scores) was applied in
  the code but omitted from the paper.

**Consequence for us.** Our project's framing describes Davidescu et al. as a *media-anchored*
greenwashing measure. On the published specification that is **not accurate** — it is a
report-internal disclosure-intensity measure. This does not weaken our research question; it
sharpens it, and it changes what we can claim. See `synthesis/open-questions.md`, which resolves
this by building our own explicitly media-anchored index (GSI-media) via GDELT rather than
claiming to reproduce theirs.

### 3.2 The polarity scale is stated two different ways

Section 2.1: A1 terms are marked **−1 / +1**.
Section 2.2: A1 terms carry "a sentiment score ranging from **−3 to +3**".

These are incompatible, and no table of per-term weights is given. If the true scale is graded
(−3…+3), the weights are not recoverable from the paper at all. *Note that this affects the
comparative sentiment score, not the GSI itself* — which is a further sign that the sentiment
machinery is disconnected from the index.

### 3.3 Min–Max normalisation: scope and timing unspecified

Normalisation to [0, 0.99] is stated, but not:
- **Applied to what** — Section 2.4 says "all ESG focus scores", Section 2.5 says the Focus
  scores. Whether the `*_tfidf` sums are normalised before aggregation is inferred, not stated.
  (The arithmetic in §2 implies they must be, since GSI lands in [0, 0.9].)
- **Over which population** — across firms within a pillar (most likely, given the [0,0.99] range
  is achieved), or across pillars, or within country/industry. Min–Max is *population-dependent*,
  so this choice changes every value. **This alone blocks exact replication.**
- Why 0.99 rather than 1.

### 3.4 The document collection D is never defined

IDF depends entirely on *D*. Reports only? Reports + media? Per country? Not stated. Combined with
§3.3 this means the component scores cannot be reproduced even with the same dictionaries.

### 3.5 Sample funnel unexplained

Filtering yields "approximately 320 companies"; the analysis uses 204. The intervening exclusions
are not described.

### 3.6 LDA is described but never used

Section 2.4 sets out LDA with a generative equation (Equation 3), and the abstract lists "topic
modeling" as a GSI component. **No topic-model output appears in the GSI formula or in any results
table.** Either it was exploratory or its role went unreported. Treat "topic modelling" as *not*
part of the index.

### 3.7 Reported statistics that contradict each other

Not replication blockers, but they lower confidence in the reported figures:

- "Given that all GSI values exceed 0.5" — Table 5 gives a **minimum of 0.00063**.
- Sensitivity rank correlations described as ranging "between 0.94 and 0.97" — Table 12 lists
  **0.842** for the environmental-dominant specification.
- Table 5's fourth column is headed "Intercede", which from its values is the **mean**
  (likely a mistranslation).
- The PSM results are called "significant" in the abstract; both ATTs have p > 0.05 and 95%
  CIs spanning zero (0.048, p = 0.077; 0.0403, p = 0.064).

---

## 4. Replication verdict

| Component | Recoverable? |
|---|---|
| Aggregation (equal-weighted mean of three pillar scores) | **Yes — verified to 4 d.p.** |
| Pillar components as TF–IDF sums over 122-term dictionaries | Structure yes, values no |
| Min–Max normalisation population | **No** |
| TF–IDF document collection *D* | **No** |
| Dictionary contents | Appendices A.1–A.4 (in PDF; not yet transcribed — see TODO) |
| Sentiment polarity scale | **No — contradictory** |
| Media contribution to the index | **None present in the published formula** |
| LDA contribution | **None present** |

**Recommendation.** Do not present our work as replicating Davidescu et al.'s GSI. Instead:

1. Implement the aggregation rule as published and verified — it is unambiguous and it *is* their
   index as specified.
2. Build our **own** explicitly media-anchored index (GSI-media, from GDELT tone), stated in full,
   rather than reconstructing an unstated differencing step.
3. Report the §3.1 finding as a contribution in its own right. A widely framed "media-anchored"
   index that contains no media term is a substantive observation about this literature, and it
   independently motivates the comparison our project makes.

**Open TODO.** Transcribe Appendices A.1–A.4 (the four dictionaries) from the PDF into
a data folder when the experiment phase begins. They are printed in the open-access PDF, so the term lists themselves
*are* recoverable even though the weighting scheme is not.
