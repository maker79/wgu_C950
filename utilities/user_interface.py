from deliveries_and_reports.reports import *

# This method will define user interface from where all the requirements
# regarding packages and trucks can be checked
# It will be called from main() function located inside main.py
from utilities.hashtable import get_package_by_id


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
            print('Current time 9:10am')
            print('*********************************************************')
            current_package_status(9, 10, 0)

            print('************************************************************')
            print('It is 10:20am. We need to correct the address for package number 9.')
            update_pack_9_address = input('Enter [0] to exit the program\n'
                                          'Enter [1] to correct the address for package number 9')

            if update_pack_9_address == '0':
                print('You chose to leave the application')
                SystemExit

            if update_pack_9_address == '1':
                print('You chose to fix the address for package number 9\n')
                print('The address will be corrected to 410 S State St, Salt Lake City, UT 84111')
                for package in truck_2.loaded_packages:
                    if package[7] == 'Wrong address listed':
                        truck_2.delete_package(package)

                update_pack_9_address = ['9', '300 State St', 'Salt Lake City', 'UT', '84103', 'EOD', '2', 'Wrong '
                                                                                                           'address '
                                                                                                           'listed',
                                         'Out for delivery']
                truck_2.add_package(update_pack_9_address)
                truck_2.truck_route = greedy_algorithm_for_shortest_distance(truck_2.truck_route)
                print('******************************************************')
                print('The address for package number 9 has been corrected.')
                print('********************************************************')
                submenu_2 = input('Enter [0] to EXIT the program: \n'
                                  'Enter [1] to see status for all the packages between 9:35am and 10:25am')

                if submenu_2 == '0':
                    print('You chose to leave the program.')
                    SystemExit

                if submenu_2 == '1':
                    print('Current time 10:10am')
                    print('*********************************************************')
                    current_package_status(10, 10, 0)

                    submenu_3 = input('Enter [0] to EXIT the program: \n'
                                      'Enter [1] to see status for all the packages between 12:03pm and 1:12pm')

                    if submenu_3 == '0':
                        print('You chose to leave the program.')
                        SystemExit

                    if submenu_3 == '1':
                        print('Current time 12:57pm')
                        print('********************************************************')
                        current_package_status(12, 57, 0)

                        print('*********************************************************')
                        print('*Final Results of the Deliveries*')
                        del_results = input('Enter [0] to EXIT the program\n'
                                            'Enter [1] to see the details of the deliveries:')

                        if del_results == '0':
                            print('You chose to leave the program')
                            SystemExit

                        if del_results == '1':
                            make_deliveries()
                            total_truck_miles_traveled()
                            SystemExit

    elif entry_point == '2':
        print('Time 7:59am. Packages should be at the HUB or \n'
              'delayed on flight. Check for an individual package by id')
        index = '1'
        while index == '1':
            print('****************************************************')
            search_package_id = input('Enter package ID from 1 to 40 :')
            package_id = int(search_package_id)

            get_package_by_id(package_id)
            print('*****************************************************')
            another_search = input('Press any key to EXIT\n'
                                   'Press [1] to do another search by ID: ')
            index = another_search

        user_interface()
