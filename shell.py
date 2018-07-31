from core import *
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
        print(
            " 'Uglies' by Scott Westerfield is 10 dollars a day. \n 'Unwind' by Neal Shusterman is 16 dollars a day. \n 'Binge' by Tyler Oakley is 20 dollars a day."
        )
        print("------------------------------------------------")
        back = input(
            "Which of these books would you like to return today?").strip()
        if back == 'Uglies':
            book_return(inventory_dictionary, 'Uglies')
            disk.write_to_inventory(inventory_dictionary)
            disk.write_to_history('-5.0')
            print("Thank you for reading one of our books!")
            break
        elif back == 'Unwind':
            book_return(inventory_dictionary, 'Unwind')
            disk.write_to_inventory(inventory_dictionary)
            disk.write_to_history('-8.0')
            print("Thank you for reading one of our books!")
            break
        elif back == 'Binge':
            book_return(inventory_dictionary, 'Binge')
            disk.write_to_inventory(inventory_dictionary)
            disk.write_to_history('-10.0')
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
            )
            if keep == 'return':
                bring_back()
            elif keep == 'b' or keep == 'back':
                return
            else:
                break
        while True:
            print('-------------------------------------------------')
            print(
                " 'Uglies' by Scott Westerfeld is 10 dollars a day. \n 'Unwind' by Neal Shusterman is 16 dollars a day. \n 'Binge' by Tyler Oakley is 20 dollars a day."
            )
            print("------------------------------------------------")
            response = input(
                " What book would you like to rent today?\n (type [d]one when you are finished shopping)\n"
            ).strip()
            if response == 'Uglies':
                if check_stock(inventory_dictionary, 'Uglies') == True:
                    print(
                        "Sorry! That book is out of stock, please choose another one of our quality books!"
                    )
                else:
                    print("-----------------------------------")
                    print("{} has {} copies in stock.".format(
                        inventory_dictionary['Uglies']['Name'],
                        inventory_dictionary['Uglies']['In Stock']))
                    print("It will be {}  dollars for 5 days.".format(
                        set_days(10, 5)))
                    print("With Sales Tax your total is: ${}".format(
                        sales_tax(set_days(10, 5))))
                    print("The Deposit is: $5.00")
                    print("Your Final Total is: $58.85")
                    update_stock(inventory_dictionary, 'Uglies')
                    disk.write_to_inventory(inventory_dictionary)
                    disk.write_to_history('58.85')
                    # print("----------------------------------------------")
            elif response == 'Unwind':
                if check_stock(inventory_dictionary, 'Unwind') == True:
                    print(
                        "Sorry! That book is out of stock, please choose another one of our quality books!"
                    )
                else:
                    print("-----------------------------------")
                    print("{} has {} copies in stock.".format(
                        inventory_dictionary['Unwind']['Name'],
                        inventory_dictionary['Unwind']['In Stock']))
                    print("It will be {} dollars for 5 days.".format(
                        set_days(16, 5)))
                    print("With Sales Tax your total is: ${}".format(
                        round(sales_tax(set_days(16, 5)))))
                    print("The Deposit is: $8.00")
                    print("Your Final Total is: $94.16")
                    update_stock(inventory_dictionary, 'Unwind')
                    disk.write_to_inventory(inventory_dictionary)
                    disk.write_to_history('94.16')
                    # print("----------------------------------------------")
            elif response == 'Binge':
                if check_stock(inventory_dictionary, 'Binge') == True:
                    print(
                        "Sorry! That book is out of stock, please choose another one of our quality books!"
                    )
                else:
                    print("-----------------------------------")
                    print("{} has {} copies in stock.".format(
                        inventory_dictionary['Binge']['Name'],
                        inventory_dictionary['Binge']['In Stock']))
                    print("It will be {} dollars for 5 days.".format(
                        set_days(20, 5)))
                    print("With Sales Tax your total is: ${}".format(
                        round(sales_tax(set_days(20, 5)))))
                    print("The Deposit is: $10.00")
                    print("Your Final Total is: $117.70")
                    update_stock(inventory_dictionary, 'Binge')
                    disk.write_to_inventory(inventory_dictionary)
                    disk.write_to_history('117.70')
                    # print("----------------------------------------------")
            elif response == 'd' or response == 'done':
                break
            # elif response == 'b' or response == 'back':
            # break
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
            print(make_inventory_string(inventory_dictionary))
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
