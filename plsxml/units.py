"""
===========================
Units (:mod:`plsxml.units`)
===========================

Summary
-------
The units module contains additional unit definitions to support unit conversion.

Custom Units
------------
The following custom units have been added to support PLS-CADD's unit names.

"""

import inspect
import astropy.units as u
from astropy.units.core import add_enabled_units
from astropy.units.utils import generate_unit_summary

_ns = globals()

u.def_unit(['Sec'], u.s, namespace = _ns, doc = 'Second.')
u.def_unit(['in'], u.imperial.inch, namespace = _ns, doc = 'Inch.')
u.def_unit(['lbs'], u.imperial.lbf, namespace = _ns, doc = 'Pound force.')
u.def_unit(['kips'], 1000 * u.imperial.lbf, namespace = _ns, doc = 'Kip force.')
u.def_unit(['plf'], u.imperial.lbf / u.imperial.ft, namespace = _ns, doc = 'Pound force per foot.')
u.def_unit(['psi'], u.imperial.lbf / u.imperial.inch**2, namespace = _ns, doc = 'Pound force per square inch.')
u.def_unit(['psf'], u.imperial.lbf / u.imperial.ft**2, namespace = _ns, doc = 'Pound force per square foot.')
u.def_unit(['pcf'], u.imperial.lbf / u.imperial.ft**3, namespace = _ns, doc = 'Pound force per cubic foot.')
u.def_unit(['ksi'], 1000*u.imperial.lbf / u.imperial.inch**2, namespace = _ns, doc = 'Kips per square inch.')

def _enable_units():
    """Enables custom units in Astropy."""
    u.imperial.enable()
    return add_enabled_units(inspect.getmodule(_enable_units))

_enable_units()
__doc__ += generate_unit_summary(globals())
