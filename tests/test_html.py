"""Test for the Learn Astropy HTML theme."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import pytest

from learnastropytutorialtheme.html import LearnAstropyHtmlExporter

from .support.helpers import write_conversion


@pytest.mark.parametrize("theme", ["light", "dark"])
def test_html_export(theme: str) -> None:
    """Integration test for the HTML export with light and dark theme variants.

    Output is written to `_build/{theme}`.
    """
    test_notebook = Path(__file__).parent.joinpath("color-excess.ipynb")

    resources = {
        "learn_astropy_editor_url": (
            "https://mybinder.org/v2/gh/astropy/astropy-tutorials/"
            "main?labpath=tutorials%2Fcolor-excess%2Fcolor-excess.ipynb"
        ),
        "learn_astropy_source_url": (
            "https://github.com/astropy/astropy-tutorials/blob/main/tutorials/"
            "color-excess/color-excess.ipynb"
        ),
        "learn_astropy_ipynb_download_url": (
            "https://learn.astropy.org/tutorials/color-excess.ipynb"
        ),
    }

    exporter = LearnAstropyHtmlExporter()
    exporter.theme = theme
    html, resources = exporter.from_filename(
        str(test_notebook.resolve()), resources=resources
    )

    resources = deepcopy(resources)
    write_conversion(base_dir=theme, content=html, resources=resources)
