import mmh3  # MurmurHash library

class MurmurHashWrapper:
    def __init__(self, size):
        self.size = size

    def hash(self, key):
        # Using MurmurHash to generate a hash value
        return mmh3.hash(key) % self.size

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
        self.hash_func = MurmurHashWrapper(self.size)
        self.umac = UMAC(mac_key) if mac_key else None
        self.count = 0

    def set(self, key, value):
        print(self.table)
        
        print(f"Load factor threshold: {self.count / self.size}")
        if self.count / self.size > 0.7:  # Load factor threshold
            self._resize()
            print(f"resized..")
        mac = self.umac.generate_mac(value) if self.umac else None
        index = self.hash_func.hash(key)
        print(f"Index calculated: {index}")
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
        self.hash_func = MurmurHashWrapper(self.size)
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
    ("Himalaya", "Himalaya.Dua@example.com"),
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

[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
Load factor threshold: 0.0
Index calculated: 0
[[('Swathi', 'Swathi@example.com', 67790305)], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
Load factor threshold: 0.058823529411764705
Index calculated: 9
[[('Swathi', 'Swathi@example.com', 67790305)], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 1483322508)], [], [], [], [], [], [], []]
Load factor threshold: 0.11764705882352941
Index calculated: 14
[[('Swathi', 'Swathi@example.com', 67790305)], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 1483322508)], [], [], [], [], [('Cai', 'Cai@example.com', 4253737963)], [], []]
Load factor threshold: 0.17647058823529413
Index calculated: 15
[[('Swathi', 'Swathi@example.com', 67790305)], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 1483322508)], [], [], [], [], [('Cai', 'Cai@example.com', 4253737963)], [('Shreya', 'Shreya@example.com', 2205024520)], []]
Load factor threshold: 0.23529411764705882
Index calculated: 10
[[('Swathi', 'Swathi@example.com', 67790305)], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 1483322508)], [('Mengxiao', 'Mengxiao@example.com', 432258665)], [], [], [], [('Cai', 'Cai@example.com', 4253737963)], [('Shreya', 'Shreya@example.com', 2205024520)], []]
Load factor threshold: 0.29411764705882354
Index calculated: 16
[[('Swathi', 'Swathi@example.com', 67790305)], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 1483322508)], [('Mengxiao', 'Mengxiao@example.com', 432258665)], [], [], [], [('Cai', 'Cai@example.com', 4253737963)], [('Shreya', 'Shreya@example.com', 2205024520)], [('Himalaya Dua', 'Himalaya.Dua@example.com', 4017076411)]]
Load factor threshold: 0.35294117647058826
Index calculated: 15
[[('Swathi', 'Swathi@example.com', 67790305)], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 1483322508)], [('Mengxiao', 'Mengxiao@example.com', 432258665)], [], [], [], [('Cai', 'Cai@example.com', 4253737963)], [('Shreya', 'Shreya@example.com', 2205024520), ('Eluri', 'Eluri@example.com', 1237542427)], [('Himalaya Dua', 'Himalaya.Dua@example.com', 4017076411)]]
Load factor threshold: 0.4117647058823529
Index calculated: 13
[[('Swathi', 'Swathi@example.com', 67790305)], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 1483322508)], [('Mengxiao', 'Mengxiao@example.com', 432258665)], [], [], [('Fu', 'Fu@example.com', 2640219225)], [('Cai', 'Cai@example.com', 4253737963)], [('Shreya', 'Shreya@example.com', 2205024520), ('Eluri', 'Eluri@example.com', 1237542427)], [('Himalaya Dua', 'Himalaya.Dua@example.com', 4017076411)]]
Load factor threshold: 0.47058823529411764
Index calculated: 15
[[('Swathi', 'Swathi@example.com', 67790305)], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 1483322508)], [('Mengxiao', 'Mengxiao@example.com', 432258665)], [], [], [('Fu', 'Fu@example.com', 2640219225)], [('Cai', 'Cai@example.com', 4253737963)], [('Shreya', 'Shreya@example.com', 2205024520), ('Eluri', 'Eluri@example.com', 1237542427), ('Siyi', 'Siyi@example.com', 2027001880)], [('Himalaya Dua', 'Himalaya.Dua@example.com', 4017076411)]]
Load factor threshold: 0.5294117647058824
Index calculated: 13


Index 0: [('Swathi', 'Swathi@example.com', 67790305)]
Index 1: []
Index 2: []
Index 3: []
Index 4: []
Index 5: []
Index 6: []
Index 7: []
Index 8: []
Index 9: [('Akram', 'Akram@example.com', 1483322508)]
Index 10: [('Mengxiao', 'Mengxiao@example.com', 432258665)]
Index 11: []
Index 12: []
Index 13: [('Fu', 'Fu@example.com', 2640219225), ('Jacob', 'Jacob@example.com', 1230626306)]
Index 14: [('Cai', 'Cai@example.com', 4253737963)]
Index 15: [('Shreya', 'Shreya@example.com', 2205024520), ('Eluri', 'Eluri@example.com', 1237542427), ('Siyi', 'Siyi@example.com', 2027001880)]
Index 16: [('Himalaya Dua', 'Himalaya.Dua@example.com', 4017076411)]

('Eluri@example.com', 1237542427)
('Swathi@example.com', 67790305)

(None, None)