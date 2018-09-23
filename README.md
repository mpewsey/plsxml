# PLSXML

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/plsxml.svg)
![PyPI](https://img.shields.io/pypi/v/plsxml.svg)
[![Build Status](https://travis-ci.com/line-mind/plsxml.svg?branch=master)](https://travis-ci.com/line-mind/plsxml)
[![Documentation Status](https://readthedocs.org/projects/plsxml/badge/?version=latest)](https://plsxml.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/line-mind/plsxml/branch/master/graph/badge.svg)](https://codecov.io/gh/line-mind/plsxml)


## Table of Contents

<!--
* [PLSXML](plsxml.rst)
* [Data](data.rst)-->
* [Example Usage](https://github.com/line-mind/plsxml/blob/master/example.ipynb)

## About

This package provides a class for parsing PLS-CADD XML files to `pandas` data frames for manipulation with Python.

## Installation

The package may be installed via pip:

```
pip install plsxml
```

## Usage

Once installed, data may be loaded from XML files or ZIP files containing XML simply by passing the XML and/or ZIP paths
to the `PLSXML` class.

```
from plsxml import PLSXML
paths = ['folder1/xml_file.xml', 'folder2/zip_file.zip']
plsxml = PLSXML(paths)
```

The data will be loaded into various `pandas.DataFrame` based on the XML file table names and assigned to the class.
For more detailed information, see the [example notebook](https://github.com/line-mind/plsxml/blob/master/example.ipynb).
