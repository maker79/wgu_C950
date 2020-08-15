# This file is to create class Truck with fallowing methods
class Truck:

    def __init__(self):
        self.truck_route = []
        self.truck_speed = 0.3  # per min equivalent to 18mph
        self.loaded_packages = []
        self.start_time = None
        self.current_time = None
        self.end_time = None

    # This method will insert a package onto the truck and it will
    # append the address for the package to the truck's route
    def add_package(self, package):
        self.loaded_packages.append(package)
        self.truck_route.append(package[1])

    # This method will remove the packages from the truck that are delivered
    # and it will remove the address for the delivered package from the truck's route
    def delete_package(self, package):
        self.loaded_packages.remove(package)
        self.truck_route.remove(package[1])

    # Calling this method truck will leave the hub and begin deliveries
    def begin_deliveries(self, time):
        self.start_time = time

    # When called this will return the time for the deliveries that are done
    def packages_delivered(self, time):
        self.current_time = time
        return time

    # This method will provide the time for the truck that is done with the deliveries
    # and it has returned to hub
    def back_to_hub(self, time):
        self.end_time = time
        return time
