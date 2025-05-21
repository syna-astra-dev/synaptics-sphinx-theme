#!/bin/bash

BASE_DIR=$(dirname $(readlink -f ${BASH_SOURCE[0]}))

cd ${BASE_DIR}

docker build -t ghcr.io/syna-astra-dev/synaptics-sphinx-theme/builder:latest .