from setuptools import find_packages
from setuptools import setup

setup(
    name="Name Generator",
    version="0.0.1",
    author="Eduardo Olivares",
    url="https://github.com/skailer52/name-genertor",
    packages=find_packages(exclude=("tests")),
    install_requires=["requests==2.27.1"],
)
