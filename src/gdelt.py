"""GDELT tone retrieval -- the media anchor.

GDELT is used instead of NewsAPI because NewsAPI's free tier returns roughly one
month of history, which cannot support a multi-year panel. GDELT has no API key
requirement and reaches back much further.

Two access routes:
    DOC 2.0 API : https://api.gdeltproject.org/api/v2/doc/doc
                  Good for per-firm queries. Capped at ~250 articles per query
                  and a rolling window. TODO: verify the current window.
    BigQuery    : gdelt-bq.gdeltv2.gkg -- for bulk/long history. Needs a GCP
                  account; ~1 TB/month of queries is free.

CRITICAL DESIGN POINT
---------------------
Article VOLUME is retained as a first-class output, not discarded as a nuisance.
The number of articles about a firm is a direct measure of media visibility, and
it is the key regressor in the salience hypothesis (H3). A pipeline that returns
only mean tone throws away the variable the study is actually about.
"""


def query_tone(
    company_aliases: list[str],
    start_date: str,
    end_date: str,
    esg_filter: bool = True,
) -> "pd.DataFrame":  # noqa: F821
    """Retrieve article-level tone for one firm over a date range.

    Parameters
    ----------
    company_aliases : list[str]
        Query strings from entity_matching.match_to_gdelt.
    esg_filter : bool
        Restrict to sustainability/ESG/environment-related coverage. Without
        this the tone reflects general business news (earnings, M&A) rather than
        environmental reputation.

    Returns
    -------
    DataFrame with at least: date, url, domain, tone, positive_score,
    negative_score, polarity, matched_alias.

    TODO
    ----
    - Parse V2Tone: comma-separated as
      tone,positive,negative,polarity,activity_density,self_ref_density,word_count.
    - Respect GDELT_COURTESY_DELAY_SEC between requests.
    - CACHE to data/raw/gdelt/ keyed by (alias, date range). Never re-fetch.
    - Record the retrieval date -- GDELT is a living database.
    - Define the ESG filter as an explicit, documented theme/keyword list, not an
      ad-hoc string. It is a research choice and must be reproducible.
    """
    raise NotImplementedError


def aggregate_firm_year(articles: "pd.DataFrame") -> "pd.DataFrame":  # noqa: F821
    """Collapse article-level tone to firm-year observations.

    Returns
    -------
    DataFrame: firm_id, year, mean_tone, median_tone, tone_sd,
               article_count, domain_count

    `article_count` and `domain_count` are the VISIBILITY measures -- carry them
    forward, they are not diagnostics.

    TODO
    ----
    - Decide and document the minimum article count for a usable firm-year
      observation. A mean tone computed from two articles is noise. Proposal:
      require >= 10, and report how many firm-years this drops.
    - Consider trimming or winsorising extreme tone values.
    - Provide both calendar-year and trailing-12-month windows (robustness check
      in open-questions.md 4.4).
    """
    raise NotImplementedError
