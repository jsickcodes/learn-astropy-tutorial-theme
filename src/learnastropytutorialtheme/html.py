"""HTML Exporter for Learn Astropy Tutorials."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from nbconvert.exporters.html import HTMLExporter


class LearnAstropyHtmlExporter(HTMLExporter):
    """HTML exporter for Learn Astropy HTML notebooks."""

    export_from_notebook = "Learn Astropy HTML"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        # Add the default template to the search path
        self.extra_template_basedirs.append(self._template_name_default())

    def _template_name_default(self) -> str:
        """Select built-in HTML theme as the default.

        Overrides `HTMLExporter._template_name_default`.
        """
        return str(
            Path(__file__).parent.joinpath("templates").joinpath("html")
        )

    def _init_resources(self, resources: Dict[str, Any]) -> Dict[str, Any]:
        """Add additional metadata to the Jinja context via the resources
        dictionary.
        """
        resources = super()._init_resources(resources)
        resources["Learn"] = "Astropy!"

        # Toggle between 'light' and 'dark' themes
        resources["theme"] = "light"

        return resources
