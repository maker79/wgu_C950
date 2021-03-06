import csv


# The goal of this hash table is to improve the speed of accessing the packages
class PackageHashTable:

    # This method is the constructor method initialized to empty
    # Complexity is O(N)
    def __init__(self, capacity=32):
        self.table = []

        for i in range(capacity):
            self.table.append([])

    # This method will add a package into the Hashtable based on the key-index 0(PackageId)
    # from csv file, package_file.csv
    # Big O complexity is O(1)
    def add_package(self, key, value_package):
        value_package[0] = int(value_package[0])
        bucket_space = key % len(self.table)
        self.table[bucket_space].append(value_package)
        if value_package[7] != 'Delayed on flight---will not arrive to depot until 9:05 am':
            value_package.append('Package at HUB')
        if value_package[7] == 'Delayed on flight---will not arrive to depot until 9:05 am':
            value_package.append('Package delayed on flight-not in HUB')

    # This method will search for an existing package from the table, based on package Id
    # Complexity O(N)
    def get_package(self, key):
        # get the bucket_space from where particular id should be found
        bucket_space = key % len(self.table)
        bucket_list = self.table[bucket_space]

        # loop through the list from one bucket space to find a package id
        # if the package gets found it will get returned, otherwise returns None
        for package_id in bucket_list:
            if package_id[0] == key:
                return package_id
        return None

    # This method will look for package Id and remove it from the table
    # Complexity O(N)
    def delete_package(self, key):
        # get the bucket_space from where particular id should be found
        bucket_space = hash(key) % len(self.table)
        bucket_list = self.table[bucket_space]
        # loop through the bucket list and remove the package id if matches a key entered
        for package_id in bucket_list:
            if package_id[0] == key:
                bucket_list.remove(key)


# This method will read the csv file that contains package info
# and import the data from the package_file.csv to the hashtable
# Complexity O(N)
def get_package_info(file_name):
    packages_list = PackageHashTable()
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        # the next will skip over headers and start reading from 1st actual package, line 2
        next(csv_reader, None)

        for line in csv_reader:
            packages_list.add_package(int(line[0]), line)  # adding package Id as an integer

    return packages_list


list_of_packages = get_package_info(
    u'C:\\Users\\Vladan\\PycharmProjects\\TSP_data_structures_and_algorithms_II\\data\\package_file.csv')


# This method will look through the hash table for the package by Id and display the info
def get_package_by_id(package_info):
    package_found = list_of_packages.get_package(package_info)
    print(package_found)
