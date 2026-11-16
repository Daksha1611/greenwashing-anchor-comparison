# Note 06 — Lagasio (2024), the ESG-washing Severity Index (ESGSI)

**Citation.** Lagasio, V. (2024). ESG-washing detection in corporate sustainability reports.
*International Review of Financial Analysis, 96*, 103742. https://doi.org/10.1016/j.irfa.2024.103742
(Elsevier; open access, CC BY)

**File.** Not in `papers/`. Open access but the automated download was blocked; see
[`papers/TO_OBTAIN.md`](../papers/TO_OBTAIN.md).

**Citation check.** Verified against Crossref: single author, article 103742, November 2024.
**This note is based on the abstract and publisher metadata only; we have not read the full
text.** Anything marked † below comes from our research brief rather than from the abstract and
has not been checked against the paper.

---

## Research question

Can we put a number on the gap between how a company *portrays* its sustainability practices and
what it *actually does*, using only the text of its sustainability report?

## Method

Natural language processing over the sustainability reports of **749 listed companies**. The
abstract says the index is built by "integrating sentiment analysis with the frequency of
sustainability terms": in other words, a sentiment score is compared with a sustainability-content
score, both taken from the report. The result is the **ESG-washing Severity Index (ESGSI)**.

## Headline results

- The abstract reports **significant variation in ESG-washing across industries and geographical
  regions**. It gives no numbers, and we do not add any.
- The authors draw a policy conclusion: stricter and more standardised sustainability reporting
  rules are needed.

## Reality anchor

**None in substance, as far as the abstract shows.** Both ingredients (sentiment and term
frequency) come from the same report text. The index is *described* as capturing the gap
between portrayed and actual practice, but the abstract names no external measure of actual
practice. This should be confirmed in the paper's method section before it is relied on.

## How it relates to our project

This is the closest relative of **Paper 1** (Davidescu et al.'s "Greenwashing Severity
Index"). The names are almost the same, and both describe a text-derived "gap" index. That makes
it the natural test of whether our Paper 1 finding is about one paper or about a family of indices.

What we found for Paper 1 is that its published formula contains **no external term**
(`synthesis/gsi-formula.md`). If the ESGSI has the same structure, then the "severity index"
approach in general scores report text against itself, and the finding applies to a strand of
the literature rather than to one study.

We can answer one part of this now. **Paper 1 does not cite Lagasio.** We searched the text of
Paper 1's PDF (including its reference list) for "Lagasio", "ESGSI" and "ESG-washing" and found
no mention. So the two indices appear to have been developed independently.

**Open questions to check once the paper is in hand (these are questions, not findings):**

1. Does the ESGSI formula contain any term that comes from outside the report (news, emissions,
   violations, ratings)?
2. Is its "sustainability content score" a term-frequency measure of the same kind as Paper 1's
   TF–IDF ESG scores? If so, both indices reward heavy ESG vocabulary.
3. Does it say anywhere how the index was validated, and against what?

## Limitations

- Based on the abstract only. The index construction, the validation and the actual results are
  not known to us.
- If the index is text-internal, it shares the weakness we flag for Papers 1 and 4: it cannot tell
  an honest, verbose firm from a dishonest one.
- A sample of 749 listed companies across regions suggests global coverage, but we do not know how
  firms were selected or which reporting language was used.
