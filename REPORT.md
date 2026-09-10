# Greenwashing Detection: Do Different Ways of Measuring It Agree?

**A review of five papers — what they show, how they connect, and the project idea that comes out of them**

Business Economics project · initial review phase

---

## Contents

1. [What this report is about](#1-what-this-report-is-about)
2. [The five papers, one by one](#2-the-five-papers-one-by-one)
3. [What the papers agree on](#3-what-the-papers-agree-on)
4. [The gap nobody has filled](#4-the-gap-nobody-has-filled)
5. [The project idea](#5-the-project-idea)
6. [Datasets we would need to implement this](#6-datasets-we-would-need-to-implement-this)
7. [Where the project stands, and how we plan to improve it](#7-where-the-project-stands-and-how-we-plan-to-improve-it)
8. [Quick reference: terms](#8-quick-reference-terms)

---

## 1. What this report is about

**The common topic:** companies say a lot about how green they are. Some of them
are lying. Can we catch them automatically?

The word for the lying is **greenwashing** — making a company look more
environmentally responsible than it actually is. Researchers define it as the
gap between two things:

- **what a company says** — its sustainability report, its press releases, its
  glossy "our commitment to the planet" pages; and
- **what a company does** — its actual emissions, its pollution fines, its real
  operations.

If the talk is much better than the actions, that's greenwashing.

**The measurement problem.** To catch greenwashing automatically you need both
halves of that gap as numbers. The "talk" half is reasonably easy — you feed the
sustainability report to a computer and score the language. The **"do" half is
the hard part.** What counts as the truth about a company's actual
environmental behaviour?

Different researchers have picked different answers, and this report calls that
choice the **reality anchor**:

| Reality anchor | What it means |
|---|---|
| **Violations** | Has the government fined this company for breaking environmental law? |
| **Emissions** | How much carbon does this company actually put in the air? |
| **Media** | What does the press say about this company's environmental record? |
| **None** | Just analyse the report's language and don't check it against anything |

**This is the central problem the project addresses.** All four choices exist in published,
peer-reviewed research. Everybody picks one and stops. **Nobody has checked
whether they give the same answer.** If you rank companies from worst to best
greenwasher using violations, and then rank them again using media coverage, do
you get the same list — or two completely different lists?

That matters, because if they disagree, then at least one of these published
methods isn't measuring greenwashing at all. It's measuring something else.

**What we did:** read all five papers, summarised them in plain language, worked
out what they agree on, identified the specific gap between them, and designed
an experiment that would test it. No experiments have been run yet — this is the
review phase.

---

## 2. The five papers, one by one

### Paper 1 — Detecting Greenwashing in ESG Disclosure (the "GSI" paper)

*Davidescu, Manta, Bîrlan, Miler & Niță (2026). Sustainability, 18(3), 1486.*

**What they did.** Took 204 big companies in Central and Eastern Europe, collected
their sustainability reports and news coverage about them, and built a score
called the **Greenwashing Severity Index (GSI)**. They describe it as measuring
the gap between what a company says about itself and what the press says about it.

**What we understood.**

- The method is dictionary-based. They built four word lists by hand: a
  greenwashing list (1,140 "good" words like *sustainability* and *ethical*, and
  990 "bad" words like *pollution* and *eco-fraud*), plus separate 122-word lists
  for Environmental, Social and Governance terms.
- They count how often those words show up, weight them with **TF-IDF** (a
  standard technique that boosts words distinctive to one document and suppresses
  words that appear everywhere), and combine them into one number per company.
- Average GSI was **0.5765**, which they read as "moderate greenwashing
  everywhere". Germany scored worst (0.6086), Lithuania best (0.5157). Finance,
  online commerce and aviation were the worst industries; construction the best.
- **Big companies scored better** (0.49) than small ones, which they explain as
  large firms being under more scrutiny so they behave better.

**The problem we found — this is important.** We worked through their formula
carefully. It is:

```
GSI = ⅓ × (Environmental score) + ⅓ × (Social score) + ⅓ × (Governance score)
```

Every single one of those three inputs is calculated **from the company's own
report**. The news articles they collected never enter the formula. They're used
in a separate side-analysis and then dropped.

So despite the paper saying the GSI measures the gap between company talk and
press coverage, **the published formula computes no gap at all.** It measures how
densely a report is packed with ESG buzzwords. A company that writes the word
"sustainability" more often gets a higher greenwashing score — regardless of what
it actually does, and regardless of what the press says.

**What could be improved.** Besides the formula issue, we found several things
that don't hold up:

- The paper's main claim — that companies which emphasise one ESG pillar over the
  others show "significantly higher" greenwashing — is **not statistically significant** — the two tests give p = 0.077
  and p = 0.064, both above the usual 0.05 cutoff, and both confidence intervals
  include zero.
- The text says "all GSI values exceed 0.5", but their own table reports a
  minimum of 0.00063.
- The word-scoring scale is described two contradictory ways (−1/+1 in one
  section, −3 to +3 in another).
- They describe using topic modelling, but no topic-modelling result appears
  anywhere in the index or the tables.

We wrote this up in detail in [`synthesis/gsi-formula.md`](synthesis/gsi-formula.md)
because the project originally planned to replicate this index.

---

### Paper 2 — Identifying Greenwashing Using Natural-Language Processing

*Gorovaia & Makrominas (2025). European Financial Management, 31(1), 427–462.*

**What they did.** The cleanest idea in the set. Split US companies into two
groups using a hard, external fact — **has this company been fined for an
environmental violation, yes or no?** — then read both groups' sustainability
reports and asked: do polluters write differently?

**What we understood.**

- They were careful about sample bias. Instead of grabbing whatever reports were
  easy to find (which would over-select big, green, well-organised companies),
  they started from the full population of firms, statistically matched each
  violator to a similar non-violator, and only *then* went looking for reports.
  That gave **993 matched pairs**, 1,120 reports, 441 companies, 2008–2022.
- Polluters write **longer** reports: 20,304 words vs 15,091.
- Polluters write **more positively**: 0.823 vs 0.816.
- Polluters write **more about the environment**: 0.185 vs 0.175.
- Polluters write **less readably** — more dense, harder to follow.
- All of those differences are statistically significant at the 1% level
  (readability is the exception, not significant).
- **The strongest finding:** companies *change* how they write right after
  getting caught. Their difference-in-differences test — which compares the same
  firm before and after a violation — shows environmental content jumping
  significantly (effect 0.175, p < 0.001) once a firm becomes a violator.

So a company that just polluted responds by writing more, sounding happier, and
talking about the environment more. That's greenwashing caught in the act.

**What could be improved.**

- The authors are honest about a real limitation: a fine proves guilt, but **no
  fine doesn't prove innocence.** A "clean" firm might just not have been caught.
- Their violation data comes from commercial databases (MSCI, Refinitiv), not
  from the environmental regulator directly. Our project would use the regulator's
  own records instead, which is a slight improvement.

---

### Paper 3 — Do Environmental Scores Become a "Greenwashing" Tool?

*Peng, Li, Tang, Lan & Cui (2024). Business Strategy and the Environment, 33(3), 2084–2115.*

**What they did.** No text analysis at all — this one is pure numbers. Take the
**environmental score** that rating agencies assign to big companies (the kind
that drives investment decisions), and check it against how much carbon those
companies actually emit. 199 Fortune Global 500 companies, 27 countries,
2001–2020.

**What we understood.**

- The obvious expectation: high environmental score should mean low emissions.
- **They found the opposite.** Higher environmental scores go with *higher*
  emissions. The effect is strong and statistically solid (coefficient 0.775 for
  absolute emissions, 1.304 for emissions per unit of sales, both significant at
  the 1% level).
- In other words, the score companies get for being green is positively related
  to how much they pollute. It's working as a cover story.
- **Forcing companies to disclose didn't fix it.** The effect holds in countries
  with mandatory disclosure rules and is, if anything, *larger* there.
- **The Paris Agreement didn't fix it either.** And in countries with strong
  hierarchical culture, it got worse afterwards.

**Why this paper matters so much for us.** It proves the "reality check" approach
works, using a totally different method from Paper 2 — and reaches the same
conclusion. Two independent anchors, two independent methods, one answer:
**companies that talk greener often perform worse.**

**What could be improved.**

- The environmental scores come from a single rating provider, and rating
  providers famously disagree with each other.
- The culture measures are static — they can't capture change over the 20 years
  studied.
- Financial firms are excluded entirely.

---

### Paper 4 — Corporate Greenwashing Index: A Deep Learning Approach

*Wang, Gao & Sun (2025). EPJ Data Science, 14, 44.*

**What they did.** The most technically advanced text method in the set. Used
**MacBERT** — a modern AI language model — to read Chinese company reports
sentence by sentence and score greenwashing. 9,534 company-years, 2008–2023.

**What we understood.**

- They split greenwashing into two separate behaviours, which is a genuinely
  useful idea:
  - **Selective disclosure** — staying quiet about the things you did badly.
    Measured as the share of required topics the company simply didn't mention.
  - **Expressive manipulation** — dressing up what you *do* say. Measured as the
    share of statements that are vague and aspirational rather than concrete and
    checkable.
- A statement counts as **substantive** if it's verifiable and hard to fake —
  actual numbers, specific case studies. It counts as **symbolic** if it's just
  aspiration, vague qualitative claims, or last year's wording recycled.
- The two get combined using a **geometric mean** (multiply them, take the square
  root) rather than a simple average. That's deliberate: a company only scores
  badly overall if it does *both* things. With a simple average, one bad
  component could carry the whole score.
- The AI agrees with human labellers **97.79%** of the time on the first
  component and **95.13%** on the second.

**Why they used an AI model instead of word lists.** This is the key methodological
lesson, and it's a direct criticism of Paper 1's approach: a keyword list
**cannot** tell a real commitment from a vague aspiration, because both use exactly
the same words. "We are committed to reducing emissions" and "We reduced
emissions by 12% in 2023" share most of their vocabulary but mean completely
different things. Only a model that reads context can separate them.

**What could be improved.**

- **The index never checks against reality.** Both components are computed purely
  from the report's own text. That 97.79% accuracy figure means the AI agrees
  with *human readers* — not that it agrees with whether the company actually
  pollutes.
- The authors never claim otherwise. This is the same weakness as Paper 1, but
  this paper is open about it.
- Chinese A-share companies under a specific disclosure regime — transfer to US
  companies is untested.

---

### Paper 5 — Mapping the Greenwashing Research Landscape

*Forliano, Battisti, de Bernardi & Kliestik (2025). Review of Managerial Science, 19, 3407–3456.*

**What it is.** Not an experiment — a systematic review that maps the whole
research field. They collected **97 peer-reviewed articles** from the two main
academic databases and analysed the structure of the literature.

**What we understood.**

- The field splits into four themes: (1) symbolic management and CSR
  communication, (2) environmental regulation and institutional complexity,
  (3) performance and sustainable practices, (4) marketing, perception and trust.
- Research is dominated by **macro-level theories** — legitimacy theory (firms
  talk green to stay socially acceptable), institutional theory (rules and norms
  shape behaviour), and stakeholder theory (firms respond to whoever has power
  over them).
- They propose organising the field across three levels: macro (society), meso
  (the organisation), micro (individual people).

**How useful it is for us — moderately.** Two limits are worth stating clearly:

- It maps **theories**, not **measurement methods**. It doesn't compare
  violation-anchored vs media-anchored vs emissions-anchored approaches. So it
  gives us context and vocabulary, but it does **not** prove our specific gap
  exists.
- Its coverage closed in **February 2025** — before Papers 1 and 4 were published.
  The two most methodologically relevant papers in our set aren't in the map.

What it *does* usefully confirm: the field genuinely does define and measure
greenwashing in inconsistent ways. That's consistent with our worry that
different measures may not be measuring the same thing.

---

## 3. What the papers agree on

Reading them together, four points come up repeatedly:

1. **The talk–action gap is real, and it's been proven twice independently.**
   Paper 2 checks against fines and finds polluters write more and better.
   Paper 3 checks against carbon and finds high scorers emit more. Different
   anchors, different methods, same conclusion. This is the most solid finding
   in the set.

2. **More disclosure does not mean more honesty.** Paper 3 shows mandatory
   disclosure rules didn't close the gap. Paper 1 finds that companies emphasising
   ESG more score *worse*, not better. Paper 2 finds violators write the longest
   reports of all. Forcing companies to say more just produces more sophisticated
   talk.

3. **Word-counting is not good enough.** Paper 4 makes the case explicitly:
   dictionaries can't separate a real commitment from an empty one because the
   vocabulary is identical. Papers 1's method is exactly the dictionary approach
   Paper 4 argues against.

4. **Companies react strategically to being caught.** Paper 2's before-and-after
   test is the clearest evidence: get fined, then immediately write more
   environmental content in a more positive tone.

---

## 4. The gap nobody has filled

Here is the situation, laid out plainly:

| Paper | What it checks green talk against |
|---|---|
| Paper 2 (Gorovaia & Makrominas) | Environmental fines |
| Paper 3 (Peng et al.) | Measured carbon emissions |
| Paper 4 (Wang et al.) | **Nothing** — by explicit design |
| Paper 1 (Davidescu et al.) | **Nothing** — media claimed, but not actually in the formula |

**Every paper commits to one anchor and stops.** There is not a single statistic
anywhere in this literature comparing one greenwashing measure against another —
no correlation, no overlap test, nothing.

### Why this matters — two of the papers contradict each other

Look at what Papers 1 and 3 each say about **big companies**:

- **Paper 1:** big companies are the *cleanest* (score 0.49, well below the 0.5765
  average). Their explanation: large firms are watched closely, so they behave.
- **Paper 3:** studies *only* very large companies — the Fortune Global 500 — and
  finds systematic greenwashing throughout.

Both are peer-reviewed. Both can't be straightforwardly right. There's one
explanation that makes both true at once:

> The text/media-based measure isn't detecting greenwashing in big companies at
> all. It's detecting that big companies have **professional communications
> departments** — they write polished reports, they get lots of press coverage,
> they know how to sound credible.

We call this the **visibility problem** (or *salience hypothesis*): media-based
greenwashing measures may largely be measuring **how visible a company is**, not
how much it lies.

Nobody has tested it. And notably, **the authors of Paper 1 ask for exactly this
test themselves** — their own suggested next step is to check NLP-based
greenwashing indicators against real environmental outcomes like emissions data
and enforcement actions.

### Why it matters beyond academia

ESG ratings move real money — which funds buy which stocks, what companies pay to
borrow. Paper 3 already showed one widely used commercial environmental score is
positively linked to the pollution it's supposed to measure inversely.

Academic greenwashing indices are being proposed as the *fix* for those flawed
ratings. If the fix shares the same flaw — rewarding visibility and polished
writing rather than actual conduct — then it reproduces the problem it was built
to solve. And media-based measures are the ones most likely to be adopted widely,
because news data is cheap, global and constantly updated in a way that
regulatory records aren't.

---

## 5. The project idea

**The research question:**

> Do greenwashing measures built on media sentiment identify the same companies as
> measures built on regulatory violation records — or is media-based greenwashing
> detection largely measuring how visible a company is?

### The design in one picture

Take **the same 150–300 US companies**. Score their sustainability reports once
(the "talk"). Then check that talk against **three different realities** and see
whether the three resulting rankings agree.

```
        The same 150-300 US-listed companies
                        │
         Score their sustainability reports
        (ClimateBERT: promises vs actual actions)
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
    GSI-media     GSI-violation   GSI-emissions
   talk vs press   talk vs fines   talk vs carbon
     (GDELT)        (EPA ECHO)       (EPA GHGRP)
        │               │               │
        └───────────────┼───────────────┘
                        ▼
        Do the three rankings agree?
   ┌────────────────────┴────────────────────┐
   ▼                                         ▼
 THEY AGREE                            THEY DISAGREE
 media measures are                    at least one is not
 a valid cheap proxy                   measuring greenwashing
```

### What we'd actually test

1. **Do the rankings match overall?** Using **Spearman rank correlation** — a
   measure of whether two lists put things in the same order, from −1 (exactly
   reversed) through 0 (unrelated) to +1 (identical).

2. **Do they agree on the worst offenders?** This matters more than the overall
   correlation. Take the worst 10% under each measure and see how much those
   groups overlap, using the **Jaccard index** (plain overlap) and **Cohen's κ**
   (overlap corrected for what you'd expect by luck). Two lists can look
   reasonably correlated overall while completely disagreeing about who the worst
   companies are — and the worst companies are the only ones anyone acts on.

3. **Is the media measure just tracking visibility?** Run a regression predicting
   the media-based score from **company size** and **how many news articles
   mention the company**. If those two things explain most of it, the salience
   hypothesis is supported.

### One design decision worth understanding

We build the company list from **emissions and filing records first**, and only
*then* go looking for sustainability reports — never the other way round.

This copies Paper 2's careful sampling. If you start by collecting whatever
reports are easy to find, you automatically over-select big, visible, well-resourced
companies — which are exactly the companies our hypothesis is about. That would
spoil the result before we started.

### An honest note on what we can claim

Because Paper 1's index turned out not to contain a media component (Section 2),
we **cannot** describe this project as "replicating the media-anchored index and
comparing it". We build our own media-anchored measure, specify it fully
ourselves, and say so. The discovery about Paper 1's formula becomes a finding in
its own right rather than a foundation we build on.

---

## 6. Datasets we would need to implement this

Everything here is **free**. Full detail with access notes and field lists is in
[`synthesis/datasets-and-access.md`](synthesis/datasets-and-access.md).

| Source | What it gives us | Access |
|---|---|---|
| **GDELT** | Global news with a computed **tone score** per article — our media anchor | Free, no key |
| **EPA ECHO** | US environmental violations, inspections, fines — our violation anchor | Free REST API, no key |
| **EPA GHGRP** | Facility-level greenhouse gas emissions — our emissions anchor | Free download |
| **SEC EDGAR** | Company filings and the official company ID (CIK) that ties everything together | Free; requires a contact email in requests |
| **Responsibility Reports** | Free archive of sustainability report PDFs | Free, needs scraping |
| **CDP** | Standardised climate disclosures | Partly licensed — optional |

**Why GDELT and not NewsAPI:** NewsAPI's free tier only gives about one month of
history. We need several years.

**The model: ClimateBERT, not FinBERT.** ClimateBERT is trained on climate text
and can distinguish a *commitment* (a promise about the future) from an *action*
(something actually done) — which is precisely the distinction Paper 4 showed
matters. FinBERT is trained on financial sentiment (bullish vs bearish) and is
the wrong tool.

### The hardest practical problem

**Connecting company names to facility records.** The EPA tracks *facilities*, not
companies. One corporation might own 200 facilities under 50 different operating
names, and ownership changes over time. There is no shared ID between the news
data, the EPA data and the stock market data.

This matters more than it sounds, and here's the trap: **bad matching creates
noise, and noise pushes correlations toward zero — which is exactly the result
our hypothesis predicts.** So sloppy data work would "prove" our hypothesis for
completely the wrong reason. Any finding of disagreement is only believable if we
measure and report how well the matching worked.

One useful shortcut: the EPA's emissions database publishes a `PARENT_COMPANY`
field, which does part of this job for us.

---

## 7. Where the project stands, and how we plan to improve it

### 7.1 What the project is right now

**Right now this project is a literature review and a research design. Nothing has
been built or measured.**

Concretely, what exists today:

| What | Status |
|---|---|
| Five papers read in full and annotated | Done — `notes/01`–`notes/05` |
| Paper 1's index reconstructed and verified | Done — `synthesis/gsi-formula.md` |
| Papers compared side by side | Done — `synthesis/comparison.md` |
| Data sources identified with access notes | Done — `synthesis/datasets-and-access.md` |
| Research question and hypotheses | Written — `synthesis/open-questions.md` |
| Sixth paper | **Not obtained** |
| Company sample | **Not built** — no list of firms exists yet |
| Data retrieved from any source | **None** |
| Any index computed | **None** |
| Code | **None** — deliberately, this phase is reading and design |

So the honest description is: **we understand the problem and we know what we
would build. We have not started building it.**

**What the review has actually produced** — three things worth keeping:

1. **A framing.** The "reality anchor" idea — that the interesting difference
   between these papers is *what they check green talk against* — is our own
   organising concept, and it turns five loosely related papers into one clear
   question.
2. **A verified finding.** Paper 1's Greenwashing Severity Index does not contain
   the media component the paper says it does. We confirmed this by checking the
   arithmetic against the authors' own published tables. This is publishable on its own.
3. **A design that follows from the gap** rather than one imposed on it, including
   sampling choices copied from the most methodologically careful paper in the set.

### 7.2 How we hope to improve on the existing work

Five specific improvements, each one answering a weakness we found:

**1. Compare anchors instead of picking one.**
Every paper reviewed commits to a single reality anchor and stops. We compute
three on the same companies and measure whether they agree. This is the core
contribution and nothing in the literature does it.

**2. Use a language model instead of word lists.**
Paper 1 counts dictionary words. Paper 4 demonstrates why that fails: "we are
committed to reducing emissions" and "we cut emissions 12% in 2023" share almost
all their vocabulary but mean opposite things. We use ClimateBERT's
commitment-versus-action distinction, which is the English equivalent of what
Paper 4 did for Chinese.

**3. Use the regulator's own records, not a commercial database.**
Paper 2 identifies violators through MSCI and Refinitiv fields. We go to EPA ECHO
directly — the primary source those databases are themselves derived from. Fewer
intermediaries, and the full violation history rather than a summary flag.

**4. Specify the index fully, so it can be replicated.**
Paper 1's index cannot be reproduced from the paper: the normalisation population
and the document collection are both unstated. Whatever we build, every step will be
written down in enough detail that someone else can rebuild it. Having found this
problem in another paper, it would be a bad result to repeat it in our own.

**5. Test the thing that would invalidate our own result.**
Bad company-to-facility matching produces noise, noise pushes correlations toward
zero, and low correlation is exactly what our hypothesis predicts. So sloppy data
work would "confirm" our hypothesis for entirely the wrong reason. We measure the
match rate and re-run everything on the high-confidence subset. A disagreement
result is only believable if this check passes.

### 7.3 The technical part

Everything below is free and open. No paid data subscription, no commercial ESG
database, no GPU strictly required.

**Language and core libraries**

| Component | Choice | Why |
|---|---|---|
| Language | **Python 3.11+** | Standard for this kind of work |
| PDF text extraction | **pypdf** | PyPDF2 is deprecated and must not be used |
| Sentence splitting | **spaCy** | Sustainability reports are full of bullets, headings and table fragments that naive splitting mangles |
| Language model | **transformers** (Hugging Face) | Runs ClimateBERT |
| Data handling | **pandas** | Standard |
| Statistics | **scipy.stats**, **statsmodels**, **scikit-learn** | Spearman, regression, Cohen's κ respectively |
| Web requests | **requests** | All four data sources are plain web APIs |

**The model: ClimateBERT, not FinBERT.** ClimateBERT is a BERT-family model
pre-trained on climate text, with a classifier that separates a *commitment* (a
promise about the future) from an *action* (something actually done). That is
exactly the distinction that makes a greenwashing measure work. **FinBERT is the
wrong tool** — it is trained on financial sentiment, meaning bullish versus
bearish analyst language, which has nothing to do with environmental claims.

It is a small model by modern standards (roughly 110 million internal settings, far
smaller than GPT-scale models), so it runs on an ordinary laptop processor. A
graphics card would make it faster but is not needed at this sample size.

**The four data interfaces**

| Source | Interface | Auth | Main technical catch |
|---|---|---|---|
| **GDELT** | DOC 2.0 web API; BigQuery for bulk history | None | ~250 articles per query and a rolling window — long histories need BigQuery. Parse the `V2Tone` field, which packs seven comma-separated values |
| **EPA ECHO** | Web API (`get_facilities`, `detailed_facility_report`, `get_case_report`) | None | Paginated; broad queries time out, so filter by state or industry code. Several fields are fixed 3- or 5-year lookbacks, **not** annual values — treating them as yearly would be a serious error |
| **EPA GHGRP** | Annual bulk download; Envirofacts API | None | Only covers facilities emitting 25,000+ tonnes CO2e/year. Publishes a `PARENT_COMPANY` field — the single most useful shortcut we have |
| **SEC EDGAR** | `data.sec.gov` submissions API; full-text search | None, but a contact email in the `User-Agent` header is **mandatory** — requests without one are refused | Hard enforced limit of 10 requests/second |

**The pipeline**

```
   Build the company list FIRST
   (GHGRP emitters  ->  matched to SEC CIK  ->  150-300 firms)
                        │
        then go and fetch their sustainability reports
                        │
                        ▼
              pypdf  ->  spaCy sentence split
                        │
                        ▼
              ClimateBERT: commitment vs action
                        │
                = the "talk" score
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
     GDELT           EPA ECHO        EPA GHGRP
    tone score      violations       emissions
        │               │               │
        └───────────────┼───────────────┘
                        ▼
        GSI-media / GSI-violation / GSI-emissions
                        │
                        ▼
     scipy: Spearman  |  sklearn: Cohen's kappa
             statsmodels: salience regression
```

**Why the company list is built first.** This is a technical decision with a
statistical reason. If you start by collecting whatever sustainability reports are
easy to find, you automatically over-select large, visible, well-resourced firms —
which are precisely the firms the salience hypothesis is about. The sample would be spoiled
before any analysis began. Paper 2 solved this by matching firms *before*
looking for reports, and we copy that ordering.

**The hard engineering problem: entity matching.**
The EPA tracks **facilities**. The stock market tracks **companies**. GDELT tracks
**free-text names**. There is no shared identifier anywhere.

One corporation may own 200 facilities under 50 operating names, and ownership
changes year to year — so matches must be year-aware, not static. There are also simpler problems: legal
endings (INC, CORP, LLC, HOLDINGS), and names that are genuinely ambiguous, where
"Delta" could be an airline or a tap manufacturer.

The plan, in order of reliability: start from GHGRP's `PARENT_COMPANY` field, bridge
into ECHO through the shared facility registry ID, then exact matching on cleaned-up
names, then approximate ("fuzzy") matching **checked by hand**, then hand-coding
whatever is left.
At 150–300 firms, hand-checking the remainder is perhaps a day of work and worth
doing properly.

**Engineering practices that matter here**

- **Save every API response the first time it is fetched.** GDELT and ECHO are live
  databases that change over time; without saved copies, results cannot be repeated. Record the
  retrieval date alongside the data.
- **Fix the analysis parameters before computing anything** — the correlation
  threshold, the "worst 10%" cutoff, the regression specification. Otherwise the
  analysis can be tuned, consciously or not, until it produces an interesting answer.
- **Log extraction failures rather than dropping them silently.** A PDF that fails
  to parse is a missing company, and image-only PDFs correlate with smaller, older
  firms — so silent failures would quietly reshape the sample.
- **Keep article *volume* as its own variable.** It is not a diagnostic to be
  discarded after fetching tone; the number of articles about a firm is the direct
  measure of visibility, and it is the key regressor in the salience test.

### 7.4 Immediate next steps

1. **Obtain the sixth paper** — *Detecting greenwashing behaviour in decarbonization
   performance* (Accounting & Finance, 2025). Its title suggests another
   emissions-based anchor, directly relevant to the comparison.
2. **Build the company list.** Match GHGRP emitters to SEC CIKs and get to a clean
   150–300 firms. Everything depends on this and it is the part most likely to go wrong.
3. **Do GDELT first.** No key and no facility matching are needed, just company-name
   queries. It is the quickest way to get one full path working from end to end.
4. **Then EPA ECHO and GHGRP**, then compute the three indices and compare.

A cheap early result is available before any of that: since Paper 1's index reduces
to "how many ESG buzzwords are in the report", we can test whether that *alone*
correlates with any real-world anchor. If it doesn't, that says something about a
whole family of dictionary-based methods.

---

## 8. Quick reference: terms

| Term | Plain meaning |
|------|---------------|
| **Greenwashing** | Making a company look more environmentally responsible than it actually is — the gap between green talk and real conduct. |
| **ESG** | Environmental, Social, Governance — the three-part framework for rating companies on non-financial performance. |
| **ESG rating** | A score assigned by a commercial provider (MSCI, Refinitiv). Drives real investment decisions, which is why accuracy matters. |
| **Reality anchor** | Our term for the external fact a greenwashing measure is checked against — fines, emissions, media, or nothing. |
| **Sustainability / CSR report** | The voluntary annual document where a company describes its environmental and social performance. |
| **GSI** | Greenwashing Severity Index — the score from Paper 1. |
| **TF-IDF** | A way of scoring how distinctive a word is to one document. Common words get suppressed, distinctive ones amplified. |
| **Topic modelling / LDA** | Automatically finding the themes running through a set of documents without being told what to look for. |
| **Propensity score matching** | Pairing each "treated" company (e.g. a polluter) with a very similar untreated one, so you compare like with like. |
| **Difference-in-differences** | Comparing the same companies before and after an event, against a control group — good evidence of cause, not just correlation. |
| **Spearman correlation** | Whether two lists rank things in the same order. −1 = reversed, 0 = unrelated, +1 = identical. |
| **Jaccard index** | How much two sets overlap: the shared members divided by the total distinct members. |
| **Cohen's κ** | Agreement between two classifications, corrected for the agreement you'd get by pure chance. |
| **EPA ECHO** | The US environmental regulator's public database of violations, inspections and fines. |
| **GHGRP** | The US programme requiring large facilities to report greenhouse gas emissions. Only covers big emitters (25,000+ tonnes CO2e/year). |
| **GDELT** | A free global news database that computes a **tone** score for each article, roughly −100 (negative) to +100 (positive). |
| **ClimateBERT** | An AI language model trained on climate text; can tell a promise apart from a completed action. |
| **API** | A way for a program to request data from a website directly, instead of a person clicking through pages. |
| **Entity matching** | Working out that a company in one dataset is the same company in another, when they use different names and IDs. |
| **Fuzzy matching** | Matching names that are similar but not identical (e.g. "Exxon Mobil Corp" and "ExxonMobil"). Always needs checking by hand. |
| **CIK** | The unique ID the US financial regulator gives each company. We use it as the common key to link all our data together. |
| **Scope 1 / 2 / 3** | Emission categories: 1 = direct from your own operations, 2 = from the energy you buy, 3 = everything else in your supply chain. |
| **Salience hypothesis** (visibility problem) | Our idea that media-based greenwashing scores mostly track how *visible* a company is, not how much it lies. |
