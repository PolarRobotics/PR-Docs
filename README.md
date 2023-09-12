# PR-Docs
## Polar Robotics Documentation
### Local Installation
- Install `python3` and `pip` via your preferred method 
  - For Windows, via Microsoft Store or online installer
  - For Linux or WSL, `sudo apt-get install python3` and `sudo apt-get install python3-pip`
- Install `sphinx` with `pip install sphinx`
  - `sphinx-build --version` to check version and ensure sphinx installed properly
  - For completeness, the command to start a new documentation project/repo is `sphinx-quickstart`, but don't do this in this repo.
- Install the ReadTheDocs theme with `pip install sphinx-rtd-theme`
- Build the site by navigating to `/docs` and running `./make html`.
  - Note that `/` is the root of this project, and `./` refers to the current directory.