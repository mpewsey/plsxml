====================
PLSXML Documentation
====================

.. image:: https://img.shields.io/pypi/pyversions/plsxml.svg
    :target: #

.. image:: https://img.shields.io/pypi/v/plsxml.svg
    :target: #

.. image:: https://travis-ci.com/mpewsey/plsxml.svg?branch=master
    :target: https://travis-ci.com/mpewsey/plsxml

.. image:: https://readthedocs.org/projects/plsxml/badge/?version=latest
    :target: https://plsxml.readthedocs.io/en/latest/?badge=latest

.. image:: https://codecov.io/gh/mpewsey/plsxml/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/mpewsey/plsxml

About
=====
The PLSXML package provides a class for parsing PLS-CADD XML files to
:class:`pandas.DataFrame` for manipulation with Python.


Installation
============
The package may be installed via `pip` by running the below command:

.. code-block:: none

    pip install plxsml


Usage
=====
Once installed, data may be loaded from XML files or ZIP files containing XML
simply by passing the XML and/or ZIP paths to the :class:`.PLSXML` class.

.. code-block:: python

    from plsxml import PLSXML
    paths = ['folder1/xml_file.xml', 'folder2/zip_file.zip']
    plsxml = PLSXML(paths)

The data will be loaded into various :class:`pandas.DataFrame` based on the XML
file table names and assigned to the class. For more detailed information, see
the `example notebook <https://github.com/mpewsey/plsxml/blob/master/example.ipynb>`_.


PLS-CADD XML Files
==================
Most reports in the PLS-CADD suite can be exported to XML by right-clicking and
selecting the export to XML option. It is also possible to export an XML file
containing data for an entire line through the File menu. XML files for an
entire line can be large (several GB); therefore, archiving the resulting XML
to ZIP can greatly aid in transferring the file across systems and save disk
space if the file is more permanently retained. The PLSXML package is also able
to read data directly from ZIP files for this reason.


API Documentation
=================
.. toctree::
    :maxdepth: 1

    plsxml
