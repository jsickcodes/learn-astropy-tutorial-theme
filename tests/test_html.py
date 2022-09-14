"""Test for the Learn Astropy HTML theme."""

from __future__ import annotations

from pathlib import Path

from learnastropytutorialtheme.html import LearnAstropyHtmlExporter

from .lib.helpers import write_conversion


def test_html_export() -> None:
    """Smoke test for the HTML export.

    Output is written to _build/html_export.
    """
    test_notebook = Path(__file__).parent.joinpath("color-excess.ipynb")
    html, resources = LearnAstropyHtmlExporter().from_filename(test_notebook)
    write_conversion(base_dir="html_export", content=html, resources=resources)
