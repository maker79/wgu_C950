import csv
from utilities.hashtable import PackageHashTable


# This method will read the csv file that contains package info
# and import the data from the package_file.csv to the hashtable
# Complexity O(N)

def get_package_info(file_name):
    packages_list = PackageHashTable()
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # the next will skip over headers and start reading from 1st actual package, line 2
        next(csv_reader)

        for line in csv_reader:
            packages_list.add_package(int(line[0]), line)  # adding package Id as an integer

    return packages_list


list_of_packages = get_package_info('C:\Users\Vladan\PycharmProjects\TSP_data_structures_and_algorithms_II\data\package_file.csv')
print(list_of_packages)
