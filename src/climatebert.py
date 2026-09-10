"""ClimateBERT scoring of disclosure language -- the "talk" half of every index.

https://huggingface.co/climatebert

WHY CLIMATEBERT AND NOT FINBERT
-------------------------------
FinBERT is trained on financial sentiment -- bullish vs bearish analyst language.
That is the wrong domain for climate disclosure text. ClimateBERT is pre-trained
on climate-related text and provides a commitment-vs-action classifier, which is
precisely the distinction this project needs.

CONCEPTUAL LINEAGE
------------------
This is the English-language analogue of Wang et al. (2025)'s symbolic-vs-
substantive split, which they implemented with MacBERT for Chinese CSR reports.
Their key insight, which we inherit: a keyword/dictionary method CANNOT separate
a concrete commitment from a vague aspiration, because both use the same
vocabulary. That is why a transformer is required and why Davidescu et al.'s
TF-IDF keyword sums cannot do this job.

Their validation figures, as a benchmark for ours: 97.79% accuracy / 98.82% F1
for selective disclosure; 95.13% / 95.59% for expressive manipulation -- against
HUMAN LABELS, not against environmental reality. Ours will be the same kind of
number and carries the same caveat.
"""


def load_model(model_name: str):
    """Load a ClimateBERT model and tokenizer.

    TODO
    ----
    - Use transformers AutoTokenizer / AutoModelForSequenceClassification.
    - Cache to disk; do not re-download per run.
    - Confirm exact model IDs against the ClimateBERT HF org before use --
      the ones in config.py are unverified.
    """
    raise NotImplementedError


def split_sentences(text: str) -> list[str]:
    """Split report text into sentences for classification.

    TODO
    ----
    - Use spacy. Sustainability reports are full of bullet lists, headings and
      table fragments that naive splitting mangles.
    - Drop fragments below a minimum token count -- they classify unreliably.
    """
    raise NotImplementedError


def classify_commitment_vs_action(sentences: list[str]) -> "pd.DataFrame":  # noqa: F821
    """Label each sentence as commitment (future promise) or action (done).

    Returns
    -------
    DataFrame: sentence, label, score

    TODO
    ----
    - Batch inference; these models are slow one sentence at a time.
    - Retain the probability, not just the argmax -- a firm-level ratio built
      from soft scores is less brittle than one built from hard labels.
    - Filter to climate-relevant sentences FIRST (climate detector model),
      otherwise the ratio is diluted by boilerplate.
    """
    raise NotImplementedError


def firm_disclosure_scores(classified: "pd.DataFrame") -> dict:  # noqa: F821
    """Aggregate sentence labels to firm-level disclosure measures.

    Returns
    -------
    dict with: n_climate_sentences, commitment_ratio, action_ratio,
               commitment_to_action_ratio

    TODO
    ----
    - `commitment_ratio` (talk-heavy, action-light) is the greenwashing-relevant
      direction.
    - Normalise by document length -- Gorovaia & Makrominas found violators write
      substantially LONGER reports (20,304 vs 15,091 words), so any raw count is
      partly just a length measure.
    - Decide whether to follow Wang et al.'s GEOMETRIC mean when combining
      components. Their reasoning is sound: a geometric mean scores a firm high
      only if it does both things, whereas an arithmetic mean lets one component
      carry the score. See notes/04.
    """
    raise NotImplementedError
