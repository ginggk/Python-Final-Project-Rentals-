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


def user_select_book(inventory_dictionary, type_of_transaction):
    while True:
        # print('-------------------------------------------------')
        core.printable_inventory(inventory_dictionary)
        print("------------------------------------------------")
        response = input(
            " What book would you like to " + type_of_transaction +
            " today?\n (type [d]one when you are finished shopping)\n").strip(
            )
        if response in inventory_dictionary.keys():
            if core.check_stock(inventory_dictionary,
                                response) and type_of_transaction == "rent":
                print(
                    "Sorry! That book is out of stock, please choose another one of our quality books!"
                )
            else:
                return response
        else:
            print(
                "We are sorry, we do not have that book. Please choose a provided book."
            )


def bring_back(inventory_dictionary):
    response = user_select_book(inventory_dictionary, 'return')
    core.book_return(inventory_dictionary, response)
    print("Here is your deposit...")
    print("Thank you for reading one of our books!")
    # go in core and write the right function
    deposit = core.negative_deposit(inventory_dictionary, response)
    transaction = core.history_string(response, 'return', deposit)
    return transaction


def user_rent(inventory_dictionary):
    response = user_select_book(inventory_dictionary, 'rent')

    core.update_stock(inventory_dictionary, response)
    # go in core and write the right function
    sale = core.set_days(inventory_dictionary[response]['Price'], 5)
    tax = core.sales_tax(sale)
    deposit = core.deposit(inventory_dictionary, response)
    total = core.final_total(inventory_dictionary[response]['Price'], tax,
                             deposit)
    print(core.make_book_sentence(inventory_dictionary, response, sale))
    transaction = core.history_string(response, 'rent', total)
    return transaction


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
