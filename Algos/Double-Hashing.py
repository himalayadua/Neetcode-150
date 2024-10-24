def double_hashing_insertion(keys, table_size):
    # Initialize the hash table with None
    hash_table = [None] * table_size
    collision_count =0
    print (hash_table)
    # Primary hash function
    def h1(x):
        return x % table_size

    # Secondary hash function
    def h2(x):
        return 1 + (x % (table_size - 1))

    # Inserting keys using double hashing
    for key in keys:
        index = h1(key)
        step_size = h2(key)
        # Find a spot using double hashing
        while hash_table[index] is not None:
            index = (index + step_size) % table_size
            collision_count += 1
        hash_table[index] = key
        print (hash_table)
        print(f"Number of collisions: {collision_count}")
    return hash_table

# Given sequence of integers
keys = [27, 18, 29, 28, 39, 13, 16]
# Hash table size
table_size = 11

# Perform double hashing insertion
final_hash_table = double_hashing_insertion(keys, table_size)
print(final_hash_table)
