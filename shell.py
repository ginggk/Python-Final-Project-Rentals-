from core import *
import disk


def welcome():
    print("Welcome to GB's Book Rental Store!!")


def user_employee():
    while True:
        comment = input(
            "Are you a [1]employee or a [2]customer?").strip().lower()
        if comment == 'customer' or comment == '2':
            user()
        elif comment == 'employee' or comment == '1':
            employee()
        else:
            print(
                "Invalid choice! Please tell us if you are a customer or a trusted employee!"
            )


# def make_inventory():
# inventory = open_inventory()
# return inventory


def user():
    inventory_information = disk.open_inventory()
    inventory_dictionary = disk.create_inventory(inventory_information)
    while True:
        print(
            " 'Uglies' by Scott Westerfield is 10 dollars a day. \n 'Unwind' by Neal Shusterman is 16 dollars a day. \n 'Binge' by Tyler Oakley is 20 dollars a day."
        )
        print("------------------------------------------------")
        response = input(
            " What book would you like to rent today?\n (type [d]one when you are finished shopping)\n"
        ).strip()
        if response == 'Uglies':
            print("{} has {} copies in stock.".format(
                inventory_dictionary['Uglies']['Name'],
                inventory_dictionary['Uglies']['In Stock']))
            print("It will be {}  dollars for 5 days.".format(set_days(10, 5)))
            print("With Sales Tax your total is: ${}".format(
                sales_tax(set_days(10, 5))))
            print("----------------------------------------------")
        elif response == 'Unwind':
            print("{} has {} copies in stock.".format(
                inventory_dictionary['Unwind']['Name'],
                inventory_dictionary['Unwind']['In Stock']))
            print("It will be {} dollars for 5 days.".format(set_days(16, 5)))
            print("With Sales Tax your total is: ${}".format(
                round(sales_tax(set_days(16, 5)))))
            print("----------------------------------------------")
        elif response == 'Binge':
            print("{} has {} copies in stock.".format(
                inventory_dictionary['Binge']['Name'],
                inventory_dictionary['Binge']['In Stock']))
            print("It will be {} dollars for 5 days.".format(set_days(20, 5)))
            print("With Sales Tax your total is: ${}".format(
                round(sales_tax(set_days(20, 5)))))
            print("----------------------------------------------")
        elif response == 'd' or response == 'done':
            break
        else:
            print(
                "We are sorry, we do not have that book. Please choose a provided book."
            )


def employee():
    while True:
        choice = input(
            "Would you like to see what is in [s]tock, [t]ransaction history, or [c]alculate the total revenue?"
        ).strip().lower()
        if choice == 's' or choice == 'in stock':
            print("stock")
        elif choice == 'h' or choice == 'history':
            print('history')
        elif choice == 't' or choice == 'total revenue':
            print('Total Revenue')
        else:
            print(
                "That is not a valid response, please put in a valid choice!")


def main():
    welcome()
    inventory_information = disk.open_inventory()
    inventory_dictionary = disk.create_inventory(inventory_information)
    user_employee()
    make_inventory()
    # inventory_information = open_inventory()
    # inventory_dictionary = disk.create_inventory(inventory_information)


if __name__ == '__main__':
    main()
