# Note 08 — Bingler, Kraus, Leippold & Webersinke (2022), ClimateBert on TCFD disclosures

**Citation (DOI corrected).** Bingler, J. A., Kraus, M., Leippold, M., & Webersinke, N. (2022).
Cheap talk and cherry-picking: What ClimateBert has to say on corporate climate risk disclosures.
*Finance Research Letters, 47*, 102776. https://doi.org/10.1016/j.frl.2022.102776
(Elsevier; open access, CC BY)

**File.** `papers/bingler-2022-climatebert-frl.pdf` (Oxford ORA copy; the PDF states it is an open
access article under CC BY).

**Citation check.** The DOI in our research brief (`…frl.2021.102776`) returns 404. A Crossref
title search finds this paper under **`10.1016/j.frl.2022.102776`**: same title, same four
authors in the same order, *Finance Research Letters* 47, article 102776, June 2022. The PDF we
hold shows the same volume and article number. **Full text read.**

---

## Research question

Voluntary climate-risk disclosure, such as support for the Task Force on Climate-related
Financial Disclosures (TCFD), is widely praised. Is that praise justified? Do firms that
publicly support the TCFD actually disclose more useful climate information?

## Method

- **Model.** The authors train **ClimateBERT**, a language model fine-tuned from BERT on climate
  text, to recognise disclosure content in each of the four TCFD recommendation categories
  (governance, strategy, risk management, metrics and targets).
- **Training data.** More than 17,300 sentences labelled by hand for the TCFD categories, plus
  more than 300,000 general-language sentences from annual reports to teach the model what
  *non*-climate wording looks like.
- **Sample.** Annual reports of **818 firms** that support the TCFD, for fiscal years 2014–2019,
  so the authors can see whether disclosure changed after a firm signed up.

## Headline results

- The abstract's conclusion: the firms' TCFD support is **mostly cheap talk**, and firms
  **cherry-pick**, reporting mainly **non-material** climate-risk information.
- The paper finds no considerable increase in reporting after 2016, when EU non-financial
  reporting rules began to apply.
- Firms headquartered in North America and Europe disclose relatively more than firms in Asia,
  which report roughly half as much as their North American counterparts.

We give no further numbers because we have not tabulated the paper's results.

## Reality anchor

**None.** The analysis is text-internal: it classifies what the reports say. It does not compare
the text with emissions, fines or news. (Note 07 is the later paper that does relate cheap talk to
outside outcomes.)

## How it relates to our project

- **Voluntary framework membership is not an anchor.** Supporting the TCFD is a public signal of
  seriousness; this paper finds the disclosure that follows is mostly cheap talk. That supports our
  argument against treating disclosure volume or framework membership as a stand-in for conduct.
- **It introduces the method** that note 07 later links to emissions and news, and that we would use
  for the talk side of our design.
- **It is a counterexample to word counting.** A classifier that reads sentences in context can
  separate relevant from irrelevant disclosure in a way that a dictionary cannot, which is the
  same lesson as Paper 4 (Wang et al.).

## Limitations

(Our reading; the paper's own discussion is short.)

- Text-internal: it says what firms *wrote*, not whether what they wrote was true or whether they
  acted on it.
- The sample is firms that *chose* to support the TCFD, so it cannot say how TCFD supporters
  compare with firms that did not.
- "Non-material" is a judgement made by the classification scheme; it is not an external fact
  about the firm.
