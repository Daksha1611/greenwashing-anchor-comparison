# Glossary

Plain-language definitions for the terms used across this repository. Ordered roughly from
subject-matter concepts to statistical and data-source terms.

---

### Greenwashing

Making a company look more environmentally responsible than it actually is. In this literature it
is defined as the **gap between "apparent" sustainability performance** (what the company says in
its reports and marketing) **and "real" sustainability performance** (what it actually does —
emissions, violations, practices).

The term dates to 1986 and originally covered misleading environmental *advertising*. Modern
research extends it in two directions: to sustainability *reporting* rather than just marketing,
and — as in Davidescu et al. (2026) — across all three ESG pillars rather than the environmental
one alone.

Two distinct strategies are worth separating (Wang et al. 2025):
- **Selective disclosure** — staying quiet about what went badly.
- **Expressive manipulation** — dressing up what you do report in unverifiable, aspirational language.

### ESG (Environmental, Social, Governance)

The three-part framework used to assess corporate sustainability beyond financial performance:

- **Environmental** — emissions, resource use, pollution, waste.
- **Social** — labour standards, human rights, diversity, community relations, customer welfare.
- **Governance** — board structure, internal controls, transparency, anti-corruption,
  shareholder rights.

ESG **ratings** issued by providers (MSCI, Refinitiv, Sustainalytics) drive real capital
allocation — index inclusion, fund mandates, cost of capital — which is why their accuracy matters
beyond academia. Providers disagree with each other substantially, which is part of the problem.

### Greenwashing Severity Index (GSI)

The composite index from Davidescu et al. (2026). **As published**, it is the equally weighted
mean of three TF–IDF-based ESG term scores computed from a firm's own sustainability report:

```
GSI = ⅓·E_tfidf + ⅓·S_tfidf + ⅓·G_tfidf
```

Higher values are interpreted as more greenwashing. Reported sample mean: 0.5765.

**Important caveat.** The paper describes the GSI as measuring the discrepancy between corporate
disclosure and external media coverage, but **no media term appears in the formula** — every input
comes from the firm's own report. In this repository, "GSI" without qualification means the
formula as published. Our own indices are always written **GSI-media**, **GSI-violation** and
**GSI-emissions** to keep them distinct. See `synthesis/gsi-formula.md`.

### TF–IDF (Term Frequency – Inverse Document Frequency)

A way of scoring how *distinctive* a word is to one document within a collection, rather than just
how often it appears.

- **TF (term frequency)** — how often the word appears in this document, divided by the
  document's length.
- **IDF (inverse document frequency)** — `log(total documents / documents containing the word)`.
  A word appearing in every document gets an IDF near zero; a rare word gets a high one.

Multiply them. The effect: words common everywhere ("company", "sustainability") are suppressed,
while words distinctive to a particular document are amplified.

> **Watch out:** IDF depends on the **document collection** you compute it over. The same word in
> the same report gets a different TF–IDF score depending on what else is in the corpus. This is
> one reason Davidescu et al.'s index is not exactly reproducible — they never state what their
> collection contained.

### Topic modelling / LDA (Latent Dirichlet Allocation)

**Topic modelling** discovers themes running through a collection of documents without being told
what to look for in advance.

**LDA** is the classic algorithm. It assumes each document is a mixture of topics, and each topic
is a mixture of words, then works backwards from the observed words to infer both. A
sustainability report might come out as 40% emissions, 30% workforce, 30% governance.

> Davidescu et al. describe LDA in their methodology, but no topic-model output appears in their
> GSI formula or in any results table. Treat topic modelling as **not** part of that index.

### Propensity score matching (PSM)

A technique for approximating a controlled experiment using observational data.

The problem: you want to compare violator firms with non-violator firms, but violators might
differ systematically — bigger, older, in dirtier industries. Any difference you observe could
just be those characteristics.

PSM fixes this by estimating each firm's *propensity* — its probability of being a violator given
its observable characteristics — and then pairing each violator with a non-violator of nearly
identical propensity. Comparing matched pairs isolates the effect of interest.

- **ATT (average treatment effect on the treated)** — the average outcome difference across
  matched pairs.
- **Caliper** — the maximum propensity distance allowed for a valid match.
- **With/without replacement** — whether one control firm may be matched to several treated firms.

Used by both Gorovaia & Makrominas (993 matched pairs, for sample construction) and Davidescu et
al. (48 and 71 pairs, for estimating an effect).

### Spearman rank correlation (ρ)

Measures whether two variables **rank** items in the same order, from −1 (perfectly reversed)
through 0 (unrelated) to +1 (identical ordering).

Unlike Pearson correlation, it uses only ranks, not raw values — so it doesn't assume a straight-line
relationship and isn't distorted by outliers or by two indices being on different scales.

**Why this project uses it:** our three indices live on incompatible scales (news tone, penalty
dollars, tonnes of CO2e). What we care about is whether they put the *same firms at the top*, and
that is a question about ranks.

### Cohen's κ (kappa)

Measures agreement between two classifiers, **corrected for the agreement you would expect by
chance**.

If two indices each flag the worst 10% of firms, they'll overlap sometimes purely by luck. κ
subtracts that baseline. κ = 0 means agreement no better than chance; κ = 1 means perfect
agreement. Rough convention: below 0.20 slight, 0.21–0.40 fair, 0.41–0.60 moderate, 0.61–0.80
substantial, above 0.80 near-perfect.

> Paired in this project with the **Jaccard index** — the plain overlap of two sets
> (intersection ÷ union), with no chance correction. Reporting both prevents overstating agreement.

### EPA ECHO (Enforcement and Compliance History Online)

The US Environmental Protection Agency's public database of environmental compliance and
enforcement, covering facility inspections, violations, formal enforcement actions and monetary
penalties. Free REST API, no key. https://echo.epa.gov/

Our **GSI-violation** anchor.

> Two structural cautions. **Facilities are not companies** — one corporation may own hundreds of
> facilities under different operating names, so aggregating to parent company is a genuine
> research problem. And **a firm with no recorded violation is not proven clean**, only
> unpenalised (Gorovaia & Makrominas make this asymmetry explicit).

### GHGRP (Greenhouse Gas Reporting Program)

The EPA programme requiring large US facilities to report annual greenhouse gas emissions, browsable
through the **FLIGHT** tool at https://ghgdata.epa.gov/

Our **GSI-emissions** anchor.

> **Reporting threshold: 25,000 metric tons CO2e per year.** Smaller emitters and most
> service-sector firms are absent entirely, which biases any GHGRP-based sample toward industrial
> firms. Covers **direct (Scope 1)** emissions at US facilities only. Usefully, it publishes a
> `PARENT_COMPANY` field — the best available shortcut for company-to-facility matching.

**Emission scopes:** *Scope 1* — direct emissions from sources the company owns.
*Scope 2* — indirect emissions from purchased energy. *Scope 3* — everything else in the value
chain. GHGRP is Scope 1; Peng et al. used Scope 1+2, so the two are **not** directly comparable.

### GDELT tone

**GDELT** (Global Database of Events, Language, and Tone) continuously monitors global news and
computes, among much else, a **tone score** for each article — roughly −100 to +100, in practice
mostly −10 to +10, where negative indicates negative coverage. Free, no API key.
https://www.gdeltproject.org/

Our **GSI-media** anchor.

> Chosen over NewsAPI because NewsAPI's free tier returns roughly one month of history, far too
> little for a multi-year panel. GDELT's `V2Tone` field bundles average tone with positive/negative
> scores, polarity and reference densities.
>
> **Coverage volume is retained as a separate variable, not discarded** — the number of articles
> about a firm is a direct measure of its media visibility, and it is the key regressor in the
> salience hypothesis this project tests.

### ClimateBERT

A family of language models pre-trained on climate-related text, including a classifier that
distinguishes **commitments** (promises about the future) from **actions** (things actually done).
https://huggingface.co/climatebert

Our disclosure-side measure, and the English-language analogue of Wang et al.'s
symbolic-versus-substantive distinction.

> **Not FinBERT.** FinBERT is trained on financial sentiment — bullish versus bearish analyst
> language. Wrong domain for climate disclosure text.

### Salience hypothesis

This project's central conjecture: that media-anchored greenwashing measures largely track **how
visible a firm is** — its size, newsworthiness and volume of press coverage — rather than how much
it actually greenwashes. Tested by regressing GSI-media on firm size and media coverage volume
with sector fixed effects.

### Reality anchor

Our term for the external, non-textual fact a greenwashing measure is validated against —
violations, emissions, media coverage, or nothing. The organising column of
`synthesis/comparison.md`, and the axis along which this project's contribution is defined.
