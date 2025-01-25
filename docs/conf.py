# Configuration file for the Sphinx documentation builder.

project = 'Three Level Programming – Documentation'
copyright = '2024, Raymond Hettinger'
author = 'Raymond Hettinger'

# Add any Sphinx extension module names here
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

# The master toctree document
master_doc = 'index'

# Theme settings
#html_theme = 'sphinx_rtd_theme'
html_theme = 'alabaster'
html_title = 'Three Level Programming – Documentation'
