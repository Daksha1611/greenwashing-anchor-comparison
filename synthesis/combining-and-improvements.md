# Combining the papers: how the design could produce better results

This file turns the 24 papers into twelve concrete improvements to the design in
`open-questions.md`. Each one is labelled:

- **[From paper]**: the idea comes from a specific paper, named, and the paper's own result is
  what we rely on.
- **[Our proposal]**: the idea is ours, motivated by one or more papers but not tested by them.

**Nothing here has been built or run.** This is a design document. Where an idea depends on a
detail we could only take from our research brief, it is marked †, and `papers/SOURCES.md` says
which notes rest on abstracts only.

## The index set after the improvements

| Index | Talk measured against | Source of the outside measure |
|---|---|---|
| GSI-media | Average tone of news coverage | GDELT |
| GSI-violation | Regulatory violations and penalties | EPA ECHO (cross-check: Violation Tracker, terms unchecked) |
| GSI-emissions | Measured facility emissions | EPA GHGRP |
| **GSI-ratings** (new) | A commercial disclosure score minus a commercial performance score | A vendor such as Refinitiv, following Yu et al. |
| **GSI-controversy** (new) | A controversy or negative-event measure | Following Ghitti et al. † |

---

## 1. Compare five measures, not three

**[From papers 14, 19; supported by 12, 15, 20.]** Add **GSI-ratings** (disclosure minus
performance, after Yu et al.) and a **controversy-based index** (after Ghitti et al. †) alongside
GSI-media, GSI-violation and GSI-emissions.

*Why.* The ratings and controversy measures are what applied finance actually uses: Luu et al.
and Liu et al. use the ratings gap, and Bacher et al. use a controversy-based measure †. Whether
they agree with the hard anchors is probably the most practically relevant result the study could
give. Caveat: the construction of the Ghitti et al. measure is **unverified** (note 19).

## 2. Use multi-trait multi-method (MTMM) logic

**[Our proposal.]** Treat "greenwashing" as **one trait** measured by **several methods**, the
anchors. Report the **full correlation matrix of the five indices** and ask: do measures that
share an anchor type (violations, emissions) correlate more with each other than with
media-based ones? That turns H4 into a standard validity test.

*Reference point.* **[From paper 24 †]** Gibson Brandon et al. report an average correlation of
about 0.45 between ESG raters. We would use that as a yardstick for "moderate" agreement, after
confirming the figure from the paper.

## 3. Test event responses

**[From papers 21, 22, 2.]** Use dated, external events such as **EPA formal enforcement actions**
and **major penalties**. A measure that captures misconduct should move around such events:

- the talk score should rise after the event (Paper 2's difference-in-differences; Cho 2009's
  case study of Total),
- the violation index should rise by construction,
- the media index should rise if media is tracking conduct.

A media index that moves with coverage spikes but not with enforcement events is tracking
attention, not conduct. The method follows Utz (2019) †, who studies how ratings move around
scandals.

## 4. Measure omission, not just tone: automated counter-accounting

**[Our proposal, from Boiral (18) and Paper 4.]** Boiral compared 116 significant negative news
events against 23 reports by hand and found that 90 per cent were left out. We would automate
the idea: for each firm-year, take GDELT negative-tone, environment-themed events and check
whether the sustainability report mentions the issue. The resulting **omission rate** is a
media-anchored version of Wang et al.'s "selective disclosure" component, measured against events
that actually happened rather than a list of required topics.

*Why it is better than average tone.* It uses media for *what happened* and the report for *what
was said*, instead of comparing two sentiments. Caveat: whether an event is in the news at all
still depends on visibility.

## 5. Separate attention from tone

**[Our proposal, motivated by papers 23, 24 and 17.]** Split media into (a) **coverage volume**,
(b) **average tone** and (c) the **count of negative events**. Then build a **visibility-adjusted
media index**: the residual from regressing media tone on log size, log coverage volume and
sector.

*Why.* If the adjusted index agrees with the hard anchors much better than the raw one, that is
direct evidence for the salience hypothesis (H3), and it gives practitioners a usable correction.
Paper 17 reports that ESG scores correlate with news-coverage metrics, which makes this concrete.

## 6. Define greenwashing as talk conditional on performance

**[Our proposal, from papers 10 and 11 against Paper 2.]** Good performers can legitimately say
more, so raw talk is ambiguous. For each anchor, regress the talk score on that anchor's
performance measure (with sector-year effects) and use the **residual** as the greenwashing
score: talk that the firm's actual performance does not explain.

*Why.* It makes each index a principled "talk minus what performance justifies", rather than an
arbitrary difference of two differently scaled numbers. It also speaks directly to the
contradiction in `extended-literature.md` §3.2.

## 7. Use the published cheap-talk definition for the talk side

**[From papers 7 and 8.]** Adopt the **cheap talk index (CTI)** definition † (share of imprecise
versus precise climate commitments) rather than inventing a new promise-versus-action score. It
is validated, published and directly comparable to prior results. This is a design choice for a
possible future implementation; nothing is built in this project.

## 8. Standardise peer-relatively

**[From paper 14 †.]** Standardise every index **within industry-year** before comparing them, so
sector differences in emissions or newsworthiness do not drive agreement or disagreement. We only
have this description of Yu et al.'s construction from the brief; the Luu et al. description we
read standardises over the sample and does not say within industry-year.

## 9. Use predictive validity as the tie-breaker

**[From papers 15, 19, 20; formalised as H6.]** If the indices disagree, the question becomes
which to trust. Test which index best predicts **future conduct** (next-year EPA penalties, and
GHGRP emissions growth as in Bingler et al.) and **future market outcomes** (crash risk, firm
value).

*Priority.* **Conduct outcomes come first.** Market outcomes can themselves reflect visibility,
so a measure that predicts crash risk may be tracking attention.

## 10. Use the GHGRP as a natural experiment

**[From paper 12; formalised as H7.]** The GHGRP's 2010 start, with its 25,000 tonne CO2e
threshold, gives a before/after and a treated/untreated split. Check which indices register the
policy effect in the direction Luu et al. report (greenwashing falls). This reuses the data
source we already plan to use.

## 11. Combine only after testing agreement

**[Our proposal, building on Dorfleitner & Utz (16).]** Their framework combines pillars into a
single indicator. We add the step before: **if the pillars do not agree, averaging them hides the
disagreement.** So:

1. report agreement first;
2. build a **"consensus greenwasher" flag**: a firm in the top decile on at least two hard
   anchors, as a conservative combined measure;
3. only then consider a **weighted composite**, with weights justified by predictive validity
   (point 9) rather than equal weighting, which is the choice Paper 1 makes without
   justification.

Dorfleitner & Utz themselves suggest calibrating weights on firm-years where case examination
shows whether greenwashing occurred; that is close in spirit to point 9.

## 12. Check whether Paper 1's formula problem is shared

**[Our proposal, from paper 6.]** Compare Lagasio's ESGSI construction with Davidescu et al.'s
GSI. If the "severity index" family generally scores report text without an external term, our
Paper 1 finding becomes a finding about a strand of the literature. We have already established
one thing: **Paper 1 does not cite Lagasio**. Whether the ESGSI formula has an external term is
an **open check** that needs the full text of paper 6, which we do not have.

---

## What this does not change

- The primary research question and H1–H4 stay as in `open-questions.md`.
- The sampling rule stays: **build the firm list from GHGRP and SEC records first, and only then
  look for reports**, never the reverse.
- The entity-matching risk stays the dominant threat: noisy matches bias correlations toward
  zero, which would look like support for our hypothesis for the wrong reason.
- This remains a literature review and design project. No analysis code, scraper or model is
  part of it.
