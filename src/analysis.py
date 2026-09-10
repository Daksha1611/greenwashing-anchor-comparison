"""Statistical comparison of the three indices -- the actual test.

Implements the tests specified in synthesis/open-questions.md 4.3:

    H1 convergence      Spearman rho between index pairs
    H2 top-decile       Jaccard index + Cohen's kappa
    H3 salience         OLS of GSI-media on size and coverage volume
    H4 anchor concord.  do the two HARD anchors agree better with each other?

PRE-SPECIFICATION
-----------------
Thresholds, the decile cut and the regression specification are fixed in
config.py BEFORE indices are computed. Do not tune them after seeing results.
"""


def spearman_matrix(indices: "pd.DataFrame", bootstrap: int = 1000) -> "pd.DataFrame":  # noqa: F821
    """Pairwise Spearman rank correlations with bootstrap confidence intervals.

    TODO
    ----
    - scipy.stats.spearmanr for point estimates.
    - Bootstrap CIs -- a point estimate alone cannot support a claim of
      divergence. "rho = 0.12, 95% CI [-0.04, 0.28]" is a finding; "rho = 0.12"
      is not.
    - Apply Benjamini-Hochberg across the pairwise tests; report raw AND
      adjusted p-values.
    """
    raise NotImplementedError


def top_decile_overlap(a: "pd.Series", b: "pd.Series", cut: float = 0.10) -> dict:  # noqa: F821
    """Agreement between two indices on which firms are the worst offenders.

    Returns
    -------
    dict: n_a, n_b, n_overlap, jaccard, cohens_kappa

    WHY BOTH STATISTICS
    -------------------
    Jaccard is the plain overlap (intersection / union). Cohen's kappa corrects
    for the overlap expected by chance. Reporting Jaccard alone would overstate
    agreement -- two random top-deciles overlap ~10% of the time by construction.

    WHY THE TAILS MATTER MOST
    -------------------------
    Whole-sample rank correlation can look respectable while the top deciles --
    the firms anyone would actually investigate or divest from -- disagree
    completely. This is the practically decisive test.

    TODO
    ----
    - sklearn.metrics.cohen_kappa_score on binary top-decile flags.
    - Re-run at ROBUSTNESS_CUTS (5%, 20%); conclusions must not hinge on 10%.
    """
    raise NotImplementedError


def salience_regression(
    panel: "pd.DataFrame",  # noqa: F821
    include_conduct: bool = False,
) -> "sm.regression.linear_model.RegressionResults":  # noqa: F821
    """Test H3: is GSI-media explained by visibility rather than conduct?

        GSI_media ~ log(size) + log(article_count) + C(sector)

    Parameters
    ----------
    include_conduct : bool
        Add GSI-violation / GSI-emissions to test INCREMENTAL validity. If real
        conduct adds little adjusted R-squared over size and coverage volume,
        that is direct support for the salience hypothesis.

    TODO
    ----
    - statsmodels OLS with sector fixed effects; cluster standard errors by firm.
    - Report adjusted R-squared for both specifications side by side -- the
      COMPARISON is the result, not either model alone.
    - Check VIF: size and article_count will correlate substantially. If they are
      collinear enough to be inseparable, say so plainly rather than reporting
      unstable coefficients as if they were interpretable.
    """
    raise NotImplementedError


def robustness_suite(panel: "pd.DataFrame", crosswalk: "pd.DataFrame") -> dict:  # noqa: F821
    """Re-run the headline tests under alternative specifications.

    TODO
    ----
    Required re-runs (open-questions.md 4.4):
      - HIGH-CONFIDENCE MATCH SUBSET ONLY. This one is not optional. Match noise
        biases correlations toward zero, which would mimic our hypothesised
        result. A null finding is uninterpretable without it.
      - Emissions intensity in place of absolute emissions.
      - Alternative GDELT tone windows (calendar year vs trailing 12 months).
      - Top 5% and top quintile in place of top decile.
      - Lagged media tone, to probe reverse causality (coverage may FOLLOW a
        violation rather than independently detect greenwashing).
    """
    raise NotImplementedError
