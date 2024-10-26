import random

class UniversalHash:
    def __init__(self, size):
        self.size = size
        self.a = random.randint(1, size - 1)
        self.b = random.randint(0, size - 1)

    def hash(self, key):
        #print(f"a: {self.a}")
        #print(f"b: {self.b}")
        return ((self.a * hash(key) + self.b) % self.size)

class UMAC:
    def __init__(self, key):
        self.key = key

    def generate_mac(self, message):
        # Simple UMAC-like function (not secure, just for demonstration purposes)
        h = (hash(message) + hash(self.key)) % (2**32)
        return h

class ChainedHashTable:
    def __init__(self, initial_size=10, mac_key=None):
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
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.hash_func = UniversalHash(self.size)
        for chain in old_table:
            for key, value, mac in chain:
                index = self.hash_func.hash(key)
                self.table[index].append((key, value, mac))

# Sample test for the hash table implementation with MACs
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

mac_key = "my_secret_key"
hash_table = ChainedHashTable(initial_size=10, mac_key=mac_key)
for name, email in people:
    hash_table.set(name, email)

# Display the contents of the hash table
hash_table.display()

# Testing retrieval of existing and non-existing keys
print(hash_table.get("Kaustubha Eluri")) 
print(hash_table.get("Swathi Arasu"))  

# Test retrieval of a non-existing key
print(hash_table.get("John"))  # Should return (None, None)




[[], [], [], [], [], [], [], [], [], []]
Load factor threshold: 0.0
Index calculated: 5
[[], [], [], [], [], [('Swathi Arasu', 'Swathi.Arasu@example.com', 1218340602)], [], [], [], []]
Load factor threshold: 0.1
Index calculated: 1
[[], [('Akram Bayat', 'Akram.Bayat@example.com', 2479594996)], [], [], [], [('Swathi Arasu', 'Swathi.Arasu@example.com', 1218340602)], [], [], [], []]
Load factor threshold: 0.2
Index calculated: 9
[[], [('Akram Bayat', 'Akram.Bayat@example.com', 2479594996)], [], [], [], [('Swathi Arasu', 'Swathi.Arasu@example.com', 1218340602)], [], [], [], [('Mengfei Cai', 'Mengfei.Cai@example.com', 2666109712)]]
Load factor threshold: 0.3
Index calculated: 3
[[], [('Akram Bayat', 'Akram.Bayat@example.com', 2479594996)], [], [('Shreya Chavan', 'Shreya.Chavan@example.com', 3269199966)], [], [('Swathi Arasu', 'Swathi.Arasu@example.com', 1218340602)], [], [], [], [('Mengfei Cai', 'Mengfei.Cai@example.com', 2666109712)]]
Load factor threshold: 0.4
Index calculated: 7
[[], [('Akram Bayat', 'Akram.Bayat@example.com', 2479594996)], [], [('Shreya Chavan', 'Shreya.Chavan@example.com', 3269199966)], [], [('Swathi Arasu', 'Swathi.Arasu@example.com', 1218340602)], [], [('Mengxiao Du', 'Mengxiao.Du@example.com', 2086792577)], [], [('Mengfei Cai', 'Mengfei.Cai@example.com', 2666109712)]]
Load factor threshold: 0.5
Index calculated: 5
[[], [('Akram Bayat', 'Akram.Bayat@example.com', 2479594996)], [], [('Shreya Chavan', 'Shreya.Chavan@example.com', 3269199966)], [], [('Swathi Arasu', 'Swathi.Arasu@example.com', 1218340602), ('Himalaya Dua', 'Himalaya.Dua@example.com', 2883400276)], [], [('Mengxiao Du', 'Mengxiao.Du@example.com', 2086792577)], [], [('Mengfei Cai', 'Mengfei.Cai@example.com', 2666109712)]]
Load factor threshold: 0.6
Index calculated: 5
[[], [('Akram Bayat', 'Akram.Bayat@example.com', 2479594996)], [], [('Shreya Chavan', 'Shreya.Chavan@example.com', 3269199966)], [], [('Swathi Arasu', 'Swathi.Arasu@example.com', 1218340602), ('Himalaya Dua', 'Himalaya.Dua@example.com', 2883400276), ('Kaustubha Eluri', 'Kaustubha.Eluri@example.com', 1714956961)], [], [('Mengxiao Du', 'Mengxiao.Du@example.com', 2086792577)], [], [('Mengfei Cai', 'Mengfei.Cai@example.com', 2666109712)]]
Load factor threshold: 0.7
Index calculated: 1
[[], [('Akram Bayat', 'Akram.Bayat@example.com', 2479594996), ('Yonghua Fu', 'Yonghua.Fu@example.com', 1916513743)], [], [('Shreya Chavan', 'Shreya.Chavan@example.com', 3269199966)], [], [('Swathi Arasu', 'Swathi.Arasu@example.com', 1218340602), ('Himalaya Dua', 'Himalaya.Dua@example.com', 2883400276), ('Kaustubha Eluri', 'Kaustubha.Eluri@example.com', 1714956961)], [], [('Mengxiao Du', 'Mengxiao.Du@example.com', 2086792577)], [], [('Mengfei Cai', 'Mengfei.Cai@example.com', 2666109712)]]
Load factor threshold: 0.8
resized..
Index calculated: 8
[[], [], [], [], [], [], [('Mengfei Cai', 'Mengfei.Cai@example.com', 2666109712)], [], [('Shreya Chavan', 'Shreya.Chavan@example.com', 3269199966), ('Siyi Gao', 'Siyi.Gao@example.com', 1077736283)], [], [('Mengxiao Du', 'Mengxiao.Du@example.com', 2086792577)], [], [('Akram Bayat', 'Akram.Bayat@example.com', 2479594996), ('Yonghua Fu', 'Yonghua.Fu@example.com', 1916513743)], [], [('Swathi Arasu', 'Swathi.Arasu@example.com', 1218340602), ('Himalaya Dua', 'Himalaya.Dua@example.com', 2883400276), ('Kaustubha Eluri', 'Kaustubha.Eluri@example.com', 1714956961)], [], [], [], [], []]
Load factor threshold: 0.45
Index calculated: 6



Index 0: []
Index 1: []
Index 2: []
Index 3: []
Index 4: []
Index 5: []
Index 6: [('Mengfei Cai', 'Mengfei.Cai@example.com', 2666109712), ('Alwin Jacob', 'Alwin.Jacob@example.com', 1552445188)]
Index 7: []
Index 8: [('Shreya Chavan', 'Shreya.Chavan@example.com', 3269199966), ('Siyi Gao', 'Siyi.Gao@example.com', 1077736283)]
Index 9: []
Index 10: [('Mengxiao Du', 'Mengxiao.Du@example.com', 2086792577)]
Index 11: []
Index 12: [('Akram Bayat', 'Akram.Bayat@example.com', 2479594996), ('Yonghua Fu', 'Yonghua.Fu@example.com', 1916513743)]
Index 13: []
Index 14: [('Swathi Arasu', 'Swathi.Arasu@example.com', 1218340602), ('Himalaya Dua', 'Himalaya.Dua@example.com', 2883400276), ('Kaustubha Eluri', 'Kaustubha.Eluri@example.com', 1714956961)]
Index 15: []
Index 16: []
Index 17: []
Index 18: []
Index 19: []

('Kaustubha.Eluri@example.com', 1714956961)
('Swathi.Arasu@example.com', 1218340602)
(None, None)

