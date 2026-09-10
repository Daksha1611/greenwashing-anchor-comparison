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

Companies say a great deal about how green they are, and some of them are lying.
The question behind this project is whether we can catch them automatically.

The word for that lying is greenwashing: making a company look more
environmentally responsible than it really is. Researchers define it as the gap
between two things:

- what a company says, in its sustainability report, its press releases and its
  public commitments; and
- what a company does, in its actual emissions, its pollution fines and its
  day-to-day operations.

If the talk is much better than the actions, that is greenwashing.

The difficulty is measurement. To catch greenwashing automatically you need both
halves of that gap as numbers. The talk half is reasonably straightforward, since
you can feed the sustainability report to a computer and score the language. The
second half is the hard part. What counts as the truth about a company's actual
environmental behaviour?

Different researchers have given different answers, and throughout this report we
call that choice the reality anchor:

| Reality anchor | What it means |
|---|---|
| Violations | Has the government fined this company for breaking environmental law? |
| Emissions | How much carbon does this company actually put into the air? |
| Media | What does the press say about this company's environmental record? |
| None | Analyse the report's language without checking it against anything |

This is the central problem the project addresses. All four of these choices
appear in published, peer-reviewed research. Every study picks one and stops there,
and nobody has checked whether they give the same answer. If you rank companies
from worst to best greenwasher using violation records, then rank them again using
media coverage, do you get the same list or two completely different ones?

That matters, because if the two lists disagree then at least one of these
published methods is not measuring greenwashing at all. It is measuring something
else.

What we did was read all five papers, summarise them in plain language, work out
what they agree on, identify the gap between them, and design a study that would
test it. Nothing has been measured yet; this is the review stage.

---

## 2. The five papers, one by one

### Paper 1 — Detecting Greenwashing in ESG Disclosure (the "GSI" paper)

*Davidescu, Manta, Bîrlan, Miler & Niță (2026). Sustainability, 18(3), 1486.*

**What they did.** Took 204 big companies in Central and Eastern Europe, collected
their sustainability reports and news coverage about them, and built a score
called the Greenwashing Severity Index (GSI). They describe it as measuring
the gap between what a company says about itself and what the press says about it.

**What we understood.**

- The method is dictionary-based. They built four word lists by hand: a
  greenwashing list (1,140 "good" words like *sustainability* and *ethical*, and
  990 "bad" words like *pollution* and *eco-fraud*), plus separate 122-word lists
  for Environmental, Social and Governance terms.
- They count how often those words show up, weight them using TF-IDF (a standard
  technique that boosts words distinctive to one document and plays down words
  that appear everywhere), and combine them into one number per company.
- The average GSI was 0.5765, which they read as moderate greenwashing
  everywhere. Germany scored worst (0.6086), Lithuania best (0.5157). Finance,
  online commerce and aviation were the worst industries; construction the best.
- Big companies scored better (0.49) than small ones, which they put down to
  large firms being watched more closely.

**The problem we found.** We worked through their formula carefully. It comes
down to this:

```
GSI = ⅓ × (Environmental score) + ⅓ × (Social score) + ⅓ × (Governance score)
```

All three of those inputs are calculated from the company's own report. The news
articles they collected never enter the formula at all. They are used in a
separate piece of analysis and then dropped.

So although the paper says the GSI measures the gap between what a company claims
and how the press describes it, **the published formula measures no gap at all.**
What it actually measures is how densely a report is packed with ESG vocabulary. A
company that uses the word "sustainability" more often scores as more of a
greenwasher, no matter what it does in practice and no matter what the press says.

**What could be improved.** Beyond the formula, several other things did not hold
up when we checked them:

- The paper's main claim is that companies emphasising one ESG pillar over the
  others show "significantly higher" greenwashing. This is not statistically
  significant. The two tests give p = 0.077 and p = 0.064, both above the usual
  0.05 cutoff, and both confidence intervals include zero.
- The text says "all GSI values exceed 0.5", but their own table reports a
  minimum of 0.00063.
- The word-scoring scale is described in two contradictory ways: −1 and +1 in one
  section, −3 to +3 in another.
- They describe using topic modelling, but no topic-modelling result appears
  anywhere in the index or the tables.

This mattered to us because the project originally planned to build on this index,
so we worked through the formula step by step and checked it against the figures
the paper itself reports.

---

### Paper 2 — Identifying Greenwashing Using Natural-Language Processing

*Gorovaia & Makrominas (2025). European Financial Management, 31(1), 427–462.*

**What they did.** This is the cleanest idea in the set. They split US companies
into two groups using a hard external fact, namely whether the company has been
fined for an environmental violation, then read both groups' sustainability
reports to see whether polluters write differently.

**What we understood.**

- They were careful about sample bias. Instead of grabbing whatever reports were
  easy to find (which would over-select big, green, well-organised companies),
  they started from the full population of firms, statistically matched each
  violator to a similar non-violator, and only *then* went looking for reports.
  That gave 993 matched pairs, 1,120 reports and 441 companies, over 2008 to 2022.
- Polluters write longer reports: 20,304 words against 15,091.
- They write more positively: 0.823 against 0.816.
- They write more about the environment: 0.185 against 0.175.
- They write less readably, meaning denser text that is harder to follow.
- All of those differences are statistically significant at the 1% level
  (readability is the exception, not significant).
- The strongest finding is that companies change how they write straight after
  getting caught. Their difference-in-differences test compares the same firm
  before and after a violation, and shows environmental content rising sharply
  (effect 0.175, p < 0.001) once a firm becomes a violator.

So a company that has just polluted responds by writing more, sounding more
positive, and saying more about the environment. This is the closest thing in the
five papers to catching greenwashing as it happens.

**What could be improved.**

- The authors are open about one real limitation. A fine proves guilt, but the
  absence of a fine does not prove innocence. A company that looks clean may
  simply not have been caught.
- Their violation data comes from commercial databases (MSCI, Refinitiv), not
  from the environmental regulator directly. Our project would use the regulator's
  own records instead, which is a slight improvement.

---

### Paper 3 — Do Environmental Scores Become a "Greenwashing" Tool?

*Peng, Li, Tang, Lan & Cui (2024). Business Strategy and the Environment, 33(3), 2084–2115.*

**What they did.** There is no text analysis in this one; it works purely with
numbers. They take the environmental score that rating agencies give to large
companies, the kind of score that influences investment decisions, and check it
against how much carbon those companies actually emit. The sample is 199 Fortune
Global 500 companies across 27 countries, from 2001 to 2020.

**What we understood.**

- The obvious expectation is that a high environmental score should mean low
  emissions.
- They found the opposite. Higher environmental scores go with higher
  emissions. The effect is strong and statistically solid (coefficient 0.775 for
  absolute emissions, 1.304 for emissions per unit of sales, both significant at
  the 1% level).
- In other words, the score a company gets for being green rises with how much it
  pollutes. The score is working as a cover story.
- Forcing companies to disclose did not fix it. The effect holds in countries with
  mandatory disclosure rules, and is if anything larger there.
- The Paris Agreement did not fix it either, and in countries with strongly
  hierarchical cultures it grew worse afterwards.

**Why this paper matters for us.** It shows that the reality-check approach works,
using a completely different method from Paper 2 and reaching the same conclusion.
Two independent anchors, two independent methods, one answer: companies that talk
greener often perform worse.

**What could be improved.**

- The environmental scores come from a single rating provider, and rating
  providers famously disagree with each other.
- The culture measures are static, so they cannot capture change over the 20 years
  studied.
- Financial firms are excluded entirely.

---

### Paper 4 — Corporate Greenwashing Index: A Deep Learning Approach

*Wang, Gao & Sun (2025). EPJ Data Science, 14, 44.*

**What they did.** This is the most technically advanced text method in the set.
They used MacBERT, a modern AI language model, to read Chinese company reports
sentence by sentence and score greenwashing, covering 9,534 company-years from
2008 to 2023.

**What we understood.**

- They split greenwashing into two separate behaviours, which is a genuinely
  useful idea:
  - Selective disclosure, meaning staying quiet about the things you did badly.
    They measure it as the share of required topics the company never mentions.
  - Expressive manipulation, meaning dressing up whatever you do say. They measure
    it as the share of statements that are vague and aspirational rather than
    concrete and checkable.
- A statement counts as substantive if it can be checked and would be hard to
  fake, such as actual figures or specific examples. It counts as symbolic if it
  is only aspiration, vague description, or last year's wording repeated.
- The two are combined using a geometric mean, which means multiplying them and
  taking the square root, rather than a simple average. This is deliberate. A
  company only scores badly overall if it does both things, whereas with a simple
  average one bad component could carry the whole score.
- The model agrees with human labellers 97.79% of the time on the first component
  and 95.13% on the second.

**Why they used an AI model instead of word lists.** This is the most useful
methodological lesson in the set, and it is effectively a criticism of Paper 1's
approach. A keyword list cannot tell a real commitment from a vague aspiration,
because both use the same words. "We are committed to reducing emissions" and "We
reduced emissions by 12% in 2023" share most of their vocabulary but mean very
different things. Only a model that reads context can tell them apart.

**What could be improved.**

- The index never checks against reality. Both components come purely from the
  report's own text. The 97.79% figure means the model agrees with human readers,
  not that it agrees with whether the company actually pollutes.
- The authors never claim otherwise. This is the same weakness as Paper 1, but
  this paper is open about it.
- The sample is Chinese A-share companies under a particular disclosure regime,
  and whether the method transfers to US companies is untested.

---

### Paper 5 — Mapping the Greenwashing Research Landscape

*Forliano, Battisti, de Bernardi & Kliestik (2025). Review of Managerial Science, 19, 3407–3456.*

**What it is.** This is not an experiment but a systematic review mapping the
whole research field. The authors collected 97 peer-reviewed articles from the two
main academic databases and analysed the structure of the literature.

**What we understood.**

- The field splits into four themes: (1) symbolic management and CSR
  communication, (2) environmental regulation and institutional complexity,
  (3) performance and sustainable practices, (4) marketing, perception and trust.
- Research is dominated by macro-level theories: legitimacy theory, where firms
  talk green to stay socially acceptable; institutional theory, where rules and
  norms shape behaviour; and stakeholder theory, where firms respond to whoever
  has power over them.
- They propose organising the field across three levels: macro (society), meso
  (the organisation), micro (individual people).

**How useful it is for us.** Moderately, and two limits are worth stating clearly.

It maps theories rather than measurement methods. It does not compare
violation-based, media-based and emissions-based approaches against each other, so
it gives us context and vocabulary but does not itself prove that our particular
gap exists.

Its coverage also closed in February 2025, before Papers 1 and 4 appeared, so the
two most relevant papers in our set are not in the map.

What it does usefully confirm is that the field defines and measures greenwashing
in inconsistent ways, which fits our concern that different measures may not be
measuring the same thing.

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

The position across the five papers is this:

| Paper | What it checks green talk against |
|---|---|
| Paper 2 (Gorovaia & Makrominas) | Environmental fines |
| Paper 3 (Peng et al.) | Measured carbon emissions |
| Paper 4 (Wang et al.) | Nothing, by explicit design |
| Paper 1 (Davidescu et al.) | Nothing; media is claimed but is not in the formula |

Every paper commits to one anchor and stops there. We could not find a single
statistic anywhere in this literature comparing one greenwashing measure against
another: no correlation, no test of overlap, nothing.

### Why this matters: two of the papers contradict each other

Compare what Papers 1 and 3 say about large companies.

Paper 1 finds that big companies are the cleanest, scoring 0.49 against a sample
average of 0.5765. Its explanation is that large firms are watched closely and so
behave better.

Paper 3 studies only very large companies, the Fortune Global 500, and finds
greenwashing throughout.

Both are peer-reviewed, and both cannot be straightforwardly right. There is one
explanation that would make both true at the same time. The text and media-based
measure may not be detecting greenwashing in big companies at all. It may simply
be detecting that big companies have professional communications departments: they
write polished reports, they attract a lot of press coverage, and they know how to
sound credible.

We call this the visibility problem, or the salience hypothesis. Media-based
greenwashing measures may largely be measuring how visible a company is rather
than how much it lies.

Nobody has tested this. It is also worth noting that the authors of Paper 1 ask
for this test themselves: their own suggested next step is to check NLP-based
greenwashing indicators against real environmental outcomes such as emissions data
and enforcement actions.

### Why it matters beyond academia

ESG ratings move real money. They influence which funds buy which stocks and what
companies pay to borrow. Paper 3 has already shown that one widely used commercial
environmental score rises with the pollution it is supposed to measure inversely.

Academic greenwashing indices are now being proposed as the fix for those flawed
ratings. If the fix carries the same flaw, rewarding visibility and polished
writing rather than actual conduct, then it reproduces the problem it was built to
solve. Media-based measures are also the ones most likely to be adopted widely,
because news data is cheap, global and constantly updated in a way that regulatory
records are not.

---

## 5. The project idea

The research question is this:

> Do greenwashing measures built on media sentiment identify the same companies as
> measures built on regulatory violation records, or is media-based greenwashing
> detection largely measuring how visible a company is?

### The design in one picture

We take the same 150 to 300 US companies, score their sustainability reports once
to capture the talk, then check that talk against three different realities and
see whether the three resulting rankings agree.

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

### What we would test

First, whether the rankings match overall. We would use Spearman rank correlation,
which measures whether two lists put things in the same order, running from −1 for
exactly reversed, through 0 for unrelated, to +1 for identical.

Second, whether the measures agree on the worst offenders. This matters more than
the overall correlation. We would take the worst 10% under each measure and see how
far those groups overlap, using the Jaccard index for plain overlap and Cohen's
kappa for overlap corrected for chance. Two lists can look reasonably correlated
overall while disagreeing completely about which companies are worst, and the worst
companies are the only ones anyone acts on.

Third, whether the media measure is simply tracking visibility. We would run a
regression predicting the media-based score from company size and from how many
news articles mention the company. If those two things explain most of it, the
visibility problem is confirmed.

### One design decision worth explaining

We build the company list from emissions and filing records first, and only then
go looking for sustainability reports, never the other way round.

This follows Paper 2's approach to sampling. If you start by collecting whatever
reports are easy to find, you end up over-selecting large, visible, well-resourced
companies, which are exactly the companies our hypothesis is about. The result
would be spoiled before we began.

### What we can and cannot claim

Because Paper 1's index turned out not to contain a media component, we cannot
describe this project as replicating a media-based index and comparing it against
others. Instead we build our own media-based measure, set it out in full, and say
clearly that it is ours. What we found about Paper 1's formula becomes a result in
its own right rather than a foundation we build on.

---

## 6. Datasets we would need to implement this

Everything here is free to access.

| Source | What it gives us | Access |
|---|---|---|
| GDELT | Global news with a tone score for each article; our media anchor | Free, no login |
| EPA ECHO | US environmental violations, inspections and fines; our violation anchor | Free, no login |
| EPA GHGRP | Emissions reported by individual facilities; our emissions anchor | Free download |
| SEC EDGAR | Company filings and the official company ID that ties everything together | Free, but a contact email must be included |
| Responsibility Reports | An archive of sustainability report PDFs | Free, needs scraping |
| CDP | Standardised climate disclosures | Partly licensed, so optional |

We would use GDELT rather than NewsAPI because NewsAPI's free tier only reaches
about one month back, and we need several years.

---

## 7. Where the project stands, and how we plan to improve it

### 7.1 Where we are now

This project is still at the reading and planning stage. We have gone through the
five papers in detail, worked out how they relate to one another, and settled on a
research question. We have not collected any data or measured anything yet.

The reading was more useful than we expected, for three reasons.

First, it gave us a way to organise the field. When we started, the five papers
looked like five loosely related studies about greenwashing. The thing that
actually separates them is what each one checks green talk against, which is the
idea we have called the reality anchor throughout this report. Once we saw that,
the papers arranged themselves into a single question rather than a list.

Second, we found a real problem in one of them. Paper 1 is presented as a
media-based index, and we planned to build on it. Working through the formula, it
turned out not to use the news data at all. We checked our reading by
recalculating the authors' own published figures, and the arithmetic matches
exactly, so this is not a misunderstanding on our part. That changed the project:
instead of extending their index, we now have to build our own and say clearly
that we are doing so.

Third, the design we ended up with comes out of the gap rather than being decided
in advance. The sampling method, in particular, is copied from Paper 2 because
their approach directly avoids a problem that would otherwise ruin our result.

What we do not have yet is the practical part. There is no list of companies to
study, no data downloaded from any source, and nothing has been computed. The
next stage of the work is building those things.

### 7.2 How we hope to improve on the existing work

We see five ways this project could go beyond what the five papers already do,
and each one answers a specific weakness we found while reading them.

**Compare the anchors instead of choosing one.** Every paper we read commits to a
single reality anchor and stops there. We want to calculate three on the same
companies and check whether they agree. This is the main contribution, and as far
as we can tell nothing in the literature does it.

**Use a language model rather than word lists.** Paper 1 counts words from a
dictionary. Paper 4 shows why this does not work well: "we are committed to
reducing emissions" and "we cut emissions by 12% in 2023" use almost the same
words but mean very different things. We plan to use ClimateBERT, which is built
to tell a promise apart from a completed action.

**Go to the regulator's own records.** Paper 2 identifies polluters using fields
in commercial databases. We would use the EPA's public records directly, which is
the original source those databases draw on, and which gives the full history
rather than a summary flag.

**Write the method down properly.** Paper 1's index cannot be rebuilt from the
paper, because two important steps are never stated. Whatever we build, we want to
describe every step in enough detail that someone else could reproduce it. Having
criticised another paper for this, it would be a poor outcome to repeat it.

**Test the thing that could undermine our own result.** This one matters most.
If we match companies to facilities badly, the errors add noise, and noise pushes
correlations toward zero. But low correlation is exactly what our hypothesis
predicts. So careless data work would appear to confirm our argument for entirely
the wrong reason. We plan to measure how well the matching worked and repeat the
analysis using only the cases we are confident about. If we do find disagreement
between the anchors, that check is what makes the finding believable.

### 7.3 The technical side

Everything we plan to use is free and open. No paid data subscription, no
commercial ESG database, and no specialised hardware.

**Tools.** The work would be done in Python. For reading the report PDFs we would
use pypdf, since the older PyPDF2 is no longer maintained. Splitting reports into
sentences needs spaCy, because sustainability reports are full of bullet points,
headings and table fragments that simpler methods break on. The language model
runs through the transformers library. For the analysis itself, scipy handles the
rank correlation, scikit-learn provides Cohen's kappa, and statsmodels handles the
regression. Data goes through pandas, and requests handles the downloads.

**The model.** We would use ClimateBERT rather than FinBERT. ClimateBERT is
trained on climate text and can separate a promise about the future from something
already done, which is exactly the distinction a greenwashing measure depends on.
FinBERT is trained on financial sentiment, meaning whether analysts sound positive
or negative about a stock, which is a different problem entirely. ClimateBERT is
also small by modern standards, so it runs on a normal laptop.

**The data sources**, and the practical catch with each:

| Source | How we get it | Login needed | The catch |
|---|---|---|---|
| **GDELT** | Web API, or BigQuery for longer histories | No | Returns about 250 articles per query, so long histories need the bulk route |
| **EPA ECHO** | Web API | No | Results come in pages, and broad queries time out. Several fields cover a fixed three- or five-year window rather than a single year, which would be easy to misread as annual data |
| **EPA GHGRP** | Annual bulk download | No | Only covers facilities emitting 25,000 tonnes of CO2e or more per year. It does publish a parent-company field, which helps a lot |
| **SEC EDGAR** | Web API | No, but a contact email must be included in every request or it is refused | Limited to 10 requests per second |

**The order of work.** The company list has to be built first, from the emissions
and filing records, and only then do we go looking for sustainability reports.
This sounds like a small detail but it is not. If we started by collecting whatever
reports were easy to find, we would end up with a sample of large, visible,
well-resourced companies, which are precisely the companies our hypothesis is
about. The result would be spoiled before we began. Paper 2 handles this by
matching firms before searching for reports, and we would do the same.

Once the list exists, each company's report goes through pypdf, then spaCy to
split it into sentences, then ClimateBERT to score how much of it is promises
versus completed actions. That gives the "talk" score. The three anchors are
collected separately and combined with it to produce the three indices, which are
then compared.

**The hardest part.** The EPA tracks factories and plants. The stock market tracks
companies. GDELT tracks names as they appear in news text. None of these share an
identifier, so linking them is a genuine problem rather than a formality.

A single corporation might own two hundred sites operating under fifty different
names, and ownership changes from year to year, so any link we build has to be
year-specific. On top of that there are ordinary difficulties: company names carry
endings like INC, CORP and LLC, and some names are genuinely ambiguous, where
"Delta" could be an airline or a tap manufacturer.

Our plan is to work from the most reliable evidence downwards: start with the
parent-company field the EPA already publishes, use the shared site ID to move
across to the violations database, then match on cleaned-up names, then allow
approximate matches but check them by hand, and finally hand-code whatever is left
over. With 150 to 300 companies this is manageable, probably about a day of work,
and it is worth doing carefully.

**A few habits we want to keep.** Every download should be saved the first time we
fetch it, because GDELT and the EPA databases change over time and results would
otherwise not be repeatable. The analysis settings, such as the correlation
threshold and where we draw the "worst 10%" line, should be fixed before we
calculate anything, so that we cannot end up adjusting them until the answer looks
interesting. Any report that fails to convert from PDF should be recorded rather
than quietly skipped, because scanned documents tend to come from smaller and
older firms and losing them silently would change the sample. And the number of
news articles about each company needs to be kept as a variable in its own right,
since that is our measure of visibility and the whole salience test depends on it.

### 7.4 What we do next

The immediate task is building the company list, matching the EPA's emissions
reporters to their stock market IDs to get a clean set of 150 to 300 firms.
Everything else depends on this, and it is also the step most likely to cause
trouble, so it makes sense to do it first and see how bad the matching problem
really is.

After that we would start with GDELT, because it needs no login and no facility
matching, just company names. It is the quickest way to get one complete path
working from start to finish, which would tell us whether the overall approach
holds together before we invest effort in the harder data sources. The EPA
violation and emissions data would follow, and only then would we calculate the
three indices and compare them.

There is one result we could get early and cheaply. Since Paper 1's index reduces
to counting how many ESG words appear in a report, we can test whether that alone
has any relationship to a real-world measure. If it does not, that says something
useful about a whole family of dictionary-based methods, and it does not require
the full pipeline to find out.

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
