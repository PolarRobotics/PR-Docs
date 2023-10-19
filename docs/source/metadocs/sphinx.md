# Sphinx
- This documentation site uses [Sphinx](https://www.sphinx-doc.org/en/master/) with the [ReadTheDocs](https://about.readthedocs.com/) theme.
- All documentation files should be using [Markdown](https://www.markdownguide.org/cheat-sheet/).
  - Specifically, we use [MyST (Markedly Structured Text)](https://myst-parser.readthedocs.io/en/latest/) which is a Markdown version of reStructuredText (the default markup language for Sphinx).
  - [This quickstart guide](https://cerodell.github.io/sphinx-quickstart-guide/build/html/markdown.html) is also useful.
  - [The official documentation of syntax is here.](https://myst-parser.readthedocs.io/en/v0.16.1/syntax/syntax.html)

## Tables of Contents
- In order to be accessible outside of searching directly for it, a page needs to be added to a *table of contents*, or `toctree`.
  -  One of these is in `index.md` (on the site, `/index.html`).
- See also the [syntax documentation](https://myst-parser.readthedocs.io/en/v0.16.1/syntax/syntax.html) linked above.
- An example of the `toctree` syntax from [this resource](https://coderefinery.github.io/sphinx-lesson/toctree/) is below.
  - Essentially, this is a codeblock with a unique language ID that tells MyST to parse it differently.

````
```{toctree}
---
caption: Contents
maxdepth: 1
---

basics
creating-using-web
creating-using-desktop
contributing
doi
websites
```
````

### Generating TOCs
- It is easier to generate TOCs using `tree`.
  - For instance, to list all the files in `docs/source/hardware` in the format needed to place in the TOC in `index.md`, use the command below.
    - The `sed` command uses regex to remove the extensions from any files (including `.md` in the `toctree` doesn't work).


```sh
# from /docs/source
tree -if --noreport hardware | sed 's/\.[^.]*$//'
```

## Hosting on ReadTheDocs
- This documentation page is hosted via ReadTheDocs.
  - This requires a few things in order to build successfully:
    - `/.readthedocs.yaml`, a configuration file
      - In our case, it was necessary to change the path to `conf.py` appropriately.
      - It was also necessary to uncomment the bottom section to install python requirements.
    - `/requirements.txt`
      - This is generated with `pip freeze > requirements.txt`.