"""HTML Exporter for Learn Astropy Tutorials."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from nbconvert.exporters.html import HTMLExporter


class LearnAstropyHtmlExporter(HTMLExporter):
    """HTML exporter for Learn Astropy HTML notebooks."""

    export_from_notebook = "Learn Astropy HTML"

    @property
    def extra_template_basedirs(self) -> List[str]:
        """Include this package's built-in template in the search path."""
        _paths = super()._default_extra_template_basedirs()
        _paths.append(self._template_name_default())
        return _paths

    def _template_name_default(self) -> str:
        """Select built-in HTML theme as the default."""
        return str(
            Path(__file__).parent.joinpath("templates").joinpath("html")
        )

    def _init_resources(self, resources: Dict[str, Any]) -> Dict[str, Any]:
        """Add additional metadata to the Jinja context via the resources
        dictionary.
        """
        resources = super()._init_resources(resources)
        resources["Learn"] = "Astropy!"
        return resources
