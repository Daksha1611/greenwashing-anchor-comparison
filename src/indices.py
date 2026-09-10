"""The three index constructors.

Each index pairs the SAME disclosure measure (ClimateBERT commitment-heavy
language) with a DIFFERENT reality anchor. That is the whole design: hold the
"talk" constant, vary the "action", and see whether the resulting rankings agree.

    GSI-media      : talk vs media tone         (GDELT)
    GSI-violation  : talk vs violation record   (EPA ECHO)
    GSI-emissions  : talk vs measured emissions (EPA GHGRP)

All three are standardised to a common scale before comparison, since the raw
units (tone points, penalty dollars, tonnes CO2e) are incommensurable.

ALSO IMPLEMENTED HERE, as a reference point: the Davidescu et al. (2026) GSI
exactly as published. We do NOT claim to replicate their full index -- the
component scores are not reproducible from the paper (see
synthesis/gsi-formula.md 4) -- but the aggregation rule IS recoverable and has
been verified to 4 d.p. against their published tables.
"""


def standardise(series: "pd.Series", method: str = "zscore") -> "pd.Series":  # noqa: F821
    """Put an index on a comparable scale.

    TODO
    ----
    - Default z-score. Offer rank-based (percentile) as an alternative, since our
      headline tests are rank-based anyway and percentiles are robust to the
      heavy tails in penalty and emissions data.
    - Standardise WITHIN year if pooling across years.
    - Do NOT use Min-Max here without thinking: it is population-dependent, which
      is one of the reasons Davidescu et al.'s index cannot be reproduced.
    """
    raise NotImplementedError


def gsi_media(
    disclosure: "pd.DataFrame",  # noqa: F821
    gdelt_tone: "pd.DataFrame",  # noqa: F821
) -> "pd.DataFrame":  # noqa: F821
    """Media-anchored greenwashing index.

    High when a firm talks green (commitment-heavy disclosure) but media coverage
    of its environmental conduct is negative.

    Returns
    -------
    DataFrame: firm_id, year, gsi_media, article_count, mean_tone

    IMPORTANT: `article_count` is returned alongside the index, not consumed by
    it. It is the visibility regressor for H3. Keep them separate -- folding
    volume into the index would make the salience test circular.

    TODO
    ----
    - Specify the combination rule EXPLICITLY and document it. This is our own
      index, stated in full, precisely because Davidescu et al.'s media anchoring
      is not recoverable from their paper.
    - Proposal: standardise commitment_ratio and negated mean_tone separately,
      then combine. Consider the geometric mean per Wang et al.
    - Drop firm-years below the minimum article threshold (see gdelt.py).
    """
    raise NotImplementedError


def gsi_violation(
    disclosure: "pd.DataFrame",  # noqa: F821
    echo_violations: "pd.DataFrame",  # noqa: F821
) -> "pd.DataFrame":  # noqa: F821
    """Violation-anchored greenwashing index.

    High when a firm talks green but has a substantive violation record.
    This is the closest analogue to Gorovaia & Makrominas (2025), though anchored
    to EPA ECHO directly rather than to commercial database fine fields.

    TODO
    ----
    - Use per-facility-normalised violation rates, not raw counts (see
      echo_client.aggregate_to_parent).
    - Firms matched to zero facilities must be EXCLUDED, not scored as clean.
    - Record that non-violation != compliance, and carry that caveat into the
      write-up rather than only into this docstring.
    """
    raise NotImplementedError


def gsi_emissions(
    disclosure: "pd.DataFrame",  # noqa: F821
    ghgrp_emissions: "pd.DataFrame",  # noqa: F821
    intensity: bool = False,
) -> "pd.DataFrame":  # noqa: F821
    """Emissions-anchored greenwashing index.

    High when a firm talks green but emits heavily. Closest analogue to
    Peng et al. (2024).

    Parameters
    ----------
    intensity : bool
        Use emissions/revenue instead of absolute. Peng et al. found the two
        behave differently, so BOTH must be reported.

    TODO
    ----
    - Sector-relative emissions: a cement plant is not comparable to a software
      firm on absolute tonnes. Consider within-NAICS standardisation, and note
      that this interacts with the sector fixed effects in the H3 regression.
    """
    raise NotImplementedError


def davidescu_gsi_as_published(
    e_score: "pd.Series",  # noqa: F821
    s_score: "pd.Series",  # noqa: F821
    g_score: "pd.Series",  # noqa: F821
) -> "pd.Series":  # noqa: F821
    """Davidescu et al. (2026) GSI, exactly as published.

        GSI = (1/3)*E + (1/3)*S + (1/3)*G

    VERIFIED: reproduces the paper's published figures to 4 d.p. across every
    reported grouping (whole sample 0.5765; Germany 0.6086; Poland 0.5414;
    Lithuania 0.5157). See synthesis/gsi-formula.md 2.

    NOTE what this index is and is not. Every input derives from the firm's own
    report, so it measures ESG term density in disclosure -- NOT a report-vs-media
    discrepancy, despite the paper's description. Implemented here as a reference
    point and to support the secondary question in open-questions.md 6: does
    disclosure intensity, on its own, correlate with ANY reality anchor?

    TODO
    ----
    - Trivial to implement; the hard part is the inputs.
    - Components require the A.2-A.4 dictionaries (122 terms each), still to be
      transcribed from the PDF appendices into data/raw/dictionaries/.
    - Exact component reproduction is NOT possible: the Min-Max normalisation
      population and the TF-IDF document collection are both unstated. Any
      implementation is ours, not theirs -- label it accordingly in the write-up.
    """
    raise NotImplementedError
