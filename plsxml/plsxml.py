"""
The PLSXML module contains a class for parsing PLS-CADD XML files.
"""

import ast
from collections import OrderedDict
import xml.etree.ElementTree as et
import pandas as pd
import astropy.units as u
u.imperial.enable()


class PLSXML(OrderedDict):
    """
    A class for parsing PLS-CADD XML files. Data can be accessed using
    via table name -> row index -> column name. Example:

    .. code::

        PLSXML['galloping_ellipses_summary'][0]['phase']


    Parameters:
        source : str or list
            A string or list of strings defining the XML file path(s).
            If None, then no tables will be parsed.
        tables : list
            A list of strings defining the table names to be loaded from the
            referenced XML files. If None, then all tables in the XML files
            will be parsed.
        parse_units : bool
            If True, elements with the 'units' attribute will attempt to be
            converted to Astropy quantities. This operation takes longer so could
            be disabled if including units is unimportant to you.
        print_statuses : bool
            If True, status messages will be printed during the parsing process.
            This can be useful to see the progress of long XML files.
    """
    def __init__(self, source = None, tables = None, parse_units = False, print_statuses = False):
        self.parse_units = parse_units
        self.print_statuses = print_statuses

        if source != None:
            if type(source) == str:
                source = [source]
            for x in source:
                self.append(x, tables)

    def drop_duplicates(self, data):
        """Drops duplicates from list of dictionaries in place."""
        oset = set()
        drop_indices = []

        for i, x in enumerate(data):
            h = hash(tuple(x.items()))
            if h not in oset:
                oset.add(h)
            else:
                drop_indices.append(i)

        for i in reversed(drop_indices):
            del data[i]

    def convert_type(self, data):
        """Converts data into appropriate type if it can."""
        try:
            return ast.literal_eval(data)
        except:
            return data

    def clean_unit(self, unit):
        """Attemps to replace characters and units that astrpoy cannot understand."""
        repl = {
            '-' : ' ',
            'psi' : '(lbf / inch^2)',
            'ksi' : '(1000 lbf / inch^2)',
            'lbs' : 'lbf',
            'deg F' : 'deg_F',
            'Sec' : 's'
        }

        for x, y in repl.items():
            unit = unit.replace(x, y)
        return unit

    def append(self, source, tables = None):
        """
        Parses the input file into a dictionary. If tables is None,
        all tables will be loaded. Otherwise, pass a list of the specific
        table names to be parsed.

        Parameters:
            source : str
                A string defining the XML file path.
            tables: list
                A list of strings defining the table names to be loaded from the
                referenced XML file. If None, then all tables in the XML file
                will be parsed.
        """
        self.print('Parsing:', source)
        messages = set()
        exist_tables = set(self.keys())
        new_tables = set()

        if tables != None:
            if type(tables) == str:
                tables = {tables}
            else:
                tables = set(tables)

        table = None
        obj = None
        titledetail = None

        for event, elem in et.iterparse(source, events = ('start', 'end')):
            if event == 'start':
                if elem.tag == 'table':
                    if tables is None or elem.attrib['tagname'] in tables:
                        table = elem.attrib['tagname']
                        titledetail = elem.attrib['titledetail']
                        new_tables.add(table)
                        self.print('Loading:', table)
                        if table not in self.keys():
                            self[table] = []

                elif table is not None and obj is None and elem.tag != 'source_file':
                    obj = elem.tag
                    odict = OrderedDict()
                    if titledetail not in (None, ''):
                        odict['titledetail'] = self.convert_type(titledetail)

            elif event == 'end':
                if elem.tag == 'table':
                    table = None
                    obj = None
                    titledetail = None

                elif table != None and elem.tag == obj:
                    self[table].append(odict)
                    obj = None

                elif obj != None:
                    v = self.convert_type(elem.text)
                    if self.parse_units and type(v) != str and 'units' in elem.attrib:
                        try:
                            unit = self.clean_unit(elem.attrib['units'])
                            v *= u.Unit(unit)
                        except:
                            messages.add('Unit {!r} could not be parsed.'.format(elem.attrib['units']))
                    odict[elem.tag] = v

                elem.clear()

        new_tables &= exist_tables

        for key in new_tables:
            self.print('Dropping Duplicates:', key)
            self.drop_duplicates(self[key])

        if messages:
            print('\n'.join(messages))

    def print(self, *args):
        """Prints the message if print_statuses is True."""
        if self.print_statuses:
            print(*args)

    def table_summary(self):
        """Returns a string of all parsed tables, keys, and example values."""
        keys = ''
        for table in sorted(self.keys()):
            keys += '\n{:s}\n'.format(table)
            if self[table]:
                for key in self[table][0].keys():
                    v = self[table][0][key]
                    s = '\t{!s:60}\t{!r}\n' if type(v) == str else '\t{!s:60}\t{}\n'
                    keys += s.format(key, v)
        return keys

    def dataframes(self, tables = None):
        """
        Returns a dictionary of dataframes for the parsed tables specified.

        Parameters:
            tables : list
                A list of strings defining the table names for which dataframes
                will be created. If None, then all tables parsed in the object
                will be converted.
        """
        d = OrderedDict()

        if tables is None:
            tables = self.keys()

        for table in tables:
            if self[table]:
                d[table] = pd.DataFrame.from_dict(self[table], dtype = 'object')
        return d
