from model.delivery_locations import *


# This method will implement greedy algorithm that will be used
# to determine the best possible route for each truck that starts its deliveries
# from the hub. It will start from the hub "4001 South 700 East" and it will sort
# the addresses that are attached to each package and determine the next location
# among deliveries based on the shortest distance
# Complexity is O(n log n)

def greedy_algorithm_for_shortest_distance(truck_route):
    starting_point = '4001 South 700 East'
    distances = locations.distance
    route_to_sort = truck_route

    # greedy algo for shortest distance will start at the hub and build a better route
    better_route = [starting_point]

    # while loop will loop through the route that was passed to the algorithm
    # until all the location are removed from the list
    # and it will return the shortest route
    while len(route_to_sort) != 0:
        beginning = [0, starting_point]

        # for loop will loop through the route that needs to be sorted
        # and it will get distance between each location
        for del_point in route_to_sort:
            distance = distances[better_route[-1], del_point]

            if beginning[0] == 0:
                beginning = [distance, del_point]
            if distance < beginning[0] and distance != 0:
                beginning = [distance, del_point]

        if beginning[1] not in better_route:
            better_route.append(beginning[1])

        route_to_sort.remove(beginning[1])

    return better_route  # the better rout is returned
