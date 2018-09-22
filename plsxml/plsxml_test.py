from pytest import approx
from .data import data_path, data_names, load_data
from .plsxml import PLSXML


def test_init():
    path = data_path('galloping')
    xml = PLSXML(path)
    assert len(xml.keys()) > 0


def test_append():
    path = data_path('galloping')
    xml = PLSXML()
    xml.append(path)
    assert len(xml.keys()) > 0


def test_append_multiple():
    path = data_path('galloping')
    xml = PLSXML([path, path])
    assert len(xml.keys()) > 0


def test_append_bad_path():
    path = 'bad_file_name.docx'
    xml = PLSXML(path)
    assert len(xml.keys()) == 0


def test_tables_none():
    path = data_path('galloping')
    xml = PLSXML(path, tables='')
    assert len(xml.keys()) == 0


def test_tables_specific():
    path = data_path('galloping')
    xml = PLSXML(path, tables='galloping_ellipses_summary')
    assert len(xml.keys()) == 1


def test_table_summary():
    path = data_path('galloping')
    xml = PLSXML(path)
    print(xml.table_summary())


def test_verbose():
    path = data_path('galloping')
    xml = PLSXML(path, verbose=True)


def test_load_data():
    for x in data_names():
        xml = load_data(x)
