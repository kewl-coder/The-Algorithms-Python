class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    def search(self, key):
        index = self.hash_function(key)
        return self.table[index]

my_hash_table = HashTable(10)
my_hash_table.insert("name", "John")
my_hash_table.insert("age", 30)

search_key = "name"
result = my_hash_table.search(search_key)

if result:
    print(f"{search_key}: {result}")
else:
    print(f"{search_key} not found.")
