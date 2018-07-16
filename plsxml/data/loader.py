"""
The PLSXML data module contains sample and test data.
"""

import os
from ..plsxml import PLSXML

DATA_FOLDER = os.path.abspath(os.path.dirname(__file__))

METADATA = {
'galloping' :
    {'file' : 'galloping.xml',
     'tables' : None
    }
}

def data_names():
    """Returns a list of dataset names."""
    return sorted(METADATA.keys())


def data_path(name):
    """Returns the path for the dataset."""
    return os.path.join(DATA_FOLDER, METADATA[name]['file'])


def load_data(name):
    """Returns a PLSXML object for the dataset."""
    path = data_path(name)
    return PLSXML(path, METADATA[name]['tables'])
