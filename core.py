def create_inventory(inv_list):
    inventory_dictionary = {}
    for inventory in inv_list:
        items = inventor.split(',')
        key = items[0].strip()
        value = int(items[1].strip())
        inventory_dictionary[key] = value
    return inventory_dictionary


def make_inventory_string(inventory_dictionary):
    '''{str, int, int, int, number, int} -> str
    Returns the user_dictionary into a string.
    '''
    inventory_string = 'name, stock, price, replacement fee, sales tax, deposit'
    for name, stock, price, replacement_fee, sales_tax, deposit in inventory_dictionary.items(
    ):
        inventory_string += '\n{},{}, {}, {}, {}, {}'.format(
            name, stock, price, replacement_fee, sales_tax, deposit)
    return inventory_dictionaryrent():
    

