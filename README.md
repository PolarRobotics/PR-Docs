# PR-Docs
## Polar Robotics Documentation
### Local Installation
- Install `python3` and `pip` via your preferred method.
  - For Windows, via Microsoft Store or an online installer (Google "python 3")
  - For Linux or WSL, `sudo apt-get install python3` and `sudo apt-get install python3-pip` (or use appropriate package manager for your distro)
    - You may also be able to directly install Sphinx using your package manager.
- Install `sphinx` with `pip install -U sphinx`
  - `sphinx-build --version` to check version and ensure sphinx installed properly
  - For completeness, the command to start a new documentation project/repo is `sphinx-quickstart`, but don't do this in this repo.
- Install the ReadTheDocs theme with `pip install -U sphinx-rtd-theme`.
- Install the MyST-Parser Markdown parser with `pip install -U myst-parser`.
- Build the site by navigating to `/docs` and running `./make html`.
  - Note that `/` is the root of this project, and `./` refers to the current directory.

#### Editing
- It is recommended to install the [MyST extension](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) as this is the flavor of Markdown being used for our documentation.
  - After installation, when editing a Markdown file in VS Code, you can press `Ctrl+K`, then `V`

#### Troubleshooting
- https://pip.pypa.io/en/stable/installation/
- Windows: If `pip` is not registered as a command, run `py -m ensurepip --upgrade`. This should install pip. 
  - You will need to restart your shell and possibly your computer before `pip` will function.

### Resources
- https://www.sphinx-doc.org/en/master/usage/markdown.html
- https://cerodell.github.io/sphinx-quickstart-guide/build/html/markdown.html
- https://myst-parser.readthedocs.io/en/latest/index.html
- https://docs.readthedocs.io/en/latest/tutorial/index.html
- https://www.writethedocs.org/guide/