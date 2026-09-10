"""Shared configuration and constants.

TODO: move secrets (if any are ever needed) to environment variables, never here.
"""

from pathlib import Path

# --- Paths ---------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_INTERIM = PROJECT_ROOT / "data" / "interim"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
PAPERS_DIR = PROJECT_ROOT / "Papers"

# --- Sample frame --------------------------------------------------------
# See synthesis/open-questions.md 4.1. Frame is built from GHGRP+EDGAR first,
# then reports are sought -- never the reverse, which would reintroduce the
# selection bias Gorovaia & Makrominas designed their sampling to avoid.
TARGET_SAMPLE_MIN = 150
TARGET_SAMPLE_MAX = 300
STUDY_YEARS = range(2019, 2024)

# --- API etiquette -------------------------------------------------------
# SEC's limit is documented and enforced; the others are courtesy limits that
# will still get you blocked. TODO: re-verify all of these against live docs.
SEC_USER_AGENT = "TODO-set-contact-email"  # SEC REQUIRES a contact email; requests without one are refused
SEC_RATE_LIMIT_PER_SEC = 10
GDELT_COURTESY_DELAY_SEC = 1.0
ECHO_COURTESY_DELAY_SEC = 0.5
SCRAPE_COURTESY_DELAY_SEC = 2.0

# --- Analysis parameters (PRE-SPECIFIED -- do not tune after seeing results) ---
DIVERGENCE_RHO_THRESHOLD = 0.3   # |rho| below this is read as divergence (H1)
TOP_DECILE = 0.10                # primary cut for Jaccard / Cohen's kappa (H2)
ROBUSTNESS_CUTS = (0.05, 0.20)   # top 5% and top quintile, as robustness checks

# --- Models --------------------------------------------------------------
# ClimateBERT, not FinBERT: FinBERT is trained on financial (bullish/bearish)
# sentiment and is the wrong domain for climate disclosure text.
CLIMATEBERT_COMMITMENT_MODEL = "climatebert/distilroberta-base-climate-commitment"
CLIMATEBERT_DETECTOR_MODEL = "climatebert/distilroberta-base-climate-detector"
# TODO: confirm exact model IDs on https://huggingface.co/climatebert before use.

# --- Reporting thresholds we inherit from the data -----------------------
GHGRP_REPORTING_THRESHOLD_TCO2E = 25_000  # facilities below this simply are not in GHGRP
