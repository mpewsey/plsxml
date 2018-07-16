# PLSXML

[![Build Status](https://travis-ci.com/line-mind/plsxml.svg?branch=master)](https://travis-ci.com/line-mind/plsxml)
[![Documentation Status](https://readthedocs.org/projects/plsxml/badge/?version=latest)](https://plsxml.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/line-mind/plsxml/branch/master/graph/badge.svg)](https://codecov.io/gh/line-mind/plsxml)

## API Contents

* [About](#about)
* [Installation](#installation)
* [Example Usage](#example-usage)

## Module Contents

* [PLSXML](plsxml.rst)
* [Data Loader](data.rst)

## About

This package provides a class for parsing PLS-CADD XML files to dictionaries and `pandas` dataframes. It is also capable of converting elements with 'units' attributes to `astropy` quantities, though currently this package may not be able to handle all units.

## Installation

This package may be installed via pip:

```
pip install git+https://github.com/line-mind/plsxml#egg=plsxml
```

## Example Usage

See [example.ipynb](example.ipynb) for example usages of this package.
