"""Test for the Learn Astropy HTML theme."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

from learnastropytutorialtheme.html import LearnAstropyHtmlExporter

from .support.helpers import write_conversion


def test_html_export() -> None:
    """Smoke test for the HTML export.

    Output is written to _build/html_export.
    """
    test_notebook = Path(__file__).parent.joinpath("color-excess.ipynb")
    html, resources = LearnAstropyHtmlExporter().from_filename(
        str(test_notebook.resolve())
    )
    resources = deepcopy(resources)
    resources["learn_astropy_editor_url"] = (
        "https://mybinder.org/v2/gh/astropy/astropy-tutorials/"
        "main?labpath=tutorials%2Fcolor-excess%2Fcolor-excess.ipynb"
    )
    resources["learn_astropy_source_url"] = (
        "https://github.com/astropy/astropy-tutorials/blob/main/tutorials/"
        "color-excess/color-excess.ipynb"
    )
    resources[
        "learn_astropy_ipynb_download_url"
    ] = "https://learn.astropy.org/tutorials/color-excess.ipynb"
    write_conversion(base_dir="html_export", content=html, resources=resources)
