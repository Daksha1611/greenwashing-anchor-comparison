"""Greenwashing anchor-comparison pipeline.

Scaffold only. No module here is implemented; every function raises
NotImplementedError. See ../synthesis/open-questions.md for the experimental
design these modules will serve.

Pipeline order:
    1. entity_matching  -- build the firm universe and the join keys (do this FIRST)
    2. pdf_extract      -- sustainability report text
    3. climatebert      -- score disclosure language (the "talk" half)
    4. gdelt / echo / ghgrp -- retrieve the three reality anchors
    5. indices          -- construct GSI-media, GSI-violation, GSI-emissions
    6. analysis         -- Spearman, Jaccard, Cohen's kappa, salience regression
"""

__version__ = "0.1.0"
