"""
Summary
-------
The PLSXML module contains a class for parsing PLS-CADD XML files.

Classes
-------

"""

import os
import re
import ast
import zipfile
import pandas as pd
import xml.etree.cElementTree as et


class PLSXML(dict):
    """
    A class for parsing PLS-CADD XML files.

    Parameters
    ----------
    path : str or list, default is None
        A string or list of strings defining the ZIP or XML file path(s).
        If None, then no files will be loaded.
    tables : list, default is None
        A list of strings defining the table names to be loaded from the
        referenced XML files. If None, then all tables in the XML files
        will be parsed.
    verbose : bool, default is False
        If True, status messages will be printed during the parsing process.
        This can be useful to see the progress of long XML files.

    Examples
    --------
    >>> from plsxml import PLSXML
    >>> from plsxml.data import data_path

    To load data from the intializer:

    >>> path = data_path('galloping') # DATA_FOLDER/galloping.xml
    >>> xml = PLSXML(path)

    You can add files after the initialization via the `append` method:

    >>> xml.append(path)

    The class is a subclass of a dictionary. Once loaded, data can be accessed
    via table name > column name > row index:

    >>> xml['galloping_ellipses_summary']['minimum_clearance_galloping_ellipse_method'][0]
    'Single mid span'

    A summary of keys can be acquired via the `table_summary` method:

    >>> print(xml.table_summary())
    galloping_ellipses_summary
    	rowtext                                          None
    	structure                                        'TERM'
    	set                                              1
    	phase                                            1
    	ahead_span_length                                258.2
    	minimum_clearance_set                            1
    	minimum_clearance_phase                          2
    	minimum_clearance_galloping_ellipse_method       'Single mid span'
    	minimum_clearance_distance                       1.52
    	minimum_clearance_overlap                        0.0
    	minimum_clearance_wind_from                      'Left'
    	minimum_clearance_mid_span_sag                   12.15
    	minimum_clearance_insulator_swing_angle          0.0
    	minimum_clearance_span_swing_angle               63.1
    	minimum_clearance_major_axis_length              16.2
    	minimum_clearance_minor_axis_length              6.5
    	minimum_clearance_b_distance                     3.0

    """
    def __init__(self, path=None, tables=None, verbose=False):
        self.verbose = verbose

        if path is not None:
            if type(path) == str:
                path = [path]
            for x in path:
                self.append(x, tables)

    @staticmethod
    def _convert_type(data):
        """Converts data into appropriate type if it can."""
        try:
            return ast.literal_eval(data)
        except:
            return data

    @staticmethod
    def _is_xml(path):
        """Returns True if the input path is a valid XML file name."""
        fname, ext = os.path.splitext(path)

        # Valid extensions
        extensions = {'.xml'}

        # Regex expressions in fname to exclude
        regex = re.compile('__MACOSX|\.')

        return ext in extensions and not regex.search(fname)

    def append(self, path, tables=None):
        """
        Parses the input file into the class dictionary. If tables is None,
        all tables will be loaded. Otherwise, pass a list of the specific
        table names to be parsed.

        Parameters
        ----------
        path : str
            A string defining the XML file path.
        tables : list, default is None
            A list of strings defining the table names to be loaded from the
            referenced XML file. If None, then all tables in the XML file
            will be parsed.
        """
        if tables is not None:
            if type(tables) is str:
                tables = {tables}
            else:
                tables = set(tables)

        # Zipfile
        if zipfile.is_zipfile(path):
            with zipfile.ZipFile(path, 'r') as zf:
                for x in zf.namelist():
                    if self._is_xml(x):
                        with zf.open(x, 'r') as fh:
                            self._print('Parsing:', path, x)
                            self._load_xml(fh, tables)

        # XML
        elif os.path.isfile(path) and self._is_xml(path):
            with open(path, 'rb') as fh:
                self._print('Parsing:', path)
                self._load_xml(fh, tables)

        else:
            print('Append Skipped :: {!r} is not a valid path.'.format(path))


    def _load_xml(self, source, tables):
        """
        Loads the input file into the class dictionary. If tables is None,
        all tables will be loaded. Otherwise, pass a list of the specific
        table names to be parsed.

        Parameters
        ----------
        source : file handle
            A file handle for the XML file.
        tables : list, default is None
            A list of strings defining the table names to be loaded from the
            referenced XML file. If None, then all tables in the XML file
            will be parsed.
        """
        tablesdict = {}

        table = None
        obj = None
        titledetail = None

        for event, elem in et.iterparse(source, events=('start', 'end')):
            if event == 'start':
                if elem.tag == 'table':
                    if tables is None or elem.attrib['tagname'] in tables:
                        table = elem.attrib['tagname']
                        titledetail = elem.attrib['titledetail']
                        self._print('Loading:', table)

                        if table not in tablesdict:
                            tablesdict[table] = []

                elif table is not None and obj is None and elem.tag != 'source_file':
                    obj = elem.tag
                    odict = {}
                    if titledetail not in {None, ''}:
                        # Title details are included in some POLE and TOWER reports
                        odict['titledetail'] = self._convert_type(titledetail)

            elif event == 'end':
                if elem.tag == 'table':
                    table = None
                    obj = None
                    titledetail = None

                elif table is not None and elem.tag == obj:
                    tablesdict[table].append(odict)
                    obj = None

                elif obj is not None:
                    odict[elem.tag] = self._convert_type(elem.text)

                elem.clear()

        for k in list(tablesdict):
            d = tablesdict.pop(k)
            if k in self:
                self[k].append(d, sort=False)
                self._print('Dropping Duplicates:', k)
                self[k].drop_duplicates(inplace=True)
            else:
                self[k] = pd.DataFrame.from_dict(d)
                # Create new dataframe with columns in order.
                # Copy included to prevent possible view warnings during manipulation.
                self[k] = self[k][list(d[0])].copy()
            del d

    def _print(self, *args):
        """Prints the message if verbose is True."""
        if self.verbose:
            print(*args)

    def table_summary(self):
        """Returns a string of all parsed tables, keys, and example values."""
        summary = ''
        for table in sorted(self):
            summary += '\n{:s}\n'.format(table)
            for key in self[table]:
                v = self[table][key][0]
                summary += '\t{!s:60}\t{}\n'.format(key, v)
        return summary
