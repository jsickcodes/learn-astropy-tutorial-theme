"""nbconvert preprocessor that extracts the document outline (TOC)."""

from __future__ import annotations

from typing import Any, Dict, Tuple

from nbconvert.preprocessors import Preprocessor
from nbformat import NotebookNode


class TocPreprocessor(Preprocessor):
    """An nbconvert preprocessor that extracts the document outline (TOC)
    into the resources for the HTML exporter to use.
    """

    def preprocess(
        self, nb: NotebookNode, resources: Dict[str, Any]
    ) -> Tuple[NotebookNode, Dict[str, Any]]:
        """Extract the document outline (TOC) into the resources for the HTML
        exporter to use.
        """
        resources["learn_astropy_toc"] = "hello from toc"
        return nb, resources
