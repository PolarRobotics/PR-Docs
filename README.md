# PR-Docs
## Polar Robotics Documentation
### Local Installation
#### Installing Windows Subsystem for Linux
- If you are not on Windows, you can skip this section and proceed directly to Python/Sphinx installation.
- Using WSL is strongly recommended for development with Python and Sphinx.
  - If you do not already have `pip` fully functional on Windows and know how to utilize it, use WSL.
- You can either search for "Windows Subsystem for Linux" in the Microsoft Store, or run the command `wsl --install`.
  - You will likely be prompted to grant elevation/administrator-level access - grant this.
  - By default, WSL will install Ubuntu. Unless you are already familiar with another Linux distribution, continue with this distro.
  - You will need to reboot your computer after WSL has finished installing.
- Run WSL via the command `wsl` or via the start menu (search "wsl").
  - It may take a while to finish installing Ubuntu (or your chosen distro).'
- Once complete, WSL will ask you to choose a UNIX username and password.
  - Choose a brief appropriate username. Your first name or ONU email address name will suffice.
  - Choose a password. It need not be overly long, as you will need to type it frequently.
  - **When inputting your password, no characters will appear - this is normal.** Simply continue typing your desired password.
    - You will be asked to confirm your password by typing it again - this will help if you type it incorrectly.
- Once the previous steps have finished, you will be presented with a shell prompt that looks like this:

```sh
user@desktop:~$
```

- From here, you can continue to the next section to install Python and Sphinx.

#### Installing Python and Sphinx
- Install `python3` and `pip` via your package manager.
  - For Ubuntu, run `sudo apt-get install python3` and `sudo apt-get install python3-pip`.
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
  - `sphinx` may be installed in a path similar to `%appdata%\..\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages` or `%appdata%\..\Local\Programs\Python\Python310\Scripts`.

### Resources
- https://www.sphinx-doc.org/en/master/usage/markdown.html
- https://cerodell.github.io/sphinx-quickstart-guide/build/html/markdown.html
- https://myst-parser.readthedocs.io/en/latest/index.html
- https://docs.readthedocs.io/en/latest/tutorial/index.html
- https://www.writethedocs.org/guide/