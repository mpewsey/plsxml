"""
Contains functions for returning built-in dataset information.

Functions
---------
.. autosummary::
    :toctree:

    data_names
    data_path
    load_data

Dataset Names
-------------
The following dataset names are available for use with the above functions:

=============   ============================================================
Name            Description
=============   ============================================================
galloping       An XML file containing data for a Galloping Ellipses Summary
                report.

galloping_zip   A ZIP file containing data for a Galloping Ellipses
                Summary report.
=============   ============================================================
"""

from .loader import *
