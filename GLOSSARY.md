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

The extended literature adds two anchor types to the original four: the **ratings gap** (a
disclosure score minus a performance score) and **controversy** (negative news events, as opposed
to average media tone). See the entries below.

---

## Added with the extended literature (notes 06–24)

### Cheap talk / ClimateBERT CTI

**Cheap talk** is climate language that costs the firm nothing to say and commits it to nothing:
vague, non-specific statements about intentions rather than concrete, checkable commitments.

Bingler et al. (2022, 2024) use **ClimateBERT**, a language model fine-tuned on climate text, to
find it. The 2024 paper turns this into the **cheap talk index (CTI)**, which † measures the
share of imprecise versus precise climate commitments in a report. They then relate the CTI to
climate initiatives, emissions and negative news. († = from our research brief; the abstract does
not define the index.)

> Not the same as the "symbolic" side of Wang et al.'s split, though closely related: both
> separate vague aspiration from verifiable action.

### Counter-accounting

Setting a company's own account of itself against **independent information** about the same
company, such as news events, NGO reports or regulatory records, to see what the company left
out. Boiral (2013) does it by hand: he compared 23 GRI A/A+ reports against 116 significant news
events and found that 90 per cent of the significant negative events were not reported.

Our proposal (Improvement 4) is to automate it as an **omission rate**: the share of a firm's
negative, environment-themed news events that its report never mentions.

### Ratings-gap greenwashing score (disclosure minus performance)

The most common way empirical finance and accounting papers measure greenwashing. Take a
commercial **ESG disclosure score** (how much the firm reports) and a commercial **ESG
performance score** (how well it does), standardise both, and subtract:

```
greenwashing = standardised disclosure score − standardised performance score
```

A high value means disclosure runs ahead of performance. Yu et al. (2020) define it; Luu et al.
(2025) and Liu et al. (2024) † use it. Both halves are **third-party scores**, so the measure
inherits the biases of the ratings (see *Size bias* and *Rating disagreement*). In this repository
it is a **reality-anchor type of its own**, and our proposed fourth index is **GSI-ratings**.

### ESG controversy score

A score that rates a company by **negative news events** (scandals, lawsuits, accidents,
allegations) that involve it, built by a data provider from media coverage. It is used as the
"outside" side of some greenwashing measures (Ghitti et al. †, Bacher et al. †, and as a possible
misconduct input in Dorfleitner & Utz). It is different from **average media tone**, which is what
our planned GDELT measure uses: a controversy score counts what happened, tone describes how
coverage sounded.

> Because it comes from news, a controversy score is exposed to the visibility problem: well-known
> firms get more coverage of everything they do wrong.

### Rating disagreement

The fact that different ESG data providers give the same company different scores. Gibson Brandon
et al. (2021) study seven providers for S&P 500 firms, find that stock returns are positively
related to disagreement (mainly on the environmental dimension), and † report an average
correlation between providers of about 0.45. For us it is both a model and a warning: it is the
same exercise we propose for greenwashing indices, and it shows that "measuring the same concept"
does not guarantee agreement.

### Size bias

The tendency of a score to rise with **firm size**, independently of conduct. Drempetic et al.
(2020) † find that firm size, the resources available for producing ESG data and data
availability all raise a firm's ESG score, favouring large firms. A follow-up (Dobrick et al.,
2023) † reports that it persists in Refinitiv data. It is the main prior evidence for our
**salience hypothesis**.

### Legitimacy theory vs voluntary disclosure theory

Two competing explanations for why firms disclose environmental information, with opposite
predictions about who talks more.

- **Legitimacy theory.** Firms disclose to keep their social licence to operate. Firms under
  pressure, such as those that have just caused a spill or been fined, talk *more*. Supported by
  Gorovaia & Makrominas (violators write more), Cho et al. (disclosure tracks exposure) and Cho
  (2009).
- **Voluntary disclosure theory.** Firms with good news tell the market, so good performers
  disclose *more*. Supported by Clarkson et al. † and Tadros & Magnan.

Which one the data support seems to depend on what is counted: volume and tone, or hard
verifiable items. See `synthesis/extended-literature.md` §3.2.

### MTMM matrix (multi-trait multi-method)

A standard way to test whether several measures are measuring the same thing. You take one
underlying **trait** (here, greenwashing), measure it by several **methods** (here, the anchors),
and lay out all the correlations in one matrix. If the methods are valid, measures of the same
trait should agree more than measures of different traits, and measures that share a method type
should not agree only because of that shared method. In our design: do the violation and emissions
indices (both "hard" anchors) correlate with each other more than with the media index?

### Predictive validity

How well a measure predicts something it *should* predict later. If two greenwashing indices
disagree, the one that better predicts **next-year EPA penalties**, say, has the stronger claim to
measure real conduct. Liu et al. (crash risk), Ghitti et al. † (firm value) and Bacher et al.
(asset prices) validate against market outcomes; we would put conduct outcomes first, because
market outcomes can themselves reflect visibility. (Hypothesis H6.)

### Quasi-natural experiment / difference-in-differences

A **quasi-natural experiment** is an event or rule that affects some firms and not others, in a
way the firms did not choose, so it works like an experiment without one being run.
**Difference-in-differences (DiD)** compares how the affected ("treated") group changes before and
after the event, against how an unaffected ("control") group changes over the same period.

Luu et al. (2025) use the US GHGRP, which required large emitters to report from 2010, as the
event: 134 treated firms against 2,597 controls. Gorovaia & Makrominas use a staggered version for
the effect of a violation. For us, the GHGRP gives a test of whether an index responds to a real
policy change (Hypothesis H7).
