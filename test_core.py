import core

from bcca.test import should_print


def test_set_days():
    assert core.set_days(10, 5) == 50
    assert core.set_days(0, 0) == 0


def test_sales_tax():
    assert round(core.sales_tax(50), 2) == round(3.5, 2)
    assert round(core.sales_tax(68.9), 2) == round(73.72300000000001 - 68.9, 2)
    assert round(core.sales_tax(core.set_days(10, 5)), 2) == round(
        53.5 - 50, 2)


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
    days = 1
    cost = core.set_days(inventory_dictionary[choice]['Price'], days)
    tax = core.sales_tax(cost)
    deposit = core.deposit(inventory_dictionary, choice)
    assert round(core.final_total(cost, tax, deposit), 2) == round(
        (40 + 2.8 + 2), 2)


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
    response = 'table'
    cost = inventory_dictionary[response]['Price']
    deposit = core.deposit(inventory_dictionary, response)
    sale = core.set_days(10, 5)
    tax = core.sales_tax(sale)
    total = core.final_total(inventory_dictionary[response]['Price'], tax,
                             deposit)

    assert core.make_book_sentence(inventory_dictionary, response, sale) == """
You have rented table for $40(12 in stock).
It will be $200 for 5 days.
With Sales Tax your total is: $14.000000000000002
Your deposit is: $4.5
Your Final total is: $58.5"""


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
    assert core.negative_deposit(inventory_dictionary,
                                 choice) == -2.3000000000000003


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
Replacement Fee: $4.5
Name of Book: James and the Giant Peach
Price: $40
Stock: 16
Replacement Fee: $2.3000000000000003"""


def test_deposit():
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

    response = 'chair'

    assert core.deposit(inventory_dictionary, response) == 2.3000000000000003


def test_history_string():

    title = 'Hairspray'
    type_of_sale = 'rent'
    money = 20.0

    assert core.history_string(title, type_of_sale,
                               money) == "Hairspray, rent, 20.0"
