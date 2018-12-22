import os
from ..plsxml import PLSXML

__all__ = ['data_names', 'data_path', 'load_data']


DATA_FOLDER = os.path.dirname(os.path.abspath(__file__))


METADATA = dict(
    galloping=dict(
        file='galloping.xml',
        tables=None
    ),
    galloping_zip=dict(
        file='galloping.zip',
        tables=None
    )
)


def data_names():
    """
    Returns a list of built-in dataset names.
    """
    return sorted(METADATA.keys())


def data_path(name):
    """
    Returns the path for the built-in dataset.

    Parameters
    ----------
    name : str
        The name of the dataset.
    """
    return os.path.join(DATA_FOLDER, METADATA[name]['file'])


def load_data(name):
    """
    Returns a PLSXML object for the built-in dataset.

    Parameters
    ----------
    name : str
        The name of the dataset.
    """
    path = data_path(name)
    return PLSXML(path, METADATA[name]['tables'])
