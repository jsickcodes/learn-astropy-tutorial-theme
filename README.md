# Learn Astropy Tutorial Theme

This is an [nbconvert](https://nbconvert.readthedocs.io/) custom exporter and template for [Learn Astropy's](https://learn.astropy.org) Jupyter notebook-based tutorials.

## Features

- This theme adds a header, sidebar, and footer around the core notebook HTML content. The header includes links to the Learn Astropy site along with links for downloading the notebook, opening in Binder, and viewing the notebook on GitHub.
- The theme automatically runs a custom `TocPreprocessor` nbconvert preprocessor that extracts the document outline from Markdown cells and renders a document outline in the sidebar.
- Dark and light themes are supported, though they need to be rendered as separate HTML files.

## Resources schema

The Learn Astropy Tutorial Theme can add links to the rendered notebook HTML to make the page work within the larger Learn Astropy site.
These links are
You can configure these links by setting the `resources` parameter when running the HTML exporter (e.g. with the `LearnAstropyHtmlExporter.from_filename` method) with a dictionary containing the following keys:

- `learn_astropy_editor_url`. The URL to the notebook in an online notebook viewer/editor, such as Binder. The user must compute the full URL. Omit this field if you do not want to include a link to an online editor.
- `learn_astropy_editor_label`. The text for the link to the editor. Defaults to "Open in Binder".
- `learn_astropy_source_url`. The URL to the notebook in a source code repository, such as GitHub. Omit this field if you do not want to include a link to the source code.
- `learn_astropy_source_label`. The text for the link to the source code. Defaults to "View on GitHub".
- `learn_astropy_ipynb_download_url`. The URL to download this notebook as a Jupyter notebook file. Omit this field if you do not want to include a link to download the notebook.

## Usage with Python API

```python
from pathlib import Path
from traitlets.config import Config
from learnastropytutorialtheme.html import LearnAstropyHtmlExporter

nb_path = Path("path/to/notebook.ipynb")

config = Config()  # add additional nbconvert exporter configuration here

# Add theme configuration / metadata
resources = {
    "learn_astropy_editor_url": "https://mybinder.org/v2/gh/...",
    "learn_astropy_source_url": "https://github.com/...",
    "learn_astropy_ipynb_download_url": (
        "https://learn.astropy.org/tutorials/..."
    ),
}

exporter = LearnAstropyHtmlExporter(config=config)
exporter.theme = "light"  # or "dark"
html, resources = exporter.from_filename(str(nb_path), resources=resources)

Path(f"{resources['name']}.html").write_text(html)
for name, content in resources["outputs"].items():
    Path(name).write_bytes(content)
```
