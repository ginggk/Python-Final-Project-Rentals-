import core

# from bcca.test import fake_file, should_print


def test_set_days():
    assert core.set_days(10, 5) == 50
    assert core.set_days(0, 0) == 0


def test_sales_tax():
    assert core.sales_tax(50) == 53.5
    assert core.sales_tax(68.9) == 73.72300000000001
    assert core.sales_tax(core.set_days(10, 5)) == 53.5


def test_update_stock():
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

    core.update_stock(inventory_dictionary, item)

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

    core.make_inventory_string(inventory_dictionary)

    assert 'chair, 12, 40, 50'


def test_check_stock():
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

    assert core.check_stock(inventory_dictionary, item)

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

    assert not core.check_stock(inventory_dictionary, item)


def test_book_return():
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

    item = 'chair'

    assert core.book_return(inventory_dictionary, item)

    inventory_dictionary = {
        'table': {
            'name': 'table',
            'In Stock': 12,
            'price': 40,
            'color': 'black'
        },
        'chair': {
            'name': 'chair',
            'In Stock': 16,
            'price': 40,
            'color': 'brown'
        }
    }
