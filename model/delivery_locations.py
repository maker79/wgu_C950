# The purpose of this file is to read in names of all the locations from distances_file.csv and
# build the delivery points(vertices). It will also read in the mileage from the same file
# and connect those delivery points with the distance in miles(edges of the graph)

from utilities.graph import Graph
import csv


# This method will read in the distance_file.csv file
# Complexity is O(N)


def get_distances(file_name):
    distance_data = []

    with open(file_name, 'r') as distance_file:
        csv_reader = csv.reader(distance_file)
        next(csv_reader, None)

        for line in csv_reader:
            distance_data.append(line)

    return distance_data


# This method will read in the distances file and pull out the addresses of the locations
# in order to create delivery points-vertices and connect them
# Complexity is O(N^2)

# def set_delivery_locations(file_name):
#     delivery_data = get_distances(file_name)
#     distances = Graph()
#
#     for line in delivery_data:
#         distances.add_location(line[1]) # this location is a street address

    # it will start grabbing distances from distances file

