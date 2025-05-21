FROM sphinxdoc/sphinx:7.4.7

LABEL org.opencontainers.image.source="https://github.com/syna-astra-dev/synaptics-sphinx-theme"

COPY . /usr/local/share/synaptics-sphinx-theme

RUN pip install -e /usr/local/share/synaptics-sphinx-theme

ENTRYPOINT [ "/usr/local/share/synaptics-sphinx-theme/scripts/entrypoint.sh" ]
