import core
import disk


def welcome():
    print("Welcome to GB's Book Rental Store!!")


def user_employee():
    while True:
        comment = input(
            "Are you a [1]employee or a [2]customer?(if you would like to quit, please type (q).\n"
        ).lower().strip()
        if comment in ['customer', '2']:
            return 'customer'
        elif comment in ['employee', '1']:
            return 'employee'
        elif comment == 'q' or comment == 'quit':
            return 'quit'
        print(
            "Invalid choice! Please tell us if you are a customer or a trusted employee!"
        )


def bring_back(inventory_dictionary):
    while True:
        print('-------------------------------------------------')
        core.printable_inventory(inventory_dictionary)
        print("------------------------------------------------")
        back = input(
            "Which of these books would you like to return today?").strip()
        if back in inventory_dictionary:
            core.book_return(inventory_dictionary, back)
            print("Here is your deposit...")
            print("Thank you for reading one of our books!")
            break
        else:
            print("That is not one of our book, try again please.")


def get_rent_or_return():
    while True:
        print('--------------------------------------------------')
        keep = input(
            "Would you like to return or rent a book today?\n(if you would like to go back, type(b)\n"
        ).strip().lower()
        if keep in ['rent', 'return']:
            return keep
        elif keep in ['back', 'b']:
            return 'back'
        print('invalid!!')


def user_select_book(inventory_dictionary):
    while True:
        print('-------------------------------------------------')
        core.printable_inventory(inventory_dictionary)
        print("------------------------------------------------")
        response = input(
            " What book would you like to rent today?\n (type [d]one when you are finished shopping)\n"
        ).strip()
        if response in inventory_dictionary.keys():
            if core.check_stock(inventory_dictionary, response) == True:
                print(
                    "Sorry! That book is out of stock, please choose another one of our quality books!"
                )
            else:
                return response
        else:
            print(
                "We are sorry, we do not have that book. Please choose a provided book."
            )


def user_rent(inventory_dictionary):
    response = user_select_book(inventory_dictionary)
    print('you rented', core.make_book_sentence(inventory_dictionary,
                                                response))
    core.update_stock(inventory_dictionary, response)


def employee():
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
    while True:
        decision = user_employee()
        if decision == 'customer':
            rent_or_return = get_rent_or_return()
            if rent_or_return in ['rent', 'return']:
                if rent_or_return == 'rent':
                    transaction = user_rent(inventory_dictionary)
                elif rent_or_return == 'return':
                    transaction = bring_back(inventory_dictionary)
                disk.write_to_inventory(inventory_dictionary)
                disk.write_to_history(transaction)
            else:
                continue
        elif decision == 'employee':
            employee(inventory_dictionary)
        elif decision == 'quit':
            print('exiting program...')
            exit()


if __name__ == '__main__':
    main()
