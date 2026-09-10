"""EPA GHGRP / FLIGHT loader -- the emissions anchor.

https://ghgdata.epa.gov/ -- bulk downloads by year; also served through the
Envirofacts API at https://data.epa.gov/efservice/

STRUCTURAL SAMPLE CONSTRAINT
----------------------------
GHGRP covers only facilities emitting >= 25,000 metric tons CO2e per year. Small
emitters and most service-sector firms are ABSENT ENTIRELY. Any GHGRP-based
sample frame is therefore skewed toward industrial firms. This is a real
limitation of the study and must be stated in the write-up, not worked around.

SCOPE MISMATCH -- do not compare naively to Peng et al. (2024)
-------------------------------------------------------------
GHGRP covers direct (Scope 1) emissions at US facilities only. Peng et al. used
Refinitiv Scope 1 + Scope 2 across global operations. The two measures are NOT
interchangeable, and any comparison to their coefficients must say so.

USEFUL: GHGRP publishes a PARENT_COMPANY field with ownership percentages -- the
best available seed for company-to-facility matching. See entity_matching.
"""


def load_ghgrp_year(year: int) -> "pd.DataFrame":  # noqa: F821
    """Load one year of GHGRP facility emissions.

    Returns
    -------
    DataFrame: FACILITY_ID, FACILITY_NAME, PARENT_COMPANY, ownership_pct,
               REPORTING_YEAR, CO2E_EMISSION, NAICS_CODE, FRS_ID, lat, lon

    TODO
    ----
    - Prefer the annual bulk download over per-facility API calls.
    - Cache to data/raw/ghgrp/; record retrieval date.
    - FRS_ID is the bridge to ECHO -- preserve it carefully, it saves most of the
      ECHO matching work.
    """
    raise NotImplementedError


def aggregate_to_parent(
    facilities: "pd.DataFrame",  # noqa: F821
    crosswalk: "pd.DataFrame",  # noqa: F821
) -> "pd.DataFrame":  # noqa: F821
    """Roll facility emissions up to firm-year.

    TODO
    ----
    - Attribute pro-rata by ownership percentage where reported. Document the
      choice; full attribution to a majority owner is defensible but must be
      stated.
    - Produce BOTH absolute emissions and intensity (emissions / revenue). Peng
      et al. found the two behave differently -- absolute CE coefficient 0.775
      vs intensity CI 1.304 -- so reporting only one hides variation.
    - Revenue for the intensity denominator comes from SEC filings; note the
      currency/units and fiscal-year alignment.
    """
    raise NotImplementedError
