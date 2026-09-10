# Note 04 — Wang, Gao & Sun (2025), deep-learning greenwashing index

**Citation (extracted from PDF).** Wang, X., Gao, X., & Sun, M. (2025). Construction and analysis
of corporate greenwashing index: a deep learning approach. *EPJ Data Science, 14*, 44.
https://doi.org/10.1140/epjds/s13688-025-00562-w (Springer, open access, CC BY-NC-ND 4.0)

**File.** `Papers/s13688-025-00562-w.pdf`

**Citation completion flagged.** The supplied citation had no authors. Extracted:
**Xiao Wang, Xukuo Gao (corresponding), and Meng Sun**, all of the School of Management, Xi'an
University of Architecture and Technology, Xi'an, China. Article number **44**, volume **14**.
Handling editor: Anna Sapienza. Everything else in the supplied citation is correct.

---

## Research question

Can a modern language model read corporate social responsibility reports sentence by sentence and
produce a defensible numeric greenwashing score — one that catches disclosure that is "formally
compliant but substantively vacuous"?

## Method

**Sample.** CSR reports of Chinese **A-share** listed companies, **2008–2023**. Financial and
insurance companies, and ST/ST* companies (firms flagged for financial distress), are excluded.
Final dataset: **9,534 observations.**

**Model.** **MacBERT**, a BERT-family language model pre-trained for Chinese.

> *BERT* is a neural language model that reads a sentence in both directions at once, so it
> interprets each word using the words on both sides of it. That context-sensitivity is the stated
> reason for preferring it to the dictionary/word-count methods used in most earlier work — a
> keyword list cannot tell a real commitment from a vague aspiration, because both use the same
> vocabulary.

**Two components, each a separately fine-tuned classifier.** Greenwashing is decomposed into two
distinct strategies:

1. **Selective disclosure (GWLS)** — staying quiet about the things you did badly.

   ```
   GWLS = 100 × (1 − Number of Disclosed Items / Total Required Items)
   ```

   The item checklist comes from the indicator system of Huang and Chu (reference [23] in the paper).

2. **Expressive manipulation (GWLE)** — dressing up what you do say.

   ```
   GWLE = 100 × (Number of Symbolic Disclosures / Total Disclosed Items)
   ```

   A disclosure is **substantive** if it is verifiable and hard to fake — factual statements, case
   studies, quantitative detail. It is **symbolic** if it is aspirational, purely qualitative, or a
   repeat of last year's wording.

**Composite index — geometric mean:**

```
GWL = √(GWLS × GWLE)
```

> A geometric mean, not an arithmetic one. This is a meaningful choice: it means a firm scores high
> overall only if it does *both* things. If either component is near zero, GWL is near zero. An
> arithmetic mean would let one component alone carry the score. Worth noting when we design our
> own composites.

**Training.** Two independent fine-tuning runs on two independently hand-labelled datasets
(80% train / 10% validation / 10% test). 6,493 sentences were labelled for the first task.
Labelling used written audit guidelines, independent annotators and iterative training.

## Headline results (real numbers)

**Agreement with human labelling:**

| Index | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| GWLS | 97.79% | 97.98% | 99.67% | 98.82% |
| GWLE | 95.13% | 95.54% | 95.64% | 95.59% |

MacBERT outperformed the comparison models overall, and recalculating GWL with alternative models
left the index materially unchanged — the authors' evidence that the index is not an artefact of
model choice.

## Limitations — including one the authors do not stress

- **Stated:** the item checklist is inherited from a specific prior indicator system, so the index
  inherits that system's judgements about what firms are "required" to disclose.
- **Stated:** the setting is Chinese A-share firms under a "semi-mandatory" disclosure regime;
  transferability to US filings is not tested.
- **My flag — no external reality anchor whatsoever.** Both components are computed *entirely
  from the report's own text*. The 97.79% accuracy figure measures agreement with **human
  annotators**, not agreement with **environmental reality**. A model can be near-perfect at
  identifying vague language and still tell you nothing about whether the firm pollutes. This is
  the same category of gap as in Davidescu et al. (note 01), stated more honestly here: Wang et al.
  never claim an external anchor, whereas Davidescu et al. claim one they do not implement.

## Connection to the other papers

- **Best-executed pure-text index in the set.** Sentence-level classification with a validated
  model is a genuine methodological step up from dictionary counting.
- **vs. Davidescu et al. (note 01):** both are composite text indices; the honesty of the framing
  differs. Also a methodological warning — if a fine-tuned transformer is needed to separate
  commitment from action, a TF–IDF keyword sum almost certainly cannot.
- **Direct relevance to our design:** the substantive-vs-symbolic distinction is exactly what
  **ClimateBERT**'s commitment-vs-action classifier does for English climate text. Wang et al. is
  our closest methodological template, and the geometric-mean composite is a design option for our
  own indices.
- **vs. Gorovaia & Makrominas (note 02) and Peng et al. (note 03):** those two supply the external
  validation this paper lacks. Combining Wang et al.'s measurement sophistication with their
  anchoring discipline is essentially the shape of our proposed study.
