import core
import disk


def welcome():
    print("Welcome to GB's Book Rental Store!!")


def user_employee():
    while True:
        comment = input(
            "Are you a [1]employee or a [2]customer?(if you would like to quit, please type (q).\n"
        ).strip().lower()
        if comment == 'customer' or comment == '2':
            user()
        elif comment == 'employee' or comment == '1':
            employee()
        elif comment == 'q' or comment == 'quit':
            break
        else:
            print(
                "Invalid choice! Please tell us if you are a customer or a trusted employee!"
            )


# def make_inventory():
# inventory = open_inventory()
# return inventory


def bring_back():
    inventory_information = disk.open_inventory()
    inventory_dictionary = disk.create_inventory(inventory_information)
    while True:
        print('-------------------------------------------------')
        core.printable_inventory(inventory_dictionary)
        print("------------------------------------------------")
        back = input(
            "Which of these books would you like to return today?").strip()
        if back in inventory_dictionary:
            core.book_return(inventory_dictionary, back)
            disk.write_to_inventory(inventory_dictionary)
            disk.write_to_history(
                core.negative_dep(inventory_dictionary, back))
            print("Here is your deposit...")
            print("Thank you for reading one of our books!")
            break
        else:
            print("That is not one of our book, try again please.")


def user():
    inventory_information = disk.open_inventory()
    inventory_dictionary = disk.create_inventory(inventory_information)
    while True:
        while True:
            print('--------------------------------------------------')
            keep = input(
                "Would you like to return or rent a book today?\n(if you would like to go back, type(b)\n"
            ).strip().lower()
            if keep == 'return':
                bring_back()
            elif keep == 'b' or keep == 'back':
                return
            else:
                break
        while True:
            print('-------------------------------------------------')
            core.printable_inventory(inventory_dictionary)
            print("------------------------------------------------")
            response = input(
                " What book would you like to rent today?\n (type [d]one when you are finished shopping)\n"
            ).strip()
            if response in inventory_dictionary:
                if core.check_stock(inventory_dictionary, response) == True:
                    print(
                        "Sorry! That book is out of stock, please choose another one of our quality books!"
                    )
                else:
                    print("-----------------------------------")
                    print(
                        core.make_book_sentence(inventory_dictionary,
                                                response))
                    core.update_stock(inventory_dictionary, response)
                    disk.write_to_inventory(inventory_dictionary)
                    disk.write_to_history(
                        inventory_dictionary[response]['Replacement Fee'])
            else:
                print(
                    "We are sorry, we do not have that book. Please choose a provided book."
                )


def employee():
    inventory_information = disk.open_inventory()
    inventory_dictionary = disk.create_inventory(inventory_information)
    while True:
        choice = input(
            "Would you like to see what is in [s]tock, transaction [h]istory, or calculate the [t]otal revenue?\n (type [d]one when finished.) \n"
        ).strip().lower()
        if choice == 's' or choice == 'in stock':
            print(core.make_inventory_string(inventory_dictionary))
        elif choice == 'h' or choice == 'history':
            disk.history()
        elif choice == 't' or choice == 'total revenue':
            print('Total Revenue: ${}.'.format(disk.get_total()))
        elif choice == 'done' or choice == 'd':
            break
        else:
            print(
                "That is not a valid response, please put in a valid choice!")


def main():
    welcome()
    inventory_information = disk.open_inventory()
    inventory_dictionary = disk.create_inventory(inventory_information)
    user_employee()
    # make_inventory()
    # inventory_information = open_inventory()
    # inventory_dictionary = disk.create_inventory(inventory_information)


if __name__ == '__main__':
    main()
