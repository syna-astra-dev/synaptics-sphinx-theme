#!/bin/bash

set -e

mkdir -p _build

if [[ -f Doxyfile ]]; then
    echo Building doxygen...
    if [[ -f _build/doxygen/xml/index.xml ]]; then
        echo "Doxygen XML already exists. Skipping doxygen build."
    else
        doxygen Doxyfile
    fi    
else
    echo "Doxygen file not found. Skipping doxygen build."
fi

echo Building sphinx...

sphinx-build . _build/html

echo Updating permission of files...

chown -R $(stat -c '%u:%g' . ) _build

echo Done
