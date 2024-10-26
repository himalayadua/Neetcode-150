import random

class UniversalHash:
    def __init__(self, size):
        self.size = size
        self.a = random.randint(1, size - 1)
        self.b = random.randint(0, size - 1)

    def hash(self, key):
        return ((self.a * hash(key) + self.b) % self.size)

class UMAC:
    def __init__(self, key):
        self.key = key

    def generate_mac(self, message):
        # Simple UMAC-like function (not secure, just for demonstration purposes)
        h = (hash(message) + hash(self.key)) % (2**32)
        return h

class ChainedHashTable:
    def __init__(self, initial_size=17, mac_key=None):  # Use a prime number for initial size
        self.size = initial_size
        self.table = [[] for _ in range(self.size)]
        self.hash_func = UniversalHash(self.size)
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
        self.hash_func = UniversalHash(self.size)
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
Index calculated: 13
[[], [], [], [], [], [], [], [], [], [], [], [], [], [('Swathi', 'Swathi@example.com', 2425990779)], [], [], []]
Load factor threshold: 0.058823529411764705
Index calculated: 11
[[], [], [], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 4048731513)], [], [('Swathi', 'Swathi@example.com', 2425990779)], [], [], []]
Load factor threshold: 0.11764705882352941
Index calculated: 0
[[('Cai', 'Cai@example.com', 1008965841)], [], [], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 4048731513)], [], [('Swathi', 'Swathi@example.com', 2425990779)], [], [], []]
Load factor threshold: 0.17647058823529413
Index calculated: 0
[[('Cai', 'Cai@example.com', 1008965841), ('Shreya', 'Shreya@example.com', 1100312892)], [], [], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 4048731513)], [], [('Swathi', 'Swathi@example.com', 2425990779)], [], [], []]
Load factor threshold: 0.23529411764705882
Index calculated: 12
[[('Cai', 'Cai@example.com', 1008965841), ('Shreya', 'Shreya@example.com', 1100312892)], [], [], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 4048731513)], [('Mengxiao', 'Mengxiao@example.com', 804645939)], [('Swathi', 'Swathi@example.com', 2425990779)], [], [], []]
Load factor threshold: 0.29411764705882354
Index calculated: 14
[[('Cai', 'Cai@example.com', 1008965841), ('Shreya', 'Shreya@example.com', 1100312892)], [], [], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 4048731513)], [('Mengxiao', 'Mengxiao@example.com', 804645939)], [('Swathi', 'Swathi@example.com', 2425990779)], [('Himalaya Dua', 'Himalaya.Dua@example.com', 1228992528)], [], []]
Load factor threshold: 0.35294117647058826
Index calculated: 1
[[('Cai', 'Cai@example.com', 1008965841), ('Shreya', 'Shreya@example.com', 1100312892)], [('Eluri', 'Eluri@example.com', 953962961)], [], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 4048731513)], [('Mengxiao', 'Mengxiao@example.com', 804645939)], [('Swathi', 'Swathi@example.com', 2425990779)], [('Himalaya Dua', 'Himalaya.Dua@example.com', 1228992528)], [], []]
Load factor threshold: 0.4117647058823529
Index calculated: 2
[[('Cai', 'Cai@example.com', 1008965841), ('Shreya', 'Shreya@example.com', 1100312892)], [('Eluri', 'Eluri@example.com', 953962961)], [('Fu', 'Fu@example.com', 2006358976)], [], [], [], [], [], [], [], [], [('Akram', 'Akram@example.com', 4048731513)], [('Mengxiao', 'Mengxiao@example.com', 804645939)], [('Swathi', 'Swathi@example.com', 2425990779)], [('Himalaya Dua', 'Himalaya.Dua@example.com', 1228992528)], [], []]
Load factor threshold: 0.47058823529411764
Index calculated: 9
[[('Cai', 'Cai@example.com', 1008965841), ('Shreya', 'Shreya@example.com', 1100312892)], [('Eluri', 'Eluri@example.com', 953962961)], [('Fu', 'Fu@example.com', 2006358976)], [], [], [], [], [], [], [('Siyi', 'Siyi@example.com', 3078597532)], [], [('Akram', 'Akram@example.com', 4048731513)], [('Mengxiao', 'Mengxiao@example.com', 804645939)], [('Swathi', 'Swathi@example.com', 2425990779)], [('Himalaya Dua', 'Himalaya.Dua@example.com', 1228992528)], [], []]
Load factor threshold: 0.5294117647058824
Index calculated: 15
Index 0: [('Cai', 'Cai@example.com', 1008965841), ('Shreya', 'Shreya@example.com', 1100312892)]
Index 1: [('Eluri', 'Eluri@example.com', 953962961)]
Index 2: [('Fu', 'Fu@example.com', 2006358976)]
Index 3: []
Index 4: []
Index 5: []
Index 6: []
Index 7: []
Index 8: []
Index 9: [('Siyi', 'Siyi@example.com', 3078597532)]
Index 10: []
Index 11: [('Akram', 'Akram@example.com', 4048731513)]
Index 12: [('Mengxiao', 'Mengxiao@example.com', 804645939)]
Index 13: [('Swathi', 'Swathi@example.com', 2425990779)]
Index 14: [('Himalaya Dua', 'Himalaya.Dua@example.com', 1228992528)]
Index 15: [('Jacob', 'Jacob@example.com', 234840909)]
Index 16: []
('Eluri@example.com', 953962961)
('Swathi@example.com', 2425990779)
(None, None)