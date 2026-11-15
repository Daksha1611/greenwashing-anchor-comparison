# Note 07 — Bingler, Kraus, Leippold & Webersinke (2024), cheap talk, initiatives, emissions and reputation

**Citation.** Bingler, J. A., Kraus, M., Leippold, M., & Webersinke, N. (2024). How cheap talk in
climate disclosures relates to climate initiatives, corporate emissions, and reputation risk.
*Journal of Banking & Finance, 164*, 107191. https://doi.org/10.1016/j.jbankfin.2024.107191
(Elsevier; hybrid open access, CC BY)

**File.** Not in `papers/`. Open access (accepted manuscript at the Zurich Open Repository), but
the automated download was blocked; see [`papers/TO_OBTAIN.md`](../papers/TO_OBTAIN.md).

**Citation check.** Verified against Crossref: four authors in the order given, article 107191,
July 2024. **This note is based on the abstract and publisher metadata only; we have not read the
full text.** Anything marked † comes from our research brief and has not been checked against
the paper.

---

## Research question

Does vague climate talk in annual reports relate to what firms actually do about climate: do
their climate initiatives, their emissions and their reputation line up with how precise their
commitments are?

## Method

The authors introduce **ClimateBert CTI**, a deep-learning model that flags climate-related
**cheap talk** (imprecise, non-committal climate statements) in the annual reports of firms in
the **MSCI World** index. They then relate the amount of cheap talk to three things: membership
of climate initiatives, emissions, and negative news coverage.

† The cheap talk index (CTI) is the share of imprecise versus precise climate commitments; the
sample is 14,584 annual reports, 2010–2020. (From our brief; the abstract does not give these.)

## Headline results

All from the abstract:

- **Only targeted climate engagement** is associated with less cheap talk.
- **Voluntary climate disclosures are associated with more cheap talk.**
- Cheap talk **correlates with increased negative news coverage** and **higher emissions growth**.
- The authors' reading: cheap talk helps assess how effective climate initiatives are and helps
  anticipate reputation and transition-risk exposure.

† Targeted engagement in the brief means initiatives such as Climate Action 100+.

## Reality anchor

**One talk measure related to two outside facts, separately:** emissions growth and negative
news coverage. This is the closest thing in the literature we have read to a multi-anchor study.

## How it relates to our project

This is the single most important new paper for us, for two reasons.

1. **It gives us a ready, published way to measure the "talk" half.** Our design wants a
   commitment-versus-action split in the report text. This model is a published, peer-reviewed
   version of that idea, so we would adopt its definition rather than invent our own
   (see Improvement 7 in `synthesis/combining-and-improvements.md`). It is also the direct
   successor of the model in note 08.
2. **It narrows our gap, and we should say so plainly.** The paper relates one talk measure to
   emissions *and* to negative news, so it touches two of our anchors. But it treats them as two
   separate *correlates* of cheap talk. It does not build two competing greenwashing measures
   (talk-versus-emissions and talk-versus-media) and ask whether they rank the same firms as
   worst. That comparison is still missing, so our gap stands, in a narrower form. See
   `synthesis/extended-literature.md`.

It also says something useful about frameworks: voluntary disclosure goes with *more* cheap talk,
so framework membership is not a sign of honest conduct.

## Limitations

- Based on the abstract only; sample details and effect sizes are not known to us (apart from †).
- Reporting both news and emissions as *correlates* of text does not say which one is the better
  stand-in for "reality"; negative news coverage may track a firm's visibility as much as its
  conduct, which is the question our project asks.
- Our own caution: emissions growth and news coverage are both outcomes, not a ground truth about
  misleading intent.
