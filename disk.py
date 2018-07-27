from core import *


def create_inventory(inv_list):
    inventory_dictionary = {}
    for inventory in inv_list:
        items = inventory.split(',')
        name = items[0].strip()
        stock = int(items[1].strip())
        price = float(items[2].strip())
        replacement_fee = int(items[3].strip())
        # sales_tax = float(items[4].strip())
        # deposit = float(items[5].strip())
        # inv_list = []
        inventory_dictionary[name] = {
            'Name': name,
            'In Stock': stock,
            'Price': price,
            'Replacement Fee': replacement_fee
            # 'Sales Tax': sales_tax,
            # 'Deposit': deposit
        }
        # inv_list.append(name, stock, price, replacement_fee, sales_tax,
        # deposit)
    return inventory_dictionary


def open_inventory():
    with open('inventory.txt', 'r') as file:
        # file.readline()
        new_file_info = file.readlines()
    return new_file_info


def write_to_inventory(inventory_dictionary):
    # inventory_information = open_inventory()
    # inventory_dictionary = create_inventory(inventory_information)
    with open('inventory.txt', 'w') as file:
        # file.readline(4)
        # up_stock = update_stock(inventory_dictionary, 'In St')
        inventory_string = make_inventory_string(inventory_dictionary)
        # file.write(up_stock)
        file.write(inventory_string)
        # file.close()
    # file.writeline


def write_to_history(total):
    # total = 0
    with open('history.txt', 'a') as file:
        file.write(str(total))
        file.write('\n')


def get_total():
    with open('history.txt') as file:
        total = 0
        for line in file:
            total += float(line.strip())
    return total
