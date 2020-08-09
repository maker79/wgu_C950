# This file will utilize class Truck to create truck objects which will be doing deliveries
# and it will contain all the methods that will meet requirements and deal with constraints
# regarding deliveries

from model.truck import Truck
from utilities.graph import Graph
from utilities.hashtable import *
from model.delivery_locations import *

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

            if package[5] == '10:30 AM' and package[7] == 'Delayed on flight---will not arrive to depot until 9:05 am':
                truck_2.add_package(package)

    # This for loop will handle packages that have to be delivered by 10:30 am with no special notes 3rd priority
