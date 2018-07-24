from core import *
from disk import *


def welcome():
    print("Welcome to GB's Book Rental Store!!")


def user():
    print(
        "'Uglies' by Scott Westerfield is 10 dollars a day. \n 'Unwind' by Neal Shusterman is 16 dollars a day. \n 'Binge' by Tyler Oakley is 20 dollars a day."
    )
    response = input("What book would you like to rent today?").strip()
    if response == 'Uglies':
        print("It will be {} for 5 days.".format(
            disk.inventory['Book1']['Price']))
    elif response == 'Unwind':
        print("It will be {} for 5 days.".format(
            disk.inventory['Book2']['Price']))
    elif response == 'Binge':
        print("It will be {} for 5 days.".format(
            disk.inventory['Book3']['Price']))


def employee():
    while True:
        employee = input(
            "Would you like to see what is in [s]tock, [t]ransaction history, or [c]alculate the total revenue?"
        ).strip().lower()
        if employee == 's' or employee == 'in stock':
            print("stock")
        elif employee == 'h' or employee == 'history':
            print('history')
        elif employee == 't' or employee == 'total revenue':
            print('Total Revenue')
        else:
            print(
                "That is not a valid response, please put in a valid choice!")


def main():
    welcome()
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
            break


if __name__ == '__main__':
    main()
