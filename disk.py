import core


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
        inventory_string = core.make_inventory_string(inventory_dictionary)
        # file.write(up_stock)
        file.write(inventory_string)
        # file.close()
    # file.writeline


def write_to_history(total):
    # total = 0
    with open('history.txt', 'a') as file:
        file.write(str(total))
        file.write('\n')


def is_number(b):
    return b.count('.') < 2 and b.replace('.', '').isnumeric()


def get_total():
    with open('history.txt') as file:
        lines = file.readlines()
        # sales = []
        total = 0
        for line in lines:
            if line.strip():
                string_split = line.strip().split(',')
                number_line = string_split[-1].strip()

            if is_number(number_line):
                # print("WOO")
                total += float(number_line.strip())
        return total


# def receive_book(inventory_dictionary):
#     """{number} -> number
#     When a user returns a book, it also adds one negative number to the history.txt file.
#     """    return total
#     with open('history.txt', 'a') as file:

# def returnItem(book):
# """book = string of book title"""
# if book === "title1":
#     deposit = 5
# elif book === "title2":
#     deposit = 10
# elif book == "title2":
#     deposit = 15


def history():
    with open('history.txt') as file:
        history = file.read()
    print(history)
