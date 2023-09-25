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
- The following steps should be done inside WSL (or in your terminal, if on Linux or MacOS).
- Update your packages via your package manager.
  - For Ubuntu, run `sudo apt-get update` and then `sudo apt-get upgrade`.
- Install `python3` and `pip` via your package manager.
  - For Ubuntu, run `sudo apt-get install python3` and `sudo apt-get install python3-pip`.
  - For MacOS, you will need to install Homebrew, and use `brew` to install these packages.
- Install `sphinx` with `pip install -U sphinx`
  - `sphinx-build --version` to check version and ensure sphinx installed properly
    - You may also be able to install `sphinx` or `python3-sphinx` directly from your package manager.
  - For completeness, the command to start a new documentation project/repo is `sphinx-quickstart`, but don't do this in this repo.
- Install the ReadTheDocs theme with `pip install -U sphinx-rtd-theme`.
- Install the MyST-Parser Markdown parser with `pip install -U myst-parser`.
- It is recommended to install the [MyST extension](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) as this is the flavor of Markdown being used for our documentation.
  - After installation, when editing a Markdown file in VS Code, you can press `Ctrl+K`, then `V` to open a pane to render the Markdown source file, providing you a preview of the file you are working on.

#### Contributing
- First, clone this repo (`PR-Docs`) to a suitable location on your computer. 
  - **Make note of the location you clone to.** 
  - For Windows, this tutorial assumes you use the default location of `C:\Users\<YourUsername>\Documents\GitHub`, but realistically you should use a different directory.
    - For the purposes of this tutorial, "directory" is essentially synonymous with "folder" that you may be used to.
    - `<YourUsername>` should be replaced with whatever your Windows username is.
- From here, all terminal commands should be ran inside WSL (or your terminal, for Linux and MacOS).
- On startup, your current working directory will likely be `~`, which is your 'home' directory.
  - You can view your current working directory at any time by using the command `pwd` (print working directory).
  - If on WSL, this is inside your Linux environment, which is effectively separate from the rest of your computer.
- A few things to note:
  1. You can view files and folders in the current directory using `ls`.
  2. `.` refers to the current directory (visible via `pwd`)
  3. `..` refers to the directory one level above (the directory containing the current directory).
- Change your current working directory to the location you cloned using `cd`. 
  - In WSL, you can do this with `cd /mnt/c/Users/<YourUsername>/Documents/GitHub`. Note that Linux filesystems use forward slashes, while Windows uses backslashes (but will generally convert forward slashes to backslashes).
  - On Linux or MacOS, you should be able to navigate to the target location from your home directory more easily.
- Once your current working directory is `PR-Docs`, you will be able to build the site by navigating to `./docs` and running `make html`.
  - You can also run `make.bat` from Windows Powershell from the same directory using `./make html`.
- You can edit the files in the directory normally with VS Code natively from your operating system, but you will need to build them using the terminal.

#### Launching Webserver
- In the root directory (`/`) run the following command:
```sh
python3 -m http.server
```

### Resources
- https://www.sphinx-doc.org/en/master/usage/markdown.html
- https://cerodell.github.io/sphinx-quickstart-guide/build/html/markdown.html
- https://myst-parser.readthedocs.io/en/latest/index.html
- https://docs.readthedocs.io/en/latest/tutorial/index.html
- https://www.writethedocs.org/guide/