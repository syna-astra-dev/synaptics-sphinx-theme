FROM sphinxdoc/sphinx:7.4.7

RUN apt-get update && apt-get install -y --no-install-recommends plantuml doxygen

LABEL org.opencontainers.image.source="https://github.com/syna-astra-dev/synaptics-sphinx-theme"

COPY . /usr/local/share/synaptics-sphinx-theme

RUN pip install -e /usr/local/share/synaptics-sphinx-theme

ENTRYPOINT [ "/usr/local/share/synaptics-sphinx-theme/scripts/entrypoint.sh" ]
