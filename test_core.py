from core import *

# from bcca.test import fake_file, should_print


def test_set_days():
    assert set_days(10, 5) == 50
    assert set_days(0, 0) == 0


def test_sales_tax():
    assert sales_tax(50) == 53.5
    assert sales_tax(68.9) == 73.72300000000001
    assert sales_tax(set_days(10, 5)) == 53.5


# def test_check_stock():
#     inventory_dictionary = {
#         'table': {
#             'name': 'table',
#             'stock': 12,
#             'price': 40,
#         },
#         'chair': {
#             'name': 'chair',
#             'stock': 12,
#             'price': 40,
#         }
#     }

#     item = 'chair'

#     # stock = inventory_dictionary['chair']['stock']

#     check_stock(inventory_dictionary, item)

#     assert {
#         'table': {
#             'name': 'table',
#             'stock': 12,
#             'price': 40,
#         },
#         'chair': {
#             'name': 'chair',
#             'stock': 11,
#             'price': 40,
#         }
#     } == inventory_dictionary


def test_make_inventory_string():

    inventory_dictionary = {
        'table': {
            'name': 'table',
            'stock': 12,
            'price': 40,
            'color': 'black'
        },
        'chair': {
            'name': 'chair',
            'stock': 12,
            'price': 40,
            'color': 'brown'
        }
    }

    make_inventory_string(inventory_dictionary)

    assert 'Chair, 12, 40'
