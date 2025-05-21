#!/bin/bash

set -e

mkdir -p _build

echo Building sphinx...

sphinx-build . _build/html

echo Updating permission of files...

chown -R $(stat -c '%u:%g' . ) _build

echo Done
