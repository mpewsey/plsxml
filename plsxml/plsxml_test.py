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


def test_tables_all():
    path = data_path('galloping')
    xml = PLSXML(path, tables = '')
    assert len(xml.keys()) == 0


def test_tables_specific():
    path = data_path('galloping')
    xml = PLSXML(path, tables = 'galloping_ellipses_summary')
    assert len(xml.keys()) == 1


def test_table_summary():
    path = data_path('galloping')
    xml = PLSXML(path)
    print(xml.table_summary())


def test_dataframes():
    path = data_path('galloping')
    xml = PLSXML(path)
    print(xml.dataframes())


def test_drop_duplicates():
    n, m = [], []
    path = data_path('galloping')
    xml1 = PLSXML(path)
    xml2 = PLSXML(path)
    xml2.append(path)

    for k in xml1.keys():
        n.append(len(xml1[k]))
        m.append(len(xml2[k]))

    assert approx(n) == m


def test_print_statuses():
    path = data_path('galloping')
    xml = PLSXML(path, print_statuses = True)


def test_load_data():
    for x in data_names():
        xml = load_data(x)
