# This method will define user interface from where all the requirements
# regarding packages and trucks can be checked
# It will be called from main() function located inside main.py
from utilities.deliveries import load_truck_get_the_route


def user_interface():
    entry_point = input("Welcome to the main screen. Please, choose your options:\n"
                        "Enter 0 - leave the program\n"
                        "Enter 1 - load trucks\n"
                        "Enter 2 - lookup package by ID\n")

    # This option will exit entry point and close the application
    if entry_point == '0':
        print('You chose to leave the application')
        SystemExit

    elif entry_point == '1':
        print('TIME: 08:00am -- Packages are now loaded.')
        load_truck_get_the_route()



