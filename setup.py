from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sparrowone",
    version="0.0.1",
    description="Python client for Sparrow payment gateway",
    long_description=long_description,
    url="https://github.com/SparrowDevelopment/sparrow-api-python",
    author="Sparrow One",
    author_email="info@sparrowone.com",
    license="MIT",
    install_requires=[
        "requests >= 2.0"
    ],
    packages=["sparrowone"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: API",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
