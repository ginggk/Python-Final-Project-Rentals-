from core import *


def test_set_days():
    assert set_days(10, 5) == 50
    assert set_days(0, 0) == 0


def test_sales_tax():
    assert sales_tax(50) == 53.5
    assert sales_tax(68.9) == 73.72300000000001
    assert sales_tax(set_days(10, 5)) == 53.5
