# This file contains methods that are responsible for reporting and displaying confirmation
# that all the requirements are met(ex. mileage is under 145mi, all packages are delivered on time...)

from utilities.graph import Graph
from utilities.deliveries import *
from model.truck import Truck
from model.delivery_locations import *
from datetime import *


# This method will get the miles traveled by an individual truck which will later help to get
# total miles traveled by all trucks
# Complexity is O(N)
def truck_miles_traveled(route):
    distance_list = locations.distance
    miles_traveled = 0

    for i in range(0, len(route) - 1):
        miles_traveled = miles_traveled + distance_list[route[i], route[i + 1]]

    return miles_traveled


# This method will get the total of miles traveled by all trucks
# Complexity is O(1)
def total_truck_miles_traveled():
    truck_1_miles_traveled = truck_miles_traveled(truck_1.truck_route)
    truck_2_miles_traveled = truck_miles_traveled(truck_2.truck_route)
    truck_3_miles_traveled = truck_miles_traveled(truck_3.truck_route)

    total_mi_traveled = truck_1_miles_traveled + truck_2_miles_traveled + truck_3_miles_traveled

    print('Truck number 1 traveled ' + str(round(truck_1_miles_traveled)))
    print('Truck number 2 traveled ' + str(round(truck_2_miles_traveled)))
    print('Truck number 3 traveled ' + str(round(truck_3_miles_traveled)))
    print('***************************************************************')
    print('Total miles traveled by all three trucks is: ' + str(round(total_mi_traveled)))


# This method will make sure that all the packages are delivered to the correct address
# Complexity is O(N^2)
def make_deliveries():
    mi_between_dlv_points = locations.distance

    # Deliveries for truck number 1
    start_truck_number_1 = datetime(2020, 8, 9, 8, 0)
    truck_1.start_time = start_truck_number_1
    truck_1.current_time = start_truck_number_1

    for i in range(0, len(truck_1.truck_route) - 1):
        distance = mi_between_dlv_points[truck_1.truck_route[i], truck_1.truck_route[i + 1]]
        speed = truck_1.truck_speed
        minutes = distance / speed
        time_delivered = truck_1.current_time + minutes
        truck_1.current_time = datetime(2020, 8, 9, time_delivered.hour, time_delivered.minute)
        delivery_update = 'Package delivered at :' + str(time_delivered)

        for package in truck_1.loaded_packages:
            if truck_1.truck_route[i + 1] == package[1]:
                package[8] = delivery_update

    truck_1.end_time = truck_1.current_time

    print('Packages that were delivered using truck number 1: ', *truck_1.loaded_packages, sep='\n')

    # Deliveries for truck number 2
