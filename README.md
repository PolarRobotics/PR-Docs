# PR-Docs
## Polar Robotics Documentation
### Local Installation
- Install `python3` and `pip` via your preferred method 
  - For Windows, via Microsoft Store or online installer
  - For Linux or WSL, `sudo apt-get install python3` and `sudo apt-get install python3-pip`
- Install `sphinx` with `pip install -U sphinx`
  - `sphinx-build --version` to check version and ensure sphinx installed properly
  - For completeness, the command to start a new documentation project/repo is `sphinx-quickstart`, but don't do this in this repo.
- Install the ReadTheDocs theme with `pip install -U sphinx-rtd-theme`.
- Install the MyST-Parser Markdown parser with `pip install -U myst-parser`.
- Build the site by navigating to `/docs` and running `./make html`.
  - Note that `/` is the root of this project, and `./` refers to the current directory.


### Resources
- https://www.sphinx-doc.org/en/master/usage/markdown.html
- https://docs.readthedocs.io/en/latest/tutorial/index.html
- https://www.writethedocs.org/guide/