#!/bin/sh
set -e

BIN_DIR=`dirname $0`
PROJECT_DIR="${BIN_DIR}"
export FREENIT_ENV="build"
. ${BIN_DIR}/common.sh


setup
pip install hatchling


rm -rf *.egg-info build dist
find . -name '*.pyc' -exec rm -rf {} \;
hatchling build
rm -f db.sqlite*
