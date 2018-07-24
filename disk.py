import core


def open_file():
    with open('inventory.txt', 'r') as file:
        return file.readlines()
