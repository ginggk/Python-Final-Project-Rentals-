# import core
import disk


def welcome():
    print("Welcome to GB's Book Rental Store!!")

def user():
    print("{0} 'Uglies' by Scott Westerfield is 10 dollars a day. \n {1} 'Unwind' by Neal Shusterman is 16 dollars a day. \n {2} 'Binge' by Tyler Oakley is 20 dollars a day.").format(.., .., ..)
    response = input("What book would you like to rent today?").strip()
    if response == 'Uglies':
        print("It will be {} for 5 days.").format(inventory['Book1']['Price'])
    elif response == 'Unwind':
        print("It will be {} for 5 days.").format(inventory['Book2']['Price'])
    elif response == 'Binge':
        print("It will be {} for 5 days.").format(inventory['Book3']['Price'])


def employee():
    while True:
        employee = input("Would you like to see what is in [s]tock, [t]ransaction history, or [c]alculate the total revenue?").strip().lower()
        if employee == 's' or employee == 'in stock':
            # stock()
        elif employee == 'h' or employee == 'history':
            # history()
        elif employee == 't' or employee == 'total revenue':
            # total_revenue()
        else:
            print("That is not a valid response, please put in a valid choice!")




def main():
    welcome()
    while True:
        user = input("Are you a [1]employee or a [2]customer?")
        if user == 'customer' or user == '1':
            user()
        elif user == 'employee' or user == '2':
            employee()
        else: 
            print("Invalid choice! Please tell us if you are a customer or a trusted employee!")


if __name__ == '__main__':
    main()
