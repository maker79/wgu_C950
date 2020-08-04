# from utilities.package_csv_reader import get_package_info


# The goal of this hash table is to improve the speed of accessing the packages
class PackageHashTable:

    def __init__(self):
        self.capacity = 32
        self.table = []

        for i in range(self.capacity):
            self.table.append([])

    # This method will add a package into the Hashtable based on the key-index 0(PackageId)
    # form csv file, package_file.csv
    # Big O complexity is O(1)
    def add_package(self, key, value_package):
        value_package[0] = int(value_package[0])
        bucket_space = key % len(self.table)
        self.table[bucket_space].append(value_package)

    # This method will search for an existing package from the table, based on package Id
    # Complexity O(N)
    def get_package(self, key):
        # get the bucket_space from where particular id should be found
        bucket_space = key % len(self.table)
        bucket_list = self.table[bucket_space]

        # loop through the list from one bucket space to find a package id
        for package_id in bucket_list:
            if package_id[0] == key:
                return package_id
            else:
                return False

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



