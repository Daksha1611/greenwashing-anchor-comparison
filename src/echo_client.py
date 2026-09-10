"""EPA ECHO REST client -- the regulatory violation anchor.

https://echo.epa.gov/tools/web-services -- free, no API key.

Endpoints of interest:
    get_facilities / get_facility_info  -- facility search and metadata
    detailed_facility_report            -- richest per-facility view
    get_case_report                     -- formal enforcement cases
    cwa_/caa_/rcra_rest_services        -- media-specific detail

TWO ASYMMETRIES THAT MUST BE CARRIED THROUGH THE WHOLE PIPELINE
---------------------------------------------------------------
1. No recorded violation does NOT mean clean -- only unpenalised. Gorovaia &
   Makrominas are explicit that a fine-based measure gives positive assurance for
   violators and only negative assurance for everyone else. Our GSI-violation
   inherits this exactly.
2. A firm matched to ZERO facilities is not the same as a firm with zero
   violations. Conflating the two would silently score unmatched firms as clean.
   Keep `n_facilities_matched` alongside every violation count.
"""


def get_facilities(
    state: str | None = None,
    naics: str | None = None,
    name: str | None = None,
) -> "pd.DataFrame":  # noqa: F821
    """Search ECHO facilities.

    TODO
    ----
    - Handle pagination via cursor; broad queries time out, so filter by state
      or NAICS and iterate.
    - Return at least: RegistryID (FRS), FacName, FacState, NAICS, FacLat/FacLong.
    - Respect ECHO_COURTESY_DELAY_SEC; cache to data/raw/echo/.
    """
    raise NotImplementedError


def get_facility_violations(registry_id: str, years: range) -> "pd.DataFrame":  # noqa: F821
    """Retrieve violation, inspection and penalty history for one facility.

    TODO
    ----
    - Pull: FacQtrsWithNC (quarters in non-compliance), CurrVioFlag, Insp5yr,
      FacPenaltyCount, FacPenaltyAmt, FacComplianceStatus.
    - NOTE the reporting windows: several ECHO fields are fixed 3- or 5-year
      lookbacks, NOT per-year values. Do not treat them as annual observations
      without checking. This is an easy and serious error.
    - Where per-year granularity is needed, use get_case_report and date-filter
      the enforcement actions.
    """
    raise NotImplementedError


def aggregate_to_parent(
    facility_violations: "pd.DataFrame",  # noqa: F821
    crosswalk: "pd.DataFrame",  # noqa: F821
) -> "pd.DataFrame":  # noqa: F821
    """Roll facility-level violations up to parent company / firm-year.

    TODO
    ----
    - Join on the year-aware crosswalk from entity_matching.
    - Sum penalties and counts; also compute per-facility rates, since a firm
      with 200 facilities will mechanically accrue more violations than one with
      3. Raw counts alone would just re-measure firm size -- the exact confound
      this study exists to expose.
    - Consider normalising by a state-year enforcement baseline: ECHO reflects
      REGULATOR activity as well as firm conduct, and enforcement intensity
      varies by state and EPA region.
    - Carry n_facilities_matched through. Always.
    """
    raise NotImplementedError
