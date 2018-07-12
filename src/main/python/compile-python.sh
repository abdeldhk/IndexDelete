!/usr/bin/env bash

echo "Current folder : `pwd`"
echo "Working folder : $1"
TARGET=$1
PIP_REPOSITORY=https://repository.rnd.amadeus.net/repository/api/pypi/pypi/simple

# Remove virtual env and output folder
rm -rf ${TARGET}/v_env dist

# Start virtual environment
virtualenv ${TARGET}/v_env
source ${TARGET}/v_env/bin/activate

# Install installers
pip install --index-url=${PIP_REPOSITORY} --upgrade pip
pip install --index-url=${PIP_REPOSITORY} pyinstaller
easy_install --index-url=${PIP_REPOSITORY} distribute
pip install --index-url=${PIP_REPOSITORY} --upgrade distribute
pip install --index-url=${PIP_REPOSITORY} elasticsearch
# Install whole module
pip install --index-url=${PIP_REPOSITORY} -e .

python ${TARGET}/v_env/bin/pyinstaller DeleteIndexElastic.py --onefile --distpath ${TARGET}/dist --workpath ${TARGET}/build -n indexDelete.elf

# Purge working directories
deactivate
rm -rf ${TARGET}/build
rm -rf *.egg-info
rm -f *.spec
