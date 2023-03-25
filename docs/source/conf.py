# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Essential MySQL'
copyright = '2023, LL'
author = 'LL'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "lacus-w", # Username
    "github_repo": "Essential-MySQL", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/docs/source/", # Path in the checkout to the docs root
}
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- For Chinese projects
latex_engine = "xelatex"
latex_use_xindy = False
latex_elements = {
    "preamble": "\\usepackage[UTF8]{ctex}\n",
}
