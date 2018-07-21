# PLSXML

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/plsxml.svg)
![PyPI](https://img.shields.io/pypi/v/plsxml.svg)
[![Build Status](https://travis-ci.com/line-mind/plsxml.svg?branch=master)](https://travis-ci.com/line-mind/plsxml)
[![Documentation Status](https://readthedocs.org/projects/plsxml/badge/?version=latest)](https://plsxml.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/line-mind/plsxml/branch/master/graph/badge.svg)](https://codecov.io/gh/line-mind/plsxml)


## Table of Contents

* [PLSXML](plsxml.rst)
* [Data](data.rst)

## About

This package provides a class for parsing PLS-CADD XML files to dictionaries and `pandas` data frames. It is also capable of converting elements with 'units' attributes to `astropy` quantities, though currently this package may not be able to handle all units.

## Installation

This package may be installed via pip:

```
pip install plsxml
```

## Example Usage

See [example.ipynb](https://github.com/line-mind/plsxml/blob/master/example.ipynb) for example usages of this package.

## Local Testing

Testing is performed using `pytest` and `pytest-cov`. To test the package locally,
run the following command from the root directory:

```
pytest --cov
```

To summarize testing coverage results in HTML, run:

```
coverage html
```
