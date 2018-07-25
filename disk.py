import core


def create_inventory(inv_list):
    inventory_dictionary = {}
    for inventory in inv_list:
        items = inventory.split(',')
        name = items[0].strip()
        stock = int(items[1].strip())
        price = float(items[2].strip())
        replacement_fee = int(items[3].strip())
        sales_tax = float(items[4].strip())
        deposit = float(items[5].strip())
        # inv_list = []
        inventory_dictionary[name] = {
            'Name': name,
            'In Stock': stock,
            'Price': price,
            'Replacement Fee': replacement_fee,
            'Sales Tax': sales_tax,
            'Deposit': deposit
        }
        # inv_list.append(name, stock, price, replacement_fee, sales_tax,
        # deposit)
    return inventory_dictionary


# def make_inventory_string(inventory_dictionary):
#     '''{str, int, int, int, number, int} -> str
#     Returns the user_dictionary into a string.
#     '''
#     inventory_string = 'name, stock, price, replacement fee, sales tax, deposit'
#     for name, stock, price, replacement_fee, sales_tax, deposit in inventory_dictionary.items(
#     ):
#         inventory_string += '\n{},{}, {}, {}, {}, {}'.format(
#             name, stock, price, replacement_fee, sales_tax, deposit)
#     return inventory_dictionary


def open_inventory():
    with open('inventory.txt', 'r') as file:
        # file.readline()
        new_file_info = file.readlines()
    return new_file_info
