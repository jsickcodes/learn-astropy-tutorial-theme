# Learn Astropy Tutorial Theme

This is an [nbconvert](https://nbconvert.readthedocs.io/) custom exporter and template for Learn Astropy's Jupyter notebook-based tutorials.

## Resources schema

The Learn Astropy Tutorial Theme can add links to the rendered notebook HTML to make the page work within the larger Learn Astropy site.
These links are
You can configure these links by setting the `resources` parameter when running the HTML exporter (e.g. with the `LearnAstropyHtmlExporter.from_filename` method) with a dictionary containing the following keys:

- `learn_astropy_editor_url`. The URL to the notebook in an online notebook viewer/editor, such as Binder. The user must compute the full URL. Omit this field if you do not want to include a link to an online editor.
- `learn_astropy_editor_label`. The text for the link to the editor. Defaults to "Open in Binder".
- `learn-astropy_source_url`. The URL to the notebook in a source code repository, such as GitHub. Omit this field if you do not want to include a link to the source code.
- `learn_astropy_source_label`. The text for the link to the source code. Defaults to "View on GitHub".
- `learn_astropy_ipynb_download_url`. The URL to download this notebook as a Jupyter notebook file. Omit this field if you do not want to include a link to download the notebook.
