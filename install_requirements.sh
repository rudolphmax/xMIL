#!/usr/bin/env bash


# openslide via conda
conda install openslide -c conda-forge

# nvcc for mamba-ssm
conda install cuda -c nvidia

# torch and torchvision with cuda
pip install --root-user-action=ignore torch==2.0.1+cu118 torchvision==0.15.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118

# torch==2.0.1's build utilities still require pkg_resources
pip install --root-user-action=ignore "setuptools<81"

# regular pip requirements
pip install --root-user-action=ignore --no-build-isolation -r pip_requirements.txt

# Claude (2026-09-21): CUDA-only mamba extra, split out of pip_requirements.txt
# so the package installs on machines without nvcc. Needs the conda cuda
# install above.
pip install --root-user-action=ignore --no-build-isolation -r pip_requirements_mamba.txt

# install xMIL from the local checkout
pip install --root-user-action=ignore --no-deps -e .
