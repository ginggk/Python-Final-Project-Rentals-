from core import *

# from bcca.test import fake_file, should_print


def test_set_days():
    assert set_days(10, 5) == 50
    assert set_days(0, 0) == 0


def test_sales_tax():
    assert sales_tax(50) == 53.5
    assert sales_tax(68.9) == 73.72300000000001
    assert sales_tax(set_days(10, 5)) == 53.5


def test_check_stock():
    inventory_dictionary = {
        'table': {
            'name': 'table',
            'In Stock': 12,
            'price': 40,
        },
        'chair': {
            'name': 'chair',
            'In Stock': 12,
            'price': 40,
        }
    }

    item = 'chair'

    # In Stock = inventory_dictionary['chair']['In Stock']

    update_stock(inventory_dictionary, item)

    assert {
        'table': {
            'name': 'table',
            'In Stock': 12,
            'price': 40,
        },
        'chair': {
            'name': 'chair',
            'In Stock': 11,
            'price': 40,
        }
    } == inventory_dictionary


def test_make_inventory_string():

    inventory_dictionary = {
        'table': {
            'Name': 'table',
            'In Stock': 12,
            'Price': 40,
            'Replacement Fee': '60'
        },
        'chair': {
            'Name': 'chair',
            'In Stock': 12,
            'Price': 40,
            'Replacement Fee': '50'
        }
    }

    make_inventory_string(inventory_dictionary)

    assert 'chair, 12, 40, 50'


def test_not_in_stock():
    inventory_dictionary = {
        'table': {
            'name': 'table',
            'In Stock': 12,
            'price': 40,
            'color': 'black'
        },
        'chair': {
            'name': 'chair',
            'In Stock': 0,
            'price': 40,
            'color': 'brown'
        }
    }

    item = 'chair'

    assert not_in_stock(inventory_dictionary, item)

    inventory_dictionary = {
        'table': {
            'name': 'table',
            'In Stock': 12,
            'price': 40,
            'color': 'black'
        },
        'chair': {
            'name': 'chair',
            'In Stock': 15,
            'price': 40,
            'color': 'brown'
        }
    }

    item = 'table'

    assert not not_in_stock(inventory_dictionary, item)
