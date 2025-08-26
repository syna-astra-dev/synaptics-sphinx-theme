from pathlib import Path
import os


# this code is used to substitute #xx# variables anywhere in the source, even
# inside literal blocks and code blocks

def preprocess_variables(app, docname, source):

    vars = dict(app.config.preprocessor_variables)
    vars["#release#"] = str(app.config.release)

    for varname, value in vars.items():
        source[0] = source[0].replace(varname, value)


# add extra configuration options to the app to make the theme work
def setup_config(app, config):

    branch_name = os.environ.get('GITHUB_REF', None)

    if os.environ.get('GITHUB_EVENT_NAME', None) == 'release':
        branch_name = None

    # we don't distinguish between versions and releases of the software
    app.config.version = app.config.release
    
    # add link to github if the branch information is available
    if branch_name is not None and app.config.github_repository is not None:
        app.config.html_context['display_github'] = True
        app.config.html_context['github_version'] = branch_name
        app.config.html_context['github_repo'] = app.config.github_repository
        app.config.html_context['conf_py_path'] = '/' # this is used to generate the github link

    # force the theme to be the synaptics theme
    app.config.html_theme = "synaptics_sphinx_theme"

    # setup breathe to use the doxygen XML output found in _build/doxygen/xml
    if os.path.exists('_build/doxygen/xml'):
        app.config.breathe_projects['default'] = '_build/doxygen/xml'
        app.config.breathe_default_project = 'default'

    # setup myst
    app.config.myst_enable_extensions.add("colon_fence")

def setup(app):

    # add common extensions for convenience
    app.setup_extension('sphinxcontrib.plantuml')
    app.setup_extension('breathe')
    app.setup_extension('myst_parser')

    # exclude README.rst from the build by default    
    app.config.exclude_patterns += ["README.rst", "README.md"]

    app.connect('config-inited', setup_config)

    # add support for pre-processing
    app.add_config_value('preprocessor_variables', {}, True)
    app.connect('source-read', preprocess_variables)    

    # add a custom config value to track the github repository of where the documentation is stored
    app.add_config_value('github_repository', os.environ.get('GITHUB_REPOSITORY', None), 'env')

    # register theme
    app.add_html_theme('synaptics_sphinx_theme', Path(__file__).resolve().parent)

    # add custom javascript
    app.add_js_file('js/synaptics.js')
