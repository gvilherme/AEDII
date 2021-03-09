"""AEDII setup.py"""

import re
from codecs import open
from os import path

from setuptools import find_packages, setup

PACKAGE_NAME = "AEDII"
HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, "README.md"), encoding="utf-8") as fp:
    README = fp.read()
with open(path.join(HERE, PACKAGE_NAME, "const.py"), encoding="utf-8") as fp:
    VERSION = re.search('__version__ = "([^"]+)"', fp.read()).group(1)

"""extras = {
    "ci": ["coveralls"],
    "dev": ["packaging", "pre-commit"],
    "lint": [
        "black",
        "docstrfmt",
        "flake8",
        "flynt",
        "isort",
        "pydocstyle",
        "sphinx",
        "sphinx_rtd_theme",
    ],
    "readthedocs": ["sphinx"],
    "test": [
        "betamax >=0.8, <0.9",
        "betamax-matchers >=0.3.0, <0.5",
        "pytest >=2.7.3",
    ],
}
extras["dev"] += extras["lint"] + extras["test"]"""

setup(
    name=PACKAGE_NAME,
    author="Guilherme Rodrigues",
    author_email="rodrigues.guilherme@aluno.ufabc.edu.br",
    python_requires="~=3.8.5",
    classifiers=[
        "Development Status :: 0 - Development/Unstable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Academic",
    ],
    description=(
        "AEDII, an acronym for `Algoritmos e Estruturas de Dados II`, is a python package that"
        " is being used on courses projects."
    ),    
    keywords="Academic project",
    license="GNU GENERAL PUBLIC LICENSE",
    long_description=README,
    #package_data={"": ["LICENSE.txt"], PACKAGE_NAME: ["*.ini", "images/*.jpg"]},
    packages=find_packages(exclude=["tests", "tests.*", "tools", "tools.*"]),
    project_urls={
        "Change Log": "readthedocs will be added soon",
        "Documentation": "readthedocs will be added soon",
        "Issue Tracker": "none for hour.",
        "Source Code": "https://github.com/gvilherme/AEDII",
    },
    version=VERSION,
)