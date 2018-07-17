# PLSXML

[![Build Status](https://travis-ci.com/line-mind/plsxml.svg?branch=master)](https://travis-ci.com/line-mind/plsxml)
[![Documentation Status](https://readthedocs.org/projects/plsxml/badge/?version=latest)](https://plsxml.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/line-mind/plsxml/branch/master/graph/badge.svg)](https://codecov.io/gh/line-mind/plsxml)

## Contents

### API Contents

* [About](#about)
* [Installation](#installation)
* [Example Usage](#example-usage)

### Developer Contents

* [Deployment to PyPi](#deploying-to-pypi)
* [Local Testing](#local-testing)

### Module Contents

* [PLSXML](plsxml.rst)
* [Data Loader](data.rst)

## API Notes

### About

This package provides a class for parsing PLS-CADD XML files to dictionaries and `pandas` data frames. It is also capable of converting elements with 'units' attributes to `astropy` quantities, though currently this package may not be able to handle all units.

### Installation

This package may be installed via pip:

```
pip install plsxml
```

### Example Usage

See [example.ipynb](example.ipynb) for example usages of this package.

## Developer Notes

### Deployment to PyPi

To deploy a new release and issue to PyPi, add a version tag and push the
package with tags. This must occur on the master branch.

```
git tag -a #.#.# -m "version #.#.# release"
git push --tags
```

### Local Testing

Testing is performed using `pytest` and `pytest-cov`. To test the package locally,
run the following command from the root directory:

```
pytest --cov
```

To summarize testing coverage results in HTML, run:

```
coverage html
```
