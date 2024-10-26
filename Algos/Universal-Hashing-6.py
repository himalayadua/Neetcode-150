import cityhash  # Importing CityHash
import random

class CityHashWrapper:
    def __init__(self, size):
        self.size = size
        self.b = random.randint(0, size - 1)

    def hash(self, key):
        # Using CityHash to generate a hash value
        return ((cityhash.CityHash128(key) % self.size + self.b) % self.size)

class UMAC:
    def __init__(self, key):
        self.key = key

    def generate_mac(self, message):
        # Simple UMAC-like function (not secure, just for demonstration purposes)
        h = (hash(message) + hash(self.key)) % (2**32)
        return h

class ChainedHashTable:
    def __init__(self, initial_size=17, mac_key=None):
        self.size = initial_size
        self.table = [[] for _ in range(self.size)]
        self.hash_func = CityHashWrapper(self.size)
        self.umac = UMAC(mac_key) if mac_key else None
        self.count = 0

    def set(self, key, value):
        if self.count / self.size > 0.7:  # Load factor threshold
            self._resize()
        mac = self.umac.generate_mac(value) if self.umac else None
        index = self.hash_func.hash(key)
        for i, (k, v, _) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value, mac)
                return
        self.table[index].append((key, value, mac))
        self.count += 1

    def get(self, key):
        index = self.hash_func.hash(key)
        for k, v, mac in self.table[index]:
            if k == key:
                return v, mac
        return None, None

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")

    def _resize(self):
        old_table = self.table
        new_size = next_prime(self.size * 2)  # Find next prime number
        self.size = new_size
        self.table = [[] for _ in range(self.size)]
        self.hash_func = CityHashWrapper(self.size)
        for chain in old_table:
            for key, value, mac in chain:
                index = self.hash_func.hash(key)
                self.table[index].append((key, value, mac))

def next_prime(n):
    """Finds the next prime number greater than n."""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    while not is_prime(n):
        n += 1
    return n

# Sample test for the hash table implementation with MACs
people = [
    ("Swathi", "Swathi@example.com"),
    ("Akram", "Akram@example.com"),
    ("Cai", "Cai@example.com"),
    ("Shreya", "Shreya@example.com"),
    ("Mengxiao", "Mengxiao@example.com"),
    ("Himalaya", "Himalaya@example.com"),
    ("Eluri", "Eluri@example.com"),
    ("Fu", "Fu@example.com"),
    ("Siyi", "Siyi@example.com"),
    ("Jacob", "Jacob@example.com")
]

mac_key = "my_secret_key"
hash_table = ChainedHashTable(initial_size=17, mac_key=mac_key)
for name, email in people:
    hash_table.set(name, email)

# Display the contents of the hash table
hash_table.display()

# Testing retrieval of existing and non-existing keys
print(hash_table.get("Eluri")) 
print(hash_table.get("Swathi"))  

# Test retrieval of a non-existing key
print(hash_table.get("John"))  # Should return (None, None)