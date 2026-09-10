"""Extract text from sustainability report and paper PDFs.

Uses pypdf (PyPDF2 is deprecated and must not be used).

Design notes
------------
Extraction failures must be LOGGED, never silently dropped. A report that fails
to parse is a missing observation, and if we lose those quietly the sample
composition shifts without our knowing -- which matters especially here, since
scan-only PDFs correlate with smaller and older firms.
"""

from pathlib import Path


def extract_text(pdf_path: Path, layout: bool = True) -> str:
    """Return the full text of a PDF.

    Parameters
    ----------
    pdf_path : Path
    layout : bool
        Preserve visual layout. Helps keep table rows intact, which matters when
        parsing reports that carry emissions figures in tables.

    Returns
    -------
    str

    TODO
    ----
    - Implement with pypdf.PdfReader.
    - Detect image-only PDFs (near-zero extractable characters) and flag them for
      OCR rather than returning an empty string that looks like a valid parse.
    - Record per-file: page count, character count, extraction method, timestamp.
    """
    raise NotImplementedError


def extract_sections(text: str, headings: list[str]) -> dict[str, str]:
    """Split report text into named sections by heading.

    TODO
    ----
    - Sustainability reports have no standard structure; headings vary wildly.
      Start with fuzzy heading matching and expect to hand-tune.
    - Consider whether section-level analysis is needed at all, or whether
      whole-document sentence classification (per Wang et al. 2025) suffices.
      Prefer the latter if it works -- fewer arbitrary choices to defend.
    """
    raise NotImplementedError


def batch_extract(pdf_dir: Path, out_dir: Path) -> "pd.DataFrame":  # noqa: F821
    """Extract every PDF in a directory, returning a manifest of outcomes.

    The manifest is the point: it records successes AND failures, so sample
    attrition is visible.

    TODO
    ----
    - Cache: never re-extract a PDF whose output already exists.
    - Return columns: source_path, cik, year, n_pages, n_chars, status, error.
    """
    raise NotImplementedError
