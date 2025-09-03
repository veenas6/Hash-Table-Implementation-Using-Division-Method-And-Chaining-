class HashTable:
    
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with value {value} at index {index}")
                return
        self.table[index].append([key, value])
        print(f"Inserted key {key} with value {value} at index {index}")

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Found key {key} with value {pair[1]} at index {index}")
                return pair[1]
        print(f"Key {key} not found")
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                print(f"Deleted key {key} from index {index}")
                return True
        print(f"Key {key} not found, cannot delete")
        return False

    def display(self):
        print("Hash Table:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

ht = HashTable()

ht.insert(10, "Apple")
ht.insert(20, "Banana")
ht.insert(15, "Cherry")
ht.insert(25, "Date")

ht.display()

ht.search(15)    
ht.search(100) 

ht.delete(20)   
ht.delete(100)  

ht.display()
