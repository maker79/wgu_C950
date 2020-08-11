from model.truck import load_truck_get_the_route
from utilities.reports import current_package_status


# This method will define user interface from where all the requirements
# regarding packages and trucks can be checked
# It will be called from main() function located inside main.py
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

        print('**************************************************************')
        submenu_1 = input('* Enter number[0] if you wish to exit application\n'
                          '* Enter number[1] if you want to see status for all the packages\n'
                          '  between 8:35 am and 9:25 am\n')

        if submenu_1 == '0':
            print('You chose to leave the application')
            SystemExit

        if submenu_1 == '1':
            current_package_status(9, 20)
