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

````MyST
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