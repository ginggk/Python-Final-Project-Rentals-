def create_inventory(inv_list):
    inventory_dictionary = {}
    for inventory in inv_list:
        items = inventor.split(',')
        key = items[0].strip()
        value = int(items[1].strip())
        inventory_dictionary[key] = value
    return inventory_dictionary


def rent():
    inventory = open('inventory.txt')
    for item_name in inventory:
        inventory
