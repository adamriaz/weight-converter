from setuptools import find_packages, setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

NAME = "weight-converter"
DESCRIPTION = "Module for converting weight units. "
VERSION = "0.0.2"
AUTHOR = "Adam Riaz"
AUTHOR_EMAIL = "riaz_adam@hotmail.com"
LONG_DESCRIPTION = long_description
URL = "https://github.com/adamriaz/weight-converter"

# Required packages
REQUIRED = []

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*", "dist", "*.egg-info"]),
    install_requires=REQUIRED,
    include_package_data=True,
    long_description_content_type="text/markdown",
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ]
)