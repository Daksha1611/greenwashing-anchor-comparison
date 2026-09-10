# Note 03 — Peng et al. (2024), environmental scores vs actual carbon emissions

**Citation.** Peng, X., Li, J., Tang, Q., Lan, Y.-C., & Cui, X. (2024). Do environmental scores
become multinational corporations' strategic "greenwashing" tool for window-dressing carbon
reduction? A cross-cultural analysis. *Business Strategy and the Environment, 33*(3), 2084–2115.
https://doi.org/10.1002/bse.3586 (Wiley; open access under CC BY)

**File.** `Papers/Bus Strat Env - 2023 - Peng - Do environmental scores become multinational corporations  strategic  greenwashing  tool for.pdf`
**Citation check.** Matches the citation supplied exactly. (DOI added; the filename's "2023"
is the acceptance year — received 24 Mar 2023, accepted 15 Sep 2023, issue 2024.)

---

## Research question

If a company has a high environmental score, does it actually emit less carbon? And does the
national culture of the company's home country change the answer?

The logic is simple and powerful: an environmental score is a *claim* about environmental quality.
Carbon emissions are a *measured fact*. If high scorers emit more, the score is functioning as a
cover story rather than a description — "talk more, act less".

## Method

**No NLP at all.** This is important context for the comparison table: unlike the other four
papers, Peng et al. run a conventional panel regression on numeric data. There is no text analysis.

**Sample.** Multinational corporations on the 2021 Fortune Global 500 list, observed
**2001–2020**. Financial firms (SIC 6000–6999) and observations with missing variables are
excluded. Final dataset: **1,403 observations, 199 firms, 27 countries.**

**Variables.**
- *Dependent:* carbon emissions **CE** (absolute, Scope 1 + Scope 2) and carbon intensity **CI**
  (total emissions ÷ net sales). Both from Refinitiv Eikon Asset4.
- *Independent:* **EN**, the firm's total environmental score from Refinitiv Eikon Asset4.
- *Moderators:* the six Hofstede national culture dimensions — power distance, individualism,
  masculinity, uncertainty avoidance, long-term orientation, indulgence — measured for the
  **parent** country.
- Year and country fixed effects; board and firm controls. VIFs 1.09–2.38 (no multicollinearity).

> Because CE and CI correlate at .85, and individualism and indulgence at .81, only one dependent
> variable and one culture dimension enter any single regression.

## Headline results (real numbers)

**Main effect — higher environmental scores go with *more* carbon, not less:**

| Model | Coefficient on EN | t |
|---|---|---|
| Carbon emissions, t+1 | 0.775*** | 5.13 |
| Carbon emissions, t+2 | 0.678*** | 4.09 |
| Carbon intensity, t+1 | 1.304*** | 7.09 |
| Carbon intensity, t+2 | 1.168*** | 5.81 |

All significant at 1%; adjusted R² above .4 in all columns. The authors read this as direct
evidence that "the environmental score is a strategic tool for misleading stakeholders".

**Culture moderation.** Individualism, masculinity and uncertainty avoidance have **negative**
moderating effects — in those cultures the score-emissions gap narrows.

**Mandatory vs voluntary disclosure** (the result most relevant to us): the effect holds
regardless of disclosure regime, and is *larger* where disclosure is mandatory.

| Specification | EN → CE_t+1 | N |
|---|---|---|
| Mandatory disclosure countries | 1.532*** (t = 3.73) | 289 |
| Voluntary disclosure countries | 0.510*** (t = 3.46) | 1,114 |
| DiD, full sample | 0.781*** (t = 5.17) | 1,403 |

The `Post_Man × EN` interaction is **not significant** (t = 1.17), i.e. mandating disclosure did
not close the gap.

**Carbon-intensive vs not:** effect present in both (1.197** and 0.651*** for CE_t+1).

**Paris Agreement:** further analysis finds the Paris Agreement **did not prevent** greenwashing
in carbon reduction, and that it got worse in high-power-distance societies afterwards.

## Stated limitations

- Environmental scores come from a single rating provider (Refinitiv Asset4); rating agencies
  disagree substantially with one another.
- Hofstede's culture dimensions are measured at the parent-country level and are static, so they
  cannot capture within-country change over the 20-year window.
- Financial firms are excluded, limiting generalisability.

## Connection to the other papers

- **This is the cleanest "reality check" in the set.** It shows that a widely used ESG score —
  the kind that drives real investment flows — is positively associated with the very outcome it
  is supposed to measure inversely.
- **vs. Davidescu et al. (note 01):** direct tension. Davidescu et al. report that **large** firms
  have **lower** GSI (0.49) and better report/news alignment (r = 0.89), reading this as large
  firms being more honest. Peng et al.'s sample is *entirely* large firms (Fortune Global 500) and
  finds systematic greenwashing among them. If large firms are simply more visible and more
  fluent, a media-anchored index would score them as clean while an emissions anchor scores them
  as dirty. **That is the salience hypothesis, and these two papers straddle it.**
- **vs. Gorovaia & Makrominas (note 02):** mutually reinforcing, using independent anchors
  (emissions vs fines) and independent methods (regression vs NLP).
- **Supports our GSI-emissions arm:** validates GHGRP-style facility emissions as a usable
  reality anchor, and warns that Scope 1+2 absolute emissions and intensity can behave differently.
