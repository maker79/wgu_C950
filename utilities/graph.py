# This file will create a class Graph that will help to build delivery points
# in the delivery_locations.py file

class Graph:

    def __init__(self):
        self.drop_locations = {}
        self.distance = {}

    # This method will add a delivery location point to the graph
    # It will insert a location address as key to drop_locations dictionary
    def add_location(self, location_point):
        self.drop_locations[location_point] = []

    # This method will add distance between delivery points in miles
    # It will insert values in distance dictionary keys as points and values as miles

    def add_distance(self, point_x, point_y, distance=1.0):
        self.distance[(point_x, point_y)] = distance

    # This method will relate packages with a relevant location on the graph
    # it appends package to a drop_location dictionary

    def relate_package(self, hash_table):

        for bucket in hash_table.table:
            for item in bucket:
                self.drop_locations[item[1]].append(item)
