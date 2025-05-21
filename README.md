# Synaptics Sphinx Theme

This is the Sphinx theme used by Synaptics documentation.

The repository contains a python package with a Sphinx extensions that provides the theme and 
some features used by documentation.

The repository also contains a Docker file that defines an image that can be used to build 
documentation using this theme.

## Usage

First add the following line to your documenation project `conf.py`.

```
extensions = [ 'synaptics_sphinx_theme' ]
```

Then build the project with the following docker command:

```
docker run --rm -v $(pwd):$(pwd) -w $(pwd) ghcr.io/syna-astra-dev/synaptics-sphinx-theme/builder:latest
```

## Development

To perform a local build of the theme docker file use the script `build.sh`.