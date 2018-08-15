import core

from bcca.test import should_print


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


def test_final_total():
    inventory_dictionary = {
        'table': {
            'Name': 'table',
            'In Stock': 12,
            'Price': 40,
            'color': 'black',
            'Replacement Fee': 20
        },
        'chair': {
            'Name': 'chair',
            'In Stock': 16,
            'Price': 40,
            'color': 'brown',
            'Replacement Fee': 35
        }
    }

    choice = 'table'

    assert core.final_total(inventory_dictionary, choice) == 234.0


def test_make_book_sentence():
    inventory_dictionary = {
        'table': {
            'Name': 'table',
            'In Stock': 12,
            'Price': 40,
            'color': 'black',
            'Replacement Fee': 45
        },
        'chair': {
            'Name': 'chair',
            'In Stock': 16,
            'Price': 40,
            'color': 'brown',
            'Replacement Fee': 23
        }
    }

    choice = 'table'

    assert core.make_book_sentence(
        inventory_dictionary,
        choice) == """You have rented table for $40(12 in stock).
It will be $200 for 5 days.
With Sales Tax your total is: $214.0
Your deposit is: $45
Your Final total is: $259.0"""


def test_negative_deposit():
    inventory_dictionary = {
        'table': {
            'Name': 'table',
            'In Stock': 12,
            'Price': 40,
            'color': 'black',
            'Replacement Fee': 45
        },
        'chair': {
            'Name': 'chair',
            'In Stock': 16,
            'Price': 40,
            'color': 'brown',
            'Replacement Fee': 23
        }
    }

    choice = 'chair'
    assert core.negative_deposit(inventory_dictionary, choice) == -23


@should_print
def test_printable_inventory(output):
    inventory_dictionary = {
        'table': {
            'Name': 'table',
            'In Stock': 12,
            'Price': 40,
            'color': 'black',
            'Replacement Fee': 45
        },
        'James and the Giant Peach': {
            'Name': 'James and the Giant Peach',
            'In Stock': 16,
            'Price': 40,
            'Replacement Fee': 23
        }
    }

    core.printable_inventory(inventory_dictionary)

    assert output == """
Name of Book: table
Price: $40
Stock: 12
Replacement Fee: $45
Name of Book: James and the Giant Peach
Price: $40
Stock: 16
Replacement Fee: $23"""
