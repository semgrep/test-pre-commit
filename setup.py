# type: ignore
# Used for pre-commit since it expects a setup.py in repo root
# for actual setup.py see cli/setup.py
from setuptools import setup

setup(
    name="semgrep_pre_commit_package",
    version="1.800.588.2300",
    install_requires=["semgrep==1.800.588.2300"],
    packages=[],
)
