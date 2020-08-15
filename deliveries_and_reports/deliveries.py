# # This file will create instances of class Trucks and take care of deliveries
from model.delivery_locations import locations
from model.truck import Truck
from utilities.algo import greedy_algorithm_for_shortest_distance
from utilities.hashtable import list_of_packages

# This list will be used to store locations pulled out from a dictionary of our drop locations
addresses = []

locations.relate_package(list_of_packages)  # load packages and relate them with a location

truck_1 = Truck()
truck_2 = Truck()
truck_3 = Truck()


# This method will load the trucks with appropriate packages and decide which route is the best for a truck.
# It will populate the address list with the locations from locations dictionary
# Complexity is O(N^2)
def load_truck_get_the_route():
    for delivery_point in locations.drop_locations:
        addresses.append(delivery_point)

    # This for loop will look for the packages that have to be delivered by 9:00 am
    for address in addresses:
        for package in locations.drop_locations[address]:
            if package[5] == '9:00 AM':
                truck_1.add_package(package)

    # This for loop will check for packages that have to be delivered by 10:30 am and
    # delayed on flight or have any form of special note
    for address in addresses:
        for package in locations.drop_locations[address]:
            if package[5] == '10:30 AM' and package[7] != '' and \
                    package[7] != 'Can only be on truck 2' and package[7] != 'Wrong address listed' and \
                    package[7] != 'Delayed on flight---will not arrive to depot until 9:05 am':
                truck_1.add_package(package)

            elif package[5] == '10:30 AM' and \
                    package[7] == 'Delayed on flight---will not arrive to depot until 9:05 am':
                truck_2.add_package(package)

    # This for loop will handle packages that have to be delivered by 10:30 am with no special notes
    for address in addresses:
        for package in locations.drop_locations[address]:
            if package[5] == '10:30 AM' and package[7] == '':
                truck_1.add_package(package)

    # This for loop will handle packages that have to be delivered by the end of the day and those packages
    # that are delayed on flight and truck two only and those with a wrong address
    for address in addresses:
        for package in locations.drop_locations[address]:
            if package[5] == 'EOD' and package[7] == 'Delayed on flight---will not arrive to depot until 9:05 am':
                truck_2.add_package(package)
            if package[5] == 'EOD' and package[7] == 'Wrong address listed':
                truck_2.add_package(package)
            if package[5] == 'EOD' and package[7] == 'Can only be on truck 2':
                truck_2.add_package(package)

    # This for loop will handle packages that have to be delivered by the end of the day without special notes
    # but cannot be loaded onto previous trucks because other trucks already have 16 packages loaded
    for address in addresses:
        for package in locations.drop_locations[address]:
            if package[5] == 'EOD' and package[7] == '':
                if len(truck_1.loaded_packages) < 16:
                    truck_1.add_package(package)
                elif len(truck_2.loaded_packages) < 16:
                    truck_2.add_package(package)
                elif len(truck_3.loaded_packages) < 16:
                    truck_3.add_package(package)
                else:
                    print('Package cannot be loaded at this time. Please come back later!')

    # Let's create some inefficient route to make deliveries and after apply algorithm to make it efficient
    # truck_1_inefficient_route = truck_1.truck_route
    # truck_1_inefficient_route.append('4001 South 700 East')
    # truck_2_inefficient_route = truck_2.truck_route
    # truck_2_inefficient_route.append('4001 South 700 East')
    # truck_3_inefficient_route = truck_3.truck_route
    # truck_3_inefficient_route.append('4001 South 700 East')

    # Apply algorithm to make route efficient
    truck_1.truck_route = greedy_algorithm_for_shortest_distance(truck_1.truck_route)
    truck_2.truck_route = greedy_algorithm_for_shortest_distance(truck_2.truck_route)
    truck_3.truck_route = greedy_algorithm_for_shortest_distance(truck_3.truck_route)

    # Send the truck back to the warehouse
    # truck_1.truck_route.append('4001 South 700 East')
    # truck_2.truck_route.append('4001 South 700 East')
    # truck_3.truck_route.append('4001 South 700 East')

    # display data for the truck and packages after loading
    print('All trucks are now loaded and they have fallowing packages:')
    print('**********************************************************************')
    print('Truck number 1 has ' + str(len(truck_1.loaded_packages)) + ' packages')
    print('List of packages :', *truck_1.loaded_packages, sep='\n')
    print('**********************************************************************')
    print('Truck number 2 has ' + str(len(truck_2.loaded_packages)) + ' packages')
    print('List of packages :', *truck_2.loaded_packages, sep='\n')
    print('**********************************************************************')
    print('Truck number 3 has ' + str(len(truck_3.loaded_packages)) + ' packages')
    print('List of packages :', *truck_3.loaded_packages, sep='\n')
