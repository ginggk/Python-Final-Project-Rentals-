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


def check_stock(inventory_dictionary, item):
    """ {dict} -> bool
    Returns True iff the item is not in stock.
    """
    if inventory_dictionary[item]['In Stock'] == 0:
        return True


def book_return(inventory_dictionary, item):
    """{number} -> number
    When a user returns a book, adds one to the stock.
    """
    inventory_dictionary[item]['In Stock'] += 1
    return inventory_dictionary


def final_total(inventory_dictionary, choice):
    """{number, number, number, number} -> number
    Returns the final total with the given numbers together.
    """
    return sales_tax(
        set_days(inventory_dictionary[choice]['Price'],
                 5)) + inventory_dictionary[choice]['Replacement Fee']


def make_book_sentence(inventory_dictionary, choice):
    return 'You have rented {} for ${}({} in stock).\nIt will be ${} for 5 days.\nWith Sales Tax your total is: ${}\nYour deposit is: ${}\nYour Final total is: ${}'.format(
        inventory_dictionary[choice]['Name'],
        inventory_dictionary[choice]['Price'],
        inventory_dictionary[choice]['In Stock'],
        set_days(inventory_dictionary[choice]['Price'], 5),
        sales_tax(set_days(inventory_dictionary[choice]['Price'], 5)),
        inventory_dictionary[choice]['Replacement Fee'],
        final_total(inventory_dictionary, choice))
    #     for choice in enumerate(inventory_dictionary.values())
    # ])


def negative_deposit(inventory_dictionary, choice):
    return -inventory_dictionary[choice]['Replacement Fee']


def printable_inventory(inventory_dictionary):
    for key in inventory_dictionary:
        print('Name of Book: {}\nPrice: ${}\nStock: {}\nReplacement Fee: ${}'.
              format(inventory_dictionary[key]['Name'],
                     inventory_dictionary[key]['Price'],
                     inventory_dictionary[key]['In Stock'],
                     inventory_dictionary[key]['Replacement Fee']))
