"""
Summary
-------
The PLSXML data module contains methods for accessing sample and test data.

Global Variables
----------------
DATA_FOLDER
    The absolute path to the data directory.

Methods
-------

"""

import os
from ..plsxml import PLSXML

DATA_FOLDER = os.path.dirname(os.path.abspath(__file__))

_METADATA = {
'galloping':
    {'file': 'galloping.xml',
     'tables': None
    },
'galloping_zip':
    {'file': 'galloping.zip',
     'tables': None
    }
}

def data_names():
    """Returns a list of dataset names."""
    return sorted(_METADATA.keys())


def data_path(name):
    """Returns the path for the dataset."""
    return os.path.join(DATA_FOLDER, _METADATA[name]['file'])


def load_data(name):
    """Returns a PLSXML object for the dataset."""
    path = data_path(name)
    return PLSXML(path, _METADATA[name]['tables'])
