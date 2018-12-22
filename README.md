# PLSXML

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/plsxml.svg)
![PyPI](https://img.shields.io/pypi/v/plsxml.svg)
[![Build Status](https://travis-ci.com/mpewsey/plsxml.svg?branch=master)](https://travis-ci.com/mpewsey/plsxml)
[![Documentation Status](https://readthedocs.org/projects/plsxml/badge/?version=latest)](https://plsxml.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/mpewsey/plsxml/branch/master/graph/badge.svg)](https://codecov.io/gh/mpewsey/plsxml)


## About

This package provides a class for parsing PLS-CADD XML files to `pandas`
data frames for manipulation with Python.

## Installation

The package may be installed via `pip` by running the below command:

```
pip install plsxml
```

## Usage

Once installed, data may be loaded from XML files or ZIP files containing XML
simply by passing the XML and/or ZIP paths to the `PLSXML` class.

```
from plsxml import PLSXML
paths = ['folder1/xml_file.xml', 'folder2/zip_file.zip']
plsxml = PLSXML(paths)
```

The data will be loaded into various `pandas.DataFrame` based on the XML file
table names and assigned to the class. For more detailed information, see the
[example notebook](https://github.com/mpewsey/plsxml/blob/master/example.ipynb).

## PLS-CADD XML Files

Most reports in the PLS-CADD suite can be exported to XML by right-clicking and
selecting the export to XML option. It is also possible to export an XML file
containing data for an entire line through the File menu. XML files for an
entire line can be large (several GB); therefore, archiving the resulting XML
to ZIP can greatly aid in transferring the file across systems and save disk
space if the file is more permanently retained. The PLSXML package is also able
to read data directly from ZIP files for this reason.
