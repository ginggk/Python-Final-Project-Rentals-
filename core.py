def set_days(price, days):
    '''float -> float
    Returns the price for a given number of days, given the price.
    '''
    return days * price


def sales_tax(total):
    """number -> float
    Returns the total with the sales tax added to it.
    """
    return total * 1.07


def check_stock(inventory_dictionary, item):
    """{number} -> number
    Returns the stock with one less of the item bought.
    """
    for item in inventory_dictionary.keys():
        inventory_dictionary[0] -= 1
    return inventory_dictionary

    # inventory_dictionary[item] -= stock


def make_inventory_string(inventory_dictionary):
    '''{str, int, float} -> str
    Returns the user_dictionary into a string.
    '''
    inventory_string = ''
    for key, value in inventory_dictionary.items():
        name = key[1]
        stock = key[2]
        price = key[3]
        replacement_fee = key[4]
        inventory_string += '{},{}, {}, {}\n'.format(name, stock, price,
                                                     replacement_fee)
    return inventory_string
