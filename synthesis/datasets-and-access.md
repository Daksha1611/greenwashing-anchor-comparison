# Data sources: access, limits and fields

Six sources for the experimental phase. Each entry records what it gives us, how to get it, what
the constraints are, and what to watch out for.

**Status:** none of these has been accessed yet. Rate limits and field lists below come from the
providers' documented behaviour and should be **re-verified against the live docs** before the
pipeline is built — API terms change. Items I could not verify without hitting the API are marked
*(verify)*.

---

## 1. GDELT Project — media tone

- **URL:** https://www.gdeltproject.org/
- **Purpose:** historical global news volume and **computed tone** per entity — the input to
  GSI-media.
- **Access:** free, **no API key**. Two routes:
  - **DOC 2.0 API** (`https://api.gdeltproject.org/api/v2/doc/doc`) — article search and the
    `timelinetone` / `timelinevolinfo` modes. Best for per-firm time series.
  - **BigQuery** (`gdelt-bq.gdeltv2.events`, `.gkg`) — the Global Knowledge Graph, for bulk work.
    Needs a Google Cloud account; free tier covers ~1 TB of queries per month.
- **Why this and not NewsAPI:** NewsAPI's free tier returns roughly one month of history, which
  cannot support a multi-year panel. GDELT goes back to 1979 (Events) / 2015 (GKG v2).
- **Key fields:** `V2Tone` (comma-separated: average tone, positive score, negative score,
  polarity, activity reference density, self/group reference density, word count),
  `DocumentIdentifier`, `V2Organizations`, `V2Themes`, `DATE`, `SourceCommonName`.
- **Tone scale:** roughly −100 to +100, in practice mostly −10 to +10. Negative = negative coverage.
- **Constraints and gotchas:**
  - DOC 2.0 API returns a **maximum of 250 articles per query** and covers a rolling window;
    for long histories use BigQuery. *(verify current window)*
  - No published hard rate limit, but the service throttles aggressive polling — **space requests
    (~1/sec) and cache locally**.
  - **Company name matching is the hard part.** `V2Organizations` is populated by automated entity
    extraction and is noisy: "Apple" the company vs the fruit, subsidiaries under other names,
    ticker-vs-legal-name mismatches. Must be handled in the entity-matching module.
  - **Volume is confounded with size** — which is exactly what our salience regression tests.
    Retrieve article *counts* alongside tone; we need both.

## 2. EPA ECHO — environmental violations

- **URL:** https://echo.epa.gov/ · Web services: https://echo.epa.gov/tools/web-services
- **Purpose:** facility-level violations, inspections, enforcement actions and penalties — the
  input to GSI-violation.
- **Access:** free REST API, **no key required**. JSON/CSV output.
- **Main endpoints:**
  - `get_facilities` / `get_facility_info` — facility search and metadata
  - `get_case_report` — formal enforcement cases
  - `detailed_facility_report` — the richest per-facility view
  - Media-specific services: `cwa_rest_services` (Clean Water Act),
    `caa_rest_services` (Clean Air Act), `rcra_rest_services` (hazardous waste)
- **Key fields:** `RegistryID` (FRS ID), `FacName`, `FacStreet`/`FacCity`/`FacState`,
  `FacFederalAgencyFlag`, `CurrVioFlag`, `Insp5yr`, `FacQtrsWithNC` (quarters in non-compliance),
  `FacPenaltyCount`/`FacPenaltyAmt` (penalties, typically 5-year window),
  `FacComplianceStatus`, `DfrUrl`, and NAICS/SIC codes.
- **Constraints and gotchas:**
  - Query results are **paginated**; large pulls need cursor handling. Very broad queries can
    time out — filter by state or NAICS.
  - **Facilities are not companies.** One corporation owns many facilities under many operating
    names, and ownership changes over time. Aggregating facility violations to parent company is
    the central difficulty of this project — see the entity-matching discussion at the end of this file.
  - **Enforcement intensity varies by state and region**, so raw violation counts partly measure
    regulator activity, not just firm behaviour. Consider normalising by facility count or by
    state-year enforcement baseline.
  - Inherits the asymmetry Gorovaia & Makrominas flag: no violation ≠ clean.

## 3. EPA GHGRP / FLIGHT — greenhouse gas emissions

- **URL:** https://ghgdata.epa.gov/
- **Purpose:** facility-level GHG emissions — the input to GSI-emissions.
- **Access:** free. FLIGHT web interface with data export; bulk downloads (XLS/CSV) by year;
  also available via the **Envirofacts API**
  (`https://data.epa.gov/efservice/`), which serves the `PUB_DIM_FACILITY` and related tables.
- **Key fields:** `FACILITY_ID` (GHGRP ID), `FACILITY_NAME`, `PARENT_COMPANY`(!),
  `REPORTING_YEAR`, `CO2E_EMISSION` (total metric tons CO2 equivalent), `SUBPART`,
  `NAICS_CODE`, latitude/longitude, `FRS_ID`.
- **Constraints and gotchas:**
  - **Reporting threshold: facilities emitting ≥ 25,000 metric tons CO2e per year.** Small emitters
    and most service-sector firms are simply absent. This **structurally limits our sample** toward
    industrial firms — a sampling constraint we must state, not paper over.
  - Covers **direct (Scope 1)** emissions at US facilities. No Scope 2 or 3, and no non-US
    operations — so it is *not* comparable to the Refinitiv Scope 1+2 measure Peng et al. used.
  - GHGRP publishes a **`PARENT_COMPANY`** field with ownership percentages. This is the single
    most valuable shortcut for entity matching in this project — use it as a seed for the
    company → facility crosswalk.
  - Emissions are self-reported to EPA under regulation, so verified but not independent.

## 4. SEC EDGAR — filings and firm identity

- **URL:** https://www.sec.gov/edgar/search/
- **Purpose:** 10-K filings (for disclosure text), and the authoritative registry of US-listed
  firm identity (CIK, legal name, ticker, SIC).
- **Access:** free.
  - Full-text search API: `https://efts.sec.gov/LATEST/search-index?q=...`
  - Submissions API: `https://data.sec.gov/submissions/CIK##########.json`
  - Company tickers map: `https://www.sec.gov/files/company_tickers.json`
- **Requirements:** a descriptive **`User-Agent` header including a contact email is mandatory**;
  requests without one are blocked. **Rate limit: 10 requests/second**, enforced.
- **Key fields:** `cik`, `entityName`, `tickers`, `sic`, `sicDescription`, `stateOfIncorporation`,
  `formType`, `filingDate`, `accessionNumber`, former names with date ranges.
- **Why it is central here:** CIK is our **spine identifier**. Every other source gets joined to a
  CIK. EDGAR's *former names* history is essential for tracking firms through renames and mergers.
- **Gotchas:** 10-K Item 1A/Item 3 (risk factors, legal proceedings) mention environmental matters
  but in boilerplate; treat as supplementary, not as a violation anchor.

## 5. Responsibility Reports — sustainability report PDFs

- **URL:** https://www.responsibilityreports.com/
- **Purpose:** free archive of corporate sustainability/CSR report PDFs — the corpus our
  ClimateBERT scoring runs on.
- **Access:** free, browsable by company and year. **No API** — requires scraping.
- **Constraints and gotchas:**
  - **Check `robots.txt` and the site's terms before scraping; throttle politely** (≥ 2 s between
    requests). Cache every PDF locally so we fetch once.
  - Coverage is **uneven** — larger and more prominent firms are far better represented. This is
    precisely the selection bias Gorovaia & Makrominas designed their sampling to avoid, and it
    will bias our sample toward exactly the high-visibility firms our salience hypothesis concerns.
    **Mitigation: draw the sample frame from GHGRP/EDGAR first, then look for reports** — never
    the reverse.
  - PDFs vary wildly in structure; some are image-only and need OCR. Extraction failures must be
    logged, not silently dropped.

## 6. CDP — standardised climate disclosures

- **URL:** https://www.cdp.net/en/data
- **Purpose:** standardised, comparable self-reported climate data; useful as a cross-check on
  GHGRP and as a source of targets-vs-performance.
- **Access:** **the most restricted source in this list.** Some datasets are open (via the CDP
  Open Data Portal and Data Explorer); full corporate response datasets generally require a
  licence or an academic/investor agreement. *(verify current academic access terms)*
- **Key fields:** Scope 1 / 2 / 3 emissions, emissions reduction targets and progress, climate
  governance responses, CDP score (A–D−).
- **Constraints:** self-reported and **voluntary — participation itself correlates with size and
  visibility**, so CDP presence is not a neutral variable in a study about visibility.
- **Recommendation: treat CDP as optional.** The three core indices can be built without it.
  Do not let a licence negotiation block the pipeline.

---

## Joining strategy

```
                    SEC EDGAR (CIK)  ←  spine
                          │
      ┌───────────────────┼───────────────────┐
      │                   │                   │
  GHGRP PARENT_COMPANY  EPA ECHO FRS      GDELT V2Organizations
  → facility emissions  → violations       → tone + volume
      │                   │                   │
      └────────── entity_matching.py ─────────┘
                          │
              GSI-emissions / GSI-violation / GSI-media
```

**The weakest link is the join, not any single source.** GHGRP's `PARENT_COMPANY` and EPA's FRS
registry give partial crosswalks; GDELT gives only free-text organisation names. Budget real
effort here and measure match rates explicitly — an unmeasured match rate makes every downstream
correlation uninterpretable.

## Practical notes

- **Cache everything.** Every source should be saved locally on first fetch and never re-fetched
  in normal operation. Reproducibility and politeness both demand it.
- **Record retrieval dates.** ECHO and GDELT are living databases; results change under you.
- **Respect the identified rate limits** — SEC 10 req/s with a `User-Agent` contact is the only
  hard, documented, enforced one; the rest are courtesy limits that still get you blocked.
