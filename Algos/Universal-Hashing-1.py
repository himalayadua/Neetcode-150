import random

class UniversalHash:
    def __init__(self, size):
        self.size = size
        self.a = random.randint(1, size - 1)
        self.b = random.randint(0, size - 1)

    def hash(self, key):
        return ((self.a * hash(key) + self.b) % self.size)

class ChainedHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty chains
        self.hash_func = UniversalHash(size)

    def set(self, key, value):
        index = self.hash_func.hash(key)
        print(self.table)
        print(f"Index calculated: {index}")
        # Check if key exists and update
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Otherwise, append new key-value pair
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_func.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")

# Sample test for the hash table implementation
people = [
    ("Swathi Arasu", "Swathi.Arasu@example.com"),
    ("Akram Bayat", "Akram.Bayat@example.com"),
    ("Mengfei Cai", "Mengfei.Cai@example.com"),
    ("Shreya Chavan", "Shreya.Chavan@example.com"),
    ("Mengxiao Du", "Mengxiao.Du@example.com"),
    ("Himalaya Dua", "Himalaya.Dua@example.com"),
    ("Kaustubha Eluri", "Kaustubha.Eluri@example.com"),
    ("Yonghua Fu", "Yonghua.Fu@example.com"),
    ("Siyi Gao", "Siyi.Gao@example.com"),
    ("Alwin Jacob", "Alwin.Jacob@example.com")
]

hash_table = ChainedHashTable(size=10)
for name, email in people:
    hash_table.set(name, email)

# Display the contents of the hash table
hash_table.display()

# Testing retrieval of existing and non-existing keys
print(hash_table.get("Kaustubha Eluri"))  # Should return "alice@example.com"
print(hash_table.get("Swathi Arasu"))   # Should return None (not found)

# Test retrieval of a non-existing key
print(hash_table.get("John"))  # Should return (None, None)

[[], [], [], [], [], [], [], [], [], []]
Index calculated: 9
[[], [], [], [], [], [], [], [], [], [('Swathi Arasu', 'Swathi.Arasu@example.com')]]
Index calculated: 7
[[], [], [], [], [], [], [], [('Akram Bayat', 'Akram.Bayat@example.com')], [], [('Swathi Arasu', 'Swathi.Arasu@example.com')]]
Index calculated: 9
[[], [], [], [], [], [], [], [('Akram Bayat', 'Akram.Bayat@example.com')], [], [('Swathi Arasu', 'Swathi.Arasu@example.com'), ('Mengfei Cai', 'Mengfei.Cai@example.com')]]
Index calculated: 1
[[], [('Shreya Chavan', 'Shreya.Chavan@example.com')], [], [], [], [], [], [('Akram Bayat', 'Akram.Bayat@example.com')], [], [('Swathi Arasu', 'Swathi.Arasu@example.com'), ('Mengfei Cai', 'Mengfei.Cai@example.com')]]
Index calculated: 9
[[], [('Shreya Chavan', 'Shreya.Chavan@example.com')], [], [], [], [], [], [('Akram Bayat', 'Akram.Bayat@example.com')], [], [('Swathi Arasu', 'Swathi.Arasu@example.com'), ('Mengfei Cai', 'Mengfei.Cai@example.com'), ('Mengxiao Du', 'Mengxiao.Du@example.com')]]
Index calculated: 0
[[('Himalaya Dua', 'Himalaya.Dua@example.com')], [('Shreya Chavan', 'Shreya.Chavan@example.com')], [], [], [], [], [], [('Akram Bayat', 'Akram.Bayat@example.com')], [], [('Swathi Arasu', 'Swathi.Arasu@example.com'), ('Mengfei Cai', 'Mengfei.Cai@example.com'), ('Mengxiao Du', 'Mengxiao.Du@example.com')]]
Index calculated: 8
[[('Himalaya Dua', 'Himalaya.Dua@example.com')], [('Shreya Chavan', 'Shreya.Chavan@example.com')], [], [], [], [], [], [('Akram Bayat', 'Akram.Bayat@example.com')], [('Kaustubha Eluri', 'Kaustubha.Eluri@example.com')], [('Swathi Arasu', 'Swathi.Arasu@example.com'), ('Mengfei Cai', 'Mengfei.Cai@example.com'), ('Mengxiao Du', 'Mengxiao.Du@example.com')]]
Index calculated: 7
[[('Himalaya Dua', 'Himalaya.Dua@example.com')], [('Shreya Chavan', 'Shreya.Chavan@example.com')], [], [], [], [], [], [('Akram Bayat', 'Akram.Bayat@example.com'), ('Yonghua Fu', 'Yonghua.Fu@example.com')], [('Kaustubha Eluri', 'Kaustubha.Eluri@example.com')], [('Swathi Arasu', 'Swathi.Arasu@example.com'), ('Mengfei Cai', 'Mengfei.Cai@example.com'), ('Mengxiao Du', 'Mengxiao.Du@example.com')]]
Index calculated: 4
[[('Himalaya Dua', 'Himalaya.Dua@example.com')], [('Shreya Chavan', 'Shreya.Chavan@example.com')], [], [], [('Siyi Gao', 'Siyi.Gao@example.com')], [], [], [('Akram Bayat', 'Akram.Bayat@example.com'), ('Yonghua Fu', 'Yonghua.Fu@example.com')], [('Kaustubha Eluri', 'Kaustubha.Eluri@example.com')], [('Swathi Arasu', 'Swathi.Arasu@example.com'), ('Mengfei Cai', 'Mengfei.Cai@example.com'), ('Mengxiao Du', 'Mengxiao.Du@example.com')]]
Index calculated: 1


Index 0: [('Himalaya Dua', 'Himalaya.Dua@example.com')]
Index 1: [('Shreya Chavan', 'Shreya.Chavan@example.com'), ('Alwin Jacob', 'Alwin.Jacob@example.com')]
Index 2: []
Index 3: []
Index 4: [('Siyi Gao', 'Siyi.Gao@example.com')]
Index 5: []
Index 6: []
Index 7: [('Akram Bayat', 'Akram.Bayat@example.com'), ('Yonghua Fu', 'Yonghua.Fu@example.com')]
Index 8: [('Kaustubha Eluri', 'Kaustubha.Eluri@example.com')]
Index 9: [('Swathi Arasu', 'Swathi.Arasu@example.com'), ('Mengfei Cai', 'Mengfei.Cai@example.com'), ('Mengxiao Du', 'Mengxiao.Du@example.com')]


Kaustubha.Eluri@example.com
Swathi.Arasu@example.com

None
