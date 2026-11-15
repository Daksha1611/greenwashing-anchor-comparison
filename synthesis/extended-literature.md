# The extended literature: 19 more papers, in six groups

The original five papers (notes 01–05) gave us the reality-anchor idea. Nineteen more (notes
06–24) test it. They come from four publishers: Elsevier, Springer, Emerald and Taylor & Francis.
This file sorts them by what they tell us, sets out the three contradictions they expose, and
restates the gap more precisely.

Details marked † come from our research brief and are not confirmed by the abstract or the
paper. Four notes rest on full text (08, 12, 16, 17); the other fifteen rest on abstracts and
metadata. `papers/SOURCES.md` has the full record.

## 1. The thematic map

### Group A. Measuring the "talk" side (text and NLP): papers 6, 7, 8, 9

Four papers read what firms *say*. **Lagasio (2024)** builds an ESG-washing severity index from
sentiment plus sustainability-term frequency in the reports of 749 listed firms. **Bingler et
al. (2022, 2024)** train a climate-specific language model: the 2022 paper finds that support for
the TCFD framework is mostly cheap talk, with firms cherry-picking non-material information, and
the 2024 paper turns the model into a cheap talk index and relates it to initiatives, emissions
and negative news. **Hrasky (2012)** is the manual ancestor of all of them: she classifies
Australian carbon-footprint disclosure as symbolic or substantive by hand.

*What they give us:* a published way to measure the "talk" half (Bingler et al.), a warning that
voluntary framework membership is not honest conduct, a hint that symbolic talk sits in
low-emission sectors (Hrasky), and a question about Paper 1: is its text-only "gap" index part of
a family that includes Lagasio's? Paper 1 does not cite Lagasio (we searched its text).

### Group B. Disclosure against measured performance: papers 10, 11, 12, 13

These ask whether firms that perform better environmentally disclose more or less.
**Clarkson et al. (2008)** and **Tadros & Magnan (2019)** find that better performers disclose
more. **Cho et al. (2015)** show over three decades that disclosure follows legitimacy and
exposure factors, and is not valued by investors. **Luu et al. (2025)** use the US greenhouse gas
reporting rule as a natural experiment and find that greenwashing fell after it.

*What they give us:* the counterweight to Paper 2, a second use of 10-K text as a disclosure
source (Tadros & Magnan), and a policy shock on our own planned emissions data source (Luu et al.).

### Group C. The ratings-gap anchor: papers 14, 15, 16

This is the anchor type our first set of papers lacked: a commercial **disclosure score minus a
commercial performance score**. **Yu, Luu & Chen (2020)** define the measure; **Liu et al.
(2024)** † use it to predict stock price crash risk; **Dorfleitner & Utz (2024)** propose a
broader framework that combines several information sources into one indicator. Paper 12 (Luu et
al.) also uses a ratings gap, with both halves from Refinitiv.

*What they give us:* the measure most applied papers actually use, a model for standardising
scores peer-relatively, and the only explicit proposal to combine sources. This is why the ratings
gap needs to be a fourth index in our design.

### Group D. Violations: paper 17

**Raghunandan & Rajgopal (2022)** compare self-labelled ESG funds with non-ESG funds at the same
managers. ESG funds hold firms with worse compliance records, higher fines and higher emissions per
unit of revenue, yet higher ESG scores, and ESG scores track disclosure quantity and news coverage,
not conduct.

*What it gives us:* a third, independent confirmation of the talk–action gap, a new violations
database to cross-check EPA ECHO (access terms unchecked), and a partial version of our own
question, since ratings and violations visibly disagree.

### Group E. Media, controversy and events: papers 18, 19, 20, 21, 22

**Boiral (2013)** compared 23 GRI A/A+ reports with 116 significant news events and found that 90
per cent of the significant negative events went unreported. **Ghitti et al. (2024)** and **Bacher
et al. (2025)** use a controversy-based greenwashing measure † (construction unverified, see note
19): the first relates it to board features and firm value, the second to asset pricing around the
Paris Agreement. **Utz (2019)** † runs an event study on corporate scandals and finds that
aggregated ESG assessments do not warn of them. **Cho (2009)** shows qualitatively how Total SA used
disclosure after two disasters.

*What they give us:* a different media anchor from average news tone (what happened, not how it
sounded), a way to measure omission (Boiral), an event-response test (Utz, Cho), and an
anchor type, controversy, that is already used in a leading finance journal.

### Group F. Reliability of the measures themselves: papers 23, 24

**Drempetic et al. (2020)** † find that firm size, resources and data availability raise ESG
scores. **Gibson Brandon et al. (2021)** compare ESG ratings from seven providers for S&P 500 firms
and find that stock returns rise with disagreement, mainly on the environmental dimension, with
† an average between-provider correlation of about 0.45 and more disagreement for the largest
firms.

*What they give us:* strong prior evidence for the salience hypothesis, and the methodological
model for our study: the same exercise, applied to greenwashing anchors instead of ESG raters.

## 2. Where the literature agrees

1. **A talk–action gap exists, whatever the anchor.** Violations (papers 2, 17), emissions (paper
   3, 17), and negative news (papers 7, 18) all point the same way: more or better talk does not
   go with better conduct.
2. **Quantity of disclosure is a poor proxy for honesty.** Voluntary disclosure goes with more cheap
   talk (7, 8), ESG scores track how much firms disclose (17), and firms behave strategically after
   they are caught (2, 22).
3. **Visibility and size shape what gets measured.** Ratings rise with size (23), raters disagree
   most for the largest firms (24) †, ESG scores correlate with news coverage (17), and disclosure
   follows exposure (13).
4. **The methods are moving from counting words to classifying sentences.** Papers 4, 7 and 8 use
   context-aware classifiers, and Paper 4 argues explicitly that dictionaries cannot tell a real
   commitment from an empty one. (None of them tests dictionaries against classifiers on the same
   firms, so this is a direction of travel, not a result.)

## 3. Three contradictions, and how anchor choice explains them

### 3.1 Does mandatory disclosure reduce greenwashing?

**Peng et al. (Paper 3)** find that the gap between an environmental score and measured emissions
persists, and is if anything larger, in countries with mandatory disclosure. **Luu et al.
(paper 12)** find that the US GHGRP, a mandatory emissions reporting rule, reduced greenwashing.

*Why they differ.* The two use **different anchors** and **different settings**. Peng compares a
rating score with *measured emissions*; Luu uses a *ratings gap*, disclosure score minus
performance score, with both halves from the same vendor. Peng looks across countries; Luu looks
at one rule in the US. One possible reason for the difference, which is our inference and not
something either paper says: a rule that makes emissions public could change a vendor's
performance score or the quantity of disclosure without changing emissions, and a ratings gap
would show that as a gap closing where an emissions comparison would not. **The conclusion
appears to depend on the measure, which is our argument.**

### 3.2 Do bad performers say more or less?

**Paper 2** (violators write longer, more positive, more environmental reports) and **Cho et al.
(paper 13)** (disclosure tracks exposure; Cho 2009, paper 22, shows legitimation in a single
case) support **legitimacy theory**: firms under pressure talk more. **Clarkson et al. (paper
10)** † and **Tadros & Magnan (paper 11)** find that **good performers disclose more**, which
fits **voluntary disclosure theory**.

*Why they differ.* What "disclosure" means. Paper 2 measures **volume and tone**; Clarkson et al. †
use a content index of **hard, verifiable items**. Talk that costs nothing (vague, positive,
long) rises with pressure; talk that can be checked rises with performance. **This is why our
talk score must separate concrete actions from vague commitments**, as the classifiers in papers
4, 7 and 8 do, rather than count how much a firm says.

### 3.3 Are large firms cleaner?

**Paper 1** says large firms score better (GSI 0.49 against a mean of 0.5765). **Paper 3** finds
greenwashing throughout the Fortune Global 500. **Drempetic et al. (paper 23)** † show ratings are
inflated by size. **Gibson Brandon et al. (paper 24)** † find rater disagreement highest for the
largest firms. **Luu et al. (paper 12)** find large firms respond most to the GHGRP.

*Why they differ.* Taken together these point to **size and visibility shaping the measurement,
not just the behaviour**. A text- or news-based measure may find large firms "cleaner" because
they write fluent reports and get a lot of coverage. That is the **salience hypothesis (H3)**,
and it now has much more prior support than when we started. None of these papers tests it on a
greenwashing index.

## 4. The refined gap

Our first statement of the gap said, in effect, that nobody had compared anchors. Some of the new
papers come close to what we propose, so the claim has to be narrower:

- **Bingler et al. (paper 7)** relate one talk measure to both **emissions growth** and
  **negative news**, as **separate correlates**.
- **Raghunandan & Rajgopal (paper 17)** compare **ESG scores** against **violations** and
  **emissions**, which is ratings against reality.
- **Gibson Brandon et al. (paper 24)** compare **ESG raters with each other**.

> **As far as we found, no study builds several greenwashing indices on the same firms, each
> anchored to a different reality check, and tests whether they rank the same firms as worst.**

The hedge ("as far as we found") stays: we have read twenty-four papers closely or by abstract, not
the whole literature, and fifteen of the nineteen new papers only by abstract.

Two further consequences of the narrower claim:

- **What was weakened:** the idea that the question had not been approached at all. Papers 7, 17
  and 24 each do part of it.
- **What survived:** the *ranking-agreement* test across *competing greenwashing indices* on the
  *same firms*. Paper 7 treats emissions and news as correlates of a single talk score; paper 17
  works at fund level; paper 24 compares raters, not greenwashing measures.

## 5. What this adds to the design

The extended literature adds two anchor types (ratings-gap, controversy), three hypotheses (H5–H7,
in `open-questions.md`), a sharper version of H3 (anchor disagreement), and twelve proposed
improvements (`combining-and-improvements.md`). None of it has been built: this is still a review
and design project, and nothing has been measured.
