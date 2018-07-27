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


def update_stock(inventory_dictionary, item):
    """{number} -> number
    Returns the stock with one less of the item bought.
    """
    # for item in inventory_dictionary.keys():
    #     inventory_dictionary[item][stock] -= 1
    # return inventory_dictionary
    # print(inventory_dictionary[item])
    inventory_dictionary[item]['In Stock'] -= 1
    return inventory_dictionary


def make_inventory_string(inventory_dictionary):
    '''{str, int, float} -> str
    Returns the user_dictionary into a string.
    '''
    inventory_string = ''
    for key, value in inventory_dictionary.items():
        name = value['Name']
        stock = value['In Stock']
        price = value['Price']
        replacement_fee = value['Replacement Fee']
        inventory_string += '{},{}, {}, {}\n'.format(name, stock, price,
                                                     replacement_fee)
    return inventory_string


def not_in_stock(inventory_dictionary, item):
    """ {dict} -> bool
    Returns True iff the item stock is 0.
    """
    if inventory_dictionary[item]['In Stock'] <= 0:
        return True


def book_return(inventory_dictionary, item):
    """{number} -> number
    When a user returns a book, adds one to the stock.
    """
    inventory_dictionary[item]['In Stock'] += 1
    return inventory_dictionary
