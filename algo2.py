#Richard Le
#Richard.le@csu.fullerton.edu
#Marco Chavez
#marco_chavez@csu.fullerton.edu
#Arman Madatyan 
#armanmadatyan@csu.fullerton.edu
#Jeremy Mejia
#fr.jeremy@csu.fullerton.edu

class HashEntry:  
    # the constructor for a hash entry
    def __init__(self, student_id):  
        # store the student registration ID
        self.student_id = student_id  
        self.count = 1  # Start the count at 1 since the ID was seen once


class CustomHashTable:
    # the constructor for the hash table
    def __init__(self, size):  
        # Store the size of the hash table
        self.size = size  
        # array of empty chains for collision handling
        self.table = [[] for _ in range(size)]  

    def hash_function(self, key):  
         # return the index using h(key) = key mod m
        return key % self.size 

    # def for insert a new ID or increase its count if it exists
    def insert_or_increment(self, student_id):  
        # compute the hash table index
        index = self.hash_function(student_id)  
        # get the chain stored at this index
        chain = self.table[index]  

        # loop through each entry in chain
        for entry in chain:  
            # checks if the ID already exists
            if entry.student_id == student_id:  
                entry.count += 1  # increment its count by 1
                return False  # returns False if not first time

        # adds a new entry if the ID was not found
        chain.append(HashEntry(student_id))  
        return True  # returns True if first time ID
    # gets the count for a specific student ID
    def get_count(self, student_id): 
        index = self.hash_function(student_id)
        # get the chain stored at this index
        chain = self.table[index] 

        # loop through each entry in chain
        for entry in chain: 
            # check if this entry matches the target ID
            if entry.student_id == student_id:  
                return entry.count  # return how many times the ID appears

        return 0  # return 0 if the ID was not found

# function to read IDs from a file
def read_ids_from_file(filename):  
    # empty list to store IDs
    ids = []  

    # input file in read mode w/ loop for each line in file
    with open(filename, "r") as file:  
        for line in file:  
            # splits line by spaces and commas
            parts = line.replace(",", " ").split()  
            # loops through each possible ID string
            for part in parts: 
                # converts the ID to an integer and add to list
                ids.append(int(part))  

    # retursn the completed list of IDs

    return ids  

# duplicate detection function
def detect_duplicates(ids):  
    # should choose a hash table size larger than the input size
    table_size = len(ids) * 2 + 1  
    # custom hash table
    hash_table = CustomHashTable(table_size)  
    # tores IDs in the order they first appeared
    first_seen_order = []  
    # loops through everyy student Id in the input
    for student_id in ids: 
        # insert the ID or increment its count
        is_new = hash_table.insert_or_increment(student_id)  

        if is_new:  # Cchecks if this is the first time seeing the ID
            first_seen_order.append(student_id)  # stores the ID in first-seen order

    duplicates = []  # list to store duplicate IDs and their counts
    unique_count = len(first_seen_order)  # count of how many unique IDs appeared

    for student_id in first_seen_order:  # loops through IDs in first-seen order
        count = hash_table.get_count(student_id)  # gets the final count for this ID

        if count > 1:  # checks if this ID is a duplicate
            duplicates.append((student_id, count))  # then adds duplicate ID and count to the result

    return duplicates, unique_count  

# store the name of the input file
filename = "ids.txt"  
# read student IDs from the file
ids = read_ids_from_file(filename)  

# detects duplicates using the custom hash table
duplicates, unique_count = detect_duplicates(ids)

print("Duplicates found (in order of first appearance):")  

# looping through each duplicate result
for student_id, count in duplicates:  
    print(f"{student_id} -> appears {count} times")

print(f"Total unique IDs: {unique_count}")  # unique ids
print(f"Total duplicate IDs: {len(duplicates)}")  # num of id duplicates