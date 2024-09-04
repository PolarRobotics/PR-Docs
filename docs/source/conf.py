# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PR-Docs'
copyright = '2024, Polar Robotics Documentation Team'
author = 'Polar Robotics Documentation Team'
release = '0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx_rtd_theme', 'myst_parser', 'notfound.extension'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'Polar Robotics Documentation'
#html_theme = "sphinx_rtd_theme" # Default ReadTheDocs Theme
html_theme = "sphinx_book_theme" # MyST Theme (https://sphinx-book-theme.readthedocs.io/en/stable/tutorials/get-started.html)
html_static_path = ['_static']
html_css_files = ['css/custom.css']
#html_logo = "_static/images/polar_robotics_logo_t.png"

# https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/branding.html
html_theme_options = {
   "logo": {
      "image_light": "_static/images/polar_robotics_logo_t_light.png",
      "image_dark": "_static/images/polar_robotics_logo_t.png"
   }
}

# -- MyST-Parser Specific Options
myst_enable_extensions = ["colon_fence", "attrs_inline"]