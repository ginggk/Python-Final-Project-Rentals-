from core import *


def test_set_days():
    assert set_days(10, 5) == 50
    assert set_days(0, 0) == 0
