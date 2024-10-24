class LinearProbeHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % 10

    def insert(self, key):
        index = self.hash_function(key)
        # Linear probing to find an empty slot
        while self.table[index] is not None:
            index = (index + 1) % self.size
        # Insert the key into the found empty slot
        self.table[index] = key

    def display(self):
        for i, key in enumerate(self.table):
            print(f"Index {i}: {key}")

# Create a hash table of size 10
hash_table = LinearProbeHashTable(10)

# Insert the keys: [5, 15, 6, 3, 27, 8]
keys = [5, 15, 6, 3, 27, 8]
print (hash_table.table)
for key in keys:
    hash_table.insert(key)
    print (hash_table.table)


# Display the state of the hash table
hash_table.display()
